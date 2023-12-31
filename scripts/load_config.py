import time
from panduza import Client, Core, Platform

ADDR="localhost"
PORT=1883

Core.EnableLogging()

c = Client(url=ADDR, port=PORT)
c.connect()
platforms = c.scan_all_platform_interfaces()

platform_topic = next(iter(platforms.keys()))
print(platform_topic)

plat = Platform(addr=ADDR, port=PORT, topic=platform_topic)


# plat.dtree.content.set({
#     "devices": [
#         {'ref': 'Tenma.72-2710', 'settings': {'usb_serial_short': '00321FCC0454'}}
#     ]
# })

# plat.dtree.content.set({
#     "devices": [
#         {'ref': 'Hanmatek.Hm310t', 'settings': {}}
#     ]
# })

# plat.dtree.content.set({
#     "devices": [
#         {'ref': 'Hanmatek.Hm310t', 'settings': {}},
#         {'ref': 'Tenma.72-2710', 'settings': {'usb_serial_short': '00321FCC0454'}}
#     ]
# })

# plat.dtree.content.set({
#     "devices": [
#         {'ref': 'Hanmatek.Hm310t', 'settings': {}},
#         {'ref': 'Tenma.72-2710', 'settings': {'usb_serial_short': '00321FCC0454'}}
#     ]
# })

# plat.dtree.content.set({
#     "devices": [
#         {'ref': 'Korad.KA3005P', 'settings': {'usb_serial_short': '0034A5A10458'}}
#     ]
# })

# plat.dtree.content.set({
#     "devices": [
#         {'ref': 'Korad.KA3005P', 'settings': {'usb_serial_short': '0034A5A10458'}},
#         {'ref': 'Hanmatek.Hm310t', 'settings': {}},
#         {'ref': 'Tenma.72-2710', 'settings': {'usb_serial_short': '003222D50454'}}          
#     ]
# })

plat.dtree.content.set({
    "devices": [
        {'ref': 'Panduza.FakeWebcam', 'settings': {}}
    ]
})

