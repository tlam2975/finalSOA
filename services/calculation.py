class CalculationService:

    def __init__(self):
        print("🧮 [Calculation Service] Khởi tạo thành công")

    def calculate_ticket_amount(self, quantity, price):
        amount = quantity * price
        print(f"🧮 [Calculation Service] Tính thành tiền: {quantity} x {price:,} = {amount:,} VNĐ")
        return amount

    def calculate_total_revenue(self, tickets):
        total_revenue = sum(ticket['quantity'] * ticket['price'] for ticket in tickets)
        print(f"🧮 [Calculation Service] Tổng doanh thu: {total_revenue:,} VNĐ")
        return total_revenue

    def format_currency(self, amount):
        return f"{amount:,} VNĐ"