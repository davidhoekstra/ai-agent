"""Main agent entry point."""

import asyncio
import os
from dotenv import load_dotenv
from agent.core import Agent
from agent.tools import fetch_url, calculate


async def main():
    """Run the AI agent."""
    load_dotenv()
    
    # Initialize agent
    agent = Agent("MyAIAgent", model="gpt-4")
    
    # Register tools
    agent.register_tool("fetch_url", fetch_url)
    agent.register_tool("calculate", calculate)
    
    # Example interaction
    print(f"Starting {agent.name}...\n")
    
    # Run a simple prompt
    response = await agent.think("What can you help me with today?")
    print(f"Agent: {response}\n")
    
    # Print memory
    print("Agent Memory:")
    for entry in agent.get_memory():
        print(f"  {entry['role']}: {entry['content']}")


if __name__ == "__main__":
    asyncio.run(main())
