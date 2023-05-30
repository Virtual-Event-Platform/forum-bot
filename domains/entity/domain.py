from ampalibe import Payload
from ampalibe.ui import QuickReply

class Domain:
    def __init__(self, _id, name, icon, **kwargs):
        self._id =_id 
        self.name = name
        self.icon = icon

    def toQuickReply(self):
        return QuickReply(
            title=self.name,
            payload=Payload("/fiche_metiers/domain", domain=self._id),
            image_url=self.icon
        )