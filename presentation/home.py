from base import chat
from ampalibe import Payload
from ampalibe import Filetype
from ampalibe.ui import QuickReply, Button

from conf import Configuration as config
from ampalibe import async_simulate as simulate

from presentation.textes import HomeText

homeText = HomeText()

class Home:
    def __persistant_menu(self, sender_id, *ext):
        return chat.persistent_menu(
            sender_id,
            [
                Button(
                    title="Stands",
                    payload=Payload("/stands"), 
                    image_url="https://img.icons8.com/external-flaticons-lineal-color-flat-icons/64/external-stand-geek-culture-flaticons-lineal-color-flat-icons.png"
                ),
                Button(
                    title="Fiche metiers",
                    payload=Payload("/fiche_metiers"),
                    image_url="https://img.icons8.com/officel/80/business.png"
                ),
                Button(
                    title="Test Kavio",
                    payload=Payload("/test_kavio"),
                    image_url="https://img.icons8.com/ios/100/test-passed--v1.png"
                )   
            ]
        )
            

    async def get_started(self, sender_id, **ext):
        chat.send_text(
            sender_id,
            homeText.text
        )
        chat.send_file(
            sender_id,
            "assets/private/zavoka-logo.png",
            Filetype.image
        )
        self.__persistant_menu(sender_id)
        await simulate(sender_id, "/")

    async def menu(self, sender_id, cmd, **ext):
        if cmd.strip().isdigit():
            await simulate(sender_id, Payload("/stand/numero", numero=cmd))
            return
        
        extract = cmd.strip().lower().split()
        if len(extract) > 1 and extract[0] in ['stand', 'stands']:
            if extract[1].isdigit():
                await simulate(sender_id, Payload("/stand/numero", numero=extract[1]))
                return
            
        self.__persistant_menu(sender_id)
        chat.send_quick_reply( 
            sender_id,
            [
                QuickReply(
                    title="Stands",
                    payload=Payload("/stands"),
                    image_url="https://img.icons8.com/external-flaticons-lineal-color-flat-icons/64/external-stand-geek-culture-flaticons-lineal-color-flat-icons.png",
                ),
                QuickReply(
                    title="Fiche metiers",
                    payload=Payload("/fiche_metiers"),
                    image_url="https://img.icons8.com/officel/80/business.png",
                ),
                QuickReply(
                    title="Test Kavio",
                    payload=Payload("/test_kavio"),
                    image_url="https://img.icons8.com/ios/100/test-passed--v1.png",
                )
            ],
            homeText.menu
        )