# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .CardanoTxCertificateType import CardanoTxCertificateType
from .CardanoTxInputType import CardanoTxInputType
from .CardanoTxOutputType import CardanoTxOutputType
from .CardanoTxWithdrawalType import CardanoTxWithdrawalType

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class CardanoSignTx(p.MessageType):
    MESSAGE_WIRE_TYPE = 303

    def __init__(
        self,
        *,
        inputs: List[CardanoTxInputType] = None,
        outputs: List[CardanoTxOutputType] = None,
        certificates: List[CardanoTxCertificateType] = None,
        withdrawals: List[CardanoTxWithdrawalType] = None,
        protocol_magic: int = None,
        fee: int = None,
        ttl: int = None,
        network_id: int = None,
        metadata: bytes = None,
    ) -> None:
        self.inputs = inputs if inputs is not None else []
        self.outputs = outputs if outputs is not None else []
        self.certificates = certificates if certificates is not None else []
        self.withdrawals = withdrawals if withdrawals is not None else []
        self.protocol_magic = protocol_magic
        self.fee = fee
        self.ttl = ttl
        self.network_id = network_id
        self.metadata = metadata

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('inputs', CardanoTxInputType, p.FLAG_REPEATED),
            2: ('outputs', CardanoTxOutputType, p.FLAG_REPEATED),
            5: ('protocol_magic', p.UVarintType, None),
            6: ('fee', p.UVarintType, None),
            7: ('ttl', p.UVarintType, None),
            8: ('network_id', p.UVarintType, None),
            9: ('certificates', CardanoTxCertificateType, p.FLAG_REPEATED),
            10: ('withdrawals', CardanoTxWithdrawalType, p.FLAG_REPEATED),
            11: ('metadata', p.BytesType, None),
        }
