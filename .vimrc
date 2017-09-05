syntax enable
set background=dark
color MountainDew

execute pathogen#infect()
syntax on
filetype plugin indent on

set number
set mouse=a

set ruler

hi cursorcolumn term=bold
hi cursorrow cterm=bold

set noerrorbells visualbell t_vb=

nnoremap ; :

nnoremap <silent> <C-s> :w<CR>
