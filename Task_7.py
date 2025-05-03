import random
from collections import Counter

# Create a loop to simulate rolling two six-sided dice.
num_rolls = 1000000
results = []

for _ in range(num_rolls):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    results.append(total)

# Count frequency of each sum
frequencies = Counter(results)

# Calculate empirical probabilities
probabilities = {total: count / num_rolls for total, count in frequencies.items()}

theoretical = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36,
}

print(f"{'Sum':>3} | {'Empirical':>10} | {'Theoretical':>11}")
print("-" * 32)
for i in range(2, 13):
    e = probabilities.get(i, 0)
    t = theoretical.get(i, 0)
    print(f"{i:>3} | {e:>10.4f} | {t:>11.4f}")
