# Copyright (c) 2025, Alan Tom and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class OttoSettings(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		anthropic_api_key: DF.Password | None
		gemini_api_key: DF.Password | None
		global_env: DF.JSON | None
		is_enabled: DF.Check
		local_api_base: DF.Data | None
		max_llm_calls: DF.Int
		openai_api_key: DF.Password | None
		task_execution_timeout: DF.Int
	# end: auto-generated types

	@frappe.whitelist()
	def test_local_connection(self):
		"""Test if local LLM server is accessible"""
		import requests
		
		if not self.local_api_base:
			frappe.throw("Local API base URL not configured")
		
		try:
			# Remove trailing slash if present
			base_url = self.local_api_base.rstrip("/")
			
			# Test OpenAI-compatible /models endpoint
			response = requests.get(f"{base_url}/models", timeout=5)
			
			if response.status_code == 200:
				data = response.json()
				models = data.get("data", [])
				model_ids = [m.get("id", "unknown") for m in models]
				
				frappe.msgprint(
					f"✅ Server accessible!<br>"
					f"<b>{len(models)}</b> models available:<br>"
					f"{'<br>'.join(f'• {m}' for m in model_ids[:5])}"
					f"{'<br>• ...' if len(model_ids) > 5 else ''}",
					title="Local LLM Server Test",
					indicator="green"
				)
				return {"status": "success", "models": model_ids}
			else:
				frappe.throw(f"Server returned status code: {response.status_code}")
				
		except requests.exceptions.RequestException as e:
			frappe.throw(
				f"Failed to connect to local server:<br>{str(e)}",
				title="Connection Error"
			)
