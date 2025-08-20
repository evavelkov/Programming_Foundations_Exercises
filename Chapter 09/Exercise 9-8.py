# Programming Exercise 9-8: Vegetable Inventory Management System
#
# Task: Write a program that manages a vegetable inventory using pickle files.
#
# Requirements:
# 1. Import the pickle module
# 2. Create a main function that handles the menu system
# 3. Create multiple functions for different operations (display, add, change, delete)
# 4. Implement persistent storage using pickle files
# 5. Provide a menu-driven interface for inventory management
#
# Functions:
# - main(): handles menu system and calls appropriate functions
# - load_data(): loads data from pickle file or creates empty dictionary
# - save_data(data): saves data to pickle file
# - get_user_choice(): displays menu and gets user choice
# - display(data): displays current vegetables and prices
# - add(data): adds new vegetable and price
# - change(data): changes price of existing vegetable
# - delete(data): deletes vegetable and price
#
# Constants:
# - DISPLAY = 1, ADD = 2, CHANGE = 3, DELETE = 4, QUIT = 5
# - FILENAME = 'vegetables.dat'
#
# Logic:
# - Load existing data from pickle file (or create empty dictionary)
# - Display menu and get user choice
# - Use while loop to continue until user quits
# - Call appropriate function based on user choice:
#   - Display: show all vegetables and prices
#   - Add: get vegetable name and price, add to dictionary
#   - Change: get vegetable name and new price, update dictionary
#   - Delete: get vegetable name, remove from dictionary
# - Save data to pickle file when quitting
#
# Pickle Operations:
# - pickle.load(file) - load data from pickle file
# - pickle.dump(data, file) - save data to pickle file
# - open(filename, 'rb') - open file for binary reading
# - open(filename, 'wb') - open file for binary writing
#
# Dictionary Operations:
# - key in dictionary - check if key exists
# - dictionary[key] = value - add or update key-value pair
# - del dictionary[key] - remove key-value pair
# - dictionary.items() - get all key-value pairs
#
# Example:
# Menu
# ----------------------------------------
# 1. Display current vegetables and prices
# 2. Add a vegetable and price
# 3. Change the price of an existing vegetable
# 4. Delete a vegetable and price
# 5. Quit the program
#
# Enter your choice: 1
# Current vegetables and prices:
#  - Carrots ($1.50)
#  - Broccoli ($2.00)
#
# Note: 
# - Program uses pickle for persistent data storage
# - Handles file I/O errors gracefully
# - Validates user input for menu choices
# - Provides clear feedback for all operations
# - Maintains data between program runs
