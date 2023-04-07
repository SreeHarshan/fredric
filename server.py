from fastapi import FastAPI

import Fredric_v3 as fredric
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"value":"Running"}

@app.get("/getclass")
async def getClass():
    classes = fredric.get_class()
    values = dict()
    values["prev"] = classes[0]
    values["curr"] = classes[1]
    values["next"] = classes[2]
    return values

@app.get("/joinclass")
def joinClass(name):
    fredric.join_class(name) 
    return {"value":"done"}

@app.get("/getlink")
async def getlink(name):
    link = fredric.get_link(name)
    return {"link":link}

@app.get("/autojoin")
def autojoin():
    if fredric.autojoin:
        fredric.autojoin = False
        return {"autojoin":"false"}
    fredric.autojoin = True
    return {"autojoin":"true"}
