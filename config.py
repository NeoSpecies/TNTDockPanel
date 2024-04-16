class Config:
    DEBUG = True
    SECRET_KEY = 'your_secret_key'
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'sqlite:///yourdatabase.db'
    # 例外认证的路由
    NO_AUTH = ['/images/test']
