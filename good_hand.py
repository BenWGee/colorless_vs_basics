import math

def binomial_coefficient(n, k):
    """Calculate the binomial coefficient C(n, k) = n! / (k! * (n - k)!)"""
    if k > n or k < 0:
        return 0
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def probability_of_specific_lands(total_cards, total_lands, hand_size, desired_lands):
    total_blanks = total_cards - total_lands
    
    # Total ways to choose 'hand_size' cards from 'total_cards'
    total_hands = binomial_coefficient(total_cards, hand_size)
    
    # Calculate the number of hands with exactly 'desired_lands'
    favorable_hands = (binomial_coefficient(total_lands, desired_lands) *
                       binomial_coefficient(total_blanks, hand_size - desired_lands))
    
    # Probability of drawing a hand with 'desired_lands'
    probability = favorable_hands / total_hands if total_hands > 0 else 0
    return probability

# Example usage
total_cards = 99
total_lands = 42
hand_size = 7

# Calculate probabilities for different desired land counts
for desired_lands in range(2, 5):  # For 2, 3, and 4 lands
    prob = probability_of_specific_lands(total_cards, total_lands, hand_size, desired_lands)
    print(f"Probability of a hand with exactly {desired_lands} lands: {prob:.4f}")
