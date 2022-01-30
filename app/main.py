from fastapi import FastAPI, Request, HTTPException

app = FastAPI()

@app.get("/")
async def home(request: Request):
    return {'home':'web_endpoint'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
