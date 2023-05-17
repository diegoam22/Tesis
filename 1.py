import pickle
import tkinter as tk
import pandas as pd
from tkinter.filedialog import asksaveasfilename
from tkinter import *

main=tk.Tk()
main.title("Personalize una regla")
main.geometry('800x500+0+0')
lbreglas=tk.Label(main,text="Agregue una regla:").place(x=100,y=10)#etiqueta reglas
#Lista reglas
listareglas=tk.Listbox(main,width=100)#Creas una lista
listareglas.place(x=100,y=100)
lista=["1=1,","1'+ sleep(10),","1'| sleep(10),","1'|| pg_sleep(10),","1'|| 1' WAITFOR DELAY '0:0:10',",
"1' AND 123=DBMS_PIPE.RECEIVE_MESSAGE('ASD',10),","1' AND [RANDNUM]=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB([SLEEPTIME]00000000/2))),"
]
lista_columnas=["Expresiones"]
for item in lista:
    listareglas.insert(tk.END,item)
barra=Scrollbar(main)
barra.pack(side=RIGHT,fill=BOTH)
listareglas.config(yscrollcommand=barra.set)
barra.config(command=listareglas.yview)
entrada=tk.StringVar()
entrada_regla=tk.Entry(main,textvariable=entrada,width=40)
entrada_regla.place(x=250,y=10)
#Funcion agregar boton
def agregar():
    print("Si se agrego")
    listareglas.insert(tk.END,entrada.get())
    lista.append(entrada.get()+",")
    print(lista)
#Se configura los botones
botonadd=tk.Button(main,text="Agregar",height=1,width=20,command=agregar).place(x=500,y=10)
def guardar():
    print("si se guardo")
    archivo=asksaveasfilename(filetypes=[('CSV (MS-DOS)','*.csv')])#'CSV files','*.csv
    if archivo:
        #data={lista} ponerle "Expresiones,":lista
        df=pd.DataFrame(lista,columns=lista_columnas)
        df.to_csv(archivo,index=False)
        df=pd.read_csv(archivo)
    print(df)
guardar=tk.Button(main,text="Guarda r",command=guardar,width=20).place(x=500,y=40)



main.mainloop()

