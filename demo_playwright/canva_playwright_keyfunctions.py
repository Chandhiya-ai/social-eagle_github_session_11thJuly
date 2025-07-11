from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
        context = await browser.new_context()
        page = await context.new_page()

        # Step 1: Open Canva
        await page.goto("https://www.canva.com")
        await page.wait_for_timeout(3000)
        print("✅ Opened Canva")

        # Step 2: Click Log in
        await page.click("text=Log in")
        await page.wait_for_timeout(2000)

        # Step 3: Click 'Continue with Google'
        await page.click("button:has-text('Continue with Google')")
        await page.wait_for_timeout(3000)

        # Step 4: Switch to Google login popup
        pages = context.pages
        google_popup = pages[-1]  # the last opened window

        # Step 5: Enter email
        await google_popup.fill("input[type='email']", "your_email@gmail.com")
        await google_popup.click("button:has-text('Next')")
        await google_popup.wait_for_timeout(2000)

        # Step 6: Enter password
        await google_popup.fill("input[type='password']", "your_password")
        await google_popup.click("button:has-text('Next')")
        await google_popup.wait_for_timeout(5000)

        # Step 7: Wait until redirected back to Canva
        await page.wait_for_selector("text=What will you design today?", timeout=20000)
        print("🎉 Logged in via Google")

        # Optional: Screenshot
        await page.screenshot(path="canva_loggedin_google.png")

        await browser.close()

asyncio.run(main())
