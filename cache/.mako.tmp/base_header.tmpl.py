# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1664271955.963198
_enable_loop = True
_template_filename = 'themes/canterville/templates/base_header.tmpl'
_template_uri = 'base_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_header', 'html_site_title', 'html_navigation_links', 'html_translation_header']



from nikola.utils import slugify



from nikola.utils import slugify



from nikola.utils import slugify


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        def html_navigation_links():
            return render_html_navigation_links(context)
        def html_translation_header():
            return render_html_translation_header(context)
        def html_site_title():
            return render_html_site_title(context)
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <header id="header">\n        ')
        __M_writer(str(html_site_title()))
        __M_writer('\n        ')
        __M_writer(str(html_translation_header()))
        __M_writer('\n        ')
        __M_writer(str(html_navigation_links()))
        __M_writer('\n')
        if search_form:
            __M_writer('            <div class="searchform" role="search">\n                ')
            __M_writer(str(search_form))
            __M_writer('\n            </div>\n')
        __M_writer('    </header>\n    ')
        __M_writer(str(template_hooks['page_header']()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_site_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <h1 id="brand"><a href="')
        __M_writer(str(abs_link(_link("root", None, lang))))
        __M_writer('" title="')
        __M_writer(filters.html_escape(str(blog_title)))
        __M_writer('" rel="home">\n')
        if logo_url:
            __M_writer('        <img src="')
            __M_writer(str(logo_url))
            __M_writer('" alt="')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('" id="logo">\n')
        __M_writer('\n')
        if show_blog_title:
            __M_writer('        <span id="blog-title">')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</span>\n')
        __M_writer('    </a></h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        tuple = _import_ns.get('tuple', context.get('tuple', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n<div class="nav">\n    <h3 class="nav-title">Menu</h3>\n    <a href="#" class="nav-close">\n        <span class="hidden">Close</span>\n    </a>\n    <ul>\n')
        for url, text in navigation_links[lang]:
            if isinstance(url, tuple):
                __M_writer('            ')
                __M_writer('\n\n            <li class="nav-opened" role="presentation">\n                <a href="javascript:void(0)" class="nested-url" data-children="nested-')
                __M_writer(str(slugify(text, lang)))
                __M_writer('">\n                ')
                __M_writer(str(text))
                __M_writer('\n                </a>\n            </li>\n')
                for sublink, subtext in url:
                    __M_writer('                <li class="nav-opened nested-')
                    __M_writer(str(slugify(text, lang)))
                    __M_writer(' hidden" role="presentation">\n                    <a href="')
                    __M_writer(str(sublink))
                    __M_writer('" class="child">\n                    ')
                    __M_writer(str(subtext))
                    __M_writer('\n                    </a>\n                </li>\n')
            else:
                if rel_link(permalink, url) == "#":
                    __M_writer('            <li class="nav-opened nav-current" role="presentation">\n')
                else:
                    __M_writer('            <li class="nav-opened" role="presentation">\n')
                __M_writer('                <a href="')
                __M_writer(str(url))
                __M_writer('">')
                __M_writer(str(text))
                __M_writer('</a>\n            </li>\n')
        __M_writer('    ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\n    ')
        __M_writer(str(template_hooks['menu_alt']()))
        __M_writer('\n    </ul>\n</div>\n<span class="nav-cover"></span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translation_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            __M_writer('        <div id="toptranslations">\n            <h2>')
            __M_writer(str(messages("Languages:")))
            __M_writer('</h2>\n            ')
            __M_writer(str(base.html_translations()))
            __M_writer('\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/canterville/templates/base_header.tmpl", "uri": "base_header.tmpl", "source_encoding": "utf-8", "line_map": {"16": 39, "17": 40, "18": 41, "19": 42, "20": 39, "21": 40, "22": 41, "23": 42, "24": 39, "25": 40, "26": 41, "27": 42, "35": 2, "38": 0, "45": 2, "46": 16, "47": 28, "48": 70, "49": 79, "55": 4, "69": 4, "70": 6, "71": 6, "72": 7, "73": 7, "74": 8, "75": 8, "76": 9, "77": 10, "78": 11, "79": 11, "80": 14, "81": 15, "82": 15, "88": 18, "100": 18, "101": 19, "102": 19, "103": 19, "104": 19, "105": 20, "106": 21, "107": 21, "108": 21, "109": 21, "110": 21, "111": 23, "112": 24, "113": 25, "114": 25, "115": 25, "116": 27, "122": 30, "135": 30, "136": 37, "137": 38, "138": 39, "139": 41, "140": 44, "141": 44, "142": 45, "143": 45, "144": 48, "145": 49, "146": 49, "147": 49, "148": 50, "149": 50, "150": 51, "151": 51, "152": 55, "153": 56, "154": 57, "155": 58, "156": 59, "157": 61, "158": 61, "159": 61, "160": 61, "161": 61, "162": 65, "163": 65, "164": 65, "165": 66, "166": 66, "172": 72, "182": 72, "183": 73, "184": 74, "185": 75, "186": 75, "187": 76, "188": 76, "194": 188}}
__M_END_METADATA
"""
