import tkinter
print('Anas Ahmed')
print('18B-116-cs')
print('LAb 13')
print('P 01')

window = tkinter.Tk()
# to rename the title of the window
window.title("My Greetings")
# pack is used to show the object in the window
label = tkinter.Label(window, text = "Assalam O Alekum \n Welcome to UIT!").pack()
window.mainloop()
