# Password Generator

This project allows users to customize their password by specifying how many letters, symbols, and numbers it should contain. The generated password is randomized for better security.

**Technologies Used**

+ ```Python```
+ ```random``` module for shuffling and random selections

**Features**

+ Customizable password length by character type
+ Randomized order of characters for increased security
+ Simple command-line interface for user inputs

**What Users Can Do**

+ Input the desired number of letters, symbols, and numbers
+ Receive a securely randomized password based on their preferences

**The Process / How It’s Built**

+ The program collects user inputs for the number of each character type.
+ It randomly picks the specified number of letters, symbols, and numbers from predefined lists.
+ The characters are combined and shuffled to produce the final password.
+ The password is displayed as a string to the user.

**What I Learned**

+ How to use the ```random``` module for generating random indexes and shuffling lists.
+ Building functions that manage repetitive tasks (```generate_characters```).
+ Managing user input and converting it to integers for program logic.
+ How to combine and shuffle elements from multiple lists.
