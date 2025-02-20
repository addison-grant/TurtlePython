import turtle as t
from squarepiece import squarepiece

def square(size):
    for _ in range(4):
        squarepiece(size)

if __name__ == '__main__':
    square(50)
    t.mainloop()
