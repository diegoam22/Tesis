import tkinter as tk
from tkinter import filedialog
#Este modulo se trata sobre cargar los resultados en un reporte
main=tk.Tk()
main.title("Reporte")
main.geometry("800x800")

def cargar_resultados():
    ruta_archivos=filedialog.askopenfilenames(filetypes=[("Archivos de texto","*.txt")])
    for ruta_archivo in ruta_archivos:
        with open(ruta_archivo,"r") as archivo:
            leer_contenido=archivo.read()
            texto_reporte.insert(tk.END,f"\n\nContenido del archivo:{ruta_archivo}\n\n")
            texto_reporte.insert(tk.END,leer_contenido)

cargar_boton=tk.Button(main,text="Cargar archivo",command=cargar_resultados)
cargar_boton.pack()
texto_reporte=tk.Text(main,width=60,height=40)
texto_reporte.pack()

main.mainloop()
