from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as p:
        # 1. Launch browser
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # 2. Go to Canva homepage
        await page.goto("https://www.canva.com")
        print("✅ Navigated to Canva")

        # 3. Wait for heading
        await page.wait_for_selector("text=Design anything", timeout=10)
        heading = await page.text_content("text=Design anything")
        print("📰 Heading:", heading)

        # 4. Screenshot homepage
        await page.screenshot(path="canva_home.png")
        print("📸 Screenshot saved as canva_home.png")

        # 5. Click "Log in" link
        await page.click("text=Log in")
        await page.wait_for_timeout(20)
        print("🔐 Navigated to login page")

        # 6. Go back to home
        await page.go_back()
        await page.wait_for_timeout(10)
        print("↩️ Went back to homepage")

        # 7. Go forward to login page again
        await page.go_forward()
        await page.wait_for_timeout(10)
        print("➡️ Went forward to login")

        # 8. Reload login page
        await page.reload()
        print("🔄 Reloaded page")

        # 9. Close browser
        await browser.close()
        print("✅ Browser closed")

# Standard main function call
if __name__ == "__main__":
    asyncio.run(main())
