def exists_word(word, instance):
    """Aqui irá sua implementação"""
    data_list = list()
    occurrencies = list()
    for queue_item in instance.data:
        for index, linha in enumerate(queue_item['linhas_do_arquivo']):
            if word.lower() in linha.lower():
                occurrencies.append({'linha': index + 1})

        if len(occurrencies) > 0:
            data_list.append({
                'palavra': word,
                'arquivo': queue_item['nome_do_arquivo'],
                'ocorrencias': occurrencies
            })

    return data_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    data_list = list()
    occurrencies = list()
    for queue_item in instance.data:
        for index, linha in enumerate(queue_item['linhas_do_arquivo']):
            if word.lower() in linha.lower():
                occurrencies.append({
                    'linha': index + 1,
                    'conteudo': linha
                    })

        if len(occurrencies) > 0:
            data_list.append({
                'palavra': word,
                'arquivo': queue_item['nome_do_arquivo'],
                'ocorrencias': occurrencies
            })

    return data_list
