import csv
from tkinter import filedialog
import pandas as pd
import tkinter as tk
import pickle
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
main=tk.Tk()
main.title("Reporte")
main.geometry('1000x1000+0+0')

lb_subtitulo=tk.Label(main,text="Estas son las reglas usadas por el usuario").place(x=100,y=10)
listareglas_reporte=tk.Listbox(main,width=100)
listareglas_reporte.place(x=100,y=100)


def cargar():
    #main.nombre_archivo = filedialog.askopenfilename(initialdir="C:\\Users\\usuario\\Desktop\\Tesis",
     #                                          title="Escoga un archivo",
      #                                         filetypes=(("all files", "*.*"), ("Excel files", "*.csv")))
    ruta_seleccionada=filedialog.askopenfilename(initialdir="C:\\Users\\usuario\\Desktop\\Tesis",
                                               title="Escoga un archivo",
                                               filetypes=(("all files", "*.*"), ("Excel files", "*.csv")))

    archivo = open(ruta_seleccionada)#abre el archivo segun la ruta
    leer_archivo = csv.reader(archivo)#aca lee el archivo
    datos = list(leer_archivo)
    lista_nueva = []
    for x in list(range(0, len(datos))):
        lista_nueva.append(datos[x][0])
    print(lista_nueva)
    for x, y in enumerate(lista_nueva):#da el valor de la iteracion de la lista nueva
        listareglas_reporte.insert(x,y)#lo guardamos en lista_reglas que es listbox
cargar=tk.Button(main,text="Cargar Archivo",command=cargar,width=20).place(x=500,y=40)
lb_subtitulo2=tk.Label(main,text="Restringimos estas sentencias SQL").place(x=100,y=300)
listasql_reporte=tk.Listbox(main,width=100)
listasql_reporte.place(x=100,y=350)
lista_sql=["select title, link from post_table where id < 10 union select username, password from user_table; --;"
           ,"select * from comments WHERE post_id=1-SLEEP(15);" ]
for item in lista_sql:
    listasql_reporte.insert(tk.END,lista_sql)
lb_subtitulo3=tk.Label(main,text="Esta restriccion se debe a que:").place(x=100,y=540)
lb_subtitulo3=tk.Label(main,text="Estas expresiones coinciden con las expresiones prohibidas por el admin").place(x=100,y=560)

main.mainloop()

