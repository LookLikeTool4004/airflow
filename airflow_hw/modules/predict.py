import dill
import os
import pandas as pd
import json


def predict():
    # указываем путь
    path = os.environ.get('PROJECT_PATH', '.')

    # Считываем модель и время
    model_name = os.listdir(path=f'{path}/data/models')[-1]
    model_filename = f'{path}/data/models/{model_name}'
    time = model_name.split('.')[0].split('-')[-1]
    with open(model_filename, 'rb') as file:
        model = dill.load(file)

    # Функция для получения списка файлов для предсказания
    def file_list():
        return os.listdir(path=f'{path}/data/test')

    # Функция предсказания
    def prediction(file_name):
        file_path = f'{path}/data/test/{file_name}'
        with open(file_path) as fl:
            form = json.load(fl)
        df = pd.DataFrame.from_dict([form])
        y = model.predict(df)
        res = {'car_id': df['id'], 'pred': y[0]}
        return res

    # Функция получения списка ответов по предсказаниям
    def results_list(file_list):
        res_list = []
        for elem in file_list:
            res_list.append(prediction(elem))
        return res_list

    # Получаем список файлов для предсказания
    tests = file_list()

    # Производим расчет по этому списку
    final_list = results_list(tests)

    # Создаем датафрейм и сохраняем его в файл
    res_df = pd.DataFrame(final_list)
    res_df.to_csv(f'{path}/data/predictions/preds_{time}.csv', index=False)

if __name__ == '__main__':
    predict()
