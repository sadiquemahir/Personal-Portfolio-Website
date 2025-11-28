import reflex as rx
from app.states.resume_state import ResumeState


class NavbarState(rx.State):
    mobile_menu_open: bool = False

    @rx.event
    def toggle_menu(self):
        self.mobile_menu_open = not self.mobile_menu_open

    @rx.event
    def close_menu(self):
        self.mobile_menu_open = False


def nav_link(text: str, target_id: str) -> rx.Component:
    return rx.el.a(
        text,
        on_click=rx.scroll_to(target_id),
        class_name="text-slate-300 hover:text-cyan-400 font-medium transition-colors cursor-pointer hover:drop-shadow-lg",
    )


def mobile_nav_link(text: str, target_id: str) -> rx.Component:
    return rx.el.a(
        text,
        on_click=[rx.scroll_to(target_id), NavbarState.close_menu],
        class_name="block px-3 py-2 rounded-md text-base font-medium text-slate-300 hover:text-cyan-400 hover:bg-slate-800 cursor-pointer",
    )


def navbar() -> rx.Component:
    return rx.el.nav(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            "MS",
                            class_name="text-xl font-bold text-white bg-gradient-to-br from-indigo-600 to-purple-600 rounded-lg w-10 h-10 flex items-center justify-center shadow-lg shadow-indigo-500/30",
                        ),
                        rx.el.span(
                            ResumeState.name,
                            class_name="ml-3 text-xl font-bold text-slate-100 tracking-tight hover:text-cyan-400 transition-colors duration-300",
                        ),
                        class_name="flex-shrink-0 flex items-center cursor-pointer",
                        on_click=rx.scroll_to("hero"),
                    ),
                    rx.el.div(
                        rx.el.div(
                            nav_link("Home", "hero"),
                            nav_link("Skills", "skills"),
                            nav_link("Experience", "experience"),
                            nav_link("Projects", "projects"),
                            nav_link("Contact", "contact"),
                            class_name="ml-10 flex items-baseline space-x-8",
                        ),
                        class_name="hidden md:block",
                    ),
                    rx.el.div(
                        rx.el.button(
                            rx.cond(
                                NavbarState.mobile_menu_open,
                                rx.icon("x", class_name="h-6 w-6 text-slate-300"),
                                rx.icon("menu", class_name="h-6 w-6 text-slate-300"),
                            ),
                            on_click=NavbarState.toggle_menu,
                            class_name="inline-flex items-center justify-center p-2 rounded-md text-slate-400 hover:text-white hover:bg-slate-800 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-cyan-500",
                        ),
                        class_name="-mr-2 flex md:hidden",
                    ),
                ),
                class_name="flex items-center justify-between h-16",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
        ),
        rx.el.div(
            rx.el.div(
                mobile_nav_link("Home", "hero"),
                mobile_nav_link("Skills", "skills"),
                mobile_nav_link("Experience", "experience"),
                mobile_nav_link("Projects", "projects"),
                mobile_nav_link("Contact", "contact"),
                class_name="px-2 pt-2 pb-3 space-y-1 sm:px-3 bg-slate-900/95 shadow-xl rounded-b-lg border-t border-slate-800",
            ),
            class_name=rx.cond(
                NavbarState.mobile_menu_open,
                "block md:hidden absolute w-full z-50",
                "hidden md:hidden",
            ),
        ),
        class_name="glass-nav sticky top-0 z-50 border-b border-white/10",
    )