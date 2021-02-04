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
    categories = mongo.db.categories.find()
    recommendations = list(
        mongo.db.recommendations.find().sort("recommend_date", -1))
    return render_template(
        "index.html", categories=categories, recommendations=recommendations)


@app.route("/filter_categories/<recommend_category>")
def filter_categories(recommend_category):
    categories = mongo.db.categories.find()
    recommendations = list(mongo.db.recommendations.find(
        {"recommend_category": recommend_category}).sort(
            "recommend_date", -1))
    return render_template("index.html",
    categories=categories, recommendations=recommendations)


@app.route("/view_recommendation/<recommendation_id>")
def view_recommendation(recommendation_id):
    recommendation = mongo.db.recommendations.find_one(
            {"_id": ObjectId(recommendation_id)})
    return render_template(
            "recommendation.html", recommendation=recommendation)


@app.route("/register", methods=["GET", "POST"])
def register():
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
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
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
    flash("You have been logged out!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
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


@app.route("/delete_recommendation/<recommendation_id>")
def delete_recommendation(recommendation_id):
    mongo.db.recommendations.remove({"_id": ObjectId(recommendation_id)})
    flash("Task Successfully Deleted")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("manage_categories"))


@app.route("/manage_categories")
def manage_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")), debug=True)
