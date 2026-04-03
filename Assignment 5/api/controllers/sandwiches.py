from sqlalchemy.orm import Session
from fastapi import Response, status
from ..models import models, schemas

def create(db: Session, sandwich: schemas.SandwichCreate):
    # create a new instance of the sandwich model
    db_sandwich = models.Sandwich(
        sandwich_name=sandwich.sandwich_name,
        price=sandwich.price
    )
    # add it to the database
    db.add(db_sandwich)
    # commit the changes to the database
    db.commit()
    # refresh the database
    db.refresh(db_sandwich)
    return db_sandwich

# reads all sandwiches in the database
def read_all(db: Session):
    return db.query(models.Sandwich).all()

#read one specific sandwich in the database
def read_one(db: Session, sandwich_id: int):
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()

# changes an existing sandwich record in the database
def update(db: Session, sandwich_id: int, sandwich: schemas.SandwichUpdate):
    # query the database for the specific sandwich to update
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    # extract the update data from the 'sandwich' object
    update_data = sandwich.model_dump(exclude_unset=True)
    # update the database record with the new data, without synchronizing the session
    db_sandwich.update(update_data, synchronize_session=False)
    # commit the changes to the database
    db.commit()
    return db_sandwich.first()

# delete a sandwich from the database
def delete(db: Session, sandwich_id: int):
    # query the database for the sandwich to delete
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    # removes the row from the database
    db_sandwich.delete(synchronize_session=False)
    # commit the changes to the database
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
