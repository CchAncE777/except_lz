import pandas as pd
from pandas.errors import EmptyDataError

file_1 = input('Введите имя первого файла cо значением: ')
file_2 = input('Введите имя второго файла со значением: ')

class Check():
    
    def __init__(self, file_1, file_2):
        self._file_name_1 = file_1
        self._file_name_2 = file_2

    def errors_pd(self):
        
        try:
            file_pd_1 = pd.read_csv(self._file_name_1)
            file_pd_2 = pd.read_csv(self._file_name_2)
            colums_1 = file_pd_1.columns
            colums_2 = file_pd_2.columns
            

        except KeyError:
                
                if colums_1 == colums_2:
                    print(f'Структура датафрейма не соответствует ожидаемой'
                        f'\n- Названия столбцов не совпадают'
                        f'\n{colums_1}, {colums_2}')
    
                else:
                    print(f'Структура датафрейма не соответствует ожидаемой'
                        f'\n- Названия столбцов совпадают'
                        f'\n{colums_1}, {colums_2}')

        except EmptyDataError:
            print('Возникла следующая ошибка: Один из датафреймов пуст или оба датафрейма пусты')

        except FileNotFoundError:
            print('Возникла следующая ошибка: No such file or directory: ', self._file_name_1,'or', self._file_name_2)
        
        except Exception:
            print(f'Возникла неизвестная ошибка. Прошу, сообщите нашей компании')

        else: 
            print('Все действия выполнены успешно. Империя благодарит вас за работу')

    
C = Check(file_1, file_2)

C.errors_pd()