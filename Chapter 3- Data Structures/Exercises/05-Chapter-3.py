invite = ["Mom", "Dad", "Brother", "Sister"]

for people in invite:
    print('Dear ' + people + ", you are invited to dinner this evening.")


not_available = "Brother"
print(not_available + "is not available for this dinner.")


invite[invite.index(not_available)] = "Cousin"

print(f"\nInvitations Update...")

for people in invite:
    print('Dear ' + people + ", you are invited to dinner this evening.")
