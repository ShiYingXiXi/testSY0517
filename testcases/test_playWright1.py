from playwright.async_api import async_playwright

import asyncio


async def test_run(playwright):
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    await context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = await context.new_page()
    await page.goto("https://ceshiren.com")
    # 等待DOMContentLoaded事件，即DOM树构建完成
    await page.wait_for_load_state('domcontentloaded')
    await page.locator("#search-button").click()
    await page.locator("#search-term").fill("Appium")
    await page.keyboard.down("Enter")
    selector = ".results .item:nth-child(1) .topic-title"
    locator = page.locator(selector)
    # 等待元素出现在页面上
    await locator.wait_for(state='visible', timeout=5000)
    await context.tracing.stop(path="sy.zip")
    await browser.close()


# 运行异步函数
async def main():
    async with async_playwright() as playwright:
        await test_run(playwright)


asyncio.get_event_loop().run_until_complete(main())
