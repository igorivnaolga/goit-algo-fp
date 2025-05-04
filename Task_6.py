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
        while details["cost"] <= remaining_budget:
            chosen_items.append(item)
            total_calories += details["calories"]
            remaining_budget -= details["cost"]
    return total_calories, budget - remaining_budget, chosen_items

total_cal, spent, chosen = greedy_algorithm(items, 55)
print(f"Total calories: {total_cal}")
print(f"Total money spent: {spent}")
print(f"Chosen items: {chosen}")