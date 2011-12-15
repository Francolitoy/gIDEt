GSCHEMA_ID_BASE = 'org.gnome.gedit.plugins.configmaster'
GSCHEMA_ID_PLUGINS = GSCHEMA_ID_BASE + '.plugins'
GSCHEMA_ID_PREFS_EDITOR = GSCHEMA_ID_BASE + '.preferences.editor'
GSCHEMA_ID_PREFS_UI = GSCHEMA_ID_BASE + '.preferences.ui'

UI_XML = """<ui>
  <menubar name="MenuBar">
    <menu name="ToolsMenu" action="Tools">
      <placeholder name="ToolsOps_3">
        <menuitem name="RubyConfig" action="RubyConfig"/>
      </placeholder>
      <placeholder name="ToolsOps_4">
        <menuitem name="PythonConfig" action="PythonConfig"/>
      </placeholder>
    </menu>
  </menubar>
</ui>"""

TYPE_STRING = 'string'
TYPE_BOOLEAN = 'boolean'
TYPE_UINT = 'uint'
TYPE_LIST_STRING = 'strv'

# plugins
OPT_ACTIVE_PLUGINS = ('active-plugins', TYPE_LIST_STRING)

# preferences-editor
OPT_EDITOR_FONT = ('editor-font', TYPE_STRING)
OPT_SCHEME = ('scheme', TYPE_STRING)
OPT_CREATE_BACKUP_COPY = ('create-backup-copy', TYPE_BOOLEAN)
OPT_AUTO_SAVE = ('auto-save', TYPE_BOOLEAN)
OPT_AUTO_SAVE_INTERVAL = ('auto-save-interval', TYPE_UINT)
OPT_TABS_SIZE = ('tabs-size', TYPE_UINT)
OPT_INSERT_SPACES = ('insert-spaces', TYPE_BOOLEAN)
OPT_AUTO_INDENT = ('auto-indent', TYPE_BOOLEAN)
OPT_DISPLAY_LINE_NUMBERS = ('display-line-numbers', TYPE_BOOLEAN)
OPT_HIGHLIGHT_CURRENT_LINE = ('highlight-current-line', TYPE_BOOLEAN)
OPT_BRACKET_MATCHING = ('bracket-matching', TYPE_BOOLEAN)
OPT_DISPLAY_RIGHT_MARGIN = ('display-right-margin', TYPE_BOOLEAN)
OPT_RIGHT_MARGIN_POSITION = ('right-margin-position', TYPE_UINT)

# preferences-ui
OPT_TOOLBAR_VISIBLE = ('toolbar-visible', TYPE_BOOLEAN)
OPT_STATUSBAR_VISIBLE = ('statusbar-visible', TYPE_BOOLEAN)
OPT_SIDE_PANEL_VISIBLE = ('side-panel-visible', TYPE_BOOLEAN)
OPT_BOTTOM_PANEL_VISIBLE = ('bottom-panel-visible', TYPE_BOOLEAN)
OPT_MAX_RECENTS = ('max-recents', TYPE_UINT)

ALL_SETTINGS = [OPT_ACTIVE_PLUGINS, OPT_EDITOR_FONT, OPT_SCHEME, OPT_CREATE_BACKUP_COPY, OPT_AUTO_SAVE, OPT_AUTO_SAVE_INTERVAL, OPT_TABS_SIZE, OPT_INSERT_SPACES, OPT_AUTO_INDENT, OPT_DISPLAY_LINE_NUMBERS, OPT_HIGHLIGHT_CURRENT_LINE, OPT_BRACKET_MATCHING, OPT_DISPLAY_RIGHT_MARGIN, OPT_RIGHT_MARGIN_POSITION, OPT_TOOLBAR_VISIBLE, OPT_STATUSBAR_VISIBLE, OPT_SIDE_PANEL_VISIBLE, OPT_BOTTOM_PANEL_VISIBLE, OPT_MAX_RECENTS]