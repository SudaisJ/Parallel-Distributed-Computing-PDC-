import pyopencl as cl

platforms = cl.get_platforms()

print("Available OpenCL Platforms and Devices:\n")

for platform in platforms:
    print("Platform:", platform.name)

    devices = platform.get_devices()
    for device in devices:
        print("  Device Name :", device.name)
        print("  Device Type :", cl.device_type.to_string(device.type))
        print("  Version     :", device.version)
        print("-" * 40)