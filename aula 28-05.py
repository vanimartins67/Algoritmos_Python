# with open ("cadastro.txt" , "a") as x:
#     x.write("Novo cadastro\n")

# with open ("cadastro.txt", "r") as f:
#     linhas = f.readlines()
#     print(linhas[2])

# with open("cadastro.txt", "r") as f:
#     for linha in f:
#         if "joão" in linha.lower():
#             print(linha)

with open ("cadastro.txt", "r") as f:
    linhas = f.readlines()
    del linhas[2]
    with open("cadastro.txt", "w") as f:
        f.writelines(linhas)
    