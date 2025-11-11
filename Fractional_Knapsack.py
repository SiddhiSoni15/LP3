# Function to solve fractional knapsack
def fractional_knapsack(values, weights, capacity):
    n = len(values)
    
    # Calculate value-to-weight ratio for each item
    ratio = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    
    # Sort items by ratio in descending order
    ratio.sort(reverse=True, key=lambda x: x[0])
    
    total_value = 0.0
    fractions = []
    
    for r, w, v in ratio:
        if capacity >= w:
            # Take the whole item
            total_value += v
            capacity -= w
            fractions.append((v, w, 1))  # 1 means full item
        else:
            # Take fraction of item
            fraction = capacity / w
            total_value += v * fraction
            fractions.append((v, w, fraction))
            capacity = 0
            break
    
    return total_value, fractions


# Driver Code
n = int(input("Enter number of items: "))
values = []
weights = []

for i in range(n):
    v = float(input(f"Enter value of item {i+1}: "))
    w = float(input(f"Enter weight of item {i+1}: "))
    values.append(v)
    weights.append(w)

capacity = float(input("Enter capacity of knapsack: "))
max_value, fractions_taken = fractional_knapsack(values, weights, capacity)

print(f"\nMaximum value obtained: {max_value:.2f}")
print("\nDetails of items taken (value, weight, fraction taken):")
for item in fractions_taken:
    print(item)


# The Fractional Knapsack Problem is an optimization problem where items can be divided into smaller fractions.
# The goal is to maximize total value within a fixed capacity using a greedy approach — always select the item with the highest value-to-weight ratio first.
# This ensures local optimal choices that lead to a global optimum solution.
# It differs from the 0-1 knapsack, where items must be taken entirely or not at all.
# It is widely used in resource allocation, logistics, and data compression optimization scenarios

# Algorithm
# Input number of items, their values, and weights.
# Calculate value/weight ratio for each item.
# Sort items by this ratio in descending order.
# Initialize total value = 0.
# For each item:
# If it fits, take it fully.
# Else take fractional part until capacity is filled.
# Print maximum total value.

# Enter number of items: 3
# Enter value of item 1: 60
# Enter weight of item 1: 10
# Enter value of item 2: 100
# Enter weight of item 2: 20
# Enter value of item 3: 120
# Enter weight of item 3: 30
# Enter capacity of knapsack: 50
# Maximum value obtained: 240.0

# Step	      Time Complexity	Space Complexity
# Sorting	    O(n log n)	        O(n)
# Selection	       O(n)	            O(1)
# Total	        O(n log n)	        O(n)