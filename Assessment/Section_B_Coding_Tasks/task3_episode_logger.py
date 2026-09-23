"""
Module 12 - Reinforcement Learning (Assessment M12-A1)
Section B: Practical Coding Tasks
Task 3: Action-Reward Episode Logger

Requirements:
- List of possible actions: ['accept_order', 'reject_order', 'request_directions', 'mark_delivered'].
- Fixed reward dictionary: accept_order = +2, reject_order = -1, request_directions = 0, mark_delivered = +10.
- Simulate an episode by iterating through a predefined sequence of at least 6 actions.
- Print each step (action taken, step reward, running cumulative reward).
- Print total episode reward at the end.
"""

from typing import List, Dict


def run_episode_simulation(action_sequence: List[str], reward_map: Dict[str, float]) -> float:
    """
    Executes a predefined sequence of actions, logs step dynamics, and accumulates reward.
    """
    cumulative_reward: float = 0.0

    print("Step | Action Taken        | Step Reward | Running Total Reward")
    print("-" * 62)

    for step, action in enumerate(action_sequence, start=1):
        if action not in reward_map:
            raise ValueError(f"Unknown action '{action}' encountered.")

        step_reward = reward_map[action]
        cumulative_reward += step_reward

        print(f"{step:4d} | {action:20s} | {step_reward:+11.1f} | {cumulative_reward:+20.1f}")

    print("-" * 62)
    print(f"Total Episode Reward: {cumulative_reward:+.1f} points\n")
    return cumulative_reward


if __name__ == "__main__":
    print("==================================================")
    print("      TASK 3: ACTION-REWARD EPISODE LOGGER        ")
    print("==================================================\n")

    # Define possible actions & fixed reward dictionary
    possible_actions = ['accept_order', 'reject_order', 'request_directions', 'mark_delivered']
    reward_dictionary: Dict[str, float] = {
        'accept_order': 2.0,
        'reject_order': -1.0,
        'request_directions': 0.0,
        'mark_delivered': 10.0
    }

    print("Action Reward Structure:")
    for act, rwd in reward_dictionary.items():
        print(f"  - {act:20s} : {rwd:+.1f}")
    print("\nStarting Episode Simulation...\n")

    # Sequence of at least 6 actions
    action_sequence_1 = [
        'accept_order',        # +2  (Total: 2)
        'request_directions',  # +0  (Total: 2)
        'mark_delivered',      # +10 (Total: 12)
        'reject_order',        # -1  (Total: 11)
        'accept_order',        # +2  (Total: 13)
        'request_directions',  # +0  (Total: 13)
        'mark_delivered'       # +10 (Total: 23)
    ]

    print("--- Episode 1 Log ---")
    run_episode_simulation(action_sequence_1, reward_dictionary)

    # Secondary test sequence
    action_sequence_2 = [
        'reject_order',
        'reject_order',
        'accept_order',
        'request_directions',
        'mark_delivered',
        'accept_order',
        'mark_delivered'
    ]

    print("--- Episode 2 Log (Alternative Strategy) ---")
    run_episode_simulation(action_sequence_2, reward_dictionary)

    print("Episode Logger Execution Completed Successfully!")
