import tkinter
print('Anas Ahmed')
print('18B-116-cs')
print('LAb 13')
print('P 08')

window = tkinter.Tk()
window.title("My GUI with Menu")
def function():
    pass
# creating a root menu to insert all the sub menus
root_menu = tkinter.Menu(window)
window.config(menu = root_menu)

# creating sub menus in the root menu
file_menu = tkinter.Menu(root_menu) # it intializes a new sub menu in the root menu
root_menu.add_cascade(label = "File", menu = file_menu) # it createsthe name of the sub menu
file_menu.add_command(label = "New file.....", command = function) #it adds a option to the sub menu 'command' parameter is used to dosome action
file_menu.add_command(label = "Open files", command = function)
file_menu.add_separator() # it adds a line after the 'Open files'option
file_menu.add_command(label = "Exit", command = window.quit)

# creting another sub menu
edit_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Undo", command = function)
edit_menu.add_command(label = "Redo", command = function)

window.mainloop()
