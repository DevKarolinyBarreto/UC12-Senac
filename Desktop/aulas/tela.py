import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap

app = QApplication(sys.argv)

with open("Desktop/plantas.qss","r") as arquivo_qss:
   estilo = arquivo_qss.read()
   app.setStyleSheet(estilo)

janelinha = QWidget()
janelinha.setWindowTitle('Plantinhas')
janelinha.setGeometry(50, 100, 450, 350)
rotulo = QLabel('Cadastre uma nova planta :)', janelinha)
rotulo.move(60, 40)
cadastro = QLineEdit()
cadastro.setPlaceholderText('Insira o nome cientifico da planta')
cadastro2 = QLineEdit()
cadastro2.setPlaceholderText('Insira o nome popular da planta')
cadastro2.move(170, 70)
imagem = QPushButton('Inserir imagem', janelinha)
imagem.move(170, 70)
confirmar = QPushButton('Confirmar', janelinha)
confirmar.move(170, 70)
cancelar = QPushButton('Cancelar', janelinha)
cancelar.setObjectName('Cancelar')
cancelar.move(170, 70)

layout = QVBoxLayout(janelinha)
layout.addWidget(rotulo)
layout.addWidget(cadastro)
layout.addWidget(cadastro2)
layout.addWidget(imagem)
layout.addWidget(cancelar)
layout.addWidget(confirmar)

janelinha.show()

sys.exit(app.exec_())