# Telegram Message Automation with Telethon

## Description

This Python script utilizes the Telethon library to send predefined messages to a list of Telegram group chats. It's an automated way to disseminate messages at a defined interval.

## Dependencies

- Python 3.x
- Telethon library

## Setup

1. Install Telethon:

    ```bash
    pip install Telethon
    ```

2. Get your `api_id` and `api_hash` from the Telegram Developer website.
> Go to https://my.telegram.org/auth and log in.
> After logging in, click on "API development tools".
> Create a new application or select an existing one to get the api_id and api_hash.
> Remember to keep your api_id and api_hash confidential and never share them with anyone, as they provide access to your Telegram account.

3. Update `group_ids` list with the Telegram group IDs where you want to send the message.

4. Customize `message_to_send` with the message you want to send.

## How to Run

1. Save the script to a file, for example `main.py`.

2. Open a terminal, navigate to the directory containing `main.py`.

3. Run the script:

    ```bash
    python main.py
    ```

## Features

- Automatically sends a predefined message to multiple Telegram groups.
- Provides a counter to keep track of messages sent.
- Skips and prints an error message if unable to send to a particular group.
- Waits for 1800 seconds (30 minutes) before sending the next batch of messages.

## Warning

Use this script responsibly and make sure you are not violating Telegram's terms of service or the rules of the groups you are posting to.
