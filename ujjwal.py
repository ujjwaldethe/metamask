# Input Profit and Weight arrays, and bag capacity from the user
Profit = list(map(int, input("Enter the profit values separated by spaces: ").split()))
Weight = list(map(int, input("Enter the weight values separated by spaces: ").split()))
bagCapacity = int(input("Enter the capacity of the bag: "))

# Number of items
n = len(Profit)

# Initialize the DP table (n+1) x (bagCapacity+1) with zeroes
v = [[0 for _ in range(bagCapacity + 1)] for _ in range(n + 1)]

# Populate the DP table based on the formula
for i in range(1, n + 1):
    for w in range(bagCapacity + 1):
        if Weight[i - 1] <= w:
            # If including the item, take the maximum of either including or excluding the item
            v[i][w] = max(v[i - 1][w], v[i - 1][w - Weight[i - 1]] + Profit[i - 1])
        else:
            # If not including the item, carry forward the value without the item
            v[i][w] = v[i - 1][w]

# The maximum profit that can be carried in the bag is found in v[n][bagCapacity]
print("The maximum profit is:", v[n][bagCapacity])
