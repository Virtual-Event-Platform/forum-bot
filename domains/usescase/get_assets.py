from base import singleton
from data.datasources.api import Api
from data.repositories.repository import ImplRepository

@singleton
class AssetUseCase(ImplRepository):
    def __init__(self, api: Api):
        super().__init__(api)

    def get(self, _id, _type, minim=False):
        return [
            ass.toQuickReply() if minim else ass.toElement()
            for ass in self.get_assets(_id=_id, _type=_type)
        ]
    
