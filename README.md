# Web Form Automation with OpenAI and Selenium

This project demonstrates how to automate the filling and submission of a web form using OpenAI's GPT-3.5-turbo for generating dummy data and Selenium for web automation. The form in question is hosted on JotForm.

## Features

- **OpenAI Integration**: Uses GPT-3.5-turbo to generate realistic dummy data for form fields.
- **Selenium Automation**: Automates web interactions to fill and submit the form.
- **Error Handling**: Captures screenshots on errors for easier debugging.
- **Environment Variable Management**: Securely manages API keys using `dotenv`.

## Prerequisites

- Python 3.7+
- Google Chrome
- `pip` (Python package manager)

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Adibansari/ENSHRINE-ASSIGNMENT.git
    cd ENSHRINE-ASSIGNMENT
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install required packages**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Setup environment variables**:

    - Create a `.env` file in the project root directory.
    - Add your OpenAI API key to the `.env` file:

        ```env
        OPENAI_API_KEY=your_openai_api_key
        ```

## Usage

1. **Run the script**:

    ```bash
    python app.py
    ```

2. **Customization**:

    - Modify the prompts in `generate_dummy_data` function to suit your needs.
    - Adjust the element locators if the form structure changes.

## Project Structure

web-form-automation
├── README.md

├── app.py 

├── .gitignore 

├── requirements.txt

└── venv/

- `README.md`: This file.
- `app.py`: Main script for form automation.
- `requirements.txt`: List of dependencies.
- `venv/`: Virtual environment directory.

## Error Handling

The script includes basic error handling and debugging features:

- **TimeoutException**: Catches timeouts when elements are not found within the specified time.
- **Screenshots**: Takes screenshots of the page when errors occur to help with debugging.


## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Acknowledgments

- [OpenAI](https://openai.com) for the GPT-3.5-turbo API.
- [Selenium](https://www.selenium.dev/) for web automation tools.
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) for the WebDriver.
- [Dotenv](https://pypi.org/project/python-dotenv/) for managing environment variables.
