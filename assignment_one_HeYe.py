#Name: {HeYe}
#Assignment1

from turtle import *

import turtle


screen = turtle.Screen()
screen.title("Task A: Colorful Turtle Drawing")
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(36):
   
    t.color(colors[i % len(colors)])
    
    t.forward(i * 5)
    
    t.right(144)


turtle.done()

print("--- Task B: QA Bot ---")
print("Bot: Hello! I am a simple QA bot. (Type 'bye' to exit)")

while True:
    question = input("Ask me something: ").lower() 

    if question == "bye":
        print("Bot: Goodbye!")
        break
    elif question == "hello":
        print("Bot: Hello! Nice to meet you.")
    elif question == "python":
        print("Bot: Python is a language.")
    elif question == "jetson":
        print("Bot: Jetson Nano is an AI computer.")
    elif question == "ai":
        print("Bot: AI means Artificial Intelligence.")
    elif question == "name":
        print("Bot: My name is Python Bot.")
    elif question == "hku":
        print("Bot: HKU is The University of Hong Kong, a great place to study!")
    elif question == "robot":
        print("Bot: I am a robot, just a friendly AI program.")
    elif question == "human":
        print("Bot: Humans are awesome creatures who created me.")
    else:
        print("Bot: Sorry, I don't understand.")


print("\n--- Task C: Simple Calculator ---")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


op = input("Choose operation (+, -, *, /): ")


if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":

    if num2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        print("Result:", num1 / num2)
else:
    print("Invalid operation")

