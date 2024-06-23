#!/usr/bin/env python3

import cgi
import cgitb
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

cgitb.enable()

def set_volume(volume_level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(volume_level / 100.0, None)

form = cgi.FieldStorage()
volume = form.getvalue("volume")

if volume is not None:
    try:
        volume = int(volume)
        set_volume(volume)
        print("Content-Type: text/plain")
        print()
        print("Volume set to {}%".format(volume))
    except ValueError:
        print("Content-Type: text/plain")
        print()
        print("Invalid volume level")
else:
    print("Content-Type: text/plain")
    print()
    print("No volume level provided")
