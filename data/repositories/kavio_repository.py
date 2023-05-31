
from data.datasources.db import CustomModel
from data.datasources.kavio_data import KavioDataSource


class KavioImplRepository:

    def __init__(self, kavioData: KavioDataSource, model: CustomModel):
        self.model = model
        self.kavioData = kavioData

    def get_serie(self, serie):
        try:
            return self.kavioData.get_serie(serie)
        except Exception as e:
            print(e)
            return ""
    

    def get_choice(self, index):
        try:
            return self.kavioData.get_choices(index)
        except Exception as e:
            print(e)

    
    def save_choice(self, sender_id, choice):
        try:
            self.model.save_choice(sender_id, choice)
        except Exception as e:
            print(e)

    def verif_max_choice(self, sender_id, choice):
        try:
            return self.model.verif_max_choice(sender_id, choice)
        except Exception as e:
            print(e)
            return 0
        
    
    def general_results(self, sender_id):
        try:
            return self.model.general_result(sender_id)
        except Exception as e:
            print(e)
            return []


    def etat_avancement(self, sender_id):
        try:
            return self.model.etat_avancement(sender_id)
        except Exception as e:
            print(e)

    
    def remove_data(self, sender_id):
        try:
            self.model.remove_data(sender_id)
        except Exception as e:
            print(e)