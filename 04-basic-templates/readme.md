# Q4 - Basic Templates

Do the following tasks:

1. Create a new file named `app.py`

2. Implement the following routes using Flask

## /
Use the `render_template` function to render the template file `index.template.html`, and within the `<h1>` tag, put in the text `hello world`.

Inside the `index.template.html` template, do the following:

* Use the `url_for` function to add in a link to the `/galley` route.
* Use the `url_for` function to link the CSS file `styles.css` found in the `static` folder.

## /gallery
Use the `render_template` function to render the template file `gallery.template.html`. 
Display the image `puppy.jpg` found inside the static folder.