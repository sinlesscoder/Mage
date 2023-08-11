from sqlalchemy import create_engine
from getpass import getpass

# Add your credentials
username = 'postgres'
password = getpass("Type in your server password: ")
host = '209.182.236.218'
port = '8362'
database = 'pathrise'

# Dialect together: Example PostgreSQL
dialect = f'postgresql://{username}:{password}@{host}:{port}/{database}'

# Create the engine object
engine = create_engine(dialect)