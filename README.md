
# Bank-Statement-PDF-Expenses-Analyzer

[![Project Status](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

The Bank Statement PDF Analyzer is a Python application designed to help you analyze your bank statements in PDF format and calculate your total expenses based on the data within those statements. This tool is particularly useful for individuals seeking to gain insights into their spending habits or for anyone who wants to efficiently track their financial transactions.

## Table of Contents

- [Bank-Statement-PDF-Expenses-Analyzer](#bank-statement-pdf-expenses-analyzer)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [PDF File Format](#pdf-file-format)
  - [JSON Output](#json-output)
  - [Results](#results)
  - [Author](#author)
  - [License](#license)

## Installation

1. Download or clone the repository to your local machine:

    ```
    git clone https://github.com/yourusername/bank-statement-pdf-analyzer.git
    ```

2. Navigate to the project directory:

    ```
    cd bank-statement-pdf-analyzer
    ```

## Usage

To use the Bank Statement PDF Analyzer, follow these steps:

1. Run the application by providing the name of the PDF file as a command-line argument. For example:

    ```
    python bank_statement_analyzer.py your_statement.pdf
    ```

    Replace `bank_statement_analyzer.py` with the actual script filename and `your_statement.pdf` with the name of the PDF file you want to analyze.

2. The application will extract data from the PDF file, calculate the total expenses, and display the result on the console.

## PDF File Format

The application assumes that the bank statement in the PDF file has a column titled "Amount." If the column name is different in your bank statement, you can adjust the source code in the script to match your PDF format.

## JSON Output

The application generates a JSON file named `output.json` that contains the extracted transaction data. You can find this file in the project directory after running the application.

## Results

Upon completion of the analysis, the application will display the total expenses in PLN (Polish Zloty) format on the console.

## Author

- **Jaroslaw Roszyk**
- Contact: roszyk.jarek@gmail.com
- GitHub: [github.com/jaroslawroszyk](https://github.com/jaroslawroszyk)

## License

This project is available under the MIT License - see the [LICENSE](LICENSE/LICENSE) file for details.
