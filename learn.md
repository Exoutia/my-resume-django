# Django Protfolio App

### Key Points
- The django project holds some configuration that apply to the project as a whole such as project settings, URLs, shared templates and static files. Each application can have its own database and has itwn functions to control how the data is displayed to the user in HTML templates.
- Django apps are structured so that there is a sepration logic. It supports the Model-View-Controller Pattern, which is the architecture on which most web frameworks are built. The basic principle is that in each application there are three seprate files that handle the three main pieces of logic seprately:
  - **Model** defines the data strucutre. This is usually a database and is the base layer to an application.
  - **View** displays some or all of the data to the user with html and css.
  - **Controller** handles how the database and view interact.
- In django this is somewhat different as the django handles all the controller part. The pattern django utilizes is called the Model-View-Template pattern. 