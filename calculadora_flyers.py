def calcular_preco_flyers():
    print("Bem-vindo à Calculadora de Preços de Flyers!")
    
    # Entrada de dados
    quantidade = int(input("Digite a quantidade de flyers desejada: "))
    tamanho = input("Digite o tamanho do flyer (A6, A5, A4): ").upper()
    cores = input("Digite o tipo de impressão (4x0 ou 4x4): ")
    papel = input("Digite o tipo de papel (Couché 90g, Couché 115g, Couché 150g): ")
    
    # Preços base por tamanho
    precos_base = {
        'A6': 0.15,
        'A5': 0.25,
        'A4': 0.40
    }
    
    # Multiplicadores por tipo de impressão
    mult_cores = {
        '4x0': 1.0,  # Frente colorida
        '4x4': 1.8   # Frente e verso coloridos
    }
    
    # Multiplicadores por tipo de papel
    mult_papel = {
        'COUCHÉ 90G': 1.0,
        'COUCHÉ 115G': 1.2,
        'COUCHÉ 150G': 1.4
    }
    
    # Cálculos
    preco_unitario = precos_base[tamanho]
    preco_unitario *= mult_cores[cores]
    preco_unitario *= mult_papel[papel.upper()]
    
    # Desconto por quantidade
    if quantidade >= 1000:
        desconto = 0.15
    elif quantidade >= 500:
        desconto = 0.10
    elif quantidade >= 200:
        desconto = 0.05
    else:
        desconto = 0
    
    # Cálculo final
    preco_total = preco_unitario * quantidade
    preco_com_desconto = preco_total * (1 - desconto)
    
    # Exibição dos resultados
    print("\nResumo do Pedido:")
    print(f"Quantidade: {quantidade} unidades")
    print(f"Tamanho: {tamanho}")
    print(f"Impressão: {cores}")
    print(f"Papel: {papel}")
    print(f"\nPreço unitário: R$ {preco_unitario:.2f}")
    print(f"Desconto aplicado: {desconto*100:.0f}%")
    print(f"Preço total: R$ {preco_com_desconto:.2f}")

if __name__ == "__main__":
    calcular_preco_flyers()