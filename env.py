from pydantic import BaseModel
import json, random
import tasks 
class Observation(BaseModel):
    complaint: str
    location: str
    step: str


class Action(BaseModel):
    category: str | None = None
    department: str | None = None
    inspect: bool | None = None
    assign_truck: bool | None = None
    cleanup_complete: bool | None = None


class Reward(BaseModel):
    score: float


class WasteEnv:

    def __init__(self):
        with open("dataset.json") as f:
            self.data = json.load(f)

        self.current = None
        self.stage = 0
        self.history = []


    def reset(self):

        self.current = random.choice(self.data)
        self.stage = 0
        self.history = []

        return Observation(
            complaint=self.current["complaint"],
            location=self.current["location"],
            step="classification"
        )


    def state(self):

        return {
            "stage": self.stage,
            "complaint": self.current,
            "history": self.history
        }


    def step(self, action: Action):

        reward = 0.0
        done = False

        self.history.append(action.dict())

        # stage 0 classify
        if self.stage == 0:

            if action.category == self.current["category"]:
                reward += 0.4
            else:
                reward -= 0.1

            if action.department == self.current["department"]:
                reward += 0.2
            else:
                reward -= 0.05

            self.stage = 1


        # stage 1 inspection
        elif self.stage == 1:

            if action.inspect:
                reward += 0.2
            else:
                reward -= 0.05

            self.stage = 2


        # stage 2 truck assignment
        elif self.stage == 2:

            if action.assign_truck:
                reward += 0.1
            else:
                reward -= 0.02

            self.stage = 3


               # stage 3 cleanup
        elif self.stage == 3:

            if action.cleanup_complete:
                reward += 0.1
            else:
                reward -= 0.02

            done = True

        # IMPORTANT: ensure reward always between (0,1)
        reward = max(0.01, min(0.99, reward))

        return (
            Observation(
                complaint=self.current["complaint"],
                location=self.current["location"],
                step=str(self.stage)
            ),
            Reward(score=reward),
            done,
            {}
        )
