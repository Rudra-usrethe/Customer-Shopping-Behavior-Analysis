import pandas as pd
from sqlalchemy import create_engine

username = "root"
password = "18@r"
host = "Hanuman-ji"      # Usually localhost
port = "3306"
database = "project_data_analyist"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)