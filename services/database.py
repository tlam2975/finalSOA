import datetime

class DatabaseService:

    def __init__(self):
        self.tickets = []  # Mô phỏng database trong memory
        self.next_id = 1
        print("🗄️ [Database Service] Khởi tạo thành công")

    def save_ticket(self, ticket_data):
        ticket = {
            'id': self._generate_ticket_id(),
            'movie_name': ticket_data['movie_name'],
            'quantity': int(ticket_data['quantity']),
            'price': int(ticket_data['price']),
            'total_amount': ticket_data['total_amount'],
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        self.tickets.append(ticket)
        print(f"🗄️ [Database Service] Vé đã được lưu: {ticket['id']}")
        return ticket

    def get_all_tickets(self):
        print(f"🗄️ [Database Service] Lấy danh sách vé: {len(self.tickets)} vé")
        return self.tickets.copy()

    def delete_ticket(self, ticket_id):
        for i, ticket in enumerate(self.tickets):
            if ticket['id'] == ticket_id:
                deleted_ticket = self.tickets.pop(i)
                print(f"🗄️ [Database Service] Vé đã được xóa: {ticket_id}")
                return deleted_ticket
        return None

    def get_ticket_by_id(self, ticket_id):
        for ticket in self.tickets:
            if ticket['id'] == ticket_id:
                return ticket
        return None

    def _generate_ticket_id(self):
        """Tạo mã vé unique"""
        ticket_id = f"VE{str(self.next_id).zfill(6)}"
        self.next_id += 1
        return ticket_id