import reflex as rx
from app.states.resume_state import ResumeState


def experience_item(item: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                class_name="absolute w-4 h-4 bg-indigo-500 rounded-full -left-[9px] top-1.5 border-4 border-slate-900 shadow-sm ring-1 ring-indigo-500/50"
            ),
            class_name="absolute left-0 top-0 bottom-0 w-px bg-slate-800 md:static md:w-auto md:bg-transparent md:block hidden",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    item["duration"],
                    class_name="inline-block px-3 py-1 mb-2 text-xs font-semibold tracking-wider text-indigo-300 uppercase bg-indigo-900/30 border border-indigo-500/30 rounded-full",
                ),
                rx.el.h3(item["role"], class_name="text-xl font-bold text-white"),
                rx.el.div(
                    rx.el.span(
                        item["company"], class_name="font-medium text-slate-300"
                    ),
                    rx.el.span(" • ", class_name="text-slate-600 mx-2"),
                    rx.el.span(item["location"], class_name="text-slate-500 text-sm"),
                    class_name="flex flex-wrap items-center mb-4",
                ),
                rx.el.ul(
                    rx.foreach(
                        item["description"],
                        lambda d: rx.el.li(
                            d,
                            class_name="relative pl-4 before:content-['•'] before:absolute before:left-0 before:text-indigo-400",
                        ),
                    ),
                    class_name="space-y-2 text-slate-400",
                ),
                class_name="bg-slate-800/50 backdrop-blur-sm p-6 rounded-xl border border-slate-700 shadow-lg hover:border-indigo-500/50 transition-colors duration-200",
            ),
            class_name="ml-6 md:ml-8 mb-8",
        ),
        class_name="relative border-l border-slate-800 last:border-0",
    )


def education_card(edu: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("school", class_name="w-8 h-8 text-indigo-400 mb-4"),
            rx.el.h3(edu["degree"], class_name="text-lg font-bold text-white mb-2"),
            rx.el.div(
                rx.el.p(edu["institution"], class_name="text-slate-300 font-medium"),
                rx.el.p(edu["location"], class_name="text-slate-500 text-sm"),
                class_name="mb-3",
            ),
            rx.el.span(
                edu["year"],
                class_name="inline-block text-sm text-indigo-300 font-medium bg-indigo-900/30 border border-indigo-500/30 px-2 py-1 rounded mb-4",
            ),
            rx.cond(
                edu["coursework"],
                rx.el.div(
                    rx.el.span(
                        "Relevant Coursework: ",
                        class_name="font-semibold text-slate-300 text-sm",
                    ),
                    rx.el.span(
                        edu["coursework"], class_name="text-slate-400 text-sm italic"
                    ),
                    class_name="mt-2 border-t border-slate-700 pt-3",
                ),
                rx.fragment(),
            ),
            class_name="h-full",
        ),
        class_name="bg-slate-800/50 backdrop-blur-sm p-6 rounded-xl border border-slate-700 hover:border-indigo-500/30 transition-all duration-300 h-full",
    )


def experience_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Professional Experience",
                    class_name="text-3xl font-bold text-white mb-4",
                ),
                rx.el.p(
                    "My career journey and key achievements in the tech industry.",
                    class_name="text-lg text-slate-400 max-w-2xl mb-12",
                ),
                class_name="text-center sm:text-left",
            ),
            rx.el.div(
                rx.el.div(
                    rx.foreach(ResumeState.experience, experience_item),
                    class_name="max-w-3xl",
                ),
                class_name="mb-20",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Education", class_name="text-2xl font-bold text-white mb-8"
                    ),
                    class_name="mb-8 border-b border-slate-800 pb-4",
                ),
                rx.el.div(
                    rx.foreach(ResumeState.education, education_card),
                    class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
                ),
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20",
        ),
        id="experience",
        class_name="bg-[#020617]",
    )