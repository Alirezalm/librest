from abc import ABC


class Config(ABC):
    pass


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    pass
