from sqlalchemy.orm import Session
from fastapi import Response, status
from ..models import models, schemas

# creates an instance from the recipe model
def create(db: Session, recipe: schemas.RecipeCreate):
    db_recipe = models.Recipe(
        sandwich_id=recipe.sandwich_id,
        resource_id=recipe.resource_id,
        amount=recipe.amount
    )
    # adds it to the database
    db.add(db_recipe)
    # commits the changes to the database
    db.commit()
    # refresh the database
    db.refresh(db_recipe)
    return db_recipe

# returns all items in the recipe table
def read_all(db: Session):
    return db.query(models.Recipe).all()

# returns one specific item from the recipe table
def read_one(db: Session, recipe_id: int):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()

# updates one item from the recipe table
def update(db: Session, recipe_id: int, recipe: schemas.RecipeUpdate):
    # query the database for the specific recipe to update
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    # extract the update data from the 'recipe' object
    update_data = recipe.model_dump(exclude_unset=True)
    # update the item without synchronizing
    db_recipe.update(update_data, synchronize_session=False)
    # commit the changes
    db.commit()
    return db_recipe.first()

# deletes one item from the recipe table
def delete(db: Session, recipe_id: int):
    # query the database for the specific recipe to delete
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    # delete the recipe without synchronizing
    db_recipe.delete(synchronize_session=False)
    # commit the changes
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)