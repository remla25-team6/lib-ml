# lib-ml

`lib-ml` is a Python library designed for preprocessing text data, particularly for sentiment analysis models. It provides utilities to clean, tokenize, and preprocess text data efficiently.

## Features
`preprocess.py` provides methods that achieve the following:
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

## Usage Example
You can use the `preprocess` method as follows:
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

## Setup
To set up a local development environment:
```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # On Linux/macOS
venv\Scripts\activate         # On Windows

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install .                 # Installs from pyproject.toml
```

## CI/CD
This project uses GitHub Actions for automated releases. 

### Release
To publish an official release:
1. Ensure all changes are committed and pushed to any desired `release` branch.
2. Tag the commit with a version like `v1.0.0` and push:
    ```bash
    git tag v1.0.0
    git push origin v1.0.0
    ```
3. This triggers the `release.yml` workflow, which:
   * Builds the package from `main`.
   * Updates the version in `pyproject.toml`.
   * Publishes the package as a GitHub release with the tag name.

### Pre-release
To publish a pre-release for testing:
1. Push a commit to the `main` branch.
2. The `prerelease.yml` workflow automatically runs on every commit to `main`.
3. It creates a pre-release using the current timestamp (e.g., `0.1.0-pre.20250625.123456`).
4. These packages are available via:
   ```bash
   pip install git+https://github.com/remla25-team6/lib-ml@<pre-release-tag>
   ```

## AI Disclaimer
Used ChatGPT-4o to refine README.