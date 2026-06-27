from ..backup import *

def formatBackupStr(file):
 def formatHexDump(data, n=16, indent=0):
  def formatLine(i):
   line = bytearray(data[i:i+n])
   hex = ' '.join('%02x' % c for c in line)
   text = ''.join(chr(c) if 0x21 <= c <= 0x7e else '.' for c in line)
   return '%*s%-*s %s\n' % (indent, '', n*3, hex, text)
  return ''.join([formatLine(i) for i in range(0, len(data), n)])
 def formatProp(id, prop):
  resetData = ''
  if prop.resetData and prop.resetData != prop.data:
   resetData = 'reset data:\n' + formatHexDump(prop.resetData, indent=2)
  return ('id=0x%08x, size=0x%04x, attr=0x%02x:\n' % (id, len(prop.data), prop.attr)) + formatHexDump(prop.data, indent=2) + resetData + '\n'
 return ''.join([formatProp(id, prop) for id, prop in BackupFile(file).listProperties()])

def printBackupCommand(file):
 """Prints all properties in a Backup.bin file"""
 print(formatBackupStr(file))
