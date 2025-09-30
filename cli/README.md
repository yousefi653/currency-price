# Currency & Gold Price CLI

A simple command-line tool to fetch live currency and gold prices.
No need to open websites — just run the command and get the latest rates instantly.

## Installation

1. Clone the repository:
git clone https://github.com/yousefi653/currency-price.git
cd /currency-price

2. Install dependencies:
pip install -r requirements.txt

## Usage

1. Run the program:
python main.py

### Examples:

Get USD price:
price (-s or --symbol) USD

Get EUR price:
price (-s or --symbol) EUR

## Features

1. Fetches live currency exchange rates (USD, EUR, GBP, etc.).
2. Displays gold prices.
3. Simple CLI interface.

## Requirements 

1. requests>=2.32.5
2. click>=8.3.0
3. prettytable>=3.16.0

