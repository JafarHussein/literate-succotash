# Python Mastery: Functions to Weather API App
## Comprehensive Exercise Set

This document contains 8 progressive exercises for each major Python concept starting from Functions. Each set integrates concepts learned in previous modules to help build robust problem-solving skills.

---

## 1. Functions (#31)
*Concepts integrated: Variables, User Input, Math, If-statements.*

1. **Simple Greeter**: Create a function that takes a name and an age, then prints a personalized greeting.
2. **Area Calculator**: Write a function `calculate_area(shape, dimensions)` that handles circles and rectangles.
3. **Currency Converter**: A function that converts USD to local currency based on a user-provided rate.
4. **Validation Logic**: Create a function that checks if a password is valid (length > 8).
5. **Temperature Helper**: Write a function that converts Celsius to Fahrenheit using the formula.
6. **Odd/Even Checker**: A function that returns a boolean indicating if a number is even.
7. **The Multiplier**: Create a function that takes two numbers and returns their product, but only if both are positive.
8. **Mini-Calculator**: Build a function `operate(a, b, symbol)` that performs +, -, *, or / based on the symbol provided.

---

## 2. Default & Keyword Arguments (#32 - #33)
*Concepts integrated: Functions, String Methods, Format Specifiers.*

1. **Receipt Generator**: Function `print_invoice(item, price, tax=0.05)` that prints a formatted receipt.
2. **Power Function**: `power(base, exponent=2)` that returns the square by default.
3. **Profile Builder**: A function using keyword arguments to create a user profile (name, city, hobby).
4. **Message Wrapper**: A function that prints a string inside a box of characters (default char is '*').
5. **Connection String**: Create a function `db_connect(ip, port=8080, protocol="http")`.
6. **String Cleaner**: `clean_text(text, lowercase=True, remove_spaces=False)`.
7. **Discount Applier**: `apply_discount(price, percentage=10)` where the percentage can be overridden.
8. **Logging System**: A function `log_message(msg, level="INFO")` that formats the output as `[LEVEL]: msg`.

---

## 3. *args & **kwargs (#34)**
*Concepts integrated: Iterables, Loops, Arithmetic.*

1. **Infinite Adder**: Use `*args` to sum any number of integers provided.
2. **Contact Card**: Use `**kwargs` to print a list of user details (email, phone, address).
3. **String Joiner**: A function that takes `*args` and a separator keyword to join strings together.
4. **Multi-Multiplier**: Multiply all numbers passed via `*args`.
5. **Dynamic HTML Tag**: `make_tag(tag_name, content, **attributes)` to return `<tag attr="val">content</tag>`.
6. **Stats Calculator**: Function that returns the min, max, and average of `*args`.
7. **Order Summary**: A function taking `*args` (item names) and `**kwargs` (customer info) to print an order summary.
8. **Function Wrapper**: Create a function that prints "Executing..." and then calls another function with any passed args/kwargs.

---

## 4. Iterables & Membership Operators (#35 - #36)**
*Concepts integrated: Lists, Sets, Tuples, If-statements.*

1. **Inventory Check**: Use `in` to check if an item exists in a predefined list of stocks.
2. **Unique Guest List**: Take a list of names (with duplicates) and use a Set to find unique visitors.
3. **Vowel Finder**: Iterate through a string and print only the characters that are vowels using a membership check.
4. **Tuple Unpacker**: Create a list of tuples `(city, population)` and print them in a sentence using a loop.
5. **Restricted Access**: A list of "banned" usernames; check if a new input is allowed.
6. **Common Interests**: Find the intersection of two sets of hobbies.
7. **Case-Insensitive Search**: Search for a word in a list of strings, ensuring "Python" matches "python".
8. **Sub-string Presence**: Check if a list of keywords are present within a long paragraph.

---

## 5. List Comprehensions (#37)**
*Concepts integrated: Ranges, Arithmetic, Conditional Expressions.*

1. **Squares List**: Generate a list of squares for numbers 1 to 20.
2. **Even Filter**: Filter a list of random numbers to keep only the even ones.
3. **Word Lengths**: Given a list of words, create a list of their lengths.
4. **Conditional Formatting**: Create a list that says "High" if a number is > 50 and "Low" otherwise.
5. **Uppercase Names**: Convert a list of lowercase names to title case.
6. **Divisibility Master**: Generate numbers between 1-100 divisible by both 3 and 5.
7. **Nested Flattening**: Flatten a 2D list `[[1,2], [3,4]]` into `[1,2,3,4]` using comprehension.
8. **Character Filter**: Extract only the digits from a string using list comprehension.

---

## 6. Match-Case & Modules (#38 - #39)**
*Concepts integrated: Random, Math, Logic.*

1. **Weekday Finder**: Use `match-case` to print "Work" for Mon-Fri and "Weekend" for Sat-Sun.
2. **Command Parser**: A system that takes inputs like "START", "STOP", "RESTART" and matches them to actions.
3. **Math Module Lab**: Use `math.sqrt` and `math.ceil` on user input within a match-case menu.
4. **Random Choice**: Use the `random` module to pick a winner from a list generated by list comprehension.
5. **Custom Module**: Create a file `geometry.py` with area functions and import it into a main script.
6. **File Type Checker**: Use `match-case` to identify file extensions (.py, .js, .cpp).
7. **HTTP Status**: Match common status codes (200, 404, 500) to their text descriptions.
8. **Dice Simulator**: Import `random` and use match-case to print "Critical Hit" if a 20 is rolled.

---

## 7. Scope & 'if name == main' (#40 - #41)**
*Concepts integrated: Global vs Local, Modular Design.*

1. **Counter Global**: Use the `global` keyword to increment a counter inside a function.
2. **Module Protection**: Create a script that prints "Hello" only when run directly, not when imported.
3. **Shadowing Test**: Define a variable globally and a variable with the same name locally; observe the behavior.
4. **Namespace Tool**: Create two modules with functions of the same name and import them using `as` to avoid conflict.
5. **Library Script**: Write a set of math utility functions that only run a "demo" if the script is executed.
6. **Closure Simulation**: Create a function inside a function that accesses the outer scope.
7. **Variable Lifetime**: Write a loop that creates variables and check their existence outside the loop.
8. **Main Entry Point**: Refactor a previous "Calculator" project so the logic is in functions and the UI is under `if __name__ == "__main__"`.

---

## 8. OOP: Classes, Variables, & Inheritance (#46 - #48)**
*Concepts integrated: Dictionaries, Functions, Logic.*

1. **The Car Class**: Create a `Car` class with attributes (make, model, year) and a `drive()` method.
2. **Class Counter**: Use a class variable to track how many `Student` objects have been created.
3. **Animal Kingdom**: Create a base class `Animal` and subclasses `Dog` and `Cat` with unique `speak()` methods.
4. **Library System**: A `Book` class and a `Library` class that stores a list of Book objects.
5. **Employee Hierarchy**: `Employee` base class and `Manager` subclass that adds a `department` attribute.
6. **Bank Account**: A class with `balance` and methods for `deposit` and `withdraw` (with if-statement checks).
7. **Rectangle Override**: A `Shape` class inherited by `Rectangle` which calculates area.
8. **Smart Home**: A `Device` class with a status (on/off). Create `Light` and `Fan` subclasses.

---

## 9. Advanced OOP: Super, Polymorphism, & Duck Typing (#49 - #52)**
*Concepts integrated: Lists, Inherited Methods.*

1. **Super Constructor**: Use `super().__init__()` to initialize base attributes in a subclass.
2. **Shape Polymorphism**: Create a list of different shapes (Circle, Square) and call `.draw()` on each in a loop.
3. **Multiple Inheritance**: A `FlyingFish` class inheriting from both `Bird` and `Fish`.
4. **Duck Typing Payment**: Create a `process_payment(processor)` function that works with any object having a `.pay()` method.
5. **Vehicle Fleet**: An abstract-like setup where `Truck` and `Bike` override a `fuel_efficiency()` method.
6. **The Music Player**: Subclasses `MP3` and `WAV` that both have a `.play()` method used by a central player.
7. **Logger Polymorphism**: A function that accepts either a `FileLogger` or `ConsoleLogger` to record data.
8. **Extended Init**: A `Smartphone` class that uses `super()` to inherit from `Electronic` but adds `battery_life`.

---

## 10. Static/Class Methods & Magic Methods (#53 - #55)**
*Concepts integrated: Arithmetic, String Formatting.*

1. **String Representation**: Use `__str__` to make a `User` object print "User: [username]".
2. **Vector Addition**: Use `__add__` to allow two `Vector` objects to be added with `+`.
3. **Static Converter**: A `UnitConverter` class with a `@staticmethod` for Celsius to Kelvin.
4. **Class Factory**: Use `@classmethod` to create a `Person` object from a birth year instead of age.
5. **Length Magic**: Use `__len__` in a `Shelf` class to return the number of books it holds.
6. **Equality Check**: Implement `__eq__` to compare two `Product` objects by their ID.
7. **Validation Static**: A `@staticmethod` in a `Validator` class to check if an email is valid.
8. **Multiplier Magic**: Implement `__mul__` to allow an `Ingredient` object to be multiplied by a quantity.

---

## 11. Property, Decorators, & Exceptions (#56 - #58)**
*Concepts integrated: If-statements, Logic, Scope.*

1. **Protected Age**: Use `@property` and a setter to ensure a `User.age` cannot be negative.
2. **Timer Decorator**: Create a decorator that prints how long a function takes to execute.
3. **Safe Division**: Use `try-except` to handle `ZeroDivisionError` in a calculator.
4. **Debugging Decorator**: A decorator that prints the arguments a function received.
5. **Input Validator**: A loop that keeps asking for a number until a valid integer is provided (using `ValueError`).
6. **Read-Only Property**: Create a `Circle` class where `pi` is a property with no setter.
7. **Custom Exception**: Raise a `NegativeNumberError` if a user enters a negative value for a bank withdrawal.
8. **Auth Decorator**: A mock `@require_login` decorator that only runs a function if a global `logged_in` is True.

---

## 12. File I/O (#59 - #61)**
*Concepts integrated: Exception Handling, Lists, Strings.*

1. **Note Taker**: Take user input and write it to a file called `notes.txt`.
2. **Safe Reader**: Open a file and print its contents, handling the `FileNotFoundError`.
3. **Log Append**: Write a function that appends a timestamped message to `log.txt`.
4. **CSV Parser**: Read a file with names and ages (comma-separated) and print them as a dictionary.
5. **Word Counter**: Read a text file and count how many times a specific word appears.
6. **File Copier**: Write a script that reads `source.txt` and writes its content to `destination.txt`.
7. **Clean Slate**: A script that checks if a file exists; if so, deletes it and creates a fresh one.
8. **Batch Creator**: Use a loop and list comprehension to create 5 files named `test1.txt` to `test5.txt`.

---

## 13. Dates, Times & Multithreading (#62 - #64)**
*Concepts integrated: Modules, While Loops, Logic.*

1. **Birthday Countdown**: Calculate how many days are left until your next birthday.
2. **Parallel Printers**: Create two threads that print numbers 1-10 simultaneously.
3. **Time Formatter**: Print the current time in the format: "Sunday, May 03, 2026".
4. **Threaded Timer**: A function that runs in the background and prints "Tick" every 5 seconds.
5. **Age in Seconds**: Ask for a birthdate and calculate the user's age in total seconds.
6. **Race Condition Demo**: (Concept) Create two threads that increment a shared variable.
7. **Schedule Task**: Use `time.sleep()` to create a function that executes 10 seconds after being called.
8. **Logging Thread**: A main program that takes input while a background thread logs "System Active".

---

## 14. API & PyQt5 Basics (#65 - #69)**
*Concepts integrated: OOP, Dictionaries, External Modules.*

1. **Status Checker**: Use `requests` to check if `google.com` returns a 200 OK status.
2. **Hello GUI**: Create a basic PyQt5 window with the title "My First App".
3. **Label Update**: A PyQt5 window with a label that says "Hello, [User]".
4. **Image Viewer**: Use a PyQt5 Label to display a local `.jpg` or `.png` image.
5. **Vertical Layout**: Arrange 3 labels on top of each other using `QVBoxLayout`.
6. **JSON Fetcher**: Use `requests` to get data from a free API (like JSONPlaceholder) and print a specific key.
7. **Grid Layout**: Create a 2x2 grid of labels (representing a dashboard).
8. **API Error Handler**: Wrap an API request in a `try-except` block to handle connection timeouts.

---

## 15. PyQt5 Interactive & Final Projects (#70 - #77)**
*Concepts integrated: Events, CSS, API Data.*

1. **Button Click**: Add a button to a GUI that prints "Clicked!" to the console when pressed.
2. **Style with CSS**: Use `.setStyleSheet()` to make a label's text red and background black.
3. **Checkbox Logic**: A GUI where a button is only enabled if a "Terms & Conditions" checkbox is checked.
4. **Input Mirror**: A `QLineEdit` that updates a label in real-time as the user types.
5. **Digital Clock**: Combine `PyQt5` and `time` module to create a clock that updates every second.
6. **Radio Choice**: A GUI with radio buttons for "Light Mode" and "Dark Mode" that changes background colors.
7. **Stopwatch**: Build a GUI with Start, Stop, and Reset buttons using a `QTimer`.
8. **Weather App**: The final challenge: A GUI that takes a city name, calls a Weather API, and displays the temperature and description.

---
*Good luck with your practice! Combine these concepts to build even bigger projects.*
