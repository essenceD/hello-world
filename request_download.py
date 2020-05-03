import requests
n = 0
with open('c:\inputs\dataset_3378_2.txt', 'r') as file:
    url = file.readline().strip()
response = requests.get(url)
with open('c:\inputs\content.txt', 'w') as file:
    file.write(response.text)
print(len(response.text.splitlines()))
#for i in response.text.splitlines():
#    n += 1
with open('c:\outputs\\answer.txt', 'w') as file:
    file.write(str(len(response.text.splitlines())))
