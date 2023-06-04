from base import singleton
from data.datasources.api import Api
from ampalibe import Messenger, Model
from conf import Configuration as config
from data.datasources.db import CustomModel
from data.datasources.kavio_data import KavioDataSource
from domains.usescase.set_stats import StatUseCase
from domains.usescase.get_kavio import KavioUseCase
from domains.usescase.get_assets import AssetUseCase
from domains.usescase.get_stands import StandUseCase
from domains.usescase.get_fiches import FicheMetierUseCase


query = singleton(Model)()
chat = singleton(Messenger)()
api = Api(config.PB_URL, config.PB_USER, config.PB_PASSWORD)

statUsecase = StatUseCase(api)
standUseCase = StandUseCase(api)
assetUseCase = AssetUseCase(api)
ficheMetierUseCase = FicheMetierUseCase(api)
kavioUseCase =  KavioUseCase(KavioDataSource(), CustomModel())

