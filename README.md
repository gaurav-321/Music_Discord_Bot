# 🎶 Music_Discord_Bot

## ✨ Description

Music_Discord_Bot is an advanced Discord bot designed to enhance your music experience. It allows you to play music from YouTube directly in voice channels, manage a song queue, and control playback with ease.

## 🚀 Features

- **Play Music**: Add songs to the queue or start playing immediately.
- **Skip Songs**: Move on to the next track when you're ready.
- **Manage Queue**: Clear the entire queue or list all upcoming songs.
- **Stop Bot**: Disconnect from voice channels and stop playback.

## 🛠️ Installation

To get started with Music_Discord_Bot, follow these steps:

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/gag3301v/Music_Discord_Bot.git
   cd Music_Discord_Bot
   ```

2. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the project root and add your Discord bot token:
   ```
   DISCORD_TOKEN=your_bot_token_here
   ```

## 📦 Usage

Here's how you can use Music_Discord_Bot:

- **Play a Song**:
  ```sh
  /play <YouTube Link>
  ```

- **Skip the Current Song**:
  ```sh
  /skip
  ```

- **Clear the Queue**:
  ```sh
  /emptyqueue
  ```

- **Stop the Bot**:
  ```sh
  /stop
  ```

- **List the Queue**:
  ```sh
  /listqueue
  ```

## 🔧 Configuration

- **Environment Variables**: Ensure you have a `.env` file with your `DISCORD_TOKEN`.

## 🧪 Tests

To run tests, use the following command:
```sh
python -m unittest discover tests/
```

## 📁 Project Structure

```
Music_Discord_Bot/
├── app.py
├── functions.py
├── requirements.txt
└── README.md
```

- **app.py**: Main bot script handling commands and events.
- **functions.py**: Functions for YouTube audio downloads.
- **requirements.txt**: List of dependencies.

## 🙌 Contributing

We welcome contributions from the community! To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push to your forked repository.
5. Open a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

Feel free to reach out if you have any questions or suggestions! 🎶✨