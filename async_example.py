import asyncio
from playwright.async_api import async_playwright

urls = [
    "http://whatsmyuseragent.org/",
    "https://whatismyipaddress.com/",
    "https://mylocation.org/"
]

async def scrape(url):
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = await browser_type.launch()
            page = await browser.new_page()
            await page.goto(url)
            page_title = await page.title()
            print(f"With browser {browser_type} on page {page_title}")
            await page.screenshot(path=f"example{str(browser_type)}.png")
            await browser.close()

async def main():
        scrape_tasks = [scrape(url) for url in urls]
        await asyncio.wait(scrape_tasks)

asyncio.run(main())