
import json
import urllib.request


UserList=['elmiram', 'maryszmary', 'lizaku', 'nevmenandr', 'ancatmara', 'roctbb', 'akutuzov', 'agricolamz',
          'lehkost', 'kylepjohnson', 'mikekestemont', 'demidovakatya', 'shwars', 'JelteF', 'timgraham', 'arogozhnikov',
          'jasny', 'bcongdon', 'whyisjake', 'gvanrossum']

print ('Здравствуйте. Список репозиториев какого пользователя вы бы хотели посмотреть?')
username = input()

if username not in UserList: 
    print ('Выберите, пожалуйста, кого-то из этого списка:elmiram,maryszmary, lizaku, nevmenandr, ancatmara, roctbb, akutuzov,agricolamz, lehkost, kylepjohnson, mikekestemont, demidovakatya, shwars,JelteF, timgraham, arogozhnikov, jasny, bcongdon, whyisjake, gvanrossum') 

  
url = 'https://api.github.com/users/%s/repos' % username  


response = urllib.request.urlopen(url)  
text = response.read().decode('utf-8') 
data= json.loads(text)


print('У этого пользователя' + ' ' + str(len(data))+ ' ' + 'репозиториев.')


def repos(data):
    for i in data:
        print("Такой:  " + i["name"])
repos(data)

def description(data):
    for i in data:
        print("Описание:" + str(i["description"]))
description(data)


def languages(data):
    dict_lang = {}
    for i in data:
        new_1 = i['language']
        if new_1 in dict_lang:
            dict_lang[new_1]+=1
        else:
            dict_lang[new_1] = 1
        for lang in dict_lang.keys():
            print(lang, dict_lang[lang])
languages(data)
