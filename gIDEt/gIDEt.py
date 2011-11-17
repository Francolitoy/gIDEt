from gi.repository import GObject, Gtk, Gedit
import os

class GIDEt(GObject.Object, Gedit.WindowActivatable):
    __gtype_name__ = "gIDEt"
    window = GObject.property(type=Gedit.Window)
    
    def __init__(self):
        GObject.Object.__init__(self)
        
    def do_activate(self):
        icon = Gtk.Image.new_from_stock(Gtk.STOCK_YES, Gtk.IconSize.MENU)
        panel = self.window.get_side_panel()

        column = Gtk.TreeViewColumn()
        column.set_title("gIDEt")

        cell = Gtk.CellRendererPixbuf()
        column.pack_start(cell, False)
	#column.add_attribute(cell, property, indice del parametro del Treestore)
        column.add_attribute(cell, "stock-id", 0)

        cell = Gtk.CellRendererText()
        column.pack_start(cell, True)
        column.add_attribute(cell, "text", 1)
        column.add_attribute(cell, "editable", 3)
 
        treestore = Gtk.TreeStore(GObject.TYPE_STRING,    # icon
                                    GObject.TYPE_STRING,    # name
                                    GObject.TYPE_STRING,    # uri
                                    GObject.TYPE_INT)       # editable 
 
	#Recorre los el path
	parents = {}
        for dir, dirs, files in os.walk('./'):
            for subdir in dirs:
                parents[os.path.join(dir, subdir)] = treestore.append(parents.get(dir, None), [Gtk.STOCK_FILE, subdir, "dir", 0])
            for item in files:
                treestore.append(parents.get(dir, None), [Gtk.STOCK_FILE, item, "uri", 0])

        # create the treeview
        self._treeview = Gtk.TreeView.new_with_model(treestore)

	#(2) indice del parametro del Treestore
	self._treeview.set_tooltip_column(2)
        self._treeview.append_column(column)

	#crea el Scrool
   	scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self._treeview)

	#El escroll tienen q estar en un Box (VBox o HBox)
        self._panel_widget = Gtk.VBox(homogeneous=False, spacing=2)
        self._panel_widget.pack_start(scrolled, True, True, 0)
        self._panel_widget.show_all()
        
        # add the panel
        panel = self.window.get_side_panel()
        panel.add_item(self._panel_widget, "gIDEt", "gIDEt", icon)
        
        
        # drag and drop not working in GTK+ 3.0. A patch has been committed.
        self._treeview.set_reorderable(True) 

    def do_deactivate(self):
        panel = self.window.get_side_panel()
        panel.remove_item(self._side_widget)

    def do_update_state(self):
        pass