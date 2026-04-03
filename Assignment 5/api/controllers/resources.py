from sqlalchemy.orm import Session
from fastapi import Response, status
from ..models import models, schemas

# create an instance of the resource model
def create(db: Session, resource: schemas.ResourceCreate):
    db_resource = models.Resource(
        item=resource.item,
        amount=resource.amount
    )
    # add it to the database
    db.add(db_resource)
    # commit it
    db.commit()
    # refresh the database
    db.refresh(db_resource)
    return db_resource

# read all the items in the resources table
def read_all(db: Session):
    return db.query(models.Resource).all()

# reads one of the items in the resources table
def read_one(db: Session, resource_id: int):
    return db.query(models.Resource).filter(models.Resource.id == resource_id).first()

# updates a specific resource
def update(db: Session, resource_id: int, resource: schemas.ResourceUpdate):
    # query the database for the specific resource to update
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id)
    # extract the update data from the resource object
    update_data = resource.model_dump(exclude_unset=True)
    # update it without synchronizing
    db_resource.update(update_data, synchronize_session=False)
    # commit the changes to the database
    db.commit()
    return db_resource.first()

# deletes a specific resource
def delete(db: Session, resource_id: int):
    # query the database for the resource to delete
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id)
    # delete the resource without synchronizing
    db_resource.delete(synchronize_session=False)
    # commit the changes
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)