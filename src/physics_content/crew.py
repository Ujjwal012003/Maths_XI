from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from typing import List
import os
import sys
from pathlib import Path

# Add physics_content directory to Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

os.environ["CREWAI_AGENTS_CONFIG"] = "src/physics_content/config/agents.yaml"
os.environ["CREWAI_TASKS_CONFIG"] = "src/physics_content/config/tasks.yaml"

@CrewBase
class PhysicsContentCrew():
    """
    Chemistry Content Crew (Manager Loop Architecture)
    """
    agents: List[Agent]
    tasks: List[Task]
    
    def __init__(self):
        # Initialize RAG Tool
        try:
            from tools.custom_tool import PhysicsRAGTool
            self.rag_tool = PhysicsRAGTool()
            print("✅ Math RAG Tool initialized!")
        except Exception as e:
            print(f"⚠️ RAG Tool fail: {e}")
            self.rag_tool = None
            
        # Initialize Web Search Tool
        try:
            self.serper_tool = SerperDevTool()
            print("✅ SerperDev Web Search Tool initialized!")
        except Exception as e:
            print(f"⚠️ SerperDev Tool fail: {e}")
            self.serper_tool = None

    # --- AGENTS ---
    @agent
    def research_agent(self) -> Agent:
        tools = []
        if self.rag_tool: tools.append(self.rag_tool)
        if self.serper_tool: tools.append(self.serper_tool)
        return Agent(
            config=self.agents_config['research_agent'],
            verbose=True,
            tools=tools
        )

    @agent
    def content_indexer(self) -> Agent:
        tools = []
        if self.rag_tool: tools.append(self.rag_tool)
        if self.serper_tool: tools.append(self.serper_tool)
        return Agent(
            config=self.agents_config['content_indexer'],
            verbose=True,
            tools=tools
        )

    @agent
    def section_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['section_writer'],
            verbose=True,
            tools=[self.rag_tool] if self.rag_tool else []
        )

    @agent
    def reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['reviewer'],
            verbose=True
        )

    # --- TASKS ---
    @task
    def research_chapter(self) -> Task:
        return Task(config=self.tasks_config['research_chapter'])

    @task
    def create_index(self) -> Task:
        return Task(config=self.tasks_config['create_index'])

    @task
    def write_section(self) -> Task:
        return Task(config=self.tasks_config['write_section'])

    @task
    def review_section(self) -> Task:
        return Task(config=self.tasks_config['review_section'])

    # --- TWO DISTINCT CREWS ---

    def planning_crew(self) -> Crew:
        """Crew for Phase 1: Research & Indexing"""
        return Crew(
            agents=[self.research_agent(), self.content_indexer()],
            tasks=[self.research_chapter(), self.create_index()],
            process=Process.sequential,
            verbose=True
        )

    def writing_crew(self) -> Crew:
        """Crew for Phase 2: Writing a SINGLE Section"""
        return Crew(
            agents=[self.section_writer(), self.reviewer()],
            tasks=[self.write_section(), self.review_section()],
            process=Process.sequential,
            verbose=True
        )
