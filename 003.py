import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://tomsk.hh.ru/vacancies/programmist"
driver.get(url)

time.sleep(5)

vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--hhzAtjuXrYFMBMspDjrF')

parsed_data = []

for vacancy in vacancies:
    try:
        title = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___tkzIl_4-3-9').text
        company = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___tkzIl_4-3-9').text
        salary = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___pbpft_3-0-16').text
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.magritte-link___b4rEM_4-3-9').get_attribute('href')
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

    parsed_data.append([title, company, salary, link])

driver.quit()

# Записываем данные в CSV с добавлением BOM для корректного отображения кириллицы в Excel и с разделителем ;
with open("hh3.csv", 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file, delimiter=';')  # Указываем разделитель ;
    writer.writerow(['Название вакансии', 'Название компании', 'Зарплата', 'Ссылка на вакансию'])
    writer.writerows(parsed_data)

print("Парсинг завершен. Данные сохранены в hh3.csv")
