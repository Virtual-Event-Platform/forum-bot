import ampalibe
from presentation import Home
from . import stands, fiche_metiers, test_kavio


@ampalibe.command('/get_started')
async def get_started(sender_id, **ext):
    await Home().get_started(sender_id, **ext)


@ampalibe.command('/')
async def home(sender_id, **ext):
    await Home().menu(sender_id, **ext)





