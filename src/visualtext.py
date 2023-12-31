import sys

class VisualText:
    def setSymbol(self, symbol):
        if symbol != "" and len(symbol) != 1:
            raise ValueError("Error: Symbol must be only one character")
        self.symbol = symbol
        return self.symbol
    def changeValueVisualText(self, number):
        if number < 1 or number > 6:
            raise ValueError("Error: Number must be between 1 and 6")
        method_name = "diceFace" + str(number)
        method = getattr(self, method_name)
        resp = method()
        if self.symbol != "":
            resp = resp.replace("*", self.symbol)
        return resp
    def diceFace1(self):
        return """
+-------+
|       |
|   *   |
|       |
+-------+
"""
    def diceFace2(self):
        return """
+-------+
|     * |
|       |
| *     |
+-------+
"""
    def diceFace3(self):
        return """
+-------+
|     * |
|   *   |
| *     |
+-------+
"""
    def diceFace4(self):
        return """
+-------+
| *   * |
|       |
| *   * |
+-------+
"""
    def diceFace5(self):
        return """
+-------+
| *   * |
|   *   |
| *   * |
+-------+
"""
    def diceFace6(self):
        return """
+-------+
| *   * |
| *   * |
| *   * |
+-------+
"""

if __name__ == "__main__":
    try:
        vt = VisualText()
        number = int(sys.argv[1])
        symbol = sys.argv[2]
        vt.setSymbol(symbol)
        print(vt.changeValueVisualText(number))
    except IndexError:
        print("Error: Argument number and symbol is required.\nTo default value of symbol, enter empty string, example: ''")
    except ValueError as e:
        print(e)
