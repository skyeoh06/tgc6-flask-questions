# Q6 - POST requests

We are going to work with 
* forms and POST request
* passing data to the template files

## Task 1
Look at the form in the `/` route, and complete the POST version of the same route such that the template can render the first name and last name of the user. 
* Complete the POST method for the `/` route
* Complete the `process-hello.template.html` so that it will show the entered first name and last name

## Task 2
You have to create your own route and template for this task.

* Create a new route `/calculate`
* For the GET method of the route, display a form with two textboxes, with the name `number1` and `number2`, and a submit button. 
* For the POST method of the route, (that is, When the submit button is pressed), returns a template that displays sum of `number1` and `number2` 
    * Display the answer in a `<div>` with the id `answer`
    * Just displaying the answer will do. There's no need for any additional text.