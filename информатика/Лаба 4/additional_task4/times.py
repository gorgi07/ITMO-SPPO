import time

PATH = "C:/Users/erokh/PycharmProjects/Lab4/data/Input.yaml"

# ---------------- Основное задание ----------------
start_time = time.perf_counter()
for i in range(100):
    from main_task.yaml_to_xml import YamlToXmlParser
    parser = YamlToXmlParser(PATH)
    parser.convert_to_xml()
end_time = time.perf_counter()
print(f"Основное задание - {end_time - start_time}")

# ----------------------- №1 -----------------------
start_time = time.perf_counter()
for i in range(100):
    from additional_task1.yaml_to_xml_libs import YamlToXmlLibs
    parser = YamlToXmlLibs(PATH)
    parser.main()
end_time = time.perf_counter()
print(f"Дополнительное задание №1 - {end_time - start_time}")

# ----------------------- №2 -----------------------
start_time = time.perf_counter()
for i in range(100):
    from additional_task2.yaml_to_xml_regex import YamlToXmlParserRegex
    parser = YamlToXmlParserRegex(PATH)
    parser.convert_to_xml()
end_time = time.perf_counter()
print(f"Дополнительное задание №2 - {end_time - start_time}")

# ----------------------- №3 -----------------------
start_time = time.perf_counter()
for i in range(100):
    from additional_task3.yaml_to_xml_pro import YamlToXmlParserPro
    parser = YamlToXmlParserPro(PATH)
    parser.convert_to_xml()
end_time = time.perf_counter()
print(f"Дополнительное задание №3 - {end_time - start_time}")
