# Data Science Assessment M12-A1: Reinforcement Learning

**Module 12 — Reinforcement Learning Assessment Solution**  
**Program:** Data Science  
**Assessment Code:** M12-A1  
**Stack:** Python 3  

---

## Project Structure Overview

```text
Assessment/
├── README.md                              # Main guide and execution instructions
├── Section_A_Concept_Application.md       # Answers to Questions S1 through S6
├── Section_B_Coding_Tasks/
│   ├── task1_reward_function.py           # Task 1: Delivery Reward Function
│   ├── task2_state_tracker.py             # Task 2: Agent State Tracker
│   ├── task3_episode_logger.py            # Task 3: Action-Reward Episode Logger
│   └── task4_environment_simulator.py     # Task 4: Simple RL Environment Simulator
├── Section_C_Mini_Capstone/
│   └── food_delivery_rl_simulator.py      # Interactive Menu-driven Capstone Simulator
└── Section_D_AI_Augmented_Learning/
    ├── step1_ai_prompt_and_original.py    # Step 1: AI Prompt & Buggy AI Code
    ├── step2_corrected_solution.py        # Step 2: Debugged & Corrected Solution
    └── section_d_explanation.md           # Submission items 1, 2, and 3
```

---

## Instructions for Running Code Tasks

### Section B: Practical Coding Tasks
Run each task individually using Python 3:

```bash
# Task 1: Delivery Reward Function
python Assessment/Section_B_Coding_Tasks/task1_reward_function.py

# Task 2: Agent State Tracker
python Assessment/Section_B_Coding_Tasks/task2_state_tracker.py

# Task 3: Action-Reward Episode Logger
python Assessment/Section_B_Coding_Tasks/task3_episode_logger.py

# Task 4: Simple RL Environment Simulator
python Assessment/Section_B_Coding_Tasks/task4_environment_simulator.py
```

---

### Section C: Mini Capstone Project

Launch the interactive console menu:
```bash
python Assessment/Section_C_Mini_Capstone/food_delivery_rl_simulator.py
```

*Options available in menu:*
1. **Start New Delivery Episode** — Simulates a multi-step delivery shift and outputs step logs.
2. **View Agent Stats** — Displays cumulative episodes, total rewards, and average reward per episode.
3. **Exit** — Safely quits the simulator.

To run automated demo mode without interactive prompts:
```bash
python Assessment/Section_C_Mini_Capstone/food_delivery_rl_simulator.py --demo
```

---

### Section D: AI-Augmented Learning

Run the AI bug demonstration and corrected solution:
```bash
# Step 1: Original AI code demonstrating state leakage bug
python Assessment/Section_D_AI_Augmented_Learning/step1_ai_prompt_and_original.py

# Step 2: Corrected solution with state encapsulation
python Assessment/Section_D_AI_Augmented_Learning/step2_corrected_solution.py
```

Detailed writeup containing the prompt, comparison, and 3-4 line note can be found in `Section_D_AI_Augmented_Learning/section_d_explanation.md`.
