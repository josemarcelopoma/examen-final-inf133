from app.database import db


class Reservation(db.Model):
    __tablename__ = "reservations"

    # Define las columnas de la tabla `products`
    id = db.Column(db.Integer, primary_key=True)
    reservation_date = db.Column(db.string(100), nullable=False)
    num_guest = db.Column(db.integer, nullable=False)
    special_requests = db.Column(db.String(100), nullable=False)
    status = db.Column(db.string(100), nullable=False)

    
    def __init__(self, reservation_date,num_guest,special_requests,status):
       
        self.reservation_date = reservation_date
        self.num_guest = num_guest
        self.special_requests = special_requests
        self.status = status
        

    def save(self):
    db.session.add(self)
    db.session.commit()

    @staticmethod
    def get_all():
    return Reservation.query.all()

    @staticmethod
    def get_by_id(id):
    return Reservation.query.get(id)

    
    def update(self, reservation_date = None,num_guest = None,special_requests=None,status = none ):
        
        if reservation_date is not None:
            self.reservation_date = reservation_date
        if num_guest is not None:
            self.num_guest = num_guest
        

        if special_requests is not None:
            self.special_requests = special_requests
        
        if status is not none :
            self.status = status
       
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()