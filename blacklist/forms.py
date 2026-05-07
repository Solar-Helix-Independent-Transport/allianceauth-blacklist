from django import forms


class EveNoteForm(forms.Form):
    reason = forms.CharField(
        label='Reason',
        widget=forms.Textarea()
    )
    blacklisted = forms.BooleanField(
        label='Blacklist',
        required=False,
        widget=forms.CheckboxInput()
    )
    restricted = forms.BooleanField(
        label='Restricted',
        required=False,
        widget=forms.CheckboxInput()
    )
    ultra_restricted = forms.BooleanField(
        label='Ultra Restricted',
        required=False,
        widget=forms.CheckboxInput()
    )
    all_linked_chars = forms.BooleanField(
        label='Add note on ALL known Linked Characters. (Characters only)',
        required=False,
        widget=forms.CheckboxInput()
    )


class AddComment(forms.Form):
    comment = forms.CharField(
        label='Comment',
        widget=forms.Textarea()
    )
    restricted = forms.BooleanField(
        label='Restricted',
        required=False,
        widget=forms.CheckboxInput()
    )
    ultra_restricted = forms.BooleanField(
        label='Ultra Restricted',
        required=False,
        widget=forms.CheckboxInput()
    )
