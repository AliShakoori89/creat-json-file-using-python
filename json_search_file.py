import json
import os.path

print("choice your options:  ")
print("                         1. enter new name in to the list:  ")
print("                         2. search name :")
print("                         3. edit field :")
print('')
print('')
print('')
print('')
input_number_choice=int(input("1. enter num 1 , 2 or 3 : "))

if input_number_choice==1:

    d={}
    c={}

    name = input('enter Name :  ')
    lastname = input('enter LastName :  ')
    birth = input('enter date of birth : ')
    id_num = input('enter id num :  ')
    c={'Name':name,'LastName':lastname,'Birthday':birth}
    d[id_num]=c

    if not os.path.isfile('test.json'):
        with open('test.json','w')as f:
            f.write(json.dumps(d))
    else:
        with open('test.json')as f:
            feeds=json.load(f)
        feeds.update(d)
        with open('test.json','w') as f:
            f.write(json.dumps(feeds))

if input_number_choice==2:
    id_search=str(input('enter id for search: '))
    with open('test.json')as f:
        data=json.load(f)
    if id_search in data:
        print(data[id_search]['Name'],data[id_search]['LastName'],data[id_search]['Birthday'])
    else:
        print('')
        print('json file not exist id')

if input_number_choice==3:
    id_search=str(input('enter id for search: '))
    with open('test.json')as f:
        data=json.load(f)
        if id_search in data:
            data[id_search]['Name']=str(input('enter naew name : '))
            data[id_search]['LastName']=str(input('enter naew Lastname : '))
            data[id_search]['Birthday']=str(input('enter naew Birthday : '))
            with open('test.json','w') as f:
                f.write(json.dumps(data))
        else:
            print('')
            print('json file not exist id')

