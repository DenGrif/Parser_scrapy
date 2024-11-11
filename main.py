# Фильтрация данных
data = [
    [100, 110, 120],
    [400, 500, 600],
    [150, 130, 140]
    ]
list = []

for row in data:
    for item in row:
        if item > 190:
            list.append(item)

print(list)


# Преобразование одного типа данных в другое (текст в числа)
# data = [
#     ['100', '200', '300'],
#     ['400', '500', '600']
#     ]
# numbers = []
#
# for row in data:
#     for text in row:
#         number = int(text)
#         numbers.append(number)
#
# print(numbers)


# Очистка списка от лишних пробелов:
# import requests
# from bs4 import BeautifulSoup
#
# url = "https://"
#
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
#
# rows = soup.find_all("tr")
# data = []
# for row in rows:
#     cols = row.find_all("td")
#     cleaned_cols = [col.text.strip() for col in cols]
#     data.append(cleaned_cols)
#
# print(data)

#magritte-text___tkzIl_4-3-9 magritte-text___tkzIl_4-3-9