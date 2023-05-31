from data.datasources.api import Api
from data.repositories.repository import ImplRepository


class StatUseCase(ImplRepository):
    def __init__(self, api: Api):
        super().__init__(api)

    def set(self, stat):
        return self.set_stats(stat)
    
    def do_kavio(self, sender_id, finish=False):
        return self.do_kavio_stat(sender_id, finish)
        