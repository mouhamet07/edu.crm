students = [
    {
        "id": 1,
        "photo": "https://i.pravatar.cc/150?img=1",
        "name": "Aissatou Diallo",
        "email": "aissatou@email.com",
        "status": "actif",
        "active": True,
        "courses": []
    },
    {
        "id": 2,
        "photo": "https://i.pravatar.cc/150?img=2",
        "name": "Moussa Traore",
        "email": "moussa@email.com",
        "active": False,
        "courses": []
    },
    {
        "id": 3,
        "photo": "https://i.pravatar.cc/150?img=3",
        "name": "Fatou Ndiaye",
        "email": "fatou@email.com",
        "active": True,
        "courses": ["Maths"]
    },
    {
        "id": 4,
        "photo": "https://i.pravatar.cc/150?img=4",
        "name": "Fatoumata Ndione",
        "email": "fatoumata@email.com",
        "active": True,
        "courses": ["Python"]
    },
    {
        "id": 5,
        "photo": "https://i.pravatar.cc/150?img=5",
        "name": "Ousmane Ba",
        "email": "ousmane@email.com",
        "active": True,
        "courses": ["Maths", "Python"]
    }
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
        "student_ids": [1, 2]
    },
    {
        "id": 2,
        "title": "BD",
        "teacher_id": 2,
        "student_ids": [1]
    },
    {
        "id": 3,
        "title": "Réseaux",
        "teacher_id": 3,
        "student_ids": [3]
    }
]

student_courses = {}

users = {
    "admin": {
        "password": "passe",
        "role": "Administrateur"
    },
    "user": {
        "password": "passe",
        "role": "Utilisateur"
    }
}