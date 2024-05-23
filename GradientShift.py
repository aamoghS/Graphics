import random
import tkinter as tk

class GradientShift(tk.Canvas):
    WIDTH = 2000
    HEIGHT = 2000
    RECT_WIDTH = 10  

    def __init__(self, master=None, **kwargs):
        super().__init__(master, width=GradientShift.WIDTH, height=GradientShift.HEIGHT, **kwargs)
        self.grid()  

        self.draw_gradient()
        self.bind("<Button-1>", self.draw_new_gradient)  

    def draw_gradient(self):
        choice = random.randint(0, 9)
        
        c1 = random.randint(0, 255)
        c2 = random.randint(0, 255)
        c3 = random.randint(0, 255)

        for x in range(GradientShift.WIDTH // GradientShift.RECT_WIDTH): 
            if choice == 0:
                color = f'#{max(0, c1 - (x // (GradientShift.WIDTH // GradientShift.RECT_WIDTH))):02x}{min(255, c2 + x):02x}{min(255, c3 + (x // 4)):02x}'
            elif choice == 1:
                color = f'#{c1:02x}{min(255, c2 + x):02x}{c3:02x}'
            elif choice == 2:
                color = f'#{min(255, c3 + (x // 4)):02x}{min(255, c2 + x):02x}{25:02x}'
            elif choice == 3:
                color = f'#{min(255, x + (c1 // 8)):02x}{min(255, c2 + (c3 // 2)):02x}{min(255, c3 + c2):02x}'
            elif choice == 4:
                color = f'#{max(0, 201 - x):02x}{min(255, c2 + x):02x}{min(255, c3 + (x // 5)):02x}'
            elif choice == 5:
                color = f'#{min(255, (c1 // 4) + 150):02x}{min(255, c2 + x):02x}{min(255, c3 + (x // 4)):02x}'
            elif choice == 6:
                color = f'#{max(0, 252 - x):02x}{min(255, c2 + c3):02x}{min(255, c2 + (2 * x // 3)):02x}'
            elif choice == 7:
                color = f'#{max(0, 74 - (x // 4)):02x}{min(255, c2 + x):02x}{min(255, c3 + 1 + (x // 4)):02x}'
            elif choice == 8:
                color = f'#{min(255, (x // 7) + x):02x}{min(255, c2 + x):02x}{min(255, c3 + (x // 4)):02x}'
            else:
                color = f'#00{max(0, 231 - x):02x}{min(255, 5 * (c3 // 8) + 50):02x}'

            self.create_rectangle(GradientShift.RECT_WIDTH * x, 0, GradientShift.RECT_WIDTH * (x + 1), GradientShift.HEIGHT, fill=color, outline='')

    def draw_new_gradient(self, event):
        self.delete("all")  
        self.draw_gradient()  

def main():
    root = tk.Tk()
    app = GradientShift(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()
