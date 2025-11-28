import reflex as rx
from app.states.resume_state import ResumeState


def skill_badge(skill: str) -> rx.Component:
    return rx.el.span(
        skill,
        class_name="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-indigo-900/30 text-indigo-200 border border-indigo-500/30 hover:bg-indigo-900/50 hover:border-indigo-500/50 transition-colors duration-200",
    )


def skill_category_card(category: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                category["name"], class_name="text-lg font-semibold text-white mb-4"
            ),
            rx.el.div(
                rx.foreach(category["skills"], skill_badge),
                class_name="flex flex-wrap gap-2",
            ),
            class_name="h-full",
        ),
        class_name="bg-slate-800/50 backdrop-blur-sm p-6 rounded-xl shadow-lg border border-slate-700 hover:shadow-indigo-500/20 hover:border-indigo-500/30 transition-all duration-200 h-full",
    )


def skills_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Skills & Expertise",
                    class_name="text-3xl font-bold text-white mb-4",
                ),
                rx.el.p(
                    "A comprehensive overview of my technical abilities and professional competencies.",
                    class_name="text-lg text-slate-400 max-w-2xl",
                ),
                class_name="mb-12 text-center sm:text-left",
            ),
            rx.el.div(
                rx.foreach(ResumeState.skills_categories, skill_category_card),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20",
        ),
        id="skills",
        class_name="bg-[#020617]",
    )