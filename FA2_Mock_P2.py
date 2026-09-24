"""FA2 Mock P2: Translation, Summarization and Time Travel (20 marks).
Reconstructed practice template. Rename to FA2_Mock_<Emp_Num>_P2.py.
Complete TODOs and preserve GIVEN sections. No solution is included.
"""
# GIVEN - DO NOT MODIFY (imports reconstructed: top of source photos is missing)
import os
from typing import TypedDict, Optional
from dotenv import load_dotenv
from langchain_aws import ChatBedrockConverse
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.tools import tool
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import interrupt, Command

load_dotenv()

# TODO - YOUR CODE HERE: LLM setup
# Instantiate ChatBedrockConverse; variable must be named llm.
# Read model/region from .env or use the values approved in your lab.
# Downstream code calls llm.invoke(...) and, for P1, llm.bind_tools(...).
llm = None  # Replace this placeholder.

# GIVEN - DO NOT MODIFY
TARGET_LANGUAGE = "Hindi"  # Original permits changing this to "French".

class DocState(TypedDict):
    source_text: str
    translated: str
    summary: str
    refined: str


# TODO - YOUR CODE HERE: Node 1
# Translate state['source_text'] from English to TARGET_LANGUAGE formally.
# Use llm and return {"translated": <translation>}.
def translate_text(state: DocState):
    raise NotImplementedError("TODO: translate_text")


# TODO - YOUR CODE HERE: Node 2
# Use llm to concisely summarize state['translated'] in TARGET_LANGUAGE.
# Return {"summary": <summary>}.
def summarize_text(state: DocState):
    raise NotImplementedError("TODO: summarize_text")


# TODO - YOUR CODE HERE: Node 3
# Use llm to refine state['summary'] for readability and public-release tone.
# Keep TARGET_LANGUAGE; do not translate back to English.
# Do not add, remove or change facts (names, numbers, entities) in the summary.
# Return {"refined": <refined text>}.
def refine_summary(state: DocState):
    raise NotImplementedError("TODO: refine_summary")


# TODO - YOUR CODE HERE: Graph builder
# START -> translate_text -> summarize_text -> refine_summary -> END.
# Function and graph node names must match exactly.
# Compile with InMemorySaver so checkpoints are saved after each node.
# Return the compiled app.
def build_graph():
    raise NotImplementedError("TODO: build_graph")


# TODO - YOUR CODE HERE: Graph display
# Print the compiled graph structure; the original permits an ASCII view.
def display_graph(app):
    raise NotImplementedError("TODO: display_graph")


# PARTIALLY GIVEN - COMPLETE THE THREE TODO BLOCKS
# Run full pipeline, inspect checkpoints, revisit V1, then replay V2 and V3.
def run_test(app, source_text, thread_id="test_thread"):
    config = {"configurable": {"thread_id": thread_id}}
    final_state = app.invoke({"source_text": source_text}, config=config)
    print("\nFinal State after full pipeline:")
    print(final_state)

    # TODO - YOUR CODE HERE: 1. Show all checkpoints.
    # Fetch state history into a variable named history.
    # Print each snapshot's next value and checkpoint_id.
    # next == ('translate_text',): processing has not started
    # next == ('summarize_text',): V1 translated text is ready
    # next == ('refine_summary',): V2 summary is ready
    # next == (): V3 refined text is ready
    history = None  # Replace this placeholder and print the history.

    # TODO - YOUR CODE HERE: 2. Revisit V1.
    # Select the snapshot about to run summarize_text into variable v1.
    # Print its checkpoint_id and v1.values['translated'].
    v1 = None  # Replace this placeholder and print the selected version.

    # TODO - YOUR CODE HERE: 3. Replay from V1 to regenerate V2 and V3.
    # Hint: app.invoke with input None continues from a checkpoint.
    # Use v1.config and print the regenerated summary and refined text.
    raise NotImplementedError("TODO: checkpoint inspection, V1 selection and replay")


# GIVEN - DO NOT MODIFY: sample restored from code PDF page 16.
def main():
    app = build_graph()
    display_graph(app)
    print("\nTEST CASE 1")
    source = 'The city council approved a new policy to expand public transport. The plan adds 50 electric buses and three new metro lines over the next two years, aiming to cut traffic congestion and reduce carbon emissions across the region.'
    run_test(app, source, "doc_test_1")


if __name__ == "__main__":
    main()
