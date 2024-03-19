# Programming Paradigms
Programming paradigms are a way to classify programming languages based on their features. The main paradigms include procedural, object-oriented, and functional programming.

## Procedural Programming
Procedural programming is a type of imperative programming where the logic of the program is written in procedures or routines. The main focus is on the procedure that manipulates the data. It's a step-by-step programming paradigm, literally a list of instructions telling the computer what to do in which order. C and Pascal are examples of procedural programming languages.

Example in Python:

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

## Object-Oriented Programming (OOP)
Object-oriented programming is based on the concept of "objects", which contain data and methods to manipulate the data. The main focus is on objects and the operations that can be performed on them. OOP allows for concepts such as inheritance, encapsulation, and polymorphism. Languages like Java, C++, and Python support object-oriented programming.

Example in Python:
```
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

alice = Person("Alice")
alice.greet()
```

=> class, object and method

## Functional Programming
Functional programming treats computation as the evaluation of mathematical functions and avoids changing state and mutable data. In other words, it emphasizes the application of functions, in contrast to the procedural programming style, which emphasizes changes in state. Functional programming languages map input to output. This style of programming is used in languages like Haskell, Erlang, and in some parts of JavaScript.

Example in Python:
```
names = ["Alice", "Bob", "Charlie"]
greetings = map(lambda name: f"Hello, {name}!", names)

for greeting in greetings:
    print(greeting)
```

Each of these paradigms has its own strengths and weaknesses, and they are often used together in the same program. For example, Python supports both procedural and object-oriented programming, and it has some features of functional programming as well. The choice of paradigm often depends on the specific needs of the project.