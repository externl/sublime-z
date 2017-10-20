# -*- coding: utf-8 -*-

import sublime
import sublime_plugin
import subprocess
from os import environ
import re

class Settings:
    def get(setting):
        return sublime.load_settings('Z.sublime-settings').get(setting)

class ZCommand:
    def __init__(self, directory_regex):
        self.directory_regex = directory_regex
        self.shell = Settings.get('shell') or environ.get('SHELL')
        self.command = [ self.shell, '-l', '-c' ]

    def run(self, flag):
        try:
            zcmd = [ environ.get('_Z_CMD') or 'z', flag, '"{}"'.format(self.directory_regex) ]
            output = subprocess.check_output(self.command + [' '.join(zcmd)], shell=False)
            return output.decode("utf-8")
        except subprocess.CalledProcessError as e:
            e.returncode
            if e.returncode == 1:
                return ''
            elif e.returncode == 127:
                raise Exception("z not found")
            raise
        except Exception as e:
            raise

    def execute(self):
        self.run('')

    def getBestMatch(self):
        match = self.run('--echo')
        return match.strip() if match else None

    def getList(self):
        matches = self.run('--list')
        return re.findall('^[0-9]+\.?[0-9]*\s+(.*)', matches, re.MULTILINE) if matches else None

class ZOpenDirectoryCommand(sublime_plugin.WindowCommand):
    def run(self, menu=None, action=None):
        self.window.show_input_panel("Z Open Directory RegEx", "", self.on_show_input_panel_done, None, None)

    def on_show_input_panel_done(self, directory_regex):
        z = ZCommand(directory_regex)

        if Settings.get('mode') == 'best_match':
            try:
                directory = z.getBestMatch()
                if directory:
                    self.open_directory(directory)
                else:
                    sublime.message_dialog('No match for {}'.format(directory_regex))
            except Exception as e:
                sublime.error_message(str(e))
        else:
            try:
                directory_list = z.getList()
                if directory_list:
                    self.show_directories(directory_list)
                else:
                    sublime.message_dialog('No matches for {}'.format(directory_regex))
            except Exception as e:
                sublime.error_message(str(e))

    def on_directory_selected(self, directory):
        if directory:
            self.open_directory(directory)

    def open_directory(self, directory):
        if self.window.project_data():
            sublime.run_command('new_window')
        sublime.active_window().set_project_data({'folders': [{'path': directory}]})

        # Since everything has been successful let's actually z jump to the directory
        # as if we were on the command line
        ZCommand(directory).execute()

    def show_directories(self, directory_list):
        selectedCallback = lambda index: self.on_directory_selected(directory_list[index] if index > -1 else None)
        self.window.show_quick_panel(directory_list, selectedCallback, 0, 0, None)
