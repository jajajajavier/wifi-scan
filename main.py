from os import popen
import re

color = {
  "red":      "\33[31m",
  "green":    "\33[32m",
  "yellow":   "\33[33m",
  "blue":     "\33[34m",
  "magenta":  "\33[35m",
  "cyan":     "\33[36m",
  "white":    "\33[0m"
}

print()

def select_iface():
  iface_list = re.findall("Interface (\S+)\n", popen("iw dev").read())

  if len(iface_list) == 1:
    return iface_list[0]

  print(color['white'] + "Interfaces:")

  for i in range(len(iface_list)):
    print(color['magenta'] + str(i + 1) + ".  " + color['blue'] + iface_list[i])

  selected = int(input(color['green']+"\nSelect a wireless interface " + '[1-' + str(len(iface_list)) + ']' + ": "))

  return iface_list[selected - 1]


def main():
  user = popen("whoami").read().replace('\n', '')
  if user != "root":
    return print(color['red'] + "execute as sudo!")

  iface = select_iface()
  print(color['white']+"Has been selected the wireless interface: " + color['blue'] + iface)

main()
