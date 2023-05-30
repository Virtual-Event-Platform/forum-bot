import ampalibe
from presentation.stands import Stands


@ampalibe.command('/stands')
def stands(sender_id, **ext):
    Stands().menu(sender_id, **ext)


@ampalibe.command('/stands/list')
def list_stands(sender_id, **ext):
    Stands().list_stands(sender_id, **ext)


@ampalibe.command('/stands/search')
def search_stands(sender_id, **ext):
    Stands().search_stands(sender_id, **ext)


@ampalibe.action('/stands/search')
def search_stands_action(sender_id, cmd, **ext):
    return Stands().search_stands(sender_id, keyword=cmd, **ext)


@ampalibe.command('/stand')
def stand(sender_id, _id, **ext):
    return Stands().stand(sender_id, _id, **ext)

@ampalibe.command('/stand/numero')
async def stand_numero(sender_id, numero, **ext):
    return await Stands().numero(sender_id, numero, **ext)


@ampalibe.command('/stand/contact')
def stand_contact(sender_id, _id, **ext):
    return Stands().contact(sender_id, _id, **ext)


@ampalibe.command('/stand/gallery')
def stand_gallery(sender_id, _id, **ext):
    return Stands().gallery(sender_id, _id, **ext)


@ampalibe.command('/stand/asset')
def stand_asset(sender_id, entity, url, filetype, **ext):
    return Stands().asset(sender_id, entity, url, filetype, **ext)


@ampalibe.command('/stand/document')
def stand_asset_download(sender_id, _id, **ext):
    return Stands().document(sender_id, _id, **ext)