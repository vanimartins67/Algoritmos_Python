from datetime import datetime

class Agenda:
    def __init__(self):
        self.tarefas = {}
    
    def validar_data(self, dia, mes, ano):
        try:
            datetime(ano, mes, dia)
            return True
        except ValueError:
            return False
    
    def anotar_tarefa(self, dia, mes, ano, anotacao):
        if self.validar_data(dia, mes, ano):
            data_chave = f"{dia:02d}/{mes:02d}/{ano}"
            self.tarefas[data_chave] = anotacao
            print(f"✅ Tarefa anotada para {data_chave}: {anotacao}")
            return True
        else:
            print("❌ Data inválida!")
            return False
    
    def mostrar_anotacao(self, dia, mes, ano):
        data_chave = f"{dia:02d}/{mes:02d}/{ano}"
        if data_chave in self.tarefas:
            print(f"📅 Anotação para {data_chave}: {self.tarefas[data_chave]}")
            return self.tarefas[data_chave]
        else:
            print(f"📭 Nenhuma anotação para {data_chave}")
            return None


print("\n" + "="*50)
print("6 - CLASSE AGENDA")
print("="*50)

agenda = Agenda()


agenda.anotar_tarefa(15, 1, 2024, "Reunião com o professor Thiago")
agenda.anotar_tarefa(20, 2, 2024, "Entrega do trabalho de POO")
agenda.anotar_tarefa(10, 3, 2024, "Prova de Matemática")
