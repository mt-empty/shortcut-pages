# Django Cheatsheet

> Source: https://docs.djangoproject.com/en/1.9/

> Aliases: django-admin, django-query, django-lookups, python-django, django-queryset, pydjango

$ Django Admin/Manage.py Commands
    `django-admin help             {{display usage information and a list of the commands provided by each application}} 
    `django-admin help --commands  {{display a list of all available commands}} 
    `django-admin help <command>   {{display  description of command}} 
    `django-admin version          {{show version}} 
    `django-admin check            {{inspect the entire Django project for common problems}} 
    `django-admin createsuperuser  {{creates a superuser account}} 
    `django-admin dbshell          {{command-line client for the database engine}} 
    `django-admin diffsettings     {{Displays differences between the current settings file and Django’s default settings}} 
    `django-admin dumpdata         {{standard output all data in the database associated with the named application}} 
    `django-admin flush            {{Removes all data from the database}} 
    `django-admin inspectdb        {{script will inspect the database and create a model for each table within it}} 
    `django-admin makemessages     {{Runs over the entire source tree of the current directory and pulls out all strings marked for translation}} 
    `django-admin makemigrations   {{Creates new migrations based on the changes detected to your models}} 
    `django-admin migrate          {{synchronizes the database state with the current set of models and migrations}} 
    `django-admin runserver        {{Starts a lightweight development Web server on the local machine}} 
    `django-admin sendtestemail    {{Sends a test mail to the recipients}} 
    `django-admin shell            {{Starts the Python interactive interpreter}} 
    `django-admin showmigrations   {{Shows all migrations in a project}} 
    `django-admin sqlflush         {{Prints the SQL statements that would be executed for the flush command}} 
    `django-admin sqlmigrate       {{Prints the SQL for the named migration}} 
    `django-admin startapp name    {{Creates a Django app directory structure for the given app name in the current directory or the given destination}} 
    `django-admin startproject name
>                                  {{Creates a Django project directory structure for the given project name in the current directory or the given destination}} 
    `django-admin test             {{Runs tests for all installed apps.}} 
    `django-admin test             {{Runs tests for all installed apps.}} 

$ QuerySet Commands
    `filter()                      {{Returns a new QuerySet containing objects that match the given lookup parameters}} 
    `exclude()                     {{Returns a new QuerySet containing objects that do not match the given lookup parameters}} 
    `order_by()                    {{Results returned by a QuerySet are ordered by the ordering tuple given by the ordering option in the model’s Meta}} 
    `reverse()                     {{reverse the order in which a queryset’s elements are returned}} 
    `distinct()                    {{Returns a new QuerySet that uses SELECT DISTINCT in its SQL query}} 
    `values()                      {{Returns a QuerySet that returns dictionaries, rather than model instances, when used as an iterable}} 
    `values_list()                 {{Returns tuples when iterated over}} 
    `datetimes(field_name, kind, order='ASC', tzinfo=None)
>                                  {{ Returns a QuerySet that evaluates to a list of datetime.datetime objects representing all available dates of a particular kind within the contents of the QuerySet}} 
    `none()                        {{will create a queryset that never returns any objects}} 
    `all()                         {{Returns a copy of the current QuerySet}} 
    `select_related()              {{Returns a QuerySet that will “follow” foreign-key relationships}} 
    `prefetch_related()            {{Returns a QuerySet that will automatically retrieve, in a single batch, related objects for each of the specified lookups}} 
    `raw(raw_query, params=None, translations=None)
>                                  {{Takes a raw SQL query, executes it, and returns a django.db.models.query.RawQuerySet instance}} 
    `get()                         {{Returns the object matching the given lookup parameters}} 
    `create()                      {{Method for creating an object and saving it all in one step}} 
    `get_or_create()               {{A convenience method for looking up an object with the given kwargs (may be empty if your model has defaults for all fields), creating one if necessary}} 
    `bulk_create()                 {{This method inserts the provided list of objects into the database in an efficient manner}} 
    `count()                       {{Returns an integer representing the number of objects in the database matching the QuerySet}} 
    `latest()                      {{Returns the latest object in the table}} 
    `earliest()                    {{Works otherwise like latest() except the direction is changed}} 
    `first()                       {{Returns the first object matched by the queryset}} 
    `last()                        {{Returns the last object matched by the queryset}} 
    `aggregate()                   {{Returns a dictionary of aggregate values (averages, sums, etc.)}} 
    `exists()                      {{Returns True if the QuerySet contains any results}} 
    `update()                      {{Performs an SQL update query for the specified fields}} 
    `delete()                      {{Performs an SQL delete query}} 
    `save()                        {{Performs an SQL save query}} 
    `save()                        {{Performs an SQL save query}} 

$ Field LookUps
    `exact                         {{Matches Exactly}} 
    `iexact                        {{Case-insensitive exact match}} 
    `contains                      {{Case sensitive containment test}} 
    `icontains                     {{Case-insensitive containment test}} 
    `in                            {{In a given list}} 
    `gt                            {{greater than}} 
    `lt                            {{less than}} 
    `lte                           {{less than and equal to}} 
    `gte                           {{greater than and equal to}} 
    `startswith                    {{Case-sensitive starts-with}} 
    `istartswith                   {{Case-insensitive starts-with}} 
    `endswith                      {{Case-sensitive ends-with}} 
    `iendswith                     {{Case-insensitive ends-with}} 
    `range                         {{Range test (inclusive)}} 
    `date                          {{For datetime fields, casts the value as date}} 
    `year                          {{For date and datetime fields, an exact year match}} 
    `month                         {{For date and datetime fields, an exact month match}} 
    `day                           {{For date and datetime fields, an exact day match}} 
    `week_day                      {{For date and datetime fields, a ‘day of the week’ match}} 
    `hour                          {{For datetime and time fields, an exact hour match}} 
    `minute                        {{For datetime and time fields, an exact minute match}} 
    `second                        {{For datetime and time fields, an exact second match}} 
    `isnull                        {{Takes either True or False, which correspond to SQL queries of IS NULL and IS NOT NULL, respectively}} 
    `search                        {{Boolean full-text search, taking advantage of full-text indexing}} 
    `regex                         {{Case-sensitive regular expression match}} 
    `iregex                        {{Case-insensitive regular expression match}} 
    `iregex                        {{Case-insensitive regular expression match}} 

