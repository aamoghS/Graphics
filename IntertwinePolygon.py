import tkinter as tk
import random

class Polygon:

    def __init__(self):
        self.root = tk.Tk()
        self.canvas_width = 2000
        self.canvas_height = 1500
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg='black')
        self.canvas.pack()
        self.root.title('Random Polygons')
        self.root.protocol("WM_DELETE_WINDOW", self.quit)
        self.root.update()

        # Bind canvas click event
        self.canvas.bind('<Button-1>', self.create_new_polygon)

    def generate_polygon(self):
        num_points = random.randint(10, 1000)
        points = []
        for _ in range(num_points):
            x = 640 + int((random.randint(0, 7) ** 3) * (1 + random.randint(0, 1) * -2) * 2.50) + 1
            y = 380 + int((random.randint(0, 6) ** 3) * (1 + random.randint(0, 1) * -2) * 2.07) + 1
            #pygame creates inf, changing the int, the shape feature diverges as going out 
            points.extend([x, y])
        return points

    def draw_polygon(self, points):
        self.canvas.create_polygon(points, fill=self.random_color())

    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return f'#{r:02x}{g:02x}{b:02x}'

    def create_new_polygon(self, event):
        # Clear canvas
        self.canvas.delete("all")
        # Generate and draw new polygon
        polygon_points = self.generate_polygon()
        self.draw_polygon(polygon_points)

    def run(self):
        self.root.mainloop()

    def quit(self):
        self.root.destroy()

if __name__ == '__main__':
    polygon = Polygon()
    polygon.run()
