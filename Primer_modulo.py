import tkinter as tk
import subprocess
from tkinter import messagebox
from tkinter import filedialog
#En este modulo se integro la herramienta Mysqlmap para poder encontrar sentencia sql
#y validarlo junto a esta herramienta y en el tercer modulo se va a comparar esas sentencias SQL
#con las reglas que hemos propuesto
main=tk.Tk()
main.title("Detectar y validar sentencia SQL usando SQLMap")
main.geometry("700x700")
etiqueta_url=tk.Label(main,text="Ponga un URL")
entrada_url=tk.Entry(main,width=50)
salida_listbox=tk.Listbox(main,width=100,height=30)
etiqueta_url.pack()
entrada_url.pack()
salida_listbox.pack()
def sqlmap():
    url=entrada_url.get()
    direccion_sqlmap="C:/Users/usuario/PycharmProjects/sqlmap-dev"
    comando= f"python {direccion_sqlmap}/sqlmap.py -u {url}"
    #salida=subprocess.check_output(comando,shell=True)ç
    proceso = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    salida, error = proceso.communicate()
    salida = salida.decode("utf-8")

    salida_listbox.delete(0,tk.END)
    lineas = salida.split("\n")
    for linea in lineas:
        salida_listbox.insert(tk.END,linea)
def guardar_resultados():
    resultados=salida_listbox.get(0,tk.END)
    ruta_archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de Texto", "*.txt")])
    if ruta_archivo:
     with open(ruta_archivo,"w") as archivo:
        for resultado in resultados:
            archivo.write(resultado+"\n")
    messagebox.showinfo("Guardado","Los resultados se guardaron correctamente")

boton_correr=tk.Button(main,text="Correr",command=sqlmap,width=10)
boton_correr.pack()
boton_guardar=tk.Button(main,text="Guardar resultados SQLMap",command=guardar_resultados,width=20)
boton_guardar.pack()
main.mainloop()
