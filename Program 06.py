import tkinter
print('Anas Ahmed')
print('18B-116-cs')
print('LAb 13')
print('P 06')

window = tkinter.Tk()
window.title("Capturing the Mouse Events on GUI")
#creating 3 different functions for 3 events
def left_click(event):
    tkinter.Label(window, text = "Left Click!").pack()
def middle_click(event):
    tkinter.Label(window, text = "Middle Click!").pack()
def right_click(event):
    tkinter.Label(window, text = "Right Click!").pack()
window.bind("<Button-1>", left_click)
window.bind("<Button-2>", middle_click)
window.bind("<Button-3>", right_click)
window.mainloop()
