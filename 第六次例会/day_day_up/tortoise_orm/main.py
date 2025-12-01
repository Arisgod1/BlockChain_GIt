import uvicorn
import sys
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict
from typing import Optional, List

# 添加当前目录到Python路径
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
os.chdir(current_dir)

import settings
from models import Student
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()
#需要配置的信息很多,一般将其放置在一个文件里面单独存放
register_tortoise(
    app=app,
    config=settings.TORTOISE_ORM)


class StudentCreate(BaseModel):
    name: str
    number: int
    age: int
    school: str
    password: str


class StudentResponse(BaseModel):
    id: int
    name: str
    number: int
    age: int
    school: str

    model_config = ConfigDict(from_attributes=True)


class StudentQuery(BaseModel):
    number: Optional[int] = None
    name: Optional[str] = None
    school: Optional[str] = None


@app.get("/")
async def hello():
    return {"message": "学生管理系统"}


@app.post("/students", response_model=StudentResponse)
async def create_student(student: StudentCreate):
    student_obj = await Student.create(**student.dict())
    return student_obj.to_dict()


@app.post("/students/list", response_model=list[StudentResponse])
async def get_all_students():
    students = await Student.all()
    return [student.to_dict() for student in students]


@app.post("/students/query", response_model=StudentResponse)
async def get_student_by_number(query: StudentQuery):
    student = await Student.get_or_none(number=query.number)
    if not student:
        raise HTTPException(status_code=404, detail="学生未找到")
    return student.to_dict()


@app.delete("/students/{student_number}")
async def delete_student_by_number(student_number: int):
    student = await Student.get_or_none(number=student_number)
    if not student:
        raise HTTPException(status_code=404, detail="学生未找到")
    await student.delete()
    return {"message": "学生删除成功"}


if __name__ == '__main__':
    uvicorn.run('main:app', port=7070, reload=True)