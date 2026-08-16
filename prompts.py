SUMMARY_PROMPT_V1 = "Summarize this: {letter_text}"

SUMMARY_PROMPT_V2 = "Summarize this loan application:\n\n{letter_text}"

EXTRACT_SYSTEM_PROMPT = """You are an assistant to a microfinance loan officer. Extract the following information from the loan application letter and return it as a JSON object with EXACTLY these keys: applicant_name (string), amount_ghs (number), purpose (string), monthly_profit_ghs (number or null), has_collateral_or_guarantor (boolean), repayment_months (number or null). If a field is not stated in the letter, use null. Do not guess.
Output ONLY the JSON object. No explanation, no markdown code fences, no extra text."""

FEW_SHOT_EXAMPLE = """Dear Sir/Madam, My name is Yaw Owusu and I sell hardware supplies in Techiman. I am requesting a loan of
GHS 5,000 to restock my shop before the planting season. My shop currently makes about
GHS 600 profit per month. My uncle, a retired civil servant, will act as my guarantor.
I intend to repay within 10 months.
Thank you,
Yaw Owusu"""

FEW_SHOT_EXAMPLE_OUTPUT = """{
"applicant_name": "Yaw Owusu","amount_ghs": 5000,"purpose": "restock hardware shop before planting season","monthly_profit_ghs": 600,"has_collateral_or_guarantor": true,"repayment_months": 10}""" 

EXTRACT_PROMPT = """Here is an example of how to extract information from a loan application letter:
Letter: {few_shot_example}

Output: {few_shot_example_output}

Now extract the same fields from this letter:

Letter: {letter_text}

Output:"""