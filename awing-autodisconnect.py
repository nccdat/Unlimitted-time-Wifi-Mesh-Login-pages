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

    # Wait for the exit button to load
    # await page.waitForSelector('#submit.displayRow.alCenter.jfCenter')
    # Click the exit button
    await page.click('#complete > form > div.displayRow.alCenter.jfCenter.mt10 > button')

    # Close the browser
    await browser.close()

# Run the async function
asyncio.get_event_loop().run_until_complete(main())
