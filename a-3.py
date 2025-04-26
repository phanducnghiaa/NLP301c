from textblob import TextBlob

input_text = "He is a gret person. He believes in bod"

blob = TextBlob(input_text)
corrected_text = blob.correct()

print(corrected_text)
