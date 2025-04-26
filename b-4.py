from transformers import pipeline

# Tạo pipeline tóm tắt
summarizer = pipeline("summarization")

# Nhập tài liệu cần tóm tắt
document = input("Nhập tài liệu: ")

# Tóm tắt tài liệu
summary = summarizer(document, max_length=50, min_length=25, do_sample=False)

# In kết quả
print("Tóm tắt:")
print(summary[0]['summary_text'])
