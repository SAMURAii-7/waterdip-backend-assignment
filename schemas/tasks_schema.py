from .task_schema import task_schema

tasks_schema = {
    "type": "object",
    "properties": {
        "tasks": {
            "type": "array",
            "items": task_schema,
        }
    },
    "required": ["tasks"],
}
