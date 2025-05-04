# lib-ml

`lib-ml` is a Python library designed for preprocessing text data, particularly for sentiment analysis models. It provides utilities to clean, tokenize, and preprocess text data efficiently.

## Features

- **Text Cleaning**: Remove unwanted characters, HTML tags, and special symbols.
- **Lowercasing**: Converts all text to lowercase for uniformity.
- **Tokenization**: Splits text into individual words (tokens).
- **Stopword Removal**: Filters out common English stopwords, with an exception for the word "not" to preserve negations.

## Installation

To install the library, you can use the following command after the release is published:

(Example for v0.1.0), change as needed.
```bash
pip install git+https://github.com/remla25-team6/lib-ml@v0.1.0
```

## Usage example
```python
import pandas as pd
from lib_ml.preprocess import preprocess

# Example dataset
data = {'Review': ["I <3 love this product!", "This is not good.", "Enjoyable - experience"]}
dataset = pd.DataFrame(data)

# Preprocess the reviews
num_reviews = len(dataset)
corpus = preprocess(dataset, num_reviews)

print(corpus)
# Output: ['love product', 'not good', 'enjoy experi']
```



## CI/CD
This project uses GitHub Actions for automated releases. When a new tag matching the pattern vX.Y.Z is pushed, the workflow:

Updates the version in pyproject.toml.
Builds the package.
Creates a GitHub release with the built package.