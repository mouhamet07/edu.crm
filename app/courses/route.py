from flask import render_template, request, redirect, url_for, flash
from Data.db import teachers
from . import courses_bp
from app.services.course_service import (
    add_course,
    list_courses,
    delete_course,
    assign_student_to_course,
    assign_teacher_to_course,
    search_courses,
    update_course,
    get_course_by_id,
    remove_student_from_course
)
from app.services.teacher_service import (list_teachers)
from app.services.student_service import (get_student_by_id, list_students)
from app.services.auth_service import login_required


@courses_bp.route("/courses")
@login_required
def index():
    return render_template(
        "courses/list.html",
        courses=list_courses()
    )


@courses_bp.route("/courses/create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        name = request.form.get("name")
        teacher_id = request.form.get("teacher")
        if teacher_id == "":
            teacher_id = None
        resultat = add_course(name, teacher_id)

        if resultat is None:
            flash(f"Le cours '{name}' existe déjà")
        else:
            flash(f"Le cours '{name}' a été ajouté avec succès")

        return redirect(url_for("courses.index"))

    return render_template(
        "courses/create.html",
        teachers=list_teachers()
    )


@courses_bp.route("/courses/delete/<int:id>")
@login_required
def delete(id):
    resultat = delete_course(id)
    if resultat:
        flash("Le cours a été supprimé avec succès")
    else:
        flash("Le cours n'a pas été trouvé")
    return redirect(url_for("courses.index"))


@courses_bp.route("/courses/assign", methods=["GET", "POST"])
@login_required
def assign():
    if request.method == "POST":
        student_id = int(request.form.get("student"))
        course_id = int(request.form.get("course"))
        resultat = assign_student_to_course(course_id, student_id)
        if resultat:
            flash("L'étudiant a été assigné au cours")
        else:
            flash("Impossible d'assigner l'étudiant")

        return redirect(url_for("courses.index"))

    return render_template(
        "courses/assign.html",
        students=list_students(),
        courses=list_courses()
    )

@courses_bp.route("/courses/assign-teacher", methods=["GET", "POST"])
@login_required
def assign_teacher():
    if request.method == "POST":
        course_id = int(request.form.get("course"))
        teacher_id = int(request.form.get("teacher"))
        result = assign_teacher_to_course(course_id, teacher_id)
        if result:
            flash("Enseignant assigné avec succès")
        else:
            flash("Erreur lors de l'assignation")
        return redirect(url_for("courses.index"))

    return render_template(
        "courses/assign_teacher.html",
        courses=list_courses(),
        teachers=list_teachers()
    )

@courses_bp.route("/courses/search")
@login_required
def search():
    mot = request.args.get("q", "")
    results = search_courses(mot)
    return render_template(
        "courses/list.html",
        courses=results
    )


@courses_bp.route("/courses/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit(id):
    course = get_course_by_id(id)
    if request.method == "POST":
        title = request.form.get("name")
        teacher_id = request.form.get("teacher")
        if teacher_id:
            teacher_id = int(teacher_id)
        else:
            teacher_id = None
        update_course(id, title, teacher_id)

        flash("Cours modifié")
        return redirect(url_for("courses.index"))

    return render_template(
        "courses/edit.html",
        course=course,
        teachers=list_teachers()
    )

@courses_bp.route("/courses/<int:id>")
@login_required
def detail(id):

    course = get_course_by_id(id)

    if not course:
        flash("Cours introuvable")
        return redirect(url_for("courses.index"))

    if course["teacher_id"]:
        teacher = teachers[course["teacher_id"] - 1]["name"]
    else:
        teacher = "Non assigné"

    
    students = []
    for sid in course["student_ids"]:
        student = get_student_by_id(sid)
        if student:
            students.append(student)

    return render_template(
        "courses/detail.html",
        course=course,
        teacher=teacher,
        students=students
    )

@courses_bp.route("/courses/<int:course_id>/remove-student/<int:student_id>")
@login_required
def remove_student(course_id, student_id):

    result = remove_student_from_course(course_id, student_id)

    if result:
        flash("Étudiant retiré")
    else:
        flash("Erreur")

    return redirect(url_for("courses.detail", id=course_id))