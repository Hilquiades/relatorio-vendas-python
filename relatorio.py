"""Lê um CSV de vendas (data,produto,quantidade,valor_unitario) e gera um resumo."""
import csv
import sys
from collections import defaultdict


def resumir(linhas):
    """Retorna (total por mês, total por produto, total geral)."""
    por_mes, por_produto = defaultdict(float), defaultdict(float)
    for l in linhas:
        valor = int(l["quantidade"]) * float(l["valor_unitario"])
        por_mes[l["data"][:7]] += valor  # AAAA-MM
        por_produto[l["produto"]] += valor
    return dict(por_mes), dict(por_produto), sum(por_mes.values())


def brl(v):
    return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def main(caminho):
    sys.stdout.reconfigure(encoding="utf-8")  # evita erro de acento no Windows
    with open(caminho, newline="", encoding="utf-8") as f:
        mes, produto, total = resumir(csv.DictReader(f))
    print("== Vendas por mês ==")
    for k in sorted(mes):
        print(f"{k}: {brl(mes[k])}")
    print("\n== Ranking de produtos ==")
    for k, v in sorted(produto.items(), key=lambda x: -x[1]):
        print(f"{k}: {brl(v)}")
    print(f"\nTotal geral: {brl(total)}")


def _teste():
    linhas = [
        {"data": "2026-01-05", "produto": "A", "quantidade": "2", "valor_unitario": "10.5"},
        {"data": "2026-02-01", "produto": "B", "quantidade": "1", "valor_unitario": "4"},
    ]
    mes, prod, total = resumir(linhas)
    assert mes == {"2026-01": 21.0, "2026-02": 4.0} and total == 25.0
    assert prod["A"] == 21.0 and brl(1234.5) == "R$ 1.234,50"
    print("ok")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--teste":
        _teste()
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        sys.exit("uso: python relatorio.py vendas.csv  |  python relatorio.py --teste")
