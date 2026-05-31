"""Core agent implementation."""

import asyncio
from typing import Any, Callable, Dict, List, Optional


class Agent:
    """Base AI Agent class."""

    def __init__(self, name: str, model: str = "gpt-4"):
        """Initialize the agent.
        
        Args:
            name: Agent name
            model: LLM model to use
        """
        self.name = name
        self.model = model
        self.tools: Dict[str, Callable] = {}
        self.memory: List[Dict[str, Any]] = []

    def register_tool(self, name: str, func: Callable) -> None:
        """Register a tool the agent can use.
        
        Args:
            name: Tool name
            func: Callable function
        """
        self.tools[name] = func

    async def think(self, prompt: str) -> str:
        """Process a prompt and generate a response.
        
        Args:
            prompt: User prompt
            
        Returns:
            Agent response
        """
        # Add to memory
        self.memory.append({"role": "user", "content": prompt})
        
        # Process with LLM
        response = await self._call_llm(prompt)
        
        # Add response to memory
        self.memory.append({"role": "assistant", "content": response})
        
        return response

    async def _call_llm(self, prompt: str) -> str:
        """Call the language model.
        
        Args:
            prompt: Input prompt
            
        Returns:
            Model response
        """
        # Placeholder for LLM integration
        return f"Response from {self.model}: {prompt}"

    def get_memory(self) -> List[Dict[str, Any]]:
        """Get agent memory.
        
        Returns:
            List of memory entries
        """
        return self.memory
