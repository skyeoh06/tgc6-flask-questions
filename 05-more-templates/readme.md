# Q5 - Template Practise and Static Files

There are no skeleton files for this lab. You have to do everything yourself!

1. Create a new file with the name `app.py` and implement a Flask app.

2. You need to create a `static` folder in the same directory as `app.py` to put in your static asset files (images, style sheets etc.)

2. Add in the following routes, along with the relevant template files.

**Routes to create:**
## /
You have three tasks for this route:

**Task 1**
Renders a template using `render_template` which displays the following HTML:

```
<h1>About Us</h1>
<p>
    We have the best friend chicken ever!
</p>
```
**Task 2**
Display a link that allows the user to go to the `/products` route.

**Task 3**
Include the `styles.css` file, which is found in the `rawfiles` folder. (You still need to use Flask's method linking in a static file.)


## /products
Renders a template using `render_template` which displays the following HTML. Also display the image `friedchicken.jpg` which can be found inside the `rawfiles` folder.
(Hint: You still need to follow Flask's methods of displaying a static images). You can display the image anywhere in the page.

```
<h1>Products</h1>
<ul>
    <li>Fried chicken</li>
    <li>Fried chicken, spicy</li>
    <li>Fried chicken, extra spicy</li>
</ul>
```