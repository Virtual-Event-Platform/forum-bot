from base import chat, query
from ampalibe import Payload
from ampalibe.ui import QuickReply
from domains.entity.stat import Stat
from presentation.textes import StandsText
from ampalibe import async_simulate as simulate
from presentation.response import BackAndMenuButton
from base import standUseCase, assetUseCase, statUsecase

standsText = StandsText()

class Stands:
    def menu(self, sender_id, **ext):
        chat.send_quick_reply(
            sender_id,
            [
                QuickReply(
                    title="Liste des stands",
                    payload=Payload("/stands/list"),
                    image_url="https://img.icons8.com/nolan/64/list.png"
                ),
                QuickReply(
                    title="Recherche",
                    payload=Payload("/stands/search"),
                    image_url="https://img.icons8.com/nolan/64/search.png"
                )
            ],
            standsText.menu
        )
    

    def _stands(self, sender_id, stands, minim, search=False):
        if len(stands) == 0:
            chat.send_text(sender_id, standsText.no_stands)
            return BackAndMenuButton(
                title="Autre recherche" if search else "Retour",
                payload=Payload("/stands/search" if search else "/stands"),
            )
        if minim:
            chat.send_quick_reply(
                sender_id,
                stands,
                standsText.list_stands,
                next='Suivant',
            )
        else:
            chat.send_generic_template(
                sender_id, 
                stands,
                None if minim else 
                [
                    QuickReply(
                        title="Facebook Lite ?",
                        payload=Payload("/stands/list", minim=True),
                        image_url="https://img.icons8.com/nolan/64/facebook.png"
                    )
                ] + 
                ( [ QuickReply(
                        title="Autre recherche",
                        payload=Payload("/stands/search"),
                        image_url="https://img.icons8.com/nolan/64/search.png"
                    ) 
                ]  if search else [] ),
                next='Suivant'
            )


    def list_stands(self, sender_id, minim=False, **ext):
        self._stands(sender_id, standUseCase.get(minimal=minim), minim)
        
        
    def search_stands(self, sender_id, keyword=None, minim=False, **ext):
        if not keyword:
            chat.send_text(sender_id, standsText.search_stands)
            query.set_action(sender_id, "/stands/search")
            return
        query.set_action(sender_id, None)
        self._stands(sender_id, standUseCase.get(keyword=keyword, minimal=minim), minim, search=True)


    def stand(self, sender_id, _id, **ext):
        stand = standUseCase.get_one(_id=_id)

        if stand:
            chat.send_button(sender_id, stand.buttons, stand.information)
            statUsecase.set(Stat(sender_id, entity=_id))
        else:
            chat.send_text(sender_id, standsText.no_stand)


    def contact(self, sender_id, _id, **ext):
        contact = standUseCase.get_contact(_id=_id)
        if contact:
            chat.send_text(sender_id, contact)
        else:
            chat.send_text(sender_id, standsText.no_contact)
        return BackAndMenuButton(
            Payload("/stand", _id=_id),
        )
    

    def gallery(self, sender_id, _id, minim=False, **ext):
        images = assetUseCase.get(_id=_id, _type="image", minim=minim)
        if len(images) == 0:
            chat.send_text(sender_id, standsText.no_images)
            return BackAndMenuButton(
            Payload("/stand", _id=_id),
        )
        
        if minim:
            chat.send_quick_reply(
                sender_id,
                images,
                standsText.gallery,
                next='Suivant',
            )
        else:
            chat.send_generic_template(
                sender_id,
                images,
                None if minim else [
                    QuickReply(
                        title="Facebook Lite ?",
                        payload=Payload("/stand/gallery", _id=_id, minim=True),
                        image_url="https://img.icons8.com/nolan/64/facebook.png"
                    ),
                    QuickReply(
                        title="Retour",
                        payload=Payload("/stand", _id=_id),
                        image_url="https://img.icons8.com/nolan/64/return.png"
                    )
                ],
                next='Suivant'
            )
            


    def asset(self, sender_id, entity, url, filetype, **ext):
        chat.send_file_url(sender_id, url, filetype=filetype)
        _id = url.split('/')[-2]
        print(_id)
        statUsecase.set(Stat(sender_id, asset=_id))
        return BackAndMenuButton(
            Payload("/stand/" + ("gallery" if filetype == "image" else "document") , _id=entity),
        )


    def document(self, sender_id, _id, minim=False, **ext):
        documents = assetUseCase.get(_id=_id, _type='document', minim=minim)
        if len(documents) == 0:
            chat.send_text(sender_id, standsText.no_documents)
            return BackAndMenuButton(
                Payload("/stand", _id=_id),
            )

        if minim:
            chat.send_quick_reply(
                sender_id,
                documents,
                standsText.documents,
                next='Suivant',
            )
        else:
            chat.send_generic_template(
                sender_id,
                documents,
                None if minim else [
                    QuickReply(
                        title="Facebook Lite ?",
                        payload=Payload("/stand/document", _id=_id, minim=True),
                        image_url="https://img.icons8.com/nolan/64/facebook.png"
                    ),
                    QuickReply(
                        title="Retour",
                        payload=Payload("/stand", _id=_id),
                        image_url="https://img.icons8.com/nolan/64/return.png"
                    )
                ],
                next='Suivant'
            )

        
    async def numero(self, sender_id, numero, **ext):
        stand = standUseCase.get_one(numero=numero)
        if stand:
            chat.send_button(sender_id, stand.buttons, stand.information)
            statUsecase.set(Stat(sender_id, entity=stand._id))
        else:
            await simulate(sender_id, "/")

    
        
    
        
        