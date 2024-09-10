from abc import ABC, abstractmethod
from prompt import prompting
import re
prompt=prompting()
class QueryGenerator(ABC):
    @abstractmethod
    def generate_query(self, question: str) -> str:
        pass

class PythonQueryGenerator(QueryGenerator):
    def generate_query(self, question: str) -> str:
        # Placeholder for Python query generation logic
        
        convo=prompt.python_conversation()
        convo.send_message(question)
        generated_code=convo.last.text
        pattern = r'^```python\n(.+?)\n```$'
        replacement = r'\1'
        generated_code_new = re.sub(pattern, replacement, generated_code, flags=re.DOTALL)
        return "# Python query based on: " + generated_code_new

class SQLQueryGenerator(QueryGenerator):
    def generate_query(self, question: str) -> str:
        # Placeholder for SQL query generation logic
        convo=prompt.sql_conversation()
        convo.send_message(question)
        generated_code=convo.last.text
        return "-- SQL query based on: " + generated_code

class AnswerGenerator(QueryGenerator):
    def generate_query(self, question: str) -> str:
        convo=prompt.ans_conversation()
        convo.send_message(question)
        generated_ans=convo.last.text
        return "Probable answer is this" + generated_ans