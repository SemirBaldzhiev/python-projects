import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.initialize()
    
    def initialize(self):
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.speed("fastest")
        self.create()
    
    def create(self):
        self.food_x = random.randint(-280, 280)
        self.food_y = random.randint(-280, 280)
        self.goto(self.food_x, self.food_y)
        
        