import os.path


class YamlToXmlParserPro:
    def __init__(self, yaml_file: str) -> None:
        self.__yaml_doc = self.__yaml_str_editing(yaml_file)

    @staticmethod
    def __get_yaml_str(yaml_file: str) -> str:
        """Получаем строку из YAML файла"""
        with open(yaml_file, "r", encoding="utf-8") as read_file:
            yaml_text = read_file.read()
        return yaml_text

    def __yaml_str_editing(self, yaml_file) -> list:
        """Функция для удаления лишних отступов в YAML тексте"""
        yaml_doc = [i for i in self.__get_yaml_str(yaml_file).split('\n')]
        last_indent_split = None
        for i in range(len(yaml_doc)):
            if yaml_doc[i].strip().startswith("#"):
                yaml_doc[i] = ""
            elif "#" in yaml_doc[i]:
                yaml_doc[i] = yaml_doc[i].split("#")[0].rstrip()
        yaml_doc = [i for i in yaml_doc if i != ""]
        for i in range(len(yaml_doc)):
            if yaml_doc[i].strip().startswith("- "):
                indent = (len(yaml_doc[i]) - len(yaml_doc[i].replace("-", " ").strip())) // 2
                if last_indent_split is None or indent > last_indent_split:
                    yaml_doc[i] = yaml_doc[i][2:]
                    for j in range(i + 1, len(yaml_doc)):
                        new_indent = (len(yaml_doc[j]) - len(yaml_doc[j].replace("-", " ").strip())) // 2
                        if new_indent >= indent:
                            yaml_doc[j] = yaml_doc[j][2:]
                    last_indent_split = indent - 1
        yaml_doc = [i for i in yaml_doc if i != ""]
        return yaml_doc

    def convert_to_xml(self, new_file=False):
        """Записывает XML в файл"""
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
        with open(output_file, "w", encoding="utf-8") as write_file:
            write_file.write(self.__yaml_to_xml())

    def __yaml_to_xml(self) -> str:
        """Переводит текст записанный в формате YAML в XML"""
        out = ""
        last_tags = dict()
        last_indent = 0
        flag = False

        # перебираем все строки
        for i in range(len(self.__yaml_doc)):
            keys = list(last_tags.keys())
            element = self.__yaml_doc[i]
            # ищем длину отступа
            indent = (len(element) - len(element.replace("-", " ").lstrip())) // 2

            # если блок закончился, то ставим закрывающийся тэг
            if indent < last_indent:
                for j in range(len(keys) - 1, -1, -1):
                    if keys[j] < last_indent:
                        if self.__yaml_doc[i - 1].strip()[0] == "-":
                            if last_tags[last_indent - 1] != last_tags[keys[j]]:
                                out += "\t" * keys[j] + f"</{last_tags[keys[j]]}>\n"
                                break
                        elif last_tags[last_indent] != last_tags[keys[j]]:
                            out += "\t" * keys[j] + f"</{last_tags[keys[j]]}>\n"
                            break

            # Если строка содержит ':' и (следующая строка содержит '-' или состоит из двух частей (через ':')),
            # то создаем открывающий тэг
            if ((element.rstrip()[-1] == ":" and i != len(self.__yaml_doc) - 1 and
                 (self.__yaml_doc[i + 1].strip()[0] != "-" or ": " in self.__yaml_doc[i + 1].strip())) or
                    (element.rstrip()[-1] == ":" and i == len(self.__yaml_doc) - 1)):
                content = element.replace(":", "").replace("-", "").strip()
                out += "\t" * indent + f"<{content}>\n"
                last_tags[indent] = content

            # Если строка содержит ':' и следующая строка содержит '-',
            # то записываем тэг
            elif (element.rstrip()[-1] == ":" and i != len(self.__yaml_doc) - 1
                  and self.__yaml_doc[i + 1].strip()[0] == "-"):
                content = element.replace(":", "").replace("-", "").strip()
                last_tags[indent] = content

            # Если строка состоит из двух частей (через ':') и содержит '-',
            # то закрываем предыдущий тэг и открываем по новой
            # для конструкций типа:
            #   pair:
            #     - type: Лекция
            #       name: Информатика
            #     - type: Лекция
            #       name: ОСНОВЫ ПРОФЕССИОНАЛЬНОЙ ДЕЯТЕЛЬНОСТИ
            elif ": " in element and element.strip()[0] == "-":
                content = [i.replace("-", "").strip() for i in element.split(": ")]
                if flag:
                    for j in range(len(keys) - 1, -1, -1):
                        if keys[j] < indent:
                            out += "\t" * keys[j] + f"</{last_tags[keys[j]]}>\n"
                            out += "\t" * keys[j] + f"<{last_tags[keys[j]]}>\n"
                            break
                out += "\t" * indent + f"<{content[0]}>{content[1]}</{content[0]}>\n"
                last_tags[indent] = content[0]
                flag = True

            # Если строка состоит из двух частей (через ':'), то записываем содержание в тэг
            elif ": " in element:
                content = [i.replace("-", "").strip() for i in element.split(": ")]
                out += "\t" * indent + f"<{content[0]}>{content[1]}</{content[0]}>\n"
                last_tags[indent] = content[0]

            # Если идет блок значений с '-' в начале, то записываем каждый элемент внутри тэга
            # для конструкций типа:
            # week:
            #   - 3
            #   - 7
            #   - 9
            #   - 11
            else:
                content = element.replace("-", "").strip()
                if element.strip()[0] == "-":
                    out += "\t" * (indent - 1) + f"<{last_tags[indent - 1]}>{content}</{last_tags[indent - 1]}>\n"
                else:
                    out += "\t" * indent + f"<{last_tags[indent]}>{content}</{last_tags[indent]}>\n"
            last_indent = indent

        # Закрываем основные оставшиеся тэги
        keys = list(last_tags.keys())
        for j in range(len(keys) - 1, -1, -1):
            if keys[j] < last_indent:
                out += "\t" * keys[j] + f"</{last_tags[keys[j]]}>\n"
        return out


if __name__ == '__main__':
    try:
        parser = YamlToXmlParserPro("C:/Users/erokh/PycharmProjects/Lab4/data/Input.yaml")
        parser.convert_to_xml()
        print("Конвертация успешно завершена")
    except:
        print("ERROR")
