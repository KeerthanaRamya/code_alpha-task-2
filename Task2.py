
stock_prices = {
    "fruits": 180,
    "tatasalt": 50,
    "coffe powder": 80,
    "shampu": 30,
    "dal": 300,
    "sugar": 200,
    "bottles": 120,
    "tea powder": 40
}

portfolio = {}

print("Enter your stock purchases (type 'done' to finish):")
while True:
    stock = input("Enter stock item name (e.g., tea powder): ").strip().lower()
    if stock == 'done':
        break
    if stock not in stock_prices:
        print("❌ Stock not found in our records.")
        continue
    try:
        quantity = int(input(f"Enter quantity of '{stock}': "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("❌ Please enter a valid number.")

total_investment = 0
output_lines = ["\nYour Stock Portfolio:\n"]
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_investment += investment
    output_lines.append(f"{stock.title()}: {qty} units × ₹{price} = ₹{investment}\n")

output_lines.append(f"\nTotal Investment: ₹{total_investment}\n")

print("".join(output_lines))

save_choice = input("Do you want to save this result to a file? (yes/no): ").strip().lower()
if save_choice == 'yes':
    filename = input("Enter filename (e.g., portfolio.txt or portfolio.csv): ").strip()
    try:
        with open(filename, "w") as f:
            f.writelines(output_lines)
        print(f"✅ Portfolio saved to '{filename}'")
    except Exception as e:
        print(f"❌ Error saving file: {e}")
