" Vim syntax file
" Language: english 
" Maintainer: Bing 
" Last Change: 2012 Apr 11

:syntax on
:syntax case ignore

hi xMain          gui=bold guifg=beige guibg=maroon
hi emphasis       gui=bold guifg=yellow
hi Comment		  guifg=#80a0ff
hi Constant		  guifg=#ffa0a0
hi Special		  guifg=Orange
hi Identifier	  guifg=#40ffff
hi Statement	  gui=bold  guifg=#ffff60
hi PreProc		  guifg=#ff80ff
hi Type			  gui=bold  guifg=#60ff60
hi Error		  guifg=Red	guibg=Black
hi Todo			  guifg=Blue  guibg=Yellow

syn keyword Turn but nevertheless however although though whereas 
syn keyword Logical not and or nor either so hence whether both include[s] only also
syn keyword Be is are am were was be
syn keyword Need need[sed] require[sed] from 
syn keyword Attribute of at on in to which that
syn keyword Article a the 
syn match Example "for examples?"
syn match Example "one such"
syn match Example "in addition"
syn match Example "just\sas"
syn match Previous "recent works\?" 
syn match Previous "recent discovery"
syn match Previous "recent researchs\?"
syn match Previous "previous work"
syn match Enumerate "(.)"


:highlight link Turn            Statement 
:highlight link Be              Statement 
:highlight link Need            Statement 
:highlight link Logical         Statement 
:highlight link Example         Comment
:highlight link Previous        Comment
:highlight link Attribute       Identifier
:highlight link Article         Constant


":syntax keyword xMain hypothesis result do bg eg however
":syntax keyword xStatement if def class not and or for but true
":syntax keyword xKeywords init interesting possible 
":syntax keyword xKeywords at
":syntax keyword xKeywords pathway function family defect
":syntax keyword xKeywords in_vivo in_vitro
"
":highlight link xStatement Statement
":highlight link xKeywords Identifier
":highlight link xConstant Constant

