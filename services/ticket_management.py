class TicketManagementService:
    def __init__(self, database_service, calculation_service):
        self.database = database_service
        self.calculator = calculation_service
        print("🎫 [Ticket Management Service] Khởi tạo thành công")

    def add_ticket(self, ticket_data):
        print("🎫 [Ticket Management Service] Đang thêm vé mới...")

        if not self._validate_ticket_data(ticket_data):
            raise ValueError("Dữ liệu vé không hợp lệ")

        total_amount = self.calculator.calculate_ticket_amount(
            int(ticket_data['quantity']),
            int(ticket_data['price'])
        )
        ticket_data['total_amount'] = total_amount

        saved_ticket = self.database.save_ticket(ticket_data)
        print("🎫 [Ticket Management Service] Vé đã được thêm thành công")
        return saved_ticket

    def get_ticket_list(self):
        print("🎫 [Ticket Management Service] Lấy danh sách vé...")
        return self.database.get_all_tickets()

    def remove_ticket(self, ticket_id):
        print(f"🎫 [Ticket Management Service] Xóa vé: {ticket_id}")
        return self.database.delete_ticket(ticket_id)

    def get_ticket_details(self, ticket_id):
        return self.database.get_ticket_by_id(ticket_id)

    def _validate_ticket_data(self, data):
        required_fields = ['movie_name', 'quantity', 'price']
        return all(field in data and data[field] for field in required_fields)
