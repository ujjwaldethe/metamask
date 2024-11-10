def fractional_knapsack(capacity, weights, values):
    # Calculate the value-to-weight ratio for each item
    ratios = [v / w for v, w in zip(values, weights)]
    # Sort the items by their value-to-weight ratio in descending order
    sorted_items = sorted(zip(ratios, weights, values), reverse=True)
    # Initialize the result list with zeros
    result = [0.0] * len(weights)
    # Initialize the maximum profit
    max_profit = 0.0
    # Iterate over the sorted items
    for i, (ratio, weight, value) in enumerate(sorted_items):
        # If the item fits completely in the knapsack, include it
        if weight <= capacity:
            result[i] = 1.0
            capacity -= weight
            max_profit += value
        # Otherwise, include a fraction of the item
        else:
            fraction = capacity / weight
            result[i] = fraction
            max_profit += value * fraction
            break
    return result, max_profit
def main():
    # Get user input
    num_items = int(input("Enter the number of items: "))
    weights = []
    values = []
    for i in range(num_items):
        weight = float(input(f"Enter weight of item {i+1}: "))
        value = float(input(f"Enter value of item {i+1}: "))
        weights.append(weight)
        values.append(value)
    capacity = float(input("Enter the knapsack capacity: "))
    # Solve the fractional knapsack problem
    result, max_profit = fractional_knapsack(capacity, weights, values)
    # Print the result
    print("Fractions of each item to include in the knapsack:")
    for i, fraction in enumerate(result):
        print(f"Item {i+1}: {fraction:.2f}")
    print(f"Maximum profit: {max_profit:.2f}")
if __name__ == "__main__":
    main()
