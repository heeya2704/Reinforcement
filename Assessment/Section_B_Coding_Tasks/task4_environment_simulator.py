"""
Module 12 - Reinforcement Learning (Assessment M12-A1)
Section B: Practical Coding Tasks
Task 4: Simple RL Environment Simulator

Requirements:
- Define a DeliveryEnvironment class with attributes: current_state (dict with location and pending_orders),
  total_reward (float), and step_count (int).
- Implement a step(action) method that updates state, computes & returns reward, and prints new state and reward.
- Support at least three distinct actions with different state transitions & rewards (e.g., deliver_order, wait, navigate_to_zone).
- Run a loop executing predefined sequence of 5+ actions, printing per-step output and end summary.
"""

from typing import Dict, Any, List, Tuple


class DeliveryEnvironment:
    """
    Console-based Python environment modeling the full RL agent-environment loop
    for a food delivery dispatch scenario.
    """

    def __init__(self, initial_location: str = "Central Station", initial_pending_orders: int = 5):
        self.current_state: Dict[str, Any] = {
            "location": initial_location,
            "pending_orders": initial_pending_orders
        }
        self.total_reward: float = 0.0
        self.step_count: int = 0

    def step(self, action: str) -> Tuple[Dict[str, Any], float]:
        """
        Executes an action, updates environment state, computes reward feedback,
        and logs step outputs.
        """
        self.step_count += 1
        reward: float = 0.0
        transition_msg: str = ""

        if action == "deliver_order":
            if self.current_state["pending_orders"] > 0:
                self.current_state["pending_orders"] -= 1
                reward = 15.0
                transition_msg = f"Order delivered successfully! Pending orders left: {self.current_state['pending_orders']}"
            else:
                reward = -2.0
                transition_msg = "Attempted delivery with 0 pending orders! Small penalty incurred."

        elif action == "wait":
            # Waiting keeps location same, slightly penalizes idle delay
            reward = -1.0
            transition_msg = "Agent waited at current location. Slight delay penalty incurred."

        elif action == "navigate_to_zone":
            # Change location, small cost for travel distance
            zones = ["Downtown Core", "North Suburbs", "Westside Mall", "Eastside Tech Park"]
            next_zone_idx = (self.step_count) % len(zones)
            self.current_state["location"] = zones[next_zone_idx]
            reward = 3.0  # Reward positioning closer to high-demand cluster
            transition_msg = f"Navigated to new high-demand zone: {self.current_state['location']}"

        else:
            reward = -5.0
            transition_msg = f"Invalid action '{action}' attempted! Major penalty."

        # Update cumulative environment reward
        self.total_reward += reward

        # Print per-step feedback
        print(f"[Step {self.step_count:02d}] Action Taken: '{action}'")
        print(f"  Outcome      : {transition_msg}")
        print(f"  Step Reward  : {reward:+.1f}")
        print(f"  New State    : {self.current_state}")
        print(f"  Running Total: {self.total_reward:+.1f}")
        print("-" * 65)

        return self.current_state, reward

    def reset(self, initial_location: str = "Central Station", initial_pending_orders: int = 5) -> Dict[str, Any]:
        """Resets environment to initial conditions."""
        self.current_state = {
            "location": initial_location,
            "pending_orders": initial_pending_orders
        }
        self.total_reward = 0.0
        self.step_count = 0
        return self.current_state


if __name__ == "__main__":
    print("==================================================")
    print("   TASK 4: SIMPLE RL ENVIRONMENT SIMULATOR TEST   ")
    print("==================================================\n")

    env = DeliveryEnvironment(initial_location="Central Hub", initial_pending_orders=4)

    print(f"Initial State: {env.current_state}\n")

    # Sequence of 6 predefined actions
    action_sequence = [
        "navigate_to_zone",
        "deliver_order",
        "wait",
        "deliver_order",
        "navigate_to_zone",
        "deliver_order"
    ]

    print("Executing Action Sequence...\n")
    for action in action_sequence:
        env.step(action)

    print("==================================================")
    print("             EPISODE FINAL SUMMARY                ")
    print("==================================================")
    print(f"Total Steps Executed : {env.step_count}")
    print(f"Final Total Reward   : {env.total_reward:+.1f} points")
    print(f"Final State          : {env.current_state}")
    print("==================================================\n")
