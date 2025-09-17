#!/usr/bin/env python3
"""
Main FastAPI application for Docker DevDuck Multi-Agent System
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import logging
from typing import Dict, Any

# Import agents
from devduck.agent import DevDuckCoordinator
from devduck.sub_agents.localagent.agent import LocalNodeAgent
from devduck.sub_agents.cerebras.agent import CerebrasAgent

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="DevDuck Multi-Agent System",
    description="Docker workshop for multi-agent AI system coordination",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response models
class ChatRequest(BaseModel):
    message: str
    agent: str = "devduck"  # devduck, local, cerebras

class ChatResponse(BaseModel):
    response: str
    agent_used: str
    reasoning: str = None

# Initialize agents
devduck_coordinator = DevDuckCoordinator()
local_agent = LocalNodeAgent()
cerebras_agent = CerebrasAgent()

@app.get("/")
async def root():
    return HTMLResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevDuck Multi-Agent System</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .container { max-width: 800px; margin: 0 auto; }
            .agent-card { border: 1px solid #ddd; padding: 20px; margin: 10px 0; border-radius: 8px; }
            .btn { background: #007bff; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🦆 DevDuck Multi-Agent System</h1>
            <p>Welcome to the Docker DevDuck Multi-Agent Workshop!</p>
            
            <div class="agent-card">
                <h3>🎼 DevDuck Coordinator</h3>
                <p>Intelligent request routing and agent coordination</p>
                <button class="btn" onclick="testAgent('devduck')">Test DevDuck</button>
            </div>
            
            <div class="agent-card">
                <h3>💻 Local Node.js Agent</h3>
                <p>Local development expertise and code generation</p>
                <button class="btn" onclick="testAgent('local')">Test Local Agent</button>
            </div>
            
            <div class="agent-card">
                <h3>🧠 Cerebras Agent</h3>
                <p>Advanced AI analysis and complex problem solving</p>
                <button class="btn" onclick="testAgent('cerebras')">Test Cerebras Agent</button>
            </div>
            
            <h3>📋 Quick Test</h3>
            <div id="test-results" style="background: #f8f9fa; padding: 20px; border-radius: 4px; margin-top: 20px;"></div>
        </div>
        
        <script>
            async function testAgent(agent) {
                const resultsDiv = document.getElementById('test-results');
                resultsDiv.innerHTML = '<p>Testing ' + agent + ' agent...</p>';
                
                try {
                    const response = await fetch('/chat', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            message: 'Hello! Can you help me with Node.js development?',
                            agent: agent
                        })
                    });
                    
                    const data = await response.json();
                    resultsDiv.innerHTML = `
                        <h4>Response from ${data.agent_used}:</h4>
                        <p>${data.response}</p>
                        ${data.reasoning ? '<p><em>Reasoning: ' + data.reasoning + '</em></p>' : ''}
                    `;
                } catch (error) {
                    resultsDiv.innerHTML = '<p style="color: red;">Error: ' + error.message + '</p>';
                }
            }
        </script>
    </body>
    </html>
    """)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "agents": ["devduck", "local", "cerebras"]}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        if request.agent == "devduck":
            response, reasoning = await devduck_coordinator.process_request(request.message)
            return ChatResponse(response=response, agent_used="DevDuck Coordinator", reasoning=reasoning)
        
        elif request.agent == "local":
            response = await local_agent.generate_response(request.message)
            return ChatResponse(response=response, agent_used="Local Node.js Agent")
        
        elif request.agent == "cerebras":
            response = await cerebras_agent.analyze_request(request.message)
            return ChatResponse(response=response, agent_used="Cerebras Agent")
        
        else:
            raise HTTPException(status_code=400, detail="Invalid agent specified")
            
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Agent error: {str(e)}")

@app.get("/dev-ui/")
async def dev_ui():
    """Development UI redirect for compatibility"""
    return await root()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
