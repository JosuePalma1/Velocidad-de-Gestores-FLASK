class Config:
    SECRET_KEY = 'your_secret_key'
    
    # URIs de las bases de datos
    MYSQL_URI = 'mysql://root:1234567@localhost/udbinventario'
    POSTGRES_URI = 'postgresql://postgres:1234567@localhost:5433/udbinventario'
    ORACLE_URI = 'oracle://udbinventario:1234567@localhost:1521/XE'
    SQLSERVER_URI = 'mssql+pyodbc://localhost/udbinventario?driver=SQL+Server'
    
    # Configuración principal de SQLAlchemy - usa una de las URIs anteriores
    SQLALCHEMY_DATABASE_URI = MYSQL_URI  # Puedes cambiar a POSTGRES_URI, ORACLE_URI o SQLSERVER_URI según necesites
    SQLALCHEMY_TRACK_MODIFICATIONS = False