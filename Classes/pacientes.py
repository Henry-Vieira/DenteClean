"""Autor: Leandro Henry Alves Ribeiro Vieira Magalhães

Componente Curricular: EXA 854-MI-Algoritmos

Concluido em: 06/10/2023

Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
"""
class Pacientes:

    def __init__(self, nome, cpf, prontuario = []):
        self.nome = nome
        self.cpf = cpf
        self.prontuario = prontuario

    def __repr__(self):
        return (f"nome : {self.nome}, CPF : {self.cpf}, prontuario : {self.prontuario}")
        
    def to_dict(self):
        return {
            'nome': self.nome,
            'cpf': self.cpf,
            'prontuario': self.prontuario
        }

    @classmethod
    def from_dict(cls, dict_info):
        nome = dict_info['nome'] if 'nome' in dict_info else ''
        rg = dict_info['cpf'] if 'cpf' in dict_info else ''
        dados_opcionais = dict_info['dados_opcionais'] if 'dados_opcionais' in dict_info else ''
        prontuario = dict_info['prontuario']if 'prontuario' in dict_info else []
        paciente = cls(nome, rg, dados_opcionais, prontuario)
        return paciente