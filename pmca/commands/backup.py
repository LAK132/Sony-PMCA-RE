from ..backup import *

def formatBackupPropStr(id, prop):
 def formatHexDump(data, n=16, indent=0):
  def formatLine(i):
   line = bytearray(data[i:i+n])
   hex = ' '.join('%02x' % c for c in line)
   text = ''.join(chr(c) if 0x21 <= c <= 0x7e else '.' for c in line)
   return '%*s%-*s %s\n' % (indent, '', n*3, hex, text)
  return ''.join([formatLine(i) for i in range(0, len(data), n)])
 attrstr = '|'.join([attr.name for attr in BackupPropertyAttr if prop.attr & attr])
 if len(attrstr) != 0:
  attrstr = ' (' + attrstr + ')'
 resetData = ''
 if prop.resetData and prop.resetData != prop.data:
  resetData = 'reset data:\n' + formatHexDump(prop.resetData, indent=2)
 return ('id=0x%08x, size=0x%04x, attr=0x%02x%s:\n' % (id, len(prop.data), prop.attr, attrstr)) + formatHexDump(prop.data, indent=2) + resetData + '\n'

def formatBackupStr(file):
 return ''.join([formatBackupPropStr(id, prop) for id, prop in BackupFile(file).listProperties()])

def printBackupCommand(file):
 """Prints all properties in a Backup.bin file"""
 print(formatBackupStr(file))
