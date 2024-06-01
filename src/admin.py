from sqladmin import Admin, ModelView
from src.database import engine
from src.books.models import Book


def init_admin_page(app):
    admin = Admin(app, engine)

    class AdminBooks(ModelView, model=Book):
        icon = "fa-solid fa-book"
        column_list = [Book.id, Book.title]

    admin.add_view(AdminBooks)
