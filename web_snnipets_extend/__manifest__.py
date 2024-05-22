# -*- coding: utf-8 -*-
{
    'name': 'Web snippets extend',
    'category': 'Website',
    "sequence": 3,
    'version': '17.0.1.0',
    'license': 'LGPL-3',
    'author': 'click',
    'website': '',
    'data': [
        'views/assets.xml',
        'views/snippets/slider.xml',
        'views/snippets/about-us.xml',
        'views/snippets/ourcourse.xml',
        'views/snippets/achievement.xml',
        'views/snippets/teacher.xml',
        'views/snippets/event.xml',
        'views/snippets/newsfeed.xml',
        'views/snippets/footer.xml',
        'views/snippets/s_faq1_collapse.xml',
        'views/image_library.xml',
    ],
    'qweb': [
        "static/src/xml/base_inherit.xml",
    ],
    'demo': [
        'data/homepage_demo.xml',
        'data/footer_template.xml',
    ],
    'images': [
        'static/description/web_snnipets_extend_banner.jpg',
    ],
    'depends': [
        'website',
        'web',
    ],
    'application': True,
    'assets': {
        'web.assets_frontend': [
            '/web_snnipets_extend/static/src/scss/homepage.scss',
            '/web_snnipets_extend/static/src/snippets/s_faq1_collapse/001.scss',
        ],
        'web._assets_primary_variables': [
            '/web_snnipets_extend/static/src/scss/primary_variables.scss'
        ],
    }
}
