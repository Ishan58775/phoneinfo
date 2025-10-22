import requests

def get_social_media_accounts(username):
    # Instagram API endpoint
    instagram_url = f"https://www.instagram.com/{username}/?__a=1"
    
    # Snapchat API endpoint
    snapchat_url = f"https://find.snapchat.com/accounts/find?query={username}"
    
    # Facebook API endpoint
    facebook_url = f"https://graph.facebook.com/v11.0/{username}"
    
    # Send requests to the respective APIs
    instagram_response = requests.get(instagram_url)
    snapchat_response = requests.get(snapchat_url)
    facebook_response = requests.get(facebook_url)
    
    # Process the responses
    instagram_data = instagram_response.json()
    snapchat_data = snapchat_response.json()
    facebook_data = facebook_response.json()
    
    # Extract relevant information
    instagram_id = instagram_data["graphql"]["user"]["id"]
    snapchat_id = snapchat_data["data"][0]["id"]
    facebook_id = facebook_data["id"]
    
    return {
        "instagram": instagram_id,
        "snapchat": snapchat_id,
        "facebook": facebook_id
    }

# Example usage
username = "example_username"
social_media_accounts = get_social_media_accounts(username)
print(social_media_accounts)
