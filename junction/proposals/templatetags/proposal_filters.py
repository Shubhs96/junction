# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# Third Party Stuff
from django import template


register = template.Library()


@register.filter(name='reviewer_comments')
def reviewer_comments(proposal, user):
    return proposal.get_reviewer_comments_count(user) > 0

@register.filter(name='has_content_urls')
def has_content_urls(proposal):
    if proposal.content_urls:
        return True
    else:
        return False
