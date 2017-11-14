# pypagerest

A Python wrapper for [Page.REST](https://page.rest)

Page.REST is an HTTP API created by [Lakshan Perera](https://www.laktek.com) that can extract content from any web page as JSON.

<!-- ## Scraping multiple pieces of data

If you want to scrape the CSS selectors and oEmbed/OpenGraph/Response Header content at the same time, then use the `get_pr_selector` function. TODO! -->

If you request multiple URLs, the output is a Python list of the JSON responses from Page.REST. If you request only a single URL, the output is the JSON response from Page.REST not in a list. Let me know if you can think of a more useful way of returning the data for real-world use.

The json module is necessary because the json decoder in requests uses single quote marks `'` around keys which I found confuses json formatting where there are single quote marks in the values, eg. quotes in the titles of webpages. Let me know if you can see a way of removing the json dependency.

## To-Do

* Document how to do one function only on one set of urls, selectors, headers
* Document how to do more than one function on one set of urls, selectors, headers
* Document how to do more than one function on more than one set of urls, selectors, headers
* Document multiple urls with different selectors for each one
* Annotate pypagerest
* Enable oEmbed/OpenGraph/Response header content to be requested in selector function