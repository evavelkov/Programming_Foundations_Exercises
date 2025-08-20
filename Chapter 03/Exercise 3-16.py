# Programming Exercise 3-16: WiFi Troubleshooter
#
# Task: Write a program that guides users through troubleshooting a WiFi connection.
#
# Requirements:
# 1. Display the first troubleshooting step: "Reboot the computer and try to connect."
# 2. Ask if that fixed the problem
# 3. If yes, display "Glad to be of help."
# 4. If no, proceed to next step: "Reboot the router and try to connect."
# 5. Continue through the troubleshooting steps:
#    - Step 3: Check cables between router and modem
#    - Step 4: Move router to new location
#    - Step 5: Get a new router
# 6. After each step, ask if the problem is fixed and respond appropriately
#
# Logic:
# - Use nested if-else statements
# - Each step depends on the previous step not working
# - Display "Glad to be of help." when any step works
#
# Example interaction:
# Reboot the computer and try to connect.
# Did that fix the problem? no
# Reboot the router and try to connect.
# Did that fix the problem? yes
# Glad to be of help.
