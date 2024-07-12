import sys
import os
import json
import yaml
import xmltodict


def parse_arguments():
    if len(sys.argv) != 3:
        print(Usage: program.exe pathFile1.x pathFile2.y)
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(input_file):
        print(fWprowadzony plik {input_file} nie istnieje.)
        sys.exit(1)

    input_format = os.path.splitext(input_file)[1].lower()
    output_format = os.path.splitext(output_file)[1].lower()

    if input_format not in ['.xml', '.json', '.yml', '.yaml'] or output_format not in ['.xml', '.json', '.yml', '.yaml']:
        print(Wspierane rozszerzenia: .xml, .json, .yml, .yaml)
        sys.exit(1)
    
    return input_file, output_file, input_format, output_format


def read_json(file_path):
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError as e:
            print(f"Błąd podczas odczytu pliku JSON: {e}")
            sys.exit(1)
    return data


def write_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4


def read_yaml(file_path):
    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)
        except yaml.YAMLError as e:
            print(f"Błąd podczas odczytu pliku YAML: {e}")
            sys.exit(1)
    return data


def write_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(data, file)


def read_xml(file_path):
    with open(file_path, 'r') as file:
        try:
            data = xmltodict.parse(file.read())
        except Exception as e:
            print(f"Błąd podczas odczytu pliku XML: {e}")
            sys.exit(1)
    return data


def write_xml(data, file_path):
    with open(file_path, 'w') as file:
        file.write(xmltodict.unparse(data, pretty=True))


if __name__ == "__main__":
    input_file, output_file, input_format, output_format = parse_arguments()

    if input_format == '.json':
        data = read_json(input_file)
    elif input_format in ['.yml', '.yaml']:
        data = read_yaml(input_file)
    elif input_format == '.xml':
        data = read_xml(input_file)

    if output_format == '.json':
        write_json(data, output_file)
    elif output_format in ['.yml', '.yaml']:
        write_yaml(data, output_file)
    elif output_format == '.xml':
        write_xml(data, output_file)
