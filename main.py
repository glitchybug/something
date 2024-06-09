import asyncio
from playwright.async_api import async_playwright, Page, expect

#app url = "https://conduit.bondaracademy.com
#API = https://conduit-api.bondaracademy.com
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless = False)
        page = await browser.new_page()
        await nav(page)
        print(await page.title())
        for link in await page.locator(".companyCardWrapper__companyName--m8").all():
            print(await link.inner_text())

        #await page.get_by_title("Reincarnated Escort Warrior").first.click()
        #await page.locator(".companyCardWrapper__primaryInformation", has_text="TCS").click()
        #await page.locator(".companyCardWrapper__primaryInformation").first.click()
        await page.pause()
        #await something.click()
        print(await page.title())
#        await expect(page.locator("")).to_have_text("conduit")



async def nav(page:Page):
    await page.goto("https://www.ambitionbox.com/list-of-companies")
    #await page.goto("https://asuracomic.net/", timeout=0)
    #await page.get_by_text("Forms").click()
    #await page.get_by_text("Form Layouts").click()




asyncio.run(main())

