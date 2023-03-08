def encode(data):
  result=""
  for c in data:
    result+=str((int(c)+3)%10)
  return result

def decode(data):
  result=""
  for c in data:
    result+=str((int(c)-3)%10)
  return result

str_input=''
str_code=''

while True:
  print("Menu")
  print("-------------")
  print("1. Encode")
  print("2. Decode")
  print("3. Quit")

  opcion = input("\nPlease enter an option: ")

  if opcion == '1':
    print("Please enter your password to encode: ", end="")
    str_input=input()
    str_code=encode(str_input)
    print("Your password has been encoded and stored!\n")
  elif opcion=='2':
    print("The encoded password is {0}, and the original password is {1}\n".format(str_code, str_input))
  elif opcion == '3':
    break