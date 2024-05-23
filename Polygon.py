import tkinter as tk
import random
import math

class RandomArtGenerator:
    WIDTH = 800
    HEIGHT = 600

    @staticmethod
    def generate_squares(canvas):
        colors = ['#FF5733', '#FFC300', '#DAF7A6', '#9AECDB', '#A0A0A0']
        for _ in range(20):
            x = random.randint(0, RandomArtGenerator.WIDTH)
            y = random.randint(0, RandomArtGenerator.HEIGHT)
            size = random.randint(20, 100)
            color = random.choice(colors)
            canvas.create_rectangle(x, y, x + size, y + size, fill=color)

    @staticmethod
    def generate_circles(canvas):
        colors = ['#FF5733', '#FFC300', '#DAF7A6', '#9AECDB', '#A0A0A0']
        for _ in range(30):
            x = random.randint(0, RandomArtGenerator.WIDTH)
            y = random.randint(0, RandomArtGenerator.HEIGHT)
            size = random.randint(20, 100)
            color = random.choice(colors)
            canvas.create_oval(x, y, x + size, y + size, fill=color)

    @staticmethod
    def generate_strings(canvas):
        colors = ['#FF5733', '#FFC300', '#DAF7A6', '#9AECDB', '#A0A0A0']
        for _ in range(10):
            x1 = random.randint(0, RandomArtGenerator.WIDTH)
            y1 = random.randint(0, RandomArtGenerator.HEIGHT)
            x2 = random.randint(0, RandomArtGenerator.WIDTH)
            y2 = random.randint(0, RandomArtGenerator.HEIGHT)
            color = random.choice(colors)
            canvas.create_line(x1, y1, x2, y2, fill=color, width=random.randint(1, 3))

    @staticmethod
    def generate_spirals(canvas):
        colors = ['#FF5733', '#FFC300', '#DAF7A6', '#9AECDB', '#A0A0A0']
        for _ in range(10):
            x = random.randint(0, RandomArtGenerator.WIDTH)
            y = random.randint(0, RandomArtGenerator.HEIGHT)
            size = random.randint(20, 100)
            color = random.choice(colors)
            RandomArtGenerator.draw_spiral(canvas, x, y, size, color)

    @staticmethod
    def draw_spiral(canvas, x, y, size, color):
        angle = 0
        spiral_factor = 0.1
        for _ in range(100):
            x1 = x + math.cos(angle) * size
            y1 = y + math.sin(angle) * size
            x2 = x + math.cos(angle + spiral_factor) * size
            y2 = y + math.sin(angle + spiral_factor) * size
            canvas.create_line(x1, y1, x2, y2, fill=color)
            size += 1
            angle += spiral_factor

    @staticmethod
    def generate_overlap(canvas):
        colors = ['#FF5733', '#FFC300', '#DAF7A6', '#9AECDB', '#A0A0A0']
        for _ in range(20):
            x1 = random.randint(0, RandomArtGenerator.WIDTH)
            y1 = random.randint(0, RandomArtGenerator.HEIGHT)
            x2 = random.randint(0, RandomArtGenerator.WIDTH)
            y2 = random.randint(0, RandomArtGenerator.HEIGHT)
            color = random.choice(colors)
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    @staticmethod
    def generate_gradient_shift(canvas):
        colors = ['#FF5733', '#FFC300', '#DAF7A6', '#9AECDB', '#A0A0A0']
        for i in range(10):
            x1 = RandomArtGenerator.WIDTH / 10 * i
            y1 = 0
            x2 = RandomArtGenerator.WIDTH / 10 * (i + 1)
            y2 = RandomArtGenerator.HEIGHT
            color = random.choice(colors)
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    @staticmethod
    def generate_polygons(canvas):
        colors = ['#FF5733', '#FFC300', '#DAF7A6', '#9AECDB', '#A0A0A0']
        for _ in range(15):
            num_points = random.randint(3, 8)
            points = [(random.randint(0, RandomArtGenerator.WIDTH), random.randint(0, RandomArtGenerator.HEIGHT)) 
                      for _ in range(num_points)]
            color = random.choice(colors)
            canvas.create_polygon(points, fill=color)

    @staticmethod
    def generate_cubical(canvas):
        colors = ['#FF5733', '#FFC300', '#DAF7A6', '#9AECDB', '#A0A0A0']
        for _ in range(5):
            x = random.randint(0, RandomArtGenerator.WIDTH)
            y = random.randint(0, RandomArtGenerator.HEIGHT)
            size = random.randint(20, 100)
            color = random.choice(colors)
            canvas.create_rectangle(x, y, x + size, y + size, fill=color)

    @staticmethod
    def generate_rubix(canvas):
        colors = ['#FF5733', '#FFC300', '#DAF7A6', '#9AECDB', '#A0A0A0']
        for i in range(10):
            for j in range(10):
                x = RandomArtGenerator.WIDTH / 10 * i
                y = RandomArtGenerator.HEIGHT / 10 * j
                size = RandomArtGenerator.WIDTH / 10
                color = random.choice(colors)
                canvas.create_rectangle(x, y, x + size, y + size, fill=color)

    @staticmethod
    def generate_morse(canvas):
        colors = ['#FF5733', '#FFC300', '#DAF7A6', '#9AECDB', '#A0A0A0']
        morse_code = [
            (1, 1, 0, 0, 0), (1, 1, 1, 0, 0), (1, 1, 1, 1, 0), (1, 1, 1, 1, 1),
            (0, 1, 1, 1, 1), (0, 0, 1, 1, 1), (0, 0, 0, 1, 1), (0, 0, 0, 0, 1),
            (1, 0, 0, 0, 0), (1, 1, 0, 1, 1), (0, 1, 0, 1, 0)
        ]
        for i in range(10):
            for j in range(5):
                x = RandomArtGenerator.WIDTH / 10 * i
                y = RandomArtGenerator.HEIGHT / 5 * j
                size = RandomArtGenerator.WIDTH / 10
                color = random.choice(colors)
                if random.choice(morse_code):
                    canvas.create_rectangle(x, y, x + size, y + size, fill=color)

class RandomArtApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Random Artwork Generator")
        self.master.geometry(f"{RandomArtGenerator.WIDTH}x{RandomArtGenerator.HEIGHT}")

        self.canvas = tk.Canvas(self.master, width=RandomArtGenerator.WIDTH, height=RandomArtGenerator.HEIGHT)
        self.canvas.pack()

        self.generate_artwork()

        self.canvas.bind("<Button-1>", self.regenerate_artwork)

    def generate_artwork(self):
        self.canvas.delete("all")  # Clear previous drawings
        generators = [
            RandomArtGenerator.generate_squares, RandomArtGenerator.generate_circles,
            RandomArtGenerator.generate_strings, RandomArtGenerator.generate_spirals,
            RandomArtGenerator.generate_overlap, RandomArtGenerator.generate_gradient_shift,
            RandomArtGenerator.generate_polygons, RandomArtGenerator.generate_cubical,
            RandomArtGenerator.generate_rubix, RandomArtGenerator.generate_morse
        ]
        random.choice(generators)(self.canvas)

    def regenerate_artwork(self, event):
        self.generate_artwork()

def main():
    root = tk.Tk()
    app = RandomArtApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
def generate_artwork(canvas):
        canvas.delete("all")  # Clear previous drawings
        generators = [
            RandomArtGenerator.generate_person,  # Add generate_person method
            RandomArtGenerator.generate_squares, RandomArtGenerator.generate_circles,
            RandomArtGenerator.generate_strings, RandomArtGenerator.generate_spirals,
            RandomArtGenerator.generate_overlap, RandomArtGenerator.generate_gradient_shift,
            RandomArtGenerator.generate_polygons, RandomArtGenerator.generate_cubical,
            RandomArtGenerator.generate_rubix, RandomArtGenerator.generate_morse
        ]
        random.choice(generators)(canvas)
