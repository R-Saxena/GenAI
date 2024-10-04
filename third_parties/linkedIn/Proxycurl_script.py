import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("PROXYCURL_API_KEY")
headers = {"Authorization": "Bearer " + api_key}
api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
params = {
    "linkedin_profile_url": "https://www.linkedin.com/in/rsaxenaishabh/",
    "extra": "include",
    "github_profile_id": "include",
    "facebook_profile_id": "include",
    "twitter_profile_id": "include",
    "personal_contact_number": "include",
    "personal_email": "include",
    "inferred_salary": "include",
    "skills": "include",
    "use_cache": "if-present",
    "fallback_to_cache": "on-error",
}
response = requests.get(api_endpoint, params=params, headers=headers)

with open(
    "linkedInProfile.json", "wb"
) as outf:  # after saving it, use json formatting to make it little easier to read
    outf.write(response.content)
