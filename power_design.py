# 1. Name:
#      Emily McGovern
# 2. Assignment Name:
#      Lab 13: Power
# 3. Assignment Description:
#      This program will take a json list of numbers. Then it will ask
#      the user what sub-array they want to find the average in. Next the program
#      Will use the sub-array the user gave and find the highest average out of the 
#      whole list of numbers.
# 4. What was the hardest part? Be as specific as possible.
#      The pseudocode helped a lot with coding the entire program. I can see how
#      pseudocode helps build programs and makes it easier to code them. I also
#      found it interesting that I thought this program was easier than others. I think 
#      the reason behind it being easier is because I have gotten more comfortable writing code
#      and the last thing we coded was one of the more challenging programs I have coded. I am still 
#      struggling with coming up with different types of asserts. It took me awhile to come up with 
#      assert 0 <= remove_num < len(number_list). I believe that if I practice more with asserts
#      I will be able to come up with better ones for my future programs. 
# 5. How long did it take for you to complete the assignment?
#      It took me about an hour and a half to complete the assignment.

# Importing json to read json files.
import json

# Asking the user for which file they would like to use.
filename = input("Which File would you like to use? ")

# Opening the file the user asked for and seeing if the file is true.
try:
    with open(f'C:/Users/lover/OneDrive/Documents/BYUI/CSE 130/power_design/{filename}', "r") as file:
        text_numbers = file.read()
        json_data = json.loads(text_numbers)

        # Adding an assert to check if file has array in it.
        assert "array" in json_data, "json_data does not contain 'array'."
        number_list = json_data["array"]

        # Asking the user for the sub-array.
    sub_array = int(input("Please enter the sub-array: "))

    # If the sub-array is greater than the list of numbers, then the program will end.
    if sub_array > len(number_list):
        print("The sub-array is greater than the length number of numbers in the file.")

    # If the sub-array is smaller than the list of numbers, then program will continue.
    else:

        # Asserts making sure everything is correct type of int or list.
        assert type(number_list) == list
        assert type(sub_array) == int

        # Stating the total from the number_list.
        total = number_list[0]

        # Checking to make sure the sub-array is greater than or equal to 0.
        assert sub_array >= 0

        # Adding the number in the range of the sub-array to the total.
        for number in range(1, sub_array):
        
            # Making sure the number is less than the length of the list.
            assert 0 <= number < len(number_list)

            total += number_list[number]
            assert total > 0

        # Changing total into largest_sum.
        largest_sum = total

        # Going over the rest of the numbers in the number_list subtracted by sub-array.
        for remove_num in range(len(number_list) - sub_array):

            # Making sure remove_num is less than the number_list and greater than 0.
            assert 0 <= remove_num < len(number_list)

            # Adding remove_num and sub_array.
            add_number = remove_num + sub_array

            # Making sure add_num is less than length of number_list and greater than 0.
            assert 0 <= add_number < len(number_list)

            # Getting the total from number_list.
            total = total - number_list[remove_num] + number_list[add_number]
            assert total > 0

            # If the new total is greater than largest_sum, then total become largest_sum.
            if total > largest_sum:

                # Making sure the total is an integer.
                assert type(total) == int
                largest_sum = total

        # Dividing the largest_sum by the sub-array.
        largest_sum = largest_sum / sub_array
        assert largest_sum > 0

        # Printing the largest_sum to the user.
        print(f"Here is the largest sum: {round(largest_sum, 2)}")

# If there is no file, this message will fire.
except Exception as no_file:
    print(f"Error loading file: {no_file}")
