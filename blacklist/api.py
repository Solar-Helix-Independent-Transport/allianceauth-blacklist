import re
from ninja import NinjaAPI
from ninja.security import django_auth

from django.conf import settings
from django.template import Template, Context
from django.template.loader import render_to_string

from allianceauth.services.hooks import get_extension_logger

logger = get_extension_logger(__name__)

from ninja import NinjaAPI, Query, Schema

from django.db.models import Q

from .models import EveNote

api = NinjaAPI(
    title="Blacklist API",
    version="0.0.1",
    auth=django_auth,
    urls_namespace='blacklist:api',
    openapi_url=settings.DEBUG and "/openapi.json" or "")


class DatatablesServerNotes(Schema):
    length: int = 100
    start: int = 0
    draw: int = 0
    search: dict = {"search[value]": ""}
    order: list = [{"0": {"column": 0}}, {"0": {"dir": "desc"}}]
# order[0][column]=3&order[0][dir]=asc
# search[value]=test

@api.get("datatables_server_notes/", tags=["Datatables"])
def datatables_server_notes(request, params: Query[DatatablesServerNotes]):
    # BEGIN ServerSide Datatables _template_
    length = int(params.length)
    start = int(params.start)
    limit = start + length
    search_string = request.GET['search[value]']  # The dict wont cast, use manual GET
    try:
        order_col = int(request.GET['order[0][column]'])  # The dict wont cast, use manual GET
    except Exception:
        order_col = 0
    order_dir = request.GET['order[0][dir]']  # The dict wont cast, use manual GET
    draw = int(params.draw)
    # END ServerSide Datatables _template_

    # defining my own
    templates = [
        "blacklist/stubs/img.html",
        "blacklist/stubs/name.html",
        "blacklist/stubs/date.html",
        "{{ note.added_by }}",
        "blacklist/stubs/reason.html",
        "{{ note.eve_catagory }}",
        "{{ note.corporation_name }}",
        "{{ note.alliance_name }}",
        "blacklist/stubs/actions.html"
    ]
    
    columns = [
        (False, ""),
        (True, "eve_name"),
        (False, "added_at"),
        (True, "added_by"),
        (True, "reason"),
        (True, "eve_catagory"),
        (True, "corporation_name"),
        (True, "alliance_name"),
        (False, "")
    ]

    filter_q = Q()
    if len(search_string) > 0:
        val = search_string
        for x in columns:
            if x[0]: 
                filter_q |= Q(**{f'{x[1]}__icontains': val})  # Apply search to all Columns


    col_id_regex = r"columns\[(?P<id>[0-9]{1,})\]\[search\]\[value\]"
    regex = re.compile(col_id_regex)
    for c in request.GET:
        _r = regex.findall(c)
        if _r:
            _c = columns[int(_r[0])]
            if _c[0]:
                if len(request.GET[c]):
                    filter_q |= Q(**{f'{_c[1]}__iregex': request.GET[c]})
    
    order=""
    _o = columns[order_col]
    if _o[0]:
        if order_dir == 'desc':
            order = '-' + _o[1]
        else:
            order = _o[1]

    items = []
    for note in EveNote.objects.filter(filter_q).order_by(order)[start:limit]:
        ctx = {"note": note}
        row = []
        for t in templates:
            if "{{" in t:
                tplt = Template(t)
                row.append(tplt.render(Context(ctx)))
            else:
                row.append(
                    render_to_string(
                        t,
                        ctx,
                        request
                    )
                )
        items.append(row)
            
    datatables_data = {}
    datatables_data['draw'] = draw
    datatables_data['recordsTotal'] = EveNote.objects.all().count()
    datatables_data['recordsFiltered'] = EveNote.objects.filter(filter_q).count()
    datatables_data['data'] = items

    return datatables_data
