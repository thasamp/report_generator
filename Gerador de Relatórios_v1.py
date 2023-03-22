# Criado com Python 3.7
import os
import re
from os import path
import tkinter as tk
from tkinter import filedialog
from tkinter import OptionMenu
from tkinter import StringVar
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER

PATH = os.getcwd()
print(f'Diretório atual: {os.getcwd()}')
#print(f'Diretório desejado: {os.path.join(PATH,'/static/bg2.png')}')

def import_string(entry):
    filtro = re.sub(u'[^a-zA-ZÀ-ÿ0-9:&-., ]', '',entry)
    return filtro

# função para salvar o relatório em PDF
def generate_report():
    # salvando strings
    str_orgao = import_string(entry0.get())
    str_ticket = import_string(entry1.get())
    str_endereco = import_string(entry2.get())
    str_tipo = import_string(entry3.get())
    str_coordenada = import_string(entry4.get())
    
    # abre o diálogo para escolher o local de salvamento do relatório
    filename = filedialog.asksaveasfilename(defaultextension=".pdf", 
                                            initialfile=f"RF_{str_orgao}_{str_ticket}_{str_endereco}.pdf", 
                                            filetypes=[("PDF files", "*.pdf")])
    
    # cria o relatório em PDF
    c = canvas.Canvas(filename, pagesize=letter)
    
    
    # initial set
    bg2 = Image.open('static/bg2.png')
    c.drawImage('static/bg2.png', 0, 0, width=letter[0], height=letter[1])
    c.translate(0,-100)
    
    # set style
    style = getSampleStyleSheet()['Normal']
    style.alignment = TA_CENTER
    
    # set text
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(300, 750, "Relatório Fotográfico")
    
    c.setFont("Helvetica-Bold", 12)

    c.drawCentredString(300, 700, f"{str_endereco} ({str_tipo})")
    c.drawCentredString(300, 680, f"{str_coordenada}")
 #   c.drawCentredString(300, 660, f"Tipo: {entry2.get()}")
    c.drawCentredString(300, 660, f"Ticket: {str_ticket}")

    c.setFont("Helvetica", 9)
    c.drawCentredString(230, 435, "(a) Poste")
    c.drawCentredString(380, 435, "(b) Detalhe da câmera")
    c.drawCentredString(300, 225, "(c) Imagem da câmera")

    
    # insere as imagens no relatório
    img1 = Image.open(entry_img1.get())
    c.drawImage(entry_img1.get(), 150, 450, width=150, height=180)
    
    img2 = Image.open(entry_img2.get())
    c.drawImage(entry_img2.get(), 310, 450, width=150, height=180)

    img3 = Image.open(entry_img3.get())
    c.drawImage(entry_img3.get(), 150, 240, width=310, height=180)
    
    # salva o relatório
    c.setTitle(f"RF_{str_orgao}_{str_ticket}")
    c.save()

# cria a GUI
root = tk.Tk()

# cria as entradas de texto


label0 = tk.Label(root, text="Órgão: ")
label0.grid(row=0, column=0)
entry0 = tk.Entry(root)
entry0.grid(row=0, column=1)

label1 = tk.Label(root, text="Ticket: ")
label1.grid(row=1, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=1, column=1)

label2 = tk.Label(root, text="Endereço: ")
label2.grid(row=2, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=2, column=1)


label3 = tk.Label(root, text="Tipo: ")
label3.grid(row=3, column=0)
entry3 = tk.Entry(root)
entry3.grid(row=3, column=1)

label4 = tk.Label(root, text="Coordenadas: ")
label4.grid(row=4, column=0)
entry4 = tk.Entry(root)
entry4.grid(row=4, column=1)

# cria as entradas de imagem
label_img1 = tk.Label(root, text="Poste câmera")
label_img1.grid(row=5, column=0)
entry_img1 = tk.Entry(root)
entry_img1.grid(row=5, column=1)

button_img1 = tk.Button(root, text="Escolher imagem", command=lambda: entry_img1.insert(0, filedialog.askopenfilename()))
button_img1.grid(row=5, column=2)

label_img2 = tk.Label(root, text="Detalhe câmera")
label_img2.grid(row=6, column=0)
entry_img2 = tk.Entry(root)
entry_img2.grid(row=6, column=1)

button_img2 = tk.Button(root, text="Escolher imagem", command=lambda: entry_img2.insert(0, filedialog.askopenfilename()))
button_img2.grid(row=6, column=2)

label_img3 = tk.Label(root, text="Visada câmera")
label_img3.grid(row=7, column=0)
entry_img3 = tk.Entry(root)
entry_img3.grid(row=7, column=1)

button_img3 = tk.Button(root, text="Escolher imagem", command=lambda: entry_img3.insert(0, filedialog.askopenfilename()))
button_img3.grid(row=7, column=2)

# cria o botão para gerar o relatório
button_report = tk.Button(root, text="Gerar relatório", command=generate_report)
button_report.grid(row=8, column=1)

label_credits = tk.Label(root, text="Desenvolvido por Thaís Sampaio")
label_credits.grid(row=9, column=1)

menu= StringVar()
menu.set("Select Any Language")


# inicia a GUI

root.title('Gerador de Relatórios')

root.mainloop()
