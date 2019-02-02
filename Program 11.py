import tkinter
print('Anas Ahmed')
print('18B-116-cs')
print('LAb 13')
print('P 11')

window = tkinter.Tk()
window.title("Image or Logo on GUI")
# taking image from the directory and storing the source in a variable
icon = tkinter.PhotoImage(file = "UITlogo.png")
# displaying the picture using a 'Label' by passing the 'picture' variriable to 'image' parameter
label = tkinter.Label(window, image = icon)
label.pack()

window.mainloop()
