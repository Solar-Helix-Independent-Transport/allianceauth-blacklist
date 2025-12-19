from esi.openapi_clients import ESIClientProvider

from . import __title__, __url__, __version__

esi = ESIClientProvider(
    compatibility_date="",
    ua_appname=__title__,
    ua_url=__url__,
    ua_version=__version__,
    operations=[
        "PostUniverseNames",
        "GetCharactersCharacterId",
        "GetCorporationsCorporationId",
        "GetCorporationsCorporationId",
        "GetCharactersCharacterIdSearch",
        "GetAlliancesAllianceId"
    ]
)
