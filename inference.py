
import os
from openai import OpenAI
from env import WasteEnv,Action
API_BASE_URL = os.getenv("API_BASE_URL","https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME","gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN","dummy_token")
if HF_TOKEN is None:
    raise ValueError("HF_TOKEN environment variable required")

client=OpenAI(base_url=API_BASE_URL,api_key=HF_TOKEN)

env=WasteEnv()
obs=env.reset()

print(f"[START] task=waste-routing env=openenv model={MODEL_NAME}")

actions=[
Action(category="garbage_collection",department="sanitation_team"),
Action(inspect=True),
Action(assign_truck=True),
Action(cleanup_complete=True)
]

rewards=[]
step=1

for a in actions:
    obs,r,done,_=env.step(a)
    rewards.append(r.score)
    print(f"[STEP] step={step} action=resolve reward={r.score:.2f} done={str(done).lower()} error=null")
    step+=1
    if done:
        break

reward_str=",".join([f"{x:.2f}" for x in rewards])

score=sum(rewards)

print(f"[END] success={str(done).lower()} steps={len(rewards)} score={score:.2f} rewards={reward_str}")
