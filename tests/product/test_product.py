from inventory_report.inventory.product import Product


def test_cria_produto():
    product_test = {
       "id": "1",
       "nome_do_produto": "CADEIRA",
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2022-04-04",
       "data_de_validade": "2023-02-09",
       "numero_de_serie": "FR48",
       "instrucoes_de_armazenamento": "Conservar em local fresco"
     }

    product = Product(
        product_test["id"],
        product_test["nome_do_produto"],
        product_test["nome_da_empresa"],
        product_test["data_de_fabricacao"],
        product_test["data_de_validade"],
        product_test["numero_de_serie"],
        product_test["instrucoes_de_armazenamento"],
    )

    assert product.id == product_test["id"]
    assert product.nome_do_produto == product_test["nome_do_produto"]
    assert product.nome_da_empresa == product_test["nome_da_empresa"]
    assert (
        product.data_de_fabricacao == product_test["data_de_fabricacao"]
    )
    assert product.data_de_validade == product_test["data_de_validade"]
    assert product.numero_de_serie == product_test["numero_de_serie"]
    assert (
        product.instrucoes_de_armazenamento
        == product_test["instrucoes_de_armazenamento"]
    )
