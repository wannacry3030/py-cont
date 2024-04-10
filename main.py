import tkinter as tk
from tkinter import messagebox
import csv 
from datetime  import datetime
import os

csv_file_path = "total_envios.csv"

def adicionar_envio():
    data_atual = datetime.now().strftime("%Y-%m-%d")
    try:
        if os.path.exists(csv_file_path):
            modo_abertura = 'a'
        else:
            modo_abertura = "w"
            
        with open(csv_file_path, modo_abertura, newline='')  as file:
              writer = csv.writer(file)
              if modo_abertura == 'w':
                  writer.writerow(["Data", "Quantidade"])
              writer.writerow([data_atual, 1])
        messagebox.showinfo("Sucesso", "Envio registrado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao registrar o envio: {e}")
        
def exibir_relatorio():
    try:
        if not os.path.exists(csv_file_path):
            messagebox.showinfo("Relatório", "Nenhum envio de currículo registrado até o momento.")
            return
          
        envios = {}
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Data"] in envios:
                    envios[row["Data"]] += 1
                else:
                    envios[row["Data"]] = 1
                    
        relatorio = "Relatório de Envios de Currículos:\n\n"
        for data, quantidade in envios.items():
            relatorio += f"Data: {data}, quantidade: {quantidade}\n"
            
        messagebox.showinfo("Relatório de Envios", relatorio)
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao gerar o relatório: {e}")
        
def criar_interface():
    janela = tk.Tk()
    janela.title("Contador de Envios de Currículo")
    
    btn_adicionaar_envio = tk.Button(janela, text="Registrar Envio de Currículo", command=adicionar_envio)
    btn_adicionaar_envio.pack(pady=10)
    
    btn_exibir_relatorio = tk.Button(janela, text="Exibir Relatório", command=exibir_relatorio)
    btn_exibir_relatorio.pack(pady=10)
    
    janela.mainloop()
    
criar_interface()