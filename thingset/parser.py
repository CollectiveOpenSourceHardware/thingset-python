from time import time, sleep
from thingset.packet import SingleFrame

class CSVParser(object):
    def __init__(self, file):
        self.csv = open(file, 'r')
        self.header = next(self.csv).split(';')

    def __iter__(self):
        for line in self.csv:
            content = line.split(';')

            data = bytes.fromhex(''.join([self._makehex(b) for b in content[4:]]))
            pkt = SingleFrame(data=data)
            identifier = int(content[2], 16) + (0b11 << 24)
            pkt.parseIdentifier(identifier)
            pkt.timestamp = float(content[0])
            yield pkt

        self.csv.close()
    
    def _makehex(self, string):
        string = string.rstrip()
        if len(string) == 1:
            return '0' + string
        return string

def playback(tracefile, duration=600):
    p = CSVParser(tracefile)
    message = iter(p)
    playbackStart = time()
    while (time() - playbackStart) < duration:
        pkt = next(message)
        timediff = time() - playbackStart
        if pkt.timestamp*0.001 <= timediff:
            printNice(pkt)
        else:
            sleep(pkt.timestamp*0.001)
            printNice(pkt)

def printNice(msg):
    print("[{}] Prio {} from Source {}: DataObjectID: {} -> {:.3f}".format(msg.timestamp, msg.priority, msg.source, msg.dataobjectID,msg.cbor))