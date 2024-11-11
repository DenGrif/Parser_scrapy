import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://tomsk.hh.ru/vacancies/programmist"

driver.get(url)

time.sleep(5)

vacansies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--hhzAtjuXrYFMBMspDjrF')

parsed_data = []

for vacancy in vacansies:
    try:
        title = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___tkzIl_4-3-9').text
        company = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___tkzIl_4-3-9').text
        salary = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___pbpft_3-0-16').text
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.magritte-link___b4rEM_4-3-9').get.attribute('href')
    except:
        print("произошла ошибка при парсинге")
        continue

    parsed_data.append(f"Название вакансии: {title}\nКомпания: {company}\nЗарплата: {salary}\nСсылка: {link}\n{'-'*40}")

driver.quit()

with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'название компании', 'зарплата', 'ссылка на вакансию'])
    writer.writerows(parsed_data)
