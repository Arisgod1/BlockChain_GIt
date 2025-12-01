from tortoise.models import Model
from tortoise import fields

class Student(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="姓名")
    number = fields.IntField(unique=True, description="学号")
    age = fields.IntField(description="年龄")
    school = fields.CharField(max_length=100, description="学校")
    password = fields.CharField(max_length=32, description="密码")

    class Meta:
        table = "students"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "number": self.number,
            "age": self.age,
            "school": self.school
        }


