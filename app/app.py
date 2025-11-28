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
        rx.el.link(rel="icon", href="/favicon.ico", type="image/x-icon"),
        rx.el.meta(
            name="description",
            content="Portfolio of Mahir Sadique, a Software Engineer specializing in full-stack development, robotics, and AI. Explore projects, skills, and experience.",
        ),
        rx.el.meta(name="author", content="Mahir Sadique"),
        rx.el.meta(
            name="keywords",
            content="software engineer, full stack developer, robotics, AI, python, react, svelte, portfolio, Mahir Sadique",
        ),
        rx.el.meta(
            property="og:title", content="Mahir Sadique | Software Engineer Portfolio"
        ),
        rx.el.meta(
            property="og:description",
            content="Portfolio of Mahir Sadique, a Software Engineer specializing in full-stack development, robotics, and AI.",
        ),
        rx.el.meta(property="og:type", content="website"),
    ],
)
app.add_page(
    index,
    route="/",
    on_load=ResumeState.load_resume_data,
    title="Mahir Sadique | Software Engineer Portfolio",
)