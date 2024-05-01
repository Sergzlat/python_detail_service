class Config:
    # Основные настройки приложения

class DevelopmentConfig(Config):
    # Настройки для разработки
    pass  # добавьте здесь свой код

class ProductionConfig(Config):
    # Настройки для продакшена

configurations = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
