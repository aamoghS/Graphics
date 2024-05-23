import tkinter as tk
import random

class Overlap(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.canvas = tk.Canvas(self, width=2000, height=1500)
        self.canvas.pack()
        self.draw()
        self.bind("<Button-1>", self.create_new_overlap)

    def draw(self):
        self.canvas.create_rectangle(0, 0, 2000, 1500, fill=self.random_color())
        
        xx, yy = -200, -200
        numof = random.randint(200, 1400)
        stepsize = 1400 // numof

        for _ in range(random.randint(20000, 40000)):
            color = self.random_color()
            self.canvas.create_rectangle(xx, yy, xx + random.randint(90, 100), yy + 100, fill=color)

            xx += stepsize
            yy += stepsize
            if xx > 1500:
                xx = -200
            if yy > 900:
                yy = -200

    def create_new_overlap(self, event):
        new_overlap = Overlap()
        new_overlap.mainloop()

    def random_color(self):
        return "#%02x%02x%02x" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

app = Overlap()
app.mainloop()
