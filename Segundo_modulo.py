import tkinter as tk
from tkinter import messagebox
import subprocess
from  tkinter import filedialog
main=tk.Tk()
main.title("Soporte y validación usando DSSS")
main.geometry("800x800")

etiqueta_url=tk.Label(main,text="Ponga un URL")
etiqueta_url.pack()
entrada_url=tk.Entry(main,width=30)
entrada_url.pack()
resultados_listbox=tk.Listbox(main,width=65,height=35)
resultados_listbox.pack()

def ejecutar_dsss():
    url=entrada_url.get()
    direccion_dsss = "C:/Users/usuario/PycharmProjects/DSSS-master"
    comando = f"python {direccion_dsss}/dsss.py -u {url}"
    proceso = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    salida, error = proceso.communicate()
    salida = salida.decode("utf-8")

    resultados_listbox.delete(0, tk.END)
    lineas=salida.split("\n")
    for linea in lineas:
        resultados_listbox.insert(tk.END,linea)
def guardar_resultados():
    resultados=resultados_listbox.get(0,tk.END)
    ruta_archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de Texto", "*.txt")])
    if ruta_archivo:
     with open(ruta_archivo,"w" ) as archivo:
        for resultado in resultados:
            archivo.write(resultado+"\n")

    messagebox.showinfo("Guardado","Los resultados se han guardado corrrectamente.")

ejecutar_boton=tk.Button(main,text="Correr",command=ejecutar_dsss)
ejecutar_boton.pack()
guardar_boton=tk.Button(main,text="Guardar",command=guardar_resultados)
guardar_boton.pack()
main.mainloop()
