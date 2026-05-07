from django.template.defaulttags import register
from django.utils.safestring import mark_safe


@register.simple_tag()
def eve_logo(id, name, cat, size):
    if cat == "character":
        return mark_safe(
            f'<img class="img-circle" src="https://images.evetech.net/characters/{id}/portrait?size={size}" style="min-height: {size}px; min-width: {size}px;max-height: {size}px; max-width: {size}px;" title="{name}">'
        )

    elif cat == "corporation":
        return mark_safe(
            f'<img class="img-circle" src="https://images.evetech.net/corporations/{id}/logo?size={size}" style="min-height: {size}px; min-width: {size}px;max-height: {size}px; max-width: {size}px;" title="{name}">'
        )

    elif cat == "alliance":
        return mark_safe(
            f'<img class="img-circle" src="https://images.evetech.net/alliances/{id}/logo?size={size}" style="min-height: {size}px; min-width: {size}px;max-height: {size}px; max-width: {size}px;" title="{name}">'
        )

    else:
        return ""
