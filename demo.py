import yaml
import os
def main():
        current_path = os.path.dirname(__file__)
        with open(current_path + "/data.yml", 'r') as f:
            data = yaml.load(f)
            print(type(data))
            print(data)

if __name__ == '__main__':
    main()



