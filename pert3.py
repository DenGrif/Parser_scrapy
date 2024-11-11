import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
url = "https://tomsk.hh.ru/vacancies/programmist"
driver.get(url)

try:
    # Увеличиваем время ожидания до 20 секунд
    wait = WebDriverWait(driver, 20)
    vacancies = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'vacancy-serp-item')))
except TimeoutException:
    print("Не удалось загрузить вакансии. Проверьте структуру страницы или увеличьте время ожидания.")
    driver.quit()
    exit()

parsed_data = []

for vacancy in vacancies:
    try:
        title = vacancy.find_element(By.CSS_SELECTOR, 'a.magritte-link___b4rEM_4-3-9 magritte-link_style_neutral___iqoW0_4-3-9 magritte-link_enable-visited___Biyib_4-3-9').text
        company = vacancy.find_element(By.CSS_SELECTOR, 'a.magritte-link___b4rEM_4-3-9 magritte-link_style_neutral___iqoW0_4-3-9').text
        salary = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___pbpft_3-0-16 magritte-text_style-primary___AQ7MW_3-0-16 magritte-text_typography-label-1-regular___pi3R-_3-0-16').text if vacancy.find_elements(By.CSS_SELECTOR, 'span[data-qa="vacancy-serp__vacancy-compensation"]') else "Не указана"
        link = vacancy.find_element(By.CSS_SELECTOR, 'a[data-qa="serp-item__title"]').get_attribute('href')
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

    parsed_data.append([title, company, salary, link])

driver.quit()

with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Название компании', 'Зарплата', 'Ссылка на вакансию'])
    writer.writerows(parsed_data)

print("Парсинг завершен. Данные сохранены в hh.csv")
