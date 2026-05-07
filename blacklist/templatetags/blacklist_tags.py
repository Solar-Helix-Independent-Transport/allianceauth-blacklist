from django.template.defaulttags import register
from django.utils.safestring import mark_safe


@register.simple_tag()
def eve_logo(id, name, cat, size):
    if cat == "character":
        return mark_safe(
            f'<img class="img-circle" src="https://images.evetech.net/characters/{id}/portrait?size={size}" style="height: {size}px; width: {size}px !important;" title="{name}">'
        )

    elif cat == "corporation":
        return mark_safe(
            f'<img class="img-circle" src="https://images.evetech.net/corporations/{id}/logo?size={size}" style="height: {size}px; width: {size}px !important;" title="{name}">'
        )

    elif cat == "alliance":
        return mark_safe(
            f'<img class="img-circle" src="https://images.evetech.net/alliances/{id}/logo?size={size}" style="height: {size}px; width: {size}px !important;" title="{name}">'
        )

    else:
        return ""
