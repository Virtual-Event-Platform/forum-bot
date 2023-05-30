import ampalibe
from presentation.fiche_metiers import FicheMetier


@ampalibe.command('/fiche_metiers')
def fiche_metiers(sender_id, **ext):
    return FicheMetier().menu(sender_id, **ext)


@ampalibe.command('/fiche_metiers/all')
def fiche_metier_all(sender_id, **ext):
    return FicheMetier().list_fiche_metiers(sender_id, **ext)


@ampalibe.command('/fiche_metier/asset')
def fiche_metier_asset(sender_id, **ext):
    return FicheMetier().asset(sender_id, **ext)


@ampalibe.command('/fiche_metiers/search')
def fiche_metier_search(sender_id, **ext):
    return FicheMetier().search_fiche_metiers(sender_id, **ext)


@ampalibe.action('/fiche_metiers/search')
def fiche_metier_search_act(sender_id, cmd, **ext):
    return FicheMetier().search_fiche_metiers(sender_id, keyword=cmd,**ext)


@ampalibe.command('/fiche_metiers/domain')
def fiche_metier_domain(sender_id, **ext):
    return FicheMetier().list_by_domain(sender_id, **ext)
