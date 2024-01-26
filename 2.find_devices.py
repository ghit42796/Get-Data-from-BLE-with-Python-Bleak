import asyncio
from bleak import BleakScanner

target_device_name = "YOUR_DEVICE_NAME"

async def main():
    # Scan for all available devices
    devices = await BleakScanner.discover()

    for device in devices:
        if device.name == target_device_name:
            print(f"Found target device: {device.name}, {device.address}")

asyncio.run(main())