"""Autor: Leandro Henry Alves Ribeiro Vieira Magalhães

Componente Curricular: EXA 854-MI-Algoritmos

Concluido em: 21/02/2024

Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
"""

import time

from Classes.Clinica import Clinica


def main():
    print('Bem vindo a clinica DenteClean')
    clinica = Clinica()
    while True:
        role = int(input("Qual sua função ?: \n1- Recepcionista\n2- Dentista\n3- Sair\nEscolha sua opção: "))
        match role:
            case 1:
                recepcionista = clinica.recepcionista
                while True:
                    time.sleep(1)
                    print("\n--- Menu da Recepcionista ---")
                    print("1. Adicionar sessão") #Adiciona sessões a serem marcadas
                    print("2. Sessões criadas") # lista de sessões criadas
                    print("3. Iniciar sessão")  # inicia a sessão
                    print("4. Recepcionar paciente") # Recebe paciente na clinica após ser adicionado no sistema e marcado consulta
                    print("5. Marcar paciente") # Marca consulta do paciente, porem não o coloca na lista de atendimento
                    print("6. Adicionar novo paciente") # Cadastra novo paciente
                    print("7. Proximo paciente da fila") # Mostra qual o proximo paciente da fila
                    print("8. Listar todos os atendimentos da sessão") # Lista todos os atendimentos marcados
                    print("9. Voltar") # Volta ao menu principal
                    choice = int(input("Escolha uma opção: "))
                    match choice:
                        case 1:
                            time.sleep(1)
                            recepcionista.add_sessao()
                        case 2:
                            time.sleep(1)
                            recepcionista.listar_sessoes()
                        case 3:
                            time.sleep(1)
                            recepcionista.init_sessao()
                        case 4:
                            time.sleep(1)
                            recepcionista.confirmar_horario()
                        case 5:
                            time.sleep(1)
                            recepcionista.marcar_paciente()
                        case 6:
                            time.sleep(1)
                            recepcionista.add_paciente()
                        case 7:
                            time.sleep(1)
                            recepcionista.proximo_paciente()
                        case 8:
                            time.sleep(1)
                            recepcionista.listar_atendimentos()
                        case 9:
                            break
                        case _:
                            print("Opção inválida. Por favor, escolha uma opção válida.")
            case 2:
                dentista = clinica.dentista
                while True:
                    time.sleep(1)
                    print("\n--- Menu do Dentista ---")
                    print("1. Localizar sessão cadastrada")
                    print("2. Escolha sessão clínica a iniciar")
                    print("3. Chamar próximo paciente")
                    print("4. Ler prontuário completo do paciente")
                    print("5. Ler primeira anotação do paciente")
                    print("6. Ler última anotação do paciente")
                    print("7. Realizar nova anotação")
                    print("8. Voltar")
                    choice = int(input("Escolha uma opção: "))
                    match choice:
                        case 1:
                            time.sleep(1)
                            dentista.busca_sessao()
                        case 2:
                            time.sleep(1)
                            dentista.init_sessao()
                        case 3:
                            time.sleep(1)
                            dentista.atender_paciente()
                        case 4:
                            time.sleep(1)
                            dentista.ler_prontuario()
                        case 5:
                            time.sleep(1)
                            dentista.ler_prim_anotacao()
                        case 6:
                            time.sleep(1)
                            dentista.ler_ult_anotacao()
                        case 7:
                            time.sleep(1)
                            dentista.fazer_anotacao()
                        case 8:
                            break
                        case _:
                            print("Opção inválida. Por favor, escolha uma opção válida.")
            case 3:
                break
            case _:
                print('Digite uma opção válida')

if __name__ == "__main__":
    main()