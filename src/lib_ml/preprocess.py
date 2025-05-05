import re
import nltk

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download stopwords from nltk
nltk.download('stopwords')

def preprocess(dataset, num_reviews):
    """
    Preprocesses the reviews.
    
    Parameters:
    - dataset: pandas DataFrame, the dataset containing reviews.
    - num_reviews: int, the number of reviews to process.
    
    Returns:
    - list: A list of preprocessed reviews (corpus).
    """
    ps = PorterStemmer()
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')

    corpus = []

    for i in range(num_reviews):
        review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
        review = review.lower()
        review = review.split()
        review = [ps.stem(word) for word in review if word not in set(all_stopwords)]
        review = ' '.join(review)
        corpus.append(review)

    return corpus
