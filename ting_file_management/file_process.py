import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    for queue_item in instance.data:
        if queue_item['nome_do_arquivo'] == path_file:
            return f"Arquivo {path_file} já está na fila"

    file_reader = txt_importer(path_file)

    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_reader),
        "linhas_do_arquivo": file_reader,
    }

    instance.enqueue(result)
    print(result, file=sys.stdout)
    return f"Arquivo {path_file} adicionado à fila"


def remove(instance):
    """Aqui irá sua implementação"""
    if len(instance.data) == 0:
        print("Não há elementos", file=sys.stdout)
    else:
        first_element = instance.data[0]["nome_do_arquivo"]
        instance.dequeue()
        print(f"Arquivo {first_element} removido com sucesso", file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    if position > len(instance.data) or position < 0:
        print("Posição inválida", file=sys.stderr)
    else:
        print(instance.data[position], file=sys.stdout)
