import yaml
import csv


class YamlToCsvParser:
    def __init__(self, yaml_file: str) -> None:
        self.yaml_dict = self.yaml_to_dict(yaml_file)

    def convert(self) -> None:
        column_names, data = self.get_data_and_keys(self.yaml_dict)
        self.write_csv(column_names, data)

    @staticmethod
    def yaml_to_dict(yaml_file: str) -> dict:
        with open(yaml_file, "r", encoding="utf-8") as yaml_data:
            yaml_parsed = yaml.load(yaml_data, Loader=yaml.FullLoader)
        return yaml_parsed

    @staticmethod
    def get_data_and_keys(yaml_parsed: dict) -> tuple[list, list]:
        data = []
        for element in yaml_parsed['schedule']['pair']:
            new_dict = {}
            for key, value in element.items():
                if isinstance(value, dict):
                    for new_key, new_value in value.items():
                        new_dict[new_key] = new_value
                else:
                    new_dict[key] = value
            data.append(new_dict)
        for element in data:
            for key, value in element.items():
                if key == 'start' or key == 'end':
                    element[key] = f"{value // 60}:" + f"{value % 60}".ljust(2, "0")
        column_names = list(data[0].keys())
        return column_names, data

    @staticmethod
    def write_csv(column_names: list, data: list) -> None:
        with open('Output.csv', 'w', encoding="utf-8", newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=column_names, delimiter=';')
            writer.writeheader()
            writer.writerows(data)


if __name__ == '__main__':
    try:
        PATH = "C:/Users/erokh/PycharmProjects/Lab4/data/Input.yaml"
        parser = YamlToCsvParser(PATH)
        parser.convert()
        print("Конвертация успешно завершена")
    except:
        print("ERROR")

