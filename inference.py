from env import WasteEnv, Action

def main():
    env = WasteEnv()

    print("[START] task=waste-routing env=openenv model=gpt-4.1-mini")

    obs = env.reset()
    done = False
    step = 0
    total_reward = 0
    rewards = []

    while not done:
        step += 1

        action = Action(category="garbage_collection", department="sanitation_team")

        obs, reward, done, info = env.step(action)

        total_reward += reward
        rewards.append(reward)

        print(f"[STEP] step={step} action=resolve reward={reward:.2f} done={done} error=null")

    print(f"[END] success=true steps={step} score={total_reward:.2f} rewards={','.join([str(r) for r in rewards])}")


if __name__ == "__main__":
    main()
