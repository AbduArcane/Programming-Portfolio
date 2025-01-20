prompt = "Please Enter Your Age: "
prompt += "\nPlease Enter 'quit' When Done!"

while True:
    Age = input(prompt)
    if Age == 'quit':
        break
    Age = int(Age)

    if Age < 3:
        print("The Ticket is free!")
    elif Age < 13:
        print("The Ticket is $10!")
    else:
        print("The ticket is $15!")
