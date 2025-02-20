import turtle as t

def triangle(size):
    for _ in range(3):
        t.forward(size)
        t.right(120)

if __name__ == '__main__':
    triangle(150)
    t.mainloop()
