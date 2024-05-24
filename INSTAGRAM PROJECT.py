# Import the necessary modules
#!pip install instaloader
import instaloader
import cv2

# Create an instance of Instaloader class
bot = instaloader.Instaloader()

# Login with username and password
username = "your_username"  # replace with your actual username
password = "your_password"  # replace with your actual password

try:
    bot.login(user=username, passwd=password)
except Exception as e:
    print(f"Login failed: {e}")
    exit()

# Interactive login on terminal (optional, comment out if not needed)
# bot.interactive_login(username)  # Asks for password in the terminal

# Load a profile from an Instagram server
try:
    profile = instaloader.Profile.from_username(bot.context, username)
    print(type(profile))
except Exception as e:
    print(f"Failed to load profile: {e}")
    exit()

# Extract some valuable information from an Instagram profile
print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers: ", profile.followers)
print("Followees: ", profile.followees)
print("Bio: ", profile.biography, profile.external_url)

# Retrieve the usernames of all followers
try:
    followers = [follower.username for follower in profile.get_followers()]
    print("Followers:", followers)
except Exception as e:
    print(f"Failed to get followers: {e}")

# Retrieve the usernames of all followees
try:
    followees = [followee.username for followee in profile.get_followees()]
    print("Followees:", followees)
except Exception as e:
    print(f"Failed to get followees: {e}")

# Downloading Posts from Another Profile
# Replace 'other_username' with the target account's username and it should be public account
target_username = 'other_username'  # replace with the target account's username

try:
    target_profile = instaloader.Profile.from_username(bot.context, target_username)
    posts = target_profile.get_posts()

    for index, post in enumerate(posts, 1):
        bot.download_post(post, target=f"{target_profile.username}_{index}")
except Exception as e:
    print(f"Failed to download posts: {e}")

# Image filtering
try:
    # Import the module
    from instafilter import Instafilter

    # Apply a filter to an image
    model = Instafilter("Lo-fi")  # filter name
    new_image = model("image.jpg")  # image path

    # To save the image, use cv2
    cv2.imwrite("modified_image.jpg", new_image)
except Exception as e:
    print(f"Failed to filter image: {e}")
