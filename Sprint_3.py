import random
string_list = []                            #temporary list variable - can be ignored
char_list = []                              #contains the random characters
loop_condition = True                       #validation loop boolean

def generate_pass():                        #random password function
    for x in range(12):
        char = random.randint(33, 126)      #generates random integer between 33 and 126 - will be used as ascii values
        char_conv = chr(char)               #converts ascii value to character
        char_list.append(char)              #adds the characters to a list
        string_list.append(char_conv)       #temporary test variable

generate_pass()

sym_cnt = 0                                 #counter for symbols
letter_cnt = 0                              #counter for letters
num_count = 0                               #counter for numbers



while loop_condition:                       #while loop_condition is true
    for y in range(12):
        if (33 <= char_list[y] <= 47) or (58 <= char_list[y] <= 64) or (91 <= char_list[y] <= 96) or (
                123 <= char_list[y] <= 126):
            sym_cnt += 1                    #checks if character is a symbol and increments the symbol counter
        elif 48 <= char_list[y] <= 57:
            num_count += 1                  #checks if character is a number and increments the number counter
        elif (65 <= char_list[y] <= 90) or (97 <= char_list[y] <= 122):
            letter_cnt += 1                 #checks if character is a letter and increments the letter counter
    if (sym_cnt == 0) or (num_count == 0) or (letter_cnt == 0):    #if the string does not contain letters AND numbers AND symbols, then regenerates the passwords until the string has symbols, letters and numbers
        string_list = []
        char_list = []
        generate_pass()
        sym_cnt = 0
        num_count = 0
        letter_cnt = 0
    else:                                  #if the string has letters, symbols and numbers then ends the program.
        loop_condition = False

string = ''
string = string.join(string_list)
print(string)