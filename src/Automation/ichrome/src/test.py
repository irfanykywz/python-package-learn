from ichrome import AsyncChromeDaemon

import asyncio

async def main():
    async with AsyncChromeDaemon() as cromed:
        async with cromed.connect_tab() as tab:
            # This tab will be created in the given BrowserContext
            await tab.goto('http://httpbin.org/ip', timeout=10)
            # print and watch your IP changed
            print(await tab.html)
            await cromed.run_forever()

asyncio.run(main())