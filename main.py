def encode(data):
    result = ""
    for c in data:
        result += str((int(c) + 3) % 10)
    return result


def decode(string):
    char_list = []
    decode_string = ""
    # Converts the string into a list
    for index in range(len(string)):
        char_list.append(int(string[index]))
    # Encodes the elements of the list
    for index in range(len(char_list)):
        # There are two cases, either it is greater than or equal to 3 or not and we have to treat it differently
        if char_list[index] >= 3:
            char_list[index] = (char_list[index] + 3) % 10
        # Adds 10 so that there will be no negative number
        else:
            char_list[index] = (char_list[index] + 10 - 3) % 10
    # Makes the new string
    for index in range(len(char_list)):
        decode_string = decode_string + str(char_list[index])

    return decode_string


str_input = ''
str_code = ''

while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    opcion = input("\nPlease enter an option: ")

    if opcion == '1':
        print("Please enter your password to encode: ", end="")
        str_input = input()
        str_code = encode(str_input)
        print("Your password has been encoded and stored!\n")
    elif opcion == '2':
        print("The encoded password is {0}, and the original password is {1}\n".format(str_code, str_input))
    elif opcion == '3':
        break
