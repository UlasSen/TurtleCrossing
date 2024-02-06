import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Cross animal")
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard=Scoreboard()

player=Player()

screen.listen()
screen.onkey(player.move_up,"Up")

car_manager=CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.car_moves()
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            scoreboard.gameover()
            game_is_on=False
    if player.ycor()>280:
        scoreboard.update_scoreboard()
        car_manager.car_speedup()
        player.goto(0,-300)

screen.exitonclick()