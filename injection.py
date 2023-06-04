from ampalibe import Messenger, Model
from data.datasources.api import Api
from conf import Configuration as config
from data.datasources.db import CustomModel
from data.datasources.kavio_data import KavioDataSource
from domains.usescase.set_stats import StatUseCase
from domains.usescase.get_kavio import KavioUseCase
from domains.usescase.get_assets import AssetUseCase
from domains.usescase.get_stands import StandUseCase
from domains.usescase.get_fiches import FicheMetierUseCase

chat, query = Messenger(), Model()
statUsecase = StatUseCase(Api(config.PB_URL, config.PB_USER, config.PB_PASSWORD))
standUseCase = StandUseCase(Api(config.PB_URL, config.PB_USER, config.PB_PASSWORD))
assetUseCase = AssetUseCase(Api(config.PB_URL, config.PB_USER, config.PB_PASSWORD))
ficheMetierUseCase = FicheMetierUseCase(Api(config.PB_URL, config.PB_USER, config.PB_PASSWORD))
kavioUseCase =  KavioUseCase(KavioDataSource(), CustomModel())

