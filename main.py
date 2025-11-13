from fastapi import FastAPI 
from Functions import *
import json


app = FastAPI()

@app.get("/test")
def aaa():
    return {"msg": "hi from test"}


@app.get("/test/name")
def bbb(name):
    return {"msg": name}


@app.post("/caesar")
def ccc(text:str, offset: int, mode: str):
    if mode == "encrypt":
      encrypt_with_caesar = Caesar1(text, offset)
      return {"encrypted_text": encrypt_with_caesar}
    if mode == "decrypt": 
      encrypt_with_caesar = Caesar2()
      return {"decrypted_text": encrypt_with_caesar}
    

@app.get("/fence/encrypt?text=none")





@app.get("/fence/encrypt?text=")
def Fences():















