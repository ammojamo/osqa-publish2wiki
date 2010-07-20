from forum.settings.base import Setting, SettingSet
from django.forms.widgets import Textarea, TextInput, PasswordInput

PUBWIKI_SET = SettingSet('publish', 'Publish to Wiki', "Set up publishing to wiki.", 3000)

PUBWIKI_URL = Setting('PUBWIKI_URL',
"http://wiki.foobar.com/cgi-bin/twiki", PUBWIKI_SET, dict(
label = "Wiki URL",
help_text = """
Base URL of the wiki (e.g. http://host/cgi-bin/twiki)
""",
widget=TextInput))

PUBWIKI_USER = Setting('PUBWIKI_USER',
"", PUBWIKI_SET, dict(
label = "Wiki username",
help_text = "Username used to login to the wiki to publish pages",
widget=TextInput))

PUBWIKI_PASS = Setting('PUBWIKI_PASS',
"", PUBWIKI_SET, dict(
label = "Wiki password",
help_text = "Password used to login to the wiki to publish pages",
widget=PasswordInput))


PUBWIKI_FILE = Setting('PUBWIKI_FILE',
"""
# <tag> : <web/page>
# e.g. core : CoreSoftware/QandA
""", PUBWIKI_SET, dict(
label = "Wiki publishing configuration",
help_text = """
Specifies how to publish to the wiki
""",
widget=Textarea(attrs={'rows': '20'})))

