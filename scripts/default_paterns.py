from pprint import pprint
from emojis import encode as emojify

class DefaultInfo(object):
    """Classe apenas para armazenamento de informações padronizadas."""
    def __init__(self, label, emoji_name):
        self._label = label
        self._emoji_name = f':{emoji_name}:'
        self._emoji = emojify(self._emoji_name)

    def label():
        def fget(self):
            return self._label
        return locals()
    label = property(**label())

    def emoji_name():
        def fget(self):
            return self.emoji_name
        return locals()
    emoji_name = property(*emoji_name())

    def emoji():
        def fget(self):
            return self._emoji
        return locals()
    emoji = property(**emoji())

class TargetInfo(DefaultInfo):
    """Informações sobre alvo."""
    def __init__(self, actions, *args, **kwargs):
        super(TargetInfo, self).__init__(*args, **kwargs)
        self._actions = actions

    def actions():
        doc = "The actions property."
        def fget(self):
            return self._actions
        return locals()
    actions = property(**actions())

"""
- Metadata 	card_index :card_index:
- Improve format/structure 	art :art:

-
- Code review changes 	ok_hand :ok_hand:
"""
default_actions = (
    DefaultInfo("Work in progress", "construction"),
    DefaultInfo("Performance", "runner"),
    DefaultInfo("Reverting changes", "rewind"),
)

feat_actions = (
    *default_actions,
)

ui_focus = (
    *default_actions,
    DefaultInfo("Accessibility", "wheelchair"),
    DefaultInfo("Cosmetic", "lipstick")
)

docs_actions = (
    *ui_focus,
    DefaultInfo("Translation", "alien")
)

data_actions = (
    DefaultInfo("Translation", "alien"),
    DefaultInfo("Configuration files", "wrench"),
    DefaultInfo("Assets", "bento")
)

security_actions = (
    *default_actions,
)

test_tag = (
    DefaultInfo("Adding a test", "white_check_mark"),
    DefaultInfo("Make a test pass", "heavy_check_mark"),
)

bug_specifications = (
    DefaultInfo("Work in progress", "construction"),
    DefaultInfo('Hotfix','fire'),
    DefaultInfo('On Linux', 'penguin'),
    DefaultInfo('On Windows', 'checkered_flag'),
    DefaultInfo('On MAC', 'apple'),
)

dependencies_actions = (
    DefaultInfo("Upgrading dependencies", "arrow_up"),
    DefaultInfo("Downgrading dependencies", "arrow_down"),
    DefaultInfo("Removing a dependency", "heavy_minus_sign"),
    DefaultInfo("Adding a dependency", "heavy_plus_sign"),
)

version_actions = (
    DefaultInfo("New", "arrow_up"),
    DefaultInfo("Returning", "arrow_down")
)

refactorable = (
    TargetInfo(feat_actions, "Feat", "zap"),
    TargetInfo(docs_actions, 'Docs', 'bookmark_tabs'),
    TargetInfo(ui_focus, "UI", "art"),
    TargetInfo(security_actions, "Security", "lock"),
)

targets = (
    *refactorable,
    TargetInfo(bug_specifications, 'Bug Fix', 'bug'),
    TargetInfo(data_actions, "Data", "game_die"),
    TargetInfo(refactorable, "Refactor", "wrench"),
    TargetInfo(test_tag, "Test", "rotating_light"),
    TargetInfo(version_actions, "Version", "bookmark"),
    TargetInfo(dependencies_actions, "Dependencies", "fork_and_knife")
)
