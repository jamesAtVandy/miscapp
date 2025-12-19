from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, database
from .models import Product, ProductSchema

app = FastAPI()

# Create tables
models.Base.metadata.create_all(bind=database.engine)

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Initial Data Seeding
def seed_db(db: Session):
    if db.query(Product).count() == 0:
        initial_products = [
            Product(id=1, name="NVIDIA RTX 5090 Ti", category="Components", price=1999.99, image="https://images.unsplash.com/photo-1591488320449-011701bb6704?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Z3JhcGhpY3MlMjBjYXJkfGVufDB8fDB8fHww", description="The absolute pinnacle of graphical processing power.", quantity=10),
            Product(id=2, name="Oculus Pro X", category="VR/AR", price=1499.00, image="https://images.unsplash.com/photo-1593508512255-86ab42a8e620?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8dnIlMjBoZWFkc2V0fGVufDB8fDB8fHww", description="Next-gen immersion with haptic feedback integration.", quantity=5),
            Product(id=3, name="Quantum Core i9-15900K", category="Components", price=799.99, image="https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Y3B1fGVufDB8fDB8fHww", description="Unleash multithreaded dominance on your workload.", quantity=20),
            Product(id=4, name="Cyber-Deck Mechanical Keyboard", category="Peripherals", price=249.50, image="https://images.unsplash.com/photo-1595225476474-87563907a212?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8bWVjaGFuaWNhbCUyMGtleWJvYXJkfGVufDB8fDB8fHww", description="Custom switches with programmable OLED displays.", quantity=15),
            Product(id=5, name="Holo-Display 8K", category="Monitors", price=3499.99, image="https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Z2FtaW5nJTIwbW9uaXRvcnxlbnwwfHwwfHx8MA%3D%3D", description="Borderless 8K resolution with holographic projection.", quantity=3),
            Product(id=6, name="Neural Link Interface", category="Experimental", price=5000.00, image="https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fHRlY2hub2xvZ3l8ZW58MHx8MHx8fDA%3D", description="Direct brain-computer interface for zero latency gaming.", quantity=1)
        ]
        db.add_all(initial_products)
        db.commit()

@app.on_event("startup")
def on_startup():
    db = database.SessionLocal()
    seed_db(db)
    db.close()

@app.get("/")
def greet():
    return "Hello"

@app.get("/products", response_model=list[ProductSchema])
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@app.get("/products/{product_id}", response_model=ProductSchema)
def get_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.post("/products", response_model=ProductSchema)
def add_product(product: ProductSchema, db: Session = Depends(get_db)):
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return {"message": "Product deleted"}
    raise HTTPException(status_code=404, detail="Product not found")

@app.put("/products/{product_id}", response_model=ProductSchema)
def update_product(product_id: int, product: ProductSchema, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    for key, value in product.model_dump().items():
        setattr(db_product, key, value)
    
    db.commit()
    db.refresh(db_product)
    return db_product











