from fastapi.responses import RedirectResponse
from sqladmin import Admin, ModelView, action
from fastapi import Request
from src.database import engine
from src.books.models import Book


def init_admin_page(app):
    admin = Admin(app, engine)

    class AdminBooks(ModelView, model=Book):
        icon = "fa-solid fa-book"
        can_delete = False
        column_list = [Book.id, Book.title, Book.author]
        column_searchable_list = [Book.title, Book.author]
        column_sortable_list = [Book.id, Book.title, Book.author]

        @action(
            name="custom_action",
            label="Custom action",
            confirmation_message="Are you sure?",
            add_in_detail=True,
            add_in_list=True,
        )
        async def approve_users(self, request: Request):
            if pks := request.query_params.get("pks", "").split(","):
                for pk in pks:
                    model: Book = await self.get_object_for_details(pk)
                    print(model)

            referer = request.headers.get("Referer")
            if referer:
                return RedirectResponse(referer)
            else:
                return RedirectResponse(request.url_for("admin:list", identity=self.identity))

    admin.add_view(AdminBooks)
