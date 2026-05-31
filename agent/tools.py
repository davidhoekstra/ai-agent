"""Agent tools and utilities."""

import requests
from typing import Any, Dict


def fetch_url(url: str) -> str:
    """Fetch content from a URL.
    
    Args:
        url: URL to fetch
        
    Returns:
        Response text
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return f"Error fetching URL: {str(e)}"


def calculate(expression: str) -> float:
    """Safely evaluate a mathematical expression.
    
    Args:
        expression: Mathematical expression
        
    Returns:
        Result of calculation
    """
    try:
        # Use eval safely with restricted namespace
        result = eval(expression, {"__builtins__": {}}, {})
        return float(result)
    except Exception as e:
        raise ValueError(f"Invalid expression: {str(e)}")
