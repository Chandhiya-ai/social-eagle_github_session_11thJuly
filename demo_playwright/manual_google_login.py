from playwright.sync_api import sync_playwright

def manual_google_login():
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
    user_data_dir="google_login",
    executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    headless=False

        )
        page = browser.new_page()
        page.goto("https://accounts.google.com", timeout=60000)

        print("🔐 Please complete the Google login manually.")
        print("🕒 You have about 60 seconds. Then close the browser.")
        page.wait_for_timeout(60000)  # wait for 60 seconds for manual login
        browser.close()

if __name__ == "__main__":
    manual_google_login()


