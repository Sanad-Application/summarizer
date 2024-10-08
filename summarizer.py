import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.probability import FreqDist

nltk.download('punkt')
nltk.download('stopwords')


def text_summarize(text):

    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

    frequency_dist = FreqDist(filtered_words)

    max_freq = max(frequency_dist.values())
    sentence_scores = {}

    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in frequency_dist:
                if sentence in sentence_scores:
                    sentence_scores[sentence] += frequency_dist[word] / max_freq
                else:
                    sentence_scores[sentence] = frequency_dist[word] / max_freq


    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:3]
    summary = TreebankWordDetokenizer().detokenize(summary_sentences)
    
    return summary
