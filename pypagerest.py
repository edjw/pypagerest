""" Python wrapper for Page.REST (https://page.rest) by Lakshan Perera.
Page.REST is an HTTP API you can use to extract content from any web page as JSON."""

import requests

def process_urls(pr_token, urls):
    """Takes the urls given and prepares them to be used in other functions."""
    urls_processed = []
    pr_urls = []
    for url in urls:
        urls_processed.append("&url=" + url)

    for url_processed in urls_processed:
        url_index = urls_processed.index(url_processed)
        pr_urls.append("https://page.rest/fetch?token=" + pr_token + urls_processed[url_index])

    return pr_urls

def process_selectors(selectors):
    """Takes the CSS selectors given and prepares them to be appended to urls in other functions."""
    all_selectors = ""
    for selector in selectors:
        all_selectors = all_selectors + "&selector=" + selector
    return all_selectors

def process_headers(headers):
    """Takes the Response Headers given and prepares them to be appended to the request in the Response Headers function."""
    all_headers = ""
    for header in headers:
        all_headers = all_headers + "&header=" + header
    return all_headers

def get_pr_basic(pr_token, urls):
    """Grabs site title, description, logo, favicons, canonical URL, status code, and Twitter handle.
    https://page.rest/#basic"""

    pr_urls = process_urls(pr_token, urls)
    all_responses_basic = ""
    for pr_url in pr_urls:
        response_pr_basic = requests.get(pr_url)
        response_pr_basic = response_pr_basic.text
        all_responses_basic = all_responses_basic + response_pr_basic
    return all_responses_basic

def get_pr_selector(pr_token, urls, selectors):
    """Uses CSS selectors to retrieve content from matching elements. You can use up to 10 selector queries.
    https://page.rest/#selector-queries"""

    pr_urls = process_urls(pr_token, urls)
    all_selectors = process_selectors(selectors)
    all_responses_selector = ""
    for pr_url in pr_urls:
        response_pr_selector = requests.get(pr_url + all_selectors)
        response_pr_selector = response_pr_selector.text
        all_responses_selector = all_responses_selector + response_pr_selector
    return all_responses_selector

def get_pr_prerender(pr_token, urls, selectors):
    """Extracts content from pages that render on client-side using JavaScript.
    https://page.rest/#prerender"""

    pr_urls = process_urls(pr_token, urls)
    all_selectors = process_selectors(selectors)
    all_responses_prerender = ""
    for pr_url in pr_urls:
        response_pr_prerender = requests.get(pr_url + "&prerender=1" + all_selectors)
        response_pr_prerender = response_pr_prerender.text
        all_responses_prerender = all_responses_prerender + response_pr_prerender
    return all_responses_prerender

def get_pr_oembed(pr_token, urls):
    """Gets the oEmbed content for the page as part of the response (only if available).
    https://page.rest/#embed-content"""

    pr_urls = process_urls(pr_token, urls)
    all_responses_oembed = ""
    for pr_url in pr_urls:
        response_pr_oembed = requests.get(pr_url + "&embed=1")
        response_pr_oembed = response_pr_oembed.text
        all_responses_oembed = all_responses_oembed + response_pr_oembed
    return all_responses_oembed

def get_pr_opengraph(pr_token, urls):
    """Gets the OpenGraph content for the page as part of the response (only if available).
    https://page.rest/#open-graph"""

    pr_urls = process_urls(pr_token, urls)
    all_responses_opengraph = ""
    for pr_url in pr_urls:
        response_pr_opengraph = requests.get(pr_url + "&og=1")
        response_pr_opengraph = response_pr_opengraph.text
        all_responses_opengraph = all_responses_opengraph + response_pr_opengraph
    return all_responses_opengraph

def get_pr_responseheaders(pr_token, urls, headers):
    """Gets any HTTP headers defined in the response.
    https://page.rest/#response-headers"""

    pr_urls = process_urls(pr_token, urls)
    all_headers = process_headers(headers)
    all_responses_responseheaders = ""

    for pr_url in pr_urls:
        response_pr_responseheaders = requests.get(pr_url + all_headers)
        response_pr_responseheaders = response_pr_responseheaders.text
        all_responses_responseheaders = all_responses_responseheaders + response_pr_responseheaders
    return all_responses_responseheaders
