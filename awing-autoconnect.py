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
        headless=False, slowMo=50,
        executablePath='C:/Program Files (x86)\Microsoft/Edge/Application/msedge.exe'
    )
    # Create a new page
    page = await browser.newPage()
        
    # Add console log listener
    page.on('console', lambda msg: print(f'PAGE LOG: {msg.text}'))
    
    # Go to the website
    await page.goto('http://186.186.0.1/', ignoreHTTPSErrors=True)
    # Log message indicating navigation completion
    print('Navigated to http://186.186.0.1/')
    await page.waitForNavigation()
    print('Page redirected')
    try:
        # Wait for the first button to load
        await page.waitForSelector('#acceptconnection.accept-connection.wa-button.wa-button-logo', visible=True, timeout=60000)
        print('First button found')
        # Click the first button
        await page.click('#acceptconnection.accept-connection.wa-button.wa-button-logo')
        print('Clicked first button')
    except Exception as e:
        print(f'Error finding or clicking the first button: {e}')
    # Wait for the second webpage to load (there is no second webpage but i'll leave it here for educational purpose i think)
    # await page.waitForNavigation()
    try:
        # Wait for the second button to load (the second button is on the same page as the first one, just different layer)
        await page.waitForSelector('#acceptconnection_BannerOverflow.wa-button.wa-button-maxview.wa-button-maxview-banner', visible=True, timeout=60000)
        print('Second button found')
        # Click the second button
        await page.click('#acceptconnection_BannerOverflow.wa-button.wa-button-maxview.wa-button-maxview-banner')
        print('Clicked second button')
    except Exception as e:
        print(f'Error finding or clicking the second button: {e}')

    # Close the browser
    await browser.close()
    print('Browser closed')
# Run the async function
asyncio.get_event_loop().run_until_complete(main())
