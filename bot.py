# -*- coding: utf-8 -*-
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from datetime import datetime
from bs4 import BeautifulSoup
from google.oauth2.service_account import Credentials
import requests
import gspread
import logging
import pytz
import os

logging.basicConfig(level=logging.INFO)
VIETNAMESE_TIMEZONE = pytz.timezone('Asia/Ho_Chi_Minh')
BOT_USERNAME = os.environ.get('TELEGRAM_BOT_USERNAME')
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    os.environ.get('GOOGLESHEET_KEY_FILE'),
    scopes=scopes
)
gc_client = gspread.authorize(credentials)
COMMANDS = [
    "/start - Start Bot to get list Currency",
    "/usd - Get rate of USD/VND 'US DOLLAR'",
    "/eur - Get rate of EUR/VND 'EURO'",
    "/gbp - Get rate of GBP/VND 'POUND STERLING'",
    "/jpy - Get rate of JPY/VND 'YEN'",
    "/chf - Get rate of CHF/VND 'SWISS FRANC'",
    "/cad - Get rate of CAD/VND 'CANADIAN DOLLAR'",
    "/aud - Get rate of AUD/VND 'AUSTRALIAN DOLLAR'",
    "/cny - Get rate of CND/VND 'YUAN RENMINBI'",
    "/sgd - Get rate of SGD/VND 'SINGAPORE DOLLAR'",
    "/nzd - Get rate of NZD/VND"
]


# Tools


def current() -> str:
    utc_now = datetime.now(pytz.UTC)
    vietnamese_now = utc_now.astimezone(VIETNAMESE_TIMEZONE)
    return vietnamese_now.strftime("%A, %d %B %Y %H:%M:%S")


def get_rate_usd(url: str = os.environ.get('GOOGLESHEET_URL'), sheet: int = 0) -> int:
    spreadsheet = gc_client.open_by_url(url).get_worksheet(sheet)
    last_row_index = len(spreadsheet.get_all_values())
    return spreadsheet.cell(last_row_index, 2).numeric_value


def get_forex_major(currencyID: int = 1, url: str = "https://m.netdania.com/quotes/forex-majors") -> float:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return float(soup.select_one(f'span#recid-{currencyID}-f10').text.strip())

# Commands


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hi {update.effective_user.first_name}! I am RateResponderBot. Send me a message and I will rate it.')
    await update.message.reply_text("Available commands:\n" + "\n".join(COMMANDS))


async def usd_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Wait a second, response time is usually 5s!')
    rate = get_rate_usd()
    await update.message.reply_text(f'{current()}. Rate of USD/VND is {rate:,.0f} đ.')


async def eur_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Wait a second, response time is usually 5s!')
    usd_vnd = get_rate_usd()
    eur_usd = get_forex_major(1)
    eur_vnd = 1.022 * eur_usd * usd_vnd
    await update.message.reply_text(f'{current()}. Rate of EUR/VND is {eur_vnd:,.0f} đ.')


async def gbp_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Wait a second, response time is usually 5s!')
    usd_vnd = get_rate_usd()
    gbp_usd = get_forex_major(2)
    gbp_vnd = 1.022 * gbp_usd * usd_vnd
    await update.message.reply_text(f'{current()}. Rate of GBP/VND is {gbp_vnd:,.0f} đ.')


async def jpy_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Wait a second, response time is usually 5s!')
    usd_vnd = get_rate_usd()
    usd_jpy = get_forex_major(3)
    jpy_vnd = 1.022 * 1/usd_jpy * usd_vnd
    await update.message.reply_text(f'{current()}. Rate of JPY/VND is {jpy_vnd:,.0f} đ.')


async def chf_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Wait a second, response time is usually 5s!')
    usd_vnd = get_rate_usd()
    usd_chf = get_forex_major(4)
    chf_vnd = 1.022 * 1/usd_chf * usd_vnd
    await update.message.reply_text(f'{current()}. Rate of CHF/VND is {chf_vnd:,.0f} đ.')


async def cad_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Wait a second, response time is usually 5s!')
    usd_vnd = get_rate_usd()
    usd_cad = get_forex_major(5)
    cad_vnd = 1.022 * 1/usd_cad * usd_vnd
    await update.message.reply_text(f'{current()}. Rate of CAD/VND is {cad_vnd:,.0f} đ.')


async def aud_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Wait a second, response time is usually 5s!')
    usd_vnd = get_rate_usd()
    aud_usd = get_forex_major(6)
    aud_vnd = 1.022 * aud_usd * usd_vnd
    await update.message.reply_text(f'{current()}. Rate of AUD/VND is {aud_vnd:,.0f} đ.')


async def cny_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Wait a second, response time is usually 5s!')
    usd_vnd = get_rate_usd()
    usd_cny = get_forex_major(7)
    cny_vnd = 1.022 * 1/usd_cny * usd_vnd
    await update.message.reply_text(f'{current()}. Rate of CNY/VND is {cny_vnd:,.0f} đ.')


async def sgd_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Wait a second, response time is usually 5s!')
    usd_vnd = get_rate_usd()
    usd_sgd = get_forex_major(8)
    sgd_vnd = 1.022 * 1/usd_sgd * usd_vnd
    await update.message.reply_text(f'{current()}. Rate of SGD/VND is {sgd_vnd:,.0f} đ.')


async def nzd_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Wait a second, response time is usually 5s!')
    usd_vnd = get_rate_usd()
    nzd_usd = get_forex_major(9)
    nzd_vnd = 1.022 * nzd_usd * usd_vnd
    await update.message.reply_text(f'{current()}. Rate of NZD/VND is {nzd_vnd:,.0f} đ.')


# Responses


def handle_response(text: str) -> str:
    return "We currently do not support automatic message responses, please use the functions in the menu!"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_type = update.message.chat.type
    text = update.message.text

    logging.info(
        f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME, '').strip()
            response = handle_response(new_text)
    else:
        response = handle_response(text)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.error(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    app = ApplicationBuilder().token(os.environ.get('TELEGRAM_TOKEN')).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("usd", usd_command))
    app.add_handler(CommandHandler("eur", eur_command))
    app.add_handler(CommandHandler("gbp", gbp_command))
    app.add_handler(CommandHandler("jpy", jpy_command))
    app.add_handler(CommandHandler("chf", chf_command))
    app.add_handler(CommandHandler("cad", cad_command))
    app.add_handler(CommandHandler("aud", aud_command))
    app.add_handler(CommandHandler("cny", cny_command))
    app.add_handler(CommandHandler("sgd", sgd_command))
    app.add_handler(CommandHandler("nzd", nzd_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    app.run_polling()
