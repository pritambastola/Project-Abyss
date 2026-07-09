"""
Browser Manager

Handles opening websites and web searches.
"""

from __future__ import annotations

import subprocess
import webbrowser
from urllib.parse import quote


class BrowserManager:

    def open_url(self, url: str):

        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        webbrowser.open(url)

        return True

    def search_google(self, query: str):

        url = f"https://www.google.com/search?q={quote(query)}"

        webbrowser.open(url)

        return True

    def search_youtube(self, query: str):

        url = f"https://www.youtube.com/results?search_query={quote(query)}"

        webbrowser.open(url)

        return True

    def open_incognito(self, url: str = ""):

        chrome_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        ]

        if url and not url.startswith(("http://", "https://")):
            url = "https://" + url

        for chrome in chrome_paths:
            try:
                if url:
                    subprocess.Popen([chrome, "--incognito", url])
                else:
                    subprocess.Popen([chrome, "--incognito"])
                return True
            except FileNotFoundError:
                continue

        return False