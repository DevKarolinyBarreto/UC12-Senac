# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
# from PyQt5.QtGui import QIcon, QPixmap

# def clicou():
#     texto2.setText('Clicado')

# app = QApplication(sys.argv)

# with open("Desktop/estilo.qss", "r") as arquivo_qss:
#    estilo = arquivo_qss.read()
#    app.setStyleSheet(estilo)

# janelinha = QWidget()
# janelinha.setWindowTitle('Cachorro caramelo fofinho')
# janelinha.setGeometry(50, 100, 450, 350)

# rotulo = QLabel('Clique no cachorro caramelo fofinho a baixo', janelinha)
# rotulo.move(105, 30)
# botao = QPushButton('Cachorro caramelo fofinho', janelinha)
# botao.setObjectName('mudou')
# botao.move(160, 65)
# botao.clicked.connect(clicou)
# texto2 = QLabel('              ', janelinha)
# texto2.move(210, 100)

# janelinha.show()

# sys.exit(app.exec_())


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap

app = QApplication(sys.argv)

with open("Desktop/plantas.qss", "r") as arquivo_qss:
    estilo = arquivo_qss.read()
    app.setStyleSheet(estilo)

janelinha = QWidget()
janelinha.setWindowTitle('Plantinhas')
janelinha.setGeometry(50, 100, 450, 350)

rotulo = QLabel('Cadastre uma nova planta :)', janelinha)
cadastro = QLineEdit()
cadastro.setPlaceholderText('Insira o nome científico da planta')
cadastro2 = QLineEdit()
cadastro2.setPlaceholderText('Insira o nome popular da planta')

imagem = QPushButton('Inserir imagem', janelinha)
confirmar = QPushButton('Confirmar', janelinha)
cancelar = QPushButton('Cancelar', janelinha)
cancelar.setObjectName('Cancelar')

layout = QVBoxLayout()
layout.addWidget(rotulo)
layout.addWidget(cadastro)
layout.addWidget(cadastro2)

button_layout = QHBoxLayout()
button_layout.addWidget(imagem)
button_layout.addWidget(confirmar)
button_layout.addWidget(cancelar)

layout.addLayout(button_layout)
janelinha.setLayout(layout)

janelinha.show()

sys.exit(app.exec_())
