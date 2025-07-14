import praw
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
)


def fetch_user_data(username, save_to_file=False, max_items=50):
    posts = []
    comments = []

    try:
        user = reddit.redditor(username)

        for comment in user.comments.new(limit=max_items):
            comments.append(comment.body)

        for submission in user.submissions.new(limit=max_items):
            content = f"{submission.title}\n{submission.selftext or ''}"
            posts.append(content.strip())

        if save_to_file:
            os.makedirs("output/raw", exist_ok=True)
            with open(f"output/raw/{username}_posts.txt", "w", encoding="utf-8") as f:
                f.write("\n\n".join(posts))
            with open(
                f"output/raw/{username}_comments.txt", "w", encoding="utf-8"
            ) as f:
                f.write("\n\n".join(comments))

    except Exception as e:
        print(f"❌ Reddit API error: {e}")

    return posts, comments
