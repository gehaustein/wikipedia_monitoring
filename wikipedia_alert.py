import feedparser
import html2text
import pandas as pd
from datetime import datetime, timedelta
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
from dotenv import load_dotenv

# Set global options
h = html2text.html2text

# Define wikipedia feeds to monitor

link_list = ["URL1", "URL2"]

# Empty data list to append
data_list = []

# Slack app properties and channel id to post 
load_dotenv()

client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))

channel_id = os.getenv("SLACK_CHANNEL_ID")


# Parsing data to dataframe
for link in link_list:
    d = feedparser.parse(link)
    for x in range(len(d.entries)):
        article = d.feed.title
        link = d.entries[x].link
        date = datetime.strptime(d.entries[x].updated, '%Y-%m-%dT%H:%M:%SZ')
        title = d.entries[x].title
        content = h(d.entries[x].summary)
        data_list.append([article, link, date, title])
    
wikipedia_df = pd.DataFrame(data_list, columns=["article","link","date","title"])

# Sending data to Slack
if len(wikipedia_df) >= 1:
    try:
        # Call the conversations.list method using the WebClient
        result = client.chat_postMessage(
            channel=channel_id,
            text=str(wikipedia_df[['link', 'date']])
            # You could also use a blocks[] array to send richer content
            )
        # Print result, which includes information about the message (like TS)
        print(result)
    except SlackApiError as e:
        print(f"Error: {e}")