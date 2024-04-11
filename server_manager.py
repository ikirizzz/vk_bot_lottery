import json
import pyqrcode
import qrtools
from pprint import pprint

def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding = 'utf-8') as file:
        json.dump(data, file, indent = 4)

def read(filename):
    with open(filename, 'r', encoding = 'utf-8') as file:
        return json. load(file)

def re_and_wr(data,filename):
    global Codes, Code0, CodeM, fail, PPLS, PPLS_Vivod, SonJ
    write(data, filename)
    SonJ = read(fail)
    PPLS = SonJ["PPLS"]
    PPLS_Vivod = "Список участников:"
    for i in range(1, len(PPLS)):
        PPLS_Vivod +="\n" + str(i) +".-  "+ PPLS[i]["FIO"]+ "  (id" + str(PPLS[i]["ManID"])+ ")"
    Codes = SonJ["Codes"]
    Code0 = []
    CodeM = []
    for i in range(1, len(Codes)):
        Code0.append(Codes[i]["Code"])
        CodeM.append(Codes[i]["Meth"])

def new_cods(txt):
    global Codes, Code0, CodeM, fail, PPLS, PPLS_Vivod, SonJ
    f = open(txt, 'r')
    txt1 = f.readlines()
    f.close()
    ln = len(txt1[1])
    for i in range(len(txt1)):
        SonJ["Codes"].append({"Code": txt1[i][:ln-1], "Meth": 0})
    re_and_wr(SonJ, fail)

fail = "Manager.json"



SonJ = read(fail)
ID_MD = SonJ["ID_MD"]
Tosen = SonJ["Tosen"]
PPLS  = SonJ["PPLS"]
PPLS_Vivod = "Список участников:"
for i in range(1, len(PPLS)):
    PPLS_Vivod +="\n" + str(i) +".-  "+ PPLS[i]["FIO"]+ "  (id" + str(PPLS[i]["ManID"])+ ")"
Codes = SonJ["Codes"]
Code0 = []
CodeM = []
for i in range(1, len(Codes)):
    Code0.append(Codes[i]["Code"])
    CodeM.append(Codes[i]["Meth"])


#new_cods("cods.txt")
