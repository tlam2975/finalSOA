 from flask import Flask, render_template
from config import config
from routes.api import init_routes
from services.database import DatabaseService
from services.calculation import CalculationService
from services.ticket_management import TicketManagementService
from services.business import BusinessService
import os

app = Flask(__name__)
app.config.from_object(config)

database = DatabaseService()
calculation = CalculationService()
ticket_management = TicketManagementService(database, calculation)
business = BusinessService(ticket_management, calculation)

init_routes(app, business, ticket_management, calculation)

if __name__ == '__main__':
    print("\n" + "="*50)
    print("📍 URL: http://localhost:2975")
    print("="*50)
    app.run(debug=True, host='0.0.0.0', port=2975)
