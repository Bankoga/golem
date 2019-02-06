"""
This module contains environment controls:
http://behave.readthedocs.io/en/latest/api.html#environment-file-functions
The functions handle Selenium WebDriver setup and cleanup.
(Alternatively, fixtures could be used: http://behave.readthedocs.io/en/latest/fixtures.html)
"""

# from selenium import webdriver


# Hooks

# A flexible framework would read the browser, and golem architecture choices from inputs or config data.

def before_scenario(context, scenario):
    if 'web' in context.tags:
        context.browser = webdriver.Firefox()
        context.browser.implicitly_wait(10)


def after_scenario(context, scenario):
    if 'web' in context.tags:
        context.browser.quit()
