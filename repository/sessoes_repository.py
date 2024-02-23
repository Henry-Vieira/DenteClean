"""Autor: Leandro Henry Alves Ribeiro Vieira Magalhães

Componente Curricular: EXA 854-MI-Algoritmos

Concluido em: 06/10/2023

Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
"""
import json

from Classes.sessoes import Sessoes
from Classes.pacientes import Pacientes

class SessoesRepository:
  def __init__(self) -> None:
    self.json = 'db/sessoes.json'

  def salvar_sessao(self, sessao: Sessoes):
    sessoes = self.__load_json__()

    sessoes.append(sessao.to_dict())

    with open(self.json, 'w') as file:
      json.dump(sessoes, file, indent=4)

  def buscar_sessao(self, s_dia: str):
    sessoes = self.__load_json__()

    for sessao in sessoes:
      if sessao['data'] == s_dia:
        return sessao
    return None
  
  def buscar_sessao_iniciada(self, s_dia: str):
    sessoes = self.__load_json__()

    for sessao in sessoes:
      if sessao['data'] == s_dia and sessao['inicada'] == True:
        return sessao
    return None
  
  def listar_todas_sessoes(self):
    sessoes = self.__load_json__()
    return sessoes
  
  def listar_sessoes_disponiveis(self):
    sessoes = self.__load_json__()
    disponiveis = []

    for sessao in sessoes:
      if sessao['disponivel']:
        disponiveis.append(sessao)
    
    return disponiveis
  
  def add_atendimento(self, s_dia: str, paciente, horario):
    sessoes = self.__load_json__()

    if not isinstance(paciente, Pacientes):
        atendimento = {
        "nome": paciente['nome'],
        "cpf": paciente['cpf'],
        "data": s_dia,
        "horario": horario
        }
    else:
        atendimento = {
            "nome": paciente.nome,
            "cpf": paciente.cpf,
            "data": s_dia,
            "horario": horario
            }

    for sessao in sessoes:
      if sessao['data'] == s_dia:
        atendimentos = sessao['atendimentos']
        atendimentos.append(atendimento)
        break

    with open(self.json, 'w') as file:
      json.dump(sessoes, file, indent=4)

  def init_sessao(self, dia):
    sessoes = self.__load_json__()

    for sessao in sessoes:
      if sessao['data'] == dia:
        sessao['iniciada'] = True
        with open(self.json, 'w') as file:
            json.dump(sessoes, file, indent=4)
        return sessao
    
    return None
    
  def __load_json__(self):
    with open(self.json, 'r') as file:
      sessoes = json.load(file)
    return sessoes