import os
import yaml
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain.llms import OpenAI

from tools import DataFetchTool, IndicatorCalculationTool, MarketAnalysisTool

class AInalystCrew(CrewBase):
    # 获取当前文件的目录
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 构建配置文件的路径
    config_dir = os.path.join(current_dir, 'config')

    # 解析绝对路径
    config_dir = os.path.abspath(config_dir)

    # 构建完整的配置文件路径
    agents_config_path = os.path.join(config_dir, 'agents.yaml')
    tasks_config_path = os.path.join(config_dir, 'tasks.yaml')

    # 打印路径以进行调试
    print("Current directory:", current_dir)
    print("Config directory:", config_dir)
    print("Agents config path:", agents_config_path)
    print("Tasks config path:", tasks_config_path)

    # 加载配置文件
    with open(agents_config_path, 'r') as f:
        agents_config = yaml.safe_load(f)

    with open(tasks_config_path, 'r') as f:
        tasks_config = yaml.safe_load(f)

    @agent
    def data_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['data_agent'],
            tools=[
                DataFetchTool()
            ],
            llm=OpenAI(api_key=os.getenv('OPENAI_API_KEY')),
            verbose=True
        )

    @task
    def data_fetching(self) -> Task:
        return Task(
            config=self.tasks_config['data_fetching'],
            agent=self.data_agent()
        )

    @agent
    def indicator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['indicator_agent'],
            tools=[
                IndicatorCalculationTool()
            ],
            llm=OpenAI(api_key=os.getenv('OPENAI_API_KEY')),
            verbose=True
        )

    @task
    def indicator_calculation(self) -> Task:
        return Task(
            config=self.tasks_config['indicator_calculation'],
            agent=self.indicator_agent()
        )

    @agent
    def analysis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['analysis_agent'],
            tools=[
                MarketAnalysisTool()
            ],
            llm=OpenAI(api_key=os.getenv('OPENAI_API_KEY')),
            verbose=True
        )

    @task
    def market_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['market_analysis'],
            agent=self.analysis_agent()
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )