# pypagerest

A Python wrapper for [Page.REST](https://page.rest)

Page.REST is an HTTP API created by [Lakshan Perera](https://www.laktek.com) that can extract content from any web page as JSON.

This wrapper makes it easier to access Page.REST using Python. It also make it easier to request data about multiple URLs.

## Requirements

You'll need to buy an [access token for Page.REST](https://page.rest/#payment-block). Tokens cost $5 and are valid for 365 days. There's a daily cap of 100,000 requests per token.

## Installation

The package isn't on PyPI yet but you can install pypagerest using `pipev` (for a relatively straightforward virtual environments setup) or alternatively with `pip3`. This will install the live code from Github. This code is not yet stable (though it's getting there!)

```python
pipenv install -e git+https://github.com/edjw/pypagerest#egg=pypagerest
```

```python
pip3 install git+https://github.com/edjw/pypagerest
```

## Using pypagerest

### Setup

You have to set some variables which pypagerest will use to retrieve the data you want.

```python
import pypagerest

# #Insert your Page.rest Access token here
pr_token = "Page.Rest_Access_token"

# Insert urls here inside square brackets in quotes.
# If more than one url then separate with commas.
# Use square brackets even if there's only one url. I'm going to fix this.

urls = ["https://domain.tld"] # One URL

*OR*

urls = ["https://domain.tld", "https://anotherdomain.tld"] # More than one URL

# If you want to extract content using CSS selectors, put the selectors inside square brackets like this
selectors = [".class_one", ".class_two", "#id_one", "#id_two", "h2", "p"]

# If you want to extract HTTP response headers, put the response headers inside square brackets like this
headers = ["X-Frame-Options", "X-XSS-Protection", "Content-Security-Policy"]
```

### pypagerest functions

#### Basic

Grab site title, description, logo, favicons, canonical URL, status code, and Twitter handle as described at <https://page.rest/#basic>

```python
pypagerest.get_pr_basic(pr_token, urls)
```

#### Selector queries

Use CSS selectors to retrieve content from matching elements. You can use up to 10 selector queries as described at <https://page.rest/#selector-queries>

```python
pypagerest.get_pr_selector(pr_token, urls, selectors)
```

#### Pre-render content

Extract content from pages that render on client-side using JavaScript as described at <https://page.rest/#prerender>

```python
pypagerest.get_pr_prerender(pr_token, urls, selectors)
```

#### Embed content

Get the oEmbed content for the page as part of the response (only if available) as described at <https://page.rest/#embed-content>

```python
pypagerest.get_pr_oembed(pr_token, urls)
```

#### Open Graph

Get the OpenGraph content for the page as part of the response (only if available) as described at <https://page.rest/#open-graph>

```python
pypagerest.get_pr_opengraph(pr_token, urls)
```

#### Response headers

Get the OpenGraph content for the page as part of the response (only if available) as described at <https://page.rest/#open-graph>

```python
pypagerest.get_pr_responseheaders(pr_token, urls, headers)
```

<!-- ## Scraping multiple pieces of data

If you want to scrape the CSS selectors and oEmbed/OpenGraph/Response Header content at the same time, then use the `get_pr_selector` function. TODO! -->

## Output

If you request multiple URLs, the output is a Python list of the JSON responses from Page.REST.

 If you request only a single URL, the output is the JSON response from Page.REST not in a list. Let me know if you can think of a more useful way of returning the data for real-world use.

## Notes

I have not tested this on any version of Python except 3.6.

The json module is necessary because the json decoder in requests uses single quote marks `'` around keys which I found confuses json formatting where there are single quote marks in the values, eg. quotes in the titles of webpages. Let me know if you can see a way of removing the json dependency.

## Contributing

I am new to Python and would appreciate any suggestions of how to improve pypagerest. If you want to contribute, please submit a pull request! :-)

1. Fork this repository
1. Create your feature branch `git checkout -b my-new-feature`
1. Commit your changes `git commit -am 'Add some feature'`
1. Push to the branch `git push origin my-new-feature`
1. Create a new Pull Request

## To-Do

* Document how to do one function only on one set of urls, selectors, headers
* Document how to do more than one function on one set of urls, selectors, headers
* Document how to do more than one function on more than one set of urls, selectors, headers
* Document multiple urls with different selectors for each one
* Annotate pypagerest
* Enable oEmbed/OpenGraph/Response header content to be requested in selector function