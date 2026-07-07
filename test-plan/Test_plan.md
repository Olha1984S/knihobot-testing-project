# Test Plan

## Project Information

| Item             | Description                                         |
|                  |                                                     |
| **Project**      | Knihobot Website Testing                            |
| **Application**  | https://knihobot.cz                                 |
| **Project Type** | Manual Testing Portfolio Project                    |
| **Author**       | Olha Shynkina                                       |
| **Status**       | Completed (Manual Testing) / Automation in Progress |


# Project Overview

This project focuses on testing the publicly accessible **Knihobot** website 
for educational and portfolio purposes.
Testing was performed exclusively through the public user interface without 
access to the application's source code, database, internal APIs, or administrative functionality.
The project demonstrates a complete manual testing process, including planning, 
test design, execution, defect reporting, and documentation. 
It also serves as the foundation for an expanding UI automation framework 
based on Playwright and Python.


# Testing Objectives

The primary objectives of testing were to:
- Verify core website functionality
- Validate user navigation and page transitions
- Verify search and filtering functionality
- Validate user input and public forms
- Identify UI and usability issues
- Detect functional defects
- Prepare automation candidates for future UI testing


# Test Environment

| Item             | Value                                 |
|                  |                                       |
| Website          | https://knihobot.cz                   |
| Browser          | Google Chrome (Latest Stable Version) |
| Operating System | Windows 11                            |
| Device           | Desktop                               |


# Testing Types

The following testing activities were performed:
- Functional Testing
- UI Testing
- Exploratory Testing
- Usability Testing
- Regression Testing
- Positive Testing
- Negative Testing
- Input Validation Testing
- Basic UI Automation (Playwright)


# Scope

## Included

The following functionality was tested:
- Homepage
- Website Navigation
- Authentication
- Search
- Filters & Sorting
- Catalog Navigation
- Product Cards
- Product Detail Page
- Shopping Cart
- Checkout
- Personal Account


## Excluded

The following areas were intentionally excluded because testing 
was performed without official authorization:
- Security Testing
- Penetration Testing
- Performance Testing
- Load Testing
- Database Testing
- Private API Testing
- Payment Processing
- Administrative Functionality

---

# Test Coverage

The project currently includes:
- 177 Manual Test Cases
- Functional testing of all major public user flows
- UI and usability validation
- Exploratory testing sessions
- Structured Bug Reports
- Test Summary Reports
- Test Observations
- Initial Playwright automation


# Automation Scope

Automation is currently under active development.
Implemented technologies:
- Playwright
- Python
- Pytest
- Page Object Model (POM)

Current automated scenarios include:
- Navigation
- Breadcrumb validation
- Basic UI verification

Automation coverage will continue to expand as additional user flows are implemented.


# Entry Criteria

Testing begins when:
- The website is publicly accessible
- Test data is prepared
- Required testing tools are available
- The test environment is stable


# Exit Criteria

Testing is considered complete when:
- All planned test cases have been executed
- Test results have been documented
- Confirmed defects have been reported
- Test Summary Reports have been completed


# Risks

Potential risks include:
- Production website changes during testing
- Limited access to internal functionality
- Dynamic website content
- No access to backend logs or databases
- Inability to perform intrusive testing


# Defect Management

All identified defects are documented using structured Bug Reports.
Each report includes:
- Bug ID
- Title
- Severity
- Priority
- Environment
- Steps to Reproduce
- Expected Result
- Actual Result
- Supporting Evidence


# Deliverables

The project includes the following QA artifacts:
- Test Plan
- Manual Test Cases
- Bug Reports
- Test Summary Reports
- Test Observations
- UI Automation Framework (Work in Progress)


# Conclusion

The manual testing phase has been successfully completed.
The project includes comprehensive QA documentation covering planning, 
execution, defect reporting, and test reporting across the core functionality 
of the Knihobot website.
Automation is being developed incrementally using Playwright and Python 
to extend the project's overall test coverage.
