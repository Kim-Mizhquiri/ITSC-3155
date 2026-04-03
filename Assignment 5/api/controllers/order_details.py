from sqlalchemy.orm import Session
from fastapi import Response, status
from ..models import models, schemas


def create(db: Session, order_detail: schemas.OrderDetailCreate):
    # create a new instance of the order detail model with the data
    db_order_detail = models.OrderDetail(
        order_id=order_detail.order_id,
        sandwich_id=order_detail.sandwich_id,
        amount=order_detail.amount
    )
    # add it to the database
    db.add(db_order_detail)
    # commit the changes to the database
    db.commit()
    # refresh the database
    db.refresh(db_order_detail)
    return db_order_detail

# reads all the order details
def read_all(db: Session):
    return db.query(models.OrderDetail).all()

# reads one item from the order detail table
def read_one(db: Session, order_detail_id: int):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()

# updates one item from the order detail table
def update(db: Session, order_detail_id: int, order_detail: schemas.OrderDetailUpdate):
    # query the database for the order detail to update
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id)
    # extract the update
    update_data = order_detail.model_dump(exclude_unset=True)
    # update the database without synchronizing
    db_order_detail.update(update_data, synchronize_session=False)
    # commit the changes
    db.commit()
    return db_order_detail.first()

# deletes one item from the order details table
def delete(db: Session, order_detail_id: int):
    # query the database for the specific order detail to delete
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id)
    # delete the order detail without synchronizing
    db_order_detail.delete(synchronize_session=False)
    # commit the changes
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
