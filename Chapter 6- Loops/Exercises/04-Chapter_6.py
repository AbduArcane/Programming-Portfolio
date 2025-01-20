sandwich_orders = ['Grilled Cheese', 'Falafel', 'Itallian Beef', 'Pocket']
finished_sandwiches = []

while sandwich_orders:
    Preparing_Sandwich = sandwich_orders.pop()
    print("I made your " + Preparing_Sandwich + " sandwich")
    finished_sandwiches.append(Preparing_Sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(sandwich + " is ready!")
