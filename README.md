README:
=======

This is a small RESTful web service that handles TODO lists, tasks and tags, made with Django, the Django Rest Framework module, using Swagger for documentation and Behave for testing.

NOTES:
======

    - Django has a very strict way of doing things which should be valuable in very large projects. The rest framework
    and the automated swagger docs are a big plus and essential to serious web services.

    - Relations with django were a big hastle (most of the time spent for the nested writable many-to-many relation between tasks and tags). Part of it may be due to my inexperience with the framework, but I am positive that these simple relations would not have taken so much time to implement in NODE - even for a beginner - using a noSQL database with references.