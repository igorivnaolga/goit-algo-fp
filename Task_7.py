import random
import matplotlib.pyplot as plt
from collections import Counter

def simulate_dice_rolls(num_rolls):
    # Simulate rolling two six-sided dice
    results = []
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        results.append(total)

    # Count frequencies
    frequencies = Counter(results)

    # Calculate empirical probabilities
    probabilities = {total: count / num_rolls for total, count in frequencies.items()}
    return probabilities

def plot_probabilities(probabilities, num_rolls):
    # Theoretical probabilities
    theoretical = {
        2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
        8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
    }

    sums = range(2, 13)
    empirical_probs = [probabilities.get(s, 0) for s in sums]
    theoretical_probs = [theoretical[s] for s in sums]

    # Plotting
    x = list(sums)
    bar_width = 0.4
    plt.figure(figsize=(10, 6))

    plt.bar([i - bar_width/2 for i in x], empirical_probs, width=bar_width, label='Empirical', color='skyblue')
    plt.bar([i + bar_width/2 for i in x], theoretical_probs, width=bar_width, label='Theoretical', color='orange')

    plt.xlabel('Sum of Dice Rolls')
    plt.ylabel('Probability')
    plt.title(f'Empirical vs Theoretical Probabilities ({num_rolls} rolls)')
    plt.xticks(x)

    # Show percentage values
    for i in range(len(x)):
        plt.text(x[i] - bar_width/2, empirical_probs[i] + 0.004,
                 f"{empirical_probs[i]*100:.2f}%", ha='center',
                 fontsize=6, color='blue')  
        plt.text(x[i] + bar_width/2, theoretical_probs[i] + 0.004,
                 f"{theoretical_probs[i]*100:.2f}%", ha='center',
                 fontsize=6, color='darkorange') 
    plt.legend()
    plt.ylim(0, max(empirical_probs + theoretical_probs) + 0.05)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    for rolls in [100, 1000, 10000, 100000, 1000000]:
        probabilities = simulate_dice_rolls(rolls)
        plot_probabilities(probabilities, rolls)