"""
Custom RAG Tool for Mathematics Content Generation
Retrieves content from processed Class 11 Mathematics chapters
"""

from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import sys
import os
from pathlib import Path

# Add parent directories to Python path
# custom_tool.py is at src/physics_content/tools/custom_tool.py
# query_documents.py is at project root (4 levels up)
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "RAG-Anything"))


class RAGQueryInput(BaseModel):
    """Input schema for RAG Query Tool."""
    query: str = Field(
        ..., 
        description="Physics topic, concept, or question to retrieve from processed chapters. Be specific for better results."
    )


class PhysicsRAGTool(BaseTool):
    """
    RAG-powered retrieval tool for Class 11 Mathematics content
    Sources: Processed NCERT chapters
    """
    
    name: str = "rag_anything_enhancer"
    description: str = """
    Retrieves Mathematics content from processed Class 11 chapters:
    
    AVAILABLE CHAPTERS:
    - Sets
    - Relations and Functions
    - Trigonometric Functions
    - Complex Numbers and Quadratic Equations
    - Linear Inequalities
    - Permutations and Combinations
    - Binomial Theorem
    - Sequences and Series
    - Straight Lines
    - Conic Sections
    - Introduction to Three Dimensional Geometry
    - Limits and Derivatives
    - Statistics
    - Probability
    
    WHAT YOU CAN GET:
    - Formal Definitions (Rigorous math)
    - Theorems and Step-by-Step Proofs
    - Working Rules (Algorithms for solving problems)
    - Solved Examples (Basic to Advanced)
    - Geometric Interpretations and Graphs
    
    QUERY EXAMPLES:
    Good: "Binomial theorem for positive integral indices proof"
    Good: "Sum of n terms of AP and GP formulas"
    Good: "Properties of sets with Venn diagram examples"
    Bad: "tell me everything" (too broad)
    Bad: "chapter 1" (too vague)
    
    IMPORTANT: Always use this tool BEFORE generating content to ensure accuracy.
    Make multiple specific queries rather than one broad query.
    """
    args_schema: Type[BaseModel] = RAGQueryInput
    
    # Class-level cache for query results
    _query_cache = {}
    _total_queries = 0
    _cache_hits = 0
    _estimated_cost = 0.0
    
    def _run(self, query: str) -> str:
        """
        Execute RAG query synchronously with caching and validation
        """
        # Check cache first
        if query in self._query_cache:
            self._cache_hits += 1
            print(f"✅ Cache hit ({self._cache_hits} total) for query: {query[:60]}...")
            return self._query_cache[query]
        
        # Track metrics
        self._total_queries += 1
        self._estimated_cost += 0.004
        
        print(f"🔍 RAG Query #{self._total_queries}: {query[:60]}...")
        print(f"💰 Estimated cost so far: ${self._estimated_cost:.3f}")
        
        try:
            # Import here to avoid circular dependencies
            from query_documents import query_rag_sync
            
            # Execute RAG query
            result = query_rag_sync(query, mode="hybrid", top_k=15)
            
            # Validate result quality
            if not result or len(result.strip()) < 50:
                print(f"⚠️ RAG returned insufficient content. Trying global mode...")
                result = query_rag_sync(query, mode="global", top_k=20)
            
            if not result or len(result.strip()) < 50:
                return (
                    f"⚠️ No relevant content found in processed chapters for query: '{query}'\n"
                    f"Suggestion: Try rephrasing with more specific physics terms or concepts.\n"
                    f"Available topics: electric charges, fields, potential, capacitance, "
                    f"current, resistance, magnetism, magnetic materials."
                )
            
            # Cache successful result
            self._query_cache[query] = result
            
            print(f"✅ Retrieved {len(result)} characters")
            return f"📚 Retrieved Content from Processed Chapters:\n\n{result}"
            
        except Exception as e:
            error_msg = (
                f"❌ RAG retrieval error: {str(e)}\n"
                f"This might be due to:\n"
                f"1. RAG system not initialized properly\n"
                f"2. Processed chapters not available\n"
                f"3. Query format issues\n"
                f"Proceeding with general physics knowledge (not from PDFs)."
            )
            print(error_msg)
            return error_msg
    
    @classmethod
    def get_stats(cls):
        """Get tool usage statistics"""
        return {
            "total_queries": cls._total_queries,
            "cache_hits": cls._cache_hits,
            "cache_hit_rate": f"{(cls._cache_hits/cls._total_queries*100):.1f}%" if cls._total_queries > 0 else "0%",
            "estimated_cost": f"${cls._estimated_cost:.3f}"
        }
