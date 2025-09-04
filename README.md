![App Icon](assets/TempMailGenerator.ico)

# Temp Mail Generator

A lightweight **temporary email generator** built with Flask (Python) and a modern frontend. It allows you to quickly generate disposable email addresses, view incoming messages, and refresh your inbox automatically.


## Demo

You can try the live demo here: **[Demo Link](https://jo0x01.github.io/TempMail-Generator)**

---

## Features

- **Generate temporary emails** with one click  
- **Read incoming messages** in a modern inbox interface  
- Automatic inbox refresh every 10 seconds  
- Copy email to clipboard  
- Frontend with animated gradient UI  
- Multiple API key fallback for reliability  

---

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- A [RapidAPI](https://rapidapi.com/) account with access to [Temp Mail 44 API](https://rapidapi.com/calvinloveland335703-0p6BxLYIH8f/api/temp-mail44)

---

## Installation

1. **Clone this repository**

```bash
git clone https://github.com/Jo0X01/temp-mail-generator.git
cd temp-mail-generator
```

2. **Install dependencies**

```bash
pip install flask requests
```

3. **Configure your RapidAPI keys**
   
To Obtain An API just access to [Temp Mail 44 API](https://rapidapi.com/calvinloveland335703-0p6BxLYIH8f/api/temp-mail44)

In the Python code, edit:

```python
RAPID_API_KEYS = [
    "YOUR_API_KEY_1",
    "YOUR_API_KEY_2",
    "YOUR_API_KEY_3"
]
```

---

## Usage

Run the Flask server:

```bash
python main.py
```

The app will automatically open in your browser at:

```
http://127.0.0.1:5555/
```

---

## API Endpoints

### `GET /`
Serves the frontend interface (`assets/index.html`).

### `GET /generate`
Generates a new temporary email.

**Response:**
```json
{
  "email": "example@domain.com",
  "token": "hash_token"
}
```

### `GET /inbox?tk=<token>`
Fetches inbox messages for the generated email.

**Response:**
```json
{
  "messages": [
    {
      "id": "msg123",
      "from": "sender@example.com",
      "subject": "Welcome!",
      "body_text": "Hello World",
      "created_at": "2025-09-04T10:00:00Z"
    }
  ]
}
```

---

## Frontend

- Located in `assets/index.html`
- Features a glassmorphic card design with gradient animations
- Auto-refreshes inbox every 10 seconds
- Supports copy-to-clipboard and keyboard shortcut (`C` key)

---

## Project Structure

```
.
├── main.py        # Flask backend
├── assets/
│   └── index.html # Frontend UI
│   └── TempMailGenerator.ico # App Icon
└── README.md      # This file
```

---

## License

This project is licensed under the MIT License.
