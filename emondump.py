from thingset.cansocket import CANsocket
import json, requests

sock = CANsocket('can0')  # or other interface
emonstring = 'http://192.168.178.26/emoncms/input/post?node='
apikey = 'dc8ae3d6a908d75b370ae83b1733a564'
dataObject = {0x00:{0x4001: 'vBat', 0x4002: 'vLoad', 0x4003: 'vCell1', 0x4004: 'vCell2',
			  0x4005: 'vCell3', 0x4006: 'vCell4', 0x4007: 'vCell5', 0x4008: 'iBat',
			  0x4009: 'tempBat', 0x400A: 'SOC'},
			  0x0A:{0x4001: 'vBat', 0x4002: 'vSolar', 0x4003: 'iBat', 0x4004: 'iLoad',
			  0x4005: 'tempExt', 0x4006: 'tempInt', 0x4007: 'loadEn', 0x4008: 'eInputDay_Wh',
			  0x4009: 'eOutputDay_Wh', 0x400A: 'eInputTotal_Wh', 0x400B: 'eOutputTotal_Wh'}}


while(True):
	frame = sock.receive()
	if isinstance(frame.cbor, float):
		node = 0
		if frame.source == 0x00:
			node = 'BMS'
		if frame.source == 0x0A:
			node = 'MPPT'
		if not node:
			print("Error - unknown source!")
			break
		data = {dataObject[frame.source][frame.dataobjectID]: frame.cbor}
		emonpost = emonstring + node + '&fulljson=' + json.dumps(data) + '&apikey=' + apikey
		#print("device: 0x%x  data id: 0x%x   value: %.2f" % (frame.source, frame.dataobjectID, frame.cbor))
		r = requests.get(emonpost)
		print(r.content)
