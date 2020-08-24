from tkinter import *
import time
import random

tk = Tk()
tk.title("Bounce")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk, width = 500, height = 500, bd = 0, highlightthickness = 0)
canvas.pack()
tk.update()


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25, fill = color)
        self.canvas.move(self.id, 245, 100)
        
        start = [-3, -2, -1, 1, 2, 3]
        random.shuffle(start)
        self.x = start[0]
        self.y = -3
        
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def Hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                return True
            return False
        
    def Hit_brick(self, pos):
        brick_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
            if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                return True
            return False
        
    def draw(self, counter):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

        if self.Hit_paddle(pos) == True:
            self.y = -3
        if self.Hit_brick(pos) == True:
            self.y = -3

class Brick:
    def __init__(self, canvas, ball, color):
        self.canvas = canvas
        self.x = 20
        self.y = 25
        self.a = []
        self.canvas_width = self.canvas.winfo_width()
        
        for i in range (18): 
            self.id = canvas.create_rectangle(0,0,75,30 , fill = color)
            self.canvas.move(self.id, self.x, self.y)
            self.a.append(self.id)
            self.x += 77
            if (self.x + 57) >= self.canvas_width:
                self.y += 32
                self.x = 20
        print(self.a)
        
    def draw(self):
        pos = self.canvas.coords(self.a)
        
class Paddle:
    def __init__(self, canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill = color)
        self.canvas.move(self.id, 245, 450)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.move_left)
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)
            
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x = 0
            
    def move_left(self, evt):
        pos = self.canvas.coords(self.id)
        if pos[0] > 0:
            self.x = -2
    def move_right(self, evt):
        pos = self.canvas.coords(self.id)
        if pos[2] < self.canvas_width:
            self.x = 2

    
counter = 3
while counter != 0:
    paddle = Paddle(canvas, "black")
    ball = Ball(canvas, paddle, "red")
    brick = Brick(canvas, ball, "pink")
    canvas.create_text(40, 10, text = "Lives: " + str(counter), font = ("Gotham", 14)) 

    while True:
        ball.draw(counter)
        paddle.draw()
        brick.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
        if ball.hit_bottom == True:
            counter = counter - 1
            break
    canvas.delete("all")
    
    if counter == 0:
        canvas.create_text(245, 150, text = "Game Over!", font = ("Gotham", 28))
        
        break
