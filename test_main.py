import unittest
import json
from main import main

with open("data-1.json", "r") as f:
    jsonData1 = json.load(f)
with open("data-2.json", "r") as f:
    jsonData2 = json.load(f)
with open("data-result.json", "r") as f:
    jsonExpectedResult = json.load(f)

class TestSolution(unittest.TestCase):
    def test_sanity(self):
        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(result, jsonExpectedResult)

    def test_dataType1(self):
        result = main(jsonData1)
        self.assertEqual(result, jsonExpectedResult, 'Converting from Type 1 failed')

    def test_dataType2(self):
        result = main(jsonData2)
        self.assertEqual(result, jsonExpectedResult, 'Converting from Type 2 failed')

if __name__ == '__main__':
    unittest.main()
