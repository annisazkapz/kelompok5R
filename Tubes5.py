from browser import document, alert  # Import Library Brython 

# Deklarasi Variable
input1 = document['input1']
button = document['btn']
output = document['output']
selectType = document['select-type']
selectCalculated = document['select-calculated']

# Dictionary Panjang
type1 = {'milimeter': {'milimeter': {'Rumus': lambda panjang: panjang, 'input1': 'Masukkan panjang'},
                           'centimeter': {'Rumus': lambda panjang: panjang /10, 'input1': 'Masukkan panjang'},
                           'desimeter': {'Rumus': lambda panjang: panjang /100, 'input1': 'Masukkan panjang'},
                           'meter': {'Rumus': lambda panjang: panjang /1000, 'input1': 'Masukkan panjang'},
                           'dekameter' : {'Rumus': lambda panjang: panjang /10000, 'input1': 'Masukkan panjang'},
                           'hektometer' : {'Rumus': lambda panjang: panjang /100000, 'input1': 'Masukkan panjang'},
                           'kilometer' : {'Rumus': lambda panjang: panjang/1000000, 'input1': 'Masukkan panjang'}},
        'centimeter': {'milimeter': {'Rumus': lambda panjang: panjang *10, 'input1': 'Masukkan panjang'},
                           'centimeter': {'Rumus': lambda panjang: panjang, 'input1': 'Masukkan panjang'},
                           'desimeter': {'Rumus': lambda panjang: panjang /10, 'input1': 'Masukkan panjang'},
                           'meter': {'Rumus': lambda panjang: panjang /100, 'input1': 'Masukkan panjang'},
                           'dekameter': {'Rumus': lambda panjang: panjang /1000, 'input1': 'Masukkan panjang'},
                           'hektometer': {'Rumus': lambda panjang: panjang /10000, 'input1': 'Masukkan panjang'},
                           'kilometer': {'Rumus': lambda panjang: panjang /100000, 'input1': 'Masukkan panjang'}},
        'desimeter': {'milimeter': {'Rumus': lambda panjang: panjang *100, 'input1': 'Masukkan panjang'},
                           'centimeter': {'Rumus': lambda panjang: panjang *10, 'input1': 'Masukkan panjang'},
                           'desimeter': {'Rumus': lambda panjang: panjang, 'input1': 'Masukkan panjang'},
                           'meter': {'Rumus': lambda panjang: panjang /10, 'input1': 'Masukkan panjang'},
                           'dekameter': {'Rumus': lambda panjang: panjang /100, 'input1': 'Masukkan panjang'},
                           'hektometer': {'Rumus': lambda panjang: panjang /1000, 'input1': 'Masukkan panjang'},
                           'kilometer': {'Rumus': lambda panjang: panjang /10000, 'input1': 'Masukkan panjang'}},
        'meter': {'milimeter': {'Rumus': lambda panjang: panjang *1000,'input1': 'Masukkan panjang'},
                           'centimeter': {'Rumus': lambda panjang: panjang *100, 'input1': 'Masukkan panjang'},
                           'desimeter': {'Rumus': lambda panjang: panjang *10 , 'input1': 'Masukkan panjang'},
                           'meter': {'Rumus': lambda panjang: panjang,'input1': 'Masukkan panjang'},
                           'dekameter': {'Rumus': lambda panjang: panjang /10, 'input1': 'Masukkan panjang'},
                           'hektometer': {'Rumus': lambda panjang: panjang /100, 'input1': 'Masukkan panjang'},
                           'kilometer': {'Rumus': lambda panjang: panjang /1000, 'input1': 'Masukkan panjang'}},
        'dekameter': {'milimeter': {'Rumus': lambda panjang: panjang *10000,'input1': 'Masukkan panjang'},
                           'centimeter': {'Rumus': lambda panjang: panjang *1000, 'input1': 'Masukkan panjang'},
                            'desimeter': {'Rumus': lambda panjang: panjang *100, 'input1': 'Masukkan panjang'},
                            'meter': {'Rumus': lambda panjang: panjang *10, 'input1': 'Masukkan panjang'},
                            'dekameter': {'Rumus': lambda panjang: panjang, 'input1': 'Masukkan panjang'},
                            'hektometer': {'Rumus': lambda panjang: panjang /10, 'input1': 'Masukkan panjang'},
                            'kilometer': {'Rumus': lambda panjang: panjang /100, 'input1': 'Masukkan panjang'}},
        'hektometer': {'milimeter': {'Rumus': lambda panjang: panjang *100000,'input1': 'Masukkan panjang'},
                            'centimeter': {'Rumus': lambda panjang: panjang *10000, 'input1': 'Masukkan panjang'},
                            'desimeter': {'Rumus': lambda panjang: panjang *1000, 'input1': 'Masukkan panjang'},
                            'meter': {'Rumus': lambda panjang: panjang *100, 'input1': 'Masukkan panjang'},
                            'dekameter': {'Rumus': lambda panjang: panjang *10, 'input1': 'Masukkan panjang'},
                            'hektometer': {'Rumus': lambda panjang: panjang, 'input1': 'Masukkan panjang'},
                            'kilometer': {'Rumus': lambda panjang: panjang /10, 'input1': 'Masukkan panjang'}},
        'kilometer': {'milimeter': {'Rumus': lambda panjang: panjang *1000000, 'input1': 'Masukkan panjang'},
                            'centimeter': {'Rumus': lambda panjang: panjang *100000, 'input1': 'Masukkan panjang'},
                            'desimeter': {'Rumus': lambda panjang: panjang *10000, 'input1': 'Masukkan panjang'},
                            'meter': {'Rumus': lambda panjang: panjang *1000, 'input1': 'Masukkan panjang'},
                            'dekameter': {'Rumus': lambda panjang: panjang *100, 'input1': 'Masukkan panjang'},
                            'hektometer': {'Rumus': lambda panjang: panjang *10, 'input1': 'Masukkan panjang'},
                            'kilometer': {'Rumus': lambda panjang: panjang , 'input1': 'Masukkan panjang'}}}                    


# Fungsi yang akan dijalankan ketika pilihan panjang diubah
def selectTypeAction(ev):
    x = selectType.value
    # Reset Input Field
    for i in range(1, 5):
        input[str(i)].value = ''
        input[str(i)].disabled = False

# Fungsi untuk mengubah string dari input ke int atau float
def getNum(x):
    temp = x
    # Convert string ke int
    try:
        temp = int(x)
    # Jika convert string ke int gagal (ValueError), maka convert ke float
    except ValueError:
        temp = float(x)
    finally:
        # Jika input (var temp) masih string (gagal convert ke int dan float), 
        # maka munculkan alert dan return dengan variable kosong ('')
        if temp != '' and type(temp) is str:
            alert('Harap masukkan panjang')
            temp = ''
            input1.value = temp
            return temp
        # Jika salah satu convert berhasil, maka return
        else:
            return temp

# Fungsi untuk memanggil rumus pada dictionary
def Rumus(x, num1):
    y = selectCalculated.value
    for key in type1.keys():
        if key.find(x) > -1:
            return type1[x][y]['Rumus'](num1)

# Fungsi Main
# Dijalankan ketika button di-click atau tombol 'enter' ditekan
def main(ev):
    num1 = getNum(input1.value)
    result = Rumus(selectType.value, num1)
    output.textContent = str(result)

# Fugnsi keyEnter
# Fungsi yang mengarahkan ke 'Fungsi Main' ketika tombol 'enter' ditekan
def keyEnter(ev):
    traceKey = f"{ev.code}"
    if traceKey == 'Enter':
        main(0)

selectType.bind('change', selectTypeAction) # Ketika pilihan panjang berubah, maka akan menjalankan fungsinya
button.bind('click', main) # Memanggil 'Fungsi Main' ketika button di-click

# Mengarahakan ke 'Fungsi keyEnter' ketiak 'enter' ditekan pada salah satu input field
input1.bind("keypress", keyEnter)