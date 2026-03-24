from flask import render_template, redirect, url_for, session
from app.services.auth_service import login_required
from app.dashboard import dashboard_bp
from app.services.dashboard_service import (
    get_total_students,
    get_total_teachers,
    get_total_courses,
    get_recent_courses,
    get_recent_students
)


@dashboard_bp.route("/dashboard")
@login_required
def index():
    if "user" not in session:
        return redirect(url_for("auth.login"))

    total_students = get_total_students()
    total_teachers = get_total_teachers()
    total_courses = get_total_courses()
    recent_courses = get_recent_courses()

    recent_students = get_recent_students()

    return render_template(
        "dashboard/dashboard.html",
        total_students=total_students,
        total_teachers=total_teachers,
        total_courses=total_courses,
        recent_courses=recent_courses,
        students=recent_students
    )