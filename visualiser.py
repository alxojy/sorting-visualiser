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


def update_fig(A, rects, iteration):
    for rect, val in zip(rects, randomlist):
        rect.set_height(val)
        iteration[0] += 1

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
            ax.set_title("Bubble Sort")
            anim = animation.FuncAnimation(fig, func=update_fig,
            fargs=(bar_rects, iteration), frames=bubble_sort(randomlist), interval=100,
            repeat=False)

            plt.show()

        elif sort_option.upper() == 'B':
            ax.set_title("Heap Sort")
            anim = animation.FuncAnimation(fig, func=update_fig,
            fargs=(bar_rects, iteration), frames=heap_sort(randomlist), interval=100,
            repeat=False)
            plt.show()

        elif sort_option.upper() == 'C':
            ax.set_title("Insertion Sort")
            anim = animation.FuncAnimation(fig, func=update_fig,
            fargs=(bar_rects, iteration), frames=insertion_sort(randomlist), interval=100,
            repeat=False)
            plt.show()

        elif sort_option.upper() == 'D':
            ax.set_title("Merge Sort")
            anim = animation.FuncAnimation(fig, func=update_fig,
            fargs=(bar_rects, iteration), frames=merge_sort(randomlist,0,n-1), interval=50,
            repeat=False)
            plt.show()

        elif sort_option.upper() == 'E':
            ax.set_title("Quick Sort")
            anim = animation.FuncAnimation(fig, func=update_fig,
            fargs=(bar_rects, iteration), frames=quick_sort(randomlist,0,n-1), interval=100,
            repeat=False)
            plt.show()
        
        elif sort_option.upper() == 'F':
            ax.set_title("Radix Sort")
            anim = animation.FuncAnimation(fig, func=update_fig,
            fargs=(bar_rects, iteration), frames=radix_sort(randomlist), interval=100,
            repeat=False)
            plt.show()
        
        elif sort_option.upper() == 'G':
            ax.set_title("Selection Sort")
            anim = animation.FuncAnimation(fig, func=update_fig,
            fargs=(bar_rects, iteration), frames=selection_sort(randomlist), interval=100,
            repeat=False)
            plt.show()
        
        elif sort_option.upper() == 'H':
            ax.set_title("Shell Sort")
            anim = animation.FuncAnimation(fig, func=update_fig,
            fargs=(bar_rects, iteration), frames=shell_sort(randomlist), interval=100,
            repeat=False)
            plt.show()
        
        elif sort_option.upper() == 'Q':
            quit()
        
        else:
            pass
        

