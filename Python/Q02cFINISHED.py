# Q02c

def amendMessage(inMessage,inValue1,inValue2):
    outMessage = inMessage[inValue1:inValue1+inValue2]
    return outMessage

check = 0
while check == 0:
    message = str(input("Enter a phrase 'end' to finish: "))
    if (message == "end"):
        check = 1
        print("Goodbye")
    else:
        startPos = int(input("Start position: "))
        characters = int(input("Number of characters: "))
        newMessage = amendMessage(message,startPos,characters)
        print(newMessage)
        print("Thank you")
    
