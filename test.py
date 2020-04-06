import asyncio
from tesla_api import TeslaApiClient

async def main():
    client = TeslaApiClient('bteslaorder@niconet2k.com', '2CF@wS4xGYdB')

    vehicles = await client.list_vehicles()

    print(vehicles.__len__())

    for v in vehicles:
        print(v.vin)
        await v.controls.flash_lights()
        
    await client.close()

asyncio.run(main())