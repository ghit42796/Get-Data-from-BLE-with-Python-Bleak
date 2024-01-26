import asyncio
from bleak import BleakScanner, BleakClient

target_device_name = "YOUR_DEVICE_NAME"
DEVICE_INFO_SERVICE_UUID = "0000180a-0000-1000-8000-00805f9b34fb"
MANUFACTURER_NAME_CHAR_UUID = "00002a29-0000-1000-8000-00805f9b34fb"
MODEL_NUMBER_CHAR_UUID = "00002a24-0000-1000-8000-00805f9b34fb"

async def main():
    # Scan for all available devices
    devices = await BleakScanner.discover()

    for device in devices:
        if device.name == target_device_name:
            print(f"Found target device: {device.name}, {device.address}")
            
            async with BleakClient(device) as client:
                print(f"Connected: {client.is_connected}")
                
                services = await client.get_services()
                print("Reading device information...")

                for service in services:
                    if service.uuid == DEVICE_INFO_SERVICE_UUID:
                        print(f"Device Information Service: {service.uuid}")
                        for char in service.characteristics:
                            if char.uuid == MANUFACTURER_NAME_CHAR_UUID:
                                manufacturer_name = await client.read_gatt_char(char)
                                print(f"\tManufacturer Name: {manufacturer_name}")
                            elif char.uuid == MODEL_NUMBER_CHAR_UUID:
                                model_number = await client.read_gatt_char(char)
                                print(f"\tModel Number: {model_number}")

asyncio.run(main())