import json
import sys


tst = open(sys.argv[1],"r")
val = open(sys.argv[2],"r")

testjson = json.load(tst)
valuesjson = json.load(val)
valuesobj = valuesjson.get("values")

tst.close()
val.close()

def getvaluebyid(id):
    for item in valuesobj:
        if item.get("id") == id:
            return item.get("value")

# Метод ля работы со словарем (dict)
def intothedict(tdict):
    # проверяем содержит словарь поля id и value
    if (ishaveidandvalue(tdict)):
        # если оба поля присутствуют то меняем поле value
        changevalue(tdict)

# при переборе в item возвращаются названия ключей в string
    for item in tdict:
        # получаем значение каждлго поля
        dictitem = tdict.get(item)
        # если поле содержит массив (list) то приступаем к перебору данного массива
        if isinstance(dictitem, list):
            intothelist(dictitem)

# Метод лдля работы с массивом (list)
def intothelist(tlist):
    for listitem in tlist:
        # Проверяем если в ячейке хранится словарь (dict)
        if isinstance(listitem, dict):
            intothedict(listitem)

#
def changevalue(testitem):
    ishaveidandvalue(testitem)
    testitem.update({"value": getvaluebyid(testitem.get("id"))})

# Метод для проверки наличия в массиве ключей id и value
def ishaveidandvalue(testitem):
    ishaveid = False
    ishavevalue = False

    for dick in testitem.keys():
        if dick == "id":
            ishaveid = True
        if dick == "value":
            ishavevalue = True

    if ishaveid and ishavevalue:
        return True



intothedict(testjson)

cr = open("report.json", "w+")
json.dump(testjson, cr,  indent=2, sort_keys=True)
cr.close()
