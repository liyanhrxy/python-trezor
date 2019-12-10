import logging
from typing import Iterable, Optional
from .protocol import ProtocolBasedTransport, ProtocolV1, Handle
from java.io import IOException
import binascii
LOG = logging.getLogger(__name__)

try:
    from android.nfc import NfcAdapter
    from android.nfc.tech import IsoDep
    from android.nfc import Tag
    from java import cast
except Exception as e:
    LOG.warning("NFC transport is Unavailable: {}".format(e))


class NFCHandle(Handle):
    device = None  # type:  Tag

    def __init__(self) -> None:
        self.device = cast(Tag, NFCHandle.device)
        self.handle = None  # type: Optional[IsoDep]

    def open(self) -> None:
        if self.device is not None:
            self.handle = IsoDep.get(self.device)
            try:
                self.handle.setTimeout(5000)
                self.handle.connect()
            except IOException as e:
                LOG.warning(f"NFC handler open exception {e.getMessage()}")
            """
            test code
            """
            # SELECT_APPLET_CMD = [0x00, 0xA4, 0x04, 0x00, 0x00]  #"00A4040000"
            # response = self.write_chunk_nfc(SELECT_APPLET_CMD)
            # print(response.hex())

    def close(self) -> None:
        if self.handle is not None:
            self.handle.close()
        self.handle = None

    def write_chunk_nfc(self, chunk: bytearray) -> bytes:
        assert self.handle is not None
        response = []
        try:
            chunks = binascii.unhexlify(bytes(chunk).hex())
            response =  bytes(self.handle.transceive(chunks))
        except IOException as e:
            LOG.warning(f"NFC handler write exception {e.getMessage()}")
        return response


class NFCTransport(ProtocolBasedTransport):
    """
    """

    PATH_PREFIX = "nfc"
    ENABLED = True

    def __init__(
            self, device: str, handle: NFCHandle = None) -> None:
        assert handle is not None, "nfc handler can not be None"
        self.device = device
        self.handle = handle
        super().__init__(protocol=ProtocolV1(handle))

    def get_path(self) -> str:
        return self.device

    @classmethod
    def enumerate(cls) -> Iterable["NFCTransport"]:
        return [NFCTransport(cls.PATH_PREFIX, NFCHandle())]