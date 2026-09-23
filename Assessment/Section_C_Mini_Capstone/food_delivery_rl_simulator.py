"""
Module 12 - Reinforcement Learning (Assessment M12-A1)
Section C: Mini Capstone Project
Food Delivery RL Concept Simulator

Objective:
Build a console-based Food Delivery Reinforcement Learning Simulator that models the full RL loop
(agent, environment, actions, states, and rewards) for a delivery dispatch scenario.

Requirements:
- Menu-driven interface: [1] Start New Delivery Episode, [2] View Agent Stats, [3] Exit.
- Each episode simulates a delivery agent completing a sequence of at least 5 actions.
- Tracks cumulative statistics across multiple episodes: total episodes run, total reward earned, average reward per episode.
- Agent state (current location, orders delivered, total reward) stored in dictionary and updated after every action.
- End of episode prints full summary: action taken, reward received per step, total episode reward.
"""

import random
import sys
from typing import Dict, Any, List, Tuple


class FoodDeliveryRLSimulator:
    """
    Mini Capstone RL Simulator unifying state tracking, reward formulation,
    episode logging, and cumulative performance statistics.
    """

    ACTIONS = [
        "accept_order",
        "navigate_to_restaurant",
        "pickup_order",
        "navigate_to_customer",
        "mark_delivered",
        "wait_for_order",
        "reject_order"
    ]

    LOCATIONS = [
        "Downtown Core",
        "Westside Suburbs",
        "North Plaza",
        "University Campus",
        "Financial District",
        "Eastside Hub"
    ]

    def __init__(self):
        # Overall global statistics across episodes
        self.total_episodes: int = 0
        self.total_cumulative_reward: float = 0.0

        # Persistent agent state tracking across sessions
        self.agent_state: Dict[str, Any] = {
            "current_location": "Central Hub",
            "orders_delivered": 0,
            "total_reward": 0.0,
            "status": "Idle"
        }

    def _calculate_action_reward(self, action: str) -> Tuple[float, str]:
        """Calculates reward score and descriptive message for a single action."""
        if action == "accept_order":
            return +2.0, "Accepted new order assignment."
        elif action == "navigate_to_restaurant":
            return +1.0, "Navigated to restaurant location."
        elif action == "pickup_order":
            return +3.0, "Food picked up from restaurant kitchen."
        elif action == "navigate_to_customer":
            return +2.0, "En route to customer drop-off point."
        elif action == "mark_delivered":
            # On-time delivery bonus + customer rating simulation
            rating = random.choice([4, 5, 5, 5, 3])
            bonus = 10.0 + rating
            return bonus, f"Delivered successfully on-time! Customer rating: {rating}/5 (+{bonus:.1f})"
        elif action == "wait_for_order":
            return -1.0, "Waited idly for dispatch assignment (-1.0 delay penalty)."
        elif action == "reject_order":
            return -2.0, "Rejected order assignment (-2.0 penalty)."
        else:
            return 0.0, "Neutral action executed."

    def run_episode(self, predefined_actions: List[str] = None) -> float:
        """
        Simulates one full delivery episode containing at least 5 actions.
        """
        self.total_episodes += 1
        episode_num = self.total_episodes
        
        print(f"\n==================================================")
        print(f"       STARTING DELIVERY EPISODE #{episode_num}     ")
        print(f"==================================================")

        # Decide sequence of actions (minimum 5 actions)
        if predefined_actions is None:
            # Generate logical or random sequence of 6 actions
            action_sequence = [
                "accept_order",
                "navigate_to_restaurant",
                "pickup_order",
                "navigate_to_customer",
                "mark_delivered",
                "accept_order",
                "mark_delivered"
            ]
        else:
            action_sequence = predefined_actions

        episode_logs: List[Tuple[int, str, float, float]] = []
        episode_reward: float = 0.0

        for step, action in enumerate(action_sequence, start=1):
            step_reward, detail = self._calculate_action_reward(action)
            episode_reward += step_reward

            # Update persistent agent state dictionary
            new_location = random.choice(self.LOCATIONS)
            self.agent_state["current_location"] = new_location
            self.agent_state["total_reward"] += step_reward
            if action == "mark_delivered":
                self.agent_state["orders_delivered"] += 1
            self.agent_state["status"] = f"Executing {action}"

            # Log step
            episode_logs.append((step, action, step_reward, episode_reward))

            # Display per-step action progress
            print(f"Step {step}: Action = '{action:22s}' | Reward = {step_reward:+5.1f} | Loc = {new_location}")

        # Update global stats
        self.total_cumulative_reward += episode_reward

        # Print full end-of-episode summary table
        print("\n" + "=" * 65)
        print(f"              EPISODE #{episode_num} FULL SUMMARY              ")
        print("=" * 65)
        print("Step | Action Taken            | Step Reward | Cumulative Reward")
        print("-" * 65)
        for s, act, rwd, cum_rwd in episode_logs:
            print(f"  {s:02d} | {act:24s} | {rwd:+11.1f} | {cum_rwd:+17.1f}")
        print("-" * 65)
        print(f"Total Episode Reward Earned : {episode_reward:+.1f} points")
        print(f"Current Agent Location     : {self.agent_state['current_location']}")
        print(f"Total Orders Delivered     : {self.agent_state['orders_delivered']}")
        print("=" * 65 + "\n")

        return episode_reward

    def view_agent_stats(self) -> None:
        """Displays global cumulative statistics across all run episodes."""
        avg_reward = (self.total_cumulative_reward / self.total_episodes) if self.total_episodes > 0 else 0.0

        print("\n" + "=" * 55)
        print("         AGENT GLOBAL PERFORMANCE STATISTICS        ")
        print("=" * 55)
        print(f"  Total Episodes Run        : {self.total_episodes}")
        print(f"  Total Cumulative Reward   : {self.total_cumulative_reward:+.2f}")
        print(f"  Average Reward / Episode  : {avg_reward:+.2f}")
        print(f"  Total Orders Delivered    : {self.agent_state['orders_delivered']}")
        print(f"  Current Agent Location    : {self.agent_state['current_location']}")
        print(f"  Agent Status              : {self.agent_state['status']}")
        print("=" * 55 + "\n")

    def display_menu(self) -> None:
        """Runs the interactive console menu loop."""
        while True:
            print("==================================================")
            print("   FOOD DELIVERY RL CONCEPT SIMULATOR (M12-A1)    ")
            print("==================================================")
            print("  1. Start New Delivery Episode")
            print("  2. View Agent Stats")
            print("  3. Exit")
            print("==================================================")

            try:
                choice = input("Enter option (1-3): ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nExiting simulator. Goodbye!")
                break

            if choice == "1":
                self.run_episode()
            elif choice == "2":
                self.view_agent_stats()
            elif choice == "3":
                print("\nThank you for using the Food Delivery RL Simulator! Exiting...")
                break
            else:
                print("\n[!] Invalid selection. Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    simulator = FoodDeliveryRLSimulator()

    # Check if run with automated argument flag
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        print("Running Simulator in Automated Demo Mode...\n")
        simulator.run_episode()
        simulator.run_episode([
            "accept_order", "navigate_to_restaurant", "pickup_order",
            "navigate_to_customer", "mark_delivered", "wait_for_order"
        ])
        simulator.view_agent_stats()
    else:
        # Launch interactive CLI menu
        simulator.display_menu()
