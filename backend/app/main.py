import os
import sys
from dotenv import load_dotenv
load_dotenv()
path = = os.environ["FILE_PATH"]
sys.path.append(path)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(CORSMiddleware())
