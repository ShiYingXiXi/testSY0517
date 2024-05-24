import asyncio

from playwright.async_api import async_playwright


async def test_sy():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://www.baidu.com")  # 在异步编程中，可以使用 await 来等待异步操作完成
        await asyncio.sleep(2)  # 等待 2 秒
        await browser.close()


if __name__ == "__main__":
    asyncio.run(test_sy())
