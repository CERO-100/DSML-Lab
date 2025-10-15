import nltk
from nltk import word_tokenize, pos_tag, bigrams, trigrams
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download necessary resources (only once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

# Step 1: Input text
text = "Natural Language Processing with NLTK is very interesting and powerful."

# Step 2: Tokenization (split text into words)
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Step 3: Counting Tags (POS Tagging)
tags = pos_tag(tokens)
print("\nPart of Speech Tags:")
print(tags)

# Step 4: Bigrams (pairs of consecutive words)
bi = list(bigrams(tokens))
print("\nBigrams:")
print(bi)

# Step 5: Trigrams (three consecutive words)
tri = list(trigrams(tokens))
print("\nTrigrams:")
print(tri)

# Step 6: Remove Stop Words
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
print("\nAfter Removing Stopwords:")
print(filtered_tokens)

# Step 7: Stemming
ps = PorterStemmer()
stemmed_words = [ps.stem(word) for word in filtered_tokens]
print("\nAfter Stemming:")
print(stemmed_words)