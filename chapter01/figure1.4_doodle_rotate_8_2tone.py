
from doodle import doodle

import turtle as t

if __name__ == '__main__':
    colors = ('red', 'black')
    for _ in range(4):
        for color in colors:
            t.color(color)
            doodle()
            t.left(45)
            t.forward(100)
    t.mainloop()


