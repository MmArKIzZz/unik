list_contact={}
def Name():
    name=input("Введите имя ")
    name=name.title()
    name=name.strip()
    return name
def Num():
    n=input("Введите номер ")
    n=n.replace(' ','')
    n=n.replace('-','')
    if len(n)==10 and n[0]=='9':
        n= '+7'+n
    if n[0]=='8' and len(n)==11:
        n='+7'+n[1:]
    if n[0]=='7' and len(n)==11:
        n='+'+n
    if n[:2]=='+7' and len(n)==12:
        return n
    else:
        print("Номер введён неверно")
        return Num()
def Cont(dict,name,num):
    dict[name]=num
    print("Контакт добавлен")
    return dict
def show(dict):
    print("Список контактов")
    for i in dict:
        print(i,dict[i])
def dell():
    dname=input("Введите имя контакта ")
    dname = dname.title()
    dname = dname.strip()
    if dname in list_contact:
        list_contact.pop(dname)
        print("Контакт удалён")
    else:
        print("Данного контакта не существует")
def re():
    reame = input("Введите имя контакта ")
    reame = reame.title()
    reame = reame.strip()
    if reame in list_contact:
        new_n=input("Введите номер ")
        new_n=new_n.replace(' ','')
        new_n=new_n.replace('-','')
        if len(new_n)==10 and new_n[0]=='9':
            new_n= '+7'+new_n
        if new_n[0]=='8' and len(new_n)==11:
            new_n='+7'+new_n[1:]
        if new_n[0]=='7' and len(new_n)==11:
            new_n='+'+new_n
        if new_n[:2] == '+7' and len(new_n) == 12:
            new_n=new_n
        else:
            print("Номер введён неверно")
            return re()
        print("Номер изменён")
        list_contact[reame]=new_n
def menu():
    print("Выберети дейстие: \n1.Добавить контакт\n2.Показать контакты.\n3.Удалить контакт\n4.Изменить номер\n5.Выход")
    while True:
        p=int(input())
        if p==1:
            Cont(list_contact,Name(),Num())
            return menu()
        if p==2:
            show(list_contact)
            return menu()
        if p==5:
            break
        if p==3:
            dell()
            return menu()
        if p==4:
            re()
            return menu()
menu()


    