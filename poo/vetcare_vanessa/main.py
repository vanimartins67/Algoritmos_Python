from models.tutor import Tutor
from models.veterinario import Veterinario
from models.animal import Animal
from models.consulta import Consulta
from models.prescricao import Prescricao

def menu():
    print("\n=== VetCare - Sistema Veterinário ===")
    print("1 - Cadastrar Tutor")
    print("2 - Listar Tutores")
    print("3 - Cadastrar Veterinário")
    print("4 - Listar Veterinários")
    print("5 - Cadastrar Animal")
    print("6 - Listar Animais")
    print("7 - Agendar Consulta")
    print("8 - Listar Consultas")
    print("9 - Emitir Prescrição")
    print("10 - Listar Prescrições")
    print("0 - Sair")

def cadastrar_tutor():
    print("\n--- Novo Tutor ---")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    
    tutor = Tutor(nome, telefone, endereco)
    tutor.salvar()
    print("Tutor cadastrado com sucesso!")

def listar_tutores():
    print("\n--- Lista de Tutores ---")
    temp = Tutor()
    lista = temp.listar()
    
    if lista:
        for t in lista:
            print(f"ID: {t[0]} | Nome: {t[1]} | Tel: {t[2]} | End: {t[3]}")
    else:
        print("Nenhum tutor encontrado.")

def cadastrar_veterinario():
    print("\n--- Novo Veterinário ---")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    crmv = input("CRMV: ")
    
    vet = Veterinario(nome, telefone, crmv)
    vet.salvar()
    print("Veterinário cadastrado com sucesso!")

def listar_veterinarios():
    print("\n--- Lista de Veterinários ---")
    temp = Veterinario()
    lista = temp.listar()
    
    if lista:
        for v in lista:
            print(f"ID: {v[0]} | Nome: {v[1]} | CRMV: {v[2]}")
    else:
        print("Nenhum veterinário encontrado.")

def cadastrar_animal():
    print("\n--- Novo Animal ---")
    nome = input("Nome: ")
    especie = input("Espécie: ")
    raca = input("Raça: ")
    idade = input("Idade: ")
    tutor_id = input("ID do Tutor: ")
    
    animal = Animal(nome, especie, raca, idade, tutor_id)
    animal.salvar()
    print("Animal cadastrado com sucesso!")

def listar_animais():
    print("\n--- Lista de Animais ---")
    temp = Animal()
    lista = temp.listar()
    
    if lista:
        for a in lista:
            print(f"ID: {a[0]} | Nome: {a[1]} | Espécie: {a[2]} | Dono: {a[3]}")
    else:
        print("Nenhum animal encontrado.")

def agendar_consulta():
    print("\n--- Nova Consulta ---")
    animal_id = input("ID do Animal: ")
    vet_id = input("ID do Veterinário: ")
    data = input("Data (DD/MM/AAAA): ")
    hora = input("Hora (HH:MM): ")
    
    consulta = Consulta(animal_id, vet_id, data, hora)
    consulta.salvar()
    print("Consulta agendada!")

def listar_consultas():
    print("\n--- Consultas Agendadas ---")
    temp = Consulta()
    lista = temp.listar()
    
    if lista:
        for c in lista:
            print(f"ID: {c[0]} | Data: {c[1]} | Hora: {c[2]}")
    else:
        print("Nenhuma consulta encontrada.")

def emitir_prescricao():
    print("\n--- Nova Prescrição ---")
    consulta_id = input("ID da Consulta: ")
    texto = input("Descrição dos medicamentos: ")
    
    prescricao = Prescricao(consulta_id, texto)
    prescricao.salvar()
    print("Prescrição salva!")

def listar_prescricoes():
    print("\n--- Prescrições ---")
    temp = Prescricao()
    lista = temp.listar()
    
    if lista:
        for p in lista:
            print(f"ID: {p[0]} | Consulta ID: {p[1]} | Texto: {p[2]}")
    else:
        print("Nenhuma prescrição encontrada.")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1': cadastrar_tutor()
        elif opcao == '2': listar_tutores()
        elif opcao == '3': cadastrar_veterinario()
        elif opcao == '4': listar_veterinarios()
        elif opcao == '5': cadastrar_animal()
        elif opcao == '6': listar_animais()
        elif opcao == '7': agendar_consulta()
        elif opcao == '8': listar_consultas()
        elif opcao == '9': emitir_prescricao()
        elif opcao == '10': listar_prescricoes()
        elif opcao == '0': 
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()