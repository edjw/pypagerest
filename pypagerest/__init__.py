""" Python wrapper for Page.REST (https://page.rest) by Lakshan Perera.
Page.REST is an HTTP API you can use to extract content from any web page as JSON."""
# -*- coding: utf-8 -*
from json import dumps
from concurrent.futures import ThreadPoolExecutor
from requests import Session

pr_parameters = {
    'url': None,
    'token': None,
    'selector': None,
    'prerender': None,
    'embed': None,
    'og': None,
    'header': None
}

def get_webpages(urls):
    """Asynchronously gets the data from the webpages"""
    with Session() as s:
        pr_parameters['url'] = urls
        r = s.get('https://page.rest/fetch', params=pr_parameters)
        return r

def do_requests(pr_token, urls):
    """Starts the scraping and processes the responses"""
    all_responses = []
    pr_parameters['token'] = pr_token

    with ThreadPoolExecutor(max_workers=4) as ex:
        for r in ex.map(get_webpages, urls):
            r = r.json()
            r = dumps(r)
            all_responses.append(r)

    if len(all_responses) == 1:
        return all_responses[0]
    return all_responses

def get_pr_basic(pr_token, urls):
    """Grabs site title, description, logo, favicons, canonical URL,
    status code, and Twitter handle.
    https://page.rest/#basic"""
    return do_requests(pr_token, urls)

def get_pr_selector(pr_token, urls, selectors):
    """Uses CSS selectors to retrieve content from matching elements.
    You can use up to 10 selector queries.
    https://page.rest/#selector-queries"""

    pr_parameters['selector'] = selectors
    return do_requests(pr_token, urls)

def get_pr_prerender(pr_token, urls, selectors):
    """Extracts content from pages that render on client-side using JavaScript.
    https://page.rest/#prerender"""

    pr_parameters['selector'] = selectors
    pr_parameters['prerender'] = 1
    return do_requests(pr_token, urls)

def get_pr_oembed(pr_token, urls):
    """Gets the oEmbed content for the page as part of the response (only if available).
    https://page.rest/#embed-content"""

    pr_parameters['embed'] = 1
    return do_requests(pr_token, urls)

def get_pr_opengraph(pr_token, urls):
    """Gets the OpenGraph content for the page as part of the response (only if available).
    https://page.rest/#open-graph"""

    pr_parameters['embed'] = 1
    return do_requests(pr_token, urls)

def get_pr_responseheaders(pr_token, urls, headers):
    """Gets any HTTP headers defined in the response.
    https://page.rest/#response-headers"""

    pr_parameters['header'] = headers
    return do_requests(pr_token, urls)
