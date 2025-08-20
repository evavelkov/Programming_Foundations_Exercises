# Programming Exercise: Personal Web Page Generator
#
# Task: Write a program that generates a personal HTML web page based on user input.
#
# Requirements:
# 1. Create a main function that collects user input and calls HTML generation functions
# 2. Create a write_html function that writes the main HTML structure
# 3. Create a write_head function that writes the HTML head section
# 4. Create a write_body function that writes the HTML body section
# 5. Collect user's name and self-description
# 6. Generate a complete HTML file named 'my_page.html'
#
# Functions:
# - main(): collects user input and calls write_html()
# - write_html(html_file, name, description): writes main HTML structure
# - write_head(html_file): writes HTML head section
# - write_body(html_file, name, description): writes HTML body section
#
# Logic:
# - Get user's name from input
# - Get user's self-description from input
# - Open 'my_page.html' file for writing using with statement
# - Call write_html function with file object and user data
# - In write_html function:
#   - Write opening <html> tag
#   - Call write_head function
#   - Call write_body function
#   - Write closing </html> tag
#
# HTML Structure:
# - <html> opening and closing tags
# - <head> section with title
# - <body> section with centered name and description
# - Use <center>, <h1>, <hr /> tags for formatting
#
# File Operations:
# - with open('my_page.html', 'w') as html_file: - opens file for writing
# - html_file.write() - writes HTML content
#
# HTML Elements:
# - <title>My Personal Web Page</title>
# - <center><h1>[name]</h1></center>
# - <hr /> for horizontal rules
# - [description] in body
#
# Example:
# Enter your name: John Doe
# Describe yourself: I am a computer science student who loves programming.
# (Creates my_page.html with complete HTML structure)
#
# Note: 
# - Program creates 'my_page.html' file or overwrites existing file
# - Generates valid HTML structure
# - Uses with statement for automatic file closing
# - Creates a simple but complete web page
