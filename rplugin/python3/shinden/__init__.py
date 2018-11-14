import neovim
from .shinden import Shinden


@neovim.plugin
class studio(object):
    _cmd_pre = 'Shinden'

    def __init__(self, nvim):
        self._nvim = nvim
        self._shinden = Shinden(self._nvim)

    @neovim.command(_cmd_pre+'Begin', nargs='*')
    def open_studio(self, args):
        term = int(args[0])
        script = int(args[1])
        # self.nvim.command('vsp|terminal')
        self._shinden.assign_window_num(term, script)

    @neovim.command(_cmd_pre+'Run', nargs='*')
    def run_current_cmd(self, args):
        cmd = self._nvim.current.line
        self._shinden.run_cmd(cmd)



