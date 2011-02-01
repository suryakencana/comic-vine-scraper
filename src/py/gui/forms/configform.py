'''
@author: Cory Banack
'''
# corylow: comment and cleanup this file

import clr
import log
from cvform import CVForm 
from configuration import Configuration

clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import AutoScaleMode, Button, CheckBox, \
    CheckedListBox, DialogResult, FlatStyle, Label, SelectionMode, \
    TabControl, TabPage

clr.AddReference('System.Drawing')
from System.Drawing import Point, Size

# =============================================================================
class ConfigForm(CVForm):
   '''
   This class is a popup, modal dialog that displays all of the configurable
   options available to the user.   The user can change any of the options, 
   and then click OK or Cancel to quit the dialog and contine the normal 
   execution of the program.   Clicking Cancel will discard any configuration
   changes that were made; clicking OK will save them permanently.
   '''
   
   # these are the strings that the user sees for each checkbox; they can 
   # also be used to reference each checkbox inside the checkboxlist
   __SERIES_CB = 'Series'
   __NUMBER_CB = 'Number'
   __MONTH_CB = 'Month'
   __TITLE_CB = 'Title'
   __ALT_SERIES_CB = 'Alternate Series'
   __WRITER_CB = 'Writer'
   __PENCILLER_CB = 'Penciller'
   __INKER_CB = 'Inker'
   __COVER_ARTIST_CB = 'Cover Artist'
   __COLORIST_CB = 'Colorist'
   __LETTERER_CB = 'Letterer'
   __EDITOR_CB = 'Editor'
   __SUMMARY_CB = 'Summary'
   __YEAR_CB = 'Year'
   __IMPRINT_CB = 'Imprint'
   __PUBLISHER_CB = 'Publisher'
   __VOLUME_CB = 'Volume'
   __CHARACTERS_CB = 'Characters'
   __TEAMS_CB = 'Teams'
   __LOCATIONS_CB = 'Locations'
   __WEBPAGE_CB = 'Webpage'
   __RATING_CB = 'Rating'

   
   # ==========================================================================
   def __init__(self, owner):
      ''' 
      Initializes this form.
      owner -> this form's owner window/dialog
      '''
      
      # the ok button for this dialog
      self.__ok_button = None
      
      # the cancel button for this dialog
      self.__cancel_button = None
      
      # the restore defaults button for this dialog
      self.__restore_button = None
      
      # "options" checkboxes
      self.__ow_existing_cb = None 
      self.__ignore_blanks_cb = None                                          
      self.__specify_series_cb = None
      self.__convert_imprints_cb = None
      self.__show_covers_cb = None
      self.__summary_dialog_cb = None
      self.__download_thumbs_cb = None
      self.__preserve_thumbs_cb = None
      self.__scrape_in_groups_cb = None
      self.__fast_rescrape_cb = None
      self.__rescrape_tags_cb = None
      self.__rescrape_notes_cb = None
      
      
      # "data" checkbox list
      self.__update_checklist = None
      
      CVForm.__init__(self, owner, "configformLocation")
      self.__build_gui()
          
          
   # ==========================================================================          
   def __build_gui(self):
      ''' Constructs and initializes the gui for this form. '''
      
      # 1. --- build each gui component
      self.__ok_button = self.__build_okbutton()
      self.__cancel_button = self.__build_cancel_button()
      self.__restore_button = self.__build_restore_button()
      tabcontrol = self.__build_tabcontrol()
         
      # 2. -- configure this form, and add all the gui components to it
      self.AutoScaleMode = AutoScaleMode.Font
      self.ClientSize = Size(396, 335)
      self.Text = 'Comic Vine Scraper Settings'
   
      self.Controls.Add(self.__ok_button)                                     
      self.Controls.Add(self.__cancel_button)                                 
      self.Controls.Add(self.__restore_button)                                
      self.Controls.Add(tabcontrol)                             
      
      # 3. -- define the keyboard focus tab traversal ordering
      self.__ok_button.TabIndex = 0                                        
      self.__cancel_button.TabIndex = 1                                    
      self.__restore_button.TabIndex = 2
      tabcontrol.TabIndex = 3                                 

      self.__update_gui_fired()  

      
   # ==========================================================================
   def __build_okbutton(self):
      ''' builds and returns the ok button for this form '''
      
      button = Button()
      button.DialogResult = DialogResult.OK
      button.Location = Point(228, 300)
      button.Size = Size(75, 23)
      button.Text = '&Ok'
      return button

   
   # ==========================================================================
   def __build_restore_button(self):
      ''' builds and returns the restore button for this form '''
      
      button = Button()
      button.Click += self.__restore_defaults_fired
      button.Location = Point(10, 300)
      button.Size = Size(150, 23)
      button.Text = '&Restore Defaults'
      return button

   
   # ==========================================================================
   def __build_cancel_button(self):
      ''' builds and returns the cancel button for this form '''
      
      button = Button()
      button.DialogResult = DialogResult.Cancel
      button.Location = Point(309, 300)
      button.Size = Size(75, 23)
      button.Text = '&Cancel'
      return button

      
   # ==========================================================================
   def __build_tabcontrol(self):
      ''' builds and returns the TabControl for this dialog '''
      
      tabcontrol = TabControl()
      tabcontrol.Location = Point(10, 15)
      tabcontrol.Size = Size(375, 265)
      
      tabcontrol.Controls.Add( self.__build_detailstab() )
      tabcontrol.Controls.Add( self.__build_behaviourtab() )
      tabcontrol.Controls.Add( self.__build_datatab() )
      
      return tabcontrol

 
   
   # ==========================================================================
   def __build_detailstab(self):
      ''' builds and returns the "Details" Tab for the TabControl '''
      
      tabpage = TabPage()
      tabpage.Text = "Details"
      
      # 1. --- a description label for this tabpage
      label = Label()
      label.AutoSize = True
      label.Location = Point(9, 20)
      label.Size = Size(299, 13)
      label.Text = 'Please choose which details you want to update:'
      
      # 2. --- the 'select all' button
      checkall_button = Button()
      checkall_button.Click += self.__checkall_fired
      checkall_button.Location = Point(275, 97)
      checkall_button.Size = Size(80, 23)
      checkall_button.Text = 'Select &All'
      
      # 3. --- the 'deselect all' button
      uncheckall_button = Button()
      uncheckall_button.Click += self.__uncheckall_fired
      uncheckall_button.Location = Point(275, 128)
      uncheckall_button.Size = Size(80, 23)
      uncheckall_button.Text = 'Select &None'
      
      # 4. --- build the update checklist (contains all the 'data' checkboxes)
      self.__update_checklist = CheckedListBox()
      self.__update_checklist.CheckOnClick = True
      self.__update_checklist.ColumnWidth = 120
      self.__update_checklist.ThreeDCheckBoxes = True
      self.__update_checklist.Location = Point(15, 45)
      self.__update_checklist.MultiColumn = True
      self.__update_checklist.SelectionMode = SelectionMode.One
      self.__update_checklist.Size = Size(250, 180)
      self.__update_checklist.ItemCheck += self.__update_gui_fired
      
      self.__update_checklist.Items.Add(ConfigForm.__SERIES_CB)
      self.__update_checklist.Items.Add(ConfigForm.__VOLUME_CB)
      self.__update_checklist.Items.Add(ConfigForm.__NUMBER_CB)
      self.__update_checklist.Items.Add(ConfigForm.__TITLE_CB)
      self.__update_checklist.Items.Add(ConfigForm.__MONTH_CB)
      self.__update_checklist.Items.Add(ConfigForm.__YEAR_CB)
      self.__update_checklist.Items.Add(ConfigForm.__ALT_SERIES_CB)
      self.__update_checklist.Items.Add(ConfigForm.__PUBLISHER_CB)
      self.__update_checklist.Items.Add(ConfigForm.__IMPRINT_CB)
      self.__update_checklist.Items.Add(ConfigForm.__WRITER_CB)
      self.__update_checklist.Items.Add(ConfigForm.__PENCILLER_CB)
      self.__update_checklist.Items.Add(ConfigForm.__INKER_CB)
      self.__update_checklist.Items.Add(ConfigForm.__COLORIST_CB)
      self.__update_checklist.Items.Add(ConfigForm.__LETTERER_CB)
      self.__update_checklist.Items.Add(ConfigForm.__COVER_ARTIST_CB)
      self.__update_checklist.Items.Add(ConfigForm.__EDITOR_CB)
      self.__update_checklist.Items.Add(ConfigForm.__SUMMARY_CB)
      self.__update_checklist.Items.Add(ConfigForm.__CHARACTERS_CB)
      self.__update_checklist.Items.Add(ConfigForm.__TEAMS_CB)
      self.__update_checklist.Items.Add(ConfigForm.__LOCATIONS_CB)     
      self.__update_checklist.Items.Add(ConfigForm.__WEBPAGE_CB)
      self.__update_checklist.Items.Add(ConfigForm.__RATING_CB)
   
      # 5. --- add 'em all to this tabpage
      tabpage.Controls.Add(label)
      tabpage.Controls.Add(checkall_button)
      tabpage.Controls.Add(uncheckall_button)
      tabpage.Controls.Add(self.__update_checklist)
      
      return tabpage

   
   
   # ==========================================================================
   def __build_behaviourtab(self):
      ''' builds and returns the "Behaviour" Tab for the TabControl '''
      
      tabpage = TabPage()
      tabpage.Text = "Behaviour"
      
      # 1. -- build the 'use fast rescrape' checkbox
      self.__fast_rescrape_cb = CheckBox()
      self.__fast_rescrape_cb.AutoSize = True
      self.__fast_rescrape_cb.FlatStyle = FlatStyle.System
      self.__fast_rescrape_cb.Location = Point(52, 15)
      self.__fast_rescrape_cb.Size = Size(218, 17)
      self.__fast_rescrape_cb.Text = \
         "Use previous choice when 'rescraping' comics"
      self.__fast_rescrape_cb.CheckedChanged += self.__update_gui_fired
      
      # 2. -- build the 'add rescrape hints to tags' checkbox
      self.__rescrape_tags_cb = CheckBox()
      self.__rescrape_tags_cb.AutoSize = True
      self.__rescrape_tags_cb.FlatStyle = FlatStyle.System
      self.__rescrape_tags_cb.Location = Point(82, 40)
      self.__rescrape_tags_cb.Size = Size(218, 17)
      self.__rescrape_tags_cb.Text = "Save that choice in 'Tags'"
      self.__rescrape_tags_cb.CheckedChanged += self.__update_gui_fired 
      
      # 3. -- build the 'add rescrape hints to notes' checkbox
      self.__rescrape_notes_cb = CheckBox()
      self.__rescrape_notes_cb.AutoSize = True
      self.__rescrape_notes_cb.FlatStyle = FlatStyle.System
      self.__rescrape_notes_cb.Location = Point(82, 65)
      self.__rescrape_notes_cb.Size = Size(218, 17)
      self.__rescrape_notes_cb.Text = "Save that choice in 'Notes'"
      self.__rescrape_notes_cb.CheckedChanged += self.__update_gui_fired
   
      # 4. --- build the 'scrape in groups'
      self.__scrape_in_groups_cb = CheckBox()
      self.__scrape_in_groups_cb.AutoSize = True
      self.__scrape_in_groups_cb.FlatStyle = FlatStyle.System
      self.__scrape_in_groups_cb.Location = Point(52, 95)
      self.__scrape_in_groups_cb.Size = Size(250, 17)
      self.__scrape_in_groups_cb.Text = \
         "When several comics appear to be from the same\n" \
         "series, only ask about the first one." 
      self.__scrape_in_groups_cb.CheckedChanged += self.__update_gui_fired
       
      # 5. --- build the 'specify series name' checkbox
      self.__specify_series_cb = CheckBox()
      self.__specify_series_cb.AutoSize = True
      self.__specify_series_cb.FlatStyle = FlatStyle.System
      self.__specify_series_cb.Location = Point(52, 140)
      self.__specify_series_cb.Size = Size(250, 17)
      self.__specify_series_cb.Text = \
         'Confirm each series name before searching for it'
      self.__specify_series_cb.CheckedChanged += self.__update_gui_fired
       
      
      # 6. --- build the 'display cover art' checkbox
      self.__show_covers_cb = CheckBox()
      self.__show_covers_cb.AutoSize = True
      self.__show_covers_cb.FlatStyle = FlatStyle.System
      self.__show_covers_cb.Location = Point(52, 173)
      self.__show_covers_cb.Size = Size(250, 17)
      self.__show_covers_cb.Text = \
         'When possible, display comic book cover images'
      self.__show_covers_cb.CheckedChanged += self.__update_gui_fired
      
      # 7. --- build the 'specify series name' checkbox
      self.__summary_dialog_cb = CheckBox()
      self.__summary_dialog_cb.AutoSize = True
      self.__summary_dialog_cb.FlatStyle = FlatStyle.System
      self.__summary_dialog_cb.Location = Point(52, 205)
      self.__summary_dialog_cb.Size = Size(250, 17)
      self.__summary_dialog_cb.Text = \
         'Show summary message when finished scraping'
      self.__summary_dialog_cb.CheckedChanged += self.__update_gui_fired 
            
      # 8. --- add 'em all to the tabpage 
      tabpage.Controls.Add(self.__scrape_in_groups_cb)
      tabpage.Controls.Add(self.__fast_rescrape_cb)
      tabpage.Controls.Add(self.__rescrape_tags_cb)
      tabpage.Controls.Add(self.__rescrape_notes_cb)
      tabpage.Controls.Add(self.__specify_series_cb)
      tabpage.Controls.Add(self.__summary_dialog_cb)
      tabpage.Controls.Add(self.__show_covers_cb)
      
      return tabpage
   
   
   
   # ==========================================================================
   def __build_datatab(self):
      ''' builds and returns the "Data" Tab for the TabControl '''
      
      tabpage = TabPage()
      tabpage.Text = "Data"
      
      
      # 1. --- build the 'convert imprints checkbox'
      self.__convert_imprints_cb = CheckBox()
      self.__convert_imprints_cb.AutoSize = True
      self.__convert_imprints_cb.FlatStyle = FlatStyle.System
      self.__convert_imprints_cb.Location = Point(52, 35)
      self.__convert_imprints_cb.Size = Size(250, 17)
      self.__convert_imprints_cb.Text = \
         'Convert scraped imprints to parent publisher'
      self.__convert_imprints_cb.CheckedChanged += self.__update_gui_fired
       
      # 2. -- build the 'overwrite existing' checkbox
      self.__ow_existing_cb = CheckBox()
      self.__ow_existing_cb.AutoSize = True
      self.__ow_existing_cb.FlatStyle = FlatStyle.System
      self.__ow_existing_cb.Location = Point(52, 85)
      self.__ow_existing_cb.Size = Size(218, 17)
      self.__ow_existing_cb.Text = \
         'Allow scraper to overwrite existing values in comics'
      self.__ow_existing_cb.CheckedChanged += self.__update_gui_fired 
   
      # 3. --- build the 'ignore blanks' checkbox
      self.__ignore_blanks_cb = CheckBox()                                          
      self.__ignore_blanks_cb.AutoSize = True                                       
      self.__ignore_blanks_cb.FlatStyle = FlatStyle.System                          
      self.__ignore_blanks_cb.Location = Point(82, 110)                             
      self.__ignore_blanks_cb.Size = Size(250, 17)                                  
      self.__ignore_blanks_cb.Text =\
         "...except when the new values would be empty"                            
      self.__ignore_blanks_cb.CheckedChanged += self.__update_gui_fired 
   
      # 4. --- build the 'download thumbnails' checkbox
      self.__download_thumbs_cb = CheckBox()
      self.__download_thumbs_cb.AutoSize = True
      self.__download_thumbs_cb.FlatStyle = FlatStyle.System
      self.__download_thumbs_cb.Location = Point(52, 160)
      self.__download_thumbs_cb.Size = Size(250, 17)
      self.__download_thumbs_cb.Text = \
         'Update thumbnails for fileless comics'
      self.__download_thumbs_cb.CheckedChanged += self.__update_gui_fired
      
      # 5. --- build the 'preserve thumbnails' checkbox
      self.__preserve_thumbs_cb = CheckBox()
      self.__preserve_thumbs_cb.AutoSize = True
      self.__preserve_thumbs_cb.FlatStyle = FlatStyle.System
      self.__preserve_thumbs_cb.Location = Point(82, 185)
      self.__preserve_thumbs_cb.Size = Size(250, 17)
      self.__preserve_thumbs_cb.Text = \
         '...&except when they already have thumbnails'
      self.__preserve_thumbs_cb.CheckedChanged += self.__update_gui_fired
            
      # 6. --- add 'em all to the tabpage 
      tabpage.Controls.Add(self.__ow_existing_cb)
      tabpage.Controls.Add(self.__ignore_blanks_cb)
      tabpage.Controls.Add(self.__convert_imprints_cb)
      tabpage.Controls.Add(self.__download_thumbs_cb)
      tabpage.Controls.Add(self.__preserve_thumbs_cb)
      
      return tabpage
  
         
   # ==========================================================================
   def show_form(self):
      '''
      Displays this form, blocking until the user closes it.  When it is closed,
      this method will return a Configuration object containing the settings 
      that this dialog was displaying when it was closed (these settings were
      also just saved on the filesystem, so they are also the settings that 
      this dialog will display the next time it is opened.)
      
      If the user clicks 'Cancel' then this method will simply return null. 
      '''
      
      log.debug("opened the settings dialog.")
      defaults = Configuration()
      defaults.load_defaults()
      self.__set_configuration(defaults) 
      dialogAnswer = self.ShowDialog() # blocks
      if dialogAnswer == DialogResult.OK:
         config = self.__get_configuration()
         config.save_defaults()
         log.debug("closed the settings dialog.")
      else:
         config = None
         log.debug("cancelled the settings dialog.")
      return config

      
   # ==========================================================================
   def __get_configuration(self):
      '''
      Returns a Configuration object the describes the current state of all the
      gui components on this ConfigForm.
      '''
      
      def is_checked( checkbox ):
         return self.__update_checklist.GetItemChecked( \
            self.__update_checklist.Items.IndexOf(checkbox) )
      
      config = Configuration()
      
      # 1. --- first get the parts from the checklist box (data tab)
      config.update_series_b = is_checked(ConfigForm.__SERIES_CB)
      config.update_number_b = is_checked(ConfigForm.__NUMBER_CB)
      config.update_month_b = is_checked(ConfigForm.__MONTH_CB)
      config.update_title_b = is_checked(ConfigForm.__TITLE_CB)
      config.update_alt_series_b = is_checked(ConfigForm.__ALT_SERIES_CB)
      config.update_writer_b = is_checked(ConfigForm.__WRITER_CB)
      config.update_penciller_b = is_checked(ConfigForm.__PENCILLER_CB)
      config.update_inker_b = is_checked(ConfigForm.__INKER_CB)
      config.update_cover_artist_b = is_checked(ConfigForm.__COVER_ARTIST_CB)
      config.update_colorist_b = is_checked(ConfigForm.__COLORIST_CB)
      config.update_letterer_b = is_checked(ConfigForm.__LETTERER_CB)
      config.update_editor_b = is_checked(ConfigForm.__EDITOR_CB)
      config.update_summary_b = is_checked(ConfigForm.__SUMMARY_CB)
      config.update_year_b = is_checked(ConfigForm.__YEAR_CB)
      config.update_imprint_b = is_checked(ConfigForm.__IMPRINT_CB)
      config.update_publisher_b = is_checked(ConfigForm.__PUBLISHER_CB)
      config.update_volume_b = is_checked(ConfigForm.__VOLUME_CB)
      config.update_characters_b = is_checked(ConfigForm.__CHARACTERS_CB)
      config.update_teams_b = is_checked(ConfigForm.__TEAMS_CB)
      config.update_locations_b = is_checked(ConfigForm.__LOCATIONS_CB)
      config.update_webpage_b = is_checked(ConfigForm.__WEBPAGE_CB)
      config.update_rating_b = is_checked(ConfigForm.__RATING_CB)

      
      # 2. --- then get the parts from the other checkboxes (options tab)
      config.ow_existing_b = self.__ow_existing_cb.Checked
      config.convert_imprints_b = self.__convert_imprints_cb.Checked
      config.specify_series_b = self.__specify_series_cb.Checked
      config.ignore_blanks_b = self.__ignore_blanks_cb.Checked
      config.show_covers_b = self.__show_covers_cb.Checked
      config.download_thumbs_b = self.__download_thumbs_cb.Checked
      config.preserve_thumbs_b = self.__preserve_thumbs_cb.Checked
      config.fast_rescrape_b = self.__fast_rescrape_cb.Checked
      config.scrape_in_groups_b = self.__scrape_in_groups_cb.Checked
      config.rescrape_notes_b = self.__rescrape_notes_cb.Checked
      config.rescrape_tags_b = self.__rescrape_tags_cb.Checked
      config.summary_dialog_b = self.__summary_dialog_cb.Checked
      return config
 
   
   # ==========================================================================
   def __set_configuration(self, config):
      '''
      Sets the state of all the gui components on this ConfigForm to match the 
      contents of the given Configuration object.
      '''
      
      def set_checked( checkbox, checked ):
         self.__update_checklist.SetItemChecked( \
            self.__update_checklist.Items.IndexOf(checkbox), checked )
      
      # 1. --- set get the parts in the checklist box (data tab)
      set_checked(ConfigForm.__SERIES_CB, config.update_series_b)
      set_checked(ConfigForm.__NUMBER_CB, config.update_number_b)
      set_checked(ConfigForm.__MONTH_CB, config.update_month_b)
      set_checked(ConfigForm.__TITLE_CB, config.update_title_b)
      set_checked(ConfigForm.__ALT_SERIES_CB, config.update_alt_series_b)
      set_checked(ConfigForm.__WRITER_CB, config.update_writer_b)
      set_checked(ConfigForm.__PENCILLER_CB, config.update_penciller_b)
      set_checked(ConfigForm.__INKER_CB, config.update_inker_b)
      set_checked(ConfigForm.__COVER_ARTIST_CB,config.update_cover_artist_b)
      set_checked(ConfigForm.__COLORIST_CB, config.update_colorist_b)
      set_checked(ConfigForm.__LETTERER_CB, config.update_letterer_b)
      set_checked(ConfigForm.__EDITOR_CB, config.update_editor_b)
      set_checked(ConfigForm.__SUMMARY_CB, config.update_summary_b)
      set_checked(ConfigForm.__YEAR_CB, config.update_year_b)
      set_checked(ConfigForm.__IMPRINT_CB, config.update_imprint_b)
      set_checked(ConfigForm.__PUBLISHER_CB, config.update_publisher_b)
      set_checked(ConfigForm.__VOLUME_CB, config.update_volume_b)
      set_checked(ConfigForm.__CHARACTERS_CB, config.update_characters_b)
      set_checked(ConfigForm.__TEAMS_CB, config.update_teams_b)
      set_checked(ConfigForm.__LOCATIONS_CB, config.update_locations_b)
      set_checked(ConfigForm.__WEBPAGE_CB, config.update_webpage_b)
      set_checked(ConfigForm.__RATING_CB, config.update_rating_b)
      
      # 2. --- then get the parts in the other checkboxes (options tab)
      self.__ow_existing_cb.Checked = config.ow_existing_b
      self.__convert_imprints_cb.Checked = config.convert_imprints_b
      self.__specify_series_cb.Checked = config.specify_series_b
      self.__ignore_blanks_cb.Checked = config.ignore_blanks_b
      self.__show_covers_cb.Checked = config.show_covers_b
      self.__download_thumbs_cb.Checked = config.download_thumbs_b
      self.__preserve_thumbs_cb.Checked = config.preserve_thumbs_b
      self.__fast_rescrape_cb.Checked = config.fast_rescrape_b
      self.__scrape_in_groups_cb.Checked = config.scrape_in_groups_b
      self.__rescrape_notes_cb.Checked = config.rescrape_notes_b
      self.__rescrape_tags_cb.Checked = config.rescrape_tags_b
      self.__summary_dialog_cb.Checked = config.summary_dialog_b
      
      self.__update_gui_fired()
      
      
   # ==========================================================================
   def __restore_defaults_fired(self, sender, args):
      ''' called when the user clicks the "restore defaults"  button '''
      
      self.__set_configuration(Configuration())
      log.debug("all settings were restored to their default values")
      self.__update_gui_fired()
      
      
   # ==========================================================================
   def __update_gui_fired(self, sender = None, args = None):
      ''' called anytime the gui for this form should be updated '''
      self.__ignore_blanks_cb.Enabled = self.__ow_existing_cb.Checked
      self.__preserve_thumbs_cb.Enabled = self.__download_thumbs_cb.Checked
       
              
   # ==========================================================================
   def __checkall_fired(self, sender, args):
      ''' called when the user clicks the "select all" button '''
      for i in range(self.__update_checklist.Items.Count):
         self.__update_checklist.SetItemChecked(i, True)
   
   
   # ==========================================================================
   def __uncheckall_fired(self, sender, args):
      ''' called when the user clicks the "select none" button '''
      for i in range(self.__update_checklist.Items.Count):
         self.__update_checklist.SetItemChecked(i, False)