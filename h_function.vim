" Vim syntax file
" Language: Bingnote
" Maintainer: Bing 
" Last Change: 2012 Apr 12

:syntax clear
:syntax case ignore

hi Comment		  guifg=#80a0ff
hi Constant		  guifg=#ffa0a0
hi Special		  guifg=Orange
hi Identifier	  guifg=#40ffff
hi Statement	  gui=bold  guifg=#ffff60
hi PreProc		  guifg=#ff80ff
hi Type			  gui=bold  guifg=#60ff60
hi Error		  guifg=Red	guibg=Black
hi Todo			  guifg=Blue  guibg=Yellow


syn keyword Attribute of at on in to
syn keyword xTerm protein function growth
syn keyword xUseless unknown
syn keyword xLocal Mitochondrial cytoplasm
syn match xUseage "required\ for"
syn match GeneName ".*\t"

:highlight link xUseage    
:highlight link GeneName   Statement 
:highlight link Attribute Identifier
:highlight link xTerm Type
:highlight link xUseless Error 
:highlight link xLocal Comment

