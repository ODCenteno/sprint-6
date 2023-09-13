# Sprint 6

## Urban Grocers API testing with Pytest

This project consist in develop tests for the Urban 
Grocers' API, that manage a food delivery service including
user's creation, orders, warehouses and delivery ops.

A test checklist was provided to test the kit's creation endpoint.

## Task

- Create the tests using Pytest
  - endpoint: /api/v1/kits
- Push the code to GitHub
- Send the repository to evaluation

### Environment
- MacOS Ventura 13.5.2
- IDE: Pycharm
- PyCharm 2023.1.2 (Community Edition)
  - Build #PC-231.9011.38, built on May 16, 2023
  - Runtime version: 17.0.6+10-b829.9 aarch64
- Python 3.10
- Server: tripleten-services.com

## Checklist
### Feature: Creating a kit with valid Name Length
__Scenario__: Creating a kit with a valid minimum name length (1 character)
- Given the minimum required characters for a valid name, 
When a user creates a kit, then the response code should be 201.

__Scenario__: Creating a kit with a valid maximum length (51 characters)
- Given the maximum allowed characters for a valid name, when a user creates a kit, then
the response code should be 201.

__Scenario__: Creating a kit using special characters 
- Given 

__Scenario__: Creating a kit with invalid name length (0 characters)
- Given the minimum required characters for a valid name, when a user
creates a kit with a 0 character name, then the response code should be 400.

__Scenario__: Creating a kit with invalid name length (52 characters)
- Given the maximum allowed characters for a valid name, when a user creates a kit with name of 52 characters, 
then the response code should be 400.


