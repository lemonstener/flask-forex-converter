### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?  

  Python is used for the backend in a web application while JS can be used for both front and back. Python uses indentation for code blocks while JS relies on brackets. While they both have similar synthax, Python's is shorter. It is generally accepted that variable naming in Python should be done with snake_case and camelCase for JS. Python is very 'error happy' while JS is not. If a function written in Python expects a parameter it cannot be omitted while JS is more lenient about that. Python differentiates between whole and decimal numbers as int and float while JS does not and considers both of them as a number.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

    Using the .get method with a default value 
       stuff.get('c',3)
    Using setdefault method
       stuff.setdefault('c',3)


- What is a unit test?
  
  A way to test a single component of an application

- What is an integration test?

  A way to test multiple components of an application

- What is the role of web application framework, like Flask?

  To make it easier and faster for a developer to create an application. For example, Flask is used for making requests to a server. Without it you would need to write a lot more code to achieve the same thing. 

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  Dependding on the application but '/foods/pretzel' would be generally preferred due to it's simplicity.

- How do you collect data from a URL placeholder parameter using Flask?

  request.args?

- How do you collect data from the query string using Flask?

  request.args

- How do you collect data from the body of the request using Flask?

  request.form

- What is a cookie and what kinds of things are they commonly used for?

  Text files created by a website and stored in your browser which are used to customize your experience, remember preferences and generally keep track of your data. They are constantly sent back and forth from your browser to the server and back to your browser which is why they have to be very small in size. 

- What is the session object in Flask?

  The interval between a client logging in to the server and logging out. Similar to cookies but bigger in size and stored on the server. The session data is stored in a temporary directory on the server.

- What does Flask's `jsonify()` do?

  Formats data into JSON format and sends it to a JS request.
