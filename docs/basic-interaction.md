# Basic Agent Interaction

Learn the fundamentals of interacting with your multi-agent system.

## Exercise 1: First Contact with the Main Agent

Test basic communication with the multi-agent system:

- Open the web interface at http://0.0.0.0:8000
- Try the following sample interaction:

```
Hello I'm Phil
```

**Expected Outcome**: DevDuck should respond and introduce the system capabilities.

```
Hello! I'm DevDuck, your main development assistant and project coordinator. How can I assist you today? If you have a question that is more suitable for my specialized agent, Cerebras, or Local Agent, I can transfer your question to them. Let me know if you need help with advanced computational tasks, complex problem-solving, general development tasks, or project coordination.
```

## Exercise 2. Conversation with the Local Agent

Continue your interaction with the local agent:


```
Local Agent generate a Node.js hello world program
```

**Expected Outcome**: 

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

Continue your conversation with the local agent:


```
Add a Person class with a greet method
```

```
To create a Person class with a greet method in Node.js, you can use the following code:

class Person {
 constructor(name) {
   this.name = name;
 }

 greet() {
   console.log(`Hello, ${this.name}!`);
 }
}

// Create a new person instance
const myPerson = new Person('John');

// Call the greet method
myPerson.greet(); // Output: Hello, John!
In this example, we define a Person class with a constructor that takes a name parameter. The class has a greet method that logs a greeting message with the person's name. We then create a new Person instance called myPerson and call the greet method on it.
```

## Exercise 3. Conversation with Cerebras Agent


```
Cerebras can you analyse and comment this code
```


**Expected Outcome**: 


```
To analyze and comment the given code, I will transfer this question to the Cerebras agent.

transfer_to_agent('cerebras_agent');
This code defines a Person class with a constructor that takes a name parameter and a greet method that logs a greeting message with the person's name. It also creates a new Person instance called myPerson and calls the greet method on it.

The code is well-structured and follows good practices for defining classes in JavaScript. However, it would be more efficient to use an arrow function for the greet method to avoid creating a new function every time an instance of the Person class is created.

Here's the updated code:

class Person {
constructor(name) {
  this.name = name;
}

greet = () => {
  console.log(`Hello, ${this.name}!`);
}
}

// Create a new person instance
const myPerson = new Person('John');

// Call the greet method
myPerson.greet(); // Output: Hello, John!
This updated code uses an arrow function for the greet method, which improves performance by avoiding the creation of a new function every time an instance of the Person class is created.
```

Contiue your conversation with Cerebras Agent:

```
Can you generate the tests
```

```
To generate tests for the Person class, I will create a test file called person_test.js and write some test cases using the describe and it functions from the Mocha testing framework.

First, let's install Mocha and Chai assertion library:

npm install mocha chai
Now, here's the person_test.js file:

const { expect } = require('chai');
const Person = require('./person');

describe('Person', () => {
let person;

beforeEach(() => {
  person = new Person('John');
});

it('should create a new person instance', () => {
  expect(person).to.be.an.instanceOf(Person);
});

it('should have a name property', () => {
  expect(person.name).to.equal('John');
});

it('should greet the person correctly', () => {
  person.greet();
  const logOutput = console.log.apply(console, arguments);
  expect(logOutput).to.equal(`Hello, John!`);
});
});
In this test file, we import the expect function from Chai and the Person class from the local file. We use the describe function to group related test cases, and the it function to define individual test cases.

The beforeEach function is used to set up the test environment before each test case. In this case, we create a new Person instance before each test.

We have three test cases:

should create a new person instance: This test checks if the Person constructor creates a new instance of the class.
should have a name property: This test checks if the Person instance has a name property.
should greet the person correctly: This test checks if the greet method logs the correct greeting message.
To run the tests, execute the following command:

mocha person_test.js
This will run the tests and display the results. If the tests pass, it means the Person class is working as expected. If any test fails, you can investigate the issue and fix the code accordingly.
```




