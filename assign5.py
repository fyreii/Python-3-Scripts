"""

Teresa Henderson
06/14/2016
CST 100 - Bansal
Assignment 5

Part I:  Function find_longest_word
Part II: Functions allNumAvg, posNumAvg, nonPosAvg

06/15/2015: Corrected output from find_word_length


"""


def take_in_words():
    # open an empty list to put words into
    word_list = []
    # ask the user for words
    user_prompt = input("Please enter a phrase: ")
    # add each word entered to the list
    word_list.append(user_prompt)
    return word_list


# takes "word_list" as an argument as per instructions
def find_longest_word(word_list):
    print("The list of words entered is: ")
    print(word_list)
    # for each word in the list
    for word in word_list:
        # split using space as a delimiter
        chunks = word.split(" ")
        # sort the words by length in reverse
        # so the largest word is first in the list
        chunks.sort(key=len, reverse=True)
        # print the first value in the sorted list
        print("The longest word in the list is: " + chunks[0] + "\n")


# this function takes in a list of numbers until
# the user enters the sentinel value (-9999)
def take_in_numbers():
    # open an empty list to put the user entered numbers into
    num_list = []
    # this is always true for valid data until the sentinel value is reached
    while True:
        # attempt to get valid user input and append to the list
        try:
            add_nums = int(input("Please enter any rational integer (-9999 to end): "))
            num_list.append(add_nums)
        # if input received is anything but an integer, throw an error
        # and ask the user for valid input once more
        except (TypeError, ValueError):
            print("You must enter a rational number!")
        else:
            # if at any point the user enters the sentinel value, the loop ends
            if add_nums == -9999:
                print("The list of all numbers entered is: " + str(num_list[:-1]))
                break
    # we want the list minus the last value (-9999) returned
    return num_list[:-1]


# calculates the average of all numbers in the list passed from
# take_in_numbers()
def all_num_avg(num_list):
    b = 0
    for a in num_list:
        b = b + a
        all_avg = b / len(num_list)
        return all_avg


# calculates and returns the average of all positive numbers
# after it isolates them from the rest of the list
def pos_num_avg(num_list):
    pos_only = []
    e = 0
    for p in num_list:
        if p > 0:
            pos_only.append(p)
    for d in pos_only:
        e = e + d
        pos_avg = e / len(pos_only)
        return pos_avg


# calculates and returns the average of all the negative numbers
# after it isolates them from the rest of the list
def neg_num_avg(num_list):
    neg_only = []
    h = 0
    for n in num_list:
        if n < 0:
            neg_only.append(n)
    for g in neg_only:
        h = h + g
        neg_avg = h / len(neg_only)
        return neg_avg


# this function creates the dictonary with the required output
# receiving values passed from the functions above
def create_dict(all_avg, pos_avg, neg_avg):
    my_dict = {'AllNumAvg': all_avg, 'PosNumAvg': pos_avg, 'NonPosAvg': neg_avg}
    print(my_dict)

# The longest_word function
#find_longest_word(take_in_words())

# The average functions
run_list = take_in_numbers()
create_dict(float(all_num_avg(run_list)), float(pos_num_avg(run_list)), float(neg_num_avg(run_list)))




