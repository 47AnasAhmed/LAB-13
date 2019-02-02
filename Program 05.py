import tkinter
print('Anas Ahmed')
print('18B-116-cs')
print('LAb 13')
print('P 05')

window = tkinter.Tk()
window.title("Binding Functions")
# creating a function called say_Assalam_o_Alekum()
def say_Assalam_o_Alekum():
    tkinter.Label(window, text = "Assalam o Alekum").pack()
tkinter.Button(window, text = "Click Me!", command =say_Assalam_o_Alekum).pack()
# 'command' is executed when you click the button in this above case we're calling the function 'say_Assalam_o_Alekum'.
window.mainloop()
