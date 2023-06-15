import tkinter as tk
import subprocess
#En este modulo se integro la herramienta Mysqlmap para poder encontrar sentencia sql
#y validarlo junto a esta herramienta y en el tercer modulo se va a comparar esas sentencias SQL
#con las reglas que hemos propuesto
main=tk.Tk()
main.title("Detectar y validar sentencia SQL")
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
    salida=subprocess.check_output(comando,shell=True)
    salida_listbox.delete(0,tk.END)
    for linea in salida.splitlines():
        salida_listbox.insert(tk.END,linea)
boton_correr=tk.Button(main,text="Correr",command=sqlmap,width=10)
boton_correr.pack()
main.mainloop()
