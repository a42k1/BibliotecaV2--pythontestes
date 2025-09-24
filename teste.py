from biblioteca import livro, user

livro1 = livro("O Silmarillio", "J.R.R. Tolkien")
livro2 = livro("The Complete Poems", "William Blake")

user1 = user("Abner")
user2 = user("Cassandra")

print("=== Teste Biblioteca ===\n")

print(f"1. {user1} tenta pegar o livro 1:")
user1.pegar_livro(livro1)

print(f"\n2. {user2} tenta pegar o mesmo livro 1:")
user2.pegar_livro(livro1)

print("\n3. Lista de livros de cada usuário:")
user1.list_livros()
user2.list_livros()

print(f"\n4. {user1} devolve o livro:")
user1.dev_livro(livro1)

print(f"\n5. {user2} tenta pegar o livro novamente:")
user2.pegar_livro(livro1)

print("\n6. Lista final de livros dos dois:")
user1.list_livros()
print("")
user2.list_livros()
print("\nFim do teste.")