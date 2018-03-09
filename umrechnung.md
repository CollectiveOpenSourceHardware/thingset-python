## Umrechnung ThingSet -> CBOR

### ThingSet Byte 1 < 32(dez):
```
cbor_byte1 = (thingset_byte1 & 0x1C) << 3 + (thingset_byte1 & 0x03) + 0x18
```

### ThingSet Byte 1 >= 32(dez) < 64(dez):
```
cbor_byte1 = (thingset_byte1 & 0x18) << 1 + (thingset_byte1 & 0x07) + 0xC0
```