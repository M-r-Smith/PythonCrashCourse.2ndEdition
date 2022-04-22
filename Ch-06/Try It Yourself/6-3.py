# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let's call it a glossary.
#      -Think of five programming words you've learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
#      -Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. 
#       Use the newline character(\n) to insert a blank line between each word meaning pair in your output.
programmer_words = {'loops': 'used when you have a block of code which you want to repeat a fixed number of times',
                    'if-elif-else': 'the program will evaluate test expression and will execute the remaining statements only if the given test expression turns out to be true', 
                    'key-value':'An item has a key and a corresponding value that is expressed as a pair (key: value).', 
                    '.get()': 'The get() method returns the value of the item with the specified key.', 
                    '.title()': 'The title() method returns a string where the first character in every word is upper case.',
                    }
for words in programmer_words.items():
    print(words)
    
# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Excercise 6-3 (page 99)
# by replacing your series of print() calls with a loop that runs through the dictionary's keys and values.
# When you're sure that your loop works, add five more Python terms to your glossary. 
# When you run your program again, these new words and meanings should automatically be included in the output.
programmer_words = {'loops': 'used when you have a block of code which you want to repeat a fixed number of times',
                    'if-elif-else': 'the program will evaluate test expression and will execute the remaining statements only if the given test expression turns out to be true', 
                    'key-value':'An item has a key and a corresponding value that is expressed as a pair (key: value).', 
                    '.get()': 'The get() method returns the value of the item with the specified key.', 
                    '.title()': 'The title() method returns a string where the first character in every word is upper case.',
                    }
for names, definitions in programmer_words.items():
    print(f"\n{names}")
    print(f"{definitions}")
    
    