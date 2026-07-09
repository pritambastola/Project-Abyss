"""
Browser Commands
"""


def register(registry, browser):

    registry.register(
        "open {value} in incognito",
        browser.open_incognito
    )

    registry.register(
        "open incognito",
        lambda: browser.open_incognito("")
    )

    registry.register(
        "search {value}",
        browser.search_google
    )

    registry.register(
        "youtube {value}",
        browser.search_youtube
    )