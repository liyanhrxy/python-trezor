# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class BixinMessageSE(p.MessageType):
    MESSAGE_WIRE_TYPE = 902

    def __init__(
        self,
        inputmessage: bytes = None,
    ) -> None:
        self.inputmessage = inputmessage

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('inputmessage', p.BytesType, 0),  # required
        }
