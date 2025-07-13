"""
Utilitaires pour l'analyse des templates Jinja2
"""

from jinja2 import Environment, meta
from typing import Set


def extract_jinja_variables(template_content: str) -> Set[str]:
    try:
        env = Environment()
        ast_nodes = env.parse(template_content)
        variables = meta.find_undeclared_variables(ast_nodes)
        return variables
    except Exception:
        return set()
