from sqlalchemy import create_engine,text
from sqlalchemy.exc import SQLAlchemyError
engine = create_engine('mysql://root:@localhost/jobhub')
conn = engine.connect()
   
def load_jobs_from_db():
    try:
        with engine.connect() as conn:
            results = conn.execute(text("SELECT * FROM jobs"))
            jobs = [dict(row._asdict()) for row in results.fetchall()]
        return jobs
    except SQLAlchemyError as e:
        print(f"Error loading jobs from the database: {e}")
        return []
conn.close()
