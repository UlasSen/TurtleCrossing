
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE
    def create_cars(self):
        random_num=random.randint(1,6)
        if random_num==2:
            new_car=Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y=random.randint(-260,260)
            new_car.goto(300,random_y)
            new_car.setheading(180)
            self.all_cars.append(new_car)
    
    def car_moves(self):
        for car in self.all_cars:
            car.forward(self.car_speed)
    
    def car_speedup(self):
        self.car_speed += MOVE_INCREMENT
        