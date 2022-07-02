from pyrogram import idle, Client, filters
from config import PREFIX
from Eagle import *
import logging
import uvloop
import sys
import importlib
import glob
from pathlib import Path


# PLUGIN LOAD SUPPORT BY @H1M4N5HU0P

def load_plugs(plugname):
    modules = Path(f"Eagle/modules/{plugname}.py")
    myfiles = f"Eagle.modules.{plugname}"
    spec = importlib.util.spec_from_file_location(myfiles, modules)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugname)
    spec.loader.exec_module(load)
    sys.modules["Eagle.modules." + plugname] = load
    print("Eagle Userbot - Successfully Imported " + plugname)

if __name__ == "__main__":
    modules = "Eagle/modules/*.py"
    plugins = glob.glob(modules)
    for myfiles in plugins:
        with open(myfiles) as f:
            module = Path(f.name)
            plugname = module.stem
            load_plugs(plugname.replace(".py", ""))


uvloop.install() # speedup

app.start()
me = app.get_me()
print(f"Your Eagle Userbot is ready to fly... Congratulations {me.id} !!. Type {PREFIX}alive to check If your bot is working... Join @EAGLEUB for future updates...")
idle()
