import unittest

from src.reconcile_accounts import reconcile_accounts
from src.constants import TransactionStatus


class TestReconcileAccounts(unittest.TestCase):
    """
    Test cases for reconcile_accounts module
    """

    def setUp(self) -> None:
        self.transactions1 = [
            ["2020-12-04", "Tecnologia", "16.00", "Bitbucket"],
            ["2020-12-04", "Jurídico", "60.00", "LinkSquares"],
            ["2020-12-05", "Tecnologia", "50.00", "AWS"],
        ]
        self.transactions2 = [
            ["2020-12-04", "Tecnologia", "16.00", "Bitbucket"],
            ["2020-12-05", "Tecnologia", "49.99", "AWS"],
            ["2020-12-04", "Jurídico", "60.00", "LinkSquares"],
        ]

        self.checked_transactions1 = [
            ["2020-12-04", "Tecnologia", "16.00", "Bitbucket", TransactionStatus.FOUND],
            ["2020-12-04", "Jurídico", "60.00", "LinkSquares", TransactionStatus.FOUND],
            ["2020-12-05", "Tecnologia", "50.00", "AWS", TransactionStatus.MISSING],
        ]
        self.checked_transactions2 = [
            ["2020-12-04", "Tecnologia", "16.00", "Bitbucket", TransactionStatus.FOUND],
            ["2020-12-05", "Tecnologia", "49.99", "AWS", TransactionStatus.MISSING],
            ["2020-12-04", "Jurídico", "60.00", "LinkSquares", TransactionStatus.FOUND],
        ]
        return super().setUp()

    def test_data_integrity(self):
        with self.assertRaises(TypeError):
            reconcile_accounts("Items", "Items2")
            reconcile_accounts([[]], self.transactions2)

    def test_data_check(self):
        checked_transactions1, checked_transactions2 = reconcile_accounts(self.transactions1, self.transactions2)
        self.assertEqual(checked_transactions1, self.checked_transactions1)
        self.assertEqual(checked_transactions2, self.checked_transactions2)
