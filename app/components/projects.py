import reflex as rx
from app.states.resume_state import ResumeState, Project, Certificate, TechStackItem


def tech_badge(tech: str) -> rx.Component:
    return rx.el.span(
        tech,
        class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-slate-900 text-slate-300 border border-slate-700 shadow-sm",
    )


def project_card(project: Project) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(
                    project["icon"],
                    class_name="w-16 h-16 text-indigo-400 opacity-90 group-hover:scale-110 transition-transform duration-300 drop-shadow-lg",
                ),
                class_name="w-full h-56 bg-gradient-to-br from-[#1e1e2f] to-[#2d2d44] flex items-center justify-center transition-colors duration-300 group-hover:from-[#25253a] group-hover:to-[#363652] relative",
            ),
            class_name="relative overflow-hidden",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    project["title"], class_name="text-2xl font-bold text-white mb-3"
                ),
                rx.el.p(
                    project["description"],
                    class_name="text-slate-400 text-sm mb-6 leading-relaxed line-clamp-4",
                ),
                rx.el.div(
                    rx.foreach(project["technologies"], tech_badge),
                    class_name="flex flex-wrap gap-2 mb-6",
                ),
            ),
            rx.el.div(
                rx.el.a(
                    rx.icon(
                        "github",
                        class_name="w-5 h-5 mr-2 group-hover:text-white transition-colors",
                    ),
                    "Code",
                    href=project["github_url"],
                    target="_blank",
                    class_name="inline-flex items-center text-sm font-medium text-slate-400 hover:text-white transition-colors px-4 py-2 rounded-lg hover:bg-slate-800",
                ),
                rx.el.a(
                    rx.icon("external-link", class_name="w-5 h-5 mr-2"),
                    "Live Demo",
                    href=project["demo_url"],
                    target="_blank",
                    class_name="inline-flex items-center text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-500 transition-colors px-4 py-2 rounded-lg shadow-lg shadow-indigo-600/20",
                ),
                class_name="flex items-center justify-between pt-4 border-t border-slate-700/50",
            ),
            class_name="p-8 flex flex-col flex-grow justify-between bg-[#151525]",
        ),
        class_name="group bg-[#151525] rounded-2xl overflow-hidden border border-slate-800 shadow-xl hover:shadow-2xl hover:shadow-indigo-500/10 hover:border-indigo-500/30 transition-all duration-300 flex flex-col h-full transform hover:-translate-y-1",
    )


def filter_button(category: str) -> rx.Component:
    return rx.el.button(
        category,
        on_click=lambda: ResumeState.set_category(category),
        class_name=rx.cond(
            ResumeState.selected_category == category,
            "px-5 py-2 rounded-full text-sm font-bold bg-indigo-600 text-white shadow-lg shadow-indigo-600/25 transition-all duration-200",
            "px-5 py-2 rounded-full text-sm font-medium bg-[#1e1e2f] text-slate-400 hover:bg-slate-800 hover:text-white border border-slate-700/50 hover:border-slate-600 transition-all duration-200",
        ),
    )


def tab_button(tab_name: str) -> rx.Component:
    return rx.el.button(
        rx.el.span(
            tab_name,
            class_name=rx.cond(
                ResumeState.active_tab == tab_name,
                "relative z-10 flex items-center gap-2 text-white",
                "relative z-10 flex items-center gap-2 text-slate-400 group-hover:text-white",
            ),
        ),
        rx.cond(
            ResumeState.active_tab == tab_name,
            rx.el.div(
                class_name="absolute inset-0 bg-gradient-to-r from-indigo-600 to-purple-600 rounded-xl shadow-lg opacity-100 transition-opacity duration-300"
            ),
            None,
        ),
        on_click=lambda: ResumeState.set_tab(tab_name),
        class_name="relative px-8 py-3 text-sm font-bold transition-all duration-300 ease-in-out overflow-hidden group",
    )


def certificate_card(cert: Certificate) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(cert["icon"], class_name="w-10 h-10 text-indigo-400"),
            class_name="w-20 h-20 rounded-2xl bg-slate-800/50 flex items-center justify-center mb-6 group-hover:bg-indigo-900/30 transition-colors border border-slate-700 group-hover:border-indigo-500/30",
        ),
        rx.el.h3(cert["title"], class_name="text-xl font-bold text-white mb-2"),
        rx.el.p(cert["issuer"], class_name="text-slate-400 font-medium mb-3"),
        rx.el.span(
            cert["date"],
            class_name="inline-block px-3 py-1 text-xs font-bold tracking-wide text-indigo-300 bg-indigo-900/20 border border-indigo-500/20 rounded-lg",
        ),
        class_name="bg-[#151525] p-8 rounded-2xl border border-slate-800 shadow-xl hover:shadow-2xl hover:shadow-indigo-500/10 hover:border-indigo-500/30 transition-all duration-300 group h-full transform hover:-translate-y-1",
    )


def tech_stack_card(item: TechStackItem) -> rx.Component:
    return rx.el.div(
        rx.icon(
            item["icon"],
            class_name=f"w-16 h-16 mb-6 transition-transform duration-300 group-hover:scale-110 group-hover:rotate-3 {item['color']}",
        ),
        rx.el.h3(
            item["name"], class_name="text-lg font-bold text-white text-center mb-1"
        ),
        rx.el.span(
            item["category"],
            class_name="text-xs font-medium text-slate-500 uppercase tracking-wider",
        ),
        class_name="flex flex-col items-center justify-center p-8 bg-[#151525] rounded-2xl border border-slate-800 shadow-lg hover:shadow-2xl hover:shadow-indigo-500/10 hover:border-indigo-500/30 transition-all duration-300 group h-full transform hover:-translate-y-2",
    )


def projects_view() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.foreach(ResumeState.project_categories, filter_button),
            class_name="flex flex-wrap gap-3 mb-12 justify-center",
        ),
        rx.el.div(
            rx.foreach(ResumeState.filtered_projects, project_card),
            class_name="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-5xl mx-auto",
        ),
    )


def certificates_view() -> rx.Component:
    return rx.el.div(
        rx.foreach(ResumeState.certificates, certificate_card),
        class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6",
    )


def tech_stack_view() -> rx.Component:
    return rx.el.div(
        rx.foreach(ResumeState.tech_stack_items, tech_stack_card),
        class_name="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-6",
    )


def projects_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "PORTFOLIO",
                    class_name="text-indigo-500 font-bold tracking-[0.2em] uppercase text-sm mb-3 block animate-fade-in",
                ),
                rx.el.h2(
                    "Showcase",
                    class_name="text-4xl md:text-5xl font-bold text-white mb-6 tracking-tight",
                ),
                rx.el.p(
                    "Explore my journey through projects, certifications, and technical expertise. Each section represents a milestone in my continuous learning path.",
                    class_name="text-lg text-slate-400 max-w-2xl mx-auto mb-12 leading-relaxed",
                ),
                class_name="text-center mb-12",
            ),
            rx.el.div(
                rx.el.div(
                    rx.foreach(ResumeState.portfolio_tabs, tab_button),
                    class_name="inline-flex p-1.5 bg-[#0f0f1a] rounded-2xl border border-slate-800/50 shadow-inner",
                ),
                class_name="flex justify-center mb-16",
            ),
            rx.el.div(
                rx.match(
                    ResumeState.active_tab,
                    ("Projects", projects_view()),
                    ("Certificates", certificates_view()),
                    ("Tech Stack", tech_stack_view()),
                    projects_view(),
                ),
                class_name="min-h-[400px] animate-fade-in-up",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24",
        ),
        id="projects",
        class_name="bg-[#020617] relative",
    )