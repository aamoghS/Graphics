import tkinter as tk
import random
import math

class RandomArtGenerator:
    WIDTH = 800
    HEIGHT = 600

    @staticmethod
    def generate_squares(canvas):
        colors = ['#ADD8E6', '#90EE90', '#D3D3D3']  # Light blue, light green, light grey
        for _ in range(20):
            x = random.randint(0, RandomArtGenerator.WIDTH)
            y = random.randint(0, RandomArtGenerator.HEIGHT)
            size = random.randint(20, 100)
            color = random.choice(colors)
            canvas.create_rectangle(x, y, x + size, y + size, fill=color)

    @staticmethod
    def generate_circles(canvas):
        colors = ['#ADD8E6', '#90EE90', '#D3D3D3']
        for _ in range(30):
            x = random.randint(0, RandomArtGenerator.WIDTH)
            y = random.randint(0, RandomArtGenerator.HEIGHT)
            size = random.randint(20, 100)
            color = random.choice(colors)
            canvas.create_oval(x, y, x + size, y + size, fill=color)

    @staticmethod
    def generate_strings(canvas):
        colors = ['#ADD8E6', '#90EE90', '#D3D3D3']
        for _ in range(10):
            x1 = random.randint(0, RandomArtGenerator.WIDTH)
            y1 = random.randint(0, RandomArtGenerator.HEIGHT)
            x2 = random.randint(0, RandomArtGenerator.WIDTH)
            y2 = random.randint(0, RandomArtGenerator.HEIGHT)
            color = random.choice(colors)
            canvas.create_line(x1, y1, x2, y2, fill=color, width=random.randint(1, 3))

    @staticmethod
    def generate_spirals(canvas):
        colors = ['#ADD8E6', '#90EE90', '#D3D3D3']
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
        colors = ['#ADD8E6', '#90EE90', '#D3D3D3']
        for _ in range(20):
            x1 = random.randint(0, RandomArtGenerator.WIDTH)
            y1 = random.randint(0, RandomArtGenerator.HEIGHT)
            x2 = random.randint(0, RandomArtGenerator.WIDTH)
            y2 = random.randint(0, RandomArtGenerator.HEIGHT)
            color = random.choice(colors)
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    @staticmethod
    def generate_gradient_shift(canvas):
        colors = ['#ADD8E6', '#90EE90', '#D3D3D3']
        for i in range(10):
            x1 = RandomArtGenerator.WIDTH / 10 * i
            y1 = 0
            x2 = RandomArtGenerator.WIDTH / 10 * (i + 1)
            y2 = RandomArtGenerator.HEIGHT
            color = random.choice(colors)
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    @staticmethod
    def generate_polygons(canvas):
        colors = ['#ADD8E6', '#90EE90', '#D3D3D3']
        for _ in range(15):
            num_points = random.randint(3, 8)
            points = [(random.randint(0, RandomArtGenerator.WIDTH), random.randint(0, RandomArtGenerator.HEIGHT)) 
                      for _ in range(num_points)]
            color = random.choice(colors)
            canvas.create_polygon(points, fill=color)

    @staticmethod
    def generate_cubical(canvas):
        colors = ['#ADD8E6', '#90EE90', '#D3D3D3']
        for _ in range(5):
            x = random.randint(0, RandomArtGenerator.WIDTH)
            y = random.randint(0, RandomArtGenerator.HEIGHT)
            size = random.randint(20, 100)
            color = random.choice(colors)
            canvas.create_rectangle(x, y, x + size, y + size, fill=color)

    @staticmethod
    def generate_rubix(canvas):
        colors = ['#ADD8E6', '#90EE90', '#D3D3D3']
        for i in range(10):
            for j in range(10):
                x = RandomArtGenerator.WIDTH / 10 * i
                y = RandomArtGenerator.HEIGHT / 10 * j
                size = RandomArtGenerator.WIDTH / 10
                color = random.choice(colors)
                canvas.create_rectangle(x, y, x + size, y + size, fill=color)

    @staticmethod
    def generate_morse(canvas):
        colors = ['#ADD8E6', '#90EE90', '#D3D3D3']
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
        RandomArtGenerator.generate_squares(self.canvas)
        RandomArtGenerator.generate_circles(self.canvas)
        RandomArtGenerator.generate_strings(self.canvas)
        RandomArtGenerator.generate_spirals(self.canvas)
        RandomArtGenerator.generate_overlap(self.canvas)
        RandomArtGenerator.generate_gradient_shift(self.canvas)
        RandomArtGenerator.generate_polygons(self.canvas)
        RandomArtGenerator.generate_cubical(self.canvas)
        RandomArtGenerator.generate_rubix(self.canvas)
        RandomArtGenerator.generate_morse(self.canvas)

    def regenerate_artwork(self, event):
        self.generate_artwork()

def main():
    root = tk.Tk()
    app = RandomArtApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
class RandomArtApp:
    # Existing code...

    def generate_artwork(self):
        self.canvas.delete("all")  # Clear previous drawings

        # Draw "h" using squares
        self.draw_letter_h()

        # Draw "e" using squares
        self.draw_letter_e()

        # Draw "l" using squares
        self.draw_letter_l()

        # Draw "o" using squares
        self.draw_letter_o()

        # You can continue with other shapes if needed

    def draw_letter_h(self):
        size = 50
        x_start = 50
        y_start = 50
        for i in range(5):
            self.canvas.create_rectangle(x_start, y_start + size * i, x_start + size, y_start + size * (i + 1), fill="black")
        for i in range(2):
            self.canvas.create_rectangle(x_start + size * i, y_start + size * 2, x_start + size * (i + 1), y_start + size * 3, fill="black")

    def draw_letter_e(self):
        size = 50
        x_start = 150
        y_start = 50
        for i in range(5):
            self.canvas.create_rectangle(x_start, y_start + size * i, x_start + size, y_start + size * (i + 1), fill="black")
        self.canvas.create_rectangle(x_start, y_start, x_start + size * 2, y_start + size, fill="black")
        self.canvas.create_rectangle(x_start, y_start + size * 2, x_start + size * 2, y_start + size * 3, fill="black")
        self.canvas.create_rectangle(x_start, y_start + size * 4, x_start + size * 2, y_start + size * 5, fill="black")

    def draw_letter_l(self):
        size = 50
        x_start = 300
        y_start = 50
        for i in range(5):
            self.canvas.create_rectangle(x_start, y_start + size * i, x_start + size, y_start + size * (i + 1), fill="black")
        self.canvas.create_rectangle(x_start, y_start + size * 4, x_start + size * 2, y_start + size * 5, fill="black")

    def draw_letter_o(self):
        size = 50
        x_start = 450
        y_start = 50
        for i in range(5):
            self.canvas.create_rectangle(x_start, y_start + size * i, x_start + size, y_start + size * (i + 1), fill="black")
        for i in range(2):
            self.canvas.create_rectangle(x_start + size * i, y_start, x_start + size * (i + 1), y_start + size, fill="black")
            self.canvas.create_rectangle(x_start + size * i, y_start + size * 4, x_start + size * (i + 1), y_start + size * 5, fill="black")
class RandomArtGenerator:
    # Existing code...

    @staticmethod
    def generate_squares(canvas):
        colors = ['#00BFFF', '#00FF7F', '#D3D3D3']  # Vibrant blue, vibrant green, light grey
        for _ in range(20):
            x = random.randint(0, RandomArtGenerator.WIDTH)
            y = random.randint(0, RandomArtGenerator.HEIGHT)
            size = random.randint(20, 100)
            color = random.choice(colors)
            canvas.create_rectangle(x, y, x + size, y + size, fill=color)

    @staticmethod
    def generate_circles(canvas):
        colors = ['#00BFFF', '#00FF7F', '#D3D3D3']  # Vibrant blue, vibrant green, light grey
        for _ in range(30):
            x = random.randint(0, RandomArtGenerator.WIDTH)
            y = random.randint(0, RandomArtGenerator.HEIGHT)
            size = random.randint(20, 100)
            color = random.choice(colors)
            canvas.create_oval(x, y, x + size, y + size, fill=color)

    # Repeat the same for other shapes...
