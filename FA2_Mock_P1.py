"""FA2 Mock P1: Multi-Tool AI Research Assistant (40 marks).
Reconstructed practice template; complete TODOs, preserve GIVEN sections.
Rename for submission to FA2_Mock_<Emp_Num>_P1.py.
This file intentionally has unfinished sections, not a completed solution.
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
class State(TypedDict):
    claim: str
    claim_type: str
    tool_used: str
    evidence: dict
    confidence: float
    human_feedback: Optional[str]
    final_report: str

# GIVEN - DO NOT MODIFY: exact claim text is used for dictionary lookups.
# Evidence is assessment fixture text, not a live fact-checking service.
CLIMATE_DATA = {'India renewable energy capacity grew by 30% in 2024': ["IEA Report (2024): India's renewable "
                                                         'capacity increased by 28% '
                                                         'year-over-year.',
                                                         'Bloomberg Energy Outlook: India ranked '
                                                         'third globally in new solar '
                                                         'installations.',
                                                         'Government Data: Installed capacity '
                                                         'reached 192 GW of renewables by late '
                                                         '2024.'],
 'Ocean temperatures hit record highs in 2024': ['NOAA Data: 2024 was the warmest year for ocean '
                                                 'surface temperatures since 1880.',
                                                 'Nature Climate Journal: Average ocean '
                                                 'temperature anomalies exceeded 1.2 degrees '
                                                 'Celsius globally.',
                                                 'UN Climate Division: Marine heatwaves affected '
                                                 "48% of world's oceans in 2024."]}

GENERAL_FACT_DATA = {'AI replaced 40% of human jobs in 2024': ['OECD Study: Automation affected about 11% of roles '
                                           'globally by 2024.',
                                           'McKinsey Report: AI adoption created new roles, '
                                           'offsetting large-scale job losses.',
                                           'Tech Review: AI shifted, not replaced, major segments '
                                           'of the workforce.'],
 'Global inflation rate dropped in 2024': ['IMF Report: Global inflation fell from 8.1% in 2023 to '
                                           '6.3% in 2024.',
                                           'World Bank Data: Several economies saw moderation in '
                                           'core inflation post-Q2 2024.',
                                           'Financial Times: Central banks eased interest rates in '
                                           'response to declining inflation.']}

# TODO - YOUR CODE HERE: Tools
# Define two @tool-decorated functions, using the exact names below.
# Each accepts query: str, looks up the corresponding dictionary, and returns
# {"evidence": [<evidence strings>]}.
# Unknown queries must return a placeholder LIST explaining no match was found.
# Add meaningful tool docstrings and the decorators as part of your answer.
def climate_data_tool(query: str):
    raise NotImplementedError("TODO: climate_data_tool")


def general_fact_tool(query: str):
    raise NotImplementedError("TODO: general_fact_tool")


# TODO - YOUR CODE HERE: Tool registration
# tools: list of the two tools
# tools_by_name: tool-name -> tool lookup dictionary
# llm_with_tools: llm with tools bound
# These empty values only keep the starter syntactically valid.
tools = []
tools_by_name = {}
llm_with_tools = None


# TODO - YOUR CODE HERE: Node 1
# Use llm to classify state['claim'] into exactly one of:
# Environmental, Economic, Technological.
# Return {"claim_type": <single category string>}.
def classify_claim(state: State):
    raise NotImplementedError("TODO: classify_claim")


# TODO - YOUR CODE HERE: Node 2
# Use llm_with_tools to select and invoke exactly ONE tool:
# Environmental -> climate_data_tool
# Economic or Technological -> general_fact_tool
# Pass the ORIGINAL claim as query (exact dictionary lookup).
# Inspect response.tool_calls and handle an empty tool-call list.
# Return {"tool_used": <tool name>, "evidence": <tool output dict>}.
# This FUNCTION is registered with graph node name 'retrieve_evidence'.
def decide_and_invoke_tool(state: State):
    raise NotImplementedError("TODO: decide_and_invoke_tool")


# TODO - YOUR CODE HERE: Node 3
# Use llm to score how well the evidence supports the claim.
# Prefer low confidence when evidence and claim do not strongly align.
# Return {"confidence": <float between 0.0 and 1.0>}.
def verify_confidence(state: State):
    raise NotImplementedError("TODO: verify_confidence")


# TODO - YOUR CODE HERE: Node 4
# Pause with interrupt(), passing claim, evidence and confidence.
# Return {"human_feedback": <resumed value>}.
def human_review(state: State):
    raise NotImplementedError("TODO: human_review")


# TODO - YOUR CODE HERE: Node 5
# Use llm to create the verification report. Return {"final_report": <text>}.
# Include Claim Type, Tool Invoked, Confidence, Decision,
# Human Feedback (or 'Not Required'), and a two-line Final Report.
# This FUNCTION is registered with graph node name 'finalize_report'.
def generate_final_report(state: State):
    raise NotImplementedError("TODO: generate_final_report")


# TODO - YOUR CODE HERE: Graph builder
# Register graph nodes exactly as:
# classify_claim, retrieve_evidence, verify_confidence, human_review, finalize_report.
# Start at classify_claim, retrieve evidence, then verify confidence.
# Confidence >= 0.7: finalize_report. Confidence < 0.7: human_review.
# After human_review: finalize_report. Then END.
# Compile with an InMemorySaver checkpointer and return the compiled app.
def build_graph():
    raise NotImplementedError("TODO: build_graph")


# TODO - YOUR CODE HERE: Graph display
# Print the compiled graph structure; the original permits an ASCII view.
def display_graph(app):
    raise NotImplementedError("TODO: display_graph")


# PARTIALLY GIVEN - COMPLETE THE TODO
# Original driver restored from code PDF page 10.
def run_test(app, claim, thread_id="test_thread"):
    config = {"configurable": {"thread_id": thread_id}}
    result = app.invoke({"claim": claim}, config=config)
    print("\nInitial Output:\n", result)

    # TODO - YOUR CODE HERE: handle an interrupt ONLY if one occurred.
    # Prompt for human feedback and resume with Command(resume=<feedback>).
    # Reuse the SAME app and thread config. Print the completed output.
    raise NotImplementedError("TODO: interrupt handling")


# GIVEN - DO NOT MODIFY
def main():
    app = build_graph()
    display_graph(app)
    print("\nTEST CASE 1: Technological (HIL expected)")
    run_test(app, "AI replaced 40% of human jobs in 2024", "claim_test_1")
    print("\nTEST CASE 2: Environmental (Auto-Verified)")
    run_test(app, "Ocean temperatures hit record highs in 2024", "claim_test_2")


if __name__ == "__main__":
    main()
