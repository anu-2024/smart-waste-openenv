import sys
import os
from fastapi import FastAPI
import uvicorn

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from env import WasteEnv, Action

app = FastAPI()
env = WasteEnv()


@app.get("/reset")
@app.post("/reset")
def reset():
    obs = env.reset()
    return obs.dict()


@app.get("/state")
@app.post("/state")
def state():
    return env.state()


@app.post("/step")
def step(action: Action):

    obs, r, done, info = env.step(action)

    return {
        "complaint": obs.complaint,
        "location": obs.location,
        "step": obs.step,
        "reward": r.score,
        "done": done
    }


def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()
