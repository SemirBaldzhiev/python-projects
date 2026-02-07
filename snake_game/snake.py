from turtle import Screen, Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP_DIRECTION = 90
DOWN_DIRECTION = 270
LEFT_DIRECTION = 180
RIGHT_DIRECTION = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)
    
    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)
      
    def up(self):
        if self.head.heading() != DOWN_DIRECTION:
            self.head.setheading(UP_DIRECTION)
    
    def down(self):
        if self.head.heading() != UP_DIRECTION:
            self.head.setheading(DOWN_DIRECTION)
    
    def left(self):
        if self.head.heading() != RIGHT_DIRECTION:
            self.head.setheading(LEFT_DIRECTION)
    
    def right(self):
        if self.head.heading() != LEFT_DIRECTION:
            self.head.setheading(RIGHT_DIRECTION)
    
    def move(self):
        for seg_idx in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_idx - 1].xcor()
            new_y = self.segments[seg_idx - 1].ycor()
            self.segments[seg_idx].goto(new_x, new_y)

        self.head.forward(MOVE_DIST)
    
    def grow(self):
        self.add_segment(self.segments[-1].position())