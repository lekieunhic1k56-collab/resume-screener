from pydantic import BaseModel

class Resume(BaseModel):
    name: str
    email: str
    phone: str
    education: list[str]
    work_experience: list[dict]

class JobPosting(BaseModel):
    title: str
    description: str
    requirements: list[str]
    location: str

class Application(BaseModel):
    resume: Resume
    job_posting: JobPosting
    cover_letter: str
