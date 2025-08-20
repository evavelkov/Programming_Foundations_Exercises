# Programming Exercise 7-7: Exam Grading System
#
# Task: Write a program that grades student exam answers against correct answers.
#
# Requirements:
# 1. Create a main function that handles file reading and grading
# 2. Define correct answers list (20 questions)
# 3. Read student answers from 'student_answers.txt' file
# 4. Compare student answers with correct answers
# 5. Calculate correct and incorrect counts
# 6. Track incorrect question numbers
# 7. Determine pass/fail (15+ correct to pass)
# 8. Display detailed results
# 9. Implement comprehensive exception handling
#
# Functions:
# - main(): handles file operations, grading, and display
#
# Logic:
# - Define correct answers list with 20 answers
# - Use try-except block for error handling
# - Open 'student_answers.txt' file using with statement
# - Read all lines and strip newline characters
# - Compare each student answer with correct answer
# - Count correct and incorrect answers
# - Track question numbers for incorrect answers
# - Determine pass/fail based on correct count
# - Display pass/fail message
# - Display detailed statistics
# - Display list of incorrect questions
#
# File Operations:
# - with open('student_answers.txt', 'r') as input_file: - opens file for reading
# - input_file.readlines() - reads all lines into list
# - line.rstrip('\n') - removes newline characters
#
# Grading Logic:
# - Pass threshold: 15 or more correct answers
# - Track incorrect question numbers (1-20)
# - Compare answers case-sensitive
#
# Exception Handling:
# - FileNotFoundError: 'The file could not be found'
# - IOError: 'There was an IO error.'
# - IndexError: 'There was an indexing error'
# - General exception: 'An error occurred'
#
# Output Format:
# - Pass/Fail message
# - Number of correct/incorrect answers
# - List of incorrect question numbers
#
# Example:
# Congratulations!! You passed the exam.
# Number of questions you answered correctly: 17
# Number of questions you answered incorrectly: 3
# Questions you answered incorrectly: 5, 12, 18
#
# Note: 
# - Program assumes 'student_answers.txt' exists with one answer per line
# - Answers should be in order (question 1 to 20)
# - Uses with statement for automatic file closing
# - Implements comprehensive error handling
