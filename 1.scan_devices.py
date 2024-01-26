import asyncio
from bleak import BleakScanner, BleakClient

async def main():
    # Scan for all available devices
    devices = await BleakScanner.discover()

    for device in devices:
        print(device)

asyncio.run(main())