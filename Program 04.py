import tkinter
print('Anas Ahmed')
print('18B-116-cs')
print('LAb 13')
print('P 04')

window = tkinter.Tk()
window.title("My Login Window")
# creating 2 text labels and input labels
tkinter.Label(window, text = "Username").grid(row = 0) # this isplaced in 0 0
# 'Entry' is used to display the input-field
tkinter.Entry(window).grid(row = 0, column = 1) # this is placed in 01
tkinter.Label(window, text = "Password").grid(row = 1) # this isplaced in 1 0
tkinter.Entry(window).grid(row = 1, column = 1) # this is placed in 11
# 'Checkbutton' is used to create the check buttons
tkinter.Checkbutton(window, text = "Keep Me LoggedIn").grid(columnspan = 2)
# 'columnspan' tells to take the width of 2columns
# you can also use 'rowspan' in the similar manner
window.mainloop()
