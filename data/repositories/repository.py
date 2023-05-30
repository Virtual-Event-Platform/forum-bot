from data.datasources.api import Api
from domains.entity.entity import Entity


class ImplRepository:
    def __init__(self, api: Api):
        self.api = api

    def get_stands(self, _id=None, keyword=None, numero=None):
        try:
            return self.api.get_stands(_id=_id, keyword=keyword, numero=numero)
        except Exception as e:
            print(e)
            return []
        
    def get_assets(self, _id, _type):
        try:
            return self.api.get_assets(_id, _type)
        except Exception as e:
            print(e)
            return []
        
    def get_fiches(self, _id, keyword, domain):
        try:
            return self.api.get_fiches(_id, keyword, domain)
        except Exception as e:
            print(e)
            return []
        
    def get_domains(self):
        try:
            return self.api.get_domains()
        except Exception as e:
            print(e)
            return []
        
    
    def set_stats(self, stat):
        try:
            return self.api.set_stat(stat)
        except Exception as e:
            print(e)
            return []
