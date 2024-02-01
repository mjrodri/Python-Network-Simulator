class Device:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
        self.connections = []

    def connect(self, other_device):
        self.connections.append(other_device)
        other_device.connections.append(self)

def main():
    # Create devices
    pc1 = Device("PC1", "192.168.1.1")
    pc2 = Device("PC2", "192.168.1.2")
    router = Device("Router", "192.168.1.254")

    # Connect devices
    pc1.connect(router)
    pc2.connect(router)

    # Display connections
    print(f"{pc1.name} is connected to:")
    for device in pc1.connections:
        print(f"- {device.name} ({device.ip})")

    print(f"\n{pc2.name} is connected to:")
    for device in pc2.connections:
        print(f"- {device.name} ({device.ip})")

if __name__ == "__main__":
    main()
