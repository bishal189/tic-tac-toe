# Tic-Tac-Toe GUI

## 📌 Project Overview

This is a simple Tic-Tac-Toe game implemented in Python using a GUI. The game allows two players to take turns marking `X` and `O` on a 3x3 grid.

## 🚀 Features

- Interactive GUI built with Tkinter
- Two-player functionality
- Win detection and game reset
- API key management using `python-dotenv`

## 📦 Installation

### Prerequisites

Ensure you have Python 3 installed.

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/yourusername/tic-tac-toe.git
cd tic-tac-toe
```

### 2️⃣ Create a Virtual Environment (Recommended)

```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

### 4️⃣ Setup Environment Variables

Create a `.env` file in the root directory and add:

```ini
API_KEY=your_dummy_api_key_123
```

## 🏃‍♂️ Running the Game

```sh
python run.py
```

## 🛠 Project Structure

```
├── tic_tac_toe
│   ├── gui.py         # GUI implementation
│   ├── game_logic.py  # Game logic
│   ├── utils.py       # Utility functions
│   ├── __init__.py    # Package initialization
├── .env               # Environment variables
├── requirements.txt   # Python dependencies
├── run.py             # Entry point
└── README.md          # Project documentation
```

## 🧪 Running Tests

```sh
pytest
```

## 🔑 API Key Management

The game reads an API key from `.env`, demonstrating secure environment variable management using `python-dotenv`.

## 🤝 Contributing

Feel free to fork the repo and submit pull requests!

## 📜 License

This project is licensed under the MIT License.
