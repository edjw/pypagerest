""" Python wrapper for Page.REST (https://page.rest) by Lakshan Perera. Page.REST is an HTTP API you can use to extract content from any web page as JSON."""

import requests

def get_pr_basic(pr_token, url):
    """Grabs site’s title, description, logo, favicons, canonical URL, status code, and Twitter handle. https://page.rest/#basic"""

    response_pr_basic = requests.get("https://page.rest/fetch?token=" + pr_token + "&url=" + url)
    response_pr_basic = response_pr_basic.json()
    return response_pr_basic

def get_pr_selector(pr_token, url, selectors):
    """Uses CSS selectors to retrieve content from matching elements. You can use up to 10 selector queries. https://page.rest/#selector-queries"""
    """If no selectors are given then it just behaves like get_pr_basic"""
    
    all_selectors = []
    for selector in selectors:
        all_selectors.append("&selector=" + selector)
    all_selectors = "".join(all_selectors)
    
    response_pr_selector = requests.get("https://page.rest/fetch?token=" + pr_token + "&url=" + url + all_selectors)
    response_pr_selector = response_pr_selector.json()
    return response_pr_selector

def get_pr_prerender(pr_token, url, selectors):
    """Extracts content from pages that render on client-side using JavaScript. https://page.rest/#prerender"""
    """Selectors are optional. If no selectors are given then it just behaves like get_pr_basic"""
    
    all_selectors = []
    for selector in selectors:
        all_selectors.append("&selector=" + selector)
    all_selectors = "".join(all_selectors)

    response_pr_prerender = requests.get("https://page.rest/fetch?token=" + pr_token + "&url=" + url + "&prerender=1" + all_selectors)
    response_pr_prerender = response_pr_prerender.json()
    return response_pr_prerender

def get_pr_oembed(pr_token, url):
    """Gets the oEmbed content for the page as part of the response (only if available). https://page.rest/#embed-content"""

    response_pr_oembed = requests.get("https://page.rest/fetch?token=" + pr_token + "&url=" + url + "&embed=1")
    response_pr_oembed = response_pr_oembed.json()
    return response_pr_oembed

def get_pr_opengraph(pr_token, url):
    """Gets the OpenGraph content for the page as part of the response (only if available). https://page.rest/#open-graph"""
    
    response_pr_opengraph = requests.get("https://page.rest/fetch?token=" + pr_token + "&url=" + url + "&og=1")
    response_pr_opengraph = response_pr_opengraph.json()
    return response_pr_opengraph

def get_pr_responseheaders(pr_token, url, headers): #can be multiple headers
    """Gets any HTTP headers defined in the response. https://page.rest/#response-headers"""

    all_headers = []
    for header in headers:
        all_headers.append("&header=" + header)
    all_headers = "".join(all_headers)

    response_pr_responseheaders = requests.get("https://page.rest/fetch?token=" + pr_token + "&url=" + url + all_headers)
    response_pr_responseheaders = response_pr_responseheaders.json()
    return response_pr_responseheaders