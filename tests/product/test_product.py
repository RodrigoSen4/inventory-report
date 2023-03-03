from inventory_report.inventory.product import Product


def test_cria_produto():
    pass
    product = Product(
        id=1,
        nome_da_empresa='Trybe',
        nome_do_produto='Course',
        data_de_fabricacao='03/03/2022',
        data_de_validade='03/03/2023',
        numero_de_serie='24',
        instrucoes_de_armazenamento='Armazene com cuidado',
    )

    vl1 = 'O produto Course fabricado em 03/03/2022 por Trybe'
    vl2 = 'validade até 03/03/2023 precisa ser armazenado Armazene com cuidado'

    assert repr(product) == f'{vl1} {vl2}.'
