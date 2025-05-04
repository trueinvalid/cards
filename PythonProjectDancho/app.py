from idlelib.history import History

from  flask import Flask, render_template, request, redirect,url_for
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


history = []

cards=[
    {"id":0,"question":"Какая по счету планета Земля", "answer":"4"},
    {"id":1,"question":"Первый президент Америки", "answer":"Джордж Вашингтон"},
    {"id":2,"question":"Самый лучший игрок в кс го", "answer":"$$$$1mple"},
    {"id":3,"question":"Самый богатый человек в мире", "answer":"Илон Маск"},
    {"id":4,"question":"Когда началась вторая мировая война", "answer":"1941"},
    {"id":5,"question":"Каких камней нет в море", "answer":"сухих"},
    {"id":6,"question":"Фильм с самой большой оценкой", "answer":"Побег из Шоушенка"},
    {"id":7,"question":"Где лучшие тусовки", "answer":"у нас в клубе"},

]
@app.route("/flashCard", methods=['GET','POST'])
def flashCard():
    show_id = None
    if request.method == 'POST':
        show_id = int(request.form["card_id"])
    return render_template("flashCArd.html", cards=cards, show_id=show_id)



@app.route("/calculator", methods=['GET','POST'])
def calculator():
    expression = ""
    result = ""
    if request.method == 'POST':
        expression = request.form.get("expression","")
        button = request.form.get("button","")

        if button == "AC":
            expression=""
        elif button == "=":
            try:

                result = str(eval(expression))
                history.append(f"{expression} = {result}")
                expression = result
            except:
                result = "Ошибка"
                history.append(f"{expression} = Ошибка!")
                expression = ""
        else:
            expression = expression + button
            result = expression
    return render_template("calcucator.html",result=result,expression=expression, history=history)

if __name__ == "__main__":
    app.run(debug=True)






