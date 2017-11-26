let s:plugin_path = escape(expand('<sfile>:p:h'), '\')

if !has('python')
  finish
endif

function! BFF() range
  exe 'pyfile ' . escape(s:plugin_path, ' ') . '/bff_vim.py'
  python format()
endfunction
 
command! -range BFF <line1>,<line2>call BFF()
