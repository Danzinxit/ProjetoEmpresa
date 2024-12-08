import tkinter as tk
from tkinter import messagebox
from PIL import ImageGrab
import pytesseract
import threading
import os

os.environ['TCL_LIBRARY'] = r'C:\Users\Administrator\AppData\Local\Programs\Python\Python313\tcl\tcl8'
os.environ['TK_LIBRARY'] = r'C:\Users\Administrator\AppData\Local\Programs\Python\Python313\tcl\tk8.6'

# Configure o caminho para o executável do Tesseract se não estiver no PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Administrator\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

class SelectionOverlay(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.attributes("-fullscreen", True)
        self.attributes("-alpha", 0.2)  # Transparência reduzida para foco na seleção
        self.attributes("-topmost", True)
        self.config(bg='black')

        self.start_x = None
        self.start_y = None
        self.rect = None

        self.canvas = tk.Canvas(self, cursor="cross", bg="grey20")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        self.selection = None  # (x1, y1, x2, y2)

    def on_button_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        # Cria um retângulo de seleção
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='blue', width=2)

    def on_move_press(self, event):
        cur_x, cur_y = (self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))
        # Atualiza o retângulo
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_button_release(self, event):
        end_x, end_y = (self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))
        self.selection = (min(self.start_x, end_x), min(self.start_y, end_y),
                          max(self.start_x, end_x), max(self.start_y, end_y))
        self.destroy()

class DanTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dan Text - Extração de Texto")
        self.root.geometry("700x500")
        self.root.resizable(False, False)
        self.root.config(bg="#282c34")

        # Título estilizado
        self.title_label = tk.Label(root, text="Dan Text", font=("Helvetica", 24, "bold"), bg="#61afef", fg="white", pady=10)
        self.title_label.pack(fill=tk.X)

        # Botão de captura com novo estilo
        self.capture_button = tk.Button(root, text="Capturar Texto da Tela", command=self.start_capture, font=("Helvetica", 16), bg="#98c379", fg="white", borderwidth=0, padx=20, pady=10, activebackground="#7fbf63")
        self.capture_button.pack(pady=20)

        # Caixa de texto aprimorada
        self.text_box = tk.Text(root, wrap='word', height=15, width=70, font=("Helvetica", 12), bg="#1c1c1c", fg="#dcdcdc", borderwidth=3, relief="flat", insertbackground="white")
        self.text_box.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Barra de status minimalista
        self.status_bar = tk.Label(root, text="Aguardando captura...", bg="#21252b", fg="#abb2bf", anchor="w", padx=10, font=("Helvetica", 10))
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def start_capture(self):
        # Inicia a captura em uma thread separada
        self.status_bar.config(text="Capturando...")
        threading.Thread(target=self.capture_screen).start()

    def capture_screen(self):
        try:
            # Oculta a janela principal
            self.root.withdraw()
            # Pequeno atraso para garantir que a janela está oculta
            self.root.after(200, self.show_selection_overlay)
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
            self.root.deiconify()

    def show_selection_overlay(self):
        overlay = SelectionOverlay(self.root)
        self.root.wait_window(overlay)
        selection = overlay.selection
        if selection:
            # Captura a área selecionada
            x1, y1, x2, y2 = selection
            img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
            # Realiza OCR
            extracted_text = pytesseract.image_to_string(img, lang='por')  # 'por' para português
            # Exibe o texto extraído
            self.text_box.delete(1.0, tk.END)
            self.text_box.insert(tk.END, extracted_text)

            # Copia o texto para a área de transferência
            self.root.clipboard_clear()
            self.root.clipboard_append(extracted_text)
            messagebox.showinfo("Sucesso", "O texto foi extraído e copiado para a área de transferência.")

        else:
            messagebox.showinfo("Info", "Nenhuma área foi selecionada.")
        # Mostra a janela principal novamente
        self.root.deiconify()
        self.status_bar.config(text="Aguardando captura...")

if __name__ == "__main__":
    root = tk.Tk()
    app = DanTextApp(root)
    root.mainloop()
