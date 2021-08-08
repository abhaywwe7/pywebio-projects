from pywebio.input import *
from pywebio.output import *
from flask import Flask
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH

app= Flask(__name__)

def exam():
    count=0;
    name = input("Enter your name", type="text")
    q1 = radio("What is the maximum possible length of an identifier?",["16","32","64","None of these above"])
    if q1 == "None of these above":
        count+=1;
    q2 = radio("Who developed the Python language?",["Zim Den","Guido van Rossum","Niene Stom","Wick van Rossum"])
    if q2 == "Guido van Rossum":
       count+=1;

    q3 = radio("Which one of the following is the correct extension of the Python file?",[".py",".python",".p","None of these"])
   
    if q3 == ".py":
        count+=1;

    if count>1:
        put_text(name + ", your score is "+str(count))
        style(put_text("Result : Passed"),"color:green")

    else:
        put_text(name +",your score is "+str(count))
        style(put_text("Result : Failed"),"color:red")
    put_text("Thank you for your participation..!")    

app.add_url_rule('/','webio_view',webio_view(exam),methods=['GET','POST','OPTIONS'])
app.run(host="localhost",port= 5000)

# exam()
