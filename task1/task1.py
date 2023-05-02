#this to define new function called replace_char_at_position
def replace_char_at_position(word, postion, new_char):
    if len(new_char) != 1:
        return "Error : the character must be one character only "
    # this if condition to check the length of string and the postion the user enter if it larger than string length

    if postion >= len(word):
        return "Error: the position is out of rangfor the given string."
    #word[:postion] : this to get string until the postion the user enter
    #+ new_char : this to add new charcter after the position the user enter
    #+  word[postion+1:] : this to complete the string remaining
    return word[:postion] + new_char + word[postion+1:]
    #this another solution
    #word[postion].replace(word[postion], new_char, 1) : this to replace the charcter in that postion to new charcater
    #return word[:postion] + word[postion].replace(word[postion], new_char, 1) + word[postion + 1:]

#this to make user enter the string
word = input("Enter a string: ")

#this take postion from user
pos = int(input("Enter the position of the character to replace: "))

#this take new character from user
new_char = input("Enter the new character: ")

# this to call function  replace_char_at_position that change charcter at specific position
new_s = replace_char_at_position(word, pos, new_char)

#this to print new value of word
print(new_s)