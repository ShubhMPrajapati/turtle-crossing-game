import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
cars_manager = CarManager()

screen.onkey(fun=player.moved, key="Up")

sleep_time = 0.1

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(sleep_time)
    cars_manager.create_car()
    cars_manager.car_move()

    if cars_manager.got_hit(player) == False:
        scoreboard.game_over()
        game_is_on = False

    elif player.raced_finished():
        scoreboard.score_increase()
        sleep_time -= 0.02
        player.reset()

screen.exitonclick()
