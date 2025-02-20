
import turtle as t

from doodle import doodle


def rotation_doodle():
    t.down()
    for _ in range(9):
        doodle()
        t.right(10)
        t.forward(50)


if __name__ == '__main__':
    rotation_doodle()
    t.mainloop()


