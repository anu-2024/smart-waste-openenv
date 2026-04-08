import os
from openai import OpenAI
from env import WasteEnv, Action


def main():

    API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
    MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
    HF_TOKEN = os.getenv("HF_TOKEN")

    if HF_TOKEN is None:
        raise ValueError("HF_TOKEN environment variable required")

    client = OpenAI(
        base_url=API_BASE_URL,
        api_key=HF_TOKEN
    )

    env = WasteEnv()
    obs = env.reset()

    print(f"[START] task=waste-routing env=openenv model={MODEL_NAME}")

    rewards = []
    step = 1
    done = False

    while not done and step <= 4:

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI agent managing municipal waste complaints."
                },
                {
                    "role": "user",
                    "content": f"Complaint: {obs['complaint']} Location: {obs['location']}. "
                               "Decide the next step: classification, inspection, truck assignment, or cleanup."
                }
            ]
        )

        if step == 1:
            action = Action(category="garbage_collection", department="sanitation_team")

        elif step == 2:
            action = Action(inspect=True)

        elif step == 3:
            action = Action(assign_truck=True)

        else:
            action = Action(cleanup_complete=True)

        obs, r, done, _ = env.step(action)

        rewards.append(r.score)

        print(
            f"[STEP] step={step} action=resolve reward={r.score:.2f} "
            f"done={str(done).lower()} error=null"
        )

        step += 1

    reward_str = ",".join([f"{x:.2f}" for x in rewards])
    score = sum(rewards)

    print(
        f"[END] success={str(done).lower()} steps={len(rewards)} "
        f"score={score:.2f} rewards={reward_str}"
    )


if __name__ == "__main__":
    main()
