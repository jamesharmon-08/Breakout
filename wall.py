from turtle import Turtle
from brick import Brick



# brick will be pen square width 1 length 2

class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.wall = [[1, ], [1, ], [1, ], [1, ], [1, ],[1, ],
                     [1, ], [1, ], [1, ], [1, ], [1, ],[1, ],
                     [1, ], [1, ], [1, ], [1, ], [1, ],[1, ],
                     ]
        self.create_wall()

    def create_wall(self):
        for i in range(len(self.wall)):
            self.wall[i][0] = 1
            x = -150 + ((i % 6) * 60)
            y = 200 - ((i//6) * 30)
            brk = Brick(x, y)
            self.wall[i].append(brk)

    def display_wall(self):
        for brick in self.wall:
            if brick[0] == 1:
                x = -150 + ((i % 6) * 60)
                y = 200 - ((i//6) * 30)
                brick[1].draw_brick(x, y)

    def reset_wall(self):
        for brick in self.wall:
            brick[0] = 1
            brick[1].show_brick()

    def collision(self, ball):
        for brick in self.wall:
            if brick[0] == 1:
                if brick[1].distance(ball) < 30:
                    brick[0] -= 1
                    print(brick[0])
                    if brick[0] == 0:
                        brick[1].erase_brick()
                    ball.bounce_y()
                    return True


