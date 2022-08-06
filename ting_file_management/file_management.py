import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    try:
        if path_file.endswith('.txt'):
            with open(path_file, 'r') as file:
                read_file = file.read().strip().split('\n')
                return read_file
        else:
            print("Formato inválido", file=sys.stderr)
    except FileNotFoundError:
        print(
            f"Arquivo {path_file} não encontrado",
            file=sys.stderr
            )
