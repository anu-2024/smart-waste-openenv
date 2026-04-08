import os
from typing import List, Optional

from env import WasteEnv, Action


TASK_NAME = "waste-routing"
BENCHMARK = "openenv"
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")


def log_start(task: str, env: str, model: str):
    print(f"[START] task={task} env={env} model={model}", flush=True)


def log_step(step: int, action: str, reward: float, done: bool, error: Optional[str]):
    error_val = error if error else "null"
    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error={error_val}",
        flush=True,
    )


def log_end(success: bool, steps: int, score: float, rewards: List[float]):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(
        f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={rewards_str}",
        flush=True,
    )


def main():
    env = WasteEnv()

    rewards = []
    step_count = 0
    success = False

    log_start(TASK_NAME, BENCHMARK, MODEL_NAME)

    try:
        obs = env.reset()
        done = False

        while not done and step_count < 8:
            step_count += 1

            action = Action(
                category="garbage_collection",
                department="sanitation_team"
            )

            obs, reward, done, info = env.step(action)

            reward_value = float(reward)

            rewards.append(reward_value)

            log_step(
                step=step_count,
                action="resolve",
                reward=reward_value,
                done=done,
                error=None
            )

        score = min(max(sum(rewards), 0), 1)
        success = score > 0

    except Exception as e:
        log_step(step_count, "error", 0.0, True, str(e))
        score = 0

    finally:
        log_end(success, step_count, score, rewards)


if __name__ == "__main__":
    main()
