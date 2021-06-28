# Tool Name :- SuperTools
# Author :- S.U. Pathan
# Date :- 28/06/21

import os
import sys
from time import sleep
from modules.logo import *
from modules.system import *

class tool:
  @classmethod
  def install(self):
    while True:
      system=sys()
      os.system("clear")
      logo.ins_tnc()
      inp=input("\033[1;33m Do you want to install SuperTools [Y/n]> \033[00m")
      if inp=="y" or inp=="Y":
        os.system("clear")
        logo.installing()
        if system.sudo is not None:
          #require root permission
          if os.path.exists(system.conf_dir+"/SuperTools"):
            pass
          else:
            os.system(system.sudo+" mkdir "+system.conf_dir+"/SuperTools")
          os.system(system.sudo+" cp -r modules core SuperTools.py "+system.conf_dir+"/SuperTools")
          os.system(system.sudo+" cp -r core/SuperTools "+system.bin)
          os.system(system.sudo+" cp -r core/supertools "+system.bin)
          os.system(system.sudo+" chmod +x "+system.bin+"/SuperTools")
          os.system(system.sudo+" chmod +x "+system.bin+"/supertools")
          os.system("cd .. && "+system.sudo+" rm -rf SuperTools")
          if os.path.exists(system.bin+"/SuperTools") and os.path.exists(system.conf_dir+"/SuperTools"):
            os.system("clear")
            logo.ins_sc()
            tmp=input("\033[1;36m ##> \033[00m")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input("\033[1;36m ##> \033[00m")
            break
        else:
          if os.path.exists(system.conf_dir+"/SuperTools"):
            pass
          else:
            os.system("mkdir "+system.conf_dir+"/SuperTools")
          os.system("cp -r modules core SuperTools.py "+system.conf_dir+"/SuperTools")
          os.system("cp -r core/SuperTools "+system.bin)
          os.system("cp -r core/supertools "+system.bin)
          os.system("chmod +x "+system.bin+"/SuperTools")
          os.system("chmod +x "+system.bin+"/supertools")
          os.system("cd .. && rm -rf SuperTools")
          if os.path.exists(system.bin+"/SuperTools") and os.path.exists(system.conf_dir+"/SuperTools"):
            os.system("clear")
            logo.ins_sc()
            tmp=input("\033[1;36m ##> \033[00m")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input("\033[1;36m ##> \033[00m")
            break
      else:
        break

if __name__=="__main__":
  try:
    tool.install()
  except KeyboardInterrupt:
    os.system("clear")
    logo.exit()
