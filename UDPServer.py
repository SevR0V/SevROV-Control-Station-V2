import numpy as np
import asyncio
import struct
import time

class UDPServer(asyncio.DatagramProtocol):
    def __init__(self):
        print("Server init")
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
        self.tThrusterPhaseCurrent = [[0.0, 0.0, 0.0],[0.0, 0.0, 0.0],[0.0, 0.0, 0.0],[0.0, 0.0, 0.0],[0.0, 0.0, 0.0],[0.0, 0.0, 0.0]]
        self.tManAngles = [0.0, 0.0, 0.0]
        self.tManPhaseCurrents = [[0.0,0.0],[0.0,0.0],[0.0,0.0]]
        self.tManVoltages = [0.0, 0.0, 0.0]
        self.manTelemetryObtained = False
        self.lastTelemetryTime = 0

    def connection_made(self, transport):
        self.transport = transport
        print("UDP Server started")

    def datagram_received(self, data, addr):
        received = None
        if len(data) == 44:
            #ERRORFLAGS, roll, pitch, yaw, depth, batVoltage, batCharge, batCurrent, rollSP, pitchSP
            received = struct.unpack_from("=Qfffffffff", data)            
            self.manTelemetryObtained = False
        if len(data) == 164:
            # ERRORFLAGS, roll, pitch, yaw, depth, batVoltage, batCharge, batCurrent, rollSP, pitchSP, 
            # mot1PhaseA, mot1PhaseB, mot1PhaseC, mot2PhaseA, mot2PhaseB, mot2PhaseC, mot3PhaseA, mot3PhaseB, mot3PhaseC, 
            # mot4PhaseA, mot4PhaseB, mot4PhaseC, mot5PhaseA, mot5PhaseB, mot5PhaseC, mot6PhaseA, mot6PhaseB, mot6PhaseC,
            # manAngle1, manAngle2, manAngle3, manPhaseA1, manPhaseB1, manPhaseA2, manPhaseB2, manPhaseA3, manPhaseB3, manVoltage1, manVoltage2, manVoltage3
            received = struct.unpack_from("=Qfffffffffffffffffffffffffffffffffffffff", data)
            self.manTelemetryObtained = True
        if received is None:
            print('Hui')
            return
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
        
        if self.manTelemetryObtained:
            for i in range(6):
                for j in range(3):
                    self.tThrusterPhaseCurrent[i][j] = received[10+i*3+j]
            for i in range(3):
                self.tManAngles[i] = received[28+i]
                self.tManPhaseCurrents[i][0] = received[31+i*2+0]
                self.tManPhaseCurrents[i][1] = received[31+i*2+1]
                self.tManVoltages[i] = received[37+i]
        self.lastTelemetryTime = time.time()


    def error_received(self, exc):
        print(f"Error received: {exc}")

    def connection_lost(self, exc):
        print("UDP Server stopped")
        self.transport.close()