from fastapi import FastAPI, Depends
import uvicorn as u
from sqlalchemy.orm import Session

from db.base_class import Base
from db.session import SessionLocal, engine
from schema.tag import Tag
from service.tag_service import save_tag

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/{name}")
async def hello(name: str):
    return {"Hello": "world" + name}


@app.post("/create/tag")
def create_tag(tag: Tag, db: Session = Depends(get_db)):
    tag.id = 1
    db_user = save_tag(db, tag)


Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    u.run(app, port=3000)
