"""Autor: Leandro Henry Alves Ribeiro Vieira Magalhães

Componente Curricular: EXA 854-MI-Algoritmos

Concluido em: 06/10/2023

Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
"""
from Classes.Recepcionista import Recepcionista
from Classes.Dentista import Dentista
from Classes.pacientes import Pacientes

class Clinica():
    def __init__(self) -> None:
        self.fila = []
        self.sessoes = []
        self.consultas = []
        self.recepcionista = Recepcionista(self.sessoes, self.consultas, self.fila)
        self.dentista = Dentista(self.sessoes, self.consultas, self.fila)
    
    def add_paciente_fila(self, paciente: Pacientes):
        self.fila.append(paciente)

    def listar_sessoes(self):
        for sessao in self.sessoes:
            print(sessao)
