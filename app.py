from fastapi import FastAPI, Form, Request,  HTTPException
import json
import httpx
import asyncio

app = FastAPI()
button = None

@app.post("/slack/interactivity")
async def slack_interactivity(request: Request, payload: str= Form(...)):
    global button
    try:
        action_payload = json.loads(payload)

        button_value = action_payload["actions"][0]["value"]
        print(f"button_value: {button_value}")
        button = button_value
        # async with httpx.AsyncClient() as client:
        #     await client.post(MAKE_HTTP_REQUEST_URL, json={"button_value": button_value})

        return {"text": "Response recorded"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.get("/get_value/")
async def get_value():
    while button is None:
        await asyncio.sleep(0.5)
    return {"button_value": button}