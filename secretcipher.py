def secretCipher():
    inputText = input("Enter your text to encode: ")

    while True:
      try:
        shiftAmt = int(input("Enter how many places to shift: "))
        False
        break
        
      except:
          print("Invalid input. Please enter again.")

    cipherText = ""
    for char in inputText:
        charPosition = ord(char)# returns the unicode code point representation of the passed argument
        if 48 <= charPosition <= 57: #0123456789
          if shiftAmt%10==0:
            shiftAmt+=1
          newCharPosition = (charPosition - 48 + shiftAmt) % 10 + 48

        elif 65 <= charPosition <= 90: #A-Z
          if shiftAmt%26==0:
            shiftAmt+=1
          newCharPosition = (charPosition - 65 + shiftAmt) % 26 + 65
        
        elif 97 <= charPosition <= 122: #a-Z  
          if shiftAmt%26==0:
            shiftAmt+=1
          newCharPosition = (charPosition - 97 + shiftAmt) % 26 + 97

        else:
            newCharPosition = charPosition
        cipherText += chr(newCharPosition)

    print('\n********************')
    print("Encoded Message: ")
    print(cipherText)
    print('********************')


def decipherMessage():
    inputText = input("Enter your text to decode: ")
    while True:
      try:
        shiftAmt = int(input("Enter how many places to shift: "))
        False
        break
      except:
          print("Invalid input. Please enter again.")
    

    outputText = ""
    for char in inputText:
        charPosition = ord(char)
        if 48 <= charPosition <= 57:
            newCharPosition = (charPosition - 48 - shiftAmt) % 10 + 48
        elif 65 <= charPosition <= 90:
            newCharPosition = (charPosition - 65 - shiftAmt) % 26 + 65
        elif 97 <= charPosition <= 122:
            newCharPosition = (charPosition - 97 - shiftAmt) % 26 + 97
        else:
            newCharPosition = charPosition
        outputText += chr(newCharPosition)

    print('\n********************')
    print("Decoded Message: ")
    print(outputText)
    print('********************')

secretCipher()
decipherMessage()


