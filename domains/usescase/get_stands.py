from base import singleton
from data.repositories.repository import ImplRepository


@singleton
class StandUseCase(ImplRepository):
    def __init__(self, api):
        super().__init__(api)


    def get(self, keyword=None, minimal=False):
        return [
            stand.toQuickReply() if minimal else  stand.toElement()
            for stand in self.get_stands(keyword=keyword)
        ]
    
    
    def get_one(self, _id=None, numero=None):
        res = self.get_stands(_id=_id, numero=numero)
        return res[0].toBeButton() if len(res) > 0 else None
    
    
    def get_contact(self, _id):
        res = self.get_stands(_id=_id)
        return res[0].toContact() if len(res) > 0 else None


        