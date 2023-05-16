# MovieRatingPlatform

Our goal is to create a movie rating platform with Django and Boostrap framework. The platform conforms to the MVC template. Our platform will be populated with data from the Movie-Lens dataset. If you have any problems with Bootstrap consult [Bootstrap 5 Tutorial (w3schools.com)](https://www.w3schools.com/bootstrap5/).

1. Create a project (you can the use the project from previous assignment or create a brand new one)
1. Prepare a layout template. The layout encompasses the contents of each subpage in the platform with the HTML document definition. The layout also contains the navigation bar. Put the login, logout and register buttons on the navigation bar. Content of the web page in the layout is represented with Django blocks. At this point limit yourself to a single block, this number can be expanded later on.
1. Implement the user logic to your platform. Insert the necessary user-related functions to the views file, and implement necessary forms (you can use the code from the 2nd assignment here).
1. Suggest a data model for your project. We are going to implement the following functionalities:
1. A guest user can search for a specific movie with the following filters:
   1. Genre,
   1. Movie Title,
   1. Minimum rating.
1. A guest viewer can view the details of a movie by clicking on an item in the search list. Details of a movie contain the following informations:
   1. Title of a movie,
   1. Average rating of a movie,
   1. Cross reference to IMDB,
   1. Image gallery with one image dedicated as a front image
   1. List of comments to the movie
1. Logged in users can view movies rated by them.
1. Logged in users can rate a movie.
1. Logged in users can post a comment under a movie.
1. Admin users can edit details of a movie.
1. Admin users can add a new movie.
5. Prepare templates for (the templates should extend the layout template):
1. the home page - the home page consists of:
   1. a brief introduction to the portal (you can fill it with lorem)
   1. a list the most popular movies (recently)
   1. if a logged in user is viewing the home page - a list of recommendation (for now, leave it empty)
1. the movie search page - this web page consists of:
1. A search form for genre, title, rating (use required=False in the form definition)
2. list of search results (consider several formats of the list: a table, continuous list of cards, a list) - one should be able to access a movie page through the list items
3. the movie page - this web page displays all movie data, including the movie images, comments, title, average rating, user rating (if logged in); access to the actions, such as posting a comment (if logged in); editing a movie (if admin)
3. admin page - this web page is only visible to an administrator user, it contains a form, which allows an admin to add a new movie.
6. Implement the view functions, forms and add paths to the urls.py.
6. Add hyperlinks to the movie search and homepage to the navigation bar.

That’s it for the 1st part of the assignment.
