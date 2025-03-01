from fastapi import FastAPI, Form, Request
import json
import httpx

app = FastAPI()


@app.post("/slack/interactivity")
async def slack_interactivity(request, payload: str= Form(...)):
    try:
        action_payload = json.loads(payload)

        button_value = action_payload["actions"][0]["value"]
        print(f"button_value: {button_value}")
    except:
        print("in except")
    return {"message": "Hello World"}