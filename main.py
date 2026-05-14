from excep import Check

def main(): 
    file_1 = input('Введите имя первого файла cо значением(Ожидаемого): ')
    file_2 = input('Введите имя второго файла со значением(Фактического): ')
    C = Check(file_1, file_2)
    C.errors_pd()

if __name__ == '__main__':
    main()


