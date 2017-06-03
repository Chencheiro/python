list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
message_encode = ""
message_decode = ""
while(1):
    input_s = input('Write "e" for encode, "d" for decode or "q" for quit: ')
    if (input_s == "q"):
        break
    elif (input_s == "e"):
        message = input("Give me a hot message, babe: ")
        rotation = int(input("Now, give me a rotation number: "))
        #length = len(message)
        for current in message:
            if current == " ":
                message_encode += " "
            elif current.isupper():
                message_encode += current
            else:
                pos_letter = list.index(current)
                for i in range(rotation):
                    pos_letter += 1
                    if pos_letter > 25:
                        pos_letter = 0        
                letter_encode = list[pos_letter]
                message_encode += letter_encode
        print(message_encode)
        message_encode = ""
    elif (input_s == "d"):
        message_d = input("Give me a message to decode: ")
        rotation_d = int(input("Give me the rotation of the encoded message: "))
        for current in message_d:
            if current == " ":
                message_decode += " "
            elif current.isupper():
                message_decode += current 
            else: 
                pos_letter_d = list.index(current)
                for i in range(rotation_d):
                    pos_letter_d -= 1
                    if pos_letter_d < 0:
                        pos_letter_d = 25
                letter_decode = list[pos_letter_d]
                message_decode += letter_decode
    
        print(message_decode)
        message_decode = ""
    
    else:
        print("Wrong instruction, give q,e or d, pliz")