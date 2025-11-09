from django.shortcuts import render

def home(request):
    message = {
        "type": 'success',
        'title': "Welcome Back!",
        "text": "You have successfully logged in."
    }

    context = {
        'user_name': "Giorgi",
        "is_admin": True,
        "message": message,
    }

    return render(request, "templates_app/home.html", context)

def about(request):
    return render(request, 'templates_app/about.html')

def posts(request):
    sample_posts = [
        {'title': "First Post", 'date': '2025-04-05'},
        {'title': "Second Post", 'date': '2025-04-24'},
    ]

    context = {
        "posts": sample_posts,
    }

    return render(request, 'templates_app/posts.html', context)
