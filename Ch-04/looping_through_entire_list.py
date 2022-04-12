# Looping Through an Entire List
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    
# Doing more work within a for loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

# You can write as many lines of code as you like in the for loop. Every indented line after the for loop is inside the loop.
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}\n")


# Doing Something After a for Loop.
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}. that ws a great trick!")
    print(f"I can't wait to see your next trick, {magician. title()}.\n")
print(f"Thank you, everyone. That was a great magic show!")