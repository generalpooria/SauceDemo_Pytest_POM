# Sauce Demo - Pytest E2E Test Automation

This project contains an automated end-to-end (E2E) test for the [Sauce Demo](https://www.saucedemo.com/) website. It is designed as a practice project to demonstrate skills in web automation using Python, Selenium, Pytest, and the Page Object Model (POM) design pattern.

The main test case covers a complete user purchase flow:
1.  Login to the application.
2.  Add a specific item to the shopping cart.
3.  Navigate to the cart and verify the item.
4.  Proceed to checkout and fill in user information.
5.  Verify the order details on the overview page.
6.  Finalize the purchase, confirm the order, and save a screenshot of the completion page (`order_complete.png`).

## Core Concepts & Technologies

This project was created to practice and demonstrate the following concepts:

*   **Selenium WebDriver**: For browser automation and interaction with web elements.
*   **Pytest**: As the testing framework for structuring, running, and asserting test outcomes.
*   **Page Object Model (POM)**: To create a scalable and maintainable test structure by separating UI element selectors and interactions (`pages` directory) from the actual test logic (`tests` directory).
*   **Data-Driven Testing**: Test data (credentials, user info) is externalized into a `test_data.json` file, making tests more flexible and easier to manage.
*   **Pytest Fixtures**: Used for setup and teardown operations, such as initializing the WebDriver and loading test data (`conftest.py`).
*   **HTML Test Reports**: Generating a clear, shareable HTML report of the test results using `pytest-html`.
*   **Screenshots for Evidence**: Automatically taking a screenshot upon successful order completion to provide visual proof.

## Prerequisites

*   Python 3.8+
*   Google Chrome browser
*   ChromeDriver (must match your Chrome browser version)

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/SauceDemo_Pytest_POM.git
    cd SauceDemo_Pytest_POM
    ```

2.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Run the Tests

To run the tests and generate an HTML report, execute the following command in your terminal:

```bash
pytest -v -s --html=report.html
or
python -m pytest -v -s --html=report.html
```

After the test run is complete, you can open `report.html` in your browser to see the detailed results.
