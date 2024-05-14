# How to dockerize your Telegram bot

Clone or fork this repo to use it as a base to create a dockerized Telegram bot, using Python as programming language.

## Structure

- `bot.py`: your bot's codebase
- `Dockerfile`: the file to build the bot image.
- `docker-compose.yml`: used to start the bot.
- `requirements.txt`: used to specify your dependencies.

## How to deploy the bot

1. Clone or fork this repo.
2. Write your bot in `bot.py`.
3. Write an `.env` file with your `TELEGRAM_TOKEN` in it and other env vars.
4. Run `docker-compose up -d` and wait for the build to finish.

That's it. Enjoy your dockerized bot. 🚀

# Configure Bot About

# Configure Bot Description

# Configure Bot Commands

```
start - Start Bot to get list Currency
usd - Get rate of USD/VND 'US DOLLAR'
eur - Get rate of EUR/VND 'EURO'
gbp - Get rate of GBP/VND 'POUND STERLING'
jpy - Get rate of JPY/VND 'YEN'
chf - Get rate of CHF/VND 'SWISS FRANC'
cad - Get rate of CAD/VND 'CANADIAN DOLLAR'
aud - Get rate of AUD/VND 'AUSTRALIAN DOLLAR'
cny - Get rate of CND/VND 'YUAN RENMINBI'
sgd - Get rate of SGD/VND 'SINGAPORE DOLLAR'
nzd - Get rate of NZD/VND

```
