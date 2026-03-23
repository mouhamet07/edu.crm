students = [
    {
        "id": 1,
        "photo": "https://i.pravatar.cc/150?img=1",
        "name": "Aissatou Diallo",
        "email": "aissatou@email.com",
        "status": "actif"
    },
    {
        "id": 2,
        "photo": "https://i.pravatar.cc/150?img=2",
        "name": "Moussa Traore",
        "email": "moussa@email.com",
        "status": "actif"
    },
    {
        "id": 3,
        "photo": "https://i.pravatar.cc/150?img=3",
        "name": "Fatou Ndiaye",
        "email": "fatou@email.com",
        "status": "actif"
    },
    {
        "id": 4,
        "photo": "https://i.pravatar.cc/150?img=4",
        "name": "Fatoumata Ndione",
        "email": "fatoumata@email.com",
        "status": "actif"
    },
    {
        "id": 5,
        "photo": "https://i.pravatar.cc/150?img=5",
        "name": "Ousmane Ba",
        "email": "ousmane@email.com",
        "status": "actif"
    }
]

teachers = [
    {"id": 1, "name": "Diallo", "email": "diallo@gmail.com", "speciality": "Dev"},
    {"id": 2, "name": "Sow", "email": "sow@gmail.com", "speciality": "Base de donnees"},
    {"id": 3, "name": "Barry", "email": "barry@gmail.com", "speciality": "Dev"},
    {"id": 4, "name": "Camara", "email": "camara@gmail.com", "speciality": "Reseaux"}
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
        "role": "admin"
    },
    "mouhamet": {
        "password": "passe",
        "role": "user"
    }
}