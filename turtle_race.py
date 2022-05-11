from turtle import Turtle, Screen
import random
screen = Screen()

screen.setup(width=500,height=400)

user_input = screen.textinput("Turtle race", "Which Turtle will win the race?:")
# print(user_input)
t_colors = ["red","green","yellow","orange","blue","violet"]
y_cor = [-70,-40,-10,20,50,80]
all_turtles = []

for i in range(6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(t_colors[i])
    new_turtle.goto(x=-230,y=y_cor[i])
    all_turtles.append(new_turtle)

# print(all_turtles)
random_distance = random.randint(0,10)



if user_input:
    race_on = True

while race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.pos()[0] > 230:
            winner = turtle.pencolor()
            race_on = False
            if user_input.lower == winner:
                print(f"You win the challenge!The {winner} turtle won the race.")
            else:
                print(f"You lose the challenge!The {winner} turtle won the race.")


screen.exitonclick()