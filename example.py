"""Example of how to use pypagerest"""

import pypagerest

# Insert your Page.rest API Key here
pr_token = "$Page.Rest_API_KEY"

# Insert urls here in quotes. If more than one url then separate with commas
url = "https://domain.tld"

# To extract content using CSS selectors, put selectors inside quotes inside square brackets separated by commas

selectors = [".class_one", ".class_two", "#id_one", "#id_two", "h2", "p"]

# To extract HTTP response headers, put the response headers inside quotes inside square brackets separated by commas

headers = ["X-Frame-Options", "X-XSS-Protection", "Content-Security-Policy"]


some_variable_1 = pypagerest.get_pr_basic(pr_token, url)
some_variable_2 = pypagerest.get_pr_selector(pr_token, url, selectors)
some_variable_3 = pypagerest.get_pr_prerender(pr_token, url, selectors)
some_variable_4 = pypagerest.get_pr_oembed(pr_token, url)
some_variable_5 = pypagerest.get_pr_opengraph(pr_token, url)
some_variable_6 = pypagerest.get_pr_responseheaders(pr_token, url, headers)
