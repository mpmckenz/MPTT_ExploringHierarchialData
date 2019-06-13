#Modified Preorder Tree Traversal (MPTT)

MPTT is a tool used to help manage hierarchical data in a CMS. It can be used to help streamline to process of slow database queries. This makes most tree operations much cheaper in terms of queries.

##Steps to use MPTT in your Django project:

1. add '''mptt''' to '''INSTALLED_APPS''' in your '''settings.py'''
2. Set up your model with a subclass of MPTTModel
   2a. Must define a parent field that inherits '''self''' in order to render form fields differently in the admin
   '''parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')'''
3. Add some test data, make a view, and HTML template for it
4. a simple urls.py should look similar to this
   '''
   from django.urls import path
   from m_p_tree_traversal.views import FileView
   from django.contrib import admin
   from mptt.admin import DraggableMPTTAdmin
   from m_p_tree_traversal.models import folder_file


    admin.site.register(folder_file, DraggableMPTTAdmin)
    urlpatterns = [
        path('admin/', admin.site.urls),
        path("", FileView.as_view()),
    ]
    '''
