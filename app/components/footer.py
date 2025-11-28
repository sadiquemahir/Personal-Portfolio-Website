import reflex as rx
from app.states.resume_state import ResumeState


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        "MS",
                        class_name="text-lg font-bold text-white bg-gradient-to-br from-indigo-600 to-purple-600 rounded-md w-8 h-8 flex items-center justify-center shadow-lg shadow-indigo-500/20",
                    ),
                    rx.el.p(
                        "Building digital experiences that matter.",
                        class_name="ml-3 text-slate-500 text-sm font-medium",
                    ),
                    class_name="flex items-center mb-4 md:mb-0",
                ),
                rx.el.div(
                    rx.el.p(
                        f"© 2024 {ResumeState.name}. All rights reserved.",
                        class_name="text-slate-500 text-sm",
                    ),
                    class_name="flex flex-col md:flex-row items-center gap-4",
                ),
                class_name="flex flex-col md:flex-row justify-between items-center",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8",
        ),
        class_name="bg-[#020617] border-t border-slate-800 mt-auto",
    )