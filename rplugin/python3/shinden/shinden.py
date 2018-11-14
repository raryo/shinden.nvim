class Shinden(object):
    def __init__(self, nvim):
        self._nvim = nvim
        self._windows = {}

    #
    # call first in order to assign widows.
    #
    def assign_window_num(self, term, script):
        # TODO
        # assign window to term or script automatically
        #   assign term-window, script-window
        # currently, assigin using args.
        wins = self._nvim.windows
        self._windows['term'] = wins[term]
        self._windows['script'] = wins[script]


    #
    # main routin, put cmd to terminal and run.
    #
    def run_cmd(self, cmd):
        self._nvim.current.window = self._windows['term']
        self._nvim.feedkeys('i' + cmd + '\n')
        self._nvim.current.window = self._windows['script']
