from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from enum import EnumType


class Badges(EnumType):

    OFFICE = "office"
    HYBRID = "hybrid"
    TEAMWORK = "team work"

    LEGACY = "legacy code"
    REFACTOR = "refactor"

    WORKLOAD = "workload"
    ORGANIZED = "Organization"
    DEADLINE = "deadlines"
    TIME = "time"

    PLANNING = "planning"
    CRITICAL = "critical"
    OPTIMIZER = "optimizer"


badges = {
    Badges.LEGACY: {"name": _("Legacy Code"), "description": "Maintain legacy code to keep old systems running efficiently."},
    Badges.REFACTOR: {"name": _("Refactor"), "description": "Improve and restructure code without disrupting business workflows."},
    Badges.WORKLOAD: {"name": _("Workload"), "description": "Handle tasks effectively to balance productivity and efficiency."},
    Badges.DEADLINE: {"name": _("Deadlines"), "description": "Deliver work on time while maintaining quality standards."},
    Badges.TEAMWORK: {"name": _("Teamwork"), "description": "Collaborate effectively with colleagues to achieve common goals."},
    Badges.HYBRID: {"name": _("Hybrid"), "description": "Adapt to both remote and in-office work environments seamlessly."},
    Badges.PLANNING: {"name": _("Planning"), "description": "Develop structured plans to streamline workflow and decision-making."},
    Badges.OFFICE: {"name": _("Office"), "description": "Effectively work and collaborate in an in-office or on-site setting."},
    Badges.OPTIMIZER: {"name": _("Workflow Optimizer"), "description": "Enhance processes to improve performance and reduce inefficiencies."},
    Badges.CRITICAL: {"name": _("Critical Transitions"), "description": "Manage and execute key changes without disrupting operations."},
    Badges.TIME: {"name": _("Time Management"), "description": "Prioritize and allocate time effectively to meet objectives."},
    Badges.ORGANIZED: {"name": _("Task Organization"), "description": "Maintain structured and efficient task management."},
}


links_list = [
    {"id": "intro", "name": _("Intro")},
    {"id": "experience", "name": _("Experience")},
    {"id": "skills", "name": _("Skills")},
    {"id": "projects", "name": _("Projects")},
    {"id": "education", "name": _("Education")},
    {"id": "contact", "name": _("Contact")},
]

summary = _("""I'm a versatile developer combining a solid background in accounting with strong programming skills my proficiency in Python, Django, and Odoo, along with experience in developing RESTful APIs and managing databases allows me to seamlessly bridge the gap between financial needs and software solutions """)

work_section = [
    {
        "header": _("Work Experience ( Technical )"),
        "items": [
            {
                "title": _("Full Stack Developer"),
                "from": "11/2023",
                "to": _("Present"),
                "company": _("PoultrySync"),
                "list_title": _("Responsible for"),
                "subjects": [
                    _("Optimization, troubleshooting and debugging of system to ensure stability and scalability."),
                    _("Designed and implemented custom features aligned with client needs, improving overall user experience."),
                    _("Focused on high-level planning and best practices to improve development team efficiently."),
                    _("Architected and developed RESTful APIs using Django REST Framework to support seamless integrations."),
                ],
                "badges": [
                    badges.get(Badges.PLANNING),
                    badges.get(Badges.WORKLOAD),
                    badges.get(Badges.DEADLINE),
                    badges.get(Badges.LEGACY),
                    badges.get(Badges.REFACTOR),
                    badges.get(Badges.TEAMWORK),
                    badges.get(Badges.HYBRID),
                ],
            },
            {
                "title": _("Backend Developer"),
                "from": "10/2022",
                "to": "04/2023",
                "company": _("Mighty Groups"),
                "list_title": _("Responsible for"),
                "subjects": [
                    _("Developed RESTful APIs using Django REST Framework."),
                    _("Troubleshot, debugged, and enhanced existing systems."),
                    _("Implemented custom features to meet project requirements."),
                    _("Collaborated with team members to deploy projects successfully."),
                    _("Designed ERDs and database schemas in coordination with the business team."),
                ],
                "badges": [
                    badges.get(Badges.LEGACY),
                    badges.get(Badges.REFACTOR),
                    badges.get(Badges.WORKLOAD),
                    badges.get(Badges.DEADLINE),
                    badges.get(Badges.TEAMWORK),
                    badges.get(Badges.HYBRID),
                ],
            },
        ],
    },
    {
        "header": _("Work Experience ( Non Technical )"),
        "items": [
            {
                "title": _("Expenses Accountant Specialist"),
                "from": "12/2019",
                "to": "03/2022",
                "company": _("German Lebanese For Industry (GLC)"),
                "list_title": _("Responsible for"),
                "subjects": [
                    _("Reviewing general ledger journal entries to the ERP system."),
                    _("Prepare and submit weekly/monthly reports."),
                ],
                "badges": [
                    badges.get(Badges.OPTIMIZER),
                    badges.get(Badges.WORKLOAD),
                    badges.get(Badges.DEADLINE),
                    badges.get(Badges.TEAMWORK),
                    badges.get(Badges.OFFICE),
                ],
            },
            {
                "title": _("Junior Accountant"),
                "from": "10/2018",
                "to": "10/2019",
                "company": _("KAM Egypt"),
                "list_title": _("Responsible for"),
                "subjects": [
                    _("Manage all accounting transactions and enter general ledger journal entries to the ERP odoo system."),
                ],
                "badges": [
                    badges.get(Badges.CRITICAL),
                    badges.get(Badges.WORKLOAD),
                    badges.get(Badges.ORGANIZED),
                    badges.get(Badges.TIME),
                    badges.get(Badges.OFFICE),
                ],
            },
        ],
    },
]
personal_skills_section = [
    {
        "header": _("Skills"),
        "items": [
            {"all": badges.values()},
            {"details": ""},
        ],
    },
]

tech_skills_section = [
    {
        "header": _("Tech Skills"),
        "items": [
            {"url": "https://www.python.org/", "image": "icons/python.svg", "name": "Python"},
            {"url": "https://www.djangoproject.com/", "image": "icons/django.svg", "name": "Django"},
            {"url": "https://www.django-rest-framework.org/", "image": "icons/djangorest.png", "name": "Django Rest Framework"},
            {"url": "https://htmx.org/", "image": "icons/htmx.png", "name": "HTMX"},
            {"url": "https://www.javascript.com/", "image": "icons/js.png", "name": "JavaScript"},
            {"url": "https://react.dev/", "image": "icons/react.svg", "name": "React"},
            {"url": "https://html.spec.whatwg.org/", "image": "icons/html.png", "name": "HTML"},
            {"url": "https://www.w3.org/Style/CSS/", "image": "icons/css.png", "name": "CSS"},
            {"url": "https://getbootstrap.com/", "image": "icons/bootstrap.png", "name": "Bootstrap"},
            {"url": "https://www.mysql.com/", "image": "icons/mysql.png", "name": "MySQL"},
            {"url": "https://www.postgresql.org/", "image": "icons/postgresq.svg", "name": "PostgreSQL"},
            {"url": "https://www.gnu.org/software/bash/", "image": "icons/bash.svg", "name": "BASH"},
            {"url": "https://www.odoo.com/", "image": "icons/odoo.png", "name": "Odoo"},
            {"url": "https://www.docker.com/", "image": "icons/docker.png", "name": "Docker"},
            {"url": "https://git-scm.com/", "image": "icons/git.png", "name": "Git"},
        ],
    },
]

education_section = [
    {
        "header": _("Education"),
        "items": [
            {
                "title": _("Full Stack using Python"),
                "from": "3/2022",
                "to": "9/2022",
                "company": _("ITI ( Information Technology Institute )"),
                "list_title": _("Subjects"),
                "subjects": [
                    _("Programming Fundamentals."),
                    _("Intro to Web Development + hands on experience."),
                    _("Advanced topics and tips for Web Development optimizations"),
                    _("Graduation Project + project for every sub track."),
                ],
            },
            {
                "title": _("Bachelor's In Accounting"),
                "from": "2012",
                "to": "2016",
                "company": _("Faculty Of Commerce Ain Shams University"),
                "list_title": _("Subjects"),
                "subjects": [
                    _("Accounting & Finance."),
                    _("Business & Management."),
                    _("Economics."),
                ],
            },
        ],
    },
    {
        "header": _("Certificates"),
        "items": [
            {
                "title": _("React Development Cross-Skilling Nanodegree Program"),
                "from": "9/2022",
                "to": "11/2022",
                "company": _("Udacity"),
                "list_title": _("Subjects"),
                "subjects": [
                    _("React Fundamentals."),
                    _("Advanced tips and tricks."),
                ],
            },
            {
                "title": _("Dart & Flutter"),
                "from": "2020",
                "to": "2020",
                "company": _("IT Share"),
                "list_title": _("Subjects"),
                "subjects": [
                    _("Dart & Flutter Fundamentals."),
                    _("4 Hands on projects."),
                ],
            },
            {
                "title": _("Professional Financial Accountant"),
                "from": "2018",
                "to": "2018",
                "company": _("Cairo University"),
                "list_title": _("Subjects"),
                "subjects": [
                    _("Advanced Accounting."),
                ],
            },
        ],
    },
]


projects_section = [
    {
        "header": _("Projects"),
        "items": [
            {
                "title": _("Orders Manager"),
                "stack": ["Django", "HTMX"],
                "summary": "If you're still collecting food orders manually, it's time to try Orders Manager!",
                "git": "https://github.com/hosamhamdy258/orders-manager",
                "live": "https://hosamhamdy.koyeb.app/",
            },
            {
                "title": _("Darajaty"),
                "stack": ["Django", "React"],
                "summary": "Tired of boring quizzes? With Darajaty, every question you answer, add, or review comes with rewards! Make learning engaging and fun.",
                "git": "https://github.com/hosamhamdy258/darajaty",
                "live": "https://darajaty.pythonanywhere.com/",
            },
            {
                "title": _("Shortener"),
                "stack": ["Django"],
                "summary": "Simple Url Shortener to cut long urls",
                "git": "https://github.com/hosamhamdy258/shortener",
                "live": "https://hhshortener.pythonanywhere.com",
            },
        ],
    }
]
contact_section = [
    {
        "header": _("Contact Info"),
        "items": [
            {"type": "tel", "name": "Mobile", "target": "+201015434803", "icon": "fa-solid fa-phone fa-2xl", "color": "#1ae03e"},
            {"type": "mail", "name": "Mail", "target": "hosamhamdy258@gmail.com", "icon": "fa-solid fa-envelope fa-2xl", "color": "#ffbd07"},
            {"type": "link", "name": "Github", "target": "https://github.com/hosamhamdy258", "icon": "fa-brands fa-github fa-2xl", "color": "#000000;"},
            {"type": "link", "name": "Linkedin", "target": "https://www.linkedin.com/in/hossamhamdy94/", "icon": "fa-brands fa-linkedin fa-2xl", "color": "#0a66c2"},
            {"type": "link", "name": "Website", "target": "https://dev-hosamhamdy.github.io", "icon": "fa-solid fa-globe fa-2xl", "color": "#63E6BE"},
        ],
    }
]


def index(request):
    context = {
        "title": _("Hossam Hamdy"),
        "links_list": links_list,
        "summary": summary,
        "work_section": work_section,
        "personal_skills_section": personal_skills_section,
        "tech_skills_section": tech_skills_section,
        "education_section": education_section,
        "projects_section": projects_section,
        "contact_section": contact_section,
    }
    return render(request, "base.html", context)



