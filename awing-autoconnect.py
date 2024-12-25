# Import the puppeteer library
import asyncio
from pyppeteer import launch

## PUPPETEER LESSON #1:
## when specify selector for elements, always put their class behind their selector
## like this button below with the selector #acceptconnection
## you have to .<class> behind the selector too, in this case it's accept-connection.wa-button.wa-button-logo

## The whole thing look like this, for example.
## <button id="acceptconnection" class="accept-connection wa-button wa-button-logo" 
##      onclick="onclickBtnConnect()" style="justify-content: center; 
##          background-color: rgb(80, 184, 72); color: rgb(255, 255, 255);">
##            TIẾP TỤC ĐỂ KẾT NỐI INTERNET
##  </button>

async def main():
    # Launch a browser instance
    browser = await launch(
        headless=False, slowMo=50
    )
    # Create a new page
    page = await browser.newPage()
    # Go to the website
    await page.goto('http://186.186.0.1/', ignoreHTTPSErrors=True)

    # Wait for the first button to load
    await page.waitForSelector('#acceptconnection.accept-connection.wa-button.wa-button-logo')
    # Click the first button
    await page.click('#acceptconnection.accept-connection.wa-button.wa-button-logo')

    # Wait for the second webpage to load (there is no second webpage but i'll leave it here for educational purpose i think)
    # await page.waitForNavigation()

    # Wait for the second button to load (the second button is on the same page as the first one, just different layer)
    await page.waitForSelector('#acceptconnection_BannerOverflow.wa-button.wa-button-maxview.wa-button-maxview-banner')
    # Click the second button
    await page.click('#acceptconnection_BannerOverflow.wa-button.wa-button-maxview.wa-button-maxview-banner')

    # Close the browser
    await browser.close()

# Run the async function
asyncio.get_event_loop().run_until_complete(main())
