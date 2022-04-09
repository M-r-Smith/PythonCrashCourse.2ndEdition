# 2-7 Stripping Names: Use a variable to represent a person's name, and include some whitespace characters at the beginning and end of the name.
# Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed, then print the name using each of the three stripping functions,
# lstrip(), rstrip(), and strip.

# this one strips the white space from the left side, while using \t(tab) & \n(next line).
name = '\tyusuke\n'
print(name.lstrip())

# this one strips the white space from the right side, while using \t(tab) & \n(next line).
name = '\tyusuke\n'
print(name.rstrip())

# this one strips the white space from both the left and the right, while using \t(tab) & \n(next line).
name = '\tyusuke\n'
print(name.strip())