import ctypes

from exceptions import *

class Krnl:

    def __init__(self, dll: str) -> None:
        """Initializes the Krnl Module and loads the API"""
        try:
            self.API = ctypes.CDLL(dll).KrnlApi()
        except:
            raise InvalidDLLError

    def initialize(self, check=True: bool) -> None:
        """
        initialize(self, check=True: bool) -> None
        Aliases: init, Init, Initialize
        
        check: If False, the API Initialize function will be executed without any checks, if check is True this method will check if the API is already initialized or not.

        returns None
        """
        if check:
            initBool = self.API.IsInitialized()
            if bool(initBool):
                return None
            else:
                self.API.Initialize()
        else:
            self.API.Initialize()
    
    def inject(self, check=True: bool) -> None:
        """
        inject(self, check=True: bool) -> None
        Aliases: Inject

        check: If False, the API will inject into the Roblox client without any checks, if check is True this method will check if the API is already injected or not.

        returns None
        """
        if check:
            injBool = self.API.IsInjected()
            if bool(injBool):
                return None
            else:
                self.API.Inject()
        else:
            self.API.Inject()

    def execute(self, script: str) -> bool:
        """
        execute(self, script: str) -> bool
        Aliases: Execute

        script: String of the script to be executed

        returns Bool (If Script was executed or not)
        """

        byteScript = script.encode('utf-8')

        self.API.Execute.argtypes = [ctypes.c_char_p]
        exe = self.API.Execute(byteScript)

        return bool(exe)

    def framerate(self, fps: int) -> None:
        """
        framerate(self, fps: int) -> None
        Aliases: SFR, SetFrameRate, FrameRate, Framerate, setframerate, SetFramerate, SetframeRate, sfr, frame, Frame

        fps: Integer of how much frames to limit the client to

        returns None
        """

        byteFps = fps.encode('utf-8')

        self.API.SetFrameRate.argtypes = [ctypes.c_int32]
        self.API.SetFrameRate(byteFps)

    def isinjected(self) -> bool:
        """
        isinjected(self) -> bool
        Aliases: IsInjected, isInjected, Isinjected, isinj, IsInj, Isinj, isInj

        returns Bool (If API is injected or not)
        """

        injBool = self.API.IsInjected()

        return bool(injBool)

    def isinitialized(self) -> bool:
        """
        isinitialized(self) -> bool
        Aliases: IsInitialized, isInitialized, Isinitialized, isinit, IsInit, Isinit, isInit

        returns Bool (If API is initialized or not)
        """

        initBool = self.API.IsInitialized()

        return bool(initBool)

    # Aliases
    init, Init, Initialize = initialize()
    Inject = inject()
    Execute = execute()
    SFR, SetFrameRate, FrameRate, Framerate, setframerate, SetFramerate, SetframeRate, sfr, frame, Frame = framerate()
    IsInjected, isInjected, Isinjected, isinj, IsInj, Isinj, isInj = isinjected()
    IsInitialized, isInitialized, Isinitialized, isinit, IsInit, Isinit, isInit = isinitialized()
