from backend.src.app import create_app, db
from backend.src.auth.models import User, Card

def seed_data():
    app = create_app()
    with app.app_context():
        # Create users
        user1 = User(username='user1', email='user1@example.com')
        user1.set_password('password1')
        user2 = User(username='user2', email='user2@example.com')
        user2.set_password('password2')
        
        # Add users to session
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

        # Create cards
        card1 = Card(name='Card One', set='Set A', price=1.99, alert_price=1.50, quantity=10, user_id=user1.id)
        card2 = Card(name='Card Two', set='Set B', price=2.99, alert_price=2.50, quantity=15, user_id=user1.id)
        card3 = Card(name='Card Three', set='Set C', price=3.99, alert_price=3.00, quantity=20, user_id=user2.id)
        
        # Add cards to session and commit
        db.session.add(card1)
        db.session.add(card2)
        db.session.add(card3)
        
        db.session.commit()
        print("Seed data inserted successfully.")

if __name__ == '__main__':
    seed_data()
