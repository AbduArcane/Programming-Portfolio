sandwich_orders = ['Grilled Cheese', 'pastrami', 'Falafel',
                   'pastrami', 'Itallian Beef', 'pastrami', 'Pocket']
finished_sandwiches = []

print("The deli has run out of pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print('\n')
while sandwich_orders:
    Preparing_Sandwich = sandwich_orders.pop()
    print("You're " + Preparing_Sandwich +
          " sandwich is crrently being prepared in the kitchen.")
    finished_sandwiches.append(Preparing_Sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(sandwich + " is ready!")
