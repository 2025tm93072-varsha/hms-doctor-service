from app.db.session import engine, Base
from app.models.doctor import Doctor
from app.models.schedule import Schedule

Base.metadata.create_all(bind=engine)
print("Tables created")