class Livro:
    def __init__(self, nome, autor, editora, paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas
    
    def alterar_editora(self, nova_editora):
        self.editora = nova_editora
    
    def listar_qtde_paginas(self):
        return self.paginas

livro1 = Livro("Dom Casmurro", "Machado de Assis", "Editora A", 256)
print(f"Livro: {livro1.nome}")
print(f"Autor: {livro1.autor}")
livro1.alterar_editora("Editora B")
print(f"Páginas: {livro1.listar_qtde_paginas()}")
print()