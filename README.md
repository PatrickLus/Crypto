# Crypto - Secure Remote Communication

## Overview

This project is a secure remote communication system using a symmetric encryption algorithm. It allows encryption and decryption of messages between two remote computers, sends the private key (OTP) and the encrypted message via SMS using Infobip, and saves message details in a SQLite database.

## Features

- **Encryption and Decryption**: Encrypt messages before sending and decrypt received messages upon entering an OTP.
- **SMS Integration**: Sends the OTP and encrypted message via SMS using Infobip.
- **Database Storage**: Saves message details in an SQLite database.
- **User Interface**: Simple web interface for sending and receiving messages.

## Requirements
- Python 3.x
- pip (Python package installer)
- An Infobip account with an API key
- Required Python packages (see `requirements.txt`)

## Setup

### Step 1: Sign Up for Infobip and Obtain API Key
1. Visit [Infobip](https://www.infobip.com/) and sign up for an account.
2. Log in to your Infobip account.
3. Navigate to the API keys section in the Infobip portal.
4. Generate a new API key and note it down.

### Step 2: Clone the Repository
```bash
git clone https://github.com/yourusername/secure_communication.git
cd secure_communication
