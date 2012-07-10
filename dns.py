import sublime, sublime_plugin


class HostLookupCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        from socket import gethostbyaddr
        from socket import gaierror

        sublime.status_message('getting hostnames....')
        for region in self.view.sel():
            try:
                if not region.empty():
                    text = self.view.substr(region)
                    result = gethostbyaddr(text)[0]
                    self.view.replace(edit, region, result)
            except Exception:
                continue


class NameLookupCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        from socket import gethostbyname
        from socket import gaierror

        sublime.status_message('getting ip\'s.....')
        for region in self.view.sel():
            try:
                if not region.empty():
                    text = self.view.substr(region)
                    result = gethostbyname(text)
                    self.view.replace(edit, region, result)
            except Exception: #gaierror:
                continue