import os
import tkinter as tk
import tkinter.messagebox as messagebox
import qrcode
import webbrowser

# Variável para armazenar o contador
contador_qr_code = 1

def gerar_qr_code():
    global contador_qr_code  # Acessa a variável global do contador
    link = link_entry.get()

    # Verifica se o campo está vazio
    if not link:
        messagebox.showerror("Erro", "Por favor, digite um link.")
        return

    # Gera o QR Code
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(link)
    qr.make(fit=True)

    # Define o nome do arquivo
    file_name = f"QRCode_{contador_qr_code}.png"

    # Verifica se o arquivo com o nome já existe na área de trabalho
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, file_name)
    while os.path.exists(file_path):
        contador_qr_code += 1
        file_name = f"QRCode_{contador_qr_code}.png"
        file_path = os.path.join(desktop_path, file_name)

    # Salva o QR Code como imagem
    qr_image = qr.make_image(fill="black", back_color="white")
    qr_image.save(file_path)

    # Incrementa o contador
    contador_qr_code += 1

    # Exibe a mensagem de sucesso
    messagebox.showinfo("Sucesso", f"QR Code gerado com sucesso! O arquivo '{file_name}' foi salvo na área de trabalho.")

# Cria a janela principal
window = tk.Tk()
window.title("Gerador de QR Code - por Gabriel ℣eras")
window.geometry("400x150")
window.resizable(False, False)  # Trava a janela de ser redimensionada

# Incluir símbolo ℣
symbol_label = tk.Label(window, text="📷 ℣", font=("DejaVu Sans", 30))
symbol_label.pack()

# Incluir instruções
instructions_label = tk.Label(window, text="Digite abaixo o link para gerar seu QR Code:", font=("DejaVu Sans", 12))
instructions_label.pack()

link_entry = tk.Entry(window, width=50)
link_entry.pack()

gerar_button = tk.Button(window, text="Gerar QR Code", command=gerar_qr_code)
gerar_button.pack()

def abrir_site(event):
    webbrowser.open("http://www.gabrielveras.art")

# Cria o link clicável para o seu site
link_label = tk.Label(window, text="Créditos: Gabriel ℣eras", font=("DejaVu Sans", 8), fg="blue", cursor="hand2")
link_label.pack()
link_label.bind("<Button-1>", abrir_site)

window.mainloop()
