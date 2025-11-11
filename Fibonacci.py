# Non-Recursive (Iterative) Fibonacci Function
def fib_non_recursive(n):
    a, b = 0, 1
    print("\nFibonacci Series using Iteration:")
    if n <= 0:
        print("Invalid input")
    elif n == 1:
        print(a)
    else:
        print(a, b, end=" ")
        for i in range(2, n):
            c = a + b
            print(c, end=" ")
            a, b = b, c   # update values


# Recursive Fibonacci Function
def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


# Main Code
n = int(input("Enter the number of terms: "))

# Non-recursive call
fib_non_recursive(n)

# Recursive call
print("\n\nFibonacci Series using Recursion:")
for i in range(n):
    print(fib_recursive(i), end=" ")


# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting from 0 and 1. It demonstrates the concept of recurrence relations in programming.
# The recursive method defines the series using a base case and recursive calls, while the non-recursive (iterative) method uses looping and variable updates.
# Recursion is elegant but inefficient due to repeated calculations (exponential time).
# Iteration is preferred in practice for linear efficiency and constant space usage.
# This program demonstrates both approaches to understand performance differences and step count analysis.

# Algorithm
# Take n as input.
# Non-Recursive:
# Initialize a=0, b=1.
# Print first two numbers.
# Use loop to generate next Fibonacci numbers.
# Recursive:
# Define fib_recursive(n):
# If n <= 1, return n.
# Else return fib_recursive(n−1) + fib_recursive(n−2).
# Print series using both methods.

# Sample I/O
# Enter number of terms: 6
# Fibonacci Series using Iteration:
# 0 1 1 2 3 5
# Fibonacci Series using Recursion:
# 0 1 1 2 3 5

# Method	  Time Complexity	Space Complexity
# Iterative	  O(n)	          O(1)
# Recursive	  O(2ⁿ)	          O(n)