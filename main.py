import sys
from PySide6.QtWidgets import QApplication
from interface import TelaPrincipal


if __name__ == "__main__":
    
    #Cria a aplicação 
    app = QApplication(sys.argv)
    
    #Instancia a sua janela 
    janela = TelaPrincipal()
    
    #Manda a janela aparecer na tela
    janela.show()
    
    # 4. Inicia o loop infinito de eventos. 
    # O sys.exit garante que quando o usuário fechar a janela no "X", o Python encerre o processo completamente na memória.
    sys.exit(app.exec())