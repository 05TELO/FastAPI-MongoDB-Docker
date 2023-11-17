from fastapi import FastAPI
from fastapi import Request

from api.database import collection
from api.helpers import check_field
from api.helpers import serialized_id

app = FastAPI()


@app.get("/")
def main_page():
    return {}


@app.get("/templates")
async def all_templates():
    templates = await collection.find().to_list(100)
    res = list(map(serialized_id, templates))
    return res


@app.post("/get_form")
async def get_form(request: Request):
    form_data = await request.json()
    form_fields = {k: check_field(v) for k, v in form_data.items()}
    templates = await collection.find().to_list(100)
    for template in templates:
        template_fields = template.keys() - ["_id", "name"]
        if all(
            field in form_fields and form_fields[field] == template[field]
            for field in template_fields
        ) and set(template_fields) <= set(form_fields.keys()):
            return {"name": template["name"]}
    return form_fields
