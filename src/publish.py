from forum.models import Question
from django.utils.translation import ugettext as _
from django.http import HttpResponse
from urllib import unquote
import markdown
import httplib
import urllib	
import urllib2
import settings
from forum.settings import APP_URL
from forum.actions import AskAction, AnswerAction, CommentAction

def publish(tags):
    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, settings.PUBWIKI_URL.value, settings.PUBWIKI_USER.value, settings.PUBWIKI_PASS.value)
    authhandler = urllib2.HTTPBasicAuthHandler(passman)
    opener = urllib2.build_opener(authhandler)
    urllib2.install_opener(opener)

    for line in settings.PUBWIKI_FILE.value.split('\n'):
        if not line.startswith('#'):
            tag, sep, page = line.partition(':')
            tag = tag.strip()
            page = page.strip()
            if tag in tags:

                questions = Question.objects.filter(tags__name=unquote(tag))
                text = "---+!! Q and A\n"
                text += "This page is automatically generated - any edits will be lost\n\n"
                test += "%TOC%\n\n"
                for question in questions:
                    text += '---++ Question: ' + question.headline + '\n\n'
                    text += APP_URL + question.get_absolute_url() + '\n\n'
                    text += markdown.markdown(question.body) + '\n\n'
                    for answer in question.answers:
                        text += '---+++ Answer\n\n' + markdown.markdown(answer.body) + '\n\n'

                pagehandle = urllib2.urlopen(
                    settings.PUBWIKI_URL.value + '/save/' + page,
                    urllib.urlencode({
                        'text': text.encode('utf-8')
                    }));
#                print "Published %d questions tagged %s to %s" % (len(questions), tag, page)

def question_posted(action, new):
    question = action.node
    question_updated(question)

def answer_posted(action, new):
    answer = action.node
    question = answer.question
    question_updated(question)

def comment_posted(action, new):
    comment = action.node
    post = comment.parent
    if post.__class__ == Question:
        question = post
    else:
        question = post.question
    question_updated(question)

def question_updated(question):
    publish(question.tagname_list())

AskAction.hook(question_posted)
AnswerAction.hook(answer_posted)
CommentAction.hook(comment_posted)

