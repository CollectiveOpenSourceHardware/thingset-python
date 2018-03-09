## Send and receive message via ThingSet protocol over CAN

### Create CAN socket
``` shell
sudo modprobe vcan
sudo ip link add vcan0 type vcan
sudo ip link set vcan0 up
```

### Test socket
``` shell
candump -L vcan0
cansend vcan0 012#deadbeef
```

### prepare python env (not needed but advised)
In directory with requirements.txt:

``` shell
virtualenv -p python3 .thingset
source .thingset/bin/activate
pip install -r requirements.txt
```
You can skip the first two commands, then all python packages will be added to your computer's python installation! You can leave the environment simply with
``` shell
deactivate
```

### Usage:
``` shell

```
You should see decoded cbor data

### send dummy data via cansend to test:
``` shell
cansend vcan0 014#8000FA3FF33333
cansend vcan0 014#8000820C16
cansend vcan0 014#8000C48221196AB3
cansend vcan0 014#8080C48221196AB3
```

The output should look like this:
``` shell
Message from ID 20 -> 0: 1.899999976158142
Message from ID 20 -> 0: [12, 22]
Message from ID 20 -> 0: 273.15
Error receiving package from ID 20. Error code: 0x80
```
