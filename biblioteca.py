class livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True
    
    def __str__(self):
        return f"{self.titulo} - {self.autor}"

class user:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emp = []
    
    def __str__(self):
        return self.nome
    
    def pegar_livro(self, livro):
        if livro.disponivel:
            self.livros_emp.append(livro)
            livro.disponivel = False
            print(f"{self.nome} pegou o livro: {livro}")
        else:
            print(f"Livro '{livro}' nao esta disponivel")
    
    def dev_livro(self, livro):
        if livro in self.livros_emp:
            self.livros_emp.remove(livro)
            livro.disponivel = True
            print(f"{self.nome} devolveu o livro: {livro}")
        else:
            print(f"{self.nome} nao possui o livro '{livro}'")
    
    def list_livros(self):
        if self.livros_emp:
            print(f"Livros de {self.nome}:")
            for livro in self.livros_emp:
                print(f"  - {livro}")
        else:
            print(f"{self.nome} nao possui livros emprestados")