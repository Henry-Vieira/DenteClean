"""Autor: Leandro Henry Alves Ribeiro Vieira Magalhães

Componente Curricular: EXA 854-MI-Algoritmos

Concluido em: 06/10/2023

Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
"""
class Sessoes:

    def __init__(self, iD, data, hora, duracao):
        self.iD = iD
        self.data = data
        self.hora = hora
        self.duracao = duracao
        self.atendimentos = []
        self.disponivel = True
        self.iniciada = False


    def to_dict(self):
        return{
            'iD': self.iD,
            'data': self.data,
            'hora': self.hora,
            'duracao': self.duracao,
            'atendimentos': self.atendimentos,
            'disponivel': self.disponivel,
            'iniciada': self.iniciada
        }
    

    @classmethod
    def from_dict(cls, dict_info):
        iD = dict_info['iD'] if 'iD' in dict_info else ''
        data = dict_info['data'] if 'data' in dict_info else ''
        hora = dict_info['hora'] if 'hora' in dict_info else ''
        duracao = dict_info['duracao'] if 'duracao' in dict_info else ''
        atendimentos = dict_info['atendimentos'] if 'atendimentos' in dict_info else ''
        disponivel = dict_info['disponivel'] if 'disponivel' in dict_info else ''
        iniciada = dict_info['iniciada'] if 'iniciada' in dict_info else ''
        return cls(iD, data, hora, duracao, atendimentos, disponivel, iniciada)