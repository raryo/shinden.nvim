import re


class Shinden(object):

    def __init__(self, nvim):
        self._nvim = nvim
        # self._windows = self._nvim.windows
        self._buffers = self._nvim.buffers
        self._env_buf_nums = {}
        self._env_wins = {}
        self._env_tab = None

    #
    # swapping buffers of winA and B, 
    # buf:a,win:0; buf:b,win:1;;;=>;;;buf:b,win:0; buf:a,win:1
    def _swap_buffer(self, win_a, win_b):
        buf_a = win_a.buffer
        win_a.buffer = win_b.buffer
        win_b.buffer = buf_a

    #
    # be called in init_env
    #
    def assign_window_num(self):
        # TODO
        # assign window to term or script automatically
        #   assign term-window, script-window
        # currently, assigin using args.

        env_wins = self._env_tab.windows
        for w in env_wins:
            buf = w.buffer
            type_ = 'term' if re.match('^term:.*', buf.name) else 'script'
            self._env_buf_nums[type_] = buf.number
            self._env_wins[type_] = w
        self._nvim.current.window = self._env_wins['script']
    
    #
    # call first in order to initialization
    #
    def init_env(self):
        # only when no term, one buffer
        #   ->create term window
        # otherwise
        #   ->create tab, term
        #   if buf=b, cp buf to new tab
        if len(self._buffers) == 1:
            if not re.match('^term:.*', self._buffers[1].name):
                # the Tab has only 1 buffer (not terminal)
                self._nvim.command('vsp|term')
            else:
                # the Tab has only 1 terminal-buffer
                # confirm use it
                self._nvim.command('vnew')
        else:
            # TODO 
            # copy current buffer when option is set
            self._nvim.command('tabnew|vsp|term')
        self._env_tab = self._nvim.current.tabpage
        self.assign_window_num()
       
    #
    # main routin, put cmd to terminal and run.
    #
    def run_cmd(self, cmd):
        if self._env_tab != self._nvim.current.tabpage:
            return 1
        # self._nvim.current.window = self._env_wins['term']
        # self._nvim.feedkeys('i' + cmd + '\nC-\-n')
        # self._nvim.current.window = self._env_wins['script']
        term_job_id = self._nvim.call('getbufvar',
                                      self._env_buf_nums['term'],
                                      'terminal_job_id')
        self._nvim.call('chansend', term_job_id, cmd + '\n')
