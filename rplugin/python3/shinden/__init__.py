import sys
import neovim
from .shinden import Shinden


sys.dont_write_bytecode = True


@neovim.plugin
class shinden(object):
    _cmd_pre = 'Shinden'

    def __init__(self, nvim):
        self._nvim = nvim
        self._shinden = Shinden(self._nvim)

    @neovim.command(_cmd_pre+'Begin')
    def open_shinden(self):
        # script = int(args[0])
        # term = int(args[1])
        # self.nvim.command('vsp|terminal')
        self._shinden.init_env()

    @neovim.command(_cmd_pre+'Run', nargs='*')
    def run_current_cmd(self, args):
        cmd = self._nvim.current.line
        self._shinden.run_cmd(cmd)



