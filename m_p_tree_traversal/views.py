from django.views import View
from django.shortcuts import render
from m_p_tree_traversal.models import folder_file


class FileView(View):
    def get(self, request):
        return render(request, 'index.html', {"files": folder_file.objects.all()})
