import random

def simulate_game(total_lands, black_count, colorless_count, turns=10):
    # Initialize the number of lands in play
    lands_in_play = 0
    black_in_play = 0
    colorless_in_play = 0
    
    # Create the deck with 99 cards
    deck = ['black'] * black_count + ['colorless'] * colorless_count + ['blank'] * (99 - total_lands)
    random.shuffle(deck)
    
    # Draw initial hand and check for valid lands
    while True:
        hand = deck[:7]
        lands_in_hand = hand.count('black') + hand.count('colorless')
        
        # Check if the hand has between 2 and 4 lands
        if 2 <= lands_in_hand <= 4:
            break  # Valid hand, exit the loop
        else:
            # Reshuffle the hand back into the deck and draw a new one
            deck = hand + deck[7:]  # Put the hand back into the deck
            random.shuffle(deck)  # Shuffle the deck again

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
