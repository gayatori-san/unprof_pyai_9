## NLP & Text AI

# 📄 Text Analyzer using Natural Language Processing (NLP)

A Python project that demonstrates the fundamentals of **Natural Language Processing (NLP)** by analyzing a text article. The application processes a **500+ word article**, performs text preprocessing, extracts meaningful keywords, and identifies the most frequently occurring words using popular NLP techniques.

This project serves as an introduction to the core concepts behind modern AI applications such as **ChatGPT, Search Engines, Chatbots, Resume Screeners, and Sentiment Analysis**.

---

# 📖 Project Overview

The project follows a complete NLP preprocessing pipeline:

```text
Input Article
      │
      ▼
Tokenization
      │
      ▼
Stopword Removal
      │
      ▼
Stemming
      │
      ▼
Lemmatization
      │
      ▼
Keyword Extraction
      │
      ▼
Word Frequency Analysis
```

---

# ✨ Features

* 📄 Accepts a 500+ word article as input
* 🔤 Tokenizes the text into individual words
* 🚫 Removes common stopwords
* 🌱 Applies stemming to reduce words to their root form
* 🍃 Performs lemmatization for meaningful base words
* 🔑 Extracts important keywords
* 📊 Displays the most frequently occurring words
* 📈 Provides useful statistics about the text

---

# 🛠️ Technologies Used

* **Python 3**
* **NLTK (Natural Language Toolkit)**
* **Collections (Counter)**
* **Regular Expressions (re)**

---

# 📚 Concepts Covered

* Natural Language Processing (NLP)
* Tokenization
* Stopword Removal
* Stemming
* Lemmatization
* Keyword Extraction
* Word Frequency Analysis
* Text Cleaning

---

# 📁 Project Structure

```text
Text-Analyzer/
│
├── article.txt
├── text_analyzer.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/gayatori-san/unprof_pyai_9
```

Move into the project directory:

```bash
cd Text-Analyzer
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install nltk
```

---

# ▶️ Run the Project

```bash
python text_analyzer.py
```

---

# 📊 Project Workflow

### 1️⃣ Read Article

* Load a 500+ word article from a text file or user input.

### 2️⃣ Tokenization

* Split the article into individual words and punctuation tokens.

### 3️⃣ Stopword Removal

* Remove common English words such as:

```text
the
is
are
and
of
to
in
for
with
```

### 4️⃣ Stemming

Convert words into their root form.

Example:

```text
Running  →  Run
Playing  →  Play
Studies  →  Studi
```

### 5️⃣ Lemmatization

Reduce words to meaningful dictionary forms.

Example:

```text
Running  →  Run
Better   →  Good
Children →  Child
```

### 6️⃣ Keyword Extraction

Identify the most significant words remaining after preprocessing.

### 7️⃣ Word Frequency Analysis

Display the most common words in the article.

Example:

```text
python      18
data        15
machine     13
learning    12
model       10
```

---

# 📈 Sample Output

```text
Total Words: 642

Total Tokens: 710

Stopwords Removed: 243

Unique Words: 182

Top 10 Keywords

1. python
2. data
3. machine
4. learning
5. model
6. analysis
7. ai
8. algorithm
9. training
10. prediction
```

---

# 📌 Requirements

```text
nltk
```
