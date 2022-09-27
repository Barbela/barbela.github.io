# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1664271955.932394
_enable_loop = True
_template_filename = 'themes/canterville/templates/base.tmpl'
_template_uri = 'base.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'extra_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

    ns = runtime.TemplateNamespace('header', context._clean_inheritance_tokens(), templateuri='base_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'header')] = ns

    ns = runtime.TemplateNamespace('footer', context._clean_inheritance_tokens(), templateuri='base_footer.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'footer')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        header = _mako_get_namespace(context, 'header')
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        footer = _mako_get_namespace(context, 'footer')
        GITHUB_URL = _import_ns.get('GITHUB_URL', context.get('GITHUB_URL', UNDEFINED))
        LINKEDIN_URL = _import_ns.get('LINKEDIN_URL', context.get('LINKEDIN_URL', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        blog_url = _import_ns.get('blog_url', context.get('blog_url', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        BANNER_URL = _import_ns.get('BANNER_URL', context.get('BANNER_URL', UNDEFINED))
        TWITTER_URL = _import_ns.get('TWITTER_URL', context.get('TWITTER_URL', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer(str(set_locale(lang)))
        __M_writer('\n')
        __M_writer(str(base.html_headstart()))
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        __M_writer(str(template_hooks['extra_head']()))
        __M_writer('\n</head>\n<body class="nav-closed">\n')
        __M_writer(str(header.html_navigation_links()))
        __M_writer('\n<div class="site-wrapper">\n')
        if 'main_index' in pagekind and BANNER_URL :
            __M_writer('    <header class="main-header" style="background-image: url(')
            __M_writer(str(BANNER_URL))
            __M_writer(')">\n')
        elif 'post_page' in pagekind and post.meta('banner'):
            __M_writer('    <header class="main-header" style="background-image: url(')
            __M_writer(str(post.meta('banner')))
            __M_writer(')">\n')
        else:
            __M_writer('    <header class="main-header post-head no-cover">\n')
        __M_writer('        <nav class="main-nav overlay clearfix">\n            <a class="blog-logo" href="')
        __M_writer(str(blog_url))
        __M_writer('"><img src="')
        __M_writer(str(logo_url))
        __M_writer('" alt="Blog Logo" /></a>\n            <a class="menu-button" href="#"><span class="burger">&#9776;</span><span class="word">Menu</span></a>\n        </nav>\n')
        if 'main_index' in pagekind:
            __M_writer('        <div class="vertical">\n            <div class="main-header-content inner">\n')
            if GITHUB_URL:
                __M_writer('                <a  href="')
                __M_writer(str(GITHUB_URL))
                __M_writer('" target="_blank">\n                    <span class="icon-github" style="color:white;font-size:2em"></span>\n                </a>\n                &nbsp;\n')
            if TWITTER_URL:
                __M_writer('                <a class="bloglogo" href=')
                __M_writer(str(TWITTER_URL))
                __M_writer(' target="_blank">\n                    <span class="icon-twitter" style="color:white;font-size:2em"></span>\n                </a>\n                &nbsp;\n')
            if LINKEDIN_URL:
                __M_writer('                <a  href="')
                __M_writer(str(LINKEDIN_URL))
                __M_writer('" target="_blank">\n                    <span class="icon-linkedin" style="color:white;font-size:2em"></span>\n                </a>\n                &nbsp;\n')
            __M_writer('                <h1 class="page-title">')
            __M_writer(str(title))
            __M_writer('</h1>\n                <h2 class="page-description">')
            __M_writer(str(description))
            __M_writer('</h2>\n            </div>\n        </div>\n        <a class="scroll-down icon-arrow-left" href="#content"><span class="hidden">Scroll Down</span></a>\n')
        __M_writer('    </header>\n\n    <main id="content" class="content" role="main">\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n    </main>\n    ')
        __M_writer(str(footer.html_footer()))
        __M_writer('\n</div>\n')
        __M_writer(str(base.late_load_js()))
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\n')
        __M_writer(str(body_end))
        __M_writer('\n')
        __M_writer(str(template_hooks['body_end']()))
        __M_writer('\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'header')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'footer')._populate(_import_ns, ['*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/canterville/templates/base.tmpl", "uri": "base.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 0, "64": 2, "65": 3, "66": 4, "67": 5, "68": 5, "69": 6, "70": 6, "75": 9, "76": 10, "77": 10, "78": 13, "79": 13, "80": 15, "81": 16, "82": 16, "83": 16, "84": 17, "85": 18, "86": 18, "87": 18, "88": 19, "89": 20, "90": 22, "91": 23, "92": 23, "93": 23, "94": 23, "95": 26, "96": 27, "97": 29, "98": 30, "99": 30, "100": 30, "101": 35, "102": 36, "103": 36, "104": 36, "105": 41, "106": 42, "107": 42, "108": 42, "109": 47, "110": 47, "111": 47, "112": 48, "113": 48, "114": 53, "119": 56, "120": 58, "121": 58, "122": 60, "123": 60, "128": 61, "129": 62, "130": 62, "131": 63, "132": 63, "138": 7, "148": 7, "154": 56, "169": 61, "184": 169}}
__M_END_METADATA
"""
