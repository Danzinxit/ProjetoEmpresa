🚀 Agilizador de Tarefas - Reconhecimento de Texto em Imagens 📸
Descrição
Este projeto é uma ferramenta desenvolvida em Python 🐍, que utiliza tecnologia de Reconhecimento Óptico de Caracteres (OCR) para extrair texto de qualquer imagem 🖼️ e colá-lo diretamente onde o usuário deseja. A aplicação foi projetada para agilizar tarefas diárias ⏱️, facilitando a extração de texto de imagens e sua utilização sem a necessidade de digitação manual ⌨️.

Funcionalidades principais:
📄 Extração automática de texto de imagens.
📋 Copia o texto extraído para a área de transferência.
🖥️ Permite colar o texto copiado em qualquer aplicação ou campo de texto.
🔄 Suporta uma ampla variedade de formatos de imagem, incluindo PNG, JPG, JPEG, e outros.
Pré-requisitos
Python 3.x ou superior.
Bibliotecas Python: pytesseract, Pillow, pyperclip, keyboard.
Instalação
Siga os passos abaixo para rodar o projeto localmente:

Instalar o Python 3.x: Caso ainda não tenha o Python instalado, faça o download e instale a versão mais recente do Python 🖱️.

Instalar dependências: Abra o terminal ou prompt de comando e execute o seguinte comando para instalar as bibliotecas necessárias:

bash
Copiar
pip install pytesseract Pillow pyperclip keyboard
Instalar o Tesseract OCR: O Tesseract é uma ferramenta de OCR que será usada para processar as imagens. Faça o download e siga as instruções para instalar no seu sistema:

Windows: Baixe o instalador do Tesseract aqui.
Linux: Execute o comando:
bash
Copiar
sudo apt-get install tesseract-ocr
Após a instalação, adicione o caminho do executável do Tesseract no seu sistema (caso necessário) para que a ferramenta seja reconhecida.

Baixar o código: Faça o download ou clone este repositório para o seu diretório local.

bash
Copiar
git clone https://github.com/empresa/agilizador-tarefas.git
Como Usar
Executar o programa: Após a instalação e configuração, execute o arquivo do projeto. Para isso, abra o terminal ou prompt de comando e navegue até o diretório do projeto.

bash
Copiar
python main.py
Capturar texto da imagem: Quando o programa estiver em execução, você pode selecionar uma imagem (capturada diretamente de um arquivo ou até mesmo uma captura de tela 📷) que contenha o texto que deseja copiar.

Copiar e Colar o Texto: O software irá processar a imagem, extrair o texto e copiá-lo automaticamente para a área de transferência. Você pode então colar o texto extraído em qualquer aplicação utilizando o atalho de teclado padrão (Ctrl+V) 🖱️.

Exemplo de Uso
Abra o software 💻.
Selecione ou arraste a imagem desejada para a interface do programa 🖼️.
O programa irá processar a imagem e copiar o texto para a área de transferência 📋.
Coloque o cursor no campo de destino onde deseja colar o texto e pressione Ctrl+V 🔄.
Atalhos de Teclado
Ctrl+C: Copiar o texto extraído para a área de transferência 📋.
Ctrl+V: Colar o texto copiado no campo desejado 🖥️.
Contribuindo
Contribuições são bem-vindas! 🤝 Se você deseja contribuir para este projeto, siga estas etapas:

Faça um fork deste repositório 🍴.
Crie uma nova branch (git checkout -b feature/nova-funcionalidade).
Faça as alterações e comite (git commit -am 'Adicionando nova funcionalidade').
Faça um push para a branch (git push origin feature/nova-funcionalidade).
Abra um pull request 🚀.
Licença
Este projeto está licenciado sob a MIT License 📜.

Tecnologias Utilizadas
Python 3.x 🐍
pytesseract: Biblioteca Python para acessar a ferramenta Tesseract OCR 🧠.
Pillow: Biblioteca para manipulação de imagens 🖼️.
pyperclip: Biblioteca para interagir com a área de transferência 📋.
keyboard: Biblioteca para capturar eventos do teclado ⌨️ e agilizar interações.
