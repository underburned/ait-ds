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

1. Pandas. Визуализация данных
2. Классификация *kNN*
3. Классификация. Деревья решений
4. Линейная регрессия
5. Градиентный бустинг
6. **[TBA]**

## Материал для самостоятельного изучения

1. [Установка Python. Менеджеры пакетов. Виртуальное окружение. Настройка IDE](self-study/python_stuff.md)
2. [Питон-ноутбук с примерами использования numpy](self-study/numpy_examples.ipynb)
3. [Pandas. Базовые операции](self-study/pandas_api.md)
4. **[TBA]**

## Разное

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