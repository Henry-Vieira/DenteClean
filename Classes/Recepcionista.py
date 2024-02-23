"""Autor: Leandro Henry Alves Ribeiro Vieira Magalhães

Componente Curricular: EXA 854-MI-Algoritmos

Concluido em: 06/10/2023

Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
"""
from Classes.sessoes import Sessoes
from Classes.pacientes import Pacientes
from repository.sessoes_repository import SessoesRepository
from repository.paciente_repository import PacienteRepository


class Recepcionista:
    
    def __init__(self, sessoes: list, consultas: list, fila_de_atendimento: list):
        self.pacientes_repo = PacienteRepository()
        self.sessoes_repo = SessoesRepository()
        self.sessoes = sessoes
        self.consultas = consultas
        self.fila = fila_de_atendimento


    def add_sessao(self):
        iD = len(self.sessoes_repo.listar_todas_sessoes()) + 1
        data = input("Digite a data da sessão DD:MM:AAAA: ")
        hora = input("Digite a hora da sessão HH:MM: ")
        duracao = input("Digite a duracao da sessão em minutos: ")
        s = Sessoes(iD, data, hora, duracao)
        self.sessoes.append(s)
        self.sessoes_repo.salvar_sessao(s)
    
    def init_sessao(self):
        dia = input('Informe a data atual: ')
        sessao = self.sessoes_repo.init_sessao(dia)
        if not sessao:
            print('Não foi possível encontrar a sessão.')
            return
        print('Sessão inicada com sucesso.')
        return

    def listar_sessoes(self):
        sessoes = self.sessoes_repo.listar_todas_sessoes()

        for sessao in sessoes:
            print(f"\n>\nId: {sessao['iD']} \nData e horário: {sessao['data']} às {sessao['hora']} \nDuração: {sessao['duracao']} \nAtendimentos: {sessao['atendimentos']} \nDisponível: {sessao['disponivel']}")

    def listar_sessoes_disponiveis(self):
        sessoes = self.sessoes_repo.listar_sessoes_disponiveis()

        for sessao in sessoes:
            print(f"\n>\nId: {sessao['iD']} \nData e horário: {sessao['data']} às {sessao['hora']} \nDuração: {sessao['duracao']} \nAtendimentos: {sessao['atendimentos']} \nDisponível: {sessao['disponivel']}")
        
        return sessoes

    def add_paciente(self):
        nome = input('Insira o nome do paciente a ser cadastrado: ')
        cpf = input('Insira o CPF do paciente a ser cadastrado: ')

        paciente = Pacientes(nome, cpf)
        self.pacientes_repo.salvar_paciente(paciente)
        return paciente
    
    def marcar_paciente(self):
        cpf = input('Informe o CPF do paciente: \n').strip()
        paciente = self.pacientes_repo.buscar_paciente(cpf)
        if not paciente:
            print('Paciente não cadastrado. Cadastre-o antes de marcar a consulta.')
            paciente = self.add_paciente()

        disponiveis = self.listar_sessoes_disponiveis()
        if len(disponiveis) == 0:
            print('Não existem sessões disponíveis para marcação. Crie uma nova.')
            return
         
        sessao_data = input('Seleciona a data que deseja marcar: \n')
        horario = input('Informe o horário da consulta: ')
        self.sessoes_repo.add_atendimento(sessao_data, paciente, horario)

    def listar_atendimentos(self):
        dia = input('Informe a data da sessão: ')
        sessao = self.sessoes_repo.buscar_sessao(dia)

        atendimentos = sessao['atendimentos']
        if len(atendimentos) == 0:
            print('Não foi realizado nenhum atendimento.')
            return
        for atd in atendimentos:
            print(f"\n>\nNome do Paciente: {atd['nome']}\n CPF do Paciente: {atd['cpf']}\nData e horário: {atd['data']} às {atd['horario']} \nDuração: 30min")

    def confirmar_horario(self):
        dia = input('Informe a data atual: ')
        sessao = self.sessoes_repo.buscar_sessao(dia)
        if not sessao:
            print('Não foi encontrado nenhuma sessão para o dia de hoje. Crie uma nova.')
            return
        if sessao['iniciada'] == False:
            print('A sessão do dia atual não foi iniciada.')
            return
        
        cpf = input('Informe o CPF do paciente: ')
        consultas = sessao['atendimentos']

        for consulta in consultas:
            if consulta['cpf'] == cpf:
                self.colocar_na_fila(consulta) 
                print('Marcação confirmada e paciente adicionado na fila de atendimento.')
                return

        print('O paciente não está marcado para a sessão atual.')
        return

    def colocar_na_fila(self, consulta):
        self.fila.append(consulta)

    def proximo_paciente(self):
        if len(self.fila) == 0:
            print('Fila vazia.')
            return
        atd = self.fila[0]
        print(f"\n>\nNome do Paciente: {atd['nome']}\n CPF do Paciente: {atd['cpf']}\nData e horário: {atd['data']} às {atd['horario']} \nDuração: 30min")