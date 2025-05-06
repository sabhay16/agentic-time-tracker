import openai
from config import OPENAI_API_KEY

class TimesheetAgent:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY

    def suggest_entries(self, user_context):
        system_prompt = "You are a helpful assistant that generates time entries for consultants based on previous work patterns, calendar events, and tasks."

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Context: {user_context}"}
        ]

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages,
                functions=[
                    {
                        "name": "add_time_entry",
                        "description": "Suggest a time entry",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "date": {"type": "string", "format": "date"},
                                "hours": {"type": "number"},
                                "project": {"type": "string"},
                                "notes": {"type": "string"}
                            },
                            "required": ["date", "hours", "project"]
                        }
                    }
                ],
                function_call="auto"
            )
            fn_call = response.choices[0].message.get("function_call", {})
            if fn_call.get("name") == "add_time_entry":
                import json
                return json.loads(fn_call.get("arguments", "{}"))
            return {}
        except Exception as e:
            print("OpenAI error:", e)
            return {}