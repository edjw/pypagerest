# pypagerest

A Python wrapper for [Page.REST](https://page.rest)

Page.REST is an HTTP API created by [Lakshan Perera](https://www.laktek.com) that can extract content from any web page as JSON.

## Scraping multiple pieces of data

If you want to scrape the CSS selectors and oEmbed/OpenGraph/Response Header content at the same time, then use the `get_pr_selector` function. TODO! <!-- TODO! -->

## To-Do

* Make it easy to do multiple urls
* Enable oEmbed/OpenGraph/Response header content to be requested in selector function
* Document how to do one function only on one set of urls, selectors, headers
* Document how to do more than one function on one set of urls, selectors, headers
* Document how to do more than one function on more than one set of urls, selectors, headers
* Document multiple urls with different selectors for each one
