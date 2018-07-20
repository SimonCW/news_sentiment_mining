import os
import random

def main():
    document_path = os.path.join(os.getcwd(), "input", "target_sentences.txt")
    sentence = choose_random_sentence(document_path)


def choose_random_sentence(document):
    lines = open(document).read().splitlines()
    return random.choice(lines)




if __name__ == "__main__":
    main()