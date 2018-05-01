from thingset.cansocket import CANsocket
sock = CANsocket('can0')  # or other interface
emonstring = 'http://192.168.178.26/emoncms/input/post?node=emontx&fulljson='
apikey = 'dc8ae3d6a908d75b370ae83b1733a564'

while(True):
	frame = sock.receive()
	if isinstance(frame.cbor, float):
		#print("device: 0x%x  data id: 0x%x   value: %.2f" % (frame.source, frame.dataobjectID, frame.cbor))
        print("{}&apikey={}".format(emonstring, apikey))