# import sorting algorithms
from sorting_algorithms.bubble_sort import bubble_sort
from sorting_algorithms.heap_sort import heap_sort
from sorting_algorithms.insertion_sort import insertion_sort
from sorting_algorithms.merge_sort import merge_sort
from sorting_algorithms.quick_sort import quick_sort
from sorting_algorithms.radix_sort import radix_sort
from sorting_algorithms.selection_sort import selection_sort
from sorting_algorithms.shell_sort import shell_sort

# other import statements
import random
import os
import sys
import re

# for visualisation 
from matplotlib import pyplot as plt
import matplotlib.animation as animation

# ref: https://github.com/nrsyed/sorts/blob/master/python/sorts.py
def update_fig(A, rects, iteration):
    for rect, val in zip(rects, randomlist):
        rect.set_height(val)
        iteration[0] += 1

def animate(title, args, sort_func):
    ax.set_title(title)
    anim = animation.FuncAnimation(fig, func=update_fig,
    fargs=args, frames=sort_func, interval=100,
    repeat=False)
    plt.show()

if __name__ == "__main__":
    while True:
        randomlist = []
        n = 30
        for i in range(0, n):
            randomlist.append(random.randint(1, 50))

        fig, ax = plt.subplots()
        bar_rects = ax.bar(range(len(randomlist)), randomlist, align="edge")
        text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
        iteration = [0]

        # input text
        sort_option = input("Which sort would you like to visualise? Enter the first alphabet:  \n"
        + "(A) Bubble sort \n(B) Heap sort \n(C) Insertion sort \n(D) Merge sort \n(E) Quick sort \n" + 
        "(F) Radix sort \n(G) Selection sort \n(H) Shell sort \n(Q) Quit \n")

        # sorting options
        if sort_option.upper() == 'A':
            animate("Bubble Sort", (bar_rects, iteration), bubble_sort(randomlist))

        elif sort_option.upper() == 'B':
            animate("Heap Sort", (bar_rects, iteration), heap_sort(randomlist))

        elif sort_option.upper() == 'C':
            animate("Insertion Sort", (bar_rects, iteration), insertion_sort(randomlist))

        elif sort_option.upper() == 'D':
            animate("Merge Sort", (bar_rects, iteration), merge_sort(randomlist))

        elif sort_option.upper() == 'E':
            animate("Quick Sort", (bar_rects, iteration), quick_sort(randomlist))
        
        elif sort_option.upper() == 'F':
            animate("Selection Sort", (bar_rects, iteration), selection_sort(randomlist))
        
        elif sort_option.upper() == 'G':
            animate("Shell Sort", (bar_rects, iteration), shell_sort(randomlist))
        
        elif sort_option.upper() == 'Q':
            quit()
            
        else:
            pass
        

