
if(!window.creative) window.creative = {};

// Add / update a new Lead / Communication
// subject, sender, description
frappe.send_message = function(opts, btn) {
	return frappe.call({
		type: "POST",
		method: "creative.templates.utils.send_message",
		btn: btn,
		args: opts,
		callback: opts.callback
	});
};

creative.subscribe_to_newsletter = function(opts, btn) {
	return frappe.call({
		type: "POST",
		method: "frappe.email.doctype.newsletter.newsletter.subscribe",
		btn: btn,
		args: {"email": opts.email},
		callback: opts.callback
	});
}

// for backward compatibility
creative.send_message = frappe.send_message;
