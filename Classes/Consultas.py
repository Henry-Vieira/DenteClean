"""Autor: Leandro Henry Alves Ribeiro Vieira Magalhães

Componente Curricular: EXA 854-MI-Algoritmos

Concluido em: 06/10/2023

Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
"""
from Classes import pacientes
from Classes import sessoes

class Consultas:
    def __init__(self, paciente, sessao):
        self.paciente = paciente
        self.sessao = sessao
    

    def to_dict(self):
        return{
            'paciente': self.paciente.to_dict(),
            'sessao': self.sessao.to_dict()
        }
    

    @classmethod
    def from_dict(cls, dict_info):
        paciente_dict = dict_info['paciente'] if 'paciente' in dict_info else {}
        sessao_dict = dict_info['sessao'] if 'sessao' in dict_info else {}
        paciente = pacientes.from_dict(paciente_dict)
        sessao = sessoes.from_dict(sessao_dict)
        return cls(paciente, sessao)