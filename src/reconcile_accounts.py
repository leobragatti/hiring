from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime, date as datetype

from .constants import TransactionStatus


@dataclass
class Transaction:
    date: datetype = field(compare=False)
    department: str
    value: float
    recipient: str
    status: Optional[str] = field(init=False, default=TransactionStatus.MISSING, repr=False, compare=False)

    def __post_init__(self):
        self.date = datetime.strptime(self.date, "%Y-%m-%d").date()

    def to_list(self) -> list[str]:
        return [self.date.strftime("%Y-%m-%d"), self.department, self.value, self.recipient, self.status]


def reconcile_accounts(transactions1: list[list[str]], transactions2: list[list[str]]):
    if not transactions1 or not transactions2:
        return

    result1 = [[]] * len(transactions1)
    result2 = [[]] * len(transactions2)
    for index1, data in enumerate(transactions1):
        converted_transaction = Transaction(*data)
        transaction_found = False
        for index2, data2 in enumerate(transactions2):
            converted_transaction2 = Transaction(*data2)
            checked_transaction = result2[index2]
            if not checked_transaction:
                result2[index2] = converted_transaction2.to_list()
            else:
                if checked_transaction[-1] == TransactionStatus.FOUND:
                    continue

            if converted_transaction == converted_transaction2:
                transaction_found = True
                converted_transaction.status = TransactionStatus.FOUND
                converted_transaction2.status = TransactionStatus.FOUND
                result2[index2] = converted_transaction2.to_list()
                break

        if not transaction_found:
            converted_transaction.status = TransactionStatus.MISSING

        transaction_found = False
        result1[index1] = converted_transaction.to_list()

    return (result1, result2)
