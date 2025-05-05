items = {
"pizza": {"cost": 50, "calories": 300},
"hamburger": {"cost": 40, "calories": 250},
"hot-dog": {"cost": 30, "calories": 200},
"pepsi": {"cost": 10, "calories": 100},
"cola": {"cost": 15, "calories": 220},
"potato": {"cost": 25, "calories": 350}
}

# Greedy approach
def greedy_algorithm(items, budget):

    total_calories = 0
    remaining_budget = budget
    chosen_items = []

    def calorie_per_cost(item):
        name, data = item
        return data["calories"] / data["cost"]

    sorted_items = sorted(
        items.items(), key = calorie_per_cost, reverse = True
    )

    for name, data in sorted_items:
        print(f"{name}: {data['calories'] / data['cost']:.2f} cal per cost unit")
    
    
    for item, details in sorted_items:
        if details["cost"] <= remaining_budget:
            chosen_items.append(item)
            total_calories += details["calories"]
            remaining_budget -= details["cost"]
    return total_calories, budget - remaining_budget, chosen_items


# Dynamic Programming approach
def dynamic_programming(items, budget):
    item_names = list(items.keys())

    # Create a DP table where rows represent up to the i-th item and columns represent budget
    dp_table = [[0 for x in range(budget + 1)] for y in range(len(items) + 1)]

    #Fill DP table
    for i in range(1, len(items) + 1):
        item = item_names[i - 1]
        cost = items[item]['cost']
        calories = items[item]['calories']

        for b in range(budget + 1):
            if cost > b:
                dp_table[i][b] = dp_table[i - 1][b]
            else:
                dp_table[i][b] = max(
                    dp_table[i - 1][b],
                    dp_table[i - 1][b - cost] + calories
                )

    #Backtracking to find chosen items
    chosen_items = []
    temp_budget = budget
    for i in range(len(items), 0, -1):
        if dp_table[i][temp_budget] != dp_table[i - 1][temp_budget]:
            item = item_names[i - 1]
            chosen_items.append(item)
            temp_budget -= items[item]['cost']

    return dp_table[len(items)][budget], budget - temp_budget, chosen_items


if __name__ == '__main__':
    # Execute both algorithms
    budget = 70

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print("Greedy approach:")
    print(f"Total calories: {greedy_result[0]}, Used budget: {greedy_result[1]}, Items: {greedy_result[2]}")

    print("\nDynamic programming approach:")
    print(f"Total calories: {dp_result[0]}, Used budget: {dp_result[1]}, Items: {dp_result[2]}")