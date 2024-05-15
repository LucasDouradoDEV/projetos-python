# Simulador de Dado
# Simular o uso de um dado, gerando um valor de 1 até 6
import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = "Você gostaria de gerar um novo valor para o dado?"
        #Layout
        self.layout = [
            [sg.Text("Jogar o dado?")],
            [sg.Button('Sim'), sg.Button('Não')]
        ]

    def Iniciar(self):
        
        #Criar uma Janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        #Ler os valores
        self.eventos, self.valores = self.janela.Read()
        #Fazer alguma coisa com esses valores
        try:
            if self.eventos == 'Sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'Não' or self.eventos == 'n':
                print('Agradecemos sua participação!')
            else:
                print('Favor digitar Sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


Simulador = SimuladorDeDado()
Simulador.Iniciar()