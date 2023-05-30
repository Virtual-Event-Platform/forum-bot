from data.datasources.api import Api
from data.repositories.repository import ImplRepository


class FicheMetierUseCase(ImplRepository):
    def __init__(self, api: Api):
        super().__init__(api)

    def get(self, _id=None, keyword=None, domain=None, minimal=False):
        return [
            fiche.toQuickReply() if minimal else fiche.toElement()
            for fiche in self.get_fiches(_id=_id, keyword=keyword, domain=domain)
        ]
    

    def all_domains(self):
        return [
            domain.toQuickReply()
            for domain in self.get_domains()
        ]