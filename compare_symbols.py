# Installing dependencies
from subprocess import call
call(['py', 'inst_dependencies.py'])

# Including regex and json
import re, json


STOP_WORDS = {
    'и', 'или', 'но', 'дабы', 'затем', 'потом', 'лишь', 'только',
    'он', 'мы', 'его', 'вы', 'вам', 'вас', 'ее', 'что', 'который',
    'их', 'все', 'они', 'я', 'весь', 'мне', 'меня', 'таким', 'для',
    'на', 'по', 'со', 'из', 'от', 'до', 'без', 'над', 'под', 'за',
    'при', 'после', 'во', 'не', 'же', 'то', 'бы', 'всего', 'итого',
    'даже', 'да', 'нет', 'ой', 'ого', 'эх', 'браво', 'здравствуйте',
    'спасибо', 'извините', '1', '2', '3', 'один', 'два', 'три',
    'первый', 'второй', 'третий', '.', ',', '—', '_', '=', '+', '/',
    '!', ';', ':', '%', '?', '*', 'скажем', 'может', 'допустим', 'честно',
    'говоря', 'например', 'на', 'самом', 'деле', 'однако', 'вообще', 'в', 'общем', 'вероятно',
    'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'к', 'л', 'м', 'н', 'о',
    'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я',
    'что-то', 'какой-то', 'где-то', 'как-то', 'дальше', 'ближе', 'раньше', 'позже', 'когда-то',
    'очень', 'минимально', 'максимально', 'абсолютно', 'огромный', 'предельно', 'сильно', 'слабо', 'самый',
    'сайт', 'давать', 'всегда', 'однако'
}


def getSentencesFromJSONDataset(filename: str) -> list:
    """
    Extracts sentences from the dataset represented as a JSON file.

    Args:
        filename (str): The name of the JSON file from which to extract sentences.

    Returns:
        List of the sentences from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    result = []

    for entry in data:
        sentence = {
            'id': entry['id'],
            'text': entry['text']
        }
        result.append(sentence)

    return result


def deleteNonLettersFromText(text: str) -> str:
    """
    Remove all non-letter and additional special characters from a text.

    Args:
        text (str): Input text.

    Returns:
        Text with non-letter and additional special characters removed.
    """
    # 1) Finding tokens by specified pattern and separate (pattern is sequence of Russian letters)
    # ' ' as a 2nd param means that it's a replacement string, it replaces any char
    # matched by regex with a whitespace
    # 2) Splitting `text` into words using whitespaces as the separator
    # 3) `' '.join()` makes a string from the iterable object - list in this case
    # 4) `lower()` method lowercasing all symbols
    return (' '.join(re.sub(r'[^А-Яа-я$]', ' ', text).split())).lower()


def deleteStopWordsFromSentences(sentences: list) -> list:
    """
    Remove stop words from a list of sentences.

    Args:
        sentences (list): List of sentences.

    Returns:
        List of sentences with removed stop words.
    """
    cleaned_sentences = []

    for sentence in sentences:
        text = sentence['text']
        words = text.split()

        # Creating dictionary with ID and sentence
        # where sentence will be without stop words
        cleaned_sentence = {
            'id': sentence['id'],
            'text': ' '.join([word for word in words if word not in STOP_WORDS])
        }
        cleaned_sentences.append(cleaned_sentence)

    return cleaned_sentences


def findEqualSentences(sentences: list) -> list:
    """
    Find equal sets of sentences based on the given criteria.

    Args:
        sentences (list): List of sentences with IDs.

    Returns:
        A list of lists, where each inner list contains IDs of sentences with equal sets.
    """
    cleaned_sentences = deleteStopWordsFromSentences(sentences)

    # Convert the cleaned sentences to a list of pairs (id, set of letters)
    sentence_sets = [(sentence['id'], set(deleteNonLettersFromText(
        sentence['text']))) for sentence in cleaned_sentences]

    # Create a list to store lists of IDs with equal sets
    equal_sets = []

    # Iterate through the list of sentence sets
    for i, (id1, set1) in enumerate(sentence_sets):
        # Create a list to store IDs of sentences with equal sets
        equal_sentences_id = [id1]

        for j, (id2, set2) in enumerate(sentence_sets):
            # Skip comparing the same set
            if i == j:
                continue

            # Compare sets
            if set1 == set2:
                equal_sentences_id.append(id2)

        # Sort the list of IDs to ensure a consistent order
        equal_sentences_id.sort()

        # Append the list of equal IDs to the result if it's not already there
        if equal_sentences_id not in equal_sets:
            equal_sets.append(equal_sentences_id)

    return equal_sets


def runFirstMethod(filename: str) -> None:
    sameSentences = findEqualSentences(getSentencesFromJSONDataset(filename))

    # Check if all sublists have only a single element
    if all(len(equal_group) == 1 for equal_group in sameSentences):
        print('First method to find identical sentences by meaning failed')
    else:
        print('The same by meaning sentences:')
        [print(equal_group) for equal_group in sameSentences if len(equal_group) != 1]
