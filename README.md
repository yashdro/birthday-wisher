# Birthday Wisher & Monday Motivator

Automated Python scripts that send personalised birthday emails 
and Monday motivational quotes — running 24/7 on GitHub Actions 
with no server required.

## What it does

- Checks a CSV of birthdays daily and sends a personalised 
  email on each person's birthday
- Sends a random motivational quote every Monday morning
- Runs automatically on a schedule via GitHub Actions
- No laptop or server needed — runs entirely in the cloud for free

## Tech stack

Python, pandas, smtplib, datetime, GitHub Actions

## Project structure

birthday-wisher/
├── main.py                          # Core script
├── birthdays.csv                    # Birthday contacts
├── quotes.txt                       # Monday motivation quotes
├── requirements.txt                 # Dependencies
├── letter_templates/                # Email templates
│   ├── letter_1.txt
│   ├── letter_2.txt
│   └── letter_3.txt
└── .github/workflows/
    └── scheduled.yml                # GitHub Actions schedule

## How to use

1. Fork this repository
2. Add your contacts to birthdays.csv
3. Go to Settings → Secrets and variables → Actions
4. Add your Gmail address as MY_EMAIL
5. Add your Gmail app password as MY_PASSWORD
6. Set your schedule in .github/workflows/scheduled.yml
7. GitHub Actions runs it automatically every day

## Note

Gmail requires an App Password, not your regular password.
Get one at myaccount.google.com/apppasswords
