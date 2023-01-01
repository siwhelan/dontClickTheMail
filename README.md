# dontClickTheMail 🚫📰🗞️

Are you tired of seeing the Daily Mail polluting your Reddit feeds? This Python script is here to help!

Simply run the script and it will scan the 100 newest posts in the specified subreddits for any Daily Mail articles. If it finds a post with a Daily Mail article and no comments from the bot, it will scrape the article's content and post it as a comment. That way, you and other users can read the article without giving the Daily Mail any clicks or ad revenue.

## Dependencies

This program requires the following Python modules:

    praw
    bs4 (BeautifulSoup)
    requests
    
More on praw here -> [Link](https://praw.readthedocs.io/en/stable/)

More on BeautifulSoup here -> [Link](https://pypi.org/project/beautifulsoup4/)

## Installation

To install these dependencies, run the following command:

    pip install praw bs4 requests
    
## Usage

To use this code, you will need to have a Reddit account and a Reddit API client ID and client secret. You can get these by following the instructions [here](https://praw.readthedocs.io/en/stable/getting_started/authentication.html)

Once you have your client ID and client secret, you will need to replace `yourusernamehere`  with your Reddit username and `client_id` and `client_secret` with your own client ID and client secret.

## Note

This code is for educational purposes only and is not intended for use in an automated fashion. Please use responsibly and in accordance with [Reddit's API rules](https://www.reddit.com/wiki/api/). Do not use it to spam Reddit, or to post comments that violate Reddit's terms of service. The author of this program is not responsible for any consequences that may result from the use of this program.

## Feedback

If you have any feedback, please reach out to simon@swhelan.dev

## Authors

- [@siwhelan](https://github.com/siwhelan)
