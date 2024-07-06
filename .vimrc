" 基本設定
set nocompatible
set number
set relativenumber
set showcmd
set cursorline
set wildmenu
set lazyredraw
set ignorecase
set smartcase
set hidden
set splitright
set splitbelow
syntax on
filetype plugin indent on

" プラグインマネージャーの設定 (例: vim-plug)
call plug#begin('~/.vim/plugged')

" プラグインのリスト
Plug 'github/copilot.vim'
Plug 'Valloric/YouCompleteMe'

" 補完機能のプラグイン
Plug 'davidhalter/jedi-vim'
Plug 'pangloss/vim-javascript'
Plug 'othree/html5.vim'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'windwp/nvim-autopairs'
Plug 'norcalli/nvim-colorizer.lua'

call plug#end()

" GitHub Copilotの設定
let g:copilot_no_tab_map = v:true
imap <silent><script><expr> <C-J> copilot#Accept("\<CR>")

" coc.nvimの設定
let g:coc_global_extensions = ['coc-python', 'coc-tsserver', 'coc-html', 'coc-tailwindcss', 'coc-sh']

" YouCompleteMeの設定
let g:ycm_global_ycm_extra_conf = '~/.vim/.ycm_extra_conf.py'
let g:ycm_confirm_extra_conf = 0

" Python補完設定
let g:jedi#completions_enabled = 1
let g:jedi#auto_vim_configuration = 1

" TailwindCSS補完設定
autocmd FileType html,css setlocal omnifunc=coc#refresh

" ターミナルモードから元のバッファに戻る設定
tnoremap <Esc> <C-\><C-n>

" その他の便利な設定
set clipboard=unnamedplus
set mouse=a
set expandtab
set tabstop=4
set shiftwidth=4
set softtabstop=4

" カラースキームの設定
colorscheme desert

