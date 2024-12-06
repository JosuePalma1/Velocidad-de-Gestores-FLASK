class Config:
    SECRET_KEY = 'your_secret_key'
    
    # URIs de las bases de datos
    MYSQL_URI = 'mysql://root:My123@localhost/bdproducto2'
    POSTGRES_URI = 'postgresql://postgres:123456@localhost:5432/BDPRODUCTO2'
    ORACLE_URI = 'oracle://ubdproducto2:1234567@localhost:1521/XE'
    SQLSERVER_URI = 'mssql+pyodbc://localhost/BDPRODUCTO2?driver=SQL+Server'
    
    # Configuración principal de SQLAlchemy - usa una de las URIs anteriores
    SQLALCHEMY_DATABASE_URI = MYSQL_URI  # Puedes cambiar a POSTGRES_URI, ORACLE_URI o SQLSERVER_URI según necesites
    SQLALCHEMY_TRACK_MODIFICATIONS = False