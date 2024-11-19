import os
import xml.etree.ElementTree as Xml
import yaml


class YamlToXmlLibs:
    def __init__(self, yaml_file: str) -> None:
        with open(yaml_file, "r", encoding="utf-8") as yaml_data:
            self.yaml_parsed = yaml.load(yaml_data, Loader=yaml.FullLoader)

    def main(self):
        # Преобразуем в XML
        converter = DictToXmlParser(self.yaml_parsed)
        # Сохранение в файл
        converter.save_to_file()


class DictToXmlParser:
    def __init__(self, data: dict):
        self.data = data

    def _build_xml(self, data, parent):
        """Рекурсивное построение XML дерева из словаря"""
        if isinstance(data, dict):
            for key, value in data.items():
                element = Xml.SubElement(parent, key)
                self._build_xml(value, element)
        elif isinstance(data, list):
            for item in data:
                element = Xml.SubElement(parent, "item")
                self._build_xml(item, element)
        else:
            parent.text = str(data)

    def to_xml_string(self, root_name="root"):
        """Генерирует XML строку"""
        root = Xml.Element(root_name)
        self._build_xml(self.data, root)
        return Xml.tostring(root, encoding="unicode")

    def save_to_file(self, root_name="root", new_file=False):
        """Сохраняет XML в файл"""
        if new_file:
            if not os.path.isfile(f"Output.xml"):
                output_file = "Output.xml"
            else:
                i = 1
                while os.path.isfile(f"Output ({i}).xml"):
                    i += 1
                output_file = f"Output ({i}).xml"
        else:
            output_file = "Output.xml"
        root = Xml.Element(root_name)
        self._build_xml(self.data, root)
        tree = Xml.ElementTree(root)
        Xml.indent(tree, space="  ", level=0)  # Для форматирования отступов
        tree.write(output_file, encoding="utf-8", xml_declaration=False)


# Использование
if __name__ == "__main__":
    try:
        parser = YamlToXmlLibs("C:/Users/erokh/PycharmProjects/Lab4/data/Input.yaml")
        parser.main()
        print("Конвертация успешно завершена")
    except:
        print("ERROR")
