# Always indent the line after the for statement in a loop. If you forget python will remind you:
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# This is what happens when you forget to indent. Python sees this as being logical but it doesn't produce the wanted result.
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wat to see your next trick, {magician.title()}.\n")