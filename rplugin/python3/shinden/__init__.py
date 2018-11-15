import sys
import neovim


sys.dont_write_bytecode = True


@neovim.plugin
class studio(object):
    _cmd_pre = 'Studio'

    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.command(_cmd_pre+'BeginProjcet')
    def open_studio(self):
        self.nvim.command('vsp|terminal')

    @neovim.function(_cmd_pre+'GetCurrentLine', sync=True)
    def get_current_line(self, args):
        list = self.nvim.command('ls')
        return list

    @neovim.command(_cmd_pre+'Run', nargs='*')
    def run_current_cmd(self, args):
        wins = self.nvim.windows
        cmd = self.nvim.current.line
        self.nvim.current.window = wins[0]
        self.nvim.feedkeys('i'+cmd+'\n')
        self.nvim.current.window = wins[1]

    @neovim.command(_cmd_pre+'Write')
    def write_out(self):
        self.nvim.current.line = 'sss'


