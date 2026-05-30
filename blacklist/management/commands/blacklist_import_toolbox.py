from django.core.management.base import BaseCommand
from django.db.models.signals import post_save

from blacklist.models import EveNote, EveNoteComment
from blacklist.signals import process_eve_note


class Command(BaseCommand):
    help = 'Import EveNote (Pilot Log) entries from allianceauth-toolbox into blacklist.'

    def handle(self, *args, **options):
        try:
            from toolbox.models import EveNote as ToolboxNote
        except ImportError:
            self.stderr.write(
                "Could not import toolbox models — is allianceauth-toolbox installed?")
            return

        toolbox_notes = ToolboxNote.objects.prefetch_related('comment').all()
        self.stdout.write(
            f"Found {toolbox_notes.count()} Pilot Log entries in toolbox.")

        post_save.disconnect(process_eve_note, sender=EveNote)

        note_field = EveNote._meta.get_field('added_at')
        comment_field = EveNoteComment._meta.get_field('comment_date')

        notes_created = 0
        notes_skipped = 0
        comments_created = 0
        comments_skipped = 0

        try:
            for src in toolbox_notes:
                exists = EveNote.objects.filter(
                    eve_id=src.eve_id,
                    eve_catagory=src.eve_catagory,
                    added_by=src.added_by,
                    reason=src.reason,
                ).exists()

                if exists:
                    notes_skipped += 1
                    self.stdout.write(
                        f"  SKIP note: {src.eve_name} (already exists)")
                    continue

                note = EveNote(
                    eve_id=src.eve_id,
                    eve_name=src.eve_name,
                    eve_catagory=src.eve_catagory,
                    blacklisted=src.blacklisted,
                    restricted=src.restricted,
                    ultra_restricted=src.ultra_restricted,
                    added_by=src.added_by,
                    reason=src.reason,
                    corporation_id=src.corporation_id,
                    corporation_name=src.corporation_name,
                    alliance_id=src.alliance_id,
                    alliance_name=src.alliance_name,
                )
                note_field.auto_now_add = False
                note.added_at = src.added_at
                note.save()
                note_field.auto_now_add = True

                notes_created += 1
                self.stdout.write(f"  IMPORT note: {src.eve_name}")

                for src_comment in src.comment.all():
                    comment_exists = EveNoteComment.objects.filter(
                        eve_note=note,
                        added_by=src_comment.added_by,
                        comment=src_comment.comment,
                    ).exists()

                    if comment_exists:
                        comments_skipped += 1
                        continue

                    new_comment = EveNoteComment(
                        eve_note=note,
                        added_by=src_comment.added_by,
                        comment=src_comment.comment,
                        restricted=src_comment.restricted,
                        ultra_restricted=src_comment.ultra_restricted,
                    )
                    comment_field.auto_now_add = False
                    new_comment.comment_date = src_comment.comment_date
                    new_comment.save()
                    comment_field.auto_now_add = True

                    comments_created += 1

        finally:
            post_save.connect(process_eve_note, sender=EveNote)
            note_field.auto_now_add = True
            comment_field.auto_now_add = True

        self.stdout.write(
            f"\nDone. Notes: {notes_created} imported, {notes_skipped} skipped. "
            f"Comments: {comments_created} imported, {comments_skipped} skipped."
            "Recommend a full sync with `python manage.py blacklist_sync` to ensure the Blacklist State is consistent."
        )
