import ampalibe
from presentation.stands import Stands

stands = Stands()

@ampalibe.command('/stands')
def stands_(sender_id, **ext):
    return stands.menu(sender_id, **ext)


@ampalibe.command('/stands/list')
def list_stands(sender_id, **ext):
    return stands.list_stands(sender_id, **ext)


@ampalibe.command('/stands/search')
def search_stands(sender_id, **ext):
    return stands.search_stands(sender_id, **ext)


@ampalibe.action('/stands/search')
def search_stands_action(sender_id, cmd, **ext):
    return stands.search_stands(sender_id, keyword=cmd, **ext)


@ampalibe.command('/stand')
def stand(sender_id, _id, **ext):
    return stands.stand(sender_id, _id, **ext)

@ampalibe.command('/stand/numero')
async def stand_numero(sender_id, numero, **ext):
    return await stands.numero(sender_id, numero, **ext)


@ampalibe.command('/stand/contact')
def stand_contact(sender_id, _id, **ext):
    return stands.contact(sender_id, _id, **ext)


@ampalibe.command('/stand/gallery')
def stand_gallery(sender_id, _id, **ext):
    return stands.gallery(sender_id, _id, **ext)


@ampalibe.command('/stand/asset')
def stand_asset(sender_id, entity, url, filetype, **ext):
    return stands.asset(sender_id, entity, url, filetype, **ext)


@ampalibe.command('/stand/document')
def stand_asset_download(sender_id, _id, **ext):
    return stands.document(sender_id, _id, **ext)