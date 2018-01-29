
sourcePacket = hex(int('0864'))
destPacket = format(8070, 'x')

seqNumbr = '00000000'
ackNumbr = '00000000'

dataOffset = '51020010'

print(sourcePacket + destPacket + seqNumbr + ackNumbr + dataOffset)