import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/get_categories")
def get_categories():
    """
    This function renders the index.html template and gets the categories
    and all of the recommendations from the database.
    """
    categories = mongo.db.categories.find()
    recommendations = list(
        mongo.db.recommendations.find().sort("recommend_date", -1))
    return render_template(
        "index.html", categories=categories, recommendations=recommendations)


@app.route("/filter_categories/<recommend_category>")
def filter_categories(recommend_category):
    """
    This function acts as a filter, when the user clicks on a category it
    will then only display recommendations of that paticular category.
    """
    categories = mongo.db.categories.find()
    recommendations = list(mongo.db.recommendations.find(
        {"recommend_category": recommend_category}).sort(
            "recommend_date", -1))
    return render_template(
        "index.html", categories=categories, recommendations=recommendations)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    This function enables the user to search the recommendations
    """
    query = request.form.get("query")
    recommendations = list(
        mongo.db.recommendations.find({"$text": {"$search": query}}))
    return render_template("index.html", recommendations=recommendations)


@app.route("/view_recommendation/<recommendation_id>")
def view_recommendation(recommendation_id):
    """
    This function renders the recommendation.html template and
    provides the user with the full details about the recommendation
    that they have clicked on.
    """
    recommendation = mongo.db.recommendations.find_one(
            {"_id": ObjectId(recommendation_id)})
    return render_template(
            "recommendation.html", recommendation=recommendation)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    This function checks if the username already exists and if so
    provides the user with a flash message detailing this. Werkzeug
    is used to hash the users password for additional security.
    A session cookie is then created for the new user.
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for('profile', username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    This function checks if the username exists in the database then
    checks if the password is correct for that particular user.
    If the username or password is incorrect then the user is redirected
    to the login page and a flash message is displayed.
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for('profile', username=session["user"]))

            else:
                flash("Incorrect username or password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect username or password")
            return redirect(url_for('login'))

    return render_template("login.html")


@app.route("/logout")
def logout():
    """
    This function removes the user from the current session cookie
    and then redirects them to the login page.
    """
    flash("You have been logged out!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    This function renders the profile.html template and displays the
    session users recommendations.
    """
    if session["user"]:
        username = mongo.db.users.find_one({
            "username": session["user"]})["username"]

        recommendations = list(
            mongo.db.recommendations.find().sort("recommend_date", -1))
        return render_template(
            "profile.html", recommendations=recommendations, username=username)

    return redirect(url_for("login.html"))


@app.route("/add_recommendation", methods=["GET", "POST"])
def add_recommendation():
    """
    This function enables the user to add a recommendation by inserting
    the data from the input fields into the recommendations collection
    within the database.
    """
    if request.method == "POST":
        recommendation = {
            "recommend_name": request.form.get("recommend_name"),
            "recommend_category": request.form.get("recommend_category"),
            "recommend_info": request.form.get("recommend_info"),
            "recommend_description": request.form.get("recommend_description"),
            "recommend_image": request.form.get("recommend_image"),
            "created_by": session["user"],
            "recommend_date": request.form.get("recommend_date")
        }
        mongo.db.recommendations.insert_one(recommendation)
        flash("Recommendation Successfully Added")
        return redirect(url_for("profile", username=session["user"]))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
            "add_recommendation.html", categories=categories)


@app.route("/edit_recommendation/<recommendation_id>", methods=["GET", "POST"])
def edit_recommendation(recommendation_id):
    """
    This function enables the user to edit their recommendations
    by using the update method.
    """
    if request.method == "POST":
        submit = {
            "recommend_name": request.form.get("recommend_name"),
            "recommend_category": request.form.get("recommend_category"),
            "recommend_info": request.form.get("recommend_info"),
            "recommend_description": request.form.get("recommend_description"),
            "recommend_image": request.form.get("recommend_image"),
            "created_by": session["user"],
            "recommend_date": request.form.get("recommend_date")
        }
        mongo.db.recommendations.update(
            {"_id": ObjectId(recommendation_id)}, submit)
        flash("Recommendation Successfully Updated")
        return redirect(url_for("profile", username=session["user"]))

    recommendation = mongo.db.recommendations.find_one(
            {"_id": ObjectId(recommendation_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recommendation.html", recommendation=recommendation,
        categories=categories)


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """
    This function enables the Admin for the website to edit the categories.
    """
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "category_info": request.form.get("category_info"),
            "category_image": request.form.get("category_image")
        }
        mongo.db.categories.update(
            {"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("manage_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_recommendation/<recommendation_id>")
def delete_recommendation(recommendation_id):
    """
    This function enables the user to delete their recommendations by
    using the remove method to remove the recommendation for the database.
    """
    mongo.db.recommendations.remove({"_id": ObjectId(recommendation_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    """
    This function enables the Admin for the website to delete categories
    from the category collection in the database.
    """
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("manage_categories"))


@app.route("/manage_categories")
def manage_categories():
    """
    This function renders the categories.html template and from this page the
    Admin for the website is able to add, edit and delete categories.
    """
    if session['user'] == "admin".lower():

        categories = list(mongo.db.categories.find().sort("category_name", 1))
        return render_template("categories.html", categories=categories)

    else:
        return render_template("errors/403.html")


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """
    This function renders the add_category.html template and enables the Admin
    for the website to add a new category by using the insert_one method to
    add it to the database.
    """
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name"),
            "category_info": request.form.get("category_info"),
            "category_image": request.form.get("category_image")
        }
        mongo.db.categories.insert_one(category)
        flash("Category Successfully Added")
        return redirect(url_for("manage_categories"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
            "add_category.html", categories=categories)


@app.route("/contact")
def contact():
    """
    This function renders the contact.html template.
    """
    return render_template("contact.html")


@app.errorhandler(404)
def page_not_found(e):
    """
    This function renders the 404.html template to handle any 404 errors.
    """
    return render_template("errors/404.html"), 404


@app.errorhandler(403)
def page_forbidden(e):
    """
    This function renders the 403.html template and handles any 403 errors.
    """
    return render_template("errors/403.html"), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")), debug=True)


""" ** Sources of guidance used to create this code ** """

""" The course content from code institute """
""" https://github.com/adamdelancey/ms3-tips/blob/master/app.py """
