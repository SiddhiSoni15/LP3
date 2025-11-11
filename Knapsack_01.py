def knapsack(values, weights, capacity):
    n = len(values)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Maximum value
    max_value = dp[n][capacity]

    # Backtracking to find items included
    w = capacity
    items_selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            items_selected.append(i)  # item index (1-based)
            w -= weights[i - 1]

    items_selected.reverse()  # To list items in original order

    return max_value, items_selected


# Driver Code
n = int(input("Enter number of items: "))
values = []
weights = []

for i in range(n):
    v = float(input(f"Enter value of item {i+1}: "))
    w = int(input(f"Enter weight of item {i+1}: "))  # weight must be integer
    values.append(v)
    weights.append(w)

capacity = int(input("Enter capacity of knapsack: "))  # must be integer

max_value, items_selected = knapsack(values, weights, capacity)

print(f"\nMaximum value obtained: {max_value:.2f}")
print(f"Items included in the knapsack (by item number): {items_selected}")


# The 0–1 Knapsack Problem is a combinatorial optimization problem.
# Each item has a value and a weight, and we must maximize total value within a given capacity.
# Unlike fractional knapsack, items cannot be divided — they are either taken (1) or not (0).
# The problem is solved using Dynamic Programming, which builds a table of subproblems representing best value for smaller capacities.
# It illustrates the concept of optimal substructure and overlapping subproblems.
# This approach guarantees an optimal solution efficiently compared to exponential recursion.

# Algorithm
# Input n, values[], weights[], and capacity.
# Create DP table of size (n+1) × (capacity+1).
# For each item i and capacity w:
# If item fits:
# dp[i][w] = max(value[i-1] + dp[i-1][w - weight[i-1]], dp[i-1][w])
# Else:
# dp[i][w] = dp[i-1][w]
# dp[n][capacity] gives the maximum value.
# Backtrack to find included items.

# Enter number of items: 4
# Enter value of item 1: 60
# Enter weight of item 1: 10
# Enter value of item 2: 100
# Enter weight of item 2: 20
# Enter value of item 3: 120
# Enter weight of item 3: 30
# Enter capacity: 50
# Maximum value: 220.0
# Items selected: [2, 3]

# Step	                  Time	        Space
# DP Table Construction	O(n × capacity)	O(n × capacity)
# Backtracking	        O(n)	        O(1)
# Total	                O(n × capacity)	O(n × capacity)