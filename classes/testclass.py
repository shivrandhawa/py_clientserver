#!/usr/bin/env python3

class Packet(object):
    type = "packet"
    WindowSize = "100"
    data = []
    def __init__(self,PacketType,SeqNum,data,WindowSize,AckNum):
    	self.PacketType = PacketType
    	self.SeqNum = SeqNum
    	self.data = data
    	self.WindowSize = WindowSize
    	self.AckNum = AckNum