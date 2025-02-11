import tkinter as tk
from googletrans import Translator

# Função para realizar a tradução
def traduzir():
    # Pega o texto inserido
    texto_original = entrada_texto.get("1.0", "end-1c")
    
    # Traduz o texto para o idioma escolhido
    resultado = translator.translate(texto_original, src=idioma_origem.get(), dest=idioma_destino.get())
    
    # Exibe a tradução na interface
    resultado_texto.config(state=tk.NORMAL)  # Habilita a caixa de texto para editar
    resultado_texto.delete("1.0", "end")  # Limpa o conteúdo anterior
    resultado_texto.insert(tk.END, resultado.text)  # Insere o texto traduzido
    resultado_texto.config(state=tk.DISABLED)  # Desabilita a caixa de texto para evitar edição

# Inicializa o tradutor
translator = Translator()

# Configuração da janela principal
root = tk.Tk()
root.title("Tradutor Simples")
root.geometry("500x600")
root.configure(bg="#f0f0f0")  # Cor de fundo suave

# Título do aplicativo
titulo = tk.Label(root, text="Tradutor Simples", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333")
titulo.pack(pady=10)

# Caixa de entrada de texto
entrada_texto = tk.Text(root, height=5, width=45, font=("Arial", 12), bd=2, relief="solid", wrap=tk.WORD)
entrada_texto.pack(pady=10)

# Dropdown para escolher idioma de origem
idioma_origem = tk.StringVar(root)
idioma_origem.set("pt")  # Idioma padrão: português
idiomas = ['pt', 'en', 'es', 'fr', 'de', 'it', 'ja', 'zh-cn']
dropdown_origem = tk.OptionMenu(root, idioma_origem, *idiomas)
dropdown_origem.config(font=("Arial", 12), width=10, bg="#e0e0e0")
dropdown_origem.pack(pady=5)

# Dropdown para escolher idioma de destino
idioma_destino = tk.StringVar(root)
idioma_destino.set("en")  # Idioma padrão: inglês
dropdown_destino = tk.OptionMenu(root, idioma_destino, *idiomas)
dropdown_destino.config(font=("Arial", 12), width=10, bg="#e0e0e0")
dropdown_destino.pack(pady=5)

# Botão de tradução
botao_traduzir = tk.Button(root, text="Traduzir", command=traduzir, font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", relief="solid", bd=2)
botao_traduzir.pack(pady=15)

# Caixa de texto para exibir o resultado da tradução
resultado_texto = tk.Text(root, height=5, width=45, font=("Arial", 12), bd=2, relief="solid", wrap=tk.WORD, state=tk.DISABLED)
resultado_texto.pack(pady=10)

# Rodapé (opcional)
rodape = tk.Label(root, text="Traduzido por Python", font=("Arial", 10), bg="#f0f0f0", fg="#333")
rodape.pack(side=tk.BOTTOM, pady=10)

# Inicia o aplicativo
root.mainloop()
