if __name__ == '__main__':
    sentence = input("Enter a sentence: ")
    words = map(lambda x:x.lower(), sentence.split())
    counter = dict()
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1

    print()
    print("Word Frequency:")
    for word, count in counter.items():
        print(f"\t{word}: {count}")
    print()
    print(f"Total words: {sum(counter.values())}")
    print(f"Unique words: {len(counter.keys())}")
