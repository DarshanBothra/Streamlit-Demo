# Streamlit Demo

This repository provides a simple demonstration of core Streamlit functionalities, including data visualization, user input handling, navigation between multiple pages, and building a basic mortgage calculator application.

---

## 📊 Data Visualization Demo

The file [`dataviz.py`](https://github.com/DarshanBothra/Streamlit-Demo/blob/main/dataviz.py) demonstrates:

- Loading a CSV file ([`movies.csv`](https://github.com/DarshanBothra/Streamlit-Demo/blob/main/movies.csv)) into a Pandas DataFrame.
- Displaying the dataset within the Streamlit app.
- Generating random bar and line charts for visualization.

---

## 🧩 Basic Streamlit Functionality and Page Navigation

- [`main.py`](https://github.com/DarshanBothra/Streamlit-Demo/blob/main/main.py) showcases basic Streamlit operations such as reading inputs, writing outputs, and handling button clicks.
- The [`pages`](https://github.com/DarshanBothra/Streamlit-Demo/tree/main/pages) directory contains:
  - [`1_home.py`](https://github.com/DarshanBothra/Streamlit-Demo/blob/main/pages/1_home.py)
  - [`2_dashboard.py`](https://github.com/DarshanBothra/Streamlit-Demo/blob/main/pages/2_dashboard.py)  
These files demonstrate how to implement multi-page navigation within a Streamlit application.

---

## 🏠 Mortgage Calculator Application

The [`MortgageCalculator`](https://github.com/DarshanBothra/Streamlit-Demo/tree/main/MortgageCalculator) directory features a simple mortgage calculator app. Built using Python 3 and Streamlit, this tool utilizes Streamlit’s UI components to perform mortgage-related calculations in under 5 minutes of setup time.

---

## 🚀 How to Launch the App

1. Clone or download the desired files/directories into your local system.
2. Open a terminal in the respective directory.
3. Run the app using the following command:
   ```bash
   streamlit run <filename>.py
   ```
4. A new browser window will automatically open displaying the app.

### Example: Launching the Mortgage Calculator

1. Copy the [`MortgageCalculator`](https://github.com/DarshanBothra/Streamlit-Demo/tree/main/MortgageCalculator) folder into your `Downloads` directory.
2. Open a terminal in the `Downloads` directory.
3. Run:
   ```bash
   streamlit run MortgageCalculator/main.py
   ```

---

## ⚙️ Prerequisites

Ensure the following are installed on your system:

- **Python 3** – Download from [python.org](https://www.python.org/)
- **Streamlit** – Install using pip:
  ```bash
  pip3 install streamlit
  ```

---

## 🎉 Final Note

Explore, experiment, and have fun with Streamlit!  
**Happy Learning!**
