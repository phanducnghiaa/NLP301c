def calculate_jaccard_similarity(text1, text2):
    set_1 = text1.lower().strip().split()
    set_2 = text2.lower().strip().split()

    intersection = set(set_1).intersection(set(set_2))
    print(intersection)
    union = set(set_1).union(set(set_2))
    print(union)

    jaccard_similar = len(intersection) / len(union) 
    return jaccard_similar


text1 = "The quick brown fox jumps over the lazy dog"
text2 = "A quick brown fox jumped over a lazy dog"

# Calculate similarity
similarity = calculate_jaccard_similarity(text1, text2)

# Print result
print(f"Jaccard similarity: {similarity}")