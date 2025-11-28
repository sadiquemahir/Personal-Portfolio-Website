import reflex as rx
from app.states.resume_state import ResumeState


def glowing_icon_button(icon: str, url: str) -> rx.Component:
    return rx.el.a(
        rx.icon(icon, class_name="w-6 h-6"),
        href=url,
        target="_blank",
        class_name="p-3 bg-white/10 hover:bg-white/20 text-white rounded-full transition-all duration-300 hover:scale-110 hover:shadow-[0_0_15px_rgba(167,139,250,0.5)] border border-white/10 backdrop-blur-sm",
    )


def hero_stat(icon: str, text: str) -> rx.Component:
    return rx.el.div(
        rx.icon(icon, class_name="w-5 h-5 text-cyan-400 mr-2"),
        rx.el.span(text, class_name="text-slate-300 font-medium"),
        class_name="flex items-center bg-slate-800/50 px-4 py-2 rounded-full border border-slate-700/50 backdrop-blur-md",
    )


def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                class_name="absolute top-0 -left-4 w-72 h-72 bg-purple-500 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-blob"
            ),
            rx.el.div(
                class_name="absolute top-0 -right-4 w-72 h-72 bg-cyan-500 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-blob animation-delay-2000"
            ),
            rx.el.div(
                class_name="absolute -bottom-8 left-20 w-72 h-72 bg-indigo-500 rounded-full mix-blend-multiply filter blur-xl opacity-20 animate-blob animation-delay-4000"
            ),
            class_name="absolute inset-0 overflow-hidden pointer-events-none select-none",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        "HELLO, I'M",
                        class_name="text-cyan-400 font-bold tracking-[0.2em] uppercase text-sm mb-4 block animate-fade-in",
                    ),
                    rx.el.h1(
                        ResumeState.name,
                        class_name="text-5xl sm:text-7xl md:text-8xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-white via-slate-200 to-slate-400 mb-6 tracking-tight animate-fade-in-up drop-shadow-lg",
                    ),
                    rx.el.h2(
                        ResumeState.title,
                        class_name="text-2xl sm:text-3xl md:text-4xl text-slate-300 font-light mb-8 animate-fade-in-up animation-delay-200",
                    ),
                    rx.el.p(
                        ResumeState.summary,
                        class_name="text-lg sm:text-xl text-slate-400 mb-10 leading-relaxed max-w-2xl mx-auto animate-fade-in-up animation-delay-200",
                    ),
                    rx.el.div(
                        hero_stat("map-pin", ResumeState.location),
                        hero_stat("mail", ResumeState.email),
                        class_name="flex flex-wrap justify-center gap-4 mb-12 animate-fade-in-up animation-delay-400",
                    ),
                    rx.el.div(
                        rx.el.button(
                            "Download Resume",
                            rx.icon(
                                "download",
                                class_name="w-5 h-5 ml-2 group-hover:animate-bounce",
                            ),
                            on_click=ResumeState.download_resume,
                            class_name="group relative inline-flex items-center px-8 py-4 text-base font-bold text-white bg-gradient-to-r from-indigo-600 to-purple-600 rounded-full overflow-hidden transition-all duration-300 hover:shadow-[0_0_20px_rgba(99,102,241,0.5)] hover:scale-105 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 focus:ring-offset-slate-900",
                        ),
                        rx.el.div(
                            rx.foreach(
                                ResumeState.social_links,
                                lambda link: glowing_icon_button(
                                    link["icon"], link["url"]
                                ),
                            ),
                            class_name="flex items-center gap-4",
                        ),
                        class_name="flex flex-col sm:flex-row items-center justify-center gap-6 animate-fade-in-up animation-delay-400",
                    ),
                    class_name="text-center max-w-4xl mx-auto z-10 relative",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-32 sm:py-48",
            ),
            class_name="relative z-10",
        ),
        id="hero",
        class_name="relative min-h-screen flex items-center justify-center overflow-hidden bg-slate-950",
    )