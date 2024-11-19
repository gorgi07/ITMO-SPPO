import os


def parse_yaml(yaml_content):
    lines = yaml_content.split('\n')
    result = {}
    stack = [(result, -1)]  # (current_dict_or_list, indent_level)

    for line in lines:
        if not line.strip() or line.strip().startswith('#'):
            continue  # Пропускаем пустые строки и комментарии

        indent = len(line) - len(line.lstrip())
        stripped_line = line.lstrip()
        if ':' in stripped_line:
            key, value = stripped_line.split(':', 1)
            key = key.strip()
            value = value.strip() if value else None
        else:
            key = stripped_line.strip()
            value = None

        # Удаляем элементы из стека, если отступ уменьшился
        while stack and indent <= stack[-1][1]:
            stack.pop()

        # Получаем текущий родительский элемент
        parent, _ = stack[-1] if stack else (None, -1)

        if key.startswith('-'):
            # Это элемент списка
            key = key[1:].strip()
            if isinstance(parent, dict):
                # Начинаем новый список
                if key not in parent:
                    parent[key] = []
                new_item = {}
                parent[key].append(new_item)
                if value:
                    # Если есть значение, присваиваем его
                    parent[key][-1] = value
                else:
                    # Добавляем новый элемент в стек
                    stack.append((new_item, indent))
            elif isinstance(parent, list):
                # Добавляем в существующий список
                new_item = {}
                parent.append(new_item)
                if value:
                    parent[-1] = value
                else:
                    stack.append((new_item, indent))
        else:
            # Это элемент словаря
            if isinstance(parent, list):
                # Добавляем в последний словарь в списке
                if value is not None:
                    parent[-1][key] = value
                else:
                    parent[-1][key] = {}
                    stack.append((parent[-1][key], indent))
            elif isinstance(parent, dict):
                if value is not None:
                    parent[key] = value
                else:
                    parent[key] = {}
                    stack.append((parent[key], indent))
            else:
                raise ValueError("Неверная структура YAML")

    return result


def dict_to_xml(data, indent=0):
    xml = ''
    indent_space = ' ' * indent

    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, list):
                for item in value:
                    xml += f"{indent_space}<{key}>\n"
                    xml += dict_to_xml(item, indent + 2)
                    xml += f"{indent_space}</{key}>\n"
            elif isinstance(value, dict):
                xml += f"{indent_space}<{key}>\n"
                xml += dict_to_xml(value, indent + 2)
                xml += f"{indent_space}</{key}>\n"
            else:
                xml += f"{indent_space}<{key}>{value}</{key}>\n"
    elif isinstance(data, list):
        for item in data:
            xml += dict_to_xml(item, indent)
    else:
        xml += f"{indent_space}{data}\n"

    return xml


def yaml_to_xml(yaml_file_path, new_file=False):
    with open(yaml_file_path, 'r', encoding='utf-8') as read_file:
        yaml_content = read_file.read()

    yaml_dict = parse_yaml(yaml_content)
    xml_content = dict_to_xml(yaml_dict)

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

    with open(output_file, 'w', encoding='utf-8') as write_file:
        write_file.write(xml_content)


# Преобразование в XML
yaml_to_xml("C:/Users/erokh/PycharmProjects/Lab4/data/new.yaml")
