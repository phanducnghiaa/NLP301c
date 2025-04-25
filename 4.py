from gensim.models import Phrases
from gensim.models.phrases import Phraser

def create_bigrams(texts):
    sentences = []
    for sentence in texts:
        sentences.append(sentence.lower().split())
    
    # Tạo model Phrases
    phrases = Phrases(sentences, min_count=1, threshold=1)
    
    desired_bigrams = []
    for i in sentences:
        bigrams = phrases[i]
        desired_bigrams.append(bigrams)
    
    return desired_bigrams

# Input texts
texts = [
    "The mayor of new york was there",
    "new york mayor was present"
]

# Tạo bigrams
result = create_bigrams(texts)

# In kết quả
print(result)