###
# Question 4 (20 points)
# You are given a set of items, each with a weight and a value. Your goal is to maximize the total value of items included in a knapsack with a fixed capacity. You can take a fraction of an item if needed.
# Input:
# •	An array of items, where each item is represented by a weight and a value.
# •	The maximum capacity of the knapsack.
# Output:
# •	The maximum total value that can be obtained by selecting items optimally.
# •	The fraction of each item selected.
# Write a program or Pseudocode to solve the fractional knapsack problem using a greedy algorithm. You need to properly define all notations and variables that you use in the algorithm. At the end, you need to output the maximum total value and the fraction of each item selected.
# Constraints: The input array of items will have at least one item. The weight and value of each item are positive integers. The maximum capacity of the knapsack is a positive integer.

WEIGHT_INDEX = 0
VALUE_INDEX = 1
DENSITY_INDEX = 2

def fractional_knapsack(items: [int, ...], capacity: int):
    # print(items[0])
    densities_and_items = [(items[count_item][WEIGHT_INDEX] for count_item, item in enumerate(items)), (items[i][VALUE_INDEX] for i in enumerate(items)), (0 for i in enumerate(items))]
    print(densities_and_items)
    densities = [0 for i in enumerate(items)]
    for count_item, item in enumerate(items):
        # densities_and_items[count_item][DENSITY_INDEX] = item[VALUE_INDEX] / item[WEIGHT_INDEX]
        pass
    # densities_and_items = sorted(densities_and_items, reverse=True)


items = [(5, 50), (10, 60), (20, 140), (15, 60), (25, 120)]
capacity = 30
# print(items[0][WEIGHT_INDEX])
fractional_knapsack(items, capacity)
