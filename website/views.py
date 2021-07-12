from flask import Blueprint, render_template, flash, request, redirect, url_for
from . import open_settings
import wikipedia

views = Blueprint(name="views", import_name=__name__)
settings = open_settings()

@views.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        query = request.form.get("search")
        
        if query == "":
            flash(
                message="I think you forgot to type your query !",
                category="error"
            )
            return redirect(url_for("views.home"))

        else:

            try:
                search_wikipedia = wikipedia.search(query)
                result = wikipedia.summary(search_wikipedia)
            except:
                flash(
                    message="Please make sure you have internet connection !",
                    category="error"
                )
                return redirect(url_for("views.home"))

        return render_template("index.html", settings=settings, result=result, query=query)

    return render_template("index.html", settings=settings)