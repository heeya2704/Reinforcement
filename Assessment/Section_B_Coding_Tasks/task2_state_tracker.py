"""
Module 12 - Reinforcement Learning (Assessment M12-A1)
Section B: Practical Coding Tasks
Task 2: Agent State Tracker

Requirements:
- Create dictionary representing agent's state with keys: location (str), orders_delivered (int),
  total_reward (float), is_available (bool).
- Define update_state(state, new_location, reward_earned) that updates location,
  increments orders_delivered by 1, and adds reward_earned to total_reward.
- Simulate at least four state transitions with different locations and reward values.
- After each update, print the complete current state in a clear, readable format.
"""

from typing import Dict, Any


def update_state(state: Dict[str, Any], new_location: str, reward_earned: float) -> Dict[str, Any]:
    """
    Updates the delivery agent's state dictionary after completing an action/transition.
    
    Parameters:
        state (dict): The current state dictionary.
        new_location (str): The new geographic location or zone of the agent.
        reward_earned (float): Reward score obtained from the transition.
        
    Returns:
        dict: The updated state dictionary.
    """
    state["location"] = new_location
    state["orders_delivered"] += 1
    state["total_reward"] += float(reward_earned)
    
    return state


def print_state(step_num: int, state: Dict[str, Any], transition_info: str) -> None:
    """Utility helper to pretty-print agent state."""
    print(f"--- State Transition #{step_num}: {transition_info} ---")
    print(f"  Location         : {state['location']}")
    print(f"  Orders Delivered : {state['orders_delivered']}")
    print(f"  Total Reward     : {state['total_reward']:+.2f}")
    print(f"  Is Available     : {state['is_available']}")
    print("-" * 50 + "\n")


if __name__ == "__main__":
    print("==================================================")
    print("        TASK 2: AGENT STATE TRACKER TEST          ")
    print("==================================================\n")

    # Initial Agent State
    agent_state: Dict[str, Any] = {
        "location": "Hub Central",
        "orders_delivered": 0,
        "total_reward": 0.0,
        "is_available": True
    }

    print("Initial Agent State:")
    print_state(0, agent_state, "System Initialization")

    # Transitions simulation (At least 4 transitions)
    transitions = [
        ("Downtown Diner", 12.5, "Pickup & Fast Delivery to Downtown"),
        ("Westside Apartments", 8.0, "Short Distance Delivery to Westside"),
        ("North Suburban Mall", -2.0, "Delayed Delivery to North Suburbs"),
        ("Eastside Food Plaza", 15.0, "On-Time Premium Delivery to Eastside"),
        ("South Campus Hub", 11.0, "Bonus Delivery to South Campus")
    ]

    for step, (loc, rwd, info) in enumerate(transitions, start=1):
        update_state(agent_state, new_location=loc, reward_earned=rwd)
        print_state(step, agent_state, info)

    print("State Tracker Simulation Completed Successfully!")
