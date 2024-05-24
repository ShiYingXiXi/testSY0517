import time

from playwright.sync_api import sync_playwright, expect


def test_playWright():
    playwright = sync_playwright().start()
    # 打开浏览器，headless 默认是True，
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://ceshiren.com")
    page.locator("#search-button").click()
    page.locator("#search-term").fill("web自动化")
    page.keyboard.down("Enter")

    result = page.locator(".list>li:nth-child(1).topic-title>span")
    expect(result).to_contain_text("自动化")

    page.screenshot(path='test1.png')
    time.sleep(10)
    browser.close()
    playwright.stop()
