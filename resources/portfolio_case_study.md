# Enterprise Playwright Python Automation Framework

## Project Overview

Built an enterprise-style QA automation framework using Python, Playwright and Pytest for web UI and REST API automation.

The project focuses on creating reusable, maintainable automation components and integrating automated testing into CI/CD.

## Technologies

* Python
* Playwright
* Pytest
* Requests
* REST API
* JSON
* JSON Schema
* Git
* GitHub
* GitHub Actions

## UI Automation

Implemented automated testing for the SauceDemo application including:

* Login
* Product validation
* Product selection
* Cart operations
* Checkout workflow
* Page Object Model
* Reusable Base Page
* Data-driven testing
* Environment configuration

## API Automation

Implemented REST API automation including:

* GET
* POST
* PUT
* PATCH
* DELETE
* Query parameters
* Custom headers
* Authentication handling
* Reusable API Client
* Session-based requests
* Response assertions
* JSON Schema validation

## CI/CD

Integrated the framework with GitHub Actions.

The pipeline automatically:

1. Checks out the repository
2. Sets up Python
3. Installs dependencies
4. Installs Playwright
5. Executes the Pytest suite
6. Reports the test result

## Framework Structure

The framework separates responsibilities into dedicated components:

* `pages/` — Page Object classes
* `api/` — API automation components
* `tests/` — Test cases
* `config/` — Configuration
* `data/` — Test data
* `schemas/` — JSON schemas
* `utils/` — Reusable utilities
* `.github/` — CI/CD workflows

## Current Result

The framework currently contains 11 automated tests and has been successfully executed through GitHub Actions.

## Current Development

The framework is being continuously expanded with:

* Docker-based execution
* Advanced CI/CD
* Cloud execution
* Database/SQL validation
* AI-assisted test automation

## Objective

The objective of this project is to demonstrate practical SDET capabilities through a complete automation framework rather than isolated tool demonstrations.

## Repository

GitHub:

https://github.com/Prem123e/Enterprise-Playwright-Framework
