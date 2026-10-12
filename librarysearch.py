import string 
 
# Open file safely using 'with' 
with open("C:\\Users\\admin\\Desktop\\book.txt", "r") as file: 
    text = file.read() 
 
# Convert to lowercase 
text = text.lower() 
 
  
 
# Remove punctuation 
for char in string.punctuation: 
    text = text.replace(char, "") 
 
# Split into words 
words = text.split() 
 
# Count word frequency 
word_count = {} 
 
for word in words: 
    if word in word_count: 
        word_count[word] += 1 
    else: 
        word_count[word] = 1 
 
# Sort words by frequency (descending) 
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True) 
 
# Display Top 10 Words 
print("Top 10 Words:") 
for i in range(min(10, len(sorted_words))): 
    print(f"{sorted_words[i][0]} : {sorted_words[i][1]}") 