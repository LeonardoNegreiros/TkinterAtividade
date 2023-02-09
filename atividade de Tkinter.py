from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import colorchooser

root = Tk()
root.title('Atividade de Tkinter')
root.geometry("800x600")
root.config(cursor="pirate")

def colorpicker():
    cor = colorchooser.askcolor()[1]
    root.config(bg=cor)


Tela = Canvas(root, width=600, height=400, bg="white")
Tela.pack(pady=20)

def fileselect():
    global img
    root.filename = filedialog.askopenfilename(initialdir="/c", title="Selecione um arquivo", 
                                            filetypes=(("png files", "*.png"),("all files","*.*")))
    img = ImageTk.PhotoImage(Image.open(root.filename))
    Tela.create_image(300, 300, image=img)

botao1 = Button(root, text="Cor", cursor="spider", command=colorpicker)
botao1.pack(pady=20)
botao2 = Button(root, text="Arquivo", cursor="trek", command=fileselect)
botao2.pack(pady=20)

root.mainloop()