My solutions for CS50P problem sets

Coke Machine:
Suppose that a machine sells bottles of Coca-Cola for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
Implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

Vanity Plates:
1. All vanity plates must start with at least two letters.
2. They may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
3. Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be acceptable; AAA22A would not be acceptable. The first number used cannot be a ‘0’.
4. No periods, spaces, or punctuation marks are allowed.
Program prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase.

Outdated:
Implement a program that prompts the user for a date, in month-day-year order, formatted like 9/8/1636 or September 8, 1636. Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.

Guessing Game:
Implement a program that 
- Prompts the user for a level, n. If the user does not input a positive integer, the program should prompt again.
- Randomly generates an integer between 1 and n inclusive, using the random module.
- Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output "Too small!" and prompt the user again.
If the guess is larger than that integer, the program should output "Too large!" and prompt the user again.
If the guess is the same as that integer, the program should output "Just right!" and exit.

Little Professor:
Implement a program that 
- Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program should prompt again.
- Randomly generates 10 math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 
 digits.
- Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
- Ultimately output the user’s score: the number of correct answers out of 10.
Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:
