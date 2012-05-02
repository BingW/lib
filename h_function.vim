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
hi Type			  gui=bold  guifg=lightsalmon
hi Error		  guifg=Red	guibg=Black
hi Todo			  guifg=Blue  guibg=Yellow
hi xComment       gui=bold guifg=green


syn keyword xTerm growth
syn keyword xUseless Putative
syn match xUseless "protein of unknown function"
syn keyword xLocal Mitochondrial cytoplasm
syn keyword xType ORF F C P G Hit_Bait null overexpression Bait_Hit transposable_element_gene gene_cassette
syn keyword xType unspecified tRNA long_terminal_repeat conditional repressible activation ARS 
syn keyword xType snoRNA centromere retrotransposon telomere ncRNA X_element_combinatorial_repeats 
syn keyword xType X_element_core_sequence telomeric_repeat pseudogene mating_locus rRNA snRNA misexpression
syn match xType 'reduction of function'
syn match xType 'gain of function'
syn match xType 'not physically mapped'
syn match xType 'not in systematic sequence of S288C'
syn match xType 'dominant negative' 
syn match xType 'Y\'_element'
syn match xType 'multigene locus'
syn match xUseage "required\ for"
syn match GeneName "\<[A-Z]\{1,}[0-9]\{1,}[A-Z0-9-]*\>"
syn match xComment "\#\S*\t"

:highlight link xUseage    Comment  
:highlight link GeneName   Statement 
:highlight link Attribute Identifier
:highlight link xTerm Comment
:highlight link xUseless Error 
:highlight link xLocal Comment
:highlight link xType Type
