class SimpleReport:
    pass

    @staticmethod
    def generate(item_list) -> str:
        datas_fabricacao = []
        datas_validade = []

        for item in item_list:
            datas_fabricacao.append(item['data_de_fabricacao'])
            datas_validade.append(item['data_de_validade'])

        return f'''
        Data de fabricação mais antiga: {item_list[0]['data_de_fabricacao']}
        Data de validade mais próxima: {item_list[0]['data_de_validade']}
        Empresa com mais produtos: {item_list[0]['nome_da_empresa']}
        '''


print(SimpleReport.generate(
     [
         {
             "id": 1,
             "nome_do_produto": "CADEIRA",
             "nome_da_empresa": "Forces of Nature",
             "data_de_fabricacao": "2022-04-04",
             "data_de_validade": "2023-02-09",
             "numero_de_serie": "FR48",
             "instrucoes_de_armazenamento": "Conservar em local fresco"
         }
        ]
 ))
