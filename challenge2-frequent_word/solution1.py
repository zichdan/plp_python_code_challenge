import re
from collections import Counter

def count_words(filename):
    with open(filename, 'r') as file:
        text = file.read()

    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    top_words = word_counts.most_common(10)

    return top_words

def main():
    filename = "test.txt"  # Replace with the name or path of your text file
    top_words = count_words(filename)

    print("Top 10 Most Frequent Words:")
    for word, count in top_words:
        print(f"{word}: {count}")

if __name__ == '__main__':
    main()
