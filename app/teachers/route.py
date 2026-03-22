from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.teacher_service import add_teacher, list_teachers, delete_teacher, search_teachers, update_teacher, filter_teachers_by_speciality, get_teacher_courses, count_teacher_courses

teachers_bp = Blueprint('teachers', __name__, url_prefix='/teachers', template_folder='templates')


@teachers_bp.route('/')
def teachers_list():
    search = request.args.get('search', '').strip()
    speciality = request.args.get('speciality', '').strip()

    if search:
        teachers = search_teachers(search)
    else:
        teachers = list_teachers()

    if speciality:
        teachers = [t for t in teachers if t['speciality'].lower() == speciality.lower()]

    # Ajouter le nombre de cours pour chaque enseignant
    for teacher in teachers:
        teacher['course_count'] = count_teacher_courses(teacher['id'])

    return render_template('teachers/list.html', teachers=teachers, search_query=search, speciality_filter=speciality)


@teachers_bp.route('/create', methods=['GET', 'POST'])
def create_teacher():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        speciality = request.form.get('speciality', '').strip()

        if not name or not email or not speciality:
            flash('Tous les champs sont obligatoires', 'error')
            return render_template('teachers/create.html')

        teacher, error = add_teacher(name, email, speciality)
        if error:
            flash(error, 'error')
            return render_template('teachers/create.html')
        
        flash('Enseignant créé avec succès', 'success')
        return redirect(url_for('teachers.teachers_list'))

    return render_template('teachers/create.html')


@teachers_bp.route('/delete/<int:id>')
def delete_teacher_route(id):
    if delete_teacher(id):
        flash('Enseignant supprimé avec succès', 'success')
    else:
        flash('Erreur lors de la suppression', 'error')
    return redirect(url_for('teachers.teachers_list'))


@teachers_bp.route('/search', methods=['GET', 'POST'])
def search_teacher():
    results = []
    query = ''
    if request.method == 'POST':
        query = request.form.get('query', '').strip()
        if query:
            results = search_teachers(query)
            for teacher in results:
                teacher['course_count'] = count_teacher_courses(teacher['id'])
        else:
            flash('Veuillez entrer un terme de recherche', 'warning')
    return render_template('teachers/search.html', teachers=results, search_query=query)


@teachers_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_teacher(id):
    teacher = next((t for t in list_teachers() if t['id'] == id), None)
    if not teacher:
        flash('Enseignant non trouvé', 'error')
        return redirect(url_for('teachers.teachers_list'))
    
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        speciality = request.form.get('speciality', '').strip()
        
        if not name or not email or not speciality:
            flash('Tous les champs sont obligatoires', 'error')
            return render_template('teachers/edit.html', teacher=teacher)
        
        success, error = update_teacher(id, name, email, speciality)
        if error:
            flash(error, 'error')
            return render_template('teachers/edit.html', teacher=teacher)
        
        flash('Enseignant modifié avec succès', 'success')
        return redirect(url_for('teachers.teachers_list'))
    
    return render_template('teachers/edit.html', teacher=teacher)


@teachers_bp.route('/courses/<int:id>')
def teacher_courses(id):
    teacher = next((t for t in list_teachers() if t['id'] == id), None)
    if not teacher:
        return redirect(url_for('teachers.teachers_list'))
    
    courses = get_teacher_courses(id)
    return render_template('teachers/courses.html', teacher=teacher, courses=courses)
