# Programming Exercise 3-17: Restaurant Selector
#
# Task: Write a program that helps users select a restaurant based on dietary restrictions.
#
# Requirements:
# 1. Ask if anyone in the party is vegetarian (yes/no)
# 2. Ask if anyone in the party is vegan (yes/no)
# 3. Ask if anyone in the party is gluten-free (yes/no)
# 4. Display restaurant choices based on dietary restrictions:
#    - Joe's Gourmet Burgers: only if no vegetarian, vegan, or gluten-free restrictions
#    - Mama's Fine Italian: only if no vegan or gluten-free restrictions
#    - Main Street Pizza: only if no vegan restrictions
#    - Corner Cafe: always available
#    - Chef's Kitchen: always available
# 5. Display "Here are your restaurant choices:" before listing options
#
# Logic:
# - Use boolean variables to track dietary restrictions
# - Use if statements with logical operators (and, not)
# - Always display Corner Cafe and Chef's Kitchen
#
# Example:
# Is anyone in your party a vegetarian? no
# Is anyone in your party a vegan? no
# Is anyone in your party gluten free? no
# Here are your restaurant choices:
# Joe's Gourmet Burgers
# Mama's Fine Italian
# Main Street Pizza
# Corner Cafe
# Chef's Kitchen
