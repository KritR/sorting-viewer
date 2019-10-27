from tkinter import *
import time
import numpy as np

HEIGHT = 600
WIDTH = 800

class DrawingBoard:
    def __init__(self):
        self.master = Tk()
        self.w = Canvas(self.master, width=WIDTH, height=HEIGHT)
        self.w.pack()

    def update(self):
        #self.master.update_idletasks()
        self.master.update()


def gen_lines(board, arr):
    disp = board.w
    return [disp.create_line(i,HEIGHT, i, HEIGHT - val/2) for i, val in enumerate(random_nums)]

def selection_sort(A, board):
    lines = gen_lines(board, A)
    for i in range(len(A)): 
        # Find the minimum element in remaining  
        # unsorted array 
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j 
                  
        # Swap the found minimum element with  
        # the first element         
        A[i], A[min_idx] = A[min_idx], A[i]
        lines[i], lines[min_idx] = lines[min_idx], lines[i]
        board.w.coords(lines[i], [i, HEIGHT, i, HEIGHT - (A[i])/2])
        board.w.coords(lines[min_idx], [min_idx,HEIGHT, min_idx, HEIGHT - (A[min_idx])/2])
        board.update()
    for i in lines:
        board.w.itemconfig(i, fill="green")
        board.update()

board = DrawingBoard()
random_nums = np.arange(WIDTH)
np.random.shuffle(random_nums)
selection_sort(random_nums, board)
