from langchain_community.utilities import SQLDatabase
from dotenv import load_dotenv
import os

load_dotenv()


def get_db():
    return SQLDatabase.from_uri(os.getenv("DATABASE_URL"))


