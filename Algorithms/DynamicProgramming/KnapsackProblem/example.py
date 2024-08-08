from knapsack import Knapsack

capacity = 50
weights = [10, 20, 30]
values = [60, 100, 120]

knapsack = Knapsack(capacity, weights, values)

print("Maximum value in Knapsack:", knapsack.solve())
print("Selected item indices:", knapsack.get_selected_items())
