import praw
from bs4 import BeautifulSoup
import requests

reddit = praw.Reddit()


def fetch_article_content(url):

    # Send an HTTP request to the URL of the article
    response = requests.get(url)

    # Parse the HTML of the webpage
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the h1 element
    h1_element = soup.find("h1")

    # Extract the text from the h1 element
    h1_text = h1_element.text

    # Find all div elements with the itemprop attribute set to "articleBody"
    article_body_elements = soup.find_all("div", itemprop="articleBody")

    # If there are no article body elements, return an empty string
    if not article_body_elements:
        return ""

    # Initialize an empty list to store the text from the p elements
    article_content = []

    # Iterate over the article_body_elements
    for article_body in article_body_elements:
        # Find all p elements with the class "mol-para-with-font"
        para_elements = article_body.find_all("p", class_="mol-para-with-font")

        # Extract the text from the p elements and add it to the article_content list
        # Skip p elements that are greater than or equal to 10000 characters in length
        # This avoids any issues with Reddit's comment limit of 10000 characters
        article_content += [
            element.text for element in para_elements if len(element.text) < 10000
        ]

    # Join the paragraphs with a newline character
    article_content = "\n\n".join(article_content)

    # Return the h1 text in bold, followed by the article content
    return f"***{h1_text}***\n\n{article_content}"


# Set these to your favourite subs
subreddit_names = ["worldnews", "ukpolitics", "news", "politics"]

# Iterate over the subreddit names
for subreddit_name in subreddit_names:
    # Get the subreddit object
    subreddit = reddit.subreddit(subreddit_name)

    # Use the `subreddit.new()` function to get a generator for the newest posts in the subreddit
    # You can change this limit to whatver you'd like
    for post in subreddit.new(limit=100):
        # Check if the post is a Daily Mail article, omit 'hulldailymail.co.uk' links
        # This avoids the bot getting confused over different HTML setups
        if "dailymail.co.uk" in post.url and "hulldailymail.co.uk" not in post.url:
            # Use the `praw.models.Submission.comments` method to get a list of comments for the post
            comments = post.comments
            # Check if the post has any comments
            if len(comments) > 0:
                # Iterate over the comments
                for comment in comments:
                    # Check if the comment is from your bot (so you don't create duplicate comments)
                    if comment.author == "yourusernamehere":
                        break
                else:
                    # If the bot has not already commented on the post, copy the content of the Daily Mail article
                    # and post it as a new comment with the > indentation and the message
                    content = fetch_article_content(post.url)
                    message = f"Please don't give The Mail any clicks, here's the article:\n\n {content}"
                    try:
                        # code to post the comment
                        post.reply(message)
                        # print(message)
                    except praw.exceptions.RedditAPIException as e:
                        # code to handle the exception
                        if e.error_type == "TOO_LONG":
                            # code to handle the TOO_LONG error caused bt Reddit's comment length limit
                            print("Comment is too long, skipping.")
                        else:
                            # code to handle other errors
                            print(f"An error occurred: {e}")
