# wikipedia-alert
## Setup
1. Create an app in Slack with <code>chat:write</code> and <code>channels:read</code> permission. Copy the Bot User OAuth Token and save it to the <code>.env</code> file as <code>SLACK_BOT_TOKEN="INSERT TOKEN HERE"</code>.
2. Choose or create a channel in Slack to post messages to and copy the channel id. Add the created app and save the channel id to the <code>.env</code> file as <code>SLACK_CHANNEL_ID="INSERT TOKEN HERE"</code>.
3. Under the <code># Define wikipedia feeds to monitor</code> section insert the links to the atom feeds of the wikipedia pages to monitor. Modify the <code>link_list</code> to include all the declared variables with the links.

## Automation
Configure a cronjob in a terminal to execute the python script to run the at a specified time. 

See https://crontab.guru/ for more information on how to set times and intervals.
