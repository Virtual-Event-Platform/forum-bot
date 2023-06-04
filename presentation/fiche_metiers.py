from ampalibe import Payload
from ampalibe.ui import QuickReply
from domains.entity.stat import Stat
from presentation.textes import FicheMetiersText
from presentation.response import BackAndMenuButton
from injection import chat, query, ficheMetierUseCase, statUsecase

fichemetierText = FicheMetiersText()

class FicheMetier:
    def menu(self, sender_id, **ext):
        chat.send_quick_reply(
            sender_id,
            [
                QuickReply(
                    title="Domaines",
                    payload=Payload("/fiche_metiers/domain"),
                    image_url="https://img.icons8.com/nolan/64/sorting-answers.png"
                ),
                QuickReply(
                    title="Tous",
                    payload=Payload("/fiche_metiers/all"),
                    image_url="https://img.icons8.com/nolan/64/list.png"
                ),
                QuickReply(
                    title="Recherche",
                    payload=Payload("/fiche_metiers/search"),
                    image_url="https://img.icons8.com/nolan/64/search.png"
                )
            ],
            fichemetierText.menu
        )


    def _fiche_metiers(self, sender_id, fiches, minim, search=False):
        if len(fiches) == 0:
            chat.send_text(sender_id, fichemetierText.no_stands)
            return BackAndMenuButton(
                title="Autre recherche" if search else "Retour",
                payload=Payload("/fiche_metiers/search" if search else "/fiche_metiers"),
            )
        if minim:
            chat.send_quick_reply(
                sender_id,
                fiches,
                fichemetierText.list_stands,
                next='Suivant',
            )
        else:
            chat.send_generic_template(
                sender_id, 
                fiches,
                [
                    QuickReply(
                        title="Facebook Lite ?",
                        payload=Payload("/fiche_metiers/all", minim=True),
                        image_url="https://img.icons8.com/nolan/64/facebook.png"
                    ),
                    QuickReply(
                        title="Retour",
                        payload=Payload("/fiche_metiers"),
                        image_url="https://img.icons8.com/nolan/64/return.png"
                    )
                ] + 
                ( [ QuickReply(
                        title="Autre recherche",
                        payload=Payload("/fiche_metiers/search"),
                        image_url="https://img.icons8.com/nolan/64/search.png"
                    ) 
                ]  if search else [] ),
                next='Suivant'
            )
    

    def list_fiche_metiers(self, sender_id, keyword=None, minim=False, **ext):
        return self._fiche_metiers(sender_id, ficheMetierUseCase.get(minimal=minim), minim)


    def search_fiche_metiers(self, sender_id, keyword=None, minim=False, **ext):
        if not keyword:
            chat.send_text(sender_id, fichemetierText.search_fiche_metiers)
            query.set_action(sender_id, "/fiche_metiers/search")
            return
        query.set_action(sender_id, None)
        return self._fiche_metiers(sender_id, ficheMetierUseCase.get(minimal=minim, keyword=keyword), minim, search=True)
        
    
    def asset(self, sender_id, url, **ext):
        chat.send_file_url(sender_id, url, "image")
        _id = url.split('/')[-2]
        statUsecase.set(Stat(sender_id, fiche=_id))
        return BackAndMenuButton(
            payload=Payload("/fiche_metiers"),
        )
    

    def list_by_domain(self, sender_id, domain=None, minim=False, **ext):
        if not domain:
            chat.send_quick_reply(sender_id, ficheMetierUseCase.all_domains(), "Choisissez un domaine")
            return
        self._fiche_metiers(sender_id, ficheMetierUseCase.get(minimal=minim, domain=domain), minim)
        