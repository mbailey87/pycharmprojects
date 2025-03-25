import requests, os, datetime
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
demo_company = "Imperial Brands PLC"
STOCK_API = os.environ.get('ALPHA_VANTAGE')
NEWS_API = os.environ.get('NEWS')


#------------------------------- STOCK API -------------------------------
stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': STOCK_API
}
stock_r = requests.get('https://www.alphavantage.co/query', params=stock_params)
stock_r.raise_for_status()
data = stock_r.json()
print(data)

# days_data = list(data.items())
# todays_data = days_data[0][1]
# yesterdays_data = days_data[1][1]
#
# todays_date = days_data[0][0]
# yesterdays_date = days_data[1][0]
#
# open_today = [float(val) for key, val in todays_data.items() if 'open' in key]
# close_yesterday = [float(val) for key, val in yesterdays_data.items() if 'close' in key and "adjusted" not in key]
#
# open_price_today = open_today[0]
# close_price_yesterday = close_yesterday[0]
# percent_change = (open_price_today - close_price_yesterday)/close_price_yesterday*100
#
# print(todays_data)
# print(yesterdays_data)
# print(open_price_today)
# print(close_price_yesterday)
# print(percent_change)
#
# #------------------------------- NEWS API -------------------------------
#
# if percent_change > 2 or percent_change < -2:
#     news_params = {
#         'q': COMPANY_NAME,
#         'from': yesterdays_date,
#         'to': todays_date,
#         'apiKey': NEWS_API
#     }
#
#     news_r = requests.get('https://newsapi.org/v2/everything', params=news_params)
#     news_r.raise_for_status()
#     news_data = news_r.json()['articles']
#     news_list = ''
#     for news in news_data[:3]:
#         title = news['title']
#         description = news['description']
#         url = news['url']
#         news_list += f'Headline: {title}\ndescription: {description}\nurl: {url}\n'
#
#     account_sid = os.environ.get('account_sid')
#     auth_token = os.environ.get('auth_token')
#     client = Client(account_sid, auth_token)
#     twilio_number = 'whatsapp:+14155238886'
#
#     message = client.messages.create(
#         body=f"Percent Change Alert\n{percent_change}\n{news_list}",
#         to="whatsapp:+18016693215",
#         from_=twilio_number
#     )
#     print(news_list)
#     print(message.status)
#     print(message.body)
#
# else:
#     print('no significant change')
#
#
#
# ## STEP 1: Use https://www.alphavantage.co
# # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#
# ## STEP 2: Use https://newsapi.org
# # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
#
# ## STEP 3: Use https://www.twilio.com
# # Send a seperate message with the percentage change and each article's title and description to your phone number.
#
#
# #Optional: Format the SMS message like this:
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """
#
