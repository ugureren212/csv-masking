import unittest

from challenge import (
    calc_billing_stat,
    mask_numeric,
    report_stat,
    calc_name_stats,
    mask_email_and_name,
    mask_numeric,
)

testCSV = {
    "1": [
        {
            "ID": "1",
            "Name": "John Smith",
            "Email": "john@mail.com",
            "Billing": "15000",
            "Location": "New York",
        }
    ],
    "2": [
        {
            "ID": "2",
            "Name": "Kelly Lawrence Gomez",
            "Email": "Kelly@your-mail.com",
            "Billing": "20000",
            "Location": "Washington",
        }
    ],
    "3": [
        {
            "ID": "3",
            "Name": "Carl Winslow",
            "Email": "carl-wins@mail-bot.com",
            "Billing": "40000",
            "Location": "Seattle",
        }
    ],
    "4": [
        {
            "ID": "4",
            "Name": "Carl Winslow",
            "Email": "carl-wins@mail-bot.com",
            "Billing": "20000",
            "Location": "Seattle",
        }
    ],
}

testCSV2 = {
    "1": [
        {
            "ID": "1",
            "Name": "John Smith",
            "Email": "john@mail.com",
            "Billing": "15000",
            "Location": "New York",
        }
    ],
    "2": [
        {
            "ID": "2",
            "Name": "Kelly Lawrence Gomez",
            "Email": "Kelly@your-mail.com",
            "Billing": "20000",
            "Location": "Washington",
        }
    ],
    "3": [
        {
            "ID": "3",
            "Name": "Carl Winslow",
            "Email": "carl-wins@mail-bot.com",
            "Billing": "40000",
            "Location": "Seattle",
        }
    ],
    "4": [
        {
            "ID": "4",
            "Name": "Carl Winslow",
            "Email": "carl-wins@mail-bot.com",
            "Billing": "20000",
            "Location": "Seattle",
        }
    ],
}

maskedCSV = {
    "1": [
        {
            "Email": "XXXX@XXXX.XXX",
            "Location": "New York",
            "ID": "1",
            "Billing": "15000",
            "Name": "XXXXXXXXXX",
        }
    ],
    "2": [
        {
            "Email": "XXXXX@XXXXXXXXX.XXX",
            "Location": "Washington",
            "ID": "2",
            "Billing": "20000",
            "Name": "XXXXXXXXXXXXXXXXXXXX",
        }
    ],
    "3": [
        {
            "Email": "XXXXXXXXX@XXXXXXXX.XXX",
            "Location": "Seattle",
            "ID": "3",
            "Billing": "40000",
            "Name": "XXXXXXXXXXXX",
        }
    ],
    "4": [
        {
            "Email": "XXXXXXXXX@XXXXXXXX.XXX",
            "Location": "Seattle",
            "ID": "4",
            "Billing": "20000",
            "Name": "XXXXXXXXXXXX",
        }
    ],
}

maskedNumericCSV = {
    "1": [
        {
            "Email": "john@mail.com",
            "Location": "New York",
            "ID": "1",
            "Billing": 19000,
            "Name": "John Smith",
        }
    ],
    "2": [
        {
            "Email": "Kelly@your-mail.com",
            "Location": "Washington",
            "ID": "2",
            "Billing": 19000,
            "Name": "Kelly Lawrence Gomez",
        }
    ],
    "3": [
        {
            "Email": "carl-wins@mail-bot.com",
            "Location": "Seattle",
            "ID": "3",
            "Billing": 19000,
            "Name": "Carl Winslow",
        }
    ],
    "4": [
        {
            "Email": "carl-wins@mail-bot.com",
            "Location": "Seattle",
            "ID": "4",
            "Billing": 19000,
            "Name": "Carl Winslow",
        }
    ],
}


class TestFunctions(unittest.TestCase):
    def test_calcBillingStat(self):
        self.assertEqual(calc_billing_stat(testCSV), [40000, 15000, 23750])

    def test_calcNameStats(self):
        self.assertEqual(calc_name_stats(testCSV), [20, 10, 13])

    def test_reportStat(self):
        self.assertEqual(
            report_stat(testCSV),
            [
                "Name: Max. 20, Min. 10, Avg. 13",
                "Billing: Max. 40000, Min. 15000, Avg. 23750",
            ],
        )

    def test_maskEmailAndName(self):
        completions = 0

        for line in maskedCSV:
            maskedEmail = maskedCSV[line][0]["Email"]
            email = testCSV[line][0]["Email"]

            maskedName = maskedCSV[line][0]["Name"]
            name = testCSV[line][0]["Name"]

            if len(maskedEmail) == len(email) and len(maskedName) == len(name):
                completions = completions + 1

        if completions == len(maskedCSV):
            self.assertDictEqual(mask_email_and_name(testCSV), maskedCSV)
        else:
            self.fail(
                "length of masked email and maked names are not equal to it original values"
            )

    def test_maskNumeric(self):
        self.assertDictEqual(mask_numeric(testCSV2), maskedNumericCSV)
