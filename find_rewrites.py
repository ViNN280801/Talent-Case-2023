import nltk
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from get_sentences import getSentencesFromJSONDataset

dataset = getSentencesFromJSONDataset(str(input('Enter name of the file >> ')))


def get_synonyms(word):
    synonyms = set()
    for syn in wn.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)


def generate_rewrites(sentence):
    lemmatizer = WordNetLemmatizer()
    words = nltk.word_tokenize(sentence)
    rewrites = []
    for word in words:
        synonyms = get_synonyms(lemmatizer.lemmatize(word))
        if synonyms:
            rewrites.append(synonyms)
        else:
            rewrites.append([word])
    return rewrites


for sentence in dataset:
    rewrites = generate_rewrites(sentence)
    print(f"Original Sentence: {sentence}")
    for rewrite in rewrites:
        print(" ".join(rewrite))
    print()

### DON'T WORK -> NLTK doesn't support Russian lang
