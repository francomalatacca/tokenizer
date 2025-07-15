# tokenizer

A simple, extensible regex-based tokenizer for Python, designed to split text into meaningful tokens such as words, numbers, abbreviations, currency values, and punctuation.

---

## 🚀 Features

- Detects abbreviations like `U.S.A.`
- Supports words with hyphens (e.g., `state-of-the-art`)
- Handles numbers, percentages (`20%`), and currency (`$5.99`)
- Tokenizes punctuation (`.`, `!`, `...`, etc.)
- Easy to extend with additional rules

---

## 📦 Installation

Install locally from source:

```bash
git clone https://github.com/yourusername/tokenizer.git
cd tokenizer
pip install .
```

For development (with test dependencies):

```bash
pip install -e .[dev]
```

---

## 🔧 Usage

```python
from tokenizer import Tokenizer

t = Tokenizer()
tokens = t.tokenize("The U.S.A. GDP rose by 2.5% to $5.99 trillion.")
print(tokens)
```

**Output:**

```python
['The', 'U.S.A.', 'GDP', 'rose', 'by', '2.5%', 'to', '$5.99', 'trillion', '.']
```

---

## 🧪 Running Tests

This project uses `pytest` for testing.

```bash
# Run all tests
pytest

# Run a specific test
pytest tests/test_tokenizer.py::test_currency_and_percentages -v
```

---

## 📁 Project Structure

```
tokenizer/
├── tokenizer/               # Source package
│   ├── __init__.py
│   └── tokenizer.py         # Tokenizer class
│
├── tests/
│   └── test_tokenizer.py    # Unit tests
│
├── pyproject.toml           # Build configuration
├── README.md                # Project overview (this file)
└── LICENSE                  # MIT License
```

---

## ✅ Development Setup

1. Clone the repo  
   ```bash
   git clone https://github.com/yourusername/tokenizer.git
   cd tokenizer
   ```

2. Create a virtual environment (optional but recommended)  
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies  
   ```bash
   pip install -e .[dev]
   ```

4. Run tests  
   ```bash
   pytest
   ```

---

## 💡 Future Ideas

- Add token classification (e.g., return `("20%", "PERCENTAGE")`)
- Support for other currencies (€, £, ¥)
- Handle contractions (`don't`, `it's`)
- Optional CLI usage:  
  ```bash
  $ tokenize "Hello, world!"
  ['Hello', ',', 'world', '!']
  ```

---

## 📄 License

This project is licensed under the MIT License.
