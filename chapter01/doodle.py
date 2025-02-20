import turtle as t

def doodle():
    for length in (100, 100, 50, 50, 100, 25, 25):
        t.forward(length)
        t.right(90)
    t.forward(50)

def square_doodle():
    for _ in range(4):
        doodle()
