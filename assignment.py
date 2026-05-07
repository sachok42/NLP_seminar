import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from dataset import get_split_data

# Required NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('vader_lexicon')


def analyze_part_1(text):
    """
    PART 1: Manual Heuristics (Human Intuition)
    TASK: Manually define 'good' and 'bad' words and calculate a 1-5 score.
    """
    # TODO: Create two sets of words: pos_words and neg_words

    # TODO: Tokenize the text and lowercase it

    # TODO: Create logic to return a rating from 1-5 (start at neutral 3)
    return 3


def train_part_2(training_data):
    """
    PART 2: Statistical Weighting (The Model Training)
    TASK: Build a dictionary where each word maps to its average rating based on the data.
    """
    word_totals, word_counts = {}, {}

    for text, rating in training_data:
        # TODO: Tokenize the text and lowercase it
        tokens = []

        for word in tokens:
            # TODO: Accumulate the total rating sum for this word
            # TODO: Increment the count of how many times this word has appeared
            pass

    # TODO: Create a dictionary that stores the average (Total / Count) for each word
    word_averages = {}
    return word_averages


def predict_part_2(text, word_averages):
    """
    PART 2: Statistical Weighting (Prediction)
    TASK: Guess the rating of a new review using the word averages from training.
    """
    # TODO: Tokenize the text

    # TODO: Find the average value of all known words in this text
    # Hint: Use sum() and len() of the word scores you find in word_averages
    return 3


def analyze_part_3(text):
    """
    PART 3: NLTK VADER (Professional Library)
    TASK: Use the pre-trained SentimentIntensityAnalyzer to get a compound score.
    """
    # TODO: Initialize the SentimentIntensityAnalyzer()

    # TODO: Get the 'compound' score from polarity_scores

    # TODO: Map the compound score (-1 to 1) to a star rating (1 to 5)
    return 3


def run_comparison():
    """
    The Battle of the Algorithms: Comparison Engine
    """
    train_set, test_set = get_split_data()

    # Part 2 requires a training phase to learn word weights
    model_p2 = train_part_2(train_set)

    print(f"\nNLP Workshop | Instructor: Roman Roginskii")
    print(f"{'Review Snippet':<35}    | {'Act':<3} | {'P1':<3} | {'P2':<3} | {'P3':<3}")
    print("-" * 75)

    p1mistake = 0
    p2mistake = 0
    p3mistake = 0

    for text, actual in test_set:
        p1 = analyze_part_1(text)
        p2 = predict_part_2(text, model_p2)
        p3 = analyze_part_3(text)

        print(f"{text[:33]:<35}... | {actual:<3} | {p1:<3} | {p2:<3} | {p3:<3}")

        # Calculate Error (Absolute difference)
        p1mistake += abs(p1 - actual)
        p2mistake += abs(p2 - actual)
        p3mistake += abs(p3 - actual)

    print("-" * 75)
    print(f"P1 (Manual) Average Error:      {p1mistake / len(test_set):.2f}")
    print(f"P2 (Statistical) Average Error: {p2mistake / len(test_set):.2f}")
    print(f"P3 (VADER) Average Error:       {p3mistake / len(test_set):.2f}")


if __name__ == "__main__":
    run_comparison()