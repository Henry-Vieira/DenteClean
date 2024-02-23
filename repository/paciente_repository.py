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

from Classes.pacientes import Pacientes

class PacienteRepository:
  def __init__(self) -> None:
    self.json = 'db/pacientes.json'

  def salvar_paciente(self, paciente: Pacientes):
    with open(self.json, 'r') as file:
      pacientes = json.load(file)

    pacientes.append(paciente.to_dict())

    with open(self.json, 'w') as file:
      json.dump(pacientes, file, indent=4)

  def buscar_paciente(self, cpf: str):
    with open(self.json, 'r') as file:
      pacientes = json.load(file)

    for paciente in pacientes:
      if paciente['cpf'] == cpf:
        return paciente
  
  def criar_anotacao(self, cpf: str, anotacao: str, data: str, horario: str):
    nova_nota = {
      "data": data,
      "horario": horario,
      "anotacoes": anotacao
    }

    with open(self.json, 'r') as file:
      pacientes = json.load(file)

    for paciente in pacientes:
      if paciente['cpf'] == cpf:
        prontuario = paciente['prontuario']
        prontuario.append(nova_nota)
        with open(self.json, 'w') as file:
          json.dump(pacientes, file, indent=4)
        print('Anotação registrada com sucesso.')
        return
    
      