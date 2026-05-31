"""Tests for the AI agent."""

import pytest
import asyncio
from agent.core import Agent
from agent.tools import calculate


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test agent initialization."""
    agent = Agent("TestAgent", model="gpt-4")
    assert agent.name == "TestAgent"
    assert agent.model == "gpt-4"
    assert len(agent.tools) == 0
    assert len(agent.memory) == 0


@pytest.mark.asyncio
async def test_agent_memory():
    """Test agent memory."""
    agent = Agent("TestAgent")
    response = await agent.think("Test prompt")
    
    memory = agent.get_memory()
    assert len(memory) == 2
    assert memory[0]["role"] == "user"
    assert memory[0]["content"] == "Test prompt"
    assert memory[1]["role"] == "assistant"


def test_calculate():
    """Test calculate tool."""
    result = calculate("2 + 2")
    assert result == 4.0
    
    result = calculate("10 * 5")
    assert result == 50.0


def test_calculate_invalid():
    """Test calculate with invalid expression."""
    with pytest.raises(ValueError):
        calculate("invalid()")
