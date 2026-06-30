import re
import sys
from collections import Counter

try:
    import nltk
    from nltk.corpus import stopwords
    from nltk.stem import SnowballStemmer, WordNetLemmatizer
except ImportError:
    nltk = None

CUSTOM_STOPWORDS = {
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are",
    "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but",
    "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from",
    "further", "had", "has", "have", "having", "he", "her", "here", "hers", "herself", "him",
    "himself", "his", "how", "i", "if", "in", "into", "is", "it", "its", "itself", "me", "more",
    "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought", "our",
    "ours", "ourselves", "out", "over", "own", "same", "she", "should", "so", "some", "such",
    "than", "that", "the", "their", "theirs", "them", "themselves", "then", "there", "these",
    "they", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we",
    "were", "what", "when", "where", "which", "while", "who", "whom", "why", "with", "would", "you",
    "your", "yours", "yourself", "yourselves"
}

DEFAULT_TEXT = (
    "Natural language processing is a field of artificial intelligence that gives computers the ability "
    "to read, understand, and derive meaning from human languages. It combines rule-based modeling of "
    "language with statistical, machine learning, and deep learning models. These technologies are used in a "
    "wide range of applications such as chatbots, sentiment analysis, search engines, and voice assistants. "
    "This sample text is provided to demonstrate tokenization, stopword removal, stemming, lemmatization, "
    "keyword extraction, and word frequency analysis. The goal is to show how text data can be transformed "
    "into structured information for NLP tasks."
)


def load_stopwords():
    if nltk:
        try:
            stopwords.words('english')
        except LookupError:
            nltk.download('stopwords', quiet=True)
        return set(stopwords.words('english'))
    return CUSTOM_STOPWORDS


def get_stemmer():
    if nltk:
        try:
            return SnowballStemmer('english')
        except LookupError:
            pass
    return None


def get_lemmatizer():
    if nltk:
        try:
            return WordNetLemmatizer()
        except LookupError:
            pass
    return None


def tokenize(text):
    return re.findall(r"\b[a-zA-Z']+\b", text.lower())


def remove_stopwords(tokens, stopword_set):
    return [token for token in tokens if token not in stopword_set]


def stem_tokens(tokens, stemmer):
    if stemmer:
        return [stemmer.stem(token) for token in tokens]

    # fallback simple suffix stripping
    suffixed = []
    for token in tokens:
        if token.endswith('ing') and len(token) > 4:
            suffixed.append(token[:-3])
        elif token.endswith('ed') and len(token) > 3:
            suffixed.append(token[:-2])
        elif token.endswith('s') and len(token) > 2:
            suffixed.append(token[:-1])
        else:
            suffixed.append(token)
    return suffixed


def lemmatize_tokens(tokens, lemmatizer):
    if lemmatizer:
        try:
            nltk.data.find('corpora/wordnet')
        except LookupError:
            nltk.download('wordnet', quiet=True)
        return [lemmatizer.lemmatize(token) for token in tokens]
    return tokens


def extract_keywords(tokens, top_n=10):
    counts = Counter(tokens)
    return counts.most_common(top_n)


def display_analysis(text):
    stopword_set = load_stopwords()
    stemmer = get_stemmer()
    lemmatizer = get_lemmatizer()

    tokens = tokenize(text)
    filtered = remove_stopwords(tokens, stopword_set)
    stemmed = stem_tokens(filtered, stemmer)
    lemmatized = lemmatize_tokens(filtered, lemmatizer)

    frequency = Counter(filtered)
    keywords = extract_keywords(filtered, 12)

    print('\n=== Text Analyzer Results ===')
    print(f'Total characters: {len(text)}')
    print(f'Total tokens: {len(tokens)}')
    print(f'Tokens after stopword removal: {len(filtered)}')

    print('\nTop keywords:')
    for word, count in keywords:
        print(f'  {word}: {count}')

    print('\nSample stemmed tokens:')
    print('  ', ' '.join(stemmed[:15]))

    print('\nSample lemmatized tokens:')
    print('  ', ' '.join(lemmatized[:15]))

    print('\nMost frequent words:')
    for word, count in frequency.most_common(10):
        print(f'  {word}: {count}')


def main():
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
    else:
        print('Enter your article text. Press Enter twice to finish, or Ctrl+D to use the default sample text.')
        lines = []
        try:
            while True:
                line = input()
                if not line.strip() and lines:
                    break
                lines.append(line)
        except EOFError:
            pass

        text = '\n'.join(lines).strip() or DEFAULT_TEXT

    display_analysis(text)


if __name__ == '__main__':
    main()
