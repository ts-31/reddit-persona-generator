import praw
import os
from dotenv import load_dotenv

# Load API credentials from .env
load_dotenv()

# Initialize Reddit instance
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

# Test: fetch latest 5 comments from a public user
def test_reddit_api(username="kojied"):
    try:
        user = reddit.redditor(username)
        print(f"✅ Testing Reddit API for user: u/{username}\n")

        for i, comment in enumerate(user.comments.new(limit=5), 1):
            print(f"Comment #{i}:")
            print(comment.body[:200] + "\n---\n")

        print("✅ API test successful!")

    except Exception as e:
        print("❌ API test failed:", str(e))

# Run the test
if __name__ == "__main__":
    test_reddit_api()
