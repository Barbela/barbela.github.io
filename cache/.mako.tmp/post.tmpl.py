# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1664271955.900185
_enable_loop = True
_template_filename = 'themes/canterville/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('pheader', context._clean_inheritance_tokens(), templateuri='post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pheader')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _link = context.get('_link', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        post = context.get('post', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        post = context.get('post', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        math = _mako_get_namespace(context, 'math')
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if post.meta('keywords'):
            __M_writer('    <meta name="keywords" content="')
            __M_writer(filters.html_escape(str(post.meta('keywords'))))
            __M_writer('">\n')
        __M_writer('    <meta name="author" content="')
        __M_writer(filters.html_escape(str(post.author())))
        __M_writer('">\n')
        if post.prev_post:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(post.prev_post.permalink()))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.prev_post.title())))
            __M_writer('" type="text/html">\n')
        if post.next_post:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(post.next_post.permalink()))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.next_post.title())))
            __M_writer('" type="text/html">\n')
        if post.is_draft:
            __M_writer('        <meta name="robots" content="noindex">\n')
        __M_writer('    ')
        __M_writer(str(helper.open_graph_metadata(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.twitter_card_information(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.meta_translations(post)))
        __M_writer('\n    ')
        __M_writer(str(math.math_styles_ifpost(post)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        post = context.get('post', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        math = _mako_get_namespace(context, 'math')
        def content():
            return render_content(context)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n  <article class="post post">\n    <header class="post-header">\n        <h1 class="post-title">')
        __M_writer(str(post.title()))
        __M_writer('</h1>\n        <section class="post-meta"> by\n')
        if author_pages_generated:
            __M_writer('            <a href="')
            __M_writer(str(_link('author', post.author())))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.author())))
            __M_writer('</a>\n')
        else:
            __M_writer('            ')
            __M_writer(filters.html_escape(str(post.author())))
            __M_writer('\n')
        __M_writer('            on\n')
        for tag in post.tags:
            __M_writer('                <a href="link://tag/')
            __M_writer(str(tag))
            __M_writer('">#')
            __M_writer(str(tag))
            __M_writer('</a>,\n')
        __M_writer('            <time class="post-date" datetime="')
        __M_writer(str(post.formatted_date('webiso')))
        __M_writer('">\n                ')
        __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
        __M_writer('\n            </time>\n        </section>\n    </header>\n\n    <section class="post-content">\n    ')
        __M_writer(str(post.text()))
        __M_writer('\n    </section>\n    <footer class="post-footer">\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('        <section class="comments hidden-print">\n        <h2>')
            __M_writer(str(messages("Comments")))
            __M_writer('</h2>\n        ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post._base_path)))
            __M_writer('\n        </section>\n')
        __M_writer('    ')
        __M_writer(str(math.math_scripts_ifpost(post)))
        __M_writer('\n</article>\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/canterville/templates/post.tmpl", "uri": "post.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 5, "38": 0, "57": 2, "58": 3, "59": 4, "60": 5, "61": 6, "66": 27, "71": 63, "77": 8, "87": 8, "88": 9, "89": 9, "90": 10, "91": 11, "92": 11, "93": 11, "94": 13, "95": 13, "96": 13, "97": 14, "98": 15, "99": 15, "100": 15, "101": 15, "102": 15, "103": 17, "104": 18, "105": 18, "106": 18, "107": 18, "108": 18, "109": 20, "110": 21, "111": 23, "112": 23, "113": 23, "114": 24, "115": 24, "116": 25, "117": 25, "118": 26, "119": 26, "125": 29, "139": 29, "140": 33, "141": 33, "142": 35, "143": 36, "144": 36, "145": 36, "146": 36, "147": 36, "148": 37, "149": 38, "150": 38, "151": 38, "152": 40, "153": 41, "154": 42, "155": 42, "156": 42, "157": 42, "158": 42, "159": 44, "160": 44, "161": 44, "162": 45, "163": 45, "164": 51, "165": 51, "166": 54, "167": 55, "168": 56, "169": 56, "170": 57, "171": 57, "172": 60, "173": 60, "174": 60, "175": 62, "176": 62, "182": 176}}
__M_END_METADATA
"""
