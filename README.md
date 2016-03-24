README:
=======

This is a small RESTful web service that handles TODO lists, tasks and tags, made with Django, the Django Rest Framework module, using Swagger for documentation and Behave for testing.

I decided to go with Django as it was in the assignment's "prefered" list and I though it would be a good opportunity to gain some Django experiece. I cannot say I didn't regret my decision several times throughout this small project, but I do see the appeal of Django after delving into it for about a week, and I will continue to use it for certain types of projects.

NOTES:
======

    - Django has a very strict way of doing things which could be valuable in very large projects. The rest framework
    and the automated swagger docs are a big plus and essential to serious web services.

    - Relations with django were a big hastle (most of the time spent for the nested writable many-to-many relation between tasks and tags). Part of it may be due to my inexperience with the framework, but I am positive that these simple relations would not have taken so much time to implement in NodeJS-Express-Mongo - even for a beginner.