import turtle
import sys

def koch_snowflake(length, level):
    if level == 0:
        turtle.forward(length)
        return
    length /= 3.0
    koch_snowflake(length, level-1)
    turtle.left(60)
    koch_snowflake(length, level-1)
    turtle.right(120)
    koch_snowflake(length, level-1)
    turtle.left(60)
    koch_snowflake(length, level-1)

def draw_snowflake(length, level):
    for _ in range(3):
        koch_snowflake(length, level)
        turtle.right(120)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Використання: python task_2.py <довжина> <рівень>")
        sys.exit(1)

    length = float(sys.argv[1])
    level = int(sys.argv[2])

    turtle.speed(0)
    turtle.penup()
    turtle.goto(-length/2, length/3)
    turtle.pendown()
    draw_snowflake(length, level)
    turtle.hideturtle()
    turtle.done()

