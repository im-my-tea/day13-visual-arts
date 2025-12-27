import turtle as t
import random

# --- PHASE 1: SETUP ---
is_race_on = False
screen = t.Screen()
# Set the window size so we know where the finish line is
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color: ")

# --- PHASE 2: CREATE RACERS ---
# instead of r, g, b variables, we use a list of strings
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Create 6 turtles using a loop
for turtle_index in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup() # Don't draw lines
    # Pick color based on loop index (0=red, 1=orange...)
    new_turtle.color(colors[turtle_index])
    # Go to starting line (x=-230) and different height (y)
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    # Add to our list so we can control them later
    all_turtles.append(new_turtle)

# Validation to ensure race doesn't start until user bets
if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        # 1. Check if a turtle has crossed the finish line (x > 230)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            
            # 2. Check if the user guessed correctly
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            continue

        # 3. Move random distance (0 to 10 paces)
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)










screen.exitonclick()