# from django.shortcuts import render
# from django.http import HttpResponse
#
# # Create your views here.
#
# posts = [
#     {
#         "title": "Blog post 1",
#         "Author": "Alphonso",
#         "date" : "19th december"
#     },
#     {
#         "title": "Blog post 2",
#         "Author": "sandy",
#         "date": "20th december"
#     }
# ]
#
#
# def homepage(request):
#     context = {
#         "posts" : posts
#     }
#     return render(request, 'home.html', context)
#
# def about(request):
#     return render(request, 'about.html', {'title': 'about'})
#
# def basepage(request):
#     return  render(request, 'base.html')