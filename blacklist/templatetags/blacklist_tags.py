from django.utils.safestring import mark_safe
from django.template.defaulttags import register


@register.simple_tag()
def eve_logo(id, name, cat, size):
    if cat == "character":
        return mark_safe("<img class=\"img-circle\" src=\"https://images.evetech.net/characters/{}/portrait?size={}\" style=\"height: {}px; width: {}px;\" title=\"{}\">".format(id, size, size, size, name))

    elif cat == "corporation":
        return mark_safe("<img class=\"img-circle\" src=\"https://images.evetech.net/corporations/{}/logo?size={}\" style=\"height: {}px; width: {}px;\" title=\"{}\">".format(id, size, size, size, name))

    elif cat == "alliance":
        return mark_safe("<img class=\"img-circle\" src=\"https://images.evetech.net/alliances/{}/logo?size={}\" style=\"height: {}px; width: {}px;\" title=\"{}\">".format(id, size, size, size, name))

    else:
        return ""
