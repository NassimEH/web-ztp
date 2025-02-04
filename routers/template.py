from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

from db.database import get_db
from db.models import Template
from db.schema import TemplateSchema

router = APIRouter(prefix="/template", tags=["Templates"])

@router.post("/", response_model=TemplateSchema)
def add_template(template: TemplateSchema, db: Session = Depends(get_db)):
    """Ajoute un template à la base de données"""
    new_template = Template(file_path=template.file_path)
    db.add(new_template)
    db.commit()
    db.refresh(new_template)
    return new_template

@router.get("s")
def get_templates(db: Session = Depends(get_db)):
    """Récupère la liste des templates"""
    results = db.execute(select(Template))
    return results.scalars().all()

@router.get("/{template_id}")
def get_template(template_id: int, db: Session = Depends(get_db)):
    """Récupère un template par son ID"""
    return db.get(Template, template_id)
