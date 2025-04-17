"""
Television class that mimics basic TV behavior.
"""

class Television:
    # Class constants
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Initializes a Television with default settings."""
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """Toggles the power status of the TV."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Toggles the muted state if the TV is powered on."""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increases the channel number; wraps around if at MAX_CHANNEL."""
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """Decreases the channel number; wraps around if at MIN_CHANNEL."""
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """Increases the volume if below MAX_VOLUME. Unmutes if muted."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decreases the volume if above MIN_VOLUME. Unmutes if muted."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Returns a string representing the current TV state:
        Power status, channel number, and volume.
        If muted, volume shows as 0.
        """
        if self.__muted and self.__status:
            display_volume = 0
        else:
            display_volume = self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {display_volume}"
