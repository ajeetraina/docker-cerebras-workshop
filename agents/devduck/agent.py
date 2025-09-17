#!/usr/bin/env python3
"""
DevDuck Coordinator Agent

Intelligent coordinator that routes requests to appropriate sub-agents
based on request analysis and agent capabilities.
"""

import asyncio
import logging
import os
from typing import Tuple, Dict, Any
import httpx
from .sub_agents.localagent.agent import LocalNodeAgent
from .sub_agents.cerebras.agent import CerebrasAgent

logger = logging.getLogger(__name__)

class DevDuckCoordinator:
    """Main coordinator agent that intelligently routes requests"""
    
    def __init__(self):
        self.local_agent = LocalNodeAgent()
        self.cerebras_agent = CerebrasAgent()
        
        # Request classification patterns
        self.routing_patterns = {
            'code_generation': ['generate', 'create', 'write code', 'implement', 'build'],
            'code_analysis': ['analyze', 'explain', 'review', 'debug', 'understand'],
            'complex_reasoning': ['complex', 'advanced', 'architecture', 'design pattern', 'optimization'],
            'simple_questions': ['hello', 'hi', 'what is', 'how do', 'basic']
        }
    
    def classify_request(self, message: str) -> str:
        """Classify the type of request to determine best agent"""
        message_lower = message.lower()
        
        # Check for complex reasoning needs
        if any(pattern in message_lower for pattern in self.routing_patterns['complex_reasoning']):
            return 'cerebras'
            
        # Check for code generation needs
        if any(pattern in message_lower for pattern in self.routing_patterns['code_generation']):
            return 'local'
            
        # Check for code analysis needs
        if any(pattern in message_lower for pattern in self.routing_patterns['code_analysis']):
            return 'cerebras'
            
        # Default to local for simple questions
        return 'local'
    
    async def process_request(self, message: str) -> Tuple[str, str]:
        """Process request and route to appropriate agent"""
        try:
            # Classify the request
            chosen_agent = self.classify_request(message)
            reasoning = f"Routed to {chosen_agent} agent based on request analysis"
            
            logger.info(f"DevDuck routing request to {chosen_agent} agent")
            
            # Route to appropriate agent
            if chosen_agent == 'local':
                response = await self.local_agent.generate_response(message)
                reasoning += ". Local agent chosen for Node.js development tasks."
            elif chosen_agent == 'cerebras':
                response = await self.cerebras_agent.analyze_request(message)
                reasoning += ". Cerebras agent chosen for complex analysis."
            else:
                # Fallback to local agent
                response = await self.local_agent.generate_response(message)
                reasoning += ". Fallback to local agent."
                
            return response, reasoning
            
        except Exception as e:
            logger.error(f"DevDuck coordinator error: {str(e)}")
            return f"I apologize, but I encountered an error: {str(e)}. Please try again.", "Error in coordination"
    
    async def get_status(self) -> Dict[str, Any]:
        """Get status of all agents"""
        return {
            'coordinator': 'active',
            'local_agent': 'active',
            'cerebras_agent': 'active' if os.getenv('CEREBRAS_API_KEY') else 'inactive'
        }
