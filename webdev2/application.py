from flask import Flask, render_template, request
from recommenders import random_recommender

# the main object that handles both the application 
# and the web server where the application run 
# import_name name of the module where the application is run
app = Flask(import_name=__name__)

# print(__name__)

# Decorators "@" add functionality to the function they are on 
# This particular decorator @app.route implements a URL
# the output of the view function homepage is displayed on the web screen
@app.route("/")
def homepage():
    return render_template("home.html")

    # return """
    # <h1>Hello User</h1>
    # <p>Welcome to costmary-function movie recommender</p>
    #  <p>Click <a href='/recommendations'>here</a> to get the recommendations</p>
    # """

@app.route("/recommendations")
def results():
    # request parses the URL and get the user inputs
    user_query =request.args.to_dict()
    print(user_query)
    top3 = random_recommender(user_query)
    return render_template(
        "results.html",
        recommendation_list=top3
    )
    # return render_template(
    #     "results.html",
    #     first_movie = top3[0],
    #     second_movie = top3[1],
    #     third_movie = top3[2]
    # )

   


if __name__ == "__main__":
    # Server startup
    # app.run() lauches Flask's integrated development web server
    
    # debug=True:
    # Logs out any error message
    # restart the server anytime a change in the code is detected
    app.run(debug=True)
   