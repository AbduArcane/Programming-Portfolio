invite = ["Mom", "Dad", "Brother", "Sister"]

for people in invite:
    print('Dear ' + people + ", you are invited to dinner this evening.")


print("\nUpdate, unfortuantely only 2 people are invited to dinner.")

while len(invite) > 2:
    Eliminate = invite.pop()
    print(f"Sorry for the inconvinence {
          Eliminate}, we are unable to inite you for dinner.")

print("\n The following are invited to the dinner: ")
for people in invite:
    print('Dear ' + people + ", you are invited to dinner this evening.")

del invite[0]
del invite[0]

print("\nFinal Guest List: ", invite)
