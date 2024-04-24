from fastapi import FastAPI,Request
from fastapi import FastAPI, Request, Response, HTTPException, status
import requests

TG_API_URL = 'https://multillm.ai-pro.org'
PROXIES_URL = {"http":"http://127.0.0.1:7890","https":"http://127.0.0.1:7890"}

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    global TG_API_URL,PROXIES_URL

    burp0_url = TG_API_URL +"/api/openai-completion"
    burp0_headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36", "Content-Type": "application/json"}
    burp0_json=await request.json()
    burp0_json["stream"]=True
    ret=requests.post(burp0_url, headers=burp0_headers, json=burp0_json,proxies=PROXIES_URL)
    return ret.json()

@app.api_route("/{_:path}", methods=["POST", "GET", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH", "TRACE"])
async def catch_all(_):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3699)
