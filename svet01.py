import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация браузера
driver = webdriver.Chrome()
url = "https://divan.ru/category/svet"
driver.get(url)

# Ждём, чтобы все элементы успели загрузиться
time.sleep(5)

# Получаем все элементы со светильниками
svets = driver.find_elements(By.CLASS_NAME, '_Ud0k')

parsed_data = []

# Проходим по всем элементам и получаем нужные данные
for svet in svets:
    try:
        name = svet.find_element(By.CSS_SELECTOR, 'div.lsooF span').text
        price = svet.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text
        url = svet.find_element(By.TAG_NAME, 'a').get_attribute('href')
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

    parsed_data.append([name, price, url])

# Закрываем браузер
driver.quit()

# Записываем данные в CSV-файл
with open("svet1.csv", 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Название товара', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)

print("Парсинг завершен. Данные сохранены в svet1.csv")
