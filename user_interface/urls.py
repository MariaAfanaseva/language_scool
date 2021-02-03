from user_interface.views import Views
view = Views()

urls = {
    '/': view.teachers_list_view,
    '/add_teacher/': view.add_teacher_view
}
