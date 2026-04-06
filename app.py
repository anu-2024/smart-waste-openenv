from fastapi import FastAPI
from env import WasteEnv, Action

app = FastAPI()
env = WasteEnv()

@app.get("/")
def root():
    return {"message": "Smart Waste OpenEnv API running"}

@app.get("/reset")
def reset():
    obs = env.reset()
    return obs.dict()

@app.get("/state")
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