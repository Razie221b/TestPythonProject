from playwright.sync_api import sync_playwright, Playwright, Browser, Page


class PlaywrightManager:
    playwright: Playwright = None
    browser: Browser = None
    page: Page = None
