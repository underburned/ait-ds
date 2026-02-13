# Технологии искусственного интеллекта. Анализ данных

© Петров М.В., старший преподаватель кафедры киберфотоники, Самарский университет

## Лекции

1. [Библиотека Pandas. Визуализация данных](lectures/lecture_1/lecture_1.ipynb)
2. Задачи классификации. Метрики качества. Классификация *kNN*
3. Деревья решений
4. Линейная регрессия. Метрики качества
5. Градиентный бустинг
6. **[TBA]**

## Лабораторные работы

1. [Визуализация данных](labs/lab_1.md)
2. [Классификация *kNN* **[предваритаельная версия]**](labs/lab_2.md)
3. [Классификация. Деревья решений **[предваритаельная версия]**](labs/lab_3.md)
4. [Линейная регрессия **[предваритаельная версия]**](labs/lab_4.md)
5. [Градиентный бустинг **[предваритаельная версия]**](labs/lab_5.md)
6. **[TBA]**

> Задания в L2 - L5 уточняются.

### Требования к оформлению лабораторных работ

1. Присылать ответы в jupyter-блокнотах со следующим названием файла: `<Номер группы>_<ФамилияИО>_lab_<номер лабораторной>_<тема лабораторной>.ipynb`, например, `0000_PetrovMV_lab_1_data_visualization.ipynb`
   
   > В заголовке самого блокнота (в самой первой ячейке) &ndash; название задания и ФИО автора.

2. Все ячейки, требующие вычисления, должны быть вычислены, и в присылаемом блокноте должен содержаться вывод ячеек.
   > Пустой блокнот с очищенным выводом ячеек не принимается.  

   Желательно сделать финальный прогон всего питон-ноутбука с 1 по последнюю ячейку для проверки, что различные правки кода в ячейках последовательны, а не внесены в "out of order" режиме.

3. Внутри в markdown-ячейках обязательно дублировать условие задачи в виде оглавления, каждую подзадачу оформить markdown-ячейкой с описанием подзадачи.
   > Если в ячейке кода расположен код нескольких заданий с пачкой принтов с результатами выполнения, которые (принты) скопом выводятся в последующей ячейке, то такая работа будет отправлена на доработку без смысловой проверки. Читать такое неудобно, долго и нудно, вся прелесть ноутбуков с нативным красивым рендером датафреймов теряется.

4. Желательно прокомментировать блоки кода, выполняющие ту или иную функцию.

5. Код по возможности структурировать в небольшие логические блоки, каждый в своей ячейке, чтобы легко было его понять.

6. Необходимо привести краткое описание датасета и указать ссылку на него (или прислать вместе с питон-тетрадкой). Привести список признаков с кратким описанием и единицой измерения. Явно указать целевой признак.

7. Если в пункте задания явно указано:
   - сравнить метрики &ndash; недостаточно вывести полученные цифры через принты или таблицой, необходимо кратко описать текстом, какая модель (метод) лучше и почему (метрики/критерии/хрустальный шар)
   - выбрать лучшую модель &ndash; на каком основании (метрики/критерии/хрустальный шар)
   - сделать вывод &ndash; словесно описать результат выполнения пункта задания

### Датасеты

- [Встроенные датасеты в sklearn](https://scikit-learn.org/stable/datasets)
- [Google-поиск по датасетам](https://datasetsearch.research.google.com/)

Репозитории с датасетами:
- [Kaggle](https://www.kaggle.com/datasets)  
  [Как начать работу в Kaggle: руководство для новичков в Data Science](https://habr.com/ru/post/248395/)
- [Материалы с курса OpenDataScience](https://nbviewer.org/github/Yorko/mlcourse.ai/tree/main/data/) или [тут](https://github.com/Yorko/mlcourse.ai/tree/master/data/)
- [Датасеты университета Калифорнии](https://archive.ics.uci.edu/ml/datasets)
- [Учебные датасеты для R](https://vincentarelbundock.github.io/Rdatasets/datasets.html)
- [Датасеты от FiveThirtyEight](https://data.fivethirtyeight.com/)
- [Подборка на habr](https://habr.com/ru/post/452740)
- [Подборка на Reddit](https://www.reddit.com/r/datasets/)
- [Ещё подборка 1](https://towardsai.net/p/machine-learning/best-free-datasets-for-machine-learning-and-data-science/stanfordai/3451/)
- [Ещё подборка 2](https://towardsdatascience.com/top-sources-for-machine-learning-datasets-bb6d0dc3378b)

Разные открытые данные:
- [Списки источников открытых данных от Яндекса](https://yandex.ru/promo/oda/useful)
- [Портал открытых данных Российской Федерации](https://data.gov.ru/)
- [Портал открытых данных правительства Москвы](https://data.mos.ru/opendata)
- [Открытые данные Сбербанка](https://www.sberbank.com/ru/analytics/opendata)
- [Открытые данные Министерства финансов РФ](https://www.minfin.ru/opendata/)
- [Открытые данные Министерства культуры РФ](https://opendata.mkrf.ru/opendata/)

## Материал для самостоятельного изучения

1. [Установка Python. Менеджеры пакетов. Виртуальное окружение. Настройка IDE](self-study/python_stuff.md)
2. [Питон-ноутбук с примерами использования numpy](self-study/numpy_examples.ipynb)
3. [Pandas. Базовые операции](self-study/pandas_api.md)
4. **[TBA]**

## Разное

### Корректный дамп виджетов (графиков) в jupyter notebook

Для корректного сохранения *отрендеренных* графиков в питон-тетрадке необходимо включить параметр `Save Widget State Automatically`: `Settings` &rarr; `Save Widget State Automatically`.
> Или `Save Jupyter widget state in notebooks`: `Settings` &rarr; фильтр по `widget` &rarr; `Jupyter Widgets` &rarr; `Save Jupyter widget state in notebooks`.

### Визуализация JS графиков

С визуализацией некоторых JS графиков может помочь [nbviewer](https://nbviewer.org/). Например, графики с использованием `Plotly` в 1 лекции и некоторые JS графики из 6 лекции отображаются в `nbviewer`, но графики, сгенерированные `CatBoost` &ndash; нет (хотя под капотом там тоже `Plotly`).  

> Для того чтобы графики с JS кодом и некоторые HTML блоки рендерились нормально, необходимо подписать ноутбук согласно [Trusting Notebooks](https://jupyter-notebook.readthedocs.io/en/latest/notebook.html#trusting-notebooks):

```bash
jupyter trust lecture_6.ipynb
```

Должно появиться сообщение:
```bash
Signing notebook: .\lecture_6.ipynb
```

В [документации CatBoost'а](https://catboost.ai/docs/en/features/visualization_jupyter-notebook) насчет виджетов указано следующее:
> CatBoost widgets do work in JupyterLab but only for versions 3.x, versions 4.x support is in progress.

[Требуется](https://catboost.ai/docs/en/installation/python-installation-additional-data-visualization-packages) `ipywidgets` версии 7.x или новее.