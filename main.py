# Модель: Метод Ньютона (5 семестр)
# Автор: Помазан Роман, група АІ-233

import os

from flask import Flask, jsonify, request

app = Flask(__name__)


def f(x):
    return x**3 - 2 * x**2 - 5 * x + 6


def df(x):
    return 3 * x**2 - 4 * x - 5


def newton_method(x0: float, tol: float = 1e-4, max_iter: int = 50):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return round(x, 6)
        x = x - fx / df(x)
    return round(x, 6)


@app.route("/calculate", methods=["GET"])
def calculate():
    try:
        x0 = float(request.args.get("x", 1.0))
        result = newton_method(x0)

        return jsonify(
            {
                "input_x0": x0,
                "result": result,
                "equation": "x³ - 2x² - 5x + 6 = 0",
                "method": "Newton",
            }
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    print(f"API запущено на http://0.0.0.0:{port}/calculate")
    app.run(host="0.0.0.0", port=port, debug=False)
