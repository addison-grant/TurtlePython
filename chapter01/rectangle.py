import turtle as t
from squarepiece import squarepiece

def rectangle(side1, side2):
    for _ in range(2):
        squarepiece(side1)
        squarepiece(side2)

if __name__ == '__main__':
    rectangle(200, 50)
    t.mainloop()
