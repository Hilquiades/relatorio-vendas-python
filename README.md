# Relatório de vendas em Python

Muita gente que vende por conta própria guarda tudo em planilha e perde tempo somando na mão. Fiz este script para resolver isso: ele lê um CSV de vendas e mostra quanto entrou por mês, quais produtos mais vendem e o total geral.

Usa só o que já vem no Python, então não precisa instalar nada.

## Como usar
```bash
python relatorio.py vendas_exemplo.csv
python relatorio.py --teste      # confere se as contas estão certas
```

O CSV precisa ter as colunas `data` (AAAA-MM-DD), `produto`, `quantidade` e `valor_unitario`. Tem um exemplo na pasta.

## Próximos passos que quero fazer
Exportar para Excel/PDF e gerar gráficos. Se você precisa de algo parecido adaptado para a sua planilha, é só me chamar.
