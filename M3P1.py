# -*- coding: utf-8 -*-
ticker = input("Enter stock ticker symbol: ")
shares = int(input("Enter shares bought: "))
cost_per_share = float(input("Enter the cost of each share: "))

amount_invested = shares * cost_per_share
print("\n")
print(f"Stock ticker symbol: {ticker.upper()}")
print(f"Total amount invested : ${amount_invested:.2f}")
