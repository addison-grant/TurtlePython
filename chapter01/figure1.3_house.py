from square import square
from triangle import triangle

import turtle as t

RIGHT_ANGLE = 90
STANDARD_LENGTH = 100

t.left(RIGHT_ANGLE)
square(STANDARD_LENGTH)
t.forward(STANDARD_LENGTH)
t.right(90)
t.forward(100)
t.right(180)
triangle(STANDARD_LENGTH)

t.mainloop()
