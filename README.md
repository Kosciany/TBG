# GIF Text Adder

This repository contains a Python script that adds text to a GIF file. It takes an input GIF file, adds text before GIF content, and saves the modified GIF as an output file.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.4+
- PIL library

### Installing

Clone the repository:

```bash
git clone https://github.com/Kosciany/TBG
```

Navigate to the cloned repository:

```bash
cd TBG
```

Create a virtual environment and activate it (optional):

```bash
python3 -m venv env
source env/bin/activate # On Windows, use `.\env\Scripts\activate`
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the script:

```bash
python add_text_before_gif.py input.gif "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
```

## Results

Script input:

![Example input gif](input.gif)

Script output:

![Example output gif](pbt_input.gif)

## Sources

Gif used for README creation: [Example gif source](https://media1.tenor.com/m/eFPFHSN4rJ8AAAAd/example.gif).

Font used in the script: [Roboto font](https://fonts.google.com/specimen/Roboto/about).
