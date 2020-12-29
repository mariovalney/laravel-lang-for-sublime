import os
import sublime
import sublime_plugin

class LaravelLangCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = self.view.sel()

        for region in selection:
            region_text = self.view.substr(region)
            self.view.replace(edit, region, self.format_text(region_text))

    def format_text(self, text):
        if not text:
            return text

        text = text.replace("'", "\\'")
        new_text = self.get_placeholder().format(text)
        return new_text

    def get_placeholder(self):
        filename = self.view.file_name()

        if filename[-3:] == '.js':
            return "__('{}')"

        if filename[-10:] == '.blade.php':
            return "{{{{ __('{}') }}}}"

        if filename[-4:] == '.php':
            return "__('{}')"

        return "{}"
