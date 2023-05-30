from pocketbase import PocketBase
from domains.entity.stat import Stat
from domains.entity.asset import Asset
from domains.entity.domain import Domain
from domains.entity.entity import Entity
from domains.entity.fiche import FicheMetier


class Api:
    def __init__(self, url, user, password):
        self.client = PocketBase(url)
        self.client.admins.auth_with_password(user, password)


    def _struct_stand(self, data):
        data['logo'] = self.client.base_url + f"/api/files/{data['collectionId']}/{data['id']}/{data['logo']}"
        data['_id'] = data['id']
        return data
    
    
    def _struct_asset(self, data):
        data['url'] = self.client.base_url + f"/api/files/{data['collectionId']}/{data['id']}/{data['file']}"
        data['_id'] = data['id']
        data['_type'] = data['type']
        return data
    

    def _struct_fiche(self, data):
        data['_id'] = data['id']
        data['url'] = self.client.base_url + f"/api/files/{data['collectionId']}/{data['id']}/{data['file']}"
        return data
    

    def _struct_domain(self, data):
        data['_id'] = data['id']
        return data


    def get_stands(self, _id=None, keyword=None, numero=None):
        query_params = {"sort":"category.level,name"}
        if _id:
            query_params['filter']=f"(id = '{_id}'"
        if numero:
            query_params['filter']=f"(numero = '{numero}'"
        if keyword:
            query_params['filter']=f"(name ~ '%{keyword}%'"
        query_params['filter'] = (query_params['filter'] + " && hide = False)") if 'filter' in query_params else "hide = False"

        result = self.client.collection("entities").get_full_list(
            query_params=query_params
        )
        return [
            Entity(**self._struct_stand(data.__dict__['collection_id']))
            for data in result
        ]


    def get_assets(self, _id, _type):
        result = self.client.collection("assets").get_full_list(
            query_params={
                'sort': '-updated',
                'filter': f"(entity = '{_id}' && type = '{_type}')"
            }
        )
        return [
            Asset(**self._struct_asset(data.__dict__['collection_id']))
            for data in result
        ]
    

    def get_fiches(self, _id=None, keyword=None, domain=None):
        query_params = {'sort': 'name'}
        if _id:
            query_params['filter']=f"(id = '{_id}')"
        if keyword:
            query_params['filter']=f"(name ~ '%{keyword}%')"
        if domain:
            query_params['filter']=f"(domain = '{domain}')"
        result = self.client.collection("jobs").get_full_list(
            query_params=query_params
        )
        return [
            FicheMetier(**self._struct_fiche(data.__dict__['collection_id']))
            for data in result
        ]
    

    def get_domains(self):
        result = self.client.collection("domains").get_full_list(
            query_params={'sort': 'name'})
        return [
            Domain(**self._struct_domain(data.__dict__['collection_id']))
            for data in result
        ]
    
    def set_stat(self, stat: Stat):
        data = {"sender_id": stat.sender_id}
        if stat.entity:
            data['entity'] = stat.entity
        if stat.asset:
            data['asset'] = stat.asset
        if stat.fiche:
            data['fiche'] = stat.fiche
        self.client.collection("stats").create(data)
