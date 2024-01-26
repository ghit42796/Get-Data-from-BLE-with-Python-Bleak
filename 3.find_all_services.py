import asyncio
from bleak import BleakScanner, BleakClient

target_device_name = "YOUR_DEVICE_NAME"

async def main():
    # Scan for all available devices
    devices = await BleakScanner.discover()

    for device in devices:
        if device.name == target_device_name:
            print(f"Found target device: {device.name}, {device.address}")
            
            # Connect to the target device
            async with BleakClient(device) as client:
                print(f"Connected: {client.is_connected}")
                
                services = await client.get_services()
                # Print all services and characteristics
                for service in services:
                    print(f"Service: {service.uuid}")
                    for char in service.characteristics:
                        print(f"\tCharacteristic: {char.uuid}")

asyncio.run(main())