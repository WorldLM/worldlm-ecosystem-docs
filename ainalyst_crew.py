import os
import yaml
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain.llms import OpenAI

from tools import DataFetchTool, IndicatorCalculationTool, MarketAnalysisTool

from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

@CrewBase
class AInalystCrew:
    agents_config_path = 'config/agents.yaml'
    tasks_config_path = 'config/tasks.yaml'

    with open(agents_config_path, 'r') as f:
        agents_config = yaml.safe_load(f)

    with open(tasks_config_path, 'r') as f:
        tasks_config = yaml.safe_load(f)

    @agent
    def data_agent(self) -> Agent:
        print("Creating data_agent")
        return Agent(
            config=self.agents_config['data_agent'],
            tools=[
                DataFetchTool()
            ],
            llm=llm,
            verbose=True
        )

    @task
    def data_fetching(self) -> Task:
        print("Creating data_fetching task")
        return Task(
            config=self.tasks_config['data_fetching'],
            agent=self.data_agent()
        )

    @agent
    def indicator_agent(self) -> Agent:
        print("Creating indicator_agent")
        return Agent(
            config=self.agents_config['indicator_agent'],
            tools=[
                IndicatorCalculationTool()
            ],
            llm=llm,
            verbose=True
        )

    @task
    def indicator_calculation(self) -> Task:
        print("Creating indicator_calculation task")
        return Task(
            config=self.tasks_config['indicator_calculation'],
            agent=self.indicator_agent()
        )

    @agent
    def analysis_agent(self) -> Agent:
        print("Creating analysis_agent")
        return Agent(
            config=self.agents_config['analysis_agent'],
            tools=[
                MarketAnalysisTool()
            ],
            llm=llm,
            verbose=True
        )

    @task
    def market_analysis(self) -> Task:
        print("Creating market_analysis task")
        return Task(
            config=self.tasks_config['market_analysis'],
            agent=self.analysis_agent()
        )

    @crew
    def crew(self) -> Crew:
        print("Creating crew")
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )