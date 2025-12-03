class BusinessService:
    """Dịch vụ xử lý logic nghiệp vụ"""

    def __init__(self, ticket_service, calculation_service):
        self.ticket_service = ticket_service
        self.calculator = calculation_service
        print("💼 [Business Service] Khởi tạo thành công")

    def get_movies_list(self):
        return [
            "Avatar: The Way of Water",
            "Spider-Man: No Way Home",
            "Top Gun 2: Maverick",
            "Avengers: Endgame",
            "Doctor Strange 2",
            "Minions: The Rise of Gru",
            "Thor: Love and Thunder",
            "Jurassic World Dominion"
        ]

    def get_price_options(self):
        """Lấy các lựa chọn giá vé"""
        return [
            {"value": 80000, "label": "80,000 VNĐ - Giờ chiếu sớm"},
            {"value": 100000, "label": "100,000 VNĐ - Giờ chiếu thường"},
            {"value": 120000, "label": "120,000 VNĐ - Giờ chiếu tối"},
            {"value": 150000, "label": "150,000 VNĐ - Suất chiếu VIP"}
        ]

    def process_ticket_booking(self, form_data):
        """Xử lý đặt vé"""
        try:
            ticket_data = {
                'movie_name': form_data.get('movie_name'),
                'quantity': form_data.get('quantity'),
                'price': form_data.get('price')
            }

            new_ticket = self.ticket_service.add_ticket(ticket_data)
            return {
                'success': True,
                'ticket': new_ticket,
                'message': f'Đã đặt vé "{ticket_data["movie_name"]}" thành công!'
            }
        except Exception as e:
            return {
                'success': False,
                'message': f'Lỗi đặt vé: {str(e)}'
            }

    def get_dashboard_data(self):
        """Lấy dữ liệu cho dashboard"""
        tickets = self.ticket_service.get_ticket_list()
        total_revenue = self.calculator.calculate_total_revenue(tickets)

        return {
            'tickets': tickets,
            'total_revenue': total_revenue,
            'total_tickets': len(tickets),
            'revenue_formatted': self.calculator.format_currency(total_revenue)
        }