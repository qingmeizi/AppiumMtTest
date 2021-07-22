
import yaml
def open_with_file(file_name):
    with open("./data/"+file_name + ".yml",'r',encoding='utf-8') as f:
        return yaml.load(f)

def yaml_data_with_file(file_name,key):
    with open("./data/"+file_name+".yml",'r',encoding='utf-8') as f:
        data = yaml.load(f)[key]
        case_data_list =list()
        for case_data in data.values():
            case_data_list.append(case_data)
        return case_data_list


