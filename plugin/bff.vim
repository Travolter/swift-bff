let s:plugin_path = escape(expand('<sfile>:p:h'), '\')

if !has('python')
  finish
endif

function! BFF()
  exe 'pyfile ' . escape(s:plugin_path, ' ') . '/bff_vim.py'
  python run()
endfunction
 
command! BFF call BFF()
