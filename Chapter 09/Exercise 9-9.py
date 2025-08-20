# Programming Exercise 9-9: Card Game Simulator
#
# Task: Write a program that simulates a card game between two players.
#
# Requirements:
# 1. Create a main function that handles the card game simulation
# 2. Create a create_deck function that generates a deck of cards
# 3. Create an update_hand_value function that calculates hand values
# 4. Simulate dealing cards to two players
# 5. Determine the winner based on hand values
#
# Functions:
# - main(): handles the card game simulation
# - create_deck(): creates and returns a deck of cards
# - update_hand_value(hand, value, card): updates hand value based on card dealt
#
# Constants:
# - MAX = 21 (winning number of cards)
#
# Logic:
# - Create deck of cards using create_deck() function
# - Initialize hand values for both players
# - Use while loop to continue dealing until either player exceeds MAX
# - For each round:
#   - Deal card to player 1 and update hand value
#   - Deal card to player 2 and update hand value
#   - Display cards dealt to each player
# - Determine winner based on final hand values
# - Display winner or "no winner" if both exceed MAX
#
# Card Deck Creation:
# - Create suits list: ['Spades', 'Hearts', 'Clubs', 'Diamonds']
# - Create special values dictionary for face cards
# - Create numbers list with all card values
# - Use nested loops to create deck dictionary
# - Assign appropriate values to each card
#
# Hand Value Calculation:
# - For non-Ace cards: add card value to hand
# - For Ace cards: add 11 if hand <= 10, otherwise add 1
# - Return updated hand value
#
# Dictionary Operations:
# - deck.popitem() - remove and return random key-value pair
# - dictionary[key] = value - assign value to key
#
# Example:
# Player 1 was dealt King of Hearts
# Player 2 was dealt 7 of Spades
#
# Player 1 was dealt 8 of Diamonds
# Player 2 was dealt Queen of Clubs
#
# Player 1 wins.
#
# Note: 
# - Program simulates standard 52-card deck
# - Uses dictionary to represent deck with card names as keys
# - Handles Ace values intelligently (1 or 11)
# - Continues until one or both players exceed 21
# - Determines winner based on final hand values
