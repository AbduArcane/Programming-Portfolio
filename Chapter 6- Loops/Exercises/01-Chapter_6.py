prompt = "\nPlease choose the toppings for your pizza!"
prompt += "\n Use 'quit' when you are done! : "

while True:
    toppings = input(prompt)
    if toppings != 'quit':
        print(toppings + " has been added to your pizza!")
    else:
        break
