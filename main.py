import requests

def check_account_exists(phone_number):
    # Instagram API endpoint
    instagram_url = f"https://www.instagram.com/graphql/query/?query_hash=c76146de99bb02f6415203be841dd25a&variables={{\"username\":\"{phone_number}\"}}"
    
    # Snapchat API endpoint
    snapchat_url = f"https://find.snapchat.com/accounts/find?query={phone_number}"
    
    # Facebook API endpoint
    facebook_url = f"https://graph.facebook.com/v11.0/{phone_number}"
    
    # Send requests to the respective APIs
    instagram_response = requests.get(instagram_url)
    snapchat_response = requests.get(snapchat_url)
    facebook_response = requests.get(facebook_url)
    
    # Process the responses
    instagram_data = instagram_response.json()
    snapchat_data = snapchat_response.json()
    facebook_data = facebook_response.json()
    
    # Check if accounts exist
    instagram_exists = instagram_data["data"]["user"] is not None
    snapchat_exists = len(snapchat_data["data"]) > 0
    facebook_exists = facebook_data["id"] is not None
    
    return {
        "instagram": instagram_exists,
        "snapchat": snapchat_exists,
        "facebook": facebook_exists
    }

def check_phone_number(phone_number):
    account_exists = check_account_exists(phone_number)
    
    if account_exists["instagram"]:
        print(f"Instagram: Account exists for phone number {phone_number}")
    else:
        print(f"Instagram: No account exists for phone number {phone_number}")
    
    if account_exists["snapchat"]:
        print(f"Snapchat: Account exists for phone number {phone_number}")
    else:
        print(f"Snapchat: No account exists for phone number {phone_number}")
    
    if account_exists["facebook"]:
        print(f"Facebook: Account exists for phone number {phone_number}")
    else:
        print(f"Facebook: No account exists for phone number {phone_number}")

# Interactive usage
phone_number = input("Enter a phone number: ")
check_phone_number(phone_number)
