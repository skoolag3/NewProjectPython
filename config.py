import os

load_dotenv()

class Config:

    mysql_host = os.getenv('MYSQL_HOST', 'localhost')
    mysql_port = os.getenv('MYSQL_PORT', 3306)
    mysql_user = os.getenv('MYSQL_USER', 'root')
    mysql_password = os.getenv('MYSQL_PASSWORD', 'root')
    mysql_db = os.getenv('MYSQL_DB', 'agendamento_ACME')
    mysql_cursorclass = os.getenv('MYSQL_CURSORCLASS', 'DictCursor')

    debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    secret_key = os.getenv('SECRET_KEY', 'vasco')