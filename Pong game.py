from tkinter import *
import time
import random


counter1 = 0
counter2 = 0
tk = Tk()
tk.title("Pong")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk, width = 500, height = 400, bd = 0, highlightthickness = 0)
canvas.config(bg = "black")
canvas.pack()
tk.update()

canvas.create_line(250,0,250,400,fill = "white")

class Ball:
    def __init__(self, canvas, paddle1, paddle2, color):
        self.canvas = canvas
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        self.id = canvas.create_oval(10,10,25,25, fill = color)
        self.canvas.move(self.id, 235, 200)
        self.counter1 = 0
        self.counter2 = 0
        
        start = [-2, -1, 1, 2]
        random.shuffle(start)
        self.y = start[0]
        self.x = -2
        
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_side = False

    def Hit_paddle1(self, pos):
        paddle1_pos = self.canvas.coords(self.paddle1.id)
        if pos[3] >= paddle1_pos[1] and pos[1] <= paddle1_pos[3]:
            if pos[0] >= paddle1_pos[0] and pos[0] <= paddle1_pos[2]:
                return True
            return False
        
    def Hit_paddle2(self, pos):
        paddle2_pos = self.canvas.coords(self.paddle2.id)
        if pos[3] >= paddle2_pos[1] and pos[1] <= paddle2_pos[3]:
            if pos[2] >= paddle2_pos[0] and pos[0] <= paddle2_pos[2]:
                return True
            return False        
    
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        
        if pos[1] <= 0:
            self.y = 2
        if pos[3] >= self.canvas_height:
            self.y = -2
        if pos[0] <= 0:
            self.x = 2
            self.score(False)
        if pos[2] >= self.canvas_width:
            self.x = -2
            self.score(True)

        if self.Hit_paddle1(pos) == True:
            self.x = 3
        if self.Hit_paddle2(pos) == True:
            self.x = -3
            
    def score(self, val):
        global counter1
        global counter2

        if val == True:
            a = self.canvas.create_text(125, 40, font = ("Gotham", 18), text = "Blue: " + str(counter1), fill = "white")
            canvas.itemconfig(a, fill = "black")
            counter1 += 1
            a = self.canvas.create_text(125, 40, font = ("Gotham", 18), text = "Blue: " + str(counter1), fill = "white")

        if val == False:
            b = self.canvas.create_text(375, 40, font = ("Gotham", 18), text = "Red: " + str(counter2), fill = "white")
            canvas.itemconfig(b, fill = "black")
            counter2 += 1
            b = self.canvas.create_text(375, 40, font = ("Gotham", 18), text = "Red: " + str(counter2), fill = "white")
            
class Paddle1:
    def __init__(self, canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 15, 70, fill = color)
        self.y = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        
        self.canvas.move(self.id, 0, self.canvas_height/2 - 35)
        
        self.canvas.bind_all('w', self.move_up)
        self.canvas.bind_all('s', self.move_down)
            
    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        
        if pos[1] <= 0 or pos[3] >= self.canvas_height:
            self.y = 0
            
    def move_up(self, evt):
        pos = self.canvas.coords(self.id)
        if pos[1] > 0:
            self.y = -2
    def move_down(self, evt):
        pos = self.canvas.coords(self.id)
        if pos[3] < self.canvas_height:
            self.y = 2

class Paddle2:
    def __init__(self, canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 15, 70, fill = color)
        self.y = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        
        self.canvas.move(self.id, self.canvas_width - 15, self.canvas_height/2 - 25)
        
        self.canvas.bind_all('<KeyPress-Up>', self.move_up)
        self.canvas.bind_all('<KeyPress-Down>', self.move_down)
            
    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        
        if pos[1] <= 0 or pos[3] >= self.canvas_height:
            self.y = 0
            
    def move_up(self, evt):
        pos = self.canvas.coords(self.id)
        if pos[1] > 0:
            self.y = -2
    def move_down(self, evt):
        pos = self.canvas.coords(self.id)
        if pos[3] < self.canvas_height:
            self.y = 2


paddle1 = Paddle1(canvas, "blue")
paddle2 = Paddle2(canvas, "red")
ball = Ball(canvas, paddle1, paddle2, "orange")

while True:
    ball.draw()
    paddle1.draw()
    paddle2.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
