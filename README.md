

---
title: Smart Waste Management AI Environment
emoji: ♻️
colorFrom: green
colorTo: blue
sdk: docker
app_file: app.py
pinned: false
tags:
- openenv
---

# Smart Waste Management OpenEnv Environment

## Overview

This project implements a **real-world OpenEnv simulation** for handling municipal waste complaints.
The environment simulates how a city authority processes waste-related complaints from citizens.

An AI agent interacts with the environment using the standard **OpenEnv API interface**:

* `reset()` – start a new complaint case
* `state()` – view the current environment state
* `step()` – perform an action to resolve the complaint

The agent must classify the complaint, assign the responsible department, inspect the issue, dispatch a truck, and mark cleanup completion.

---
## API Documentation

Interactive API documentation is available at:

https://qwerty123g45-smart-waste-openenv.hf.space/docs

This interface allows testers to interact with the environment endpoints directly.

# Live API (Hugging Face Space)

The environment is deployed on Hugging Face Spaces.

Base URL:

```
https://qwerty123g45-smart-waste-openenv.hf.space
```

## Reset Environment

Starts a new waste complaint scenario.

```
GET
https://qwerty123g45-smart-waste-openenv.hf.space/reset
```

Example response:

```json
{
 "complaint": "Garbage overflowing near market",
 "location": "Ward 13",
 "step": "classification"
}
```

---

## Current Environment State

Returns the current stage and complaint information.

```
GET
https://qwerty123g45-smart-waste-openenv.hf.space/state
```

Example response:

```json
{
 "stage": 0,
 "complaint": {
   "complaint": "Garbage overflowing near market",
   "location": "Ward 13",
   "category": "garbage_collection",
   "department": "sanitation_team"
 }
}
```

---

## Perform Action

Agent interacts with the environment using the step API.

```
POST
https://qwerty123g45-smart-waste-openenv.hf.space/step
```

Example request:

```json
{
 "category": "garbage_collection",
 "department": "sanitation_team",
 "inspect": true,
 "assign_truck": true,
 "cleanup_complete": true
}
```

Example response:

```json
{
 "complaint": "Garbage overflowing near market",
 "location": "Ward 13",
 "step": "1",
 "reward": 0.15,
 "done": false
}
```

---
# Observation Space

The environment returns the following observation:

| Field | Type | Description |
|------|------|-------------|
complaint | string | Description of the waste complaint |
location | string | Ward location |
step | string | Current workflow stage |

Example:

{
 "complaint": "Garbage overflowing near market",
 "location": "Ward 13",
 "step": "classification"
}

# Action Space

The agent performs actions using the following fields:

| Field | Type | Description |
|------|------|-------------|
category | string | Complaint category classification |
department | string | Responsible department |
inspect | boolean | Inspection performed |
assign_truck | boolean | Garbage truck dispatched |
cleanup_complete | boolean | Cleanup completed |
# Environment Workflow

The environment simulates a **4-step waste complaint resolution process**:

| Stage | Task                     |
| ----- | ------------------------ |
| 0     | Complaint classification |
| 1     | Site inspection          |
| 2     | Truck assignment         |
| 3     | Cleanup completion       |

Each correct action gives a **reward score between 0 and 1**.

---

# Reward Logic

| Action             | Reward |
| ------------------ | ------ |
| Correct category   | +0.4   |
| Correct department | +0.2   |
| Inspection done    | +0.2   |
| Truck assigned     | +0.1   |
| Cleanup completed  | +0.1   |

Maximum score per episode = **1.0**

---

# Project Structure

```
smart_waste_openenv
│
├── app.py              # FastAPI server
├── env.py              # OpenEnv environment implementation
├── tasks.py            # task definitions
├── dataset.json        # complaint dataset
├── inference.py        # baseline inference script
├── openenv.yaml        # OpenEnv specification
├── requirements.txt    # dependencies
├── Dockerfile          # container deployment
└── README.md
```

---

# Running Locally

Install dependencies:

```
pip install -r requirements.txt
```

Start the API server:

```
uvicorn app:app --host 0.0.0.0 --port 8000
```

Access API:

```
http://localhost:8000/reset
```

---

# Running the Baseline Agent

```
python inference.py
```

Example output:

```
[START] task=waste-routing env=openenv model=gpt-4.1-mini
[STEP] step=1 action=resolve reward=0.20 done=false error=null
[STEP] step=2 action=resolve reward=0.20 done=false error=null
[STEP] step=3 action=resolve reward=0.10 done=false error=null
[STEP] step=4 action=resolve reward=0.10 done=true error=null
[END] success=true steps=4 rewards=0.20,0.20,0.10,0.10
```

---

# Technologies Used

* Python
* FastAPI
* OpenEnv Framework
* Hugging Face Spaces
* Docker
* Pydantic

---

# Hackathon Submission

This project was created for the **Meta × Hugging Face OpenEnv Hackathon**.

The environment follows the required OpenEnv API structure:

* reset()
* state()
* step()

and includes a baseline inference script for automated evaluation.

---
