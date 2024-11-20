class conf:
    host = "localhost"
    database = "sandwich_maker_api"
    port = 3306
    user = "root"
    password = "Shazagh98!"

DATABASE_URL = f"mysql+pymysql://{conf.user}:{conf.password}@{conf.host}/{conf.database}"
