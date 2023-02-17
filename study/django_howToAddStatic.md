To add static files in a Django project, you need to follow these steps:

1. Create a directory to hold your static files: In your Django project directory, create a new directory called "static" to hold your static files. Within the "static" directory, create subdirectories for each app that will contain static files. For example, if you have an app named "blog," create a subdirectory called "blog" within the "static" directory.

2. Define STATIC_URL in settings.py: In your project's settings.py file, define the STATIC_URL variable to specify the URL where static files will be served. For example, you could set STATIC_URL to '/static/'.

3. Update STATICFILES_DIRS: In the same settings.py file, you need to define the STATICFILES_DIRS variable to tell Django where to find your static files. For example, if your static files are located in a directory named "static" within each app, you could define STATICFILES_DIRS like this:

```py
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
```

4. Load the static files in your templates: In your HTML templates, use the {% load static %} template tag to load the static files. For example, to load a CSS file named "styles.css" located in the "static/css" directory of your app, you would use the following code:

```py
{% load static %}
<link rel="stylesheet" type="text/css" href="{% static 'css/styles.css' %}">
```

Note that the path argument to the {% static %} tag is relative to your STATICFILES_DIRS.

5. Collect static files for production: When you are ready to deploy your Django project to production, you need to run the "collectstatic" management command to collect all static files from your apps into a single directory. For example, you could run the following command:

```py
python manage.py collectstatic
```

This will copy all the static files to the directory specified in the STATIC_ROOT variable, which you need to define in your settings.py file.
