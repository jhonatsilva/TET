DESCONTO_PADRAO = 0.105

acervo = []

def validar_float(mensagem):
    while True:
        texto = input(mensagem).strip().replace(',', '.')
        try:
            valor = float(texto)
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número, user virgula ou ponto.")

def validar_int(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto.isdigit() or (texto.startswith('-') and texto[1:].isdigit()):
            return int(texto)
        else:
            print("Entrada inválida. Digite um número inteiro.")      

def pausar():
    input("Pressione Enter para continuar...")              


def cadastrar_livro():
    print(f"\nCadastro de livro:")
    titulo = input("Título: ")
    autor = input("Autor: ")
    preco = validar_float("Preço em reais: ")
    estoque = validar_int("estoque em estoque: ")
        
    if not isinstance(preco, float) or preco < 0:
        print("Preço inválido: preço não é float.")
        return
    if not isinstance(estoque, int) or estoque < 0:
        print("Erro interno: estoque não é int.")
        return
    
livro = {
        "titulo": titulo,   
        "autor": autor,
        "preco": preco,     
        "estoque": estoque
    }

acervo.append(livro)
print(f"Livro cadastrado com sucesso. Total no acervo: {len(acervo)}")