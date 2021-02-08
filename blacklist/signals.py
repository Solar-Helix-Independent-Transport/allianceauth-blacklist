from django.db.models.signals import post_save
from django.dispatch import receiver
from allianceauth.authentication.models import State
from allianceauth.eveonline.models import EveCharacter, EveAllianceInfo, EveCorporationInfo
from . import models

# signals go here

import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=models.EveNote)
def process_eve_note(sender, instance: models.EveNote, *args, **kwargs):
    blk_state = State.objects.get(name="Blacklist")

    if instance.eve_catagory == "character":
        eve_char = EveCharacter.objects.get_character_by_id(instance.eve_id)
        blacklist = instance.blacklisted
        exists = blk_state.member_characters.filter(character_id=instance.eve_id).exists()
        if blacklist and exists:
            pass
        elif blacklist and not exists:
            if eve_char is None:
                eve_char = EveCharacter.objects.create_character(instance.eve_id)
            blk_state.member_characters.add(eve_char)
        elif not blacklist and exists:
            blk_state.member_characters.remove(eve_char)

    if instance.eve_catagory == "corporation":
        eve_corp = EveCorporationInfo.objects.filter(corporation_id=instance.eve_id)
        blacklist = instance.blacklisted
        exists = blk_state.member_corporations.filter(corporation_id=instance.eve_id).exists()
        if blacklist and exists:
            pass
        elif blacklist and not exists:
            if eve_corp.exists() is False:
                eve_corp = EveCorporationInfo.objects.create_corporation(instance.eve_id)
            else:
                eve_corp = eve_corp.first()
            blk_state.member_corporations.add(eve_corp)
        elif not blacklist and exists:
            blk_state.member_corporations.remove(eve_corp.first())

    if instance.eve_catagory == "alliance":
        eve_alli = EveAllianceInfo.objects.filter(alliance_id=instance.eve_id)
        blacklist = instance.blacklisted
        exists = blk_state.member_alliances.filter(alliance_id=instance.eve_id).exists()
        if blacklist and exists:
            pass
        elif blacklist and not exists:
            if eve_alli.exists() is False:
                eve_alli = EveAllianceInfo.objects.create_alliance(instance.eve_id)
            else:
                eve_alli = eve_alli.first()
            blk_state.member_alliances.add(eve_alli)
        elif not blacklist and exists:
            blk_state.member_alliances.remove(eve_alli.first())
