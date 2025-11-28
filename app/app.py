import reflex as rx
from app.components.navbar import navbar
from app.components.hero import hero
from app.components.footer import footer
from app.components.skills import skills_section
from app.components.experience import experience_section
from app.components.projects import projects_section
from app.components.contact import contact_section
from app.states.resume_state import ResumeState


def index() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            hero(),
            skills_section(),
            experience_section(),
            projects_section(),
            contact_section(),
            class_name="flex-grow",
        ),
        footer(),
        class_name="font-['Inter'] min-h-screen flex flex-col bg-[#020617] text-slate-100 selection:bg-indigo-500 selection:text-white",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap",
        "/styles.css",
    ],
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
    ],
)
app.add_page(index, route="/", on_load=ResumeState.load_resume_data)