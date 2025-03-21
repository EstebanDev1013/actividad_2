from turtle import *
from random import randrange, choice
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colors = ["black","green","purple","orange","blue"]
food_color = colors[randrange(len(colors))]
snake_color = colors[randrange(len(colors))]
if snake_color == food_color:
    food_color = colors[randrange(len(colors))]
    snake_color = colors[randrange(len(colors))]


directions = {
    "left": (-10, 0),
    "right": (10, 0),
    "up": (0, 10),
    "down": (0, -10),
}

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food():
    direction = choice(list(directions.values()))
    new_pos = vector(food.x + direction[0], food.y + direction[1])

    if inside(new_pos):
        food.x, food.y = new_pos.x, new_pos.y

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    move_food()

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
