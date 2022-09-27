# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1664271955.9914792
_enable_loop = True
_template_filename = 'themes/canterville/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'content_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('pagination', context._clean_inheritance_tokens(), templateuri='pagination_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pagination')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _link = context.get('_link', UNDEFINED)
        def content_header():
            return render_content_header(context._locals(__M_locals))
        parent = context.get('parent', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        pagekind = context.get('pagekind', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        permalink = context.get('permalink', UNDEFINED)
        front_index_header = context.get('front_index_header', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        current_page = context.get('current_page', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        page_links = context.get('page_links', UNDEFINED)
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        prevlink = context.get('prevlink', UNDEFINED)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        pagination = _mako_get_namespace(context, 'pagination')
        helper = _mako_get_namespace(context, 'helper')
        index_teasers = context.get('index_teasers', UNDEFINED)
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
        permalink = context.get('permalink', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer('        <link rel="prefetch" href="')
            __M_writer(str(posts[0].permalink()))
            __M_writer('" type="text/html">\n')
        __M_writer('    ')
        __M_writer(str(math.math_styles_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        def content_header():
            return render_content_header(context)
        nextlink = context.get('nextlink', UNDEFINED)
        pagekind = context.get('pagekind', UNDEFINED)
        math = _mako_get_namespace(context, 'math')
        front_index_header = context.get('front_index_header', UNDEFINED)
        current_page = context.get('current_page', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        page_links = context.get('page_links', UNDEFINED)
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context)
        prevlink = context.get('prevlink', UNDEFINED)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        pagination = _mako_get_namespace(context, 'pagination')
        helper = _mako_get_namespace(context, 'helper')
        index_teasers = context.get('index_teasers', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\n')
        if 'main_index' in pagekind:
            __M_writer('    ')
            __M_writer(str(front_index_header))
            __M_writer('\n')
        if page_links:
            __M_writer('    ')
            __M_writer(str(pagination.page_navigation(current_page, page_links, prevlink, nextlink, prev_next_links_reversed)))
            __M_writer('\n')
        __M_writer('<div class="postindex">\n')
        for post in posts:
            __M_writer('\n\n<article class="post post">\n    <header class="post-header">\n        <h2 class="post-title"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h2>\n    </header>\n')
            if index_teasers:
                __M_writer('    <section class="post-excerpt">\n    ')
                __M_writer(str(post.text(teaser_only=True)))
                __M_writer('\n')
            else:
                __M_writer('    <section class="post-excerpt">\n    ')
                __M_writer(str(post.text(teaser_only=False)))
                __M_writer('\n')
            __M_writer('    </section>\n    <footer class="post-meta">\n')
            if author_pages_generated:
                __M_writer('                <a href="')
                __M_writer(str(_link('author', post.author())))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('</a>\n')
            else:
                __M_writer('                ')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('\n')
            __M_writer('\n        on\n')
            for tag in post.tags:
                __M_writer('                <a href="link://tag/')
                __M_writer(str(tag))
                __M_writer('">#')
                __M_writer(str(tag))
                __M_writer('</a>,\n')
            __M_writer('\n        <time class="post-date" datetime="')
            __M_writer(str(post.formatted_date('webiso')))
            __M_writer('">\n            ')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('\n        </time>\n    </footer>\n</article>\n')
        __M_writer('</div>\n')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        __M_writer(str(math.math_scripts_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_header():
            return render_content_header(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/canterville/templates/index.tmpl", "uri": "index.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 5, "38": 0, "68": 2, "69": 3, "70": 4, "71": 5, "72": 6, "77": 14, "82": 62, "88": 8, "99": 8, "100": 9, "101": 9, "102": 10, "103": 11, "104": 11, "105": 11, "106": 13, "107": 13, "108": 13, "114": 16, "138": 16, "143": 17, "144": 18, "145": 19, "146": 19, "147": 19, "148": 21, "149": 22, "150": 22, "151": 22, "152": 24, "153": 25, "154": 26, "155": 30, "156": 30, "157": 30, "158": 30, "159": 32, "160": 33, "161": 34, "162": 34, "163": 35, "164": 36, "165": 37, "166": 37, "167": 39, "168": 41, "169": 42, "170": 42, "171": 42, "172": 42, "173": 42, "174": 43, "175": 44, "176": 44, "177": 44, "178": 46, "179": 48, "180": 49, "181": 49, "182": 49, "183": 49, "184": 49, "185": 51, "186": 52, "187": 52, "188": 53, "189": 53, "190": 58, "191": 59, "192": 59, "193": 60, "194": 60, "195": 61, "196": 61, "202": 17, "213": 202}}
__M_END_METADATA
"""
