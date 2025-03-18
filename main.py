import turtle
import time
import tkinter as tk

def calculate_gravity(mass, base_gravity):
    """Обчислює прискорення вільного падіння з урахуванням маси."""
    return base_gravity * (1 + mass / 10)

def calculate_restitution(mass):
    """Обчислює коефіцієнт відновлення швидкості."""
    return 0.5 - min(0.25, 0.02 * mass)

def start_simulation():
    global restitution_base, g, velocity_restitution_increase
    mass = float(mass_entry.get())
    g = float(acceleration_entry.get()) * (1 + mass / 10)
    restitution_base = 0.5 - min(0.25, 0.02 * mass)
    velocity_restitution_increase = 0.001
    window.destroy()


window = tk.Tk()
window.title("Введення даних")
window.geometry("300x200")

mass_label = tk.Label(window, text="Введіть масу м'ячика (в кг):")
mass_label.pack()
mass_entry = tk.Entry(window)
mass_entry.pack()

acceleration_label = tk.Label(window, text="Введіть прискорення вільного падіння (м/с²):")
acceleration_label.pack()
acceleration_entry = tk.Entry(window)
acceleration_entry.pack()

start_button = tk.Button(window, text="Почати симуляцію", command=start_simulation)
start_button.pack()
window.mainloop()

win = turtle.Screen()
win.setup(832, 832)
win.title("Вільне падіння з відбиттям")
win.bgpic("bg3.gif")

ground = turtle.Turtle()
ground.speed(0)
ground.penup()
ground.pensize(5)
ground.color("white")
ground.goto(-450, -310)
ground.begin_fill()
ground.pendown()
ground.goto(450, -310)
ground.goto(450, -500)
ground.goto(-450, -500)
ground.goto(-450, -310)
ground.end_fill()
ground.hideturtle()

ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 300)

height = 300
start_time = time.time()
velocity = 0

while True:
    global g, restitution_base, velocity_restitution_increase
    current_time = time.time()
    time_elapsed = current_time - start_time
    velocity += g * time_elapsed
    displacement = velocity * time_elapsed - 0.5 * g * time_elapsed ** 2
    height -= displacement

    if height <= -300:
        height = -300
        # Оновлення коефіцієнта відновлення на основі швидкості та маси
        adjusted_restitution = min(0.99, restitution_base + abs(velocity) * velocity_restitution_increase)
        velocity = -velocity * adjusted_restitution

    ball.sety(height)

    if abs(velocity) < 0.1 and height == -300:
        break

    start_time = current_time

win.mainloop()
