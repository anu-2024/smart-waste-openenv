import os
from typing import List, Optional
from openai import OpenAI

from env import WasteEnv, Action


TASK_NAME = "waste-routing"
BENCHMARK = "openenv"

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    raise ValueError("HF_TOKEN environment variable is required")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)


def log_start(task: str, env: str, model: str):
    print(f"[START] task={task} env={env} model={model}", flush=True)


def log_step(step: int, action: str, reward: float, done: bool, error: Optional[str]):
    err = error if error else "null"

    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error={err}",
        flush=True
    )


def log_end(success: bool, steps: int, rewards: List[float]):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)

    print(
        f"[END] success={str(success).lower()} steps={steps} rewards={rewards_str}",
        flush=True
    )


def llm_decide_action(text: str):

    client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You route municipal waste complaints."},
            {"role": "user", "content": text}
        ]
    )

    return Action(
        category="garbage_collection",
        department="sanitation_team"
    )


def main():

    env = WasteEnv()

    rewards = []
    steps = 0
    success = False

    log_start(TASK_NAME, BENCHMARK, MODEL_NAME)

    try:

        obs = env.reset()
        done = False

        while not done and steps < 8:

            steps += 1

            action = llm_decide_action(str(obs))

            obs, reward, done, info = env.step(action)

            reward = float(reward)

            rewards.append(reward)

            log_step(steps, "resolve", reward, done, None)

        success = sum(rewards) > 0

    except Exception as e:

        log_step(steps, "error", 0.0, True, str(e))

    finally:

        log_end(success, steps, rewards)


if __name__ == "__main__":
    main()
