# 2.Using a filter for a list of words:

# Create a word list containing the following games: "V Auto Theft Grand ","Fortnite", "The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"

word_list = ["V Auto Theft Grand ","Fortnite", "The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"]
print(f"The original list is: {word_list}")

# Now use filter and lambda to get from the list:
# a. Only from stars whose name is longer than 8 letters

greatereight = list(filter(lambda x: len(x.strip()) > 8, word_list)) #.strips removes the empty spaces, then we will check for the elements of the list with a length greater than 8.
print(f"The items with a length greater then 8 are: {greatereight}")

def greatereight_list(word_list):
    new_list = [] # Creation of a new list to store the results
    for x in word_list: # check the items on the list
        if len(x) > 8: # check if the length is greater than 8
            new_list.append(x) #add the results to a new list
    return new_list #returns a new list

print(f"The second option for printing the list is: {greatereight_list(word_list)}")

# b. Only from stars whose name starts with the letter F
#Option1
def filter_letter(word_list, letter):
    letter = letter.lower() #makes the letters lowercase to compare them.
    return [item for item in word_list if item.lower().startswith(letter)] #converts the letters to lowercase to compare and check the words for the ones that start with the provided criteria.
filtered_list = filter_letter(word_list, "F") #creates a new list filtering only the ones that start with "F"
print(f"The words that start with F are: {filtered_list}")

#Option2
filteredl = list(filter(lambda item: item.lower().startswith("f"), word_list))
print(f"The words that start with F on the second option are: {filteredl}")

# c. Only items whose name contains exactly 2 words

#Option1
def two_words(word_list):
    return [item for item in word_list if len(item.split()) == 2]
list_two_items = two_words(word_list)
print(f" The items that contain two words are: {list_two_items}")

#Option2

list_two_words = list(filter(lambda item: len(item.split()) == 2, word_list))
print(f" The items using lambda option and that contain two words are: {list_two_words}")

# d. Only from clouds whose name contains the letter V

#Option1
def filter_lv(word_list, lv):
    letter = lv.lower() #makes the letters lowercase to compare them.
    return [item for item in word_list if item.lower().startswith(lv)] #converts the letters to lowercase to compare and check the words for the ones that start with the provided criteria.
filt_list = filter_letter(word_list, "V") #creates a new list filtering only the ones that start with "F"
print(f"The words that start with V are: {filt_list}")

#Option2
filtl = list(filter(lambda item: item.lower().startswith("v"), word_list))
print(f"The words that start with V on the second option are: {filtl}")