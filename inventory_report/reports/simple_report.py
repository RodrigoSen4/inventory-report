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
