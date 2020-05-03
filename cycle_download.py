import requests
catalog = 'https://stepic.org/media/attachments/course67/3.6.3/' #save an adress where are the files we have to check
with open('c:\inputs\dataset_3378_3.txt', 'r') as file: #check the firdt file content
    link = file.readline().strip()
    content = link[-10:]
while True: #start downloading files until one of them wouldn't begin with word 'We'
    if 'We' in content.splitlines()[0]:
        print('GREAT! This is the file we was looking for!', '\n', 'Let us check what is inside:', '\n')
        print(content, '\n')
        with open('c:\outputs\\text_search.txt', 'w') as file: #save result
            file.write(content)
        print('This file will be saved as: "c:\outputs\\text_search.txt"')
        break
    else:   #creating new link to download next file
        dir = catalog
        print('We need a different file! Next file is:', content.splitlines()[0], 'Over the link:', link)
        new_file = requests.get(link).text
        dir += new_file
        link = dir
        content = new_file





