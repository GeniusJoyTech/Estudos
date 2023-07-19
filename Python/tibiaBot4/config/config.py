import json

def load_config():
    try:
        with open('config/config.json', 'r') as file:
            config_data = json.load(file)
    except FileNotFoundError:
        config_data = {}
    return config_data

def save_config(config_data):
    with open('config.json', 'w') as file:
        json.dump(config_data, file, indent=4)

def create_config(config_name, pos1, pos2, alt, larg):
    config_data = load_config()
    config_data[config_name] = {
        "pos1": pos1,
        "pos2": pos2,
        "alt": alt,
        "larg": larg
    }
    save_config(config_data)

def read_config(config_name):
    config_data = load_config()
    return config_data.get(config_name)

def update_config(config_name, pos1, pos2, alt, larg):
    config_data = load_config()
    if config_name in config_data:
        config_data[config_name] = {
            "pos1": pos1,
            "pos2": pos2,
            "alt": alt,
            "larg": larg
        }
        save_config(config_data)
        return True
    return False

def delete_config(config_name):
    config_data = load_config()
    if config_name in config_data:
        del config_data[config_name]
        save_config(config_data)
        return True
    return False




'''
# Exemplo de uso:

# Criar configurações
create_config("Game", [822, 134], [1519, 645], 511, 697)
create_config("Bag", [822, 134], [1519, 645], 511, 697)
create_config("BrowseField", [822, 134], [1519, 645], 511, 697)

# Exibir configurações
config_name = "Game"
config = read_config(config_name)
print(f"Configuração '{config_name}':")
print(config)

# Atualizar configuração
config_name = "Game"
if update_config(config_name, [900, 150], [1600, 700], 500, 700):
    print(f"Configuração '{config_name}' atualizada com sucesso!")
else:
    print(f"Configuração '{config_name}' não encontrada.")

# Excluir configuração
config_name = "Bag"
if delete_config(config_name):
    print(f"Configuração '{config_name}' excluída com sucesso!")
else:
    print(f"Configuração '{config_name}' não encontrada.")
'''
