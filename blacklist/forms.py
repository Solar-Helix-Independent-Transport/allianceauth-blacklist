from django import forms


class EveNoteForm(forms.Form):
    reason = forms.CharField(label='Reason', widget=forms.Textarea)
    blacklisted = forms.BooleanField(label='Blacklist', required=False)
    restricted = forms.BooleanField(label='Restricted', required=False)


class AddComment(forms.Form):
    comment = forms.CharField(label='Comment', widget=forms.Textarea)
    restricted = forms.BooleanField(label='Restricted', required=False)

