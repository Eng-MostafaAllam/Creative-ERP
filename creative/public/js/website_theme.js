
frappe.ui.form.on('Website Theme', {
	validate(frm) {
		let theme_scss = frm.doc.theme_scss;
		if (theme_scss && theme_scss.includes('frappe/public/scss/website')
			&& !theme_scss.includes('creative/public/scss/website')
		) {
			frm.set_value('theme_scss',
				`${frm.doc.theme_scss}\n@import "creative/public/scss/website";`);
		}
	}
});
