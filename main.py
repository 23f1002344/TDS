# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "fastapi",
#     "uvicorn",
# ]
# ///

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict
import json


app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"]) 

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

def parse_csv():
    res={}
    with open('q-vercel-python.json', 'r') as f:
        data = json.loads(f.readline())
        for ent in data:
            res[ent['name']]=ent['marks']

    return res


students: Dict[str, int] = parse_csv()

@app.get("/api")
def get_marks(name: list[str] = Query([],) ):
    print(name)
    marks: List[int]=[students[nm] for nm in name]
    return {"marks": marks}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)