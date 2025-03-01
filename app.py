from fastapi import FastAPI, Form, Request,  HTTPException
import json
import httpx

app = FastAPI()


@app.post("/slack/interactivity")
async def slack_interactivity(request: Request, payload: str= Form(...)):
    try:
        action_payload = json.loads(payload)

        button_value = action_payload["actions"][0]["value"]
        print(f"button_value: {button_value}")
        # async with httpx.AsyncClient() as client:
        #     await client.post(MAKE_HTTP_REQUEST_URL, json={"button_value": button_value})

        return {"text": "Response recorded"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
