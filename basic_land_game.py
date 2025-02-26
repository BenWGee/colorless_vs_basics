import random

def average_lands(total_lands, black_count, colorless_count, simulations=10000):
    total_black = 0
    total_colorless = 0
    
    for _ in range(simulations):
        black, colorless = simulate_game(total_lands, black_count, colorless_count)
        total_black += black
        total_colorless += colorless
    
    avg_black = total_black / simulations
    avg_colorless = total_colorless / simulations
    
    return avg_black, avg_colorless

def simulate_game(total_lands, black_count, colorless_count, turns=10):
    # Initialize the number of lands in play
    lands_in_play = 0
    black_in_play = 0
    colorless_in_play = 0
    
    # Create the deck with 99 cards
    deck = ['black'] * black_count + ['colorless'] * colorless_count + ['blank'] * (99 - total_lands)
    random.shuffle(deck)
    
    # Draw initial hand
    hand = deck[:7]
    lands_in_hand = hand.count('black') + hand.count('colorless')
    
    # Play lands for the number of turns
    for turn in range(turns):
        if lands_in_hand > 0:
            # Play one land from hand
            lands_in_play += 1
            if hand[0] == 'black':
                black_in_play += 1
            else:
                colorless_in_play += 1
            
            # Remove the played land from hand
            hand.pop(0)
            lands_in_hand -= 1
            
            # Draw a new card from the deck if available
            if len(deck) > 7:
                hand.append(deck[7])
                lands_in_hand += (hand[-1] == 'black') + (hand[-1] == 'colorless')
                deck.pop(7)
    
    return black_in_play, colorless_in_play

# Example usage
total_lands = 42
black_count = 20
colorless_count = 22
avg_black, avg_colorless = average_lands(total_lands, black_count, colorless_count)
print(f"Average black lands in play: {avg_black}")
print(f"Average colorless lands in play: {avg_colorless}")

