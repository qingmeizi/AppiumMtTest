import yaml


def open_with_file(file_name):
    with open("./data/"+file_name + ".yml",'r',encoding='utf-8') as f:
        return yaml.load(f)