from snake import Snake
from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BG_COLOR = "black"

screen = Screen()

screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(BG_COLOR)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    if snake.head.distance(food.food_x, food.food_y) < 15:
        food.create()
        snake.grow()
        scoreboard.update_score()
    
    is_hit_vertical_walls = snake.head.xcor() < -280 or snake.head.xcor() > 280
    is_hit_horizontal_walls = snake.head.ycor() < -280 or snake.head.ycor() > 280
    
    if is_hit_horizontal_walls or is_hit_vertical_walls:
        game_is_on = False
        scoreboard.game_over()
    
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()