from tkinter import *
import time
from copy import deepcopy as dp

H = 20
W = 20

LW = 4

D = 30  

def init():
    life = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
    ]  
    l1 = len(life)
    for i in range(H):
        if i>=l1:
            life.append([])
        l2 = len(life[i])
        for j in range(l2, W):
            life[i].append(0)
    return life
    
def draw(canvas, life):
    for i in range(H):
        for j in range(W):
            if life[i][j]:
                canvas.create_rectangle(D*j+LW/2,D*i+LW/2,D*j-LW/2+D,D*i-LW/2+D,fill="blue")
            else:
                canvas.create_rectangle(D*j,D*i,D*j+D,D*i+D,fill="white")

def change_life(life):
    new_life = dp(life)
    for i in range(H):
        for j in range(W):
            n = 0
            if 0<=i-1<H and 0<=j-1<W: n+=life[i-1][j-1]
            if 0<=i-1<H: n+=life[i-1][j]
            if 0<=i-1<H and 0<=j+1<W: n+=life[i-1][j+1]
            if 0<=j+1<W: n+=life[i][j+1]
            if 0<=i+1<H and 0<=j+1<W: n+=life[i+1][j+1]
            if 0<=i+1<H: n+=life[i+1][j]
            if 0<=i+1<H and 0<=j-1<W: n+=life[i+1][j-1]
            if 0<=j-1<W: n+=life[i][j-1]
            print(n)
            if 1<n<4:
                new_life[i][j] = 1
            else:
                new_life[i][j] = 0
    return new_life

def main(life):
    window = Tk()
    window.title('Игра "Жизнь"')
    canvas = Canvas(window,width=W*D,height=H*D,bg="white")
    canvas.pack()
    draw(canvas, life)
    time.sleep(1)
    while True:
        life = change_life(life)
        draw(canvas, life)
        time.sleep(1)
        window.update()

if __name__ == "__main__":
    life = init()
    main(life)