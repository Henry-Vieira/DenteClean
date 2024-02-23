"""Autor: Leandro Henry Alves Ribeiro Vieira Magalhães

Componente Curricular: EXA 854-MI-Algoritmos

Concluido em: 06/10/2023

Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
"""
from repository.sessoes_repository import SessoesRepository
from repository.paciente_repository import PacienteRepository

class Dentista:

    def __init__(self, sessoes: list, consultas: list, fila_de_atendimento: list):
        self.pacientes_repo = PacienteRepository()
        self.sessoes_repo = SessoesRepository()
        self.sessoes = sessoes
        self.consultas = consultas
        self.fila = fila_de_atendimento
        self.paciente_atual = None
        self.sessao_atual = None
        self.anotacoes = {}


    def init_sessao(self):
        dia = input('Informe a data atual: ')
        sessao = self.sessoes_repo.init_sessao(dia)
        if not sessao:
            print('Não foi possível encontrar a sessão.')
            return
        print('Sessão inicada com sucesso.')
        return

    def busca_sessao(self):
        dia = input('Informe a data atual: ')
        sessao = self.sessoes_repo.buscar_sessao(dia)
        if not sessao:
            print('Não foi possível encontrar a sessão.')
            return

        self.sessao_atual = sessao
        print(f"\n>\nId: {sessao['iD']} \nData e horário: {sessao['data']} às {sessao['hora']} \nDuração: {sessao['duracao']} \nDisponível: {sessao['disponivel']} \nIniciada: {sessao['iniciada']}")

        for atd in sessao['atendimentos']:
            print(f"\n>\nNome do Paciente: {atd['nome']}\n CPF do Paciente: {atd['cpf']}\nData e horário: {atd['data']} às {atd['horario']} \nDuração: 30min")
            
    def atender_paciente(self):
        if len(self.fila) == 0:
            print('Fila vazia.')
            return
        self.paciente_atual = self.fila[0]
        self.fila.pop(0)

        print(f'Próximo paciente a ser atendido: {self.paciente_atual['nome']}')


    def ler_prontuario(self):
        if not self.paciente_atual:
            print('Nenhum paciente em atendimento. Chame o próximo da fila')
            return
        paciente = self.pacientes_repo.buscar_paciente(self.paciente_atual['cpf'])
        notas = paciente['prontuario']
        if len(notas) < 1:
            print('O paciente não possui anotações no prontuário.')
        
        for nota in notas:
            print(f'\n>\nData: {nota['data']} \n Horário: {nota['horario']} \n Anotações: {nota['anotacoes']}')
    
    def ler_prim_anotacao(self):
        if not self.paciente_atual:
            print('Nenhum paciente em atendimento. Chame o próximo da fila')
            return
        paciente = self.pacientes_repo.buscar_paciente(self.paciente_atual['cpf'])
        notas = paciente['prontuario']
        if len(notas) < 1:
            print('O paciente não possui anotações no prontuário.')
        
        nota = notas[0]
        print(f'\n>\nData: {nota['data']} \n Horário: {nota['horario']} \n Anotações: {nota['anotacoes']}')
    
    def ler_ult_anotacao(self):
        if not self.paciente_atual:
            print('Nenhum paciente em atendimento. Chame o próximo da fila')
            return
        paciente = self.pacientes_repo.buscar_paciente(self.paciente_atual['cpf'])
        notas = paciente['prontuario']
        if len(notas) < 1:
            print('O paciente não possui anotações no prontuário.')
        
        nota = notas[-1]
        print(f'\n>\nData: {nota['data']} \n Horário: {nota['horario']} \n Anotações: {nota['anotacoes']}')
    
    def fazer_anotacao(self):
        nota = input('Escreva a nota: ')
        self.pacientes_repo.criar_anotacao(
            cpf=self.paciente_atual['cpf'],
            anotacao=nota,
            data=self.paciente_atual['data'],
            horario=self.paciente_atual['horario']
        )