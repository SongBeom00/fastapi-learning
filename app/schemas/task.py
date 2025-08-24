from pydantic import BaseModel, Field

# class Task(BaseModel):
#     id: int
#     title: str | None = Field(None, example='세탁소에 맡긴 것을 찾으러 가기')
#     # title: bool | None = Field(None, example='세탁소에 맡긴 것을 찾으러 가기') # Internal Server Error 발생!
#     done: bool = Field(False, description="완료 플래그")


class TaskBase(BaseModel):
    title: str | None = Field(None, example='세탁소에 맡긴 것을 찾으러 가기')


class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True

class Task(TaskBase):
    id: int
    done: bool = Field(False, description="완료 플래그")
    pass

    # class Config: # 이전 방식
    #     orm_mode = True

    class Config: # 새로운 방식 (pydantic v2)
        from_attributes = True
