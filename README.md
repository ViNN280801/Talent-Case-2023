# Talent Case Contest 2023

## В борьбе за уникальность: выявление рерайтинга

### Введение

**Рерайтинг** – обработка исходных текстовых материалов в целях их дальнейшего использования. В отличие от копирайтинга, за основу берётся уже написанный текст, который переписывается своими словами с сохранением смысла.

**Обработка естественного языка (NLP)** – это технология машинного обучения, которая дает компьютерам возможность интерпретировать, манипулировать и понимать человеческий язык.

Обработка естественного языка сочетает в себе компьютерную лингвистику, машинное обучение и модели глубокого обучения для обработки человеческого языка. Компьютерная лингвистика – это наука о понимании и построении моделей человеческого языка с помощью компьютеров и программных инструментов. Исследователи используют методы компьютерной лингвистики, такие как синтаксический и семантический анализ, для создания платформ, помогающих машинам понимать разговорный человеческий язык. Такие инструменты, как переводчики языков, синтезаторы текста в речь и программное обеспечение для распознавания речи, основаны на компьютерной лингвистике.

Обработка естественного языка имеет решающее значение для эффективного анализа текстовых и речевых данных. Таким образом, можно преодолевать различия в диалектах, сленге и грамматических нарушениях, типичных для повседневных разговоров. Компании используют этот метод для нескольких автоматизированных задач, таких как:

- Обработка, анализ и архивирование больших документов
- Анализ отзывов клиентов или записей колл-центра
- Запуск чат-ботов для автоматизированного обслуживания клиентов
- Ответы на вопросы «кто, что, когда и где»
- Классификация и извлечение текста

Полезные ссылки:\
[ML: Введение в машинное обучение](https://qudata.com/ml/ru/ML_Intro.html)\
[ML: N-граммы](https://qudata.com/ml/ru/ML_NGrams.html)\
[ML: Embedding слов](https://qudata.com/ml/ru/NN_Embedding.html)\
[ML: Embedding слов v2](https://qudata.com/ml/ru/NN_Embedding_Word2Vec.html)

### Постановка задачи

#### Цель

Используя предоставленный датасет (`sample.json`), реализовать алгоритм выявления рерайтинга:

1. Проанализировать основные приёмы рерайтинга;
2. Проанализировать различные методы обработки текстов;
3. Подобрать техническое решение для обработки файла;
4. Реализовать поиск дубликатов одним из найденных методов
5. Придумать не менее 2-х методов, которые позволят выявить
   переписанные тексты;
6. Получить список рерайтов на основе реализации алгоритмов.

#### Ограничение

Необходимо использовать исключительно алгоритмический подход. Применение нейронных сетей и готовых моделей машинного обучения запрещено.

## First method

### Description

The essense of this method - comparing symbols. Implementation of this idea consists of some simple operations:

1. Get each sentece with it ID from the JSON dataset
2. Convert each symbol of the string to lowercase
3. Erase whitespaces, all punctuation, special symbols and other non-letter symbols
4. Compare each resulting symbol sequenece with each, to find the same sequences
5. Writing IDs of the same by meaning sentences

### Usage Example

```bash
py main.py
```

Results:

```
re is already installed
json is already installed
Enter name of the file >> sample.json
The same by meaning sentences:
[2, 15, 150]
[3, 266]
[4, 13]
...
[305, 315]
[306, 412]
[307, 344]
[328, 379]
[338, 347]
[350, 374]
[388, 405]
```

Let's see [2, 15, 150] sentences from the dataset:

```json
[
  {
    "id": 2,
    "text": "Почему она так со мной поступает?"
  },
  {
    "id": 15,
    "text": "Почему она так с ней поступает?"
  },
  {
    "id": 150,
    "text": "Почему он так со мной поступает?"
  }
]
```

Or [328, 379]:

```json
[
  {
    "id": 328,
    "text": "Я знаю, что это для тебя важно."
  },
  {
    "id": 379,
    "text": "Я знаю, что для тебя это важно."
  }
]
```

### Advantages

1. Fast finding the rewrites by shuffle words in the sentence

### Disadvantages

1. Bad working on random sequences

#### Exact example of disadvantage

Assume, that we can put on input these two sentences

```
Привет, мир!
ирП! ,теривм
```

In point of view of symbol sequence equality - these two sentences are equal. But there is no any meaning on the second sentence in point of view of human. For human this is just symbol sequence.

Let's check them on the custom dataset (`custom_dataset.json`):

```json
[
  {
    "id": 1,
    "text": "Привет, мир!"
  },
  {
    "id": 2,
    "text": "ирП! ,теривм"
  }
]
```

```bash
py main.py
```

Getting the result:

```
The same by meaning sentences:
[1, 2]
```
