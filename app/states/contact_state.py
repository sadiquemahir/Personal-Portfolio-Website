import reflex as rx


class ContactState(rx.State):
    is_submitting: bool = False

    @rx.event
    async def handle_submit(self, form_data: dict):
        self.is_submitting = True
        import asyncio

        await asyncio.sleep(1)
        name = form_data.get("name", "")
        email = form_data.get("email", "")
        if not name or not email:
            self.is_submitting = False
            yield rx.toast.error("Please fill in all required fields.", duration=3000)
            return
        self.is_submitting = False
        yield rx.toast.success(f"Thanks {name}! We'll be in touch soon.", duration=5000)