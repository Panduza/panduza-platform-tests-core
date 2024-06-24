from panduza import Client, Registers

ADDR="localhost"
PORT=1883

client = Client(url=ADDR, port=PORT)
client.connect()
interfaces = client.scan_all_interfaces()

print("===")
for topic, info in interfaces.items():
    print(topic, " - ", info)


reg_map = Registers(client=client, topic="pza/default/test_map/map")
                                                                     

reg_map.write(0, [42])




