# 🚀 AutomationExercise - Selenium Test Automation

## 📌 Overview

AutomationExercise is a web-based e-commerce platform designed for QA engineers to practice automation testing. This project implements an advanced **Selenium-based test automation framework** in **Python** using **Pytest**. The framework is structured for **modularity, reusability, and scalability**, enabling efficient end-to-end testing.

---

## 🎯 Objective

- Automate **key e-commerce functionalities** to ensure reliability and efficiency.
- Enhance **test coverage** and reduce **manual efforts**.
- Validate the **User Interface (UI)** across devices.
- Ensure **cross-browser compatibility**.
- Generate **detailed reports** with logs and screenshots.

---

## 🛠 Technology Stack

- **Programming Language:** Python
- **Automation Tool:** Selenium WebDriver
- **Testing Framework:** Pytest
- **Design Pattern:** Page Object Model (POM)
- **Configuration Management:** `config.ini`
- **Reporting:** `pytest-html`, Allure Reports
- **Logging & Debugging:** Custom logging, Screenshots on failure

---

## 📂 Project Structure

```
AutomationExercise/
│-- TestCases/          # Contains all test scripts
│-- Locators/           # Stores page locators used in POM
│-- Utilities/          # Includes helper functions (readproperties.py)
│-- Configurations/     # Contains config.ini for environment settings
│-- Reports/            # Stores Allure and HTML reports
```

---

## 🔧 Features

- ✅ **End-to-End Test Automation**
- 🔄 **Reusable & Maintainable POM-based Design**
- 🌍 **Cross-Browser & Mobile-Friendly Testing**
- 📊 **Data-Driven Testing with Configurable Inputs**
- ⚡ **Parallel Test Execution for Efficiency**

---

## 📝 Automated Test Scenarios

### 👤 User Management

- Registration (Valid & Invalid Scenarios)
- Login & Logout
- Account Deletion

### 🛍 Product Management

- Searching & Filtering Products
- Adding/Removing Items from the Cart

### 🛒 Shopping & Checkout

- Cart Operations
- Price Validation
- Order Confirmation

### 📌 Profile & Address Management

- Editing User Profile
- Adding/Updating Addresses

### 📧 Contact Forms & Error Handling

- Testing Contact Us form
- Validating error messages

### 🌎 UI & Cross-Browser Testing

- Checking responsive design
- Testing on Chrome, Firefox, Edge, Safari

---

## 📊 Allure Report Integration

To ensure transparency and detailed insights into test executions, **Allure Reports** has been integrated into this framework. It provides:

### 📸 Allure Report Screenshots

#### **Overview Page**

- Displays total test cases executed.
- Shows a **33.33% pass rate**, indicating failed and passed tests.
- Highlights defects and test trends.

#### **Graphs & Status Analysis**

- Displays the breakdown of **Failed, Broken, Passed, and Skipped** test cases.
- Provides insights into test **severity levels**.
- Shows test **duration trends**.

---

## ⚠️ Challenges & Solutions

| Challenge                 | Solution                           |
| ------------------------- | ---------------------------------- |
| Handling dynamic elements | Implemented **explicit waits**     |
| Managing popups & alerts  | Used **Selenium’s alert handling** |
| Synchronization issues    | Applied **WebDriverWait**          |

---

## 🚀 Future Enhancements

- 🔄 **API Testing** using Postman or REST Assured
- ☁️ **Cloud Testing** with BrowserStack/Selenium Grid
- ⏳ **Performance Testing** for website speed optimization
- 📜 **Custom Logging & HTML Reporting** for logging and debugging
- 📷 **Screenshot Capture on Test Failure** for test failure and pass references

---

## 🏁 Conclusion

This automation framework ensures **high-quality software testing** with maximum efficiency. By leveraging **Selenium, Pytest, and POM**, it improves reliability, reduces manual efforts, and provides **comprehensive test coverage**. This project is a stepping stone for creating robust **CI/CD-ready test automation suites**.

🔥 **Automate Smart, Test Faster!** 🔥
