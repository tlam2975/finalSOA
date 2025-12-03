from flask import render_template, request, jsonify, redirect, url_for, flash

def init_routes(app, business, ticket_management, calculation):
    @app.route('/')
    def index():
        try:
            dashboard_data = business.get_dashboard_data()
            movies = business.get_movies_list()
            price_options = business.get_price_options()
            return render_template('index.html',
                                 data=dashboard_data,
                                 movies=movies,
                                 price_options=price_options)
        except Exception as e:
            flash(f'Lỗi tải trang: {str(e)}', 'error')
            return render_template('index.html', data={}, movies=[], price_options=[])
        # return render_template('index.html')

    @app.route('/api/tickets', methods=['POST'])
    def add_ticket():
        try:
            result = business.process_ticket_booking(request.form)
            if result['success']:
                flash(result['message'], 'success')
            else:
                flash(result['message'], 'error')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Lỗi hệ thống: {str(e)}', 'error')
            return redirect(url_for('index'))

    @app.route('/api/tickets/<ticket_id>', methods=['DELETE'])
    def delete_ticket(ticket_id):
        try:
            deleted_ticket = ticket_management.remove_ticket(ticket_id)
            if deleted_ticket:
                return jsonify({
                    'success': True,
                    'message': f'Đã xóa vé "{deleted_ticket["movie_name"]}" thành công!'
                })
            else:
                return jsonify({
                    'success': False,
                    'message': 'Không tìm thấy vé để xóa!'
                }), 404
        except Exception as e:
            return jsonify({
                'success': False,
                'message': f'Lỗi xóa vé: {str(e)}'
            }), 500

    @app.route('/api/revenue')
    def get_revenue():
        try:
            tickets = ticket_management.get_ticket_list()
            total_revenue = calculation.calculate_total_revenue(tickets)
            return jsonify({
                'success': True,
                'total_revenue': total_revenue,
                'revenue_formatted': calculation.format_currency(total_revenue)
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'message': f'Lỗi tính doanh thu: {str(e)}'
            }), 500

    @app.route('/api/tickets')
    def get_tickets():
        try:
            tickets = ticket_management.get_ticket_list()
            return jsonify({
                'success': True,
                'tickets': tickets
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'message': f'Lỗi lấy danh sách vé: {str(e)}'
            }), 500