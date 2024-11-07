#module for holding functions for scraping linkedin profile with TavilyAPI
from dotenv import load_dotenv
import requests
import os
import json

load_dotenv()

#!todos: investigate linkedin jobs search & posts scraping using proxycurl




def scrape_linkedin_profile(url,
                            is_mock=False,
                            static_url="https://gist.githubusercontent.com/desmondbai/2cc73c861fb283d15beb759d16d21baf/raw/8c6009db1936422c5bfa2f717e2ae1eb130970ce/gistfile1.txt"):
    """
    Function for scraping Linkedin profile page provided linkedin url, use static mock file when prompted
    Parameters:
        url <str>: url of linkedin profile to scrape from
        mock <bool>: boolean indicating whether or not to use static (scraped) profile page for testing
        static_url <str>: url of webpage (github gist page) storing scraped linkedin profile in json format
    """
    if is_mock:
        response = requests.get(static_url,
                                timeout=10,)
    else:
        api_key = os.getenv("PROXYCURL_API_KEY")
        headers = {'Authorization': 'Bearer ' + api_key}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        params = {
            'linkedin_profile_url': url,
            'extra': 'include',
            'personal_contact_number': 'include',
            'personal_email': 'include',
            'inferred_salary': 'include',
            'skills': 'include',
            'use_cache': 'if-present',
            'fallback_to_cache': 'on-error',
        }

        response = requests.get(api_endpoint,
                                params=params,
                                headers=headers)
        
    return response.json()
    
if __name__=="__main__":
    print(scrape_linkedin_profile("https://www.linkedin.com/in/eden-marco",is_mock=True))


    



    