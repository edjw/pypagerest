"""Example of how to use pypagerest"""

import pypagerest

pr_token = "$Page.Rest_API_KEY" # Insert your Page.rest API Key here

url = "https://domain.tld" # Insert 
selectors = [".title", ".subtitle"] # To extract content using CSS selectors, put selectors inside quotes inside square brackets separated by commas
headers = ["X-Frame-Options", "X-XSS-Protection", "Content-Security-Policy"] # To extract HTTP response headers, put the response headers inside quotes inside square brackets separated by commas


response = get_pr_basic(pr_token, url)
response = get_pr_selector(pr_token, url, selectors)
response = get_pr_prerender(pr_token, url, selectors)
response = get_pr_oembed(pr_token, url)
response = get_pr_opengraph(pr_token, url)
response = get_pr_responseheaders(pr_token, url, headers)
