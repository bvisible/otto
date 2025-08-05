// Copyright (c) 2025, Alan Tom and contributors
// For license information, please see license.txt

frappe.ui.form.on("Otto Settings", {
	refresh(frm) {
		// Add test button next to local_api_base field
		frm.add_custom_button(
			__("Test Local Server"),
			function () {
				if (!frm.doc.local_api_base) {
					frappe.msgprint(__("Please enter a Local LLM Server URL first"));
					return;
				}

				frappe.call({
					method: "test_local_connection",
					doc: frm.doc,
					callback: function (r) {
						// Success message is handled in the Python method
					},
				});
			},
			__("Actions")
		);
	},
});
