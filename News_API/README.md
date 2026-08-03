# News API

A simple Python project that fetches the latest news based on a user-selected category using the NewsData.io API.

## Features

- Fetch Top 10 latest news
- Search news by category
- Display news title
- Display news description
- Display news source
- Display country
- Display publish date
- Handle invalid API keys
- Handle invalid requests
- Handle unexpected errors

## Technologies Used

- Python
- Requests Library
- REST API
- JSON
- NewsData.io API

## Installation

1. Clone the repository

```bash
git clone https://github.com/krishnayadav-aiml/Python-API-Projects.git
```

2. Navigate to the project folder

```bash
cd Python-API-Projects/News_API
```

3. Install the required package

```bash
pip install requests
```

## Usage

Run the program:

```bash
python newsAPI.py
```

Enter a category when prompted.

Example:

```text
enter Category: sports
```

Supported categories include:

- business
- entertainment
- environment
- food
- health
- politics
- science
- sports
- technology
- top
- world

## Example Output

```text
Title: Glasgow passes Commonwealth Games baton to India

Description: The 2026 Commonwealth Games came to an end...

Source: India TV

Country: india

Publish Date: 2026-08-03 01:32:50
```

## Project Structure

```
News_API/
│── newsAPI.py
└── README.md
```

## API Used

- NewsData.io API

## Author

**Krishna Yadav**

GitHub: https://github.com/krishnayadav-aiml
