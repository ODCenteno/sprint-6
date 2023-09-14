# Sprint 6

## Urban Grocers API testing with Pytest

This project consist in develop tests for the Urban 
Grocers' API, that manage a food delivery service including
user's creation, orders, warehouses and delivery ops.

A test checklist was provided to test the kit's creation endpoint.

## Task

1. Create the tests using Pytest
   - endpoint: /api/v1/kits
2. Push the code to GitHub
3. Send the repository to evaluation

### Environment
- MacOS Ventura 13.5.2
- IDE: Pycharm
- PyCharm 2023.1.2 (Community Edition)
  - Build #PC-231.9011.38, built on May 16, 2023
- Python 3.10
- Server: tripleten-services.com

## Run the test
1. Clone this repository
```bash
git clone git@github.com:ODCenteno/sprint-6.git
```
2. Install dependencies
```bash
pip3 install pytest requests
```
3. Turn on the server and paste the host URL in the configuration.py archive
4. Run all tests in terminal
```bash
pytest
```

## Checklist
### Feature: Creating a kit with valid Name Length
__Scenario__: Creating a kit with a valid minimum name length (1 character)
- Given the minimum required characters for a valid name, 
When a user creates a kit, then the response code should be 201.

__Scenario__: Creating a kit with a valid maximum length (51 characters)
- Given the maximum allowed characters for a valid name, when a user creates a kit, then
the response code should be 201.

__Scenario__: Creating a kit using special characters 
- Given the characters allowed for a valid name, when the user entered special characters,
then the response code should be 201.

__Scenario__: Use of spaces is allowed
- Given the characters allowed for a valid name, when the user introduced spaces,
then the response code should be 201.

__Scenario__: Creating a kit with invalid name length (0 characters)
- Given the minimum required characters for a valid name, when a user
creates a kit with a 0 character name, then the response code should be 400.

__Scenario__: Creating a kit with invalid name length (52 characters)
- Given the maximum allowed characters for a valid name, when a user creates a kit with name of 52 characters, 
then the response code should be 400.

__Scenario__: The request params aren't sent
- Given the request format, when the user doesn't send the correct data in the request body, then 
a status code 400 should be returned.

__Scenario__: An incorrect data type is sent in the request
- Given the request format, when a user sent a number instead of string, 
then the response code is 400 and the kit is not created.


