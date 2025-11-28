import reflex as rx
from app.states.contact_state import ContactState
from app.states.resume_state import ResumeState


def contact_form() -> rx.Component:
    return rx.el.form(
        rx.el.div(
            rx.el.div(
                rx.el.label(
                    "Name",
                    html_for="name",
                    class_name="block text-sm font-medium text-slate-400 mb-1",
                ),
                rx.el.input(
                    type="text",
                    name="name",
                    id="name",
                    placeholder="John Doe",
                    required=True,
                    class_name="w-full px-4 py-3 rounded-lg bg-slate-900 border border-slate-700 text-white placeholder-slate-500 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-colors",
                ),
                class_name="mb-6",
            ),
            rx.el.div(
                rx.el.label(
                    "Email",
                    html_for="email",
                    class_name="block text-sm font-medium text-slate-400 mb-1",
                ),
                rx.el.input(
                    type="email",
                    name="email",
                    id="email",
                    placeholder="john@example.com",
                    required=True,
                    class_name="w-full px-4 py-3 rounded-lg bg-slate-900 border border-slate-700 text-white placeholder-slate-500 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-colors",
                ),
                class_name="mb-6",
            ),
            rx.el.button(
                rx.cond(
                    ContactState.is_submitting,
                    rx.el.div(
                        rx.el.div(
                            class_name="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-2"
                        ),
                        "Sending...",
                        class_name="flex items-center",
                    ),
                    rx.el.div(
                        "Send Message",
                        rx.icon("send", class_name="w-4 h-4 ml-2"),
                        class_name="flex items-center",
                    ),
                ),
                type="submit",
                disabled=ContactState.is_submitting,
                class_name="w-full flex justify-center items-center px-6 py-3 border border-transparent text-base font-medium rounded-lg text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-70 disabled:cursor-not-allowed transition-all duration-200",
            ),
        ),
        on_submit=ContactState.handle_submit,
        reset_on_submit=True,
        class_name="bg-slate-800/50 backdrop-blur-sm p-8 rounded-2xl shadow-lg border border-slate-700",
    )


def contact_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Get in Touch", class_name="text-3xl font-bold text-white mb-4"
                    ),
                    rx.el.p(
                        "Interested in working together? Feel free to reach out for collaborations or just a friendly hello.",
                        class_name="text-lg text-slate-400 mb-8",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.div(
                                rx.icon("mail", class_name="w-6 h-6 text-indigo-400"),
                                class_name="w-12 h-12 bg-slate-800 rounded-lg flex items-center justify-center mr-4 border border-slate-700",
                            ),
                            rx.el.div(
                                rx.el.p(
                                    "Email me at", class_name="text-sm text-slate-500"
                                ),
                                rx.el.a(
                                    ResumeState.email,
                                    href=f"mailto:{ResumeState.email}",
                                    class_name="text-lg font-semibold text-white hover:text-indigo-400 transition-colors",
                                ),
                            ),
                            class_name="flex items-center mb-8",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.icon(
                                    "map-pin", class_name="w-6 h-6 text-indigo-400"
                                ),
                                class_name="w-12 h-12 bg-slate-800 rounded-lg flex items-center justify-center mr-4 border border-slate-700",
                            ),
                            rx.el.div(
                                rx.el.p(
                                    "Based in", class_name="text-sm text-slate-500"
                                ),
                                rx.el.p(
                                    ResumeState.location,
                                    class_name="text-lg font-semibold text-white",
                                ),
                            ),
                            class_name="flex items-center",
                        ),
                        class_name="mt-8",
                    ),
                    class_name="lg:pr-12 mb-12 lg:mb-0",
                ),
                rx.el.div(contact_form(), class_name="w-full"),
                class_name="grid grid-cols-1 lg:grid-cols-2 gap-12",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20",
        ),
        id="contact",
        class_name="bg-[#020617]",
    )