from turtle import Turtle


START_POSITION = [(0,0), (-20, 0), (-40,0)]
MOVE_DISTANCE = 20
class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.game_on = True
    def create_snake(self):
        for coord in START_POSITION:
            self.add_seg(coord)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def turn_snake(self, heading):
        if self.head.heading() == heading - 180 or self.head.heading() == heading + 180:
            pass
        else:
            self.head.setheading(heading)

    def end_game(self):
        for seg in self.segments[1:]:
            if self.head.distance(seg) < 10:
                return False

        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:

            return False

        else:
            return True

    def extend(self):
        self.add_seg(self.segments[-1].position())

    def add_seg(self,position):
        new_seg = Turtle('square')
        new_seg.color('white')
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def reset_snake(self):
        for seg in self.segments:
            seg.reset()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

