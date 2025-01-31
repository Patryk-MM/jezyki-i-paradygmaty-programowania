import re
from collections import Counter


def count_text_elements(text):
    paragraphs = text.strip().split("\n")
    sentences = re.split(r'[.!?]', text)
    words = re.findall(r'\b\w+\b', text)
    return len(words), len(sentences), len(paragraphs)


def most_common_words(text, stop_words, n=10):
    words = re.findall(r'\b\w+\b', text.lower())
    filtered_words = [word for word in words if word not in stop_words]
    word_counts = Counter(filtered_words)
    return word_counts.most_common(n)


def transform_words_starting_with_a(text):
    words = text.split()
    transformed_words = [word[::-1] if word.lower().startswith('a') else word for word in words]
    return ' '.join(transformed_words)


if __name__ == "__main__":
    text = """
    It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his
breast in an effort to escape the vile wind, slipped quickly
through the glass doors of Victory Mansions, though not
quickly enough to prevent a swirl of gritty dust from entering along with him.
The hallway smelt of boiled cabbage and old rag mats. At
one end of it a coloured poster, too large for indoor display,
had been tacked to the wall. It depicted simply an enormous face, more than a metre wide: the face of a man of
about forty-five, with a heavy black moustache and ruggedly handsome features. Winston made for the stairs. It was
no use trying the lift. Even at the best of times it was seldom working, and at present the electric current was cut
off during daylight hours. It was part of the economy drive
in preparation for Hate Week. The flat was seven flights up,
and Winston, who was thirty-nine and had a varicose ulcer
above his right ankle, went slowly, resting several times on
the way. On each landing, opposite the lift-shaft, the poster
with the enormous face gazed from the wall. It was one of
those pictures which are so contrived that the eyes follow
you about when you move. BIG BROTHER IS WATCHING
YOU, the caption beneath it ran.
    """

    stop_words = {"the", "and", "or", "of", "to", "a", "was", "by", "her", "it", "is", "in"}

    word_count, sentence_count, paragraph_count = count_text_elements(text)
    print(f"Words: {word_count}, Sentences: {sentence_count}, Paragraphs: {paragraph_count}")

    common_words = most_common_words(text, stop_words)
    print("Most common words:", common_words)

    transformed_text = transform_words_starting_with_a(text)
    print("Transformed Text:\n", transformed_text)
