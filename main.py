from fastapi import FastAPI
import uvicorn

import ParseTextUtil

app = FastAPI()


@app.post("/v1/text-to-schedule")
def getSchedule(text: str):
    return ParseTextUtil.parseText(text)

@app.post("/v1/schedule-share")
def scheduleShare(text:str):
    return "Haven't finished yet!"


if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1", port=8000, reload=True, debug=True)
