def calculate_jaccard_similarity(text1, text2):
    # Convert texts to sets of words
    set1 = set(text1.lower().split())
    set2 = set(text2.lower().split())
    
    # Calculate intersection and union
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    
    # Calculate Jaccard similarity
    jaccard_similarity = intersection / union
    return jaccard_similarity

# Input texts
text1 = "The quick brown fox jumps over the lazy dog"
text2 = "A quick brown fox jumped over a lazy dog"

# Calculate similarity
similarity = calculate_jaccard_similarity(text1, text2)

# Print result
print(f"Jaccard similarity: {similarity}")