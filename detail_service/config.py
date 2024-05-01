class Config:
    # Основные настройки приложения

class DevelopmentConfig(Config):
    # Настройки для разработки

class ProductionConfig(Config):
    # Настройки для продакшена

configurations = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
