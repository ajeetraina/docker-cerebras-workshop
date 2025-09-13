# Local Agent Tasks

Master the Local Agent for Node.js development tasks.

## Exercise: Local Agent Programming

Use the Local Agent for basic Node.js development:

- Request a simple Node.js program:

```
Local Agent generate a Node.js hello world program
```

- Enhance the program:

```
Add a Person class with a greet method
```

**Expected Outcome**: The Local Agent should generate clean, functional Node.js code.

```
To generate a Node.js "Hello, World!" program, you can use the following code:

// Import the 'http' module
const http = require('http');

// Define the server
const server = http.createServer((req, res) => {
 // Set the response status code and content type
 res.statusCode = 200;
 res.setHeader('Content-Type', 'text/plain');

 // Send the "Hello, World!" message as the response body
 res.end('Hello, World!\n');
});

// Start the server on port 3000
server.listen(3000, () => {
 console.log('Server running at http://localhost:3000/');
});
To run this code, save it in a file (e.g., hello_world.js) and execute it using Node.js:

node hello_world.js
This will start a simple HTTP server that listens on port 3000 and responds with "Hello, World!" when you access it at http://localhost:3000.
```


