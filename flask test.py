from flask import Flask, render_template

my_skills = ["html", "css", "flask", "python"]


portfolio_app = Flask(__name__) # this is to create the app


@portfolio_app.route("/")
def index():
    return render_template("/pages/index.html",
                           title= "HOME")

    
@portfolio_app.route("/skills")
def skills():
    return render_template("pages/skills.html",
                           title= "SKILLS", 
                           skills = my_skills,
                           custom_css= "skills.css")
    
@portfolio_app.route("/about") 
def about():
    return render_template("/pages/about.html", title= "ABOUT",
                           page_head= "ABOUT",
                           custom_css= "about.css")



if __name__ == "__main__": #this to run the app based on the main file
    portfolio_app.run(debug=True, port=2000)