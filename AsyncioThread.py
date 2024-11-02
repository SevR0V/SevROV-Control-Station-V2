from UDPServer import UDPServer


from PySide6.QtCore import QThread


import asyncio


class AsyncioThread(QThread):
    def __init__(self, IP, port):
        super().__init__()
        self.loop = asyncio.new_event_loop()
        self.IP = IP
        self.port = port
        self.protocol = None
        self.transport = None
        self.udpServer = UDPServer()

    async def start_udp_server(self):
        self.transport, self.protocol = await self.loop.create_datagram_endpoint(
            lambda: self.udpServer, local_addr=('0.0.0.0', 8888)
        )

    def run(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self.start_udp_server())
        self.loop.run_forever()