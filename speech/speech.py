import platform

if platform.system == "Windows":
    from cytolk import tolk
    tolk.try_sapi(True)
    tolk.load("__compiled__" not in globals())

elif platform.system == "Darwin":
            from . import NSSS
            speaker = NSSS.NSSS ()

elif platform.system == "Linux":
    import speechd
    linux_speaker = speechd.Speaker("Loading...")

if platform.system == "Windows":
    tolk.speak(text, interupt)

elif platform.system == "Linux":
    if interupt:
        linux_speaker.cancel()
        linux_speaker.speak(text)

elif platform.system == "Darwin":
            speaker.set ("rate", 600)
            speaker.speak (text, interupt)
