SUMMARY_PROMPT_V1 = "Summarize this: {letter_text}"

SUMMARY_PROMPT_V2 = "Summarize this loan application:\n\n{letter_text}"


EXTRACT_PROMPT = """Here is an example of how to extract information from a loan application letter:
Letter: {few_shot_example}

Output: {few_shot_example_output}

Now extract the same fields from this letter:

Letter: {letter_text}

Output:"""

BRIEF_PROMPT = """Loan application letter:
{letter_text}

Extracted data:
{extracted_json}

Write the decision-support brief."""
