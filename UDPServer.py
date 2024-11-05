import numpy as np
import asyncio
import struct
import time

class UDPServer(asyncio.DatagramProtocol):
    def __init__(self):
        print("sercer init")
        self.tErrorsFlags = np.uint64(0)
        self.tRoll = 0.0
        self.tPitch = 0.0
        self.tYaw = 0.0
        self.tDepth = 0.0
        self.tCharge = 0.0
        self.tVolts = 0.0
        self.tAmps = 0.0
        self.tRollSP = 0.0
        self.tPitchSP = 0.0
        self.lastTelemetryTime = 0

    def connection_made(self, transport):
        self.transport = transport
        print("UDP Server started")

    def datagram_received(self, data, addr):
        #ERRORFLAGS, roll, pitch, yaw, depth, batVoltage, batCharge, batCurrent, rollSP, pitchSP
        received = struct.unpack_from("=Qfffffffff", data)
        self.tErrorsFlags = np.uint64(received[0])
        self.tRoll = received[1]
        self.tPitch = received[2]
        self.tYaw = received[3]
        self.tDepth = received[4]
        self.tVolts = received[5]
        self.tCharge = received[6]
        self.tAmps = received[7]
        self.tRollSP = float(received[8])
        self.tPitchSP = float(received[9])
        self.lastTelemetryTime = time.time()


    def error_received(self, exc):
        print(f"Error received: {exc}")

    def connection_lost(self, exc):
        print("UDP Server stopped")
        self.transport.close()