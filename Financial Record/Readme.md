# Financial Record Serverless Application

## Overview

This application processes financial transaction data by anonymizing sensitive information, performing risk assessments, and securely storing the results using AWS Lambda, API Gateway, and TypeScript.

## Setup

1. Clone the repository.
2. Install dependencies:
    ```bash
    npm install
    ```
3. Configure AWS credentials.
4. Deploy the application:
    ```bash
    serverless deploy
    ```

## Usage

- Send a POST request to the API Gateway endpoint with transaction data.
- The system will validate, anonymize, encrypt, assess risk, and store the transaction data.

## Testing

Run unit tests using:
```bash
npm test
