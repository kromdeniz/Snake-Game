from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Mighty Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
game_on = True


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Food eat check
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update()
        snake.update_snake()
    #Wall hit check
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.game_over()

    #Snake self hit check
    for i in range(1,len(snake.segments)):
        # print(snake.segments[i].pos(),"segment")
        # print(snake.head.pos())
        if snake.segments[i].distance(snake.head) <10:
            game_on = False
            scoreboard.game_over()



    screen.listen()


screen.exitonclick()