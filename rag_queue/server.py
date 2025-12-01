from dotenv import load_dotenv
load_dotenv()
from .client.rq_client import queue
from .queues.worker import process_query
from fastapi import FastAPI, Query
from dotenv import load_dotenv

app = FastAPI()

@app.get("/")
def root():
    return {'"status": Server is up and running'}

@app.post("/chat")
def chat(query: str = Query(..., description="THe chat query of the user")):
    job = queue.enqueue(process_query, query)
    return {'status: queued',f'job_id: {job.id}'}

@app.get("/job-status")
def get_result(job_id: str = Query(..., description="Job ID")):
    job = queue.fetch_job(job_id=job_id)
    result = job.return_value()

    return {"result": result}

# rq worker -w rq.worker.SimpleWorker - command from root repo dir to start worker