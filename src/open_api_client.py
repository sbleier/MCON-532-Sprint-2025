# os allows you to to manipulate files
import os
from openai import OpenAI
# load_dotenv loads enviroment (variables) from file
from dotenv import load_dotenv

# Load the .env file only once
#joins two paths (location of current file and /.env and puts in string
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
#loads .env file and makes enviroment variables available to python process
load_dotenv(dotenv_path=dotenv_path)

# Initialize the client only once
_client_instance = None

#creates a global and checks if there's global instance
def get_openai_client():
    global _client_instance
    if _client_instance is None:
        api_key = os.getenv("OPENAI_API_KEY")
        org_id = os.getenv("OPENAI_ORG_ID").strip()
        #calls OpenAI method to fetch client
        _client_instance = OpenAI(api_key=api_key, organization=org_id)
    return _client_instance