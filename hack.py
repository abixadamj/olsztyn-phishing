from fastapi import FastAPI, Form, status, Response
import uvicorn

app = FastAPI()

@app.get("/")
def strona():
    return {"A": "Wartość A", "B": "Wartość B"}


@app.post("/mail-login")
def read_data_form(auth_id: str = Form(...),
                         password: str = Form(...),
                         email: str = Form(...),
                         ):
    if auth_id == "NIC":
        return Response(status_code=status.HTTP_204_NO_CONTENT)



uvicorn.run(app, port=8080, host='0.0.0.0')