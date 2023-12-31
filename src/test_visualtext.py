import unittest
from visualtext import VisualText

class TestVisualText(unittest.TestCase):
    def setUp(self):
        self.vt = VisualText()
    def test_diceFace1(self):
        got = self.vt.diceFace1()
        expected = """
+-------+
|       |
|   *   |
|       |
+-------+
"""
        self.assertEqual(got, expected)
    def test_diceFace2(self):
        got = self.vt.diceFace2()
        expected = """
+-------+
|     * |
|       |
| *     |
+-------+
"""
        self.assertEqual(got, expected)
    def test_diceFace3(self):
        got = self.vt.diceFace3()
        expected = """
+-------+
|     * |
|   *   |
| *     |
+-------+
"""
        self.assertEqual(got, expected)
    def test_diceFace4(self):
        got = self.vt.diceFace4()
        expected = """
+-------+
| *   * |
|       |
| *   * |
+-------+
"""
        self.assertEqual(got, expected)
    def test_diceFace5(self):
        got = self.vt.diceFace5()
        expected = """
+-------+
| *   * |
|   *   |
| *   * |
+-------+
"""
        self.assertEqual(got, expected)
    def test_diceFace6(self):
        got = self.vt.diceFace6()
        expected = """
+-------+
| *   * |
| *   * |
| *   * |
+-------+
"""
        self.assertEqual(got, expected)
    def test_setSymbolWithValidValue(self):
        got = self.vt.setSymbol("A")
        expected = "A"
        self.assertEqual(got, expected)
    def test_setSymbolWithInvalidValue(self):
        with self.assertRaises(ValueError) as context:
            self.vt.setSymbol("Abacate")
        self.assertEqual("Error: Symbol must be only one character", str(context.exception))
    def test_changeValueVisualTextWith1(self):
        self.vt.setSymbol("?")
        got = self.vt.changeValueVisualText(1)
        expected = """
+-------+
|       |
|   ?   |
|       |
+-------+
"""
        self.assertEqual(got, expected)
    def test_changeValueVisualTextWith2(self):
        self.vt.setSymbol("A")
        got = self.vt.changeValueVisualText(2)
        expected = """
+-------+
|     A |
|       |
| A     |
+-------+
"""
        self.assertEqual(got, expected)
    def test_changeValueVisualTextWith3(self):
        self.vt.setSymbol("3")
        got = self.vt.changeValueVisualText(3)
        expected = """
+-------+
|     3 |
|   3   |
| 3     |
+-------+
"""
        self.assertEqual(got, expected)
    def test_changeValueVisualTextWith4(self):
        self.vt.setSymbol("+")
        got = self.vt.changeValueVisualText(4)
        expected = """
+-------+
| +   + |
|       |
| +   + |
+-------+
"""
        self.assertEqual(got, expected)
    def test_changeValueVisualTextWith5(self):
        self.vt.setSymbol("X")
        got = self.vt.changeValueVisualText(5)
        expected = """
+-------+
| X   X |
|   X   |
| X   X |
+-------+
"""
        self.assertEqual(got, expected)
    def test_changeValueVisualTextWith6(self):
        self.vt.setSymbol("0")
        got = self.vt.changeValueVisualText(6)
        expected = """
+-------+
| 0   0 |
| 0   0 |
| 0   0 |
+-------+
"""
        self.assertEqual(got, expected)
    def test_changeValueVisualTextWithInvalidValue(self):
        self.vt.setSymbol("")
        with self.assertRaises(ValueError) as context:
            self.vt.changeValueVisualText(10)
        self.assertEqual("Error: Number must be between 1 and 6", str(context.exception))

if __name__ == '__main__':
    unittest.main()
