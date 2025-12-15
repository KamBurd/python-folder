#Kameron Burden
# Constants
ROWS = 3    # of rows
COLS = 3    # of columns
MIN = 1     # Value of smallest number
MAX = 9     # Value of largest number


wins = 0 #Win tracker
loses = 0#Lose tracker
#Asks the user for the numbers used for the square, prompts them to enter numbers 1-9
print("A Lo Shu Magic Square is a grid with 3 rows and 3 columns, in order for it to be classified as such, the sum of each row, column, and diagonal, must all add up to the same number.")
print("An example of this is the numbers 294753618 counting as a Lo Shu Magic Square due to each row, column, and diagonal adding up to the number 15. The numbers must also only be numbers 1-9")
def ask4num():
    number1, number2, number3, number4, number5, number6, number7, number8, number9 = input("Enter 9 numbers ranging only from 1-9 to see if they classify as a Lo Shu Magic Square. Entering the number 0 will cause an error ")
    return number1, number2, number3, number4, number5, number6, number7, number8, number9
num1, num2, num3, num4, num5, num6, num7, num8, num9 = ask4num()
#Used for when the prompted user enters numbers like 0, so it prompts them
# to enter the numbers again, but without zero.
while(int(num1)) > 10 or (int(num1))< 1:
    print("EVERY number has to be ranging from  1 to 9, NO ZEROES")
    num1, num2, num3, num4, num5, num6, num7, num8, num9= ask4num()
while(int(num2)) > 10 or (int(num2))< 1:
    print("EVERY number has to be ranging from  1 to 9, NO ZEROES")
    num1, num2, num3, num4, num5, num6, num7, num8, num9= ask4num()
while(int(num3)) > 10 or (int(num3))< 1:
    print("EVERY number has to be ranging from  1 to 9, NO ZEROES")
    num1, num2, num3, num4, num5, num6, num7, num8, num9= ask4num()
while(int(num4)) > 10 or (int(num4))< 1:
    print("EVERY number has to be ranging from  1 to 9, NO ZEROES")
    num1, num2, num3, num4, num5, num6, num7, num8, num9= ask4num()
while(int(num5)) > 10 or (int(num5))< 1:
    print("EVERY number has to be ranging from  1 to 9, NO ZEROES")
    num1, num2, num3, num4, num5, num6, num7, num8, num9= ask4num()
while(int(num6)) > 10 or (int(num6))< 1:
    print("EVERY number has to be ranging from  1 to 9, NO ZEROES")
    num1, num2, num3, num4, num5, num6, num7, num8, num9= ask4num()
while(int(num7)) > 10 or (int(num7))< 1:
    print("EVERY number has to be ranging from  1 to 9, NO ZEROES")
    num1, num2, num3, num4, num5, num6, num7, num8, num9= ask4num()
while(int(num8)) > 10 or (int(num8))< 1:
    print("EVERY number has to be ranging from  1 to 9, NO ZEROES")
    num1, num2, num3, num4, num5, num6, num7, num8, num9= ask4num()
while(int(num9)) > 10 or (int(num9))< 1:
    print("EVERY number has to be ranging from  1 to 9, NO ZEROES")
    num1, num2, num3, num4, num5, num6, num7, num8, num9= ask4num()

#Main function
    
def main():
    #Global variables used to track wins and loses
    global wins
    global loses


    # Creates a 2D list.
    
    test_list = [ [num1, num2, num3],
                  [num4, num5, num6],
                  [num7, num8, num9] ]
    
    # Displays list in a row and column format.
    display_square_list(test_list)
    check_range(test_list)
    check_unique(test_list)
    check_row_sum(test_list)
    check_col_sum(test_list)
    check_diag_sum(test_list)
    # Determines if list is a Lo Shu magic square.
    if is_magic_square(test_list):
        
        print('This is a Lo Shu magic square.')
        #Increases Win counter if function is true
        wins +=1
        print("Your score is ", wins,"win(s), and ", loses, "lose(s)")
    else:
        print('This is not a Lo Shu magic square.')
        #Increases Lose counter if function is false
        loses +=1
        print("Your score is ", wins,"win(s), and ", loses, "lose(s)")
        
# The display_square_list function accepts a 2D
# list as an argument, and displays the list's values in row
# column format.
def display_square_list(value_list):
    for r in range(ROWS):
        for c in range(COLS):
            print(value_list[r][c], end=' ')
        print()

# The is_magic_square function accepts a two-dimensional
# list as an argument, and returns True if the list meets
# all the requirements of a magic square. Otherwise it
# returns False.
def is_magic_square(value_list):
    # Set status to False.
    status = False
    
    # Call functions and store their return values.
    is_in_range = check_range(value_list)
    is_unique = check_unique(value_list)
    is_equal_rows = check_row_sum(value_list)
    is_equal_cols = check_col_sum(value_list)
    is_equal_diag = check_diag_sum(value_list)

    # Determine if list meets all the requirements.
    if is_in_range and \
       is_unique and \
       is_equal_rows and \
       is_equal_cols and \
       is_equal_diag:
        
        # If it does, the status is True.
        status = True

    # Returns status.
    return status

# The check_range function accepts a two-dimensional
# list as an argument, and returns True if the values
# in the list are within the specified range. Otherwise,
# it returns False.
def check_range(value_list):
    # Status starts as true.
    status = True

    # Looks through all values in list.
    for r in range(ROWS):
        for c in range(COLS):
            # Determine if any of the values
            # are out of range.
            if int(value_list[r][c]) < MIN or \
               int(value_list[r][c]) > MAX:
                # If so, set status to False.
                status = False
                
    # Returns status.
    return status

# The check_unique function accepts a two-dimensional
# list as an argument, and returns True if the values
# in the list are unique. Otherwise, it returns False.
def check_unique(value_list):
    # Starts as true.
    status = True
    # Initialize the search value.
    search_value = MIN
    # Initialize the counter to zero.
    count = 0

    # Perform the search while the maximum value
    # has not been reached, and the values are
    # unique.
    while search_value <= MAX and status == True:
        # Step through all the values in the list.
        for r in range(ROWS):
            for c in range(COLS):
                 # Determine if the current value equals
                # the search value.
                if int(value_list[r][c]) == search_value:
                    # If so, increments counter.
                    count += 1
                # Determine if the counter variable is
                # Greater than one.
                if count > 1:
                    # If so, the value is not unique.
                    # Set status to False.
                    status = False
        # Increments search value.
        search_value += 1
        # Resets counter variable.
        count = 0
        
    # Returns status.
    return status

# The check_row_sum function accepts a two-dimensional
# list as an argument, and returns True if the sum of
# the values in each of the list's rows are equal.
# Otherwise, it returns False.
def check_row_sum(value_list):
    # Initialize status to True.
    status = True

    # Calculate the sum of the values in the first row.
    sum_row_0 = int(value_list[0][0]) + \
                int(value_list[0][1]) + \
                int(value_list[0][2])

    # Calculate the sum of the values in the second row.
    sum_row_1 = int(value_list[1][0]) + \
                int(value_list[1][1]) + \
                int(value_list[1][2])

    # Calculate the sum of the values in the third row.
    sum_row_2 = int(value_list[2][0]) + \
                int(value_list[2][1]) + \
                int(value_list[2][2])

    # Determine if the sum of any of the rows is not equal.
    if (sum_row_0 != sum_row_1) or \
       (sum_row_0 != sum_row_2) or \
       (sum_row_1 != sum_row_2):
        # If so, set the status to False
        status = False

    # Return the status.
    return status




        
# The check_col_sum function accepts a 2D
# list as an argument, and returns as True if the sum of
# the values in each of the list's columns are equal.
# Otherwise, it comes back False.
def check_col_sum(value_list):
    # Makes the status of the function start off as true.
    status = True

    # Calculate sum of the values in 1st column.
    sum_col_0 = int(value_list[0][0]) + \
                int(value_list[1][0]) + \
                int(value_list[2][0])

    # Calculate sum of the values in 2nd column.
    sum_col_1 = int(value_list[0][1]) + \
                int(value_list[1][1]) + \
                int(value_list[2][1])

    # Calculates sum of the values in 3rd column.
    sum_col_2 = int(value_list[0][2]) + \
                int(value_list[1][2]) + \
                int(value_list[2][2])

    # Determines if the sum of any of the columns
    # isn't equal.
    if (sum_col_0 != sum_col_1) or \
       (sum_col_0 != sum_col_2) or \
       (sum_col_1 != sum_col_2):
        # If so, set the status to False
        status = False

    # Return the status.
    return status

# The check_diag_sum function accepts a two-dimensional
# list as an argument, and returns True if the sum of
# the values in each of the list's diagonals are equal.
# Otherwise, it returns False.
def check_diag_sum(value_list):
    # Initialize status to True.
    status = True

    # Calculate the sum of the values in the first diagonal.
    sum_diag_0 = int(value_list[0][0]) + \
                 int(value_list[1][1]) + \
                 int(value_list[2][2])

    # Calculate the sum of the values in the second diagonal.
    sum_diag_1 = int(value_list[2][0]) + \
                 int(value_list[1][1]) + \
                 int(value_list[0][2])

    # Determine if the sum of any of the columns
    # is not equal.
    if sum_diag_0 != sum_diag_1:
        status = False

    # Returns status.
    return status


#Ending message 
def end():
    print("Thanks for playing!")

    
# The main function.
main()
#Used for when the prompted user enters numbers like 0, so it prompts them to enter the numbers again, but without zero.
replay = input("Would you like to play again? Press y for yes, and n for no.")
#Used to repeat the input for the user to start the game again with their answer being "yes"
while replay == 'y':
    num1, num2, num3, num4, num5, num6, num7, num8, num9 = ask4num()
    while(int(num1)) > 10 or (int(num1))< 1:
        print("EVERY number has to be ranging from  1 to 9, NO ZEROES")
        num1, num2, num3, num4, num5, num6, num7, num8, num9= ask4num()
    while(int(num2)) > 10 or (int(num2))< 1:
        print("EVERY number has to be ranging from  1 to 9, NO ZEROES")
        num1, num2, num3, num4, num5, num6, num7, num8, num9= ask4num()
    while(int(num3)) > 10 or (int(num3))< 1:
        print("EVERY number has to be ranging from  1 to 9, NO ZEROES")
        num1, num2, num3, num4, num5, num6, num7, num8, num9= ask4num()
    while(int(num4)) > 10 or (int(num4))< 1:
        print("EVERY number has to be ranging from  1 to 9, NO ZEROES")
        num1, num2, num3, num4, num5, num6, num7, num8, num9= ask4num()
    while(int(num5)) > 10 or (int(num5))< 1:
        print("EVERY number has to be ranging from  1 to 9, NO ZEROES")
        num1, num2, num3, num4, num5, num6, num7, num8, num9= ask4num()
    while(int(num6)) > 10 or (int(num6))< 1:
        print("EVERY number has to be ranging from  1 to 9, NO ZEROES")
        num1, num2, num3, num4, num5, num6, num7, num8, num9= ask4num()
    while(int(num7)) > 10 or (int(num7))< 1:
        print("EVERY number has to be ranging from  1 to 9, NO ZEROES")
        num1, num2, num3, num4, num5, num6, num7, num8, num9= ask4num()
    while(int(num8)) > 10 or (int(num8))< 1:
        print("EVERY number has to be ranging from  1 to 9, NO ZEROES")
        num1, num2, num3, num4, num5, num6, num7, num8, num9= ask4num()
    while(int(num9)) > 10 or (int(num9))< 1:
        print("EVERY number has to be ranging from  1 to 9, NO ZEROES")
        num1, num2, num3, num4, num5, num6, num7, num8, num9= ask4num()
    main()
    replay = input("Would you like to play again? Press y for yes, and n for no.")
#Ends the program if the answer is "no"
if replay == 'n':
    end()
