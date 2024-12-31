from flask import Flask, render_template, request, jsonify
import difflib

app = Flask(__name__)

# Tamil Grammar Corrector Class
class TamilGrammarCorrector:
    def __init__(self, correct_sentences):
        self.correct_sentences = correct_sentences

    def suggest_correction(self, sentence):
        closest_match = difflib.get_close_matches(sentence, self.correct_sentences, n=1)
        return closest_match[0] if closest_match else "No suggestion found."

# Spelling Checker Class
class SpellingChecker:
    def __init__(self, correct_words):
        self.correct_words = correct_words

    def suggest_correction(self, word):
        closest_match = difflib.get_close_matches(word, self.correct_words, n=1)
        return closest_match[0] if closest_match else "No suggestion found."

# Function to Load Data from a File
def load_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []

# Load Datasets
correct_sentences = load_file("Correct_sentences.txt")
correct_words = load_file("Tamil_words_old.txt")

# Initialize Correctors
grammar_corrector = TamilGrammarCorrector(correct_sentences)
spelling_checker = SpellingChecker(correct_words)

# Flask Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_grammar', methods=['POST'])
def check_grammar():
    sentence = request.form.get('sentence', '')
    if not sentence:
        return jsonify({"error": "No sentence provided."})
    suggestion = grammar_corrector.suggest_correction(sentence)
    return jsonify({"suggestion": suggestion})

@app.route('/check_spelling', methods=['POST'])
def check_spelling():
    word = request.form.get('word', '')
    if not word:
        return jsonify({"error": "No word provided."})
    suggestion = spelling_checker.suggest_correction(word)
    return jsonify({"suggestion": suggestion})

if __name__ == '__main__':
    app.run(debug=True)
