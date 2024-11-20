from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def main(text):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://onlineyamltools.com/convert-yaml-to-xml')
    input_element = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[3]/div/div[4]/div[1]/div[1]/div/div[1]/div[2]/textarea')
    input_element.clear()
    input_element.send_keys(text)
    output_element = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[3]/div/div[4]/div[1]/div[2]/div/div[1]/div[3]/textarea')
    return output_element.get_attribute('value')


if __name__ == '__main__':
    PATH1 = "C:/Users/erokh/PycharmProjects/Lab4/data/Input.yaml"
    PATH2 = "C:/Users/erokh/PycharmProjects/Lab4/data/new.yaml"
    PATH3 = "C:/Users/erokh/PycharmProjects/Lab4/data/resultFinal_main.yaml"
    with open(PATH2, "r", encoding="utf-8") as read_file:
        text = read_file.read()

    try:
        content = main(text)
        with open("Output.xml", "w", encoding="utf-8") as write_file:
            write_file.write(content)
    except:
        print("ОШИБКА")
