import pandas as pd
from pandas.errors import EmptyDataError

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
            Identical_columns = colums_1.intersection(colums_2)
            errors_pd_dtype = []

            for colums in Identical_columns:
                if file_pd_1[colums].dtype != file_pd_2[colums].dtype:
                    errors_pd_message = ((f'- В столбце "{colums}" тип данных не соответсвует ожидаемому.'
                                        f'\nОжидается: {file_pd_1[colums].dtype}. Фактически: {file_pd_2[colums].dtype}\n'))
                    errors_pd_dtype.append(errors_pd_message)
            if errors_pd_dtype:
                raise TypeError('\n'.join(errors_pd_dtype))

        except TypeError as e:
                
                if list(colums_1) != list(colums_2):
                    print(f'Структура датафрейма не соответствует ожидаемой'
                        f'\n- Названия столбцов не совпадают'
                        f'\nОжидается: {list(colums_1)},'
                        f'\nФактические: {list(colums_2)}'
                        f'\n{e}')
    
                else:
                    print(f'Структура датафрейма не соответствует ожидаемой'
                        f'\n- Названия столбцов совпадают'
                        f'\nОжидается: {list(colums_1)},'
                        f'\nФактические: {list(colums_2)}'
                        f'\n{e}')

        except EmptyDataError:
            print('Возникла следующая ошибка: Один из датафреймов пуст или оба датафрейма пусты')

        except FileNotFoundError:
            print('Возникла следующая ошибка: No such file or directory: ', self._file_name_1,'or', self._file_name_2)
        
        except Exception:
            print(f'Возникла неизвестная ошибка. Прошу, сообщите нашей компании')

        else: 
            print('Все действия выполнены успешно. Империя благодарит вас за работу')