"""
Module 12 - Reinforcement Learning (Assessment M12-A1)
Section B: Practical Coding Tasks
Task 1: Delivery Reward Function

Requirements:
- Define calculate_reward(delivery_time, is_on_time, customer_rating)
- Award +10 points if is_on_time is True; deduct -5 points if False.
- Add customer_rating (integer 1-5) directly to reward total.
- Print final reward with descriptive message and test with at least three combinations.
"""

def calculate_reward(delivery_time: float, is_on_time: bool, customer_rating: int) -> float:
    """
    Calculates and returns a reward score for a food delivery agent based on
    the outcome of a single delivery action.
    """
    reward = 0.0
    
    # Evaluate punctuality
    if is_on_time:
        reward += 10.0
        punctuality_status = "On Time (+10)"
    else:
        reward -= 5.0
        punctuality_status = "Delayed (-5)"
        
    # Add customer rating directly
    reward += float(customer_rating)
    
    # Descriptive log output
    print(f"--- Delivery Evaluation ---")
    print(f"Delivery Time   : {delivery_time} mins")
    print(f"Punctuality     : {punctuality_status}")
    print(f"Customer Rating : {customer_rating}/5 (+{customer_rating})")
    print(f"Final Reward    : {reward:+.1f} points\n")
    
    return reward


if __name__ == "__main__":
    print("==================================================")
    print("      TASK 1: DELIVERY REWARD FUNCTION TEST       ")
    print("==================================================\n")
    
    # Test Case 1: Fast & On-Time Delivery with Excellent Rating
    print("Test 1: Fast delivery, on-time, 5-star rating")
    r1 = calculate_reward(delivery_time=18.5, is_on_time=True, customer_rating=5)
    
    # Test Case 2: On-Time Delivery with Average Rating
    print("Test 2: Standard delivery, on-time, 3-star rating")
    r2 = calculate_reward(delivery_time=28.0, is_on_time=True, customer_rating=3)
    
    # Test Case 3: Late Delivery with Poor Rating
    print("Test 3: Severe delay, late delivery, 1-star rating")
    r3 = calculate_reward(delivery_time=52.0, is_on_time=False, customer_rating=1)
    
    # Test Case 4: Late Delivery with Decent Rating (Bonus Test)
    print("Test 4: Slightly delayed delivery, late delivery, 4-star rating")
    r4 = calculate_reward(delivery_time=35.0, is_on_time=False, customer_rating=4)
    
    print("All tests completed successfully!")
