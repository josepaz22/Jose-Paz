def decoder(string):
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
