from ampalibe import Payload
from ampalibe.ui import QuickReply, Button, Element


class FicheMetier:
    def __init__(self, _id, name, url, domain, **kwargs):
        self._id = _id 
        self.name = name 
        self.url = url 
        self.domain = domain


    def toQuickReply(self):
        return QuickReply(
            title=self.name,
            payload=Payload(f"/fiche_metier/asset", url=self.url),
            image_url=self.url + "?thumb=100x300"
        )
    

    def toElement(self):
        return Element(
            title=self.name,
            image_url=self.url,
            buttons=[
                Button(
                    title="Voir",
                    payload=Payload(f"/fiche_metier/asset", url=self.url)
                )
            ])