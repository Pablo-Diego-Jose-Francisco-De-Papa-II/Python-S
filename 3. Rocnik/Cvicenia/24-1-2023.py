import tkinter as tk
ca = tk.Canvas(height=500, width=500)
ca.pack()

# Zadanie:
#  Vykresli ciary na zaklade kliknutia
#  sipok na klavesnici.

sur, pohyb = [250, 250, 250, 250], 10
ca.create_line(tuple(sur), width=3, tags="line")

def klik(key):
    global sur, pohyb

    name = key.keysym.lower()
    match name:
        case "up": sur.extend([sur[-2], sur[-1] - pohyb])
        case "down": sur.extend([sur[-2], sur[-1] + pohyb])
        case "right": sur.extend([sur[-2] + pohyb, sur[-1]])
        case "left": sur.extend([sur[-2] - pohyb, sur[-1]])

    ca.coords("line", sur)

#ca.bind_all("<Key>", klik)


#Zadanie: importni random png subor do platna a nech sa hybe wasd.
obr, move = tk.PhotoImage(file = "notmiguel.png"), 10
ca.create_image(250, 250, image = obr, tags = "gato")

def kiten(key):
    name = key.keysym

    match name:
        case "Right": ca.move("gato", move, 0)
        case "Left":  ca.move("gato", -move, 0)
        case "Up":    ca.move("gato", 0, -move)
        case "Down":  ca.move("gato", 0, move)

ca.bind_all("<Key>", kiten)
ca.mainloop()
