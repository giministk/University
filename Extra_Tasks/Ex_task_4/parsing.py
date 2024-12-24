import re
import csv 
import urllib.request 


url = "https://msk.spravker.ru/avtoservisy-avtotehcentry/"
response = urllib.request.urlopen(url)
html_content = response.read().decode()
pattern = r"(?:-link\">)(?P<name>[^<]+)(?:[^o]*[^l]*.*\n *)(?P<address>[^\n]+)(?:\s*.*>\s*.*>\s*.*>\s*<d[^>]*>\s*.*\s*.*>(?P<phone>[^<]+).*>\s*</dl>)?(?:\s*<.*>\s*<.*\s*<.*>(?P<workhours>[^<]+)</dd>)?"

match = re.findall(pattern, html_content)
# Запись полученных данных в csv-файл
with open('inform.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Адрес', 'Телефон', 'Рабочие часы'])

    for i in match:
        writer.writerow(i)

matches = re.finditer(pattern, html_content)

for match in matches:
    print("Название:", match.group('name'))
    print("Адрес:", match.group('address'))
    print("Телефон:", match.group('phone'))
    print("Рабочие часы:", match.group('workhours'))
    print("\n")

if not re.search(pattern, html_content):
    print("No match found.")

