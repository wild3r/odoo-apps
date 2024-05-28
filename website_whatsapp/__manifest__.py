{
    "name": "Website Whatsapp",
    "summary": "Whatsapp integration",
    "category": "Website",
    "version": "17.0.1.0.0",
    "website": "",
    "author": "",
    "maintainers": ["wilder"],
    "license": "AGPL-3",
    "depends": ["website"],
    "data": [
        "templates/website.xml",
        "views/res_config_settings.xml",
    ],
    "assets": {
        "web.assets_frontend": ["/website_whatsapp/static/src/scss/website.scss"]
    },
    "installable": True,
}
