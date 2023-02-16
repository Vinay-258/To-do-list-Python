from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def root():
    return "Welcome TO FASTAPI"


Todos = {
    1: {
        "title": "Learn for FAT ",
        "completed": False,
    },
    2: {
        "title": "Attend the meeting tomorrow 3pm",
        "completed": False,
    },
    3: {
        "title": "Finish Data mining JCOMP project",
        "completed": False,
    },
    4: {
        "title": "Prepare for JEE exams",
        "completed": False,
    },
    5: {
        "title": "study for Java exam on Monday ",
        "completed": False,
    }

}


class TodoItem(BaseModel):
    title: str
    completed: bool

# 1. view all the existing todo items


@app.get("/todos", status_code=status.HTTP_200_OK)
def get_all_todo_items(title: str = ""):
    results = {}
    if title != "" or title != None:
        for id in Todos:
            if title in Todos[id]["title"]:
                results[id] = Todos[id]
    else:
        results = Todos
    return Todos


@app.get("/todos/{id}", status_code=status.HTTP_200_OK)
def get_todo_item(id: int):
    if id in Todos:
        return Todos[id]

    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

# 2. Create todo items


@app.post("/todo", status_code=status.HTTP_201_CREATED)
def create_todo_item(todo_item: TodoItem):
    id = max(Todos)+1
    Todos[id] = todo_item.dict()
    return Todos[id]


# 3. Update todo item

@app.put("/todos", status_code=status.HTTP_200_OK)
def update_todo_item(todo_item: TodoItem):
    if id in Todos:
        Todos[id] = todo_item.dict()
        return Todos[id]

    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

# 4. Delete todo item


@app.delete("/todos/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo_item(id: int):
    if id in Todos:
        Todos.pop(id)
        return

    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
