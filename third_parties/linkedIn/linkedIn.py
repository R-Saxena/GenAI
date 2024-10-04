import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """
    Scrape information from the the linkedIn profiles,
    Manually Scrape the information from the linkedin profile.

    Third Party api would be used which is called proxy curl"""

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/R-Saxena/c82e24414ca834858c7d0797372e524a/raw/c792e9f13516353e7f1c3ed65bbfdedbe6a479c3/Rishabh-Saxena-LinkedIn-profile.json"
        response = requests.get(linkedin_profile_url, timeout=10)

    else:
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = {"Authorization": f'Bearer {os.getenv("PROXYCURL_API_KEY")}'}

        response = requests.get(
            api_endpoint,
            headers=header_dic,
            params={"url": linkedin_profile_url},
            timeout=10,
        )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    data = response.json()

    return data


if __name__ == "__main__":
    linkedin_profile_url = "https://www.linkedin.com/in/rsaxenaishabh/"
    print(scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url, mock=True))
