students = [
    {"id": 1, "name": "Aissatou Diallo", "email": "aissatou@email.com","active": True,"courses": ["Maths", "Python"]},
    {"id": 2, "name": "Moussa Traore", "email": "moussa@email.com","active": True,"courses": ["Python"]},
    {"id": 3, "name": "Fatou Ndiaye", "email": "fatou@email.com","active": False,"courses": []},
    {"id": 4, "name": "Fatoumata Ndione", "email": "fatoumata@email.com","active": True,"courses": ["Maths"]}
]

teachers = [
    {"id": 1, "name": "Diallo", "email": "diallo@gmail.com", "speciality": "Dev", "courses": ["Algo", "Python"]},
    {"id": 2, "name": "Sow", "email": "sow@gmail.com", "speciality": "Base de donnees", "courses": []},
    {"id": 3, "name": "Barry", "email": "barry@gmail.com", "speciality": "Dev", "courses": []},
    {"id": 4, "name": "Camara", "email": "camara@gmail.com", "speciality": "Reseaux", "courses": []}
]

courses = [
    {
        "id": 1,
        "title": "Algo",
        "teacher_id": 1,
        "student_ids": []
    },
    {
        "id": 2,
        "title": "BD",
        "teacher_id": 2,
        "student_ids": []
    },
    {
        "id": 3,
        "title": "Réseaux",
        "teacher_id": 3,
        "student_ids": []
    }
]

student_courses = {}

users = {
    "admin": "passe"
}