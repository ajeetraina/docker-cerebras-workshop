#!/usr/bin/env python3
"""
Local Node.js Development Agent

Specialized agent for Node.js development tasks including:
- Code generation
- Basic explanations
- Development guidance
- Local model inference
"""

import asyncio
import logging
import os
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

class LocalNodeAgent:
    """Local Node.js development expert agent"""
    
    def __init__(self):
        self.model_name = os.getenv('LOCAL_MODEL_NAME', 'llama-3.2-3b-instruct')
        self.system_prompt = """
You are a Node.js development expert assistant. You specialize in:

- Writing clean, efficient Node.js code
- Explaining JavaScript and Node.js concepts
- Providing best practices for Node.js development
- Helping with npm packages and dependencies
- Debugging common Node.js issues
- Creating Express.js applications
- Working with databases in Node.js
- Writing tests for Node.js applications

Always provide practical, working code examples when possible.
Keep explanations clear and beginner-friendly when appropriate.
"""
        logger.info(f"Local Node.js Agent initialized with model: {self.model_name}")
    
    async def generate_response(self, message: str) -> str:
        """Generate response for Node.js development queries"""
        try:
            # In a real implementation, this would use a local LLM
            # For the workshop, we'll provide predefined helpful responses
            
            message_lower = message.lower()
            
            if 'hello' in message_lower or 'hi' in message_lower:
                return (
                    "Hello! I'm your local Node.js development assistant. "
                    "I can help you with:\n\n"
                    "🔹 Writing Node.js code\n"
                    "🔹 Explaining JavaScript concepts\n"
                    "🔹 Express.js applications\n"
                    "🔹 npm package management\n"
                    "🔹 Debugging Node.js issues\n\n"
                    "What would you like to work on today?"
                )
            
            elif 'express' in message_lower:
                return self._generate_express_example()
            
            elif 'package.json' in message_lower:
                return self._generate_package_json_example()
            
            elif 'api' in message_lower:
                return self._generate_api_example()
            
            elif 'test' in message_lower:
                return self._generate_testing_example()
            
            else:
                return (
                    f"I understand you're asking about: '{message}'\n\n"
                    "As your local Node.js agent, I'm here to help with development tasks. "
                    "Could you be more specific about what you'd like to accomplish? \n\n"
                    "For example:\n"
                    "• 'Create an Express.js server'\n"
                    "• 'Show me a package.json example'\n"
                    "• 'Help me build a REST API'\n"
                    "• 'How do I write tests in Node.js?'"
                )
        
        except Exception as e:
            logger.error(f"Local agent error: {str(e)}")
            return f"I apologize, but I encountered an error: {str(e)}. Please try again."
    
    def _generate_express_example(self) -> str:
        """Generate Express.js server example"""
        return """
🚀 **Express.js Server Example**

Here's a basic Express.js server setup:

```javascript
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Routes
app.get('/', (req, res) => {
    res.json({ message: 'Hello from DevDuck Express server!' });
});

app.get('/api/health', (req, res) => {
    res.json({ status: 'OK', timestamp: new Date().toISOString() });
});

// Start server
app.listen(PORT, () => {
    console.log(`🚀 Server running on port ${PORT}`);
});
```

**To get started:**
1. `npm init -y`
2. `npm install express`
3. Save the code as `server.js`
4. Run with `node server.js`
"""
    
    def _generate_package_json_example(self) -> str:
        """Generate package.json example"""
        return """
📦 **Package.json Example**

Here's a well-structured package.json for a Node.js project:

```json
{
  "name": "devduck-node-app",
  "version": "1.0.0",
  "description": "DevDuck Node.js application",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js",
    "test": "jest",
    "test:watch": "jest --watch"
  },
  "dependencies": {
    "express": "^4.18.2",
    "cors": "^2.8.5",
    "helmet": "^7.0.0",
    "dotenv": "^16.3.1"
  },
  "devDependencies": {
    "nodemon": "^3.0.1",
    "jest": "^29.6.2",
    "supertest": "^6.3.3"
  },
  "engines": {
    "node": ">=16.0.0",
    "npm": ">=8.0.0"
  },
  "keywords": ["node", "express", "api"],
  "author": "DevDuck Team",
  "license": "MIT"
}
```

**Key sections explained:**
• `scripts`: Custom commands you can run with `npm run`
• `dependencies`: Packages needed in production
• `devDependencies`: Packages needed only for development
• `engines`: Specify Node.js and npm versions
"""
    
    def _generate_api_example(self) -> str:
        """Generate REST API example"""
        return """
🔗 **REST API Example**

Here's a complete REST API with CRUD operations:

```javascript
const express = require('express');
const app = express();

app.use(express.json());

// In-memory data store (use database in production)
let users = [
    { id: 1, name: 'Alice', email: 'alice@example.com' },
    { id: 2, name: 'Bob', email: 'bob@example.com' }
];

// GET all users
app.get('/api/users', (req, res) => {
    res.json(users);
});

// GET user by ID
app.get('/api/users/:id', (req, res) => {
    const user = users.find(u => u.id === parseInt(req.params.id));
    if (!user) return res.status(404).json({ error: 'User not found' });
    res.json(user);
});

// POST create new user
app.post('/api/users', (req, res) => {
    const { name, email } = req.body;
    if (!name || !email) {
        return res.status(400).json({ error: 'Name and email required' });
    }
    
    const newUser = {
        id: users.length + 1,
        name,
        email
    };
    
    users.push(newUser);
    res.status(201).json(newUser);
});

// PUT update user
app.put('/api/users/:id', (req, res) => {
    const user = users.find(u => u.id === parseInt(req.params.id));
    if (!user) return res.status(404).json({ error: 'User not found' });
    
    const { name, email } = req.body;
    if (name) user.name = name;
    if (email) user.email = email;
    
    res.json(user);
});

// DELETE user
app.delete('/api/users/:id', (req, res) => {
    const userIndex = users.findIndex(u => u.id === parseInt(req.params.id));
    if (userIndex === -1) return res.status(404).json({ error: 'User not found' });
    
    users.splice(userIndex, 1);
    res.status(204).send();
});

app.listen(3000, () => {
    console.log('API server running on port 3000');
});
```

**Test your API with curl:**
```bash
# Get all users
curl http://localhost:3000/api/users

# Create a new user
curl -X POST http://localhost:3000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Charlie","email":"charlie@example.com"}'
```
"""
    
    def _generate_testing_example(self) -> str:
        """Generate testing example"""
        return """
🧪 **Node.js Testing Example**

Here's how to set up testing with Jest and Supertest:

**1. Install testing dependencies:**
```bash
npm install --save-dev jest supertest
```

**2. Create `tests/api.test.js`:**
```javascript
const request = require('supertest');
const app = require('../server'); // Your Express app

describe('API Endpoints', () => {
    describe('GET /api/users', () => {
        test('Should return all users', async () => {
            const response = await request(app)
                .get('/api/users')
                .expect(200);
            
            expect(Array.isArray(response.body)).toBe(true);
            expect(response.body.length).toBeGreaterThan(0);
        });
    });
    
    describe('POST /api/users', () => {
        test('Should create a new user', async () => {
            const userData = {
                name: 'Test User',
                email: 'test@example.com'
            };
            
            const response = await request(app)
                .post('/api/users')
                .send(userData)
                .expect(201);
            
            expect(response.body.name).toBe(userData.name);
            expect(response.body.email).toBe(userData.email);
            expect(response.body.id).toBeDefined();
        });
        
        test('Should return error for missing data', async () => {
            const response = await request(app)
                .post('/api/users')
                .send({})
                .expect(400);
            
            expect(response.body.error).toBeDefined();
        });
    });
});
```

**3. Add test script to package.json:**
```json
{
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch"
  }
}
```

**4. Run tests:**
```bash
npm test
```

**Key testing concepts:**
• Use `describe()` to group related tests
• Use `test()` or `it()` for individual test cases
• Use `expect()` for assertions
• Supertest helps test HTTP endpoints
"""
    
    async def get_capabilities(self) -> Dict[str, Any]:
        """Get agent capabilities"""
        return {
            'specialties': ['Node.js', 'Express.js', 'JavaScript', 'npm', 'Testing'],
            'model': self.model_name,
            'status': 'active',
            'description': 'Local Node.js development expert'
        }
