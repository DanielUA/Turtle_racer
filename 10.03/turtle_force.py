import random
import time
import turtle

WIDTH, HEIGHT = 500, 500
COLORS = [
    "red", "blue", "orange", "yellow", "black", 
    "green", "cyan", "brown", "purple", "pink"
    ]

def race(turtles):
    while True:
        for i, racer in enumerate(turtles):
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return i
            
def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1)* spacingx, -HEIGHT//2+20)
        racer.pendown()
        turtles.append(racer)
    
    return turtles


def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Incorrect input, enter a numeric")
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print("Number is not in range 2-10, Try again.")


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")


racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]
turtles = create_turtles(colors)
winner_index = race(turtles)
winner_color = colors[winner_index]
print("Winner colour is: ", winner_color)
time.sleep(5)


