# Automated Originality Assessment of academic Paper: A Collaborative Approach Integrating Human Expertise and Large Language Models

## Overview

**Dataset and source code for paper "Automated Originality Assessment of academic Paper: A Collaborative Approach Integrating Human Expertise and Large Language Models".**

This study introduces a novel method for evaluating the originality and decision-making processes of academic articles by leveraging peer reviews and the methodology sections of scholarly papers. The primary contributions of this paper include:

- Proposing a new method for predicting the originality and decision-making of academic articles.
- Investigating a new method to combine human and artificial intelligence knowledge to enhance the performance of deep learning models.
- Designing a text-guided fusion module to integrate human and artificial intelligence knowledge effectively, facilitating optimal utilization of both sources of information.
- Conducting comprehensive experiments demonstrating the effectiveness of our methodology, which has yielded commendable results.

## Model overview

This study proposes a framework consisting of knowledge-guided fusion module and two paralleled sub-tasks.<br>

[Upload%!PS-Adobe-3.1 EPSF-3.0
%ADO_DSC_Encoding: Windows Roman
%%Title: Figure4.eps-25400.pdf
%%Creator: Adobe Acrobat 23.1.0
%%For: winchy
%%CreationDate: 2025/2/7, 11:19:20
%%BoundingBox: 0 0 757 570
%%HiResBoundingBox: 0 0 757 570
%%CropBox: 0 0 757 570
%%LanguageLevel: 2
%%DocumentNeededResources: (atend)
%%DocumentSuppliedResources: (atend)
%%DocumentNeededFeatures: (atend)
%%DocumentSuppliedFeatures: (atend)
%%DocumentData: Clean7Bit
%%Pages: (atend)
%%DocumentProcessColors:  Cyan Magenta Yellow Black
%%DocumentCustomColors: (atend)
%%EndComments
%%BeginDefaults
%%ViewingOrientation: 1 0 0 1
%%EndDefaults
%%BeginProlog
%%BeginResource: procset Adobe_AGM_Utils 1.0 0
%%Version: 1.0 0
%%Copyright: Copyright(C)2000-2006 Adobe Systems, Inc. All Rights Reserved.
systemdict/setpacking known
{currentpacking	true setpacking}if
userdict/Adobe_AGM_Utils 75 dict dup begin put
/bdf
{bind def}bind def
/nd{null def}bdf
/xdf
{exch def}bdf
/ldf 
{load def}bdf
/ddf
{put}bdf	
/xddf
{3 -1 roll put}bdf	
/xpt
{exch put}bdf
/ndf
{
	exch dup where{
		pop pop pop
	}{
		xdf
	}ifelse
}def
/cdndf
{
	exch dup currentdict exch known{
		pop pop
	}{
		exch def
	}ifelse
}def
/gx
{get exec}bdf
/ps_level
	/languagelevel where{
		pop systemdict/languagelevel gx
	}{
		1
	}ifelse
def
/level2 
	ps_level 2 ge
def
/level3 
	ps_level 3 ge
def
/ps_version
	{version cvr}stopped{-1}if
def
/set_gvm
{currentglobal exch setglobal}bdf
/reset_gvm
{setglobal}bdf
/makereadonlyarray
{
	/packedarray where{pop packedarray
	}{
		array astore readonly}ifelse
}bdf
/map_reserved_ink_name
{
	dup type/stringtype eq{
		dup/Red eq{
			pop(_Red_)
		}{
			dup/Green eq{
				pop(_Green_)
			}{
				dup/Blue eq{
					pop(_Blue_)
				}{
					dup()cvn eq{
						pop(Process)
					}if
				}ifelse
			}ifelse
		}ifelse
	}if
}bdf
/AGMUTIL_GSTATE 22 dict def
/get_gstate
{
	AGMUTIL_GSTATE begin
	/AGMUTIL_GSTATE_clr_spc currentcolorspace def
	/AGMUTIL_GSTATE_clr_indx 0 def
	/AGMUTIL_GSTATE_clr_comps 12 array def
	mark currentcolor counttomark
		{AGMUTIL_GSTATE_clr_comps AGMUTIL_GSTATE_clr_indx 3 -1 roll put
		/AGMUTIL_GSTATE_clr_indx AGMUTIL_GSTATE_clr_indx 1 add def}repeat pop
	/AGMUTIL_GSTATE_fnt rootfont def
	/AGMUTIL_GSTATE_lw currentlinewidth def
	/AGMUTIL_GSTATE_lc currentlinecap def
	/AGMUTIL_GSTATE_lj currentlinejoin def
	/AGMUTIL_GSTATE_ml currentmiterlimit def
	currentdash/AGMUTIL_GSTATE_do xdf/AGMUTIL_GSTATE_da xdf
	/AGMUTIL_GSTATE_sa currentstrokeadjust def
	/AGMUTIL_GSTATE_clr_rnd currentcolorrendering def
	/AGMUTIL_GSTATE_op currentoverprint def
	/AGMUTIL_GSTATE_bg currentblackgeneration cvlit def
	/AGMUTIL_GSTATE_ucr currentundercolorremoval cvlit def
	currentcolortransfer cvlit/AGMUTIL_GSTATE_gy_xfer xdf cvlit/AGMUTIL_GSTATE_b_xfer xdf
		cvlit/AGMUTIL_GSTATE_g_xfer xdf cvlit/AGMUTIL_GSTATE_r_xfer xdf
	/AGMUTIL_GSTATE_ht currenthalftone def
	/AGMUTIL_GSTATE_flt currentflat def
	end
}def
/set_gstate
{
	AGMUTIL_GSTATE begin
	AGMUTIL_GSTATE_clr_spc setcolorspace
	AGMUTIL_GSTATE_clr_indx{AGMUTIL_GSTATE_clr_comps AGMUTIL_GSTATE_clr_indx 1 sub get
	/AGMUTIL_GSTATE_clr_indx AGMUTIL_GSTATE_clr_indx 1 sub def}repeat setcolor
	AGMUTIL_GSTATE_fnt setfont
	AGMUTIL_GSTATE_lw setlinewidth
	AGMUTIL_GSTATE_lc setlinecap
	AGMUTIL_GSTATE_lj setlinejoin
	AGMUTIL_GSTATE_ml setmiterlimit
	AGMUTIL_GSTATE_da AGMUTIL_GSTATE_do setdash
	AGMUTIL_GSTATE_sa setstrokeadjust
	AGMUTIL_GSTATE_clr_rnd setcolorrendering
	AGMUTIL_GSTATE_op setoverprint
	AGMUTIL_GSTATE_bg cvx setblackgeneration
	AGMUTIL_GSTATE_ucr cvx setundercolorremoval
	AGMUTIL_GSTATE_r_xfer cvx AGMUTIL_GSTATE_g_xfer cvx AGMUTIL_GSTATE_b_xfer cvx
		AGMUTIL_GSTATE_gy_xfer cvx setcolortransfer
	AGMUTIL_GSTATE_ht/HalftoneType get dup 9 eq exch 100 eq or
		{
		currenthalftone/HalftoneType get AGMUTIL_GSTATE_ht/HalftoneType get ne
			{
			 mark AGMUTIL_GSTATE_ht{sethalftone}stopped cleartomark
			}if
		}{
		AGMUTIL_GSTATE_ht sethalftone
		}ifelse
	AGMUTIL_GSTATE_flt setflat
	end
}def
/get_gstate_and_matrix
{
	AGMUTIL_GSTATE begin
	/AGMUTIL_GSTATE_ctm matrix currentmatrix def
	end
	get_gstate
}def
/set_gstate_and_matrix
{
	set_gstate
	AGMUTIL_GSTATE begin
	AGMUTIL_GSTATE_ctm setmatrix
	end
}def
/AGMUTIL_str256 256 string def
/AGMUTIL_src256 256 string def
/AGMUTIL_dst64 64 string def
/AGMUTIL_srcLen nd
/AGMUTIL_ndx nd
/AGMUTIL_cpd nd
/capture_cpd{
	//Adobe_AGM_Utils/AGMUTIL_cpd currentpagedevice ddf
}def
/thold_halftone
{
	level3
		{sethalftone currenthalftone}
		{
			dup/HalftoneType get 3 eq
			{
				sethalftone currenthalftone
			}{
				begin
				Width Height mul{
					Thresholds read{pop}if
				}repeat
				end
				currenthalftone
			}ifelse
		}ifelse
}def 
/rdcmntline
{
	currentfile AGMUTIL_str256 readline pop
	(%)anchorsearch{pop}if
}bdf
/filter_cmyk
{	
	dup type/filetype ne{
		exch()/SubFileDecode filter
	}{
		exch pop
	}
	ifelse
	[
	exch
	{
		AGMUTIL_src256 readstring pop
		dup length/AGMUTIL_srcLen exch def
		/AGMUTIL_ndx 0 def
		AGMCORE_plate_ndx 4 AGMUTIL_srcLen 1 sub{
			1 index exch get
			AGMUTIL_dst64 AGMUTIL_ndx 3 -1 roll put
			/AGMUTIL_ndx AGMUTIL_ndx 1 add def
		}for
		pop
		AGMUTIL_dst64 0 AGMUTIL_ndx getinterval
	}
	bind
	/exec cvx
	]cvx
}bdf
/filter_indexed_devn
{
	cvi Names length mul names_index add Lookup exch get
}bdf
/filter_devn
{	
	4 dict begin
	/srcStr xdf
	/dstStr xdf
	dup type/filetype ne{
		0()/SubFileDecode filter
	}if
	[
	exch
		[
			/devicen_colorspace_dict/AGMCORE_gget cvx/begin cvx
			currentdict/srcStr get/readstring cvx/pop cvx
			/dup cvx/length cvx 0/gt cvx[
				Adobe_AGM_Utils/AGMUTIL_ndx 0/ddf cvx
				names_index Names length currentdict/srcStr get length 1 sub{
					1/index cvx/exch cvx/get cvx
					currentdict/dstStr get/AGMUTIL_ndx/load cvx 3 -1/roll cvx/put cvx
					Adobe_AGM_Utils/AGMUTIL_ndx/AGMUTIL_ndx/load cvx 1/add cvx/ddf cvx
				}for
				currentdict/dstStr get 0/AGMUTIL_ndx/load cvx/getinterval cvx
			]cvx/if cvx
			/end cvx
		]cvx
		bind
		/exec cvx
	]cvx
	end
}bdf
/AGMUTIL_imagefile nd
/read_image_file
{
	AGMUTIL_imagefile 0 setfileposition
	10 dict begin
	/imageDict xdf
	/imbufLen Width BitsPerComponent mul 7 add 8 idiv def
	/imbufIdx 0 def
	/origDataSource imageDict/DataSource get def
	/origMultipleDataSources imageDict/MultipleDataSources get def
	/origDecode imageDict/Decode get def
	/dstDataStr imageDict/Width get colorSpaceElemCnt mul string def
	imageDict/MultipleDataSources known{MultipleDataSources}{false}ifelse
	{
		/imbufCnt imageDict/DataSource get length def
		/imbufs imbufCnt array def
		0 1 imbufCnt 1 sub{
			/imbufIdx xdf
			imbufs imbufIdx imbufLen string put
			imageDict/DataSource get imbufIdx[AGMUTIL_imagefile imbufs imbufIdx get/readstring cvx/pop cvx]cvx put
		}for
		DeviceN_PS2{
			imageDict begin
		 	/DataSource[DataSource/devn_sep_datasource cvx]cvx def
			/MultipleDataSources false def
			/Decode[0 1]def
			end
		}if
	}{
		/imbuf imbufLen string def
		Indexed_DeviceN level3 not and DeviceN_NoneName or{
			/srcDataStrs[imageDict begin
				currentdict/MultipleDataSources known{MultipleDataSources{DataSource length}{1}ifelse}{1}ifelse
				{
					Width Decode length 2 div mul cvi string
				}repeat
				end]def		
			imageDict begin
		 	/DataSource[AGMUTIL_imagefile Decode BitsPerComponent false 1/filter_indexed_devn load dstDataStr srcDataStrs devn_alt_datasource/exec cvx]cvx def
			/Decode[0 1]def
			end
		}{
			imageDict/DataSource[1 string dup 0 AGMUTIL_imagefile Decode length 2 idiv string/readstring cvx/pop cvx names_index/get cvx/put cvx]cvx put
			imageDict/Decode[0 1]put
		}ifelse
	}ifelse
	imageDict exch
	load exec
	imageDict/DataSource origDataSource put
	imageDict/MultipleDataSources origMultipleDataSources put
	imageDict/Decode origDecode put	
	end
}bdf
/write_image_file
{
	begin
	{(AGMUTIL_imagefile)(w+)file}stopped{
		false
	}{
		Adobe_AGM_Utils/AGMUTIL_imagefile xddf 
		2 dict begin
		/imbufLen Width BitsPerComponent mul 7 add 8 idiv def
		MultipleDataSources{DataSource 0 get}{DataSource}ifelse type/filetype eq{
			/imbuf imbufLen string def
		}if
		1 1 Height MultipleDataSources not{Decode length 2 idiv mul}if{
			pop
			MultipleDataSources{
			 	0 1 DataSource length 1 sub{
					DataSource type dup
					/arraytype eq{
						pop DataSource exch gx
					}{
						/filetype eq{
							DataSource exch get imbuf readstring pop
						}{
							DataSource exch get
						}ifelse
					}ifelse
					AGMUTIL_imagefile exch writestring
				}for
			}{
				DataSource type dup
				/arraytype eq{
					pop DataSource exec
				}{
					/filetype eq{
						DataSource imbuf readstring pop
					}{
						DataSource
					}ifelse
				}ifelse
				AGMUTIL_imagefile exch writestring
			}ifelse
		}for
		end
		true
	}ifelse
	end
}bdf
/close_image_file
{
	AGMUTIL_imagefile closefile(AGMUTIL_imagefile)deletefile
}def
statusdict/product known userdict/AGMP_current_show known not and{
	/pstr statusdict/product get def
	pstr(HP LaserJet 2200)eq 	
	pstr(HP LaserJet 4000 Series)eq or
	pstr(HP LaserJet 4050 Series )eq or
	pstr(HP LaserJet 8000 Series)eq or
	pstr(HP LaserJet 8100 Series)eq or
	pstr(HP LaserJet 8150 Series)eq or
	pstr(HP LaserJet 5000 Series)eq or
	pstr(HP LaserJet 5100 Series)eq or
	pstr(HP Color LaserJet 4500)eq or
	pstr(HP Color LaserJet 4600)eq or
	pstr(HP LaserJet 5Si)eq or
	pstr(HP LaserJet 1200 Series)eq or
	pstr(HP LaserJet 1300 Series)eq or
	pstr(HP LaserJet 4100 Series)eq or 
	{
 		userdict/AGMP_current_show/show load put
		userdict/show{
		 currentcolorspace 0 get
		 /Pattern eq
		 {false charpath f}
		 {AGMP_current_show}ifelse
		}put
	}if
	currentdict/pstr undef
}if
/consumeimagedata
{
	begin
	AGMIMG_init_common
	currentdict/MultipleDataSources known not
		{/MultipleDataSources false def}if
	MultipleDataSources
		{
		DataSource 0 get type
		dup/filetype eq
			{
			1 dict begin
			/flushbuffer Width cvi string def
			1 1 Height cvi
				{
				pop
				0 1 DataSource length 1 sub
					{
					DataSource exch get
					flushbuffer readstring pop pop
					}for
				}for
			end
			}if
		dup/arraytype eq exch/packedarraytype eq or DataSource 0 get xcheck and
			{
			Width Height mul cvi
				{
				0 1 DataSource length 1 sub
					{dup DataSource exch gx length exch 0 ne{pop}if}for
				dup 0 eq
					{pop exit}if
				sub dup 0 le
					{exit}if
				}loop
			pop
			}if		
		}
		{
		/DataSource load type 
		dup/filetype eq
			{
			1 dict begin
			/flushbuffer Width Decode length 2 idiv mul cvi string def
			1 1 Height{pop DataSource flushbuffer readstring pop pop}for
			end
			}if
		dup/arraytype eq exch/packedarraytype eq or/DataSource load xcheck and
			{
				Height Width BitsPerComponent mul 8 BitsPerComponent sub add 8 idiv Decode length 2 idiv mul mul
					{
					DataSource length dup 0 eq
						{pop exit}if
					sub dup 0 le
						{exit}if
					}loop
				pop
			}if
		}ifelse
	end
}bdf
/addprocs
{
	 2{/exec load}repeat
	 3 1 roll
	 [5 1 roll]bind cvx
}def
/modify_halftone_xfer
{
	currenthalftone dup length dict copy begin
	 currentdict 2 index known{
	 	1 index load dup length dict copy begin
		currentdict/TransferFunction known{
			/TransferFunction load
		}{
			currenttransfer
		}ifelse
		 addprocs/TransferFunction xdf 
		 currentdict end def
		currentdict end sethalftone
	}{
		currentdict/TransferFunction known{
			/TransferFunction load 
		}{
			currenttransfer
		}ifelse
		addprocs/TransferFunction xdf
		currentdict end sethalftone		
		pop
	}ifelse
}def
/clonearray
{
	dup xcheck exch
	dup length array exch
	Adobe_AGM_Core/AGMCORE_tmp -1 ddf 
	{
	Adobe_AGM_Core/AGMCORE_tmp 2 copy get 1 add ddf 
	dup type/dicttype eq
		{
			Adobe_AGM_Core/AGMCORE_tmp get
			exch
			clonedict
			Adobe_AGM_Core/AGMCORE_tmp 4 -1 roll ddf 
		}if
	dup type/arraytype eq
		{
			Adobe_AGM_Core/AGMCORE_tmp get exch
			clonearray
			Adobe_AGM_Core/AGMCORE_tmp 4 -1 roll ddf 
		}if
	exch dup
	Adobe_AGM_Core/AGMCORE_tmp get 4 -1 roll put
	}forall
	exch{cvx}if
}bdf
/clonedict
{
	dup length dict
	begin
	{
		dup type/dicttype eq
			{clonedict}if
		dup type/arraytype eq
			{clonearray}if
		def
	}forall
	currentdict
	end
}bdf
/DeviceN_PS2
{
	/currentcolorspace AGMCORE_gget 0 get/DeviceN eq level3 not and
}bdf
/Indexed_DeviceN
{
	/indexed_colorspace_dict AGMCORE_gget dup null ne{
		dup/CSDBase known{
			/CSDBase get/CSD get_res/Names known 
		}{
			pop false
		}ifelse
	}{
		pop false
	}ifelse
}bdf
/DeviceN_NoneName
{	
	/Names where{
		pop
		false Names
		{
			(None)eq or
		}forall
	}{
		false
	}ifelse
}bdf
/DeviceN_PS2_inRip_seps
{
	/AGMCORE_in_rip_sep where
	{
		pop dup type dup/arraytype eq exch/packedarraytype eq or
		{
			dup 0 get/DeviceN eq level3 not and AGMCORE_in_rip_sep and
			{
				/currentcolorspace exch AGMCORE_gput
				false
			}{
				true
			}ifelse
		}{
			true
		}ifelse
	}{
		true
	}ifelse
}bdf
/base_colorspace_type
{
	dup type/arraytype eq{0 get}if
}bdf
/currentdistillerparams where{pop currentdistillerparams/CoreDistVersion get 5000 lt}{true}ifelse
{
	/pdfmark_5{cleartomark}bind def
}{
	/pdfmark_5{pdfmark}bind def
}ifelse
/ReadBypdfmark_5
{
	currentfile exch 0 exch/SubFileDecode filter
	/currentdistillerparams where 
	{pop currentdistillerparams/CoreDistVersion get 5000 lt}{true}ifelse
	{flushfile cleartomark}
	{/PUT pdfmark}ifelse 	
}bdf
/ReadBypdfmark_5_string
{
	2 dict begin
	/makerString exch def string/tmpString exch def
	{
		currentfile tmpString readline not{pop exit}if
		makerString anchorsearch
		{
			pop pop cleartomark exit
		}{
			3 copy/PUT pdfmark_5 pop 2 copy(\n)/PUT pdfmark_5
		}ifelse
	}loop
	end
}bdf
/xpdfm
{
	{
		dup 0 get/Label eq
		{
			aload length[exch 1 add 1 roll/PAGELABEL
		}{
			aload pop
			[{ThisPage}<<5 -2 roll>>/PUT
		}ifelse
		pdfmark_5
	}forall
}bdf
/lmt{
	dup 2 index le{exch}if pop dup 2 index ge{exch}if pop
}bdf
/int{
	dup 2 index sub 3 index 5 index sub div 6 -2 roll sub mul exch pop add exch pop
}bdf
/ds{
	Adobe_AGM_Utils begin
}bdf
/dt{
	currentdict Adobe_AGM_Utils eq{
		end
	}if
}bdf
systemdict/setpacking known
{setpacking}if
%%EndResource
%%BeginResource: procset Adobe_AGM_Core 2.0 0
%%Version: 2.0 0
%%Copyright: Copyright(C)1997-2007 Adobe Systems, Inc. All Rights Reserved.
systemdict/setpacking known
{
	currentpacking
	true setpacking
}if
userdict/Adobe_AGM_Core 209 dict dup begin put
/Adobe_AGM_Core_Id/Adobe_AGM_Core_2.0_0 def
/AGMCORE_str256 256 string def
/AGMCORE_save nd
/AGMCORE_graphicsave nd
/AGMCORE_c 0 def
/AGMCORE_m 0 def
/AGMCORE_y 0 def
/AGMCORE_k 0 def
/AGMCORE_cmykbuf 4 array def
/AGMCORE_screen[currentscreen]cvx def
/AGMCORE_tmp 0 def
/AGMCORE_&setgray nd
/AGMCORE_&setcolor nd
/AGMCORE_&setcolorspace nd
/AGMCORE_&setcmykcolor nd
/AGMCORE_cyan_plate nd
/AGMCORE_magenta_plate nd
/AGMCORE_yellow_plate nd
/AGMCORE_black_plate nd
/AGMCORE_plate_ndx nd
/AGMCORE_get_ink_data nd
/AGMCORE_is_cmyk_sep nd
/AGMCORE_host_sep nd
/AGMCORE_avoid_L2_sep_space nd
/AGMCORE_distilling nd
/AGMCORE_composite_job nd
/AGMCORE_producing_seps nd
/AGMCORE_ps_level -1 def
/AGMCORE_ps_version -1 def
/AGMCORE_environ_ok nd
/AGMCORE_CSD_cache 0 dict def
/AGMCORE_currentoverprint false def
/AGMCORE_deltaX nd
/AGMCORE_deltaY nd
/AGMCORE_name nd
/AGMCORE_sep_special nd
/AGMCORE_err_strings 4 dict def
/AGMCORE_cur_err nd
/AGMCORE_current_spot_alias false def
/AGMCORE_inverting false def
/AGMCORE_feature_dictCount nd
/AGMCORE_feature_opCount nd
/AGMCORE_feature_ctm nd
/AGMCORE_ConvertToProcess false def
/AGMCORE_Default_CTM matrix def
/AGMCORE_Default_PageSize nd
/AGMCORE_Default_flatness nd
/AGMCORE_currentbg nd
/AGMCORE_currentucr nd
/AGMCORE_pattern_paint_type 0 def
/knockout_unitsq nd
currentglobal true setglobal
[/CSA/Gradient/Procedure]
{
	/Generic/Category findresource dup length dict copy/Category defineresource pop
}forall
setglobal
/AGMCORE_key_known
{
	where{
		/Adobe_AGM_Core_Id known
	}{
		false
	}ifelse
}ndf
/flushinput
{
	save
	2 dict begin
	/CompareBuffer 3 -1 roll def
	/readbuffer 256 string def
	mark
	{
	currentfile readbuffer{readline}stopped
		{cleartomark mark}
		{
		not
			{pop exit}
		if
		CompareBuffer eq
			{exit}
		if
		}ifelse
	}loop
	cleartomark
	end
	restore
}bdf
/getspotfunction
{
	AGMCORE_screen exch pop exch pop
	dup type/dicttype eq{
		dup/HalftoneType get 1 eq{
			/SpotFunction get
		}{
			dup/HalftoneType get 2 eq{
				/GraySpotFunction get
			}{
				pop
				{
					abs exch abs 2 copy add 1 gt{
						1 sub dup mul exch 1 sub dup mul add 1 sub
					}{
						dup mul exch dup mul add 1 exch sub
					}ifelse
				}bind
			}ifelse
		}ifelse
	}if
}def
/np
{newpath}bdf
/clp_npth
{clip np}def
/eoclp_npth
{eoclip np}def
/npth_clp
{np clip}def
/graphic_setup
{
	/AGMCORE_graphicsave save store
	concat
	0 setgray
	0 setlinecap
	0 setlinejoin
	1 setlinewidth
	[]0 setdash
	10 setmiterlimit
	np
	false setoverprint
	false setstrokeadjust
	//Adobe_AGM_Core/spot_alias gx
	/Adobe_AGM_Image where{
		pop
		Adobe_AGM_Image/spot_alias 2 copy known{
			gx
		}{
			pop pop
		}ifelse
	}if
	/sep_colorspace_dict null AGMCORE_gput
	100 dict begin
	/dictstackcount countdictstack def
	/showpage{}def
	mark
}def
/graphic_cleanup
{
	cleartomark
	dictstackcount 1 countdictstack 1 sub{end}for
	end
	AGMCORE_graphicsave restore
}def
/compose_error_msg
{
	grestoreall initgraphics	
	/Helvetica findfont 10 scalefont setfont
	/AGMCORE_deltaY 100 def
	/AGMCORE_deltaX 310 def
	clippath pathbbox np pop pop 36 add exch 36 add exch moveto
	0 AGMCORE_deltaY rlineto AGMCORE_deltaX 0 rlineto
	0 AGMCORE_deltaY neg rlineto AGMCORE_deltaX neg 0 rlineto closepath
	0 AGMCORE_&setgray
	gsave 1 AGMCORE_&setgray fill grestore 
	1 setlinewidth gsave stroke grestore
	currentpoint AGMCORE_deltaY 15 sub add exch 8 add exch moveto
	/AGMCORE_deltaY 12 def
	/AGMCORE_tmp 0 def
	AGMCORE_err_strings exch get
		{
		dup 32 eq
			{
			pop
			AGMCORE_str256 0 AGMCORE_tmp getinterval
			stringwidth pop currentpoint pop add AGMCORE_deltaX 28 add gt
				{
				currentpoint AGMCORE_deltaY sub exch pop
				clippath pathbbox pop pop pop 44 add exch moveto
				}if
			AGMCORE_str256 0 AGMCORE_tmp getinterval show( )show
			0 1 AGMCORE_str256 length 1 sub
				{
				AGMCORE_str256 exch 0 put
				}for
			/AGMCORE_tmp 0 def
			}{
				AGMCORE_str256 exch AGMCORE_tmp xpt
				/AGMCORE_tmp AGMCORE_tmp 1 add def
			}ifelse
		}forall
}bdf
/AGMCORE_CMYKDeviceNColorspaces[
	[/Separation/None/DeviceCMYK{0 0 0}]
	[/Separation(Black)/DeviceCMYK{0 0 0 4 -1 roll}bind]
	[/Separation(Yellow)/DeviceCMYK{0 0 3 -1 roll 0}bind]
	[/DeviceN[(Yellow)(Black)]/DeviceCMYK{0 0 4 2 roll}bind]
	[/Separation(Magenta)/DeviceCMYK{0 exch 0 0}bind]
	[/DeviceN[(Magenta)(Black)]/DeviceCMYK{0 3 1 roll 0 exch}bind]
	[/DeviceN[(Magenta)(Yellow)]/DeviceCMYK{0 3 1 roll 0}bind]
	[/DeviceN[(Magenta)(Yellow)(Black)]/DeviceCMYK{0 4 1 roll}bind]
	[/Separation(Cyan)/DeviceCMYK{0 0 0}]
	[/DeviceN[(Cyan)(Black)]/DeviceCMYK{0 0 3 -1 roll}bind]
	[/DeviceN[(Cyan)(Yellow)]/DeviceCMYK{0 exch 0}bind]
	[/DeviceN[(Cyan)(Yellow)(Black)]/DeviceCMYK{0 3 1 roll}bind]
	[/DeviceN[(Cyan)(Magenta)]/DeviceCMYK{0 0}]
	[/DeviceN[(Cyan)(Magenta)(Black)]/DeviceCMYK{0 exch}bind]
	[/DeviceN[(Cyan)(Magenta)(Yellow)]/DeviceCMYK{0}]
	[/DeviceCMYK]
]def
/ds{
	Adobe_AGM_Core begin
	/currentdistillerparams where
		{
		pop currentdistillerparams/CoreDistVersion get 5000 lt
			{<</DetectBlends false>>setdistillerparams}if
		}if	
	/AGMCORE_ps_version xdf
	/AGMCORE_ps_level xdf
	errordict/AGM_handleerror known not{
		errordict/AGM_handleerror errordict/handleerror get put
		errordict/handleerror{
			Adobe_AGM_Core begin
			$error/newerror get AGMCORE_cur_err null ne and{
				$error/newerror false put
				AGMCORE_cur_err compose_error_msg
			}if
			$error/newerror true put
			end
			errordict/AGM_handleerror get exec
			}bind put
		}if
	/AGMCORE_environ_ok 
		ps_level AGMCORE_ps_level ge
		ps_version AGMCORE_ps_version ge and 
		AGMCORE_ps_level -1 eq or
	def
	AGMCORE_environ_ok not
		{/AGMCORE_cur_err/AGMCORE_bad_environ def}if
	/AGMCORE_&setgray systemdict/setgray get def
	level2{
		/AGMCORE_&setcolor systemdict/setcolor get def
		/AGMCORE_&setcolorspace systemdict/setcolorspace get def
	}if
	/AGMCORE_currentbg currentblackgeneration def
	/AGMCORE_currentucr currentundercolorremoval def
	/AGMCORE_Default_flatness currentflat def
	/AGMCORE_distilling
		/product where{
			pop systemdict/setdistillerparams known product(Adobe PostScript Parser)ne and
		}{
			false
		}ifelse
	def
	/AGMCORE_GSTATE AGMCORE_key_known not{
		/AGMCORE_GSTATE 21 dict def
		/AGMCORE_tmpmatrix matrix def
		/AGMCORE_gstack 64 array def
		/AGMCORE_gstackptr 0 def
		/AGMCORE_gstacksaveptr 0 def
		/AGMCORE_gstackframekeys 14 def
		/AGMCORE_&gsave/gsave ldf
		/AGMCORE_&grestore/grestore ldf
		/AGMCORE_&grestoreall/grestoreall ldf
		/AGMCORE_&save/save ldf
		/AGMCORE_&setoverprint/setoverprint ldf
		/AGMCORE_gdictcopy{
			begin
			{def}forall
			end
		}def
		/AGMCORE_gput{
			AGMCORE_gstack AGMCORE_gstackptr get
			3 1 roll
			put
		}def
		/AGMCORE_gget{
			AGMCORE_gstack AGMCORE_gstackptr get
			exch
			get
		}def
		/gsave{
			AGMCORE_&gsave
			AGMCORE_gstack AGMCORE_gstackptr get
			AGMCORE_gstackptr 1 add
			dup 64 ge{limitcheck}if
			/AGMCORE_gstackptr exch store
			AGMCORE_gstack AGMCORE_gstackptr get
			AGMCORE_gdictcopy
		}def
		/grestore{
			AGMCORE_&grestore
			AGMCORE_gstackptr 1 sub
			dup AGMCORE_gstacksaveptr lt{1 add}if
			dup AGMCORE_gstack exch get dup/AGMCORE_currentoverprint known
				{/AGMCORE_currentoverprint get setoverprint}{pop}ifelse
			/AGMCORE_gstackptr exch store
		}def
		/grestoreall{
			AGMCORE_&grestoreall
			/AGMCORE_gstackptr AGMCORE_gstacksaveptr store 
		}def
		/save{
			AGMCORE_&save
			AGMCORE_gstack AGMCORE_gstackptr get
			AGMCORE_gstackptr 1 add
			dup 64 ge{limitcheck}if
			/AGMCORE_gstackptr exch store
			/AGMCORE_gstacksaveptr AGMCORE_gstackptr store
			AGMCORE_gstack AGMCORE_gstackptr get
			AGMCORE_gdictcopy
		}def
		/setoverprint{
			dup/AGMCORE_currentoverprint exch AGMCORE_gput AGMCORE_&setoverprint
		}def	
		0 1 AGMCORE_gstack length 1 sub{
				AGMCORE_gstack exch AGMCORE_gstackframekeys dict put
		}for
	}if
	level3/AGMCORE_&sysshfill AGMCORE_key_known not and
	{
		/AGMCORE_&sysshfill systemdict/shfill get def
		/AGMCORE_&sysmakepattern systemdict/makepattern get def
		/AGMCORE_&usrmakepattern/makepattern load def
	}if
	/currentcmykcolor[0 0 0 0]AGMCORE_gput
	/currentstrokeadjust false AGMCORE_gput
	/currentcolorspace[/DeviceGray]AGMCORE_gput
	/sep_tint 0 AGMCORE_gput
	/devicen_tints[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]AGMCORE_gput
	/sep_colorspace_dict null AGMCORE_gput
	/devicen_colorspace_dict null AGMCORE_gput
	/indexed_colorspace_dict null AGMCORE_gput
	/currentcolor_intent()AGMCORE_gput
	/customcolor_tint 1 AGMCORE_gput
	/absolute_colorimetric_crd null AGMCORE_gput
	/relative_colorimetric_crd null AGMCORE_gput
	/saturation_crd null AGMCORE_gput
	/perceptual_crd null AGMCORE_gput
	currentcolortransfer cvlit/AGMCore_gray_xfer xdf cvlit/AGMCore_b_xfer xdf
		 cvlit/AGMCore_g_xfer xdf cvlit/AGMCore_r_xfer xdf
	<<
	/MaxPatternItem currentsystemparams/MaxPatternCache get
	>>
	setuserparams
	end
}def
/ps
{
	/setcmykcolor where{
		pop
		Adobe_AGM_Core/AGMCORE_&setcmykcolor/setcmykcolor load put
	}if
	Adobe_AGM_Core begin
	/setcmykcolor
	{
		4 copy AGMCORE_cmykbuf astore/currentcmykcolor exch AGMCORE_gput
		1 sub 4 1 roll
		3{
			3 index add neg dup 0 lt{
				pop 0
			}if
			3 1 roll
		}repeat
		setrgbcolor pop
	}ndf
	/currentcmykcolor
	{
		/currentcmykcolor AGMCORE_gget aload pop
	}ndf
	/setoverprint
	{pop}ndf
	/currentoverprint
	{false}ndf
	/AGMCORE_cyan_plate 1 0 0 0 test_cmyk_color_plate def
	/AGMCORE_magenta_plate 0 1 0 0 test_cmyk_color_plate def
	/AGMCORE_yellow_plate 0 0 1 0 test_cmyk_color_plate def
	/AGMCORE_black_plate 0 0 0 1 test_cmyk_color_plate def
	/AGMCORE_plate_ndx 
		AGMCORE_cyan_plate{
			0
		}{
			AGMCORE_magenta_plate{
				1
			}{
				AGMCORE_yellow_plate{
					2
				}{
					AGMCORE_black_plate{
						3
					}{
						4
					}ifelse
				}ifelse
			}ifelse
		}ifelse
		def
	/AGMCORE_have_reported_unsupported_color_space false def
	/AGMCORE_report_unsupported_color_space
	{
		AGMCORE_have_reported_unsupported_color_space false eq
		{
			(Warning: Job contains content that cannot be separated with on-host methods. This content appears on the black plate, and knocks out all other plates.)==
			Adobe_AGM_Core/AGMCORE_have_reported_unsupported_color_space true ddf
		}if
	}def
	/AGMCORE_composite_job
		AGMCORE_cyan_plate AGMCORE_magenta_plate and AGMCORE_yellow_plate and AGMCORE_black_plate and def
	/AGMCORE_in_rip_sep
		/AGMCORE_in_rip_sep where{
			pop AGMCORE_in_rip_sep
		}{
			AGMCORE_distilling 
			{
				false
			}{
				userdict/Adobe_AGM_OnHost_Seps known{
					false
				}{
					level2{
						currentpagedevice/Separations 2 copy known{
							get
						}{
							pop pop false
						}ifelse
					}{
						false
					}ifelse
				}ifelse
			}ifelse
		}ifelse
	def
	/AGMCORE_producing_seps AGMCORE_composite_job not AGMCORE_in_rip_sep or def
	/AGMCORE_host_sep AGMCORE_producing_seps AGMCORE_in_rip_sep not and def
	/AGM_preserve_spots 
		/AGM_preserve_spots where{
			pop AGM_preserve_spots
		}{
			AGMCORE_distilling AGMCORE_producing_seps or
		}ifelse
	def
	/AGM_is_distiller_preserving_spotimages
	{
		currentdistillerparams/PreserveOverprintSettings known
		{
			currentdistillerparams/PreserveOverprintSettings get
				{
					currentdistillerparams/ColorConversionStrategy known
					{
						currentdistillerparams/ColorConversionStrategy get
						/sRGB ne
					}{
						true
					}ifelse
				}{
					false
				}ifelse
		}{
			false
		}ifelse
	}def
	/convert_spot_to_process where{pop}{
		/convert_spot_to_process
		{
			//Adobe_AGM_Core begin
			dup map_alias{
				/Name get exch pop
			}if
			dup dup(None)eq exch(All)eq or
				{
				pop false
				}{
				AGMCORE_host_sep
				{
					gsave
					1 0 0 0 setcmykcolor currentgray 1 exch sub
					0 1 0 0 setcmykcolor currentgray 1 exch sub
					0 0 1 0 setcmykcolor currentgray 1 exch sub
					0 0 0 1 setcmykcolor currentgray 1 exch sub
					add add add 0 eq
					{
						pop false
					}{
						false setoverprint
						current_spot_alias false set_spot_alias
						1 1 1 1 6 -1 roll findcmykcustomcolor 1 setcustomcolor
						set_spot_alias
						currentgray 1 ne
					}ifelse
					grestore
				}{
					AGMCORE_distilling
					{
						pop AGM_is_distiller_preserving_spotimages not
					}{
						//Adobe_AGM_Core/AGMCORE_name xddf
						false
						//Adobe_AGM_Core/AGMCORE_pattern_paint_type get 0 eq
						AGMUTIL_cpd/OverrideSeparations known and
						{
							AGMUTIL_cpd/OverrideSeparations get
							{
								/HqnSpots/ProcSet resourcestatus
								{
									pop pop pop true
								}if
							}if
						}if					
						{
							AGMCORE_name/HqnSpots/ProcSet findresource/TestSpot gx not
						}{
							gsave
							[/Separation AGMCORE_name/DeviceGray{}]AGMCORE_&setcolorspace
							false
							AGMUTIL_cpd/SeparationColorNames 2 copy known
							{
								get
								{AGMCORE_name eq or}forall
								not
							}{
								pop pop pop true
							}ifelse
							grestore
						}ifelse
					}ifelse
				}ifelse
			}ifelse
			end
		}def
	}ifelse
	/convert_to_process where{pop}{
		/convert_to_process
		{
			dup length 0 eq
				{
				pop false
				}{
				AGMCORE_host_sep
				{
				dup true exch
					{
					dup(Cyan)eq exch
					dup(Magenta)eq 3 -1 roll or exch
					dup(Yellow)eq 3 -1 roll or exch
					dup(Black)eq 3 -1 roll or
						{pop}
						{convert_spot_to_process and}ifelse
					}
				forall
					{
					true exch
						{
						dup(Cyan)eq exch
						dup(Magenta)eq 3 -1 roll or exch
						dup(Yellow)eq 3 -1 roll or exch
						(Black)eq or and
						}forall
						not
					}{pop false}ifelse
				}{
				false exch
					{
					/PhotoshopDuotoneList where{pop false}{true}ifelse
						{
						dup(Cyan)eq exch
						dup(Magenta)eq 3 -1 roll or exch
						dup(Yellow)eq 3 -1 roll or exch
						dup(Black)eq 3 -1 roll or
						{pop}
						{convert_spot_to_process or}ifelse
						}
						{
						convert_spot_to_process or
						}
					ifelse
					}
				forall
				}ifelse
			}ifelse
		}def
	}ifelse	
	/AGMCORE_avoid_L2_sep_space 
		version cvr 2012 lt 
		level2 and 
		AGMCORE_producing_seps not and
	def
	/AGMCORE_is_cmyk_sep
		AGMCORE_cyan_plate AGMCORE_magenta_plate or AGMCORE_yellow_plate or AGMCORE_black_plate or
	def
	/AGM_avoid_0_cmyk where{
		pop AGM_avoid_0_cmyk
	}{
		AGM_preserve_spots 
		userdict/Adobe_AGM_OnHost_Seps known 
		userdict/Adobe_AGM_InRip_Seps known or
		not and
	}ifelse
	{
		/setcmykcolor[
			{
				4 copy add add add 0 eq currentoverprint and{
					pop 0.0005
				}if
			}/exec cvx
			/AGMCORE_&setcmykcolor load dup type/operatortype ne{
				/exec cvx
			}if
		]cvx def
	}if
	/AGMCORE_IsSeparationAProcessColor
		{
		dup(Cyan)eq exch dup(Magenta)eq exch dup(Yellow)eq exch(Black)eq or or or
		}def
	AGMCORE_host_sep{
		/setcolortransfer
		{
			AGMCORE_cyan_plate{
				pop pop pop
			}{
			 	AGMCORE_magenta_plate{
			 		4 3 roll pop pop pop
			 	}{
			 		AGMCORE_yellow_plate{
			 			4 2 roll pop pop pop
			 		}{
			 			4 1 roll pop pop pop
			 		}ifelse
			 	}ifelse
			}ifelse
			settransfer 
		}	
		def
		/AGMCORE_get_ink_data
			AGMCORE_cyan_plate{
				{pop pop pop}
			}{
			 	AGMCORE_magenta_plate{
			 		{4 3 roll pop pop pop}
			 	}{
			 		AGMCORE_yellow_plate{
			 			{4 2 roll pop pop pop}
			 		}{
			 			{4 1 roll pop pop pop}
			 		}ifelse
			 	}ifelse
			}ifelse
		def
		/AGMCORE_RemoveProcessColorNames
			{
			1 dict begin
			/filtername
				{
				dup/Cyan eq 1 index(Cyan)eq or
					{pop(_cyan_)}if
				dup/Magenta eq 1 index(Magenta)eq or
					{pop(_magenta_)}if
				dup/Yellow eq 1 index(Yellow)eq or
					{pop(_yellow_)}if
				dup/Black eq 1 index(Black)eq or
					{pop(_black_)}if
				}def
			dup type/arraytype eq
				{[exch{filtername}forall]}
				{filtername}ifelse
			end
			}def
		level3{
			/AGMCORE_IsCurrentColor
				{
				dup AGMCORE_IsSeparationAProcessColor
					{
					AGMCORE_plate_ndx 0 eq
						{dup(Cyan)eq exch/Cyan eq or}if
					AGMCORE_plate_ndx 1 eq
						{dup(Magenta)eq exch/Magenta eq or}if
					AGMCORE_plate_ndx 2 eq
						{dup(Yellow)eq exch/Yellow eq or}if
					AGMCORE_plate_ndx 3 eq
						{dup(Black)eq exch/Black eq or}if
					AGMCORE_plate_ndx 4 eq
						{pop false}if
					}{
					gsave
					false setoverprint
					current_spot_alias false set_spot_alias
					1 1 1 1 6 -1 roll findcmykcustomcolor 1 setcustomcolor
					set_spot_alias
					currentgray 1 ne
					grestore
					}ifelse
				}def
			/AGMCORE_filter_functiondatasource
				{	
				5 dict begin
				/data_in xdf
				data_in type/stringtype eq
					{
					/ncomp xdf
					/comp xdf
					/string_out data_in length ncomp idiv string def
					0 ncomp data_in length 1 sub
						{
						string_out exch dup ncomp idiv exch data_in exch ncomp getinterval comp get 255 exch sub put
						}for
					string_out
					}{
					string/string_in xdf
					/string_out 1 string def
					/component xdf
					[
					data_in string_in/readstring cvx
						[component/get cvx 255/exch cvx/sub cvx string_out/exch cvx 0/exch cvx/put cvx string_out]cvx
						[/pop cvx()]cvx/ifelse cvx
					]cvx/ReusableStreamDecode filter
				}ifelse
				end
				}def
			/AGMCORE_separateShadingFunction
				{
				2 dict begin
				/paint? xdf
				/channel xdf
				dup type/dicttype eq
					{
					begin
					FunctionType 0 eq
						{
						/DataSource channel Range length 2 idiv DataSource AGMCORE_filter_functiondatasource def
						currentdict/Decode known
							{/Decode Decode channel 2 mul 2 getinterval def}if
						paint? not
							{/Decode[1 1]def}if
						}if
					FunctionType 2 eq
						{
						paint?
							{
							/C0[C0 channel get 1 exch sub]def
							/C1[C1 channel get 1 exch sub]def
							}{
							/C0[1]def
							/C1[1]def
							}ifelse			
						}if
					FunctionType 3 eq
						{
						/Functions[Functions{channel paint? AGMCORE_separateShadingFunction}forall]def			
						}if
					currentdict/Range known
						{/Range[0 1]def}if
					currentdict
					end}{
					channel get 0 paint? AGMCORE_separateShadingFunction
					}ifelse
				end
				}def
			/AGMCORE_separateShading
				{
				3 -1 roll begin
				currentdict/Function known
					{
					currentdict/Background known
						{[1 index{Background 3 index get 1 exch sub}{1}ifelse]/Background xdf}if
					Function 3 1 roll AGMCORE_separateShadingFunction/Function xdf
					/ColorSpace[/DeviceGray]def
					}{
					ColorSpace dup type/arraytype eq{0 get}if/DeviceCMYK eq
						{
						/ColorSpace[/DeviceN[/_cyan_/_magenta_/_yellow_/_black_]/DeviceCMYK{}]def
						}{
						ColorSpace dup 1 get AGMCORE_RemoveProcessColorNames 1 exch put
						}ifelse
					ColorSpace 0 get/Separation eq
						{
							{
								[1/exch cvx/sub cvx]cvx
							}{
								[/pop cvx 1]cvx
							}ifelse
							ColorSpace 3 3 -1 roll put
							pop
						}{
							{
								[exch ColorSpace 1 get length 1 sub exch sub/index cvx 1/exch cvx/sub cvx ColorSpace 1 get length 1 add 1/roll cvx ColorSpace 1 get length{/pop cvx}repeat]cvx
							}{
								pop[ColorSpace 1 get length{/pop cvx}repeat cvx 1]cvx
							}ifelse
							ColorSpace 3 3 -1 roll bind put
						}ifelse
					ColorSpace 2/DeviceGray put																		
					}ifelse
				end
				}def
			/AGMCORE_separateShadingDict
				{
				dup/ColorSpace get
				dup type/arraytype ne
					{[exch]}if
				dup 0 get/DeviceCMYK eq
					{
					exch begin 
					currentdict
					AGMCORE_cyan_plate
						{0 true}if
					AGMCORE_magenta_plate
						{1 true}if
					AGMCORE_yellow_plate
						{2 true}if
					AGMCORE_black_plate
						{3 true}if
					AGMCORE_plate_ndx 4 eq
						{0 false}if		
					dup not currentoverprint and
						{/AGMCORE_ignoreshade true def}if
					AGMCORE_separateShading
					currentdict
					end exch
					}if
				dup 0 get/Separation eq
					{
					exch begin
					ColorSpace 1 get dup/None ne exch/All ne and
						{
						ColorSpace 1 get AGMCORE_IsCurrentColor AGMCORE_plate_ndx 4 lt and ColorSpace 1 get AGMCORE_IsSeparationAProcessColor not and
							{
							ColorSpace 2 get dup type/arraytype eq{0 get}if/DeviceCMYK eq 
								{
								/ColorSpace
									[
									/Separation
									ColorSpace 1 get
									/DeviceGray
										[
										ColorSpace 3 get/exec cvx
										4 AGMCORE_plate_ndx sub -1/roll cvx
										4 1/roll cvx
										3[/pop cvx]cvx/repeat cvx
										1/exch cvx/sub cvx
										]cvx									
									]def
								}{
								AGMCORE_report_unsupported_color_space
								AGMCORE_black_plate not
									{
									currentdict 0 false AGMCORE_separateShading
									}if
								}ifelse
							}{
							currentdict ColorSpace 1 get AGMCORE_IsCurrentColor
							0 exch 
							dup not currentoverprint and
								{/AGMCORE_ignoreshade true def}if
							AGMCORE_separateShading
							}ifelse	
						}if			
					currentdict
					end exch
					}if
				dup 0 get/DeviceN eq
					{
					exch begin
					ColorSpace 1 get convert_to_process
						{
						ColorSpace 2 get dup type/arraytype eq{0 get}if/DeviceCMYK eq 
							{
							/ColorSpace
								[
								/DeviceN
								ColorSpace 1 get
								/DeviceGray
									[
									ColorSpace 3 get/exec cvx
									4 AGMCORE_plate_ndx sub -1/roll cvx
									4 1/roll cvx
									3[/pop cvx]cvx/repeat cvx
									1/exch cvx/sub cvx
									]cvx									
								]def
							}{
							AGMCORE_report_unsupported_color_space
							AGMCORE_black_plate not
								{
								currentdict 0 false AGMCORE_separateShading
								/ColorSpace[/DeviceGray]def
								}if
							}ifelse
						}{
						currentdict
						false -1 ColorSpace 1 get
							{
							AGMCORE_IsCurrentColor
								{
								1 add
								exch pop true exch exit
								}if
							1 add
							}forall
						exch 
						dup not currentoverprint and
							{/AGMCORE_ignoreshade true def}if
						AGMCORE_separateShading
						}ifelse
					currentdict
					end exch
					}if
				dup 0 get dup/DeviceCMYK eq exch dup/Separation eq exch/DeviceN eq or or not
					{
					exch begin
					ColorSpace dup type/arraytype eq
						{0 get}if
					/DeviceGray ne
						{
						AGMCORE_report_unsupported_color_space
						AGMCORE_black_plate not
							{
							ColorSpace 0 get/CIEBasedA eq
								{
								/ColorSpace[/Separation/_ciebaseda_/DeviceGray{}]def
								}if
							ColorSpace 0 get dup/CIEBasedABC eq exch dup/CIEBasedDEF eq exch/DeviceRGB eq or or
								{
								/ColorSpace[/DeviceN[/_red_/_green_/_blue_]/DeviceRGB{}]def
								}if
							ColorSpace 0 get/CIEBasedDEFG eq
								{
								/ColorSpace[/DeviceN[/_cyan_/_magenta_/_yellow_/_black_]/DeviceCMYK{}]def
								}if
							currentdict 0 false AGMCORE_separateShading
							}if
						}if
					currentdict
					end exch
					}if
				pop
				dup/AGMCORE_ignoreshade known
					{
					begin
					/ColorSpace[/Separation(None)/DeviceGray{}]def
					currentdict end
					}if
				}def
			/shfill
				{
				AGMCORE_separateShadingDict 
				dup/AGMCORE_ignoreshade known
					{pop}
					{AGMCORE_&sysshfill}ifelse
				}def
			/makepattern
				{
				exch
				dup/PatternType get 2 eq
					{
					clonedict
					begin
					/Shading Shading AGMCORE_separateShadingDict def
					Shading/AGMCORE_ignoreshade known
					currentdict end exch
					{pop<</PatternType 1/PaintProc{pop}/BBox[0 0 1 1]/XStep 1/YStep 1/PaintType 1/TilingType 3>>}if
					exch AGMCORE_&sysmakepattern
					}{
					exch AGMCORE_&usrmakepattern
					}ifelse
				}def
		}if
	}if
	AGMCORE_in_rip_sep{
		/setcustomcolor
		{
			exch aload pop
			dup 7 1 roll inRip_spot_has_ink not	{
				4{4 index mul 4 1 roll}
				repeat
				/DeviceCMYK setcolorspace
				6 -2 roll pop pop
			}{
				//Adobe_AGM_Core begin
					/AGMCORE_k xdf/AGMCORE_y xdf/AGMCORE_m xdf/AGMCORE_c xdf
				end
				[/Separation 4 -1 roll/DeviceCMYK
				{dup AGMCORE_c mul exch dup AGMCORE_m mul exch dup AGMCORE_y mul exch AGMCORE_k mul}
				]
				setcolorspace
			}ifelse
			setcolor
		}ndf
		/setseparationgray
		{
			[/Separation(All)/DeviceGray{}]setcolorspace_opt
			1 exch sub setcolor
		}ndf
	}{
		/setseparationgray
		{
			AGMCORE_&setgray
		}ndf
	}ifelse
	/findcmykcustomcolor
	{
		5 makereadonlyarray
	}ndf
	/setcustomcolor
	{
		exch aload pop pop
		4{4 index mul 4 1 roll}repeat
		setcmykcolor pop
	}ndf
	/has_color
		/colorimage where{
			AGMCORE_producing_seps{
				pop true
			}{
				systemdict eq
			}ifelse
		}{
			false
		}ifelse
	def
	/map_index
	{
		1 index mul exch getinterval{255 div}forall
	}bdf
	/map_indexed_devn
	{
		Lookup Names length 3 -1 roll cvi map_index
	}bdf
	/n_color_components
	{
		base_colorspace_type
		dup/DeviceGray eq{
			pop 1
		}{
			/DeviceCMYK eq{
				4
			}{
				3
			}ifelse
		}ifelse
	}bdf
	level2{
		/mo/moveto ldf
		/li/lineto ldf
		/cv/curveto ldf
		/knockout_unitsq
		{
			1 setgray
			0 0 1 1 rectfill
		}def
		level2/setcolorspace AGMCORE_key_known not and{
			/AGMCORE_&&&setcolorspace/setcolorspace ldf
			/AGMCORE_ReplaceMappedColor
			{
				dup type dup/arraytype eq exch/packedarraytype eq or
				{
					/AGMCORE_SpotAliasAry2 where{
						begin
						dup 0 get dup/Separation eq
						{
							pop
							dup length array copy
							dup dup 1 get
							current_spot_alias
							{
								dup map_alias
								{
									false set_spot_alias
									dup 1 exch setsepcolorspace
									true set_spot_alias
									begin
									/sep_colorspace_dict currentdict AGMCORE_gput
									pop pop	pop
									[
										/Separation Name 
										CSA map_csa
										MappedCSA 
										/sep_colorspace_proc load
									]
									dup Name
									end
								}if
							}if
							map_reserved_ink_name 1 xpt
						}{
							/DeviceN eq 
							{
								dup length array copy
								dup dup 1 get[
									exch{
										current_spot_alias{
											dup map_alias{
												/Name get exch pop
											}if
										}if
										map_reserved_ink_name
									}forall 
								]1 xpt
							}if
						}ifelse
						end
					}if
				}if
			}def
			/setcolorspace
			{
				dup type dup/arraytype eq exch/packedarraytype eq or
				{
					dup 0 get/Indexed eq
					{
						AGMCORE_distilling
						{
							/PhotoshopDuotoneList where
							{
								pop false
							}{
								true
							}ifelse
						}{
							true
						}ifelse
						{
							aload pop 3 -1 roll
							AGMCORE_ReplaceMappedColor
							3 1 roll 4 array astore
						}if
					}{
						AGMCORE_ReplaceMappedColor
					}ifelse
				}if
				DeviceN_PS2_inRip_seps{AGMCORE_&&&setcolorspace}if
			}def
		}if	
	}{
		/adj
		{
			currentstrokeadjust{
				transform
				0.25 sub round 0.25 add exch
				0.25 sub round 0.25 add exch
				itransform
			}if
		}def
		/mo{
			adj moveto
		}def
		/li{
			adj lineto
		}def
		/cv{
			6 2 roll adj
			6 2 roll adj
			6 2 roll adj curveto
		}def
		/knockout_unitsq
		{
			1 setgray
			8 8 1[8 0 0 8 0 0]{<ffffffffffffffff>}image
		}def
		/currentstrokeadjust{
			/currentstrokeadjust AGMCORE_gget
		}def
		/setstrokeadjust{
			/currentstrokeadjust exch AGMCORE_gput
		}def
		/setcolorspace
		{
			/currentcolorspace exch AGMCORE_gput
		}def
		/currentcolorspace
		{
			/currentcolorspace AGMCORE_gget
		}def
		/setcolor_devicecolor
		{
			base_colorspace_type
			dup/DeviceGray eq{
				pop setgray
			}{
				/DeviceCMYK eq{
					setcmykcolor
				}{
					setrgbcolor
				}ifelse
			}ifelse
		}def
		/setcolor
		{
			currentcolorspace 0 get
			dup/DeviceGray ne{
				dup/DeviceCMYK ne{
					dup/DeviceRGB ne{
						dup/Separation eq{
							pop
							currentcolorspace 3 gx
							currentcolorspace 2 get
						}{
							dup/Indexed eq{
								pop
								currentcolorspace 3 get dup type/stringtype eq{
									currentcolorspace 1 get n_color_components
									3 -1 roll map_index
								}{
									exec
								}ifelse
								currentcolorspace 1 get
							}{
								/AGMCORE_cur_err/AGMCORE_invalid_color_space def
								AGMCORE_invalid_color_space
							}ifelse
						}ifelse
					}if
				}if
			}if
			setcolor_devicecolor
		}def
	}ifelse
	/sop/setoverprint ldf
	/lw/setlinewidth ldf
	/lc/setlinecap ldf
	/lj/setlinejoin ldf
	/ml/setmiterlimit ldf
	/dsh/setdash ldf
	/sadj/setstrokeadjust ldf
	/gry/setgray ldf
	/rgb/setrgbcolor ldf
	/cmyk[
		/currentcolorspace[/DeviceCMYK]/AGMCORE_gput cvx
		/setcmykcolor load dup type/operatortype ne{/exec cvx}if
	]cvx bdf
	level3 AGMCORE_host_sep not and{
		/nzopmsc{
			6 dict begin
			/kk exch def
			/yy exch def
			/mm exch def
			/cc exch def
			/sum 0 def
			cc 0 ne{/sum sum 2#1000 or def cc}if
			mm 0 ne{/sum sum 2#0100 or def mm}if
			yy 0 ne{/sum sum 2#0010 or def yy}if
			kk 0 ne{/sum sum 2#0001 or def kk}if
			AGMCORE_CMYKDeviceNColorspaces sum get setcolorspace
			sum 0 eq{0}if
			end
			setcolor
		}bdf
	}{
		/nzopmsc/cmyk ldf
	}ifelse
	/sep/setsepcolor ldf
	/devn/setdevicencolor ldf
	/idx/setindexedcolor ldf
	/colr/setcolor ldf
	/csacrd/set_csa_crd ldf
	/sepcs/setsepcolorspace ldf
	/devncs/setdevicencolorspace ldf
	/idxcs/setindexedcolorspace ldf
	/cp/closepath ldf
	/clp/clp_npth ldf
	/eclp/eoclp_npth ldf
	/f/fill ldf
	/ef/eofill ldf
	/@/stroke ldf
	/nclp/npth_clp ldf
	/gset/graphic_setup ldf
	/gcln/graphic_cleanup ldf
	/ct/concat ldf
	/cf/currentfile ldf
	/fl/filter ldf
	/rs/readstring ldf
	/AGMCORE_def_ht currenthalftone def
	/clonedict Adobe_AGM_Utils begin/clonedict load end def
	/clonearray Adobe_AGM_Utils begin/clonearray load end def
	currentdict{
		dup xcheck 1 index type dup/arraytype eq exch/packedarraytype eq or and{
			bind
		}if
		def
	}forall
	/getrampcolor
	{
		/indx exch def
		0 1 NumComp 1 sub
		{
			dup
			Samples exch get
			dup type/stringtype eq{indx get}if
			exch
			Scaling exch get aload pop
			3 1 roll
			mul add
		}for
		ColorSpaceFamily/Separation eq 
		{sep}
		{
			ColorSpaceFamily/DeviceN eq
			{devn}{setcolor}ifelse
		}ifelse
	}bdf
	/sssetbackground{
		aload pop 
		ColorSpaceFamily/Separation eq 
		{sep}
		{
			ColorSpaceFamily/DeviceN eq
			{devn}{setcolor}ifelse
		}ifelse	
	}bdf
	/RadialShade
	{
		40 dict begin
		/ColorSpaceFamily xdf
		/background xdf
		/ext1 xdf
		/ext0 xdf
		/BBox xdf
		/r2 xdf
		/c2y xdf
		/c2x xdf
		/r1 xdf
		/c1y xdf
		/c1x xdf
		/rampdict xdf
		/setinkoverprint where{pop/setinkoverprint{pop}def}if
		gsave
		BBox length 0 gt
		{
			np
			BBox 0 get BBox 1 get moveto
			BBox 2 get BBox 0 get sub 0 rlineto
			0 BBox 3 get BBox 1 get sub rlineto
			BBox 2 get BBox 0 get sub neg 0 rlineto
			closepath
			clip
			np
		}if
		c1x c2x eq
		{
			c1y c2y lt{/theta 90 def}{/theta 270 def}ifelse
		}{
			/slope c2y c1y sub c2x c1x sub div def
			/theta slope 1 atan def
			c2x c1x lt c2y c1y ge and{/theta theta 180 sub def}if
			c2x c1x lt c2y c1y lt and{/theta theta 180 add def}if
		}ifelse
		gsave
		clippath
		c1x c1y translate
		theta rotate
		-90 rotate
		{pathbbox}stopped
		{0 0 0 0}if
		/yMax xdf
		/xMax xdf
		/yMin xdf
		/xMin xdf
		grestore
		xMax xMin eq yMax yMin eq or
		{
			grestore
			end
		}{
			/max{2 copy gt{pop}{exch pop}ifelse}bdf
			/min{2 copy lt{pop}{exch pop}ifelse}bdf
			rampdict begin
			40 dict begin
			background length 0 gt{background sssetbackground gsave clippath fill grestore}if
			gsave
			c1x c1y translate
			theta rotate
			-90 rotate
			/c2y c1x c2x sub dup mul c1y c2y sub dup mul add sqrt def
			/c1y 0 def
			/c1x 0 def
			/c2x 0 def
			ext0
			{
				0 getrampcolor
				c2y r2 add r1 sub 0.0001 lt
				{
					c1x c1y r1 360 0 arcn
					pathbbox
					/aymax exch def
					/axmax exch def
					/aymin exch def
					/axmin exch def
					/bxMin xMin axmin min def
					/byMin yMin aymin min def
					/bxMax xMax axmax max def
					/byMax yMax aymax max def
					bxMin byMin moveto
					bxMax byMin lineto
					bxMax byMax lineto
					bxMin byMax lineto
					bxMin byMin lineto
					eofill
				}{
					c2y r1 add r2 le
					{
						c1x c1y r1 0 360 arc
						fill
					}
					{
						c2x c2y r2 0 360 arc fill
						r1 r2 eq
						{
							/p1x r1 neg def
							/p1y c1y def
							/p2x r1 def
							/p2y c1y def
							p1x p1y moveto p2x p2y lineto p2x yMin lineto p1x yMin lineto
							fill
						}{
							/AA r2 r1 sub c2y div def
							AA -1 eq
							{/theta 89.99 def}
							{/theta AA 1 AA dup mul sub sqrt div 1 atan def}
							ifelse
							/SS1 90 theta add dup sin exch cos div def
							/p1x r1 SS1 SS1 mul SS1 SS1 mul 1 add div sqrt mul neg def
							/p1y p1x SS1 div neg def
							/SS2 90 theta sub dup sin exch cos div def
							/p2x r1 SS2 SS2 mul SS2 SS2 mul 1 add div sqrt mul def
							/p2y p2x SS2 div neg def
							r1 r2 gt
							{
								/L1maxX p1x yMin p1y sub SS1 div add def
								/L2maxX p2x yMin p2y sub SS2 div add def
							}{
								/L1maxX 0 def
								/L2maxX 0 def
							}ifelse
							p1x p1y moveto p2x p2y lineto L2maxX L2maxX p2x sub SS2 mul p2y add lineto
							L1maxX L1maxX p1x sub SS1 mul p1y add lineto
							fill
						}ifelse
					}ifelse
				}ifelse
			}if
		c1x c2x sub dup mul
		c1y c2y sub dup mul
		add 0.5 exp
		0 dtransform
		dup mul exch dup mul add 0.5 exp 72 div
		0 72 matrix defaultmatrix dtransform dup mul exch dup mul add sqrt
		72 0 matrix defaultmatrix dtransform dup mul exch dup mul add sqrt
		1 index 1 index lt{exch}if pop
		/hires xdf
		hires mul
		/numpix xdf
		/numsteps NumSamples def
		/rampIndxInc 1 def
		/subsampling false def
		numpix 0 ne
		{
			NumSamples numpix div 0.5 gt
			{
				/numsteps numpix 2 div round cvi dup 1 le{pop 2}if def
				/rampIndxInc NumSamples 1 sub numsteps div def
				/subsampling true def
			}if
		}if
		/xInc c2x c1x sub numsteps div def
		/yInc c2y c1y sub numsteps div def
		/rInc r2 r1 sub numsteps div def
		/cx c1x def
		/cy c1y def
		/radius r1 def
		np
		xInc 0 eq yInc 0 eq rInc 0 eq and and
		{
			0 getrampcolor
			cx cy radius 0 360 arc
			stroke
			NumSamples 1 sub getrampcolor
			cx cy radius 72 hires div add 0 360 arc
			0 setlinewidth
			stroke
		}{
			0
			numsteps
			{
				dup
				subsampling{round cvi}if
				getrampcolor
				cx cy radius 0 360 arc
				/cx cx xInc add def
				/cy cy yInc add def
				/radius radius rInc add def
				cx cy radius 360 0 arcn
				eofill
				rampIndxInc add
			}repeat
			pop
		}ifelse
		ext1
		{
			c2y r2 add r1 lt
			{
				c2x c2y r2 0 360 arc
				fill
			}{
				c2y r1 add r2 sub 0.0001 le
				{
					c2x c2y r2 360 0 arcn
					pathbbox
					/aymax exch def
					/axmax exch def
					/aymin exch def
					/axmin exch def
					/bxMin xMin axmin min def
					/byMin yMin aymin min def
					/bxMax xMax axmax max def
					/byMax yMax aymax max def
					bxMin byMin moveto
					bxMax byMin lineto
					bxMax byMax lineto
					bxMin byMax lineto
					bxMin byMin lineto
					eofill
				}{
					c2x c2y r2 0 360 arc fill
					r1 r2 eq
					{
						/p1x r2 neg def
						/p1y c2y def
						/p2x r2 def
						/p2y c2y def
						p1x p1y moveto p2x p2y lineto p2x yMax lineto p1x yMax lineto
						fill
					}{
						/AA r2 r1 sub c2y div def
						AA -1 eq
						{/theta 89.99 def}
						{/theta AA 1 AA dup mul sub sqrt div 1 atan def}
						ifelse
						/SS1 90 theta add dup sin exch cos div def
						/p1x r2 SS1 SS1 mul SS1 SS1 mul 1 add div sqrt mul neg def
						/p1y c2y p1x SS1 div sub def
						/SS2 90 theta sub dup sin exch cos div def
						/p2x r2 SS2 SS2 mul SS2 SS2 mul 1 add div sqrt mul def
						/p2y c2y p2x SS2 div sub def
						r1 r2 lt
						{
							/L1maxX p1x yMax p1y sub SS1 div add def
							/L2maxX p2x yMax p2y sub SS2 div add def
						}{
							/L1maxX 0 def
							/L2maxX 0 def
						}ifelse
						p1x p1y moveto p2x p2y lineto L2maxX L2maxX p2x sub SS2 mul p2y add lineto
						L1maxX L1maxX p1x sub SS1 mul p1y add lineto
						fill
					}ifelse
				}ifelse
			}ifelse
		}if
		grestore
		grestore
		end
		end
		end
		}ifelse
	}bdf
	/GenStrips
	{
		40 dict begin
		/ColorSpaceFamily xdf
		/background xdf
		/ext1 xdf
		/ext0 xdf
		/BBox xdf
		/y2 xdf
		/x2 xdf
		/y1 xdf
		/x1 xdf
		/rampdict xdf
		/setinkoverprint where{pop/setinkoverprint{pop}def}if
		gsave
		BBox length 0 gt
		{
			np
			BBox 0 get BBox 1 get moveto
			BBox 2 get BBox 0 get sub 0 rlineto
			0 BBox 3 get BBox 1 get sub rlineto
			BBox 2 get BBox 0 get sub neg 0 rlineto
			closepath
			clip
			np
		}if
		x1 x2 eq
		{
			y1 y2 lt{/theta 90 def}{/theta 270 def}ifelse
		}{
			/slope y2 y1 sub x2 x1 sub div def
			/theta slope 1 atan def
			x2 x1 lt y2 y1 ge and{/theta theta 180 sub def}if
			x2 x1 lt y2 y1 lt and{/theta theta 180 add def}if
		}
		ifelse
		gsave
		clippath
		x1 y1 translate
		theta rotate
		{pathbbox}stopped
		{0 0 0 0}if
		/yMax exch def
		/xMax exch def
		/yMin exch def
		/xMin exch def
		grestore
		xMax xMin eq yMax yMin eq or
		{
			grestore
			end
		}{
			rampdict begin
			20 dict begin
			background length 0 gt{background sssetbackground gsave clippath fill grestore}if
			gsave
			x1 y1 translate
			theta rotate
			/xStart 0 def
			/xEnd x2 x1 sub dup mul y2 y1 sub dup mul add 0.5 exp def
			/ySpan yMax yMin sub def
			/numsteps NumSamples def
			/rampIndxInc 1 def
			/subsampling false def
			xStart 0 transform
			xEnd 0 transform
			3 -1 roll
			sub dup mul
			3 1 roll
			sub dup mul
			add 0.5 exp 72 div
			0 72 matrix defaultmatrix dtransform dup mul exch dup mul add sqrt
			72 0 matrix defaultmatrix dtransform dup mul exch dup mul add sqrt
			1 index 1 index lt{exch}if pop
			mul
			/numpix xdf
			numpix 0 ne
			{
				NumSamples numpix div 0.5 gt
				{
					/numsteps numpix 2 div round cvi dup 1 le{pop 2}if def
					/rampIndxInc NumSamples 1 sub numsteps div def
					/subsampling true def
				}if
			}if
			ext0
			{
				0 getrampcolor
				xMin xStart lt
				{
					xMin yMin xMin neg ySpan rectfill
				}if
			}if
			/xInc xEnd xStart sub numsteps div def
			/x xStart def
			0
			numsteps
			{
				dup
				subsampling{round cvi}if
				getrampcolor
				x yMin xInc ySpan rectfill
				/x x xInc add def
				rampIndxInc add
			}repeat
			pop
			ext1{
				xMax xEnd gt
				{
					xEnd yMin xMax xEnd sub ySpan rectfill
				}if
			}if
			grestore
			grestore
			end
			end
			end
		}ifelse
	}bdf
}def
/pt
{
	end
}def
/dt{
}def
/pgsv{
	//Adobe_AGM_Core/AGMCORE_save save put
}def
/pgrs{
	//Adobe_AGM_Core/AGMCORE_save get restore
}def
systemdict/findcolorrendering known{
	/findcolorrendering systemdict/findcolorrendering get def
}if
systemdict/setcolorrendering known{
	/setcolorrendering systemdict/setcolorrendering get def
}if
/test_cmyk_color_plate
{
	gsave
	setcmykcolor currentgray 1 ne
	grestore
}def
/inRip_spot_has_ink
{
	dup//Adobe_AGM_Core/AGMCORE_name xddf
	convert_spot_to_process not
}def
/map255_to_range
{
	1 index sub
	3 -1 roll 255 div mul add
}def
/set_csa_crd
{
	/sep_colorspace_dict null AGMCORE_gput
	begin
		CSA get_csa_by_name setcolorspace_opt
		set_crd
	end
}
def
/map_csa
{
	currentdict/MappedCSA known{MappedCSA null ne}{false}ifelse
	{pop}{get_csa_by_name/MappedCSA xdf}ifelse
}def
/setsepcolor
{
	/sep_colorspace_dict AGMCORE_gget begin
		dup/sep_tint exch AGMCORE_gput
		TintProc
	end
}def
/setdevicencolor
{
	/devicen_colorspace_dict AGMCORE_gget begin
		Names length copy
		Names length 1 sub -1 0
		{
			/devicen_tints AGMCORE_gget 3 1 roll xpt
		}for
		TintProc
	end
}def
/sep_colorspace_proc
{
	/AGMCORE_tmp exch store
	/sep_colorspace_dict AGMCORE_gget begin
	currentdict/Components known{
		Components aload pop 
		TintMethod/Lab eq{
			2{AGMCORE_tmp mul NComponents 1 roll}repeat
			LMax sub AGMCORE_tmp mul LMax add NComponents 1 roll
		}{
			TintMethod/Subtractive eq{
				NComponents{
					AGMCORE_tmp mul NComponents 1 roll
				}repeat
			}{
				NComponents{
					1 sub AGMCORE_tmp mul 1 add NComponents 1 roll
				}repeat
			}ifelse
		}ifelse
	}{
		ColorLookup AGMCORE_tmp ColorLookup length 1 sub mul round cvi get
		aload pop
	}ifelse
	end
}def
/sep_colorspace_gray_proc
{
	/AGMCORE_tmp exch store
	/sep_colorspace_dict AGMCORE_gget begin
	GrayLookup AGMCORE_tmp GrayLookup length 1 sub mul round cvi get
	end
}def
/sep_proc_name
{
	dup 0 get 
	dup/DeviceRGB eq exch/DeviceCMYK eq or level2 not and has_color not and{
		pop[/DeviceGray]
		/sep_colorspace_gray_proc
	}{
		/sep_colorspace_proc
	}ifelse
}def
/setsepcolorspace
{
	current_spot_alias{
		dup begin
			Name map_alias{
				exch pop
			}if
		end
	}if
	dup/sep_colorspace_dict exch AGMCORE_gput
	begin
	CSA map_csa
	/AGMCORE_sep_special Name dup()eq exch(All)eq or store
	AGMCORE_avoid_L2_sep_space{
		[/Indexed MappedCSA sep_proc_name 255 exch 
			{255 div}/exec cvx 3 -1 roll[4 1 roll load/exec cvx]cvx 
		]setcolorspace_opt
		/TintProc{
			255 mul round cvi setcolor
		}bdf
	}{
		MappedCSA 0 get/DeviceCMYK eq 
		currentdict/Components known and 
		AGMCORE_sep_special not and{
			/TintProc[
				Components aload pop Name findcmykcustomcolor 
				/exch cvx/setcustomcolor cvx
			]cvx bdf
		}{
 			AGMCORE_host_sep Name(All)eq and{
 				/TintProc{
					1 exch sub setseparationgray 
				}bdf
 			}{
				AGMCORE_in_rip_sep MappedCSA 0 get/DeviceCMYK eq and 
				AGMCORE_host_sep or
				Name()eq and{
					/TintProc[
						MappedCSA sep_proc_name exch 0 get/DeviceCMYK eq{
							cvx/setcmykcolor cvx
						}{
							cvx/setgray cvx
						}ifelse
					]cvx bdf
				}{
					AGMCORE_producing_seps MappedCSA 0 get dup/DeviceCMYK eq exch/DeviceGray eq or and AGMCORE_sep_special not and{
	 					/TintProc[
							/dup cvx
							MappedCSA sep_proc_name cvx exch
							0 get/DeviceGray eq{
								1/exch cvx/sub cvx 0 0 0 4 -1/roll cvx
							}if
							/Name cvx/findcmykcustomcolor cvx/exch cvx
							AGMCORE_host_sep{
								AGMCORE_is_cmyk_sep
								/Name cvx 
								/AGMCORE_IsSeparationAProcessColor load/exec cvx
								/not cvx/and cvx 
							}{
								Name inRip_spot_has_ink not
							}ifelse
							[
		 						/pop cvx 1
							]cvx/if cvx
							/setcustomcolor cvx
						]cvx bdf
 					}{
						/TintProc{setcolor}bdf
						[/Separation Name MappedCSA sep_proc_name load]setcolorspace_opt
					}ifelse
				}ifelse
			}ifelse
		}ifelse
	}ifelse
	set_crd
	setsepcolor
	end
}def
/additive_blend
{
 	3 dict begin
 	/numarrays xdf
 	/numcolors xdf
 	0 1 numcolors 1 sub
 		{
 		/c1 xdf
 		1
 		0 1 numarrays 1 sub
 			{
			1 exch add/index cvx
 			c1/get cvx/mul cvx
 			}for
 		numarrays 1 add 1/roll cvx 
 		}for
 	numarrays[/pop cvx]cvx/repeat cvx
 	end
}def
/subtractive_blend
{
	3 dict begin
	/numarrays xdf
	/numcolors xdf
	0 1 numcolors 1 sub
		{
		/c1 xdf
		1 1
		0 1 numarrays 1 sub
			{
			1 3 3 -1 roll add/index cvx 
			c1/get cvx/sub cvx/mul cvx
			}for
		/sub cvx
		numarrays 1 add 1/roll cvx
		}for
	numarrays[/pop cvx]cvx/repeat cvx
	end
}def
/exec_tint_transform
{
	/TintProc[
		/TintTransform cvx/setcolor cvx
	]cvx bdf
	MappedCSA setcolorspace_opt
}bdf
/devn_makecustomcolor
{
	2 dict begin
	/names_index xdf
	/Names xdf
	1 1 1 1 Names names_index get findcmykcustomcolor
	/devicen_tints AGMCORE_gget names_index get setcustomcolor
	Names length{pop}repeat
	end
}bdf
/setdevicencolorspace
{
	dup/AliasedColorants known{false}{true}ifelse 
	current_spot_alias and{
		7 dict begin
		/names_index 0 def
		dup/names_len exch/Names get length def
		/new_names names_len array def
		/new_LookupTables names_len array def
		/alias_cnt 0 def
		dup/Names get
		{
			dup map_alias{
				exch pop
				dup/ColorLookup known{
					dup begin
					new_LookupTables names_index ColorLookup put
					end
				}{
					dup/Components known{
						dup begin
						new_LookupTables names_index Components put
						end
					}{
						dup begin
						new_LookupTables names_index[null null null null]put
						end
					}ifelse
				}ifelse
				new_names names_index 3 -1 roll/Name get put
				/alias_cnt alias_cnt 1 add def 
			}{
				/name xdf				
				new_names names_index name put
				dup/LookupTables known{
					dup begin
					new_LookupTables names_index LookupTables names_index get put
					end
				}{
					dup begin
					new_LookupTables names_index[null null null null]put
					end
				}ifelse
			}ifelse
			/names_index names_index 1 add def 
		}forall
		alias_cnt 0 gt{
			/AliasedColorants true def
			/lut_entry_len new_LookupTables 0 get dup length 256 ge{0 get length}{length}ifelse def
			0 1 names_len 1 sub{
				/names_index xdf
				new_LookupTables names_index get dup length 256 ge{0 get length}{length}ifelse lut_entry_len ne{
					/AliasedColorants false def
					exit
				}{
					new_LookupTables names_index get 0 get null eq{
						dup/Names get names_index get/name xdf
						name(Cyan)eq name(Magenta)eq name(Yellow)eq name(Black)eq
						or or or not{
							/AliasedColorants false def
							exit
						}if
					}if
				}ifelse
			}for
			lut_entry_len 1 eq{
				/AliasedColorants false def
			}if
			AliasedColorants{
				dup begin
				/Names new_names def
				/LookupTables new_LookupTables def
				/AliasedColorants true def
				/NComponents lut_entry_len def
				/TintMethod NComponents 4 eq{/Subtractive}{/Additive}ifelse def
				/MappedCSA TintMethod/Additive eq{/DeviceRGB}{/DeviceCMYK}ifelse def
				currentdict/TTTablesIdx known not{
					/TTTablesIdx -1 def
				}if
				end
			}if
		}if
		end
	}if
	dup/devicen_colorspace_dict exch AGMCORE_gput
	begin
	currentdict/AliasedColorants known{
		AliasedColorants
	}{
		false
	}ifelse
	dup not{
		CSA map_csa
	}if
	/TintTransform load type/nulltype eq or{
		/TintTransform[
			0 1 Names length 1 sub
				{
				/TTTablesIdx TTTablesIdx 1 add def
				dup LookupTables exch get dup 0 get null eq
					{
					1 index
					Names exch get
					dup(Cyan)eq
						{
						pop exch
						LookupTables length exch sub
						/index cvx
						0 0 0
						}
						{
						dup(Magenta)eq
							{
							pop exch
							LookupTables length exch sub
							/index cvx
							0/exch cvx 0 0
							}{
							(Yellow)eq
								{
								exch
								LookupTables length exch sub
								/index cvx
								0 0 3 -1/roll cvx 0
								}{
								exch
								LookupTables length exch sub
								/index cvx
								0 0 0 4 -1/roll cvx
								}ifelse
							}ifelse
						}ifelse
					5 -1/roll cvx/astore cvx
					}{
					dup length 1 sub
					LookupTables length 4 -1 roll sub 1 add
					/index cvx/mul cvx/round cvx/cvi cvx/get cvx
					}ifelse
					Names length TTTablesIdx add 1 add 1/roll cvx
				}for
			Names length[/pop cvx]cvx/repeat cvx
			NComponents Names length
 			TintMethod/Subtractive eq
 				{
 				subtractive_blend
 				}{
 				additive_blend
 				}ifelse
		]cvx bdf
	}if
	AGMCORE_host_sep{
		Names convert_to_process{
			exec_tint_transform
		}
		{	
			currentdict/AliasedColorants known{
				AliasedColorants not
			}{
				false
			}ifelse
			5 dict begin
			/AvoidAliasedColorants xdf
			/painted? false def
			/names_index 0 def
			/names_len Names length def
			AvoidAliasedColorants{
				/currentspotalias current_spot_alias def
				false set_spot_alias
			}if
			Names{
				AGMCORE_is_cmyk_sep{
					dup(Cyan)eq AGMCORE_cyan_plate and exch
					dup(Magenta)eq AGMCORE_magenta_plate and exch
					dup(Yellow)eq AGMCORE_yellow_plate and exch
					(Black)eq AGMCORE_black_plate and or or or{
						/devicen_colorspace_dict AGMCORE_gget/TintProc[
							Names names_index/devn_makecustomcolor cvx
						]cvx ddf
						/painted? true def
					}if
					painted?{exit}if
				}{
					0 0 0 0 5 -1 roll findcmykcustomcolor 1 setcustomcolor currentgray 0 eq{
					/devicen_colorspace_dict AGMCORE_gget/TintProc[
						Names names_index/devn_makecustomcolor cvx
					]cvx ddf
					/painted? true def
					exit
					}if
				}ifelse
				/names_index names_index 1 add def
			}forall
			AvoidAliasedColorants{
				currentspotalias set_spot_alias
			}if
			painted?{
				/devicen_colorspace_dict AGMCORE_gget/names_index names_index put
			}{
				/devicen_colorspace_dict AGMCORE_gget/TintProc[
					names_len[/pop cvx]cvx/repeat cvx 1/setseparationgray cvx
 					0 0 0 0/setcmykcolor cvx
				]cvx ddf
			}ifelse
			end
		}ifelse
	}
	{
		AGMCORE_in_rip_sep{
			Names convert_to_process not
		}{
			level3
		}ifelse
		{
			[/DeviceN Names MappedCSA/TintTransform load]setcolorspace_opt
			/TintProc level3 not AGMCORE_in_rip_sep and{
				[
					Names/length cvx[/pop cvx]cvx/repeat cvx
				]cvx bdf
			}{
				{setcolor}bdf
			}ifelse
		}{
			exec_tint_transform
		}ifelse
	}ifelse
	set_crd
	/AliasedColorants false def
	end
}def
/setindexedcolorspace
{
	dup/indexed_colorspace_dict exch AGMCORE_gput
	begin
		currentdict/CSDBase known{
			CSDBase/CSD get_res begin
			currentdict/Names known{
				currentdict devncs
			}{
				1 currentdict sepcs
			}ifelse
			AGMCORE_host_sep{
				4 dict begin
				/compCnt/Names where{pop Names length}{1}ifelse def
				/NewLookup HiVal 1 add string def
				0 1 HiVal{
					/tableIndex xdf
					Lookup dup type/stringtype eq{
						compCnt tableIndex map_index
					}{
						exec
					}ifelse
					/Names where{
						pop setdevicencolor
					}{
						setsepcolor
					}ifelse
					currentgray
					tableIndex exch
					255 mul cvi 
					NewLookup 3 1 roll put
				}for
				[/Indexed currentcolorspace HiVal NewLookup]setcolorspace_opt
				end
			}{
				level3
				{
					currentdict/Names known{
						[/Indexed[/DeviceN Names MappedCSA/TintTransform load]HiVal Lookup]setcolorspace_opt
					}{
						[/Indexed[/Separation Name MappedCSA sep_proc_name load]HiVal Lookup]setcolorspace_opt
					}ifelse
				}{
				[/Indexed MappedCSA HiVal
					[
					currentdict/Names known{
						Lookup dup type/stringtype eq
							{/exch cvx CSDBase/CSD get_res/Names get length dup/mul cvx exch/getinterval cvx{255 div}/forall cvx}
							{/exec cvx}ifelse
							/TintTransform load/exec cvx
					}{
						Lookup dup type/stringtype eq
							{/exch cvx/get cvx 255/div cvx}
							{/exec cvx}ifelse
							CSDBase/CSD get_res/MappedCSA get sep_proc_name exch pop/load cvx/exec cvx
					}ifelse
					]cvx
				]setcolorspace_opt
				}ifelse
			}ifelse
			end
			set_crd
		}
		{
			CSA map_csa
			AGMCORE_host_sep level2 not and{
				0 0 0 0 setcmykcolor
			}{
				[/Indexed MappedCSA 
				level2 not has_color not and{
					dup 0 get dup/DeviceRGB eq exch/DeviceCMYK eq or{
						pop[/DeviceGray]
					}if
					HiVal GrayLookup
				}{
					HiVal 
					currentdict/RangeArray known{
						{
							/indexed_colorspace_dict AGMCORE_gget begin
							Lookup exch 
							dup HiVal gt{
								pop HiVal
							}if
							NComponents mul NComponents getinterval{}forall
							NComponents 1 sub -1 0{
								RangeArray exch 2 mul 2 getinterval aload pop map255_to_range
								NComponents 1 roll
							}for
							end
						}bind
					}{
						Lookup
					}ifelse
				}ifelse
				]setcolorspace_opt
				set_crd
			}ifelse
		}ifelse
	end
}def
/setindexedcolor
{
	AGMCORE_host_sep{
		/indexed_colorspace_dict AGMCORE_gget
		begin
		currentdict/CSDBase known{
			CSDBase/CSD get_res begin
			currentdict/Names known{
				map_indexed_devn
				devn
			}
			{
				Lookup 1 3 -1 roll map_index
				sep
			}ifelse
			end
		}{
			Lookup MappedCSA/DeviceCMYK eq{4}{1}ifelse 3 -1 roll
			map_index
			MappedCSA/DeviceCMYK eq{setcmykcolor}{setgray}ifelse
		}ifelse
		end
	}{
		level3 not AGMCORE_in_rip_sep and/indexed_colorspace_dict AGMCORE_gget/CSDBase known and{
			/indexed_colorspace_dict AGMCORE_gget/CSDBase get/CSD get_res begin
			map_indexed_devn
			devn
			end
		}
		{
			setcolor
		}ifelse
	}ifelse
}def
/ignoreimagedata
{
	currentoverprint not{
		gsave
		dup clonedict begin
		1 setgray
		/Decode[0 1]def
		/DataSource<FF>def
		/MultipleDataSources false def
		/BitsPerComponent 8 def
		currentdict end
		systemdict/image gx
		grestore
		}if
	consumeimagedata
}def
/add_res
{
	dup/CSD eq{
		pop 
		//Adobe_AGM_Core begin
		/AGMCORE_CSD_cache load 3 1 roll put
		end
	}{
		defineresource pop
	}ifelse
}def
/del_res
{
	{
		aload pop exch
		dup/CSD eq{
			pop 
			{//Adobe_AGM_Core/AGMCORE_CSD_cache get exch undef}forall
		}{
			exch
			{1 index undefineresource}forall
			pop
		}ifelse
	}forall
}def
/get_res
{
	dup/CSD eq{
		pop
		dup type dup/nametype eq exch/stringtype eq or{
			AGMCORE_CSD_cache exch get
		}if
	}{
		findresource
	}ifelse
}def
/get_csa_by_name
{
	dup type dup/nametype eq exch/stringtype eq or{
		/CSA get_res
	}if
}def
/paintproc_buf_init
{
	/count get 0 0 put
}def
/paintproc_buf_next
{
	dup/count get dup 0 get
	dup 3 1 roll
	1 add 0 xpt
	get				
}def
/cachepaintproc_compress
{
	5 dict begin
	currentfile exch 0 exch/SubFileDecode filter/ReadFilter exch def
	/ppdict 20 dict def
	/string_size 16000 def
	/readbuffer string_size string def
	currentglobal true setglobal 
	ppdict 1 array dup 0 1 put/count xpt
	setglobal
	/LZWFilter 
	{
		exch
		dup length 0 eq{
			pop
		}{
			ppdict dup length 1 sub 3 -1 roll put
		}ifelse
		{string_size}{0}ifelse string
	}/LZWEncode filter def
	{		
		ReadFilter readbuffer readstring
		exch LZWFilter exch writestring
		not{exit}if
	}loop
	LZWFilter closefile
	ppdict				
	end
}def
/cachepaintproc
{
	2 dict begin
	currentfile exch 0 exch/SubFileDecode filter/ReadFilter exch def
	/ppdict 20 dict def
	currentglobal true setglobal 
	ppdict 1 array dup 0 1 put/count xpt
	setglobal
	{
		ReadFilter 16000 string readstring exch
		ppdict dup length 1 sub 3 -1 roll put
		not{exit}if
	}loop
	ppdict dup dup length 1 sub()put					
	end	
}def
/make_pattern
{
	exch clonedict exch
	dup matrix currentmatrix matrix concatmatrix 0 0 3 2 roll itransform
	exch 3 index/XStep get 1 index exch 2 copy div cvi mul sub sub
	exch 3 index/YStep get 1 index exch 2 copy div cvi mul sub sub
	matrix translate exch matrix concatmatrix
			 1 index begin
		BBox 0 get XStep div cvi XStep mul/xshift exch neg def
		BBox 1 get YStep div cvi YStep mul/yshift exch neg def
		BBox 0 get xshift add
		BBox 1 get yshift add
		BBox 2 get xshift add
		BBox 3 get yshift add
		4 array astore
		/BBox exch def
		[xshift yshift/translate load null/exec load]dup
		3/PaintProc load put cvx/PaintProc exch def
		end
	gsave 0 setgray
	makepattern
	grestore
}def
/set_pattern
{
	dup/PatternType get 1 eq{
		dup/PaintType get 1 eq{
			currentoverprint sop[/DeviceGray]setcolorspace 0 setgray
		}if
	}if
	setpattern
}def
/setcolorspace_opt
{
	dup currentcolorspace eq{pop}{setcolorspace}ifelse
}def
/updatecolorrendering
{
	currentcolorrendering/RenderingIntent known{
		currentcolorrendering/RenderingIntent get
	}
	{
		Intent/AbsoluteColorimetric eq 
		{
			/absolute_colorimetric_crd AGMCORE_gget dup null eq
		}
		{
			Intent/RelativeColorimetric eq
			{
				/relative_colorimetric_crd AGMCORE_gget dup null eq
			}
			{
				Intent/Saturation eq
				{
					/saturation_crd AGMCORE_gget dup null eq
				}
				{
					/perceptual_crd AGMCORE_gget dup null eq
				}ifelse
			}ifelse
		}ifelse
		{
			pop null	
		}
		{
			/RenderingIntent known{null}{Intent}ifelse
		}ifelse
	}ifelse
	Intent ne{
		Intent/ColorRendering{findresource}stopped
		{
			pop pop systemdict/findcolorrendering known
			{
 				Intent findcolorrendering
 				{
 					/ColorRendering findresource true exch
 				}
 				{
 					/ColorRendering findresource
					product(Xerox Phaser 5400)ne
					exch
 				}ifelse
				dup Intent/AbsoluteColorimetric eq 
				{
					/absolute_colorimetric_crd exch AGMCORE_gput
				}
				{
					Intent/RelativeColorimetric eq
					{
						/relative_colorimetric_crd exch AGMCORE_gput
					}
					{
						Intent/Saturation eq
						{
							/saturation_crd exch AGMCORE_gput
						}
						{
							Intent/Perceptual eq
							{
								/perceptual_crd exch AGMCORE_gput
							}
							{
								pop
							}ifelse
						}ifelse
					}ifelse
				}ifelse
				1 index{exch}{pop}ifelse
			}
			{false}ifelse
		}
		{true}ifelse
		{
			dup begin
			currentdict/TransformPQR known{
				currentdict/TransformPQR get aload pop
				3{{}eq 3 1 roll}repeat or or
			}
			{true}ifelse
			currentdict/MatrixPQR known{
				currentdict/MatrixPQR get aload pop
				1.0 eq 9 1 roll 0.0 eq 9 1 roll 0.0 eq 9 1 roll
				0.0 eq 9 1 roll 1.0 eq 9 1 roll 0.0 eq 9 1 roll
				0.0 eq 9 1 roll 0.0 eq 9 1 roll 1.0 eq
				and and and and and and and and
			}
			{true}ifelse
			end
			or
			{
				clonedict begin
				/TransformPQR[
					{4 -1 roll 3 get dup 3 1 roll sub 5 -1 roll 3 get 3 -1 roll sub div
					3 -1 roll 3 get 3 -1 roll 3 get dup 4 1 roll sub mul add}bind
					{4 -1 roll 4 get dup 3 1 roll sub 5 -1 roll 4 get 3 -1 roll sub div
					3 -1 roll 4 get 3 -1 roll 4 get dup 4 1 roll sub mul add}bind
					{4 -1 roll 5 get dup 3 1 roll sub 5 -1 roll 5 get 3 -1 roll sub div
					3 -1 roll 5 get 3 -1 roll 5 get dup 4 1 roll sub mul add}bind
				]def
				/MatrixPQR[0.8951 -0.7502 0.0389 0.2664 1.7135 -0.0685 -0.1614 0.0367 1.0296]def
				/RangePQR[-0.3227950745 2.3229645538 -1.5003771057 3.5003465881 -0.1369979095 2.136967392]def
				currentdict end
			}if
			setcolorrendering_opt
		}if		
	}if
}def
/set_crd
{
	AGMCORE_host_sep not level2 and{
		currentdict/ColorRendering known{
			ColorRendering/ColorRendering{findresource}stopped not{setcolorrendering_opt}if
		}{
			currentdict/Intent known{
				updatecolorrendering
			}if
		}ifelse
		currentcolorspace dup type/arraytype eq
			{0 get}if
		/DeviceRGB eq
			{
			currentdict/UCR known
				{/UCR}{/AGMCORE_currentucr}ifelse
			load setundercolorremoval
			currentdict/BG known 
				{/BG}{/AGMCORE_currentbg}ifelse
			load setblackgeneration
			}if
	}if
}def
/set_ucrbg
{
	dup null eq {pop /AGMCORE_currentbg load}{/Procedure get_res}ifelse
	dup currentblackgeneration eq {pop}{setblackgeneration}ifelse
	dup null eq {pop /AGMCORE_currentucr load}{/Procedure get_res}ifelse
	dup currentundercolorremoval eq {pop}{setundercolorremoval}ifelse
}def
/setcolorrendering_opt
{
	dup currentcolorrendering eq{
		pop
	}{
		product(HP Color LaserJet 2605)anchorsearch{
			pop pop pop
		}{
			pop
			clonedict
			begin
				/Intent Intent def
				currentdict
			end
			setcolorrendering
		}ifelse
	}ifelse
}def
/cpaint_gcomp
{
	convert_to_process//Adobe_AGM_Core/AGMCORE_ConvertToProcess xddf
	//Adobe_AGM_Core/AGMCORE_ConvertToProcess get not
	{
		(%end_cpaint_gcomp)flushinput
	}if
}def
/cpaint_gsep
{
	//Adobe_AGM_Core/AGMCORE_ConvertToProcess get
	{	
		(%end_cpaint_gsep)flushinput
	}if
}def
/cpaint_gend
{np}def
/T1_path
{
	currentfile token pop currentfile token pop mo
	{
		currentfile token pop dup type/stringtype eq
			{pop exit}if 
		0 exch rlineto 
		currentfile token pop dup type/stringtype eq
			{pop exit}if 
		0 rlineto
	}loop
}def
/T1_gsave
	level3
	{/clipsave}
	{/gsave}ifelse
	load def
/T1_grestore
	level3
	{/cliprestore}
	{/grestore}ifelse 
	load def
/set_spot_alias_ary
{
	dup inherit_aliases
	//Adobe_AGM_Core/AGMCORE_SpotAliasAry xddf
}def
/set_spot_normalization_ary
{
	dup inherit_aliases
	dup length
	/AGMCORE_SpotAliasAry where{pop AGMCORE_SpotAliasAry length add}if
	array
	//Adobe_AGM_Core/AGMCORE_SpotAliasAry2 xddf
	/AGMCORE_SpotAliasAry where{
		pop
		AGMCORE_SpotAliasAry2 0 AGMCORE_SpotAliasAry putinterval
		AGMCORE_SpotAliasAry length
	}{0}ifelse
	AGMCORE_SpotAliasAry2 3 1 roll exch putinterval
	true set_spot_alias
}def
/inherit_aliases
{
	{dup/Name get map_alias{/CSD put}{pop}ifelse}forall
}def
/set_spot_alias
{
	/AGMCORE_SpotAliasAry2 where{
		/AGMCORE_current_spot_alias 3 -1 roll put
	}{
		pop
	}ifelse
}def
/current_spot_alias
{
	/AGMCORE_SpotAliasAry2 where{
		/AGMCORE_current_spot_alias get
	}{
		false
	}ifelse
}def
/map_alias
{
	/AGMCORE_SpotAliasAry2 where{
		begin
			/AGMCORE_name xdf
			false	
			AGMCORE_SpotAliasAry2{
				dup/Name get AGMCORE_name eq{
					/CSD get/CSD get_res
					exch pop true
					exit
				}{
					pop
				}ifelse
			}forall
		end
	}{
		pop false
	}ifelse
}bdf
/spot_alias
{
	true set_spot_alias
	/AGMCORE_&setcustomcolor AGMCORE_key_known not{
		//Adobe_AGM_Core/AGMCORE_&setcustomcolor/setcustomcolor load put
	}if
	/customcolor_tint 1 AGMCORE_gput
	//Adobe_AGM_Core begin
	/setcustomcolor
	{
		//Adobe_AGM_Core begin
		dup/customcolor_tint exch AGMCORE_gput
		1 index aload pop pop 1 eq exch 1 eq and exch 1 eq and exch 1 eq and not
		current_spot_alias and{1 index 4 get map_alias}{false}ifelse
		{
			false set_spot_alias
			/sep_colorspace_dict AGMCORE_gget null ne
			{/sep_colorspace_dict AGMCORE_gget/ForeignContent known not}{false}ifelse
			3 1 roll 2 index{
				exch pop/sep_tint AGMCORE_gget exch
			}if
			mark 3 1 roll
			setsepcolorspace
			counttomark 0 ne{
				setsepcolor
			}if
			pop
			not{/sep_tint 1.0 AGMCORE_gput/sep_colorspace_dict AGMCORE_gget/ForeignContent true put}if
			pop
			true set_spot_alias
		}{
			AGMCORE_&setcustomcolor
		}ifelse
		end
	}bdf
	end
}def
/begin_feature
{
	Adobe_AGM_Core/AGMCORE_feature_dictCount countdictstack put
	count Adobe_AGM_Core/AGMCORE_feature_opCount 3 -1 roll put
	{Adobe_AGM_Core/AGMCORE_feature_ctm matrix currentmatrix put}if
}def
/end_feature
{
	2 dict begin
	/spd/setpagedevice load def
	/setpagedevice{get_gstate spd set_gstate}def
	stopped{$error/newerror false put}if
	end
	count Adobe_AGM_Core/AGMCORE_feature_opCount get sub dup 0 gt{{pop}repeat}{pop}ifelse
	countdictstack Adobe_AGM_Core/AGMCORE_feature_dictCount get sub dup 0 gt{{end}repeat}{pop}ifelse
	{Adobe_AGM_Core/AGMCORE_feature_ctm get setmatrix}if
}def
/set_negative
{
	//Adobe_AGM_Core begin
	/AGMCORE_inverting exch def
	level2{
		currentpagedevice/NegativePrint known AGMCORE_distilling not and{
			currentpagedevice/NegativePrint get//Adobe_AGM_Core/AGMCORE_inverting get ne{
				true begin_feature true{
						<</NegativePrint//Adobe_AGM_Core/AGMCORE_inverting get>>setpagedevice
				}end_feature
			}if
			/AGMCORE_inverting false def
		}if
	}if
	AGMCORE_inverting{
		[{1 exch sub}/exec load dup currenttransfer exch]cvx bind settransfer
 		AGMCORE_distilling{
 			erasepage
 		}{
 			gsave np clippath 1/setseparationgray where{pop setseparationgray}{setgray}ifelse
 			/AGMIRS_&fill where{pop AGMIRS_&fill}{fill}ifelse grestore
 		}ifelse
	}if
	end
}def
/lw_save_restore_override{
	/md where{
		pop
		md begin
		initializepage
		/initializepage{}def
		/pmSVsetup{}def
		/endp{}def
		/pse{}def
		/psb{}def
		/orig_showpage where
			{pop}
			{/orig_showpage/showpage load def}
		ifelse
		/showpage{orig_showpage gR}def
		end
	}if
}def
/pscript_showpage_override{
	/NTPSOct95 where
	{
		begin
		showpage
		save
		/showpage/restore load def
		/restore{exch pop}def
		end
	}if
}def
/driver_media_override
{
	/md where{
		pop
		md/initializepage known{
			md/initializepage{}put
		}if
		md/rC known{
			md/rC{4{pop}repeat}put
		}if
	}if
	/mysetup where{
		/mysetup[1 0 0 1 0 0]put
	}if
	Adobe_AGM_Core/AGMCORE_Default_CTM matrix currentmatrix put
	level2
		{Adobe_AGM_Core/AGMCORE_Default_PageSize currentpagedevice/PageSize get put}if
}def
/capture_mysetup
{
	/Pscript_Win_Data where{
		pop
		Pscript_Win_Data/mysetup known{
			Adobe_AGM_Core/save_mysetup Pscript_Win_Data/mysetup get put
		}if
	}if
}def
/restore_mysetup
{
	/Pscript_Win_Data where{
		pop
		Pscript_Win_Data/mysetup known{
			Adobe_AGM_Core/save_mysetup known{
				Pscript_Win_Data/mysetup Adobe_AGM_Core/save_mysetup get put
				Adobe_AGM_Core/save_mysetup undef
			}if
		}if
	}if
}def
/driver_check_media_override
{
 	/PrepsDict where
 		{pop}
		{
		Adobe_AGM_Core/AGMCORE_Default_CTM get matrix currentmatrix ne
		Adobe_AGM_Core/AGMCORE_Default_PageSize get type/arraytype eq
			{
			Adobe_AGM_Core/AGMCORE_Default_PageSize get 0 get currentpagedevice/PageSize get 0 get eq and
			Adobe_AGM_Core/AGMCORE_Default_PageSize get 1 get currentpagedevice/PageSize get 1 get eq and
			}if
			{
			Adobe_AGM_Core/AGMCORE_Default_CTM get setmatrix
			}if
		}ifelse
}def
AGMCORE_err_strings begin
	/AGMCORE_bad_environ(Environment not satisfactory for this job. Ensure that the PPD is correct or that the PostScript level requested is supported by this printer. )def
	/AGMCORE_color_space_onhost_seps(This job contains colors that will not separate with on-host methods. )def
	/AGMCORE_invalid_color_space(This job contains an invalid color space. )def
end
/set_def_ht
{AGMCORE_def_ht sethalftone}def
/set_def_flat
{AGMCORE_Default_flatness setflat}def
end
systemdict/setpacking known
{setpacking}if
%%EndResource
%%BeginResource: procset Adobe_CoolType_Core 2.31 0
%%Copyright: Copyright 1997-2006 Adobe Systems Incorporated. All Rights Reserved.
%%Version: 2.31 0
10 dict begin
/Adobe_CoolType_Passthru currentdict def
/Adobe_CoolType_Core_Defined userdict/Adobe_CoolType_Core known def
Adobe_CoolType_Core_Defined
	{/Adobe_CoolType_Core userdict/Adobe_CoolType_Core get def}
if
userdict/Adobe_CoolType_Core 70 dict dup begin put
/Adobe_CoolType_Version 2.31 def
/Level2?
	systemdict/languagelevel known dup
		{pop systemdict/languagelevel get 2 ge}
	if def
Level2? not
	{
	/currentglobal false def
	/setglobal/pop load def
	/gcheck{pop false}bind def
	/currentpacking false def
	/setpacking/pop load def
	/SharedFontDirectory 0 dict def
	}
if
currentpacking
true setpacking
currentglobal false setglobal
userdict/Adobe_CoolType_Data 2 copy known not
	{2 copy 10 dict put}
if
get
	 begin
	/@opStackCountByLevel 32 dict def
	/@opStackLevel 0 def
	/@dictStackCountByLevel 32 dict def
	/@dictStackLevel 0 def
	 end
setglobal
currentglobal true setglobal
userdict/Adobe_CoolType_GVMFonts known not
	{userdict/Adobe_CoolType_GVMFonts 10 dict put}
if
setglobal
currentglobal false setglobal
userdict/Adobe_CoolType_LVMFonts known not
	{userdict/Adobe_CoolType_LVMFonts 10 dict put}
if
setglobal
/ct_VMDictPut
	{
	dup gcheck{Adobe_CoolType_GVMFonts}{Adobe_CoolType_LVMFonts}ifelse
	3 1 roll put
	}bind def
/ct_VMDictUndef
	{
	dup Adobe_CoolType_GVMFonts exch known
		{Adobe_CoolType_GVMFonts exch undef}
		{
			dup Adobe_CoolType_LVMFonts exch known
			{Adobe_CoolType_LVMFonts exch undef}
			{pop}
			ifelse
		}ifelse
	}bind def
/ct_str1 1 string def
/ct_xshow
{
	/_ct_na exch def
	/_ct_i 0 def
	currentpoint
	/_ct_y exch def
	/_ct_x exch def
	{
		pop pop
		ct_str1 exch 0 exch put
		ct_str1 show
		{_ct_na _ct_i get}stopped 
		{pop pop}
		{
			_ct_x _ct_y moveto
			0
			rmoveto
		}
		ifelse
		/_ct_i _ct_i 1 add def
		currentpoint
		/_ct_y exch def
		/_ct_x exch def
	}
	exch
	@cshow
}bind def
/ct_yshow
{
	/_ct_na exch def
	/_ct_i 0 def
	currentpoint
	/_ct_y exch def
	/_ct_x exch def
	{
		pop pop
		ct_str1 exch 0 exch put
		ct_str1 show
		{_ct_na _ct_i get}stopped 
		{pop pop}
		{
			_ct_x _ct_y moveto
			0 exch
			rmoveto
		}
		ifelse
		/_ct_i _ct_i 1 add def
		currentpoint
		/_ct_y exch def
		/_ct_x exch def
	}
	exch
	@cshow
}bind def
/ct_xyshow
{
	/_ct_na exch def
	/_ct_i 0 def
	currentpoint
	/_ct_y exch def
	/_ct_x exch def
	{
		pop pop
		ct_str1 exch 0 exch put
		ct_str1 show
		{_ct_na _ct_i get}stopped 
		{pop pop}
		{
			{_ct_na _ct_i 1 add get}stopped 
			{pop pop pop}
			{
				_ct_x _ct_y moveto
				rmoveto
			}
			ifelse
		}
		ifelse
		/_ct_i _ct_i 2 add def
		currentpoint
		/_ct_y exch def
		/_ct_x exch def
	}
	exch
	@cshow
}bind def
/xsh{{@xshow}stopped{Adobe_CoolType_Data begin ct_xshow end}if}bind def
/ysh{{@yshow}stopped{Adobe_CoolType_Data begin ct_yshow end}if}bind def
/xysh{{@xyshow}stopped{Adobe_CoolType_Data begin ct_xyshow end}if}bind def
currentglobal true setglobal
/ct_T3Defs
{
/BuildChar
{
	1 index/Encoding get exch get
	1 index/BuildGlyph get exec
}bind def
/BuildGlyph
{
	exch begin
	GlyphProcs exch get exec
	end
}bind def
}bind def
setglobal
/@_SaveStackLevels
	{
	Adobe_CoolType_Data
		begin
		/@vmState currentglobal def false setglobal
		@opStackCountByLevel
		@opStackLevel
		2 copy known not
			{
			2 copy
			3 dict dup/args
			7 index
			5 add array put
			put get
			}
			{
			get dup/args get dup length 3 index lt
				{
				dup length 5 add array exch
				1 index exch 0 exch putinterval
				1 index exch/args exch put
				}
				{pop}
			ifelse
			}
		ifelse
			begin
			count 1 sub
			1 index lt
				{pop count}
			if
			dup/argCount exch def
			dup 0 gt
				{
				args exch 0 exch getinterval 
			astore pop
				}
				{pop}
			ifelse
			count
			/restCount exch def
			end
		/@opStackLevel @opStackLevel 1 add def
		countdictstack 1 sub
		@dictStackCountByLevel exch @dictStackLevel exch put
		/@dictStackLevel @dictStackLevel 1 add def
		@vmState setglobal
		end
	}bind def
/@_RestoreStackLevels
	{
	Adobe_CoolType_Data
		begin
		/@opStackLevel @opStackLevel 1 sub def
		@opStackCountByLevel @opStackLevel get
			begin
			count restCount sub dup 0 gt
				{{pop}repeat}
				{pop}
			ifelse
			args 0 argCount getinterval{}forall
			end
		/@dictStackLevel @dictStackLevel 1 sub def
		@dictStackCountByLevel @dictStackLevel get
		end
	countdictstack exch sub dup 0 gt
		{{end}repeat}
		{pop}
	ifelse
	}bind def
/@_PopStackLevels
	{
	Adobe_CoolType_Data
		begin
		/@opStackLevel @opStackLevel 1 sub def
		/@dictStackLevel @dictStackLevel 1 sub def
		end
	}bind def
/@Raise
	{
	exch cvx exch errordict exch get exec
	stop
	}bind def
/@ReRaise
	{
	cvx $error/errorname get errordict exch get exec
	stop
	}bind def
/@Stopped
	{
	0 @#Stopped
	}bind def
/@#Stopped
	{
	@_SaveStackLevels
	stopped
		{@_RestoreStackLevels true}
		{@_PopStackLevels false}
	ifelse
	}bind def
/@Arg
	{
	Adobe_CoolType_Data
		begin
		@opStackCountByLevel @opStackLevel 1 sub get
		begin
		args exch
		argCount 1 sub exch sub get
		end
		end
	}bind def
currentglobal true setglobal
/CTHasResourceForAllBug
	Level2?
		{
		1 dict dup
				/@shouldNotDisappearDictValue true def
				Adobe_CoolType_Data exch/@shouldNotDisappearDict exch put
				begin
				count @_SaveStackLevels
					{(*){pop stop}128 string/Category resourceforall}
				stopped pop
				@_RestoreStackLevels
				currentdict Adobe_CoolType_Data/@shouldNotDisappearDict get dup 3 1 roll ne dup 3 1 roll
					{
						 /@shouldNotDisappearDictValue known
								{
										 {
												end
												currentdict 1 index eq
													{pop exit}
												if
										 }
									 loop
								}
						 if
					}
					{
						 pop
						 end
					}
				ifelse
		}
		{false}
	ifelse
	def
true setglobal
/CTHasResourceStatusBug
	Level2?
		{
		mark
			{/steveamerige/Category resourcestatus}
		stopped
			{cleartomark true}
			{cleartomark currentglobal not}
		ifelse
		}
		{false}
	ifelse
	def
setglobal
/CTResourceStatus
		{
		mark 3 1 roll
		/Category findresource
			begin
			({ResourceStatus}stopped)0()/SubFileDecode filter cvx exec
				{cleartomark false}
				{{3 2 roll pop true}{cleartomark false}ifelse}
			ifelse
			end
		}bind def
/CTWorkAroundBugs
	{
	Level2?
		{
		/cid_PreLoad/ProcSet resourcestatus
			{
			pop pop
			currentglobal
			mark
				{
				(*)
					{
					dup/CMap CTHasResourceStatusBug
						{CTResourceStatus}
						{resourcestatus}
					ifelse
						{
						pop dup 0 eq exch 1 eq or
							{
							dup/CMap findresource gcheck setglobal
							/CMap undefineresource
							}
							{
							pop CTHasResourceForAllBug
								{exit}
								{stop}
							ifelse
							}
						ifelse
						}
						{pop}
					ifelse
					}
				128 string/CMap resourceforall
				}
			stopped
				{cleartomark}
			stopped pop
			setglobal
			}
		if
		}
	if
	}bind def
/ds
	{
	Adobe_CoolType_Core
		begin
		CTWorkAroundBugs
		/mo/moveto load def
		/nf/newencodedfont load def
		/msf{makefont setfont}bind def
		/uf{dup undefinefont ct_VMDictUndef}bind def
		/ur/undefineresource load def
		/chp/charpath load def
		/awsh/awidthshow load def
		/wsh/widthshow load def
		/ash/ashow load def
		/@xshow/xshow load def
		/@yshow/yshow load def
		/@xyshow/xyshow load def
		/@cshow/cshow load def
		/sh/show load def
		/rp/repeat load def
		/.n/.notdef def
		end
		currentglobal false setglobal
	 userdict/Adobe_CoolType_Data 2 copy known not
		 {2 copy 10 dict put}
		if
		get
		begin
		/AddWidths? false def
		/CC 0 def
		/charcode 2 string def
		/@opStackCountByLevel 32 dict def
		/@opStackLevel 0 def
		/@dictStackCountByLevel 32 dict def
		/@dictStackLevel 0 def
		/InVMFontsByCMap 10 dict def
		/InVMDeepCopiedFonts 10 dict def
		end
		setglobal
	}bind def
/dt
	{
	currentdict Adobe_CoolType_Core eq
		{end}
	if
	}bind def
/ps
	{
	Adobe_CoolType_Core begin
	Adobe_CoolType_GVMFonts begin
	Adobe_CoolType_LVMFonts begin
	SharedFontDirectory begin
	}bind def
/pt
	{
	end
	end
	end
	end
	}bind def
/unload
	{
	systemdict/languagelevel known
		{
		systemdict/languagelevel get 2 ge
			{
			userdict/Adobe_CoolType_Core 2 copy known
				{undef}
				{pop pop}
			ifelse
			}
		if
		}
	if
	}bind def
/ndf
	{
	1 index where
		{pop pop pop}
		{dup xcheck{bind}if def}
	ifelse
	}def
/findfont systemdict
	begin
	userdict
		begin
		/globaldict where{/globaldict get begin}if
			dup where pop exch get
		/globaldict where{pop end}if
		end
	end
Adobe_CoolType_Core_Defined
	{/systemfindfont exch def}
	{
	/findfont 1 index def
	/systemfindfont exch def
	}
ifelse
/undefinefont
	{pop}ndf
/copyfont
	{
	currentglobal 3 1 roll
	1 index gcheck setglobal
	dup null eq{0}{dup length}ifelse
	2 index length add 1 add dict
		begin
		exch
			{
			1 index/FID eq
				{pop pop}
				{def}
			ifelse
			}
		forall
		dup null eq
			{pop}
			{{def}forall}
		ifelse
		currentdict
		end
	exch setglobal
	}bind def
/copyarray
	{
	currentglobal exch
	dup gcheck setglobal
	dup length array copy
	exch setglobal
	}bind def
/newencodedfont
	{
	currentglobal
		{
		SharedFontDirectory 3 index known
			{SharedFontDirectory 3 index get/FontReferenced known}
			{false}
		ifelse
		}
		{
		FontDirectory 3 index known
			{FontDirectory 3 index get/FontReferenced known}
			{
			SharedFontDirectory 3 index known
				{SharedFontDirectory 3 index get/FontReferenced known}
				{false}
			ifelse
			}
		ifelse
		}
	ifelse
	dup
		{
		3 index findfont/FontReferenced get
		2 index dup type/nametype eq
			{findfont}
		if ne
			{pop false}
		if
		}
	if
	dup
		{
		1 index dup type/nametype eq
			{findfont}
		 if
		dup/CharStrings known
			{
			/CharStrings get length
			4 index findfont/CharStrings get length
			ne
				{
				pop false
				}
			if 
			}
			{pop}
			ifelse
		}
	if
		{
		pop
		1 index findfont
		/Encoding get exch
		0 1 255
			{2 copy get 3 index 3 1 roll put}
		for
		pop pop pop
		}
		{
		currentglobal
	 4 1 roll
		dup type/nametype eq
		 {findfont}
	 if
	 dup gcheck setglobal
		dup dup maxlength 2 add dict
			begin
			exch
				{
				1 index/FID ne
				2 index/Encoding ne and
					{def}
					{pop pop}
				ifelse
				}
			forall
			/FontReferenced exch def
			/Encoding exch dup length array copy def
			/FontName 1 index dup type/stringtype eq{cvn}if def dup
			currentdict
			end
		definefont ct_VMDictPut
		setglobal
		}
	ifelse
	}bind def
/SetSubstituteStrategy
	{
	$SubstituteFont
		begin
		dup type/dicttype ne
			{0 dict}
		if
		currentdict/$Strategies known
			{
			exch $Strategies exch 
			2 copy known
				{
				get
				2 copy maxlength exch maxlength add dict
					begin
					{def}forall
					{def}forall
					currentdict
					dup/$Init known
						{dup/$Init get exec}
					if
					end
				/$Strategy exch def
				}
				{pop pop pop}
			ifelse
			}
			{pop pop}
		ifelse
		end
	}bind def
/scff
	{
	$SubstituteFont
		begin
		dup type/stringtype eq
			{dup length exch}
			{null}
		ifelse
		/$sname exch def
		/$slen exch def
		/$inVMIndex
			$sname null eq
				{
				1 index $str cvs
				dup length $slen sub $slen getinterval cvn
				}
				{$sname}
			ifelse def
		end
		{findfont}
	@Stopped
		{
		dup length 8 add string exch
		1 index 0(BadFont:)putinterval
		1 index exch 8 exch dup length string cvs putinterval cvn
			{findfont}
		@Stopped
			{pop/Courier findfont}
		if
		}
	if
	$SubstituteFont
		begin
		/$sname null def
		/$slen 0 def
		/$inVMIndex null def
		end
	}bind def
/isWidthsOnlyFont
	{
	dup/WidthsOnly known
		{pop pop true}
		{
		dup/FDepVector known
			{/FDepVector get{isWidthsOnlyFont dup{exit}if}forall}
			{
			dup/FDArray known
				{/FDArray get{isWidthsOnlyFont dup{exit}if}forall}
				{pop}
			ifelse
			}
		ifelse
		}
	ifelse
	}bind def
/ct_StyleDicts 4 dict dup begin
		 /Adobe-Japan1 4 dict dup begin
					 Level2?
								{
								/Serif
								/HeiseiMin-W3-83pv-RKSJ-H/Font resourcestatus
								{pop pop/HeiseiMin-W3}
								{
							/CIDFont/Category resourcestatus
							{
								pop pop
								/HeiseiMin-W3/CIDFont resourcestatus
								{pop pop/HeiseiMin-W3}
								{/Ryumin-Light}
								ifelse
							}
							{/Ryumin-Light}
							ifelse
								}
								ifelse
								def
								/SansSerif
								/HeiseiKakuGo-W5-83pv-RKSJ-H/Font resourcestatus
								{pop pop/HeiseiKakuGo-W5}
								{
							/CIDFont/Category resourcestatus
							{
								pop pop
								/HeiseiKakuGo-W5/CIDFont resourcestatus
								{pop pop/HeiseiKakuGo-W5}
								{/GothicBBB-Medium}
								ifelse
							}
							{/GothicBBB-Medium}
							ifelse
								}
								ifelse
								def
								/HeiseiMaruGo-W4-83pv-RKSJ-H/Font resourcestatus
								{pop pop/HeiseiMaruGo-W4}
								{
							/CIDFont/Category resourcestatus
							{
								pop pop
								/HeiseiMaruGo-W4/CIDFont resourcestatus
								{pop pop/HeiseiMaruGo-W4}
								{
									/Jun101-Light-RKSJ-H/Font resourcestatus
									{pop pop/Jun101-Light}
									{SansSerif}
									ifelse
								}
								ifelse
							}
							{
								/Jun101-Light-RKSJ-H/Font resourcestatus
								{pop pop/Jun101-Light}
								{SansSerif}
								ifelse
							}
							ifelse
								}
								ifelse
								/RoundSansSerif exch def
								/Default Serif def
								}
								{
								/Serif/Ryumin-Light def
								/SansSerif/GothicBBB-Medium def
								{
								(fonts/Jun101-Light-83pv-RKSJ-H)status
								}stopped
								{pop}{
										 {pop pop pop pop/Jun101-Light}
										 {SansSerif}
										 ifelse
										 /RoundSansSerif exch def
								}ifelse
								/Default Serif def
								}
					 ifelse
		 end
		 def
		 /Adobe-Korea1 4 dict dup begin
					/Serif/HYSMyeongJo-Medium def
					/SansSerif/HYGoThic-Medium def
					/RoundSansSerif SansSerif def
					/Default Serif def
		 end
		 def
		 /Adobe-GB1 4 dict dup begin
					/Serif/STSong-Light def
					/SansSerif/STHeiti-Regular def
					/RoundSansSerif SansSerif def
					/Default Serif def
		 end
		 def
		 /Adobe-CNS1 4 dict dup begin
					/Serif/MKai-Medium def
					/SansSerif/MHei-Medium def
					/RoundSansSerif SansSerif def
					/Default Serif def
		 end
		 def
end
def
Level2?{currentglobal true setglobal}if
/ct_BoldRomanWidthProc 
	{
	stringwidth 1 index 0 ne{exch .03 add exch}if setcharwidth
	0 0
	}bind def
/ct_Type0WidthProc 
	{
	 dup stringwidth 0 0 moveto 
	 2 index true charpath pathbbox
	 0 -1 
	 7 index 2 div .88 
	 setcachedevice2
	 pop
	0 0
	}bind def
/ct_Type0WMode1WidthProc 
	{
	 dup stringwidth 
	 pop 2 div neg -0.88
	2 copy
	moveto 
	0 -1
	 5 -1 roll true charpath pathbbox
	 setcachedevice
	}bind def
/cHexEncoding
[/c00/c01/c02/c03/c04/c05/c06/c07/c08/c09/c0A/c0B/c0C/c0D/c0E/c0F/c10/c11/c12
/c13/c14/c15/c16/c17/c18/c19/c1A/c1B/c1C/c1D/c1E/c1F/c20/c21/c22/c23/c24/c25
/c26/c27/c28/c29/c2A/c2B/c2C/c2D/c2E/c2F/c30/c31/c32/c33/c34/c35/c36/c37/c38
/c39/c3A/c3B/c3C/c3D/c3E/c3F/c40/c41/c42/c43/c44/c45/c46/c47/c48/c49/c4A/c4B
/c4C/c4D/c4E/c4F/c50/c51/c52/c53/c54/c55/c56/c57/c58/c59/c5A/c5B/c5C/c5D/c5E
/c5F/c60/c61/c62/c63/c64/c65/c66/c67/c68/c69/c6A/c6B/c6C/c6D/c6E/c6F/c70/c71
/c72/c73/c74/c75/c76/c77/c78/c79/c7A/c7B/c7C/c7D/c7E/c7F/c80/c81/c82/c83/c84
/c85/c86/c87/c88/c89/c8A/c8B/c8C/c8D/c8E/c8F/c90/c91/c92/c93/c94/c95/c96/c97
/c98/c99/c9A/c9B/c9C/c9D/c9E/c9F/cA0/cA1/cA2/cA3/cA4/cA5/cA6/cA7/cA8/cA9/cAA
/cAB/cAC/cAD/cAE/cAF/cB0/cB1/cB2/cB3/cB4/cB5/cB6/cB7/cB8/cB9/cBA/cBB/cBC/cBD
/cBE/cBF/cC0/cC1/cC2/cC3/cC4/cC5/cC6/cC7/cC8/cC9/cCA/cCB/cCC/cCD/cCE/cCF/cD0
/cD1/cD2/cD3/cD4/cD5/cD6/cD7/cD8/cD9/cDA/cDB/cDC/cDD/cDE/cDF/cE0/cE1/cE2/cE3
/cE4/cE5/cE6/cE7/cE8/cE9/cEA/cEB/cEC/cED/cEE/cEF/cF0/cF1/cF2/cF3/cF4/cF5/cF6
/cF7/cF8/cF9/cFA/cFB/cFC/cFD/cFE/cFF]def
/ct_BoldBaseFont 
	 11 dict begin
		/FontType 3 def
		/FontMatrix[1 0 0 1 0 0]def
		/FontBBox[0 0 1 1]def
		/Encoding cHexEncoding def 
		/_setwidthProc/ct_BoldRomanWidthProc load def
		/_bcstr1 1 string def
		/BuildChar
		{
			exch begin
				_basefont setfont
				_bcstr1 dup 0 4 -1 roll put
				dup 
				_setwidthProc
				3 copy 
				moveto				
				show
				_basefonto setfont
				moveto
				show
			end
		}bind def
		 currentdict
	 end 
def
systemdict/composefont known
{
/ct_DefineIdentity-H
{
	/Identity-H/CMap resourcestatus
	{
		pop pop
	}
	{
		/CIDInit/ProcSet findresource begin
		 12 dict begin
		 begincmap
		 /CIDSystemInfo 3 dict dup begin
			 /Registry(Adobe)def
			 /Ordering(Identity)def
			 /Supplement 0 def
		 end def
		 /CMapName/Identity-H def
		 /CMapVersion 1.000 def
		 /CMapType 1 def
		 1 begincodespacerange
		 <0000><FFFF>
		 endcodespacerange
		 1 begincidrange
		 <0000><FFFF>0
		 endcidrange
		 endcmap
		 CMapName currentdict/CMap defineresource pop
		 end
		 end
	 }
	 ifelse
}
def
/ct_BoldBaseCIDFont 
	 11 dict begin
		/CIDFontType 1 def
		/CIDFontName/ct_BoldBaseCIDFont def
		/FontMatrix[1 0 0 1 0 0]def
		/FontBBox[0 0 1 1]def
		/_setwidthProc/ct_Type0WidthProc load def
		/_bcstr2 2 string def
		/BuildGlyph
		{
			exch begin		 
				_basefont setfont
				_bcstr2 1 2 index 256 mod put
				_bcstr2 0 3 -1 roll 256 idiv put
				_bcstr2 dup _setwidthProc		 
				3 copy 
				moveto
				show
				_basefonto setfont
				moveto
				show
			end
		}bind def
		 currentdict
	 end 
def
}if
Level2?{setglobal}if
/ct_CopyFont{
	{
		1 index/FID ne 2 index/UniqueID ne and
		{def}{pop pop}ifelse
	}forall
}bind def
/ct_Type0CopyFont 
{
	exch
	dup length dict
	begin
	ct_CopyFont
	[
	exch
	FDepVector 
	{
		 dup/FontType get 0 eq
		{	
		1 index ct_Type0CopyFont 
		/_ctType0 exch definefont
		}
		{
		/_ctBaseFont exch
		2 index exec
		}
		 ifelse 
		 exch
	}
	forall 
	pop
	]				
	/FDepVector exch def
	currentdict
	end
}bind def
/ct_MakeBoldFont
{
	 dup/ct_SyntheticBold known
	{
		dup length 3 add dict begin 
		ct_CopyFont 
		/ct_StrokeWidth .03 0 FontMatrix idtransform pop def 
		/ct_SyntheticBold true def
		currentdict 
		end 
		definefont
	}
	{
		dup dup length 3 add dict
		begin
			ct_CopyFont
			/PaintType 2 def
			/StrokeWidth .03 0 FontMatrix idtransform pop def
			/dummybold currentdict
		end
		definefont
		dup/FontType get dup 9 ge exch 11 le and 
		{
			ct_BoldBaseCIDFont
			dup length 3 add dict copy begin
			dup/CIDSystemInfo get/CIDSystemInfo exch def
			ct_DefineIdentity-H
			/_Type0Identity/Identity-H 3 -1 roll[exch]composefont
			/_basefont exch def
			/_Type0Identity/Identity-H 3 -1 roll[exch]composefont
			/_basefonto exch def
			currentdict
			end
			/CIDFont defineresource
		}
		{
			ct_BoldBaseFont
			dup length 3 add dict copy begin
			/_basefont exch def
			/_basefonto exch def
			currentdict
			end
			definefont
		}
		ifelse
	}
	ifelse
}bind def
/ct_MakeBold{
	1 index 
	1 index
	findfont
	currentglobal 5 1 roll
	dup gcheck setglobal
		dup
		 /FontType get 0 eq
			{
				dup/WMode known{dup/WMode get 1 eq}{false}ifelse
				version length 4 ge
				and
					{version 0 4 getinterval cvi 2015 ge}
					{true}
				ifelse 
					{/ct_Type0WidthProc}
					{/ct_Type0WMode1WidthProc}
				ifelse
				ct_BoldBaseFont/_setwidthProc 3 -1 roll load put
						{ct_MakeBoldFont}ct_Type0CopyFont definefont
			}
			{
				dup/_fauxfont known not 1 index/SubstMaster known not and
				{
					 ct_BoldBaseFont/_setwidthProc /ct_BoldRomanWidthProc load put
					 ct_MakeBoldFont 
				}
				{
				2 index 2 index eq
					{exch pop	}
					{
						dup length dict begin
						ct_CopyFont
						currentdict
						end
						definefont 
					}
				ifelse
				}
			ifelse
			}
		 ifelse
		 pop pop pop
		 setglobal
}bind def
/?str1 256 string def
/?set
	{
	$SubstituteFont
		begin
		/$substituteFound false def
		/$fontname 1 index def
		/$doSmartSub false def
		end
	dup
	 findfont
	$SubstituteFont
		begin
		$substituteFound
			{false}
			{
			dup/FontName known
				{
				dup/FontName get $fontname eq
				1 index/DistillerFauxFont known not and
				/currentdistillerparams where
					{pop false 2 index isWidthsOnlyFont not and}
				if
				}
				{false}
			ifelse
			}
		ifelse
		exch pop
		/$doSmartSub true def
		end
		{
		5 1 roll pop pop pop pop
		findfont
		}
		{
		1 index
		findfont
		dup/FontType get 3 eq
		{
			6 1 roll pop pop pop pop pop false
		}
		{pop true}
		ifelse
		{
		$SubstituteFont
		begin
		pop pop
		/$styleArray 1 index def
		/$regOrdering 2 index def
		pop pop
		0 1 $styleArray length 1 sub
		{
			$styleArray exch get
			ct_StyleDicts $regOrdering
			2 copy known
			{
				get
				exch 2 copy known not
				{pop/Default}
				if
				get
				dup type/nametype eq
				{
				?str1 cvs length dup 1 add exch
				?str1 exch(-)putinterval
				exch dup length exch ?str1 exch 3 index exch putinterval
				add ?str1 exch 0 exch getinterval cvn
				}
				{
				pop pop/Unknown
				}
				ifelse
			}
			{
				pop pop pop pop/Unknown
			}
			ifelse
		}
		for
		end
		findfont 
		}if
		}
	ifelse
	currentglobal false setglobal 3 1 roll
	null copyfont definefont pop
	setglobal
	}bind def
setpacking
userdict/$SubstituteFont 25 dict put
1 dict
	begin
	/SubstituteFont
		dup $error exch 2 copy known
			{get}
			{pop pop{pop/Courier}bind}
		ifelse def
	/currentdistillerparams where dup
		{
		pop pop
		currentdistillerparams/CannotEmbedFontPolicy 2 copy known
			{get/Error eq}
			{pop pop false}
		ifelse
		}
	if not
		{
		countdictstack array dictstack 0 get
			begin
			userdict
				begin
				$SubstituteFont
					begin
					/$str 128 string def
					/$fontpat 128 string def
					/$slen 0 def
					/$sname null def
					/$match false def
					/$fontname null def
					/$substituteFound false def
					/$inVMIndex null def
					/$doSmartSub true def
					/$depth 0 def
					/$fontname null def
					/$italicangle 26.5 def
					/$dstack null def
					/$Strategies 10 dict dup
						begin
						/$Type3Underprint
							{
							currentglobal exch false setglobal
							11 dict
								begin
								/UseFont exch
									$WMode 0 ne
										{
										dup length dict copy
										dup/WMode $WMode put
										/UseFont exch definefont
										}
									if def
								/FontName $fontname dup type/stringtype eq{cvn}if def
								/FontType 3 def
								/FontMatrix[.001 0 0 .001 0 0]def
								/Encoding 256 array dup 0 1 255{/.notdef put dup}for pop def
								/FontBBox[0 0 0 0]def
								/CCInfo 7 dict dup
									begin
									/cc null def
									/x 0 def
									/y 0 def
									end def
								/BuildChar
									{
									exch
										begin
										CCInfo
											begin
											1 string dup 0 3 index put exch pop
											/cc exch def
											UseFont 1000 scalefont setfont
											cc stringwidth/y exch def/x exch def
											x y setcharwidth
											$SubstituteFont/$Strategy get/$Underprint get exec
											0 0 moveto cc show
											x y moveto
											end
										end
									}bind def
								currentdict
								end
							exch setglobal
							}bind def
						/$GetaTint
							2 dict dup
								begin
								/$BuildFont
									{
									dup/WMode known
										{dup/WMode get}
										{0}
									ifelse
									/$WMode exch def
									$fontname exch
									dup/FontName known
										{
										dup/FontName get
										dup type/stringtype eq{cvn}if
										}
										{/unnamedfont}
									ifelse
									exch
									Adobe_CoolType_Data/InVMDeepCopiedFonts get
									1 index/FontName get known
										{
										pop
										Adobe_CoolType_Data/InVMDeepCopiedFonts get
										1 index get
										null copyfont
										}
										{$deepcopyfont}
									ifelse
									exch 1 index exch/FontBasedOn exch put
									dup/FontName $fontname dup type/stringtype eq{cvn}if put
									definefont
									Adobe_CoolType_Data/InVMDeepCopiedFonts get
										begin
										dup/FontBasedOn get 1 index def
										end
									}bind def
								/$Underprint
									{
									gsave
									x abs y abs gt
										{/y 1000 def}
										{/x -1000 def 500 120 translate}
									ifelse
									Level2?
										{
										[/Separation(All)/DeviceCMYK{0 0 0 1 pop}]
										setcolorspace
										}
										{0 setgray}
									ifelse
									10 setlinewidth
									x .8 mul
									[7 3]
										{
										y mul 8 div 120 sub x 10 div exch moveto
										0 y 4 div neg rlineto
										dup 0 rlineto
										0 y 4 div rlineto
										closepath
										gsave
										Level2?
											{.2 setcolor}
											{.8 setgray}
										ifelse
										fill grestore
										stroke
										}
									forall
									pop
									grestore
									}bind def
								end def
						/$Oblique
							1 dict dup
								begin
								/$BuildFont
									{
									currentglobal exch dup gcheck setglobal
									null copyfont
										begin
										/FontBasedOn
										currentdict/FontName known
											{
											FontName
											dup type/stringtype eq{cvn}if
											}
											{/unnamedfont}
										ifelse
										def
										/FontName $fontname dup type/stringtype eq{cvn}if def
										/currentdistillerparams where
											{pop}
											{
											/FontInfo currentdict/FontInfo known
												{FontInfo null copyfont}
												{2 dict}
											ifelse
											dup
												begin
												/ItalicAngle $italicangle def
												/FontMatrix FontMatrix
												[1 0 ItalicAngle dup sin exch cos div 1 0 0]
												matrix concatmatrix readonly
												end
											4 2 roll def
											def
											}
										ifelse
										FontName currentdict
										end
									definefont
									exch setglobal
									}bind def
								end def
						/$None
							1 dict dup
								begin
								/$BuildFont{}bind def
								end def
						end def
					/$Oblique SetSubstituteStrategy
					/$findfontByEnum
						{
						dup type/stringtype eq{cvn}if
						dup/$fontname exch def
						$sname null eq
							{$str cvs dup length $slen sub $slen getinterval}
							{pop $sname}
						ifelse
						$fontpat dup 0(fonts/*)putinterval exch 7 exch putinterval
						/$match false def
						$SubstituteFont/$dstack countdictstack array dictstack put
						mark
							{
							$fontpat 0 $slen 7 add getinterval
								{/$match exch def exit}
							$str filenameforall
							}
						stopped
							{
							cleardictstack
							currentdict
							true
							$SubstituteFont/$dstack get
								{
								exch
									{
									1 index eq
										{pop false}
										{true}
									ifelse
									}
									{begin false}
								ifelse
								}
							forall
							pop
							}
						if
						cleartomark
						/$slen 0 def
						$match false ne
							{$match(fonts/)anchorsearch pop pop cvn}
							{/Courier}
						ifelse
						}bind def
					/$ROS 1 dict dup
						begin
						/Adobe 4 dict dup
							begin
							/Japan1 [/Ryumin-Light/HeiseiMin-W3
										 /GothicBBB-Medium/HeiseiKakuGo-W5
										 /HeiseiMaruGo-W4/Jun101-Light]def
							/Korea1 [/HYSMyeongJo-Medium/HYGoThic-Medium]def
							/GB1	 [/STSong-Light/STHeiti-Regular]def
							/CNS1	[/MKai-Medium/MHei-Medium]def
							end def
						end def
					/$cmapname null def
					/$deepcopyfont
						{
						dup/FontType get 0 eq
							{
							1 dict dup/FontName/copied put copyfont
								begin
								/FDepVector FDepVector copyarray
								0 1 2 index length 1 sub
									{
									2 copy get $deepcopyfont
									dup/FontName/copied put
									/copied exch definefont
									3 copy put pop pop
									}
								for
								def
								currentdict
								end
							}
							{$Strategies/$Type3Underprint get exec}
						ifelse
						}bind def
					/$buildfontname
						{
						dup/CIDFont findresource/CIDSystemInfo get
							begin
							Registry length Ordering length Supplement 8 string cvs
							3 copy length 2 add add add string
							dup 5 1 roll dup 0 Registry putinterval
							dup 4 index(-)putinterval
							dup 4 index 1 add Ordering putinterval
							4 2 roll add 1 add 2 copy(-)putinterval
							end
						1 add 2 copy 0 exch getinterval $cmapname $fontpat cvs exch
						anchorsearch
							{pop pop 3 2 roll putinterval cvn/$cmapname exch def}
							{pop pop pop pop pop}
						ifelse
						length
						$str 1 index(-)putinterval 1 add
						$str 1 index $cmapname $fontpat cvs putinterval
						$cmapname length add
						$str exch 0 exch getinterval cvn
						}bind def
					/$findfontByROS
						{
						/$fontname exch def
						$ROS Registry 2 copy known
							{
							get Ordering 2 copy known
								{get}
								{pop pop[]}
							ifelse
							}
							{pop pop[]}
						ifelse
						false exch
							{
							dup/CIDFont resourcestatus
								{
								pop pop
								save
								1 index/CIDFont findresource
								dup/WidthsOnly known
									{dup/WidthsOnly get}
									{false}
								ifelse
								exch pop
								exch restore
									{pop}
									{exch pop true exit}
								ifelse
								}
								{pop}
							ifelse
							}
						forall
							{$str cvs $buildfontname}
							{
							false(*)
								{
								save exch
								dup/CIDFont findresource
								dup/WidthsOnly known
									{dup/WidthsOnly get not}
									{true}
								ifelse
								exch/CIDSystemInfo get
								dup/Registry get Registry eq
								exch/Ordering get Ordering eq and and
									{exch restore exch pop true exit}
									{pop restore}
								ifelse
								}
							$str/CIDFont resourceforall
								{$buildfontname}
								{$fontname $findfontByEnum}
							ifelse
							}
						ifelse
						}bind def
					end
				end
				currentdict/$error known currentdict/languagelevel known and dup
					{pop $error/SubstituteFont known}
				if
				dup
					{$error}
					{Adobe_CoolType_Core}
				ifelse
				begin
					{
					/SubstituteFont
					/CMap/Category resourcestatus
						{
						pop pop
						{
						$SubstituteFont
							begin
							/$substituteFound true def
							dup length $slen gt
							$sname null ne or
							$slen 0 gt and
								{
								$sname null eq
									{dup $str cvs dup length $slen sub $slen getinterval cvn}
									{$sname}
								ifelse
								Adobe_CoolType_Data/InVMFontsByCMap get
								1 index 2 copy known
									{
									get
									false exch
										{
										pop
										currentglobal
											{
											GlobalFontDirectory 1 index known
												{exch pop true exit}
												{pop}
											ifelse
											}
											{
											FontDirectory 1 index known
												{exch pop true exit}
												{
												GlobalFontDirectory 1 index known
													{exch pop true exit}
													{pop}
												ifelse
												}
											ifelse
											}
										ifelse
										}
									forall
									}
									{pop pop false}
								ifelse
									{
									exch pop exch pop
									}
									{
									dup/CMap resourcestatus
										{
										pop pop
										dup/$cmapname exch def
										/CMap findresource/CIDSystemInfo get{def}forall
										$findfontByROS
										}
										{
										128 string cvs
										dup(-)search
											{
											3 1 roll search
												{
												3 1 roll pop
													{dup cvi}
												stopped
													{pop pop pop pop pop $findfontByEnum}
													{
													4 2 roll pop pop
													exch length
													exch
													2 index length
													2 index
													sub
													exch 1 sub -1 0
														{
														$str cvs dup length
														4 index
														0
														4 index
														4 3 roll add
														getinterval
														exch 1 index exch 3 index exch
														putinterval
														dup/CMap resourcestatus
															{
															pop pop
															4 1 roll pop pop pop
															dup/$cmapname exch def
															/CMap findresource/CIDSystemInfo get{def}forall
															$findfontByROS
															true exit
															}
															{pop}
														ifelse
														}
													for
													dup type/booleantype eq
														{pop}
														{pop pop pop $findfontByEnum}
													ifelse
													}
												ifelse
												}
												{pop pop pop $findfontByEnum}
											ifelse
											}
											{pop pop $findfontByEnum}
										ifelse
										}
									ifelse
									}
								ifelse
								}
								{//SubstituteFont exec}
							ifelse
							/$slen 0 def
							end
						}
						}
						{
						{
						$SubstituteFont
							begin
							/$substituteFound true def
							dup length $slen gt
							$sname null ne or
							$slen 0 gt and
								{$findfontByEnum}
								{//SubstituteFont exec}
							ifelse
							end
						}
						}
					ifelse
					bind readonly def
					Adobe_CoolType_Core/scfindfont/systemfindfont load put
					}
					{
					/scfindfont
						{
						$SubstituteFont
							begin
							dup systemfindfont
							dup/FontName known
								{dup/FontName get dup 3 index ne}
								{/noname true}
							ifelse
							dup
								{
								/$origfontnamefound 2 index def
								/$origfontname 4 index def/$substituteFound true def
								}
							if
							exch pop
								{
								$slen 0 gt
								$sname null ne
								3 index length $slen gt or and
									{
									pop dup $findfontByEnum findfont
									dup maxlength 1 add dict
										begin
											{1 index/FID eq{pop pop}{def}ifelse}
										forall
										currentdict
										end
									definefont
									dup/FontName known{dup/FontName get}{null}ifelse
									$origfontnamefound ne
										{
										$origfontname $str cvs print
										( substitution revised, using )print
										dup/FontName known
											{dup/FontName get}{(unspecified font)}
										ifelse
										$str cvs print(.\n)print
										}
									if
									}
									{exch pop}
								ifelse
								}
								{exch pop}
							ifelse
							end
						}bind def
					}
				ifelse
				end
			end
		Adobe_CoolType_Core_Defined not
			{
			Adobe_CoolType_Core/findfont
				{
				$SubstituteFont
					begin
					$depth 0 eq
						{
						/$fontname 1 index dup type/stringtype ne{$str cvs}if def
						/$substituteFound false def
						}
					if
					/$depth $depth 1 add def
					end
				scfindfont
				$SubstituteFont
					begin
					/$depth $depth 1 sub def
					$substituteFound $depth 0 eq and
						{
						$inVMIndex null ne
							{dup $inVMIndex $AddInVMFont}
						if
						$doSmartSub
							{
							currentdict/$Strategy known
								{$Strategy/$BuildFont get exec}
							if
							}
						if
						}
					if
					end
				}bind put
			}
		if
		}
	if
	end
/$AddInVMFont
	{
	exch/FontName 2 copy known
		{
		get
		1 dict dup begin exch 1 index gcheck def end exch
		Adobe_CoolType_Data/InVMFontsByCMap get exch
		$DictAdd
		}
		{pop pop pop}
	ifelse
	}bind def
/$DictAdd
	{
	2 copy known not
		{2 copy 4 index length dict put}
	if
	Level2? not
		{
		2 copy get dup maxlength exch length 4 index length add lt
		2 copy get dup length 4 index length add exch maxlength 1 index lt
			{
			2 mul dict
				begin
				2 copy get{forall}def
				2 copy currentdict put
				end
			}
			{pop}
		ifelse
		}
	if
	get
		begin
			{def}
		forall
		end
	}bind def
end
end
%%EndResource
currentglobal true setglobal
%%BeginResource: procset Adobe_CoolType_Utility_MAKEOCF 1.23 0
%%Copyright: Copyright 1987-2006 Adobe Systems Incorporated.
%%Version: 1.23 0
systemdict/languagelevel known dup
	{currentglobal false setglobal}
	{false}
ifelse
exch
userdict/Adobe_CoolType_Utility 2 copy known
	{2 copy get dup maxlength 27 add dict copy}
	{27 dict}
ifelse put
Adobe_CoolType_Utility
	begin
	/@eexecStartData
		 <BAB431EA07F209EB8C4348311481D9D3F76E3D15246555577D87BC510ED54E
		 118C39697FA9F6DB58128E60EB8A12FA24D7CDD2FA94D221FA9EC8DA3E5E6A1C
		 4ACECC8C2D39C54E7C946031DD156C3A6B4A09AD29E1867A>def
	/@recognizeCIDFont null def
	/ct_Level2? exch def
	/ct_Clone? 1183615869 internaldict dup
			/CCRun known not
			exch/eCCRun known not
			ct_Level2? and or def
ct_Level2?
	{globaldict begin currentglobal true setglobal}
if
	/ct_AddStdCIDMap
		ct_Level2?
			{{
				mark
				Adobe_CoolType_Utility/@recognizeCIDFont currentdict put
					{
					((Hex)57 StartData
					 0615 1e27 2c39 1c60 d8a8 cc31 fe2b f6e0
					 7aa3 e541 e21c 60d8 a8c9 c3d0 6d9e 1c60
					 d8a8 c9c2 02d7 9a1c 60d8 a849 1c60 d8a8
					 cc36 74f4 1144 b13b 77)0()/SubFileDecode filter cvx exec
					}
				stopped
					{
					 cleartomark
					 Adobe_CoolType_Utility/@recognizeCIDFont get
					 countdictstack dup array dictstack
					 exch 1 sub -1 0
						 {
						 2 copy get 3 index eq
								{1 index length exch sub 1 sub{end}repeat exit}
								{pop}
						 ifelse
						 }
					 for
					 pop pop
					 Adobe_CoolType_Utility/@eexecStartData get eexec
					}
					{cleartomark}
				ifelse
			}}
			{{
				Adobe_CoolType_Utility/@eexecStartData get eexec
			}}
		ifelse bind def
userdict/cid_extensions known
dup{cid_extensions/cid_UpdateDB known and}if
	{
	 cid_extensions
	 begin
	/cid_GetCIDSystemInfo
		{
		 1 index type/stringtype eq
			{exch cvn exch}
		 if
		 cid_extensions
			 begin
			 dup load 2 index known
				{
				 2 copy
				 cid_GetStatusInfo
				 dup null ne
					{
					 1 index load
					 3 index get
					 dup null eq
						 {pop pop cid_UpdateDB}
						 {
						 exch
						 1 index/Created get eq
							 {exch pop exch pop}
							 {pop cid_UpdateDB}
						 ifelse
						 }
					 ifelse
					}
					{pop cid_UpdateDB}
				 ifelse
				}
				{cid_UpdateDB}
			 ifelse
			 end
		}bind def
	 end
	}
if
ct_Level2?
	{end setglobal}
if
	/ct_UseNativeCapability? systemdict/composefont known def
	/ct_MakeOCF 35 dict def
	/ct_Vars 25 dict def
	/ct_GlyphDirProcs 6 dict def
	/ct_BuildCharDict 15 dict dup
		begin
		/charcode 2 string def
		/dst_string 1500 string def
		/nullstring()def
		/usewidths? true def
		end def
	ct_Level2?{setglobal}{pop}ifelse
	ct_GlyphDirProcs
		begin
		/GetGlyphDirectory
			{
			systemdict/languagelevel known
				{pop/CIDFont findresource/GlyphDirectory get}
				{
				1 index/CIDFont findresource/GlyphDirectory
				get dup type/dicttype eq
					{
					dup dup maxlength exch length sub 2 index lt
						{
						dup length 2 index add dict copy 2 index
						/CIDFont findresource/GlyphDirectory 2 index put
						}
					if
					}
				if
				exch pop exch pop
				}
			ifelse
			+
			}def
		/+
			{
			systemdict/languagelevel known
				{
				currentglobal false setglobal
				3 dict begin
					/vm exch def
				}
				{1 dict begin}
			ifelse
			/$ exch def
			systemdict/languagelevel known
				{
				vm setglobal
				/gvm currentglobal def
				$ gcheck setglobal
				}
			if
			?{$ begin}if
			}def
		/?{$ type/dicttype eq}def
		/|{
			userdict/Adobe_CoolType_Data known
				{
			Adobe_CoolType_Data/AddWidths? known
				{
				 currentdict Adobe_CoolType_Data
					begin
					 begin
						AddWidths?
								{
								Adobe_CoolType_Data/CC 3 index put
								?{def}{$ 3 1 roll put}ifelse
								CC charcode exch 1 index 0 2 index 256 idiv put
								1 index exch 1 exch 256 mod put
								stringwidth 2 array astore
								currentfont/Widths get exch CC exch put
								}
								{?{def}{$ 3 1 roll put}ifelse}
							ifelse
					end
				end
				}
				{?{def}{$ 3 1 roll put}ifelse}	ifelse
				}
				{?{def}{$ 3 1 roll put}ifelse}
			ifelse
			}def
		/!
			{
			?{end}if
			systemdict/languagelevel known
				{gvm setglobal}
			if
			end
			}def
		/:{string currentfile exch readstring pop}executeonly def
		end
	ct_MakeOCF
		begin
		/ct_cHexEncoding
		[/c00/c01/c02/c03/c04/c05/c06/c07/c08/c09/c0A/c0B/c0C/c0D/c0E/c0F/c10/c11/c12
		/c13/c14/c15/c16/c17/c18/c19/c1A/c1B/c1C/c1D/c1E/c1F/c20/c21/c22/c23/c24/c25
		/c26/c27/c28/c29/c2A/c2B/c2C/c2D/c2E/c2F/c30/c31/c32/c33/c34/c35/c36/c37/c38
		/c39/c3A/c3B/c3C/c3D/c3E/c3F/c40/c41/c42/c43/c44/c45/c46/c47/c48/c49/c4A/c4B
		/c4C/c4D/c4E/c4F/c50/c51/c52/c53/c54/c55/c56/c57/c58/c59/c5A/c5B/c5C/c5D/c5E
		/c5F/c60/c61/c62/c63/c64/c65/c66/c67/c68/c69/c6A/c6B/c6C/c6D/c6E/c6F/c70/c71
		/c72/c73/c74/c75/c76/c77/c78/c79/c7A/c7B/c7C/c7D/c7E/c7F/c80/c81/c82/c83/c84
		/c85/c86/c87/c88/c89/c8A/c8B/c8C/c8D/c8E/c8F/c90/c91/c92/c93/c94/c95/c96/c97
		/c98/c99/c9A/c9B/c9C/c9D/c9E/c9F/cA0/cA1/cA2/cA3/cA4/cA5/cA6/cA7/cA8/cA9/cAA
		/cAB/cAC/cAD/cAE/cAF/cB0/cB1/cB2/cB3/cB4/cB5/cB6/cB7/cB8/cB9/cBA/cBB/cBC/cBD
		/cBE/cBF/cC0/cC1/cC2/cC3/cC4/cC5/cC6/cC7/cC8/cC9/cCA/cCB/cCC/cCD/cCE/cCF/cD0
		/cD1/cD2/cD3/cD4/cD5/cD6/cD7/cD8/cD9/cDA/cDB/cDC/cDD/cDE/cDF/cE0/cE1/cE2/cE3
		/cE4/cE5/cE6/cE7/cE8/cE9/cEA/cEB/cEC/cED/cEE/cEF/cF0/cF1/cF2/cF3/cF4/cF5/cF6
		/cF7/cF8/cF9/cFA/cFB/cFC/cFD/cFE/cFF]def
		/ct_CID_STR_SIZE 8000 def
		/ct_mkocfStr100 100 string def
		/ct_defaultFontMtx[.001 0 0 .001 0 0]def
		/ct_1000Mtx[1000 0 0 1000 0 0]def
		/ct_raise{exch cvx exch errordict exch get exec stop}bind def
		/ct_reraise
			{cvx $error/errorname get(Error: )print dup(						 )cvs print
					errordict exch get exec stop
			}bind def
		/ct_cvnsi
			{
			1 index add 1 sub 1 exch 0 4 1 roll
				{
				2 index exch get
				exch 8 bitshift
				add
				}
			for
			exch pop
			}bind def
		/ct_GetInterval
			{
			Adobe_CoolType_Utility/ct_BuildCharDict get
				begin
				/dst_index 0 def
				dup dst_string length gt
					{dup string/dst_string exch def}
				if
				1 index ct_CID_STR_SIZE idiv
				/arrayIndex exch def
				2 index arrayIndex get
				2 index
				arrayIndex ct_CID_STR_SIZE mul
				sub
					{
					dup 3 index add 2 index length le
						{
						2 index getinterval
						dst_string dst_index 2 index putinterval
						length dst_index add/dst_index exch def
						exit
						}
						{
						1 index length 1 index sub
						dup 4 1 roll
						getinterval
						dst_string dst_index 2 index putinterval
						pop dup dst_index add/dst_index exch def
						sub
						/arrayIndex arrayIndex 1 add def
						2 index dup length arrayIndex gt
							 {arrayIndex get}
							 {
							 pop
							 exit
							 }
						ifelse
						0
						}
					ifelse
					}
				loop
				pop pop pop
				dst_string 0 dst_index getinterval
				end
			}bind def
		ct_Level2?
			{
			/ct_resourcestatus
			currentglobal mark true setglobal
				{/unknowninstancename/Category resourcestatus}
			stopped
				{cleartomark setglobal true}
				{cleartomark currentglobal not exch setglobal}
			ifelse
				{
					{
					mark 3 1 roll/Category findresource
						begin
						ct_Vars/vm currentglobal put
						({ResourceStatus}stopped)0()/SubFileDecode filter cvx exec
							{cleartomark false}
							{{3 2 roll pop true}{cleartomark false}ifelse}
						ifelse
						ct_Vars/vm get setglobal
						end
					}
				}
				{{resourcestatus}}
			ifelse bind def
			/CIDFont/Category ct_resourcestatus
				{pop pop}
				{
				currentglobal true setglobal
				/Generic/Category findresource
				dup length dict copy
				dup/InstanceType/dicttype put
				/CIDFont exch/Category defineresource pop
				setglobal
				}
			ifelse
			ct_UseNativeCapability?
				{
				/CIDInit/ProcSet findresource begin
				12 dict begin
				begincmap
				/CIDSystemInfo 3 dict dup begin
				 /Registry(Adobe)def
				 /Ordering(Identity)def
				 /Supplement 0 def
				end def
				/CMapName/Identity-H def
				/CMapVersion 1.000 def
				/CMapType 1 def
				1 begincodespacerange
				<0000><FFFF>
				endcodespacerange
				1 begincidrange
				<0000><FFFF>0
				endcidrange
				endcmap
				CMapName currentdict/CMap defineresource pop
				end
				end
				}
			if
			}
			{
			/ct_Category 2 dict begin
			/CIDFont 10 dict def
			/ProcSet	2 dict def
			currentdict
			end
			def
			/defineresource
				{
				ct_Category 1 index 2 copy known
					{
					get
					dup dup maxlength exch length eq
						{
						dup length 10 add dict copy
						ct_Category 2 index 2 index put
						}
					if
					3 index 3 index put
					pop exch pop
					}
					{pop pop/defineresource/undefined ct_raise}
				ifelse
				}bind def
			/findresource
				{
				ct_Category 1 index 2 copy known
					{
					get
					2 index 2 copy known
						{get 3 1 roll pop pop}
						{pop pop/findresource/undefinedresource ct_raise}
					ifelse
					}
					{pop pop/findresource/undefined ct_raise}
				ifelse
				}bind def
			/resourcestatus
				{
				ct_Category 1 index 2 copy known
					{
					get
					2 index known
					exch pop exch pop
						{
						0 -1 true
						}
						{
						false
						}
					ifelse
					}
					{pop pop/findresource/undefined ct_raise}
				ifelse
				}bind def
			/ct_resourcestatus/resourcestatus load def
			}
		ifelse
		/ct_CIDInit 2 dict
			begin
			/ct_cidfont_stream_init
				{
					{
					dup(Binary)eq
						{
						pop
						null
						currentfile
						ct_Level2?
							{
								{cid_BYTE_COUNT()/SubFileDecode filter}
							stopped
								{pop pop pop}
							if
							}
						if
						/readstring load
						exit
						}
					if
					dup(Hex)eq
						{
						pop
						currentfile
						ct_Level2?
							{
								{null exch/ASCIIHexDecode filter/readstring}
							stopped
								{pop exch pop(>)exch/readhexstring}
							if
							}
							{(>)exch/readhexstring}
						ifelse
						load
						exit
						}
					if
					/StartData/typecheck ct_raise
					}
				loop
				cid_BYTE_COUNT ct_CID_STR_SIZE le
					{
					2 copy cid_BYTE_COUNT string exch exec
					pop
					1 array dup
					3 -1 roll
					0 exch put
					}
					{
					cid_BYTE_COUNT ct_CID_STR_SIZE div ceiling cvi
					dup array exch 2 sub 0 exch 1 exch
						{
						2 copy
						5 index
						ct_CID_STR_SIZE
						string
						6 index exec
						pop
						put
						pop
						}
					for
					2 index
					cid_BYTE_COUNT ct_CID_STR_SIZE mod string
					3 index exec
					pop
					1 index exch
					1 index length 1 sub
					exch put
					}
				ifelse
				cid_CIDFONT exch/GlyphData exch put
				2 index null eq
					{
					pop pop pop
					}
					{
					pop/readstring load
					1 string exch
						{
						3 copy exec
						pop
						dup length 0 eq
							{
							pop pop pop pop pop
							true exit
							}
						if
						4 index
						eq
							{
							pop pop pop pop
							false exit
							}
						if
						}
					loop
					pop
					}
				ifelse
				}bind def
			/StartData
				{
				mark
					{
					currentdict
					dup/FDArray get 0 get/FontMatrix get
					0 get 0.001 eq
						{
						dup/CDevProc known not
							{
							/CDevProc 1183615869 internaldict/stdCDevProc 2 copy known
								{get}
								{
								pop pop
								{pop pop pop pop pop 0 -1000 7 index 2 div 880}
								}
							ifelse
							def
							}
						if
						}
						{
						/CDevProc
							{
							 pop pop pop pop pop
							 0
							 1 cid_temp/cid_CIDFONT get
							/FDArray get 0 get
							/FontMatrix get 0 get div
							 7 index 2 div
							 1 index 0.88 mul
							}def
						}
					ifelse
					/cid_temp 15 dict def
					cid_temp
						begin
						/cid_CIDFONT exch def
						3 copy pop
						dup/cid_BYTE_COUNT exch def 0 gt
							{
							ct_cidfont_stream_init
							FDArray
								{
								/Private get
								dup/SubrMapOffset known
									{
									begin
									/Subrs SubrCount array def
									Subrs
									SubrMapOffset
									SubrCount
									SDBytes
									ct_Level2?
										{
										currentdict dup/SubrMapOffset undef
										dup/SubrCount undef
										/SDBytes undef
										}
									if
									end
									/cid_SD_BYTES exch def
									/cid_SUBR_COUNT exch def
									/cid_SUBR_MAP_OFFSET exch def
									/cid_SUBRS exch def
									cid_SUBR_COUNT 0 gt
										{
										GlyphData cid_SUBR_MAP_OFFSET cid_SD_BYTES ct_GetInterval
										0 cid_SD_BYTES ct_cvnsi
										0 1 cid_SUBR_COUNT 1 sub
											{
											exch 1 index
											1 add
											cid_SD_BYTES mul cid_SUBR_MAP_OFFSET add
											GlyphData exch cid_SD_BYTES ct_GetInterval
											0 cid_SD_BYTES ct_cvnsi
											cid_SUBRS 4 2 roll
											GlyphData exch
											4 index
											1 index
											sub
											ct_GetInterval
											dup length string copy put
											}
										for
										pop
										}
									if
									}
									{pop}
								ifelse
								}
							forall
							}
						if
						cleartomark pop pop
						end
					CIDFontName currentdict/CIDFont defineresource pop
					end end
					}
				stopped
					{cleartomark/StartData ct_reraise}
				if
				}bind def
			currentdict
			end def
		/ct_saveCIDInit
			{
			/CIDInit/ProcSet ct_resourcestatus
				{true}
				{/CIDInitC/ProcSet ct_resourcestatus}
			ifelse
				{
				pop pop
				/CIDInit/ProcSet findresource
				ct_UseNativeCapability?
					{pop null}
					{/CIDInit ct_CIDInit/ProcSet defineresource pop}
				ifelse
				}
				{/CIDInit ct_CIDInit/ProcSet defineresource pop null}
			ifelse
			ct_Vars exch/ct_oldCIDInit exch put
			}bind def
		/ct_restoreCIDInit
			{
			ct_Vars/ct_oldCIDInit get dup null ne
				{/CIDInit exch/ProcSet defineresource pop}
				{pop}
			ifelse
			}bind def
		/ct_BuildCharSetUp
			{
			1 index
				begin
				CIDFont
					begin
					Adobe_CoolType_Utility/ct_BuildCharDict get
						begin
						/ct_dfCharCode exch def
						/ct_dfDict exch def
						CIDFirstByte ct_dfCharCode add
						dup CIDCount ge
							{pop 0}
						if
						/cid exch def
							{
							GlyphDirectory cid 2 copy known
								{get}
								{pop pop nullstring}
							ifelse
							dup length FDBytes sub 0 gt
								{
								dup
								FDBytes 0 ne
									{0 FDBytes ct_cvnsi}
									{pop 0}
								ifelse
								/fdIndex exch def
								dup length FDBytes sub FDBytes exch getinterval
								/charstring exch def
								exit
								}
								{
								pop
								cid 0 eq
									{/charstring nullstring def exit}
								if
								/cid 0 def
								}
							ifelse
							}
						loop
			}def
		/ct_SetCacheDevice
			{
			0 0 moveto
			dup stringwidth
			3 -1 roll
			true charpath
			pathbbox
			0 -1000
			7 index 2 div 880
			setcachedevice2
			0 0 moveto
			}def
		/ct_CloneSetCacheProc
			{
			1 eq
				{
				stringwidth
				pop -2 div -880
				0 -1000 setcharwidth
				moveto
				}
				{
				usewidths?
					{
					currentfont/Widths get cid
					2 copy known
						{get exch pop aload pop}
						{pop pop stringwidth}
					ifelse
					}
					{stringwidth}
				ifelse
				setcharwidth
				0 0 moveto
				}
			ifelse
			}def
		/ct_Type3ShowCharString
			{
			ct_FDDict fdIndex 2 copy known
				{get}
				{
				currentglobal 3 1 roll
				1 index gcheck setglobal
				ct_Type1FontTemplate dup maxlength dict copy
					begin
					FDArray fdIndex get
					dup/FontMatrix 2 copy known
						{get}
						{pop pop ct_defaultFontMtx}
					ifelse
					/FontMatrix exch dup length array copy def
					/Private get
					/Private exch def
					/Widths rootfont/Widths get def
					/CharStrings 1 dict dup/.notdef
						<d841272cf18f54fc13>dup length string copy put def
					currentdict
					end
				/ct_Type1Font exch definefont
				dup 5 1 roll put
				setglobal
				}
			ifelse
			dup/CharStrings get 1 index/Encoding get
			ct_dfCharCode get charstring put
			rootfont/WMode 2 copy known
				{get}
				{pop pop 0}
			ifelse
			exch
			1000 scalefont setfont
			ct_str1 0 ct_dfCharCode put
			ct_str1 exch ct_dfSetCacheProc
			ct_SyntheticBold
				{
				currentpoint
				ct_str1 show
				newpath
				moveto
				ct_str1 true charpath
				ct_StrokeWidth setlinewidth
				stroke
				}
				{ct_str1 show}
			ifelse
			}def
		/ct_Type4ShowCharString
			{
			ct_dfDict ct_dfCharCode charstring
			FDArray fdIndex get
			dup/FontMatrix get dup ct_defaultFontMtx ct_matrixeq not
				{ct_1000Mtx matrix concatmatrix concat}
				{pop}
			ifelse
			/Private get
			Adobe_CoolType_Utility/ct_Level2? get not
				{
				ct_dfDict/Private
				3 -1 roll
					{put}
				1183615869 internaldict/superexec get exec
				}
			if
			1183615869 internaldict
			Adobe_CoolType_Utility/ct_Level2? get
				{1 index}
				{3 index/Private get mark 6 1 roll}
			ifelse
			dup/RunInt known
				{/RunInt get}
				{pop/CCRun}
			ifelse
			get exec
			Adobe_CoolType_Utility/ct_Level2? get not
				{cleartomark}
			if
			}bind def
		/ct_BuildCharIncremental
			{
				{
				Adobe_CoolType_Utility/ct_MakeOCF get begin
				ct_BuildCharSetUp
				ct_ShowCharString
				}
			stopped
				{stop}
			if
			end
			end
			end
			end
			}bind def
		/BaseFontNameStr(BF00)def
		/ct_Type1FontTemplate 14 dict
			begin
			/FontType 1 def
			/FontMatrix [0.001 0 0 0.001 0 0]def
			/FontBBox [-250 -250 1250 1250]def
			/Encoding ct_cHexEncoding def
			/PaintType 0 def
			currentdict
			end def
		/BaseFontTemplate 11 dict
			begin
			/FontMatrix [0.001 0 0 0.001 0 0]def
			/FontBBox [-250 -250 1250 1250]def
			/Encoding ct_cHexEncoding def
			/BuildChar/ct_BuildCharIncremental load def
			ct_Clone?
				{
				/FontType 3 def
				/ct_ShowCharString/ct_Type3ShowCharString load def
				/ct_dfSetCacheProc/ct_CloneSetCacheProc load def
				/ct_SyntheticBold false def
				/ct_StrokeWidth 1 def
				}
				{
				/FontType 4 def
				/Private 1 dict dup/lenIV 4 put def
				/CharStrings 1 dict dup/.notdef<d841272cf18f54fc13>put def
				/PaintType 0 def
				/ct_ShowCharString/ct_Type4ShowCharString load def
				}
			ifelse
			/ct_str1 1 string def
			currentdict
			end def
		/BaseFontDictSize BaseFontTemplate length 5 add def
		/ct_matrixeq
			{
			true 0 1 5
				{
				dup 4 index exch get exch 3 index exch get eq and
				dup not
					{exit}
				if
				}
			for
			exch pop exch pop
			}bind def
		/ct_makeocf
			{
			15 dict
				begin
				exch/WMode exch def
				exch/FontName exch def
				/FontType 0 def
				/FMapType 2 def
			dup/FontMatrix known
				{dup/FontMatrix get/FontMatrix exch def}
				{/FontMatrix matrix def}
			ifelse
				/bfCount 1 index/CIDCount get 256 idiv 1 add
					dup 256 gt{pop 256}if def
				/Encoding
					256 array 0 1 bfCount 1 sub{2 copy dup put pop}for
					bfCount 1 255{2 copy bfCount put pop}for
					def
				/FDepVector bfCount dup 256 lt{1 add}if array def
				BaseFontTemplate BaseFontDictSize dict copy
					begin
					/CIDFont exch def
					CIDFont/FontBBox known
						{CIDFont/FontBBox get/FontBBox exch def}
					if
					CIDFont/CDevProc known
						{CIDFont/CDevProc get/CDevProc exch def}
					if
					currentdict
					end
				BaseFontNameStr 3(0)putinterval
				0 1 bfCount dup 256 eq{1 sub}if
					{
					FDepVector exch
					2 index BaseFontDictSize dict copy
						begin
						dup/CIDFirstByte exch 256 mul def
						FontType 3 eq
							{/ct_FDDict 2 dict def}
						if
						currentdict
						end
					1 index 16
					BaseFontNameStr 2 2 getinterval cvrs pop
					BaseFontNameStr exch definefont
					put
					}
				for
				ct_Clone?
					{/Widths 1 index/CIDFont get/GlyphDirectory get length dict def}
				if
				FontName
				currentdict
				end
			definefont
			ct_Clone?
				{
				gsave
				dup 1000 scalefont setfont
				ct_BuildCharDict
					begin
					/usewidths? false def
					currentfont/Widths get
						begin
						exch/CIDFont get/GlyphDirectory get
							{
							pop
							dup charcode exch 1 index 0 2 index 256 idiv put
							1 index exch 1 exch 256 mod put
							stringwidth 2 array astore def
							}
						forall
						end
					/usewidths? true def
					end
				grestore
				}
				{exch pop}
			ifelse
			}bind def
		currentglobal true setglobal
		/ct_ComposeFont
			{
			ct_UseNativeCapability?
				{				
				2 index/CMap ct_resourcestatus
					{pop pop exch pop}
					{
					/CIDInit/ProcSet findresource
						begin
						12 dict
							begin
							begincmap
							/CMapName 3 index def
							/CMapVersion 1.000 def
							/CMapType 1 def
							exch/WMode exch def
							/CIDSystemInfo 3 dict dup
								begin
								/Registry(Adobe)def
								/Ordering
								CMapName ct_mkocfStr100 cvs
								(Adobe-)search
									{
									pop pop
									(-)search
										{
										dup length string copy
										exch pop exch pop
										}
										{pop(Identity)}
									ifelse
									}
									{pop (Identity)}
								ifelse
								def
								/Supplement 0 def
								end def
							1 begincodespacerange
							<0000><FFFF>
							endcodespacerange
							1 begincidrange
							<0000><FFFF>0
							endcidrange
							endcmap
							CMapName currentdict/CMap defineresource pop
							end
						end
					}
				ifelse
				composefont
				}
				{
				3 2 roll pop
				0 get/CIDFont findresource
				ct_makeocf
				}
			ifelse
			}bind def
			setglobal
		/ct_MakeIdentity
			{
			ct_UseNativeCapability?
				{
				1 index/CMap ct_resourcestatus
					{pop pop}
					{
					/CIDInit/ProcSet findresource begin
					12 dict begin
					begincmap
					/CMapName 2 index def
					/CMapVersion 1.000 def
					/CMapType 1 def
					/CIDSystemInfo 3 dict dup
						begin
						/Registry(Adobe)def
						/Ordering
						CMapName ct_mkocfStr100 cvs
						(Adobe-)search
							{
							pop pop
							(-)search
								{dup length string copy exch pop exch pop}
								{pop(Identity)}
							ifelse
							}
							{pop(Identity)}
						ifelse
						def
						/Supplement 0 def
						end def
					1 begincodespacerange
					<0000><FFFF>
					endcodespacerange
					1 begincidrange
					<0000><FFFF>0
					endcidrange
					endcmap
					CMapName currentdict/CMap defineresource pop
					end
					end
					}
				ifelse
				composefont
				}
				{
				exch pop
				0 get/CIDFont findresource
				ct_makeocf
				}
			ifelse
			}bind def
		currentdict readonly pop
		end
	end
%%EndResource
setglobal
%%BeginResource: procset Adobe_CoolType_Utility_T42 1.0 0
%%Copyright: Copyright 1987-2004 Adobe Systems Incorporated.
%%Version: 1.0 0
userdict/ct_T42Dict 15 dict put
ct_T42Dict begin
/Is2015?
{
 version
 cvi
 2015
 ge
}bind def
/AllocGlyphStorage
{
 Is2015?
 {	
	pop
 }
 {
	{string}forall
 }ifelse
}bind def
/Type42DictBegin
{
25 dict begin
 /FontName exch def
 /CharStrings 256 dict 
begin
	 /.notdef 0 def
	 currentdict 
end def
 /Encoding exch def
 /PaintType 0 def
 /FontType 42 def
 /FontMatrix[1 0 0 1 0 0]def
 4 array astore cvx/FontBBox exch def
 /sfnts
}bind def
/Type42DictEnd 
{
 currentdict dup/FontName get exch definefont end
ct_T42Dict exch
dup/FontName get exch put
}bind def
/RD{string currentfile exch readstring pop}executeonly def
/PrepFor2015
{
Is2015?
{		 
	/GlyphDirectory 
	 16
	 dict def
	 sfnts 0 get
	 dup
	 2 index
	(glyx)
	 putinterval
	 2 index 
	(locx)
	 putinterval
	 pop
	 pop
}
{
	 pop
	 pop
}ifelse			
}bind def
/AddT42Char
{
Is2015?
{
	/GlyphDirectory get 
	begin
	def
	end
	pop
	pop
}
{
	/sfnts get
	4 index
	get
	3 index
 2 index
	putinterval
	pop
	pop
	pop
	pop
}ifelse
}bind def
/T0AddT42Mtx2
{
/CIDFont findresource/Metrics2 get begin def end
}bind def
end
%%EndResource
currentglobal true setglobal
%%BeginFile: MMFauxFont.prc
%%Copyright: Copyright 1987-2001 Adobe Systems Incorporated. 
%%All Rights Reserved.
userdict /ct_EuroDict 10 dict put
ct_EuroDict begin
/ct_CopyFont 
{
    { 1 index /FID ne {def} {pop pop} ifelse} forall
} def
/ct_GetGlyphOutline
{
   gsave
   initmatrix newpath
   exch findfont dup 
   length 1 add dict 
   begin 
		ct_CopyFont 
		/Encoding Encoding dup length array copy 
		dup
		4 -1 roll
		0 exch put   
		def
		currentdict
   end
   /ct_EuroFont exch definefont
   1000 scalefont setfont
   0 0 moveto
   [
       <00> stringwidth 
       <00> false charpath
       pathbbox
       [
       {/m cvx} {/l cvx} {/c cvx} {/cp cvx} pathforall
   grestore
   counttomark 8 add
}
def
/ct_MakeGlyphProc
{
   ] cvx
   /ct_PSBuildGlyph cvx
   ] cvx
} def
/ct_PSBuildGlyph 
{ 
 	gsave 
	8 -1 roll pop 
	7 1 roll 
        6 -2 roll ct_FontMatrix transform 6 2 roll
        4 -2 roll ct_FontMatrix transform 4 2 roll
        ct_FontMatrix transform 
	currentdict /PaintType 2 copy known {get 2 eq}{pop pop false} ifelse  
	dup  9 1 roll 
	{  
		currentdict /StrokeWidth 2 copy known  
		{   
			get 2 div   
			0 ct_FontMatrix dtransform pop
			5 1 roll  
			4 -1 roll 4 index sub   
			4 1 roll   
			3 -1 roll 4 index sub  
			3 1 roll   
			exch 4 index add exch  
			4 index add  
			5 -1 roll pop  
		}  
		{	 
			pop pop 
		}  
		ifelse  
	}       
    if  
	setcachedevice  
        ct_FontMatrix concat
        ct_PSPathOps begin 
		exec 
	end 
	{  
		currentdict /StrokeWidth 2 copy known  
			{ get }  
			{ pop pop 0 }  
  	    ifelse  
		setlinewidth stroke  
	}  
	{   
	    fill  
	}  
	ifelse  
    grestore
} def 
/ct_PSPathOps 4 dict dup begin 
	/m {moveto} def 
	/l {lineto} def 
	/c {curveto} def 
	/cp {closepath} def 
end 
def 
/ct_matrix1000 [1000 0 0 1000 0 0] def
/ct_AddGlyphProc  
{
   2 index findfont dup length 4 add dict 
   begin 
	ct_CopyFont 
	/CharStrings CharStrings dup length 1 add dict copy
      begin
         3 1 roll def  
         currentdict 
      end 
      def
      /ct_FontMatrix ct_matrix1000 FontMatrix matrix concatmatrix def
      /ct_PSBuildGlyph /ct_PSBuildGlyph load def
      /ct_PSPathOps /ct_PSPathOps load def
      currentdict
   end
   definefont pop
}
def
systemdict /languagelevel known
{
	/ct_AddGlyphToPrinterFont {
		2 copy
		ct_GetGlyphOutline 3 add -1 roll restore 
		ct_MakeGlyphProc 
		ct_AddGlyphProc
	} def
}
{
	/ct_AddGlyphToPrinterFont {
	    pop pop restore
		Adobe_CTFauxDict /$$$FONTNAME get
		/Euro
		Adobe_CTFauxDict /$$$SUBSTITUTEBASE get
		ct_EuroDict exch get
		ct_AddGlyphProc
	} def
} ifelse
/AdobeSansMM 
{ 
556 0 24 -19 541 703 
	{ 
	541 628 m 
	510 669 442 703 354 703 c 
	201 703 117 607 101 444 c 
	50 444 l 
	25 372 l 
	97 372 l 
	97 301 l 
	49 301 l 
	24 229 l 
	103 229 l 
	124 67 209 -19 350 -19 c 
	435 -19 501 25 509 32 c 
	509 131 l 
	492 105 417 60 343 60 c 
	267 60 204 127 197 229 c 
	406 229 l 
	430 301 l 
	191 301 l 
	191 372 l 
	455 372 l 
	479 444 l 
	194 444 l 
	201 531 245 624 348 624 c 
	433 624 484 583 509 534 c 
	cp 
	556 0 m 
	}
ct_PSBuildGlyph
} def
/AdobeSerifMM 
{ 
500 0 10 -12 484 692 
	{ 
	347 298 m 
	171 298 l 
	170 310 170 322 170 335 c 
	170 362 l 
	362 362 l 
	374 403 l 
	172 403 l 
	184 580 244 642 308 642 c 
	380 642 434 574 457 457 c 
	481 462 l 
	474 691 l 
	449 691 l 
	433 670 429 657 410 657 c 
	394 657 360 692 299 692 c 
	204 692 94 604 73 403 c 
	22 403 l 
	10 362 l 
	70 362 l 
	69 352 69 341 69 330 c 
	69 319 69 308 70 298 c 
	22 298 l 
	10 257 l 
	73 257 l 
	97 57 216 -12 295 -12 c 
	364 -12 427 25 484 123 c 
	458 142 l 
	425 101 384 37 316 37 c 
	256 37 189 84 173 257 c 
	335 257 l 
	cp 
	500 0 m 
	} 
ct_PSBuildGlyph 
} def 
end		
%%EndFile
setglobal
Adobe_CoolType_Core begin /$None SetSubstituteStrategy end
%%BeginResource: procset Adobe_AGM_Image 1.0 0
%%Version: 1.0 0
%%Copyright: Copyright(C)2000-2006 Adobe Systems, Inc. All Rights Reserved.
systemdict/setpacking known
{
	currentpacking
	true setpacking
}if
userdict/Adobe_AGM_Image 71 dict dup begin put
/Adobe_AGM_Image_Id/Adobe_AGM_Image_1.0_0 def
/nd{
	null def
}bind def
/AGMIMG_&image nd
/AGMIMG_&colorimage nd
/AGMIMG_&imagemask nd
/AGMIMG_mbuf()def
/AGMIMG_ybuf()def
/AGMIMG_kbuf()def
/AGMIMG_c 0 def
/AGMIMG_m 0 def
/AGMIMG_y 0 def
/AGMIMG_k 0 def
/AGMIMG_tmp nd
/AGMIMG_imagestring0 nd
/AGMIMG_imagestring1 nd
/AGMIMG_imagestring2 nd
/AGMIMG_imagestring3 nd
/AGMIMG_imagestring4 nd
/AGMIMG_imagestring5 nd
/AGMIMG_cnt nd
/AGMIMG_fsave nd
/AGMIMG_colorAry nd
/AGMIMG_override nd
/AGMIMG_name nd
/AGMIMG_maskSource nd
/AGMIMG_flushfilters nd
/invert_image_samples nd
/knockout_image_samples	nd
/img nd
/sepimg nd
/devnimg nd
/idximg nd
/ds
{
	Adobe_AGM_Core begin
	Adobe_AGM_Image begin
	/AGMIMG_&image systemdict/image get def
	/AGMIMG_&imagemask systemdict/imagemask get def
	/colorimage where{
		pop
		/AGMIMG_&colorimage/colorimage ldf
	}if
	end
	end
}def
/ps
{
	Adobe_AGM_Image begin
	/AGMIMG_ccimage_exists{/customcolorimage where 
		{
			pop
			/Adobe_AGM_OnHost_Seps where
			{
			pop false
			}{
			/Adobe_AGM_InRip_Seps where
				{
				pop false
				}{
					true
				}ifelse
			}ifelse
			}{
			false
		}ifelse 
	}bdf
	level2{
		/invert_image_samples
		{
			Adobe_AGM_Image/AGMIMG_tmp Decode length ddf
			/Decode[Decode 1 get Decode 0 get]def
		}def
		/knockout_image_samples
		{
			Operator/imagemask ne{
				/Decode[1 1]def
			}if
		}def
	}{	
		/invert_image_samples
		{
			{1 exch sub}currenttransfer addprocs settransfer
		}def
		/knockout_image_samples
		{
			{pop 1}currenttransfer addprocs settransfer
		}def
	}ifelse
	/img/imageormask ldf
	/sepimg/sep_imageormask ldf
	/devnimg/devn_imageormask ldf
	/idximg/indexed_imageormask ldf
	/_ctype 7 def
	currentdict{
		dup xcheck 1 index type dup/arraytype eq exch/packedarraytype eq or and{
			bind
		}if
		def
	}forall
}def
/pt
{
	end
}def
/dt
{
}def
/AGMIMG_flushfilters
{
	dup type/arraytype ne
		{1 array astore}if
	dup 0 get currentfile ne
		{dup 0 get flushfile}if
		{
		dup type/filetype eq
			{
			dup status 1 index currentfile ne and
				{closefile}
				{pop}
			ifelse
			}{pop}ifelse
		}forall
}def
/AGMIMG_init_common
{
	currentdict/T known{/ImageType/T ldf currentdict/T undef}if
	currentdict/W known{/Width/W ldf currentdict/W undef}if
	currentdict/H known{/Height/H ldf currentdict/H undef}if
	currentdict/M known{/ImageMatrix/M ldf currentdict/M undef}if
	currentdict/BC known{/BitsPerComponent/BC ldf currentdict/BC undef}if
	currentdict/D known{/Decode/D ldf currentdict/D undef}if
	currentdict/DS known{/DataSource/DS ldf currentdict/DS undef}if
	currentdict/O known{
		/Operator/O load 1 eq{
			/imagemask
		}{
			/O load 2 eq{
				/image 
			}{
				/colorimage
			}ifelse
		}ifelse
		def
		currentdict/O undef
	}if
	currentdict/HSCI known{/HostSepColorImage/HSCI ldf currentdict/HSCI undef}if
	currentdict/MD known{/MultipleDataSources/MD ldf currentdict/MD undef}if
	currentdict/I known{/Interpolate/I ldf currentdict/I undef}if
	currentdict/SI known{/SkipImageProc/SI ldf currentdict/SI undef}if
	/DataSource load xcheck not{
		DataSource type/arraytype eq{
			DataSource 0 get type/filetype eq{
				/_Filters DataSource def
				currentdict/MultipleDataSources known not{
					/DataSource DataSource dup length 1 sub get def 
				}if
			}if
		}if
		currentdict/MultipleDataSources known not{
			/MultipleDataSources DataSource type/arraytype eq{
				DataSource length 1 gt
			}
			{false}ifelse def
		}if
	}if
	/NComponents Decode length 2 div def
	currentdict/SkipImageProc known not{/SkipImageProc{false}def}if
}bdf
/imageormask_sys
{
	begin
		AGMIMG_init_common
		save mark
		level2{
			currentdict
			Operator/imagemask eq{
				AGMIMG_&imagemask
			}{
				use_mask{
					process_mask AGMIMG_&image
				}{
					AGMIMG_&image
				}ifelse
			}ifelse
		}{
			Width Height
			Operator/imagemask eq{
				Decode 0 get 1 eq Decode 1 get 0 eq	and
				ImageMatrix/DataSource load
				AGMIMG_&imagemask
			}{
				BitsPerComponent ImageMatrix/DataSource load
				AGMIMG_&image
			}ifelse
		}ifelse
		currentdict/_Filters known{_Filters AGMIMG_flushfilters}if
		cleartomark restore
	end
}def
/overprint_plate
{
	currentoverprint{
		0 get dup type/nametype eq{
			dup/DeviceGray eq{
				pop AGMCORE_black_plate not
			}{
				/DeviceCMYK eq{
					AGMCORE_is_cmyk_sep not
				}if
			}ifelse
		}{
			false exch
			{
				 AGMOHS_sepink eq or
			}forall
			not
		}ifelse
	}{
		pop false
	}ifelse
}def
/process_mask
{
	level3{
		dup begin
		/ImageType 1 def
		end
		4 dict begin
			/DataDict exch def
			/ImageType 3 def
			/InterleaveType 3 def
			/MaskDict 9 dict begin
				/ImageType 1 def
				/Width DataDict dup/MaskWidth known{/MaskWidth}{/Width}ifelse get def
				/Height DataDict dup/MaskHeight known{/MaskHeight}{/Height}ifelse get def
				/ImageMatrix[Width 0 0 Height neg 0 Height]def
				/NComponents 1 def
				/BitsPerComponent 1 def
				/Decode DataDict dup/MaskD known{/MaskD}{[1 0]}ifelse get def
				/DataSource Adobe_AGM_Core/AGMIMG_maskSource get def
			currentdict end def
		currentdict end
	}if
}def
/use_mask
{
	dup/Mask known	{dup/Mask get}{false}ifelse
}def
/imageormask
{
	begin
		AGMIMG_init_common
		SkipImageProc{
			currentdict consumeimagedata
		}
		{
			save mark
			level2 AGMCORE_host_sep not and{
				currentdict
				Operator/imagemask eq DeviceN_PS2 not and{
					imagemask
				}{
					AGMCORE_in_rip_sep currentoverprint and currentcolorspace 0 get/DeviceGray eq and{
						[/Separation/Black/DeviceGray{}]setcolorspace
						/Decode[Decode 1 get Decode 0 get]def
					}if
					use_mask{
						process_mask image
					}{
						DeviceN_NoneName DeviceN_PS2 Indexed_DeviceN level3 not and or or AGMCORE_in_rip_sep and 
						{
							Names convert_to_process not{
								2 dict begin
								/imageDict xdf
								/names_index 0 def
								gsave
								imageDict write_image_file{
									Names{
										dup(None)ne{
											[/Separation 3 -1 roll/DeviceGray{1 exch sub}]setcolorspace
											Operator imageDict read_image_file
											names_index 0 eq{true setoverprint}if
											/names_index names_index 1 add def
										}{
											pop
										}ifelse
									}forall
									close_image_file
								}if
								grestore
								end
							}{
								Operator/imagemask eq{
									imagemask
								}{
									image
								}ifelse
							}ifelse
						}{
							Operator/imagemask eq{
								imagemask
							}{
								image
							}ifelse
						}ifelse
					}ifelse
				}ifelse
			}{
				Width Height
				Operator/imagemask eq{
					Decode 0 get 1 eq Decode 1 get 0 eq	and
					ImageMatrix/DataSource load
					/Adobe_AGM_OnHost_Seps where{
						pop imagemask
					}{
						currentgray 1 ne{
							currentdict imageormask_sys
						}{
							currentoverprint not{
								1 AGMCORE_&setgray
								currentdict imageormask_sys
							}{
								currentdict ignoreimagedata
							}ifelse				 		
						}ifelse
					}ifelse
				}{
					BitsPerComponent ImageMatrix 
					MultipleDataSources{
						0 1 NComponents 1 sub{
							DataSource exch get
						}for
					}{
						/DataSource load
					}ifelse
					Operator/colorimage eq{
						AGMCORE_host_sep{
							MultipleDataSources level2 or NComponents 4 eq and{
								AGMCORE_is_cmyk_sep{
									MultipleDataSources{
										/DataSource DataSource 0 get xcheck
											{
											[
											DataSource 0 get/exec cvx
											DataSource 1 get/exec cvx
											DataSource 2 get/exec cvx
											DataSource 3 get/exec cvx
											/AGMCORE_get_ink_data cvx
											]cvx
											}{
											DataSource aload pop AGMCORE_get_ink_data
											}ifelse def
									}{
										/DataSource 
										Width BitsPerComponent mul 7 add 8 idiv Height mul 4 mul 
										/DataSource load
										filter_cmyk 0()/SubFileDecode filter def
									}ifelse
									/Decode[Decode 0 get Decode 1 get]def
									/MultipleDataSources false def
									/NComponents 1 def
									/Operator/image def
									invert_image_samples
						 			1 AGMCORE_&setgray
									currentdict imageormask_sys
								}{
									currentoverprint not Operator/imagemask eq and{
 			 							1 AGMCORE_&setgray
 			 							currentdict imageormask_sys
 			 						}{
 			 							currentdict ignoreimagedata
 			 						}ifelse
								}ifelse
							}{	
								MultipleDataSources NComponents AGMIMG_&colorimage						
							}ifelse
						}{
							true NComponents colorimage
						}ifelse
					}{
						Operator/image eq{
							AGMCORE_host_sep{
								/DoImage true def
								currentdict/HostSepColorImage known{HostSepColorImage not}{false}ifelse
								{
									AGMCORE_black_plate not Operator/imagemask ne and{
										/DoImage false def
										currentdict ignoreimagedata
					 				}if
								}if
						 		1 AGMCORE_&setgray
								DoImage
									{currentdict imageormask_sys}if
							}{
								use_mask{
									process_mask image
								}{
									image
								}ifelse
							}ifelse
						}{
							Operator/knockout eq{
								pop pop pop pop pop
								currentcolorspace overprint_plate not{
									knockout_unitsq
								}if
							}if
						}ifelse
					}ifelse
				}ifelse
			}ifelse
			cleartomark restore
		}ifelse
		currentdict/_Filters known{_Filters AGMIMG_flushfilters}if
	end
}def
/sep_imageormask
{
 	/sep_colorspace_dict AGMCORE_gget begin
	CSA map_csa
	begin
	AGMIMG_init_common
	SkipImageProc{
		currentdict consumeimagedata
	}{
		save mark 
		AGMCORE_avoid_L2_sep_space{
			/Decode[Decode 0 get 255 mul Decode 1 get 255 mul]def
		}if
 		AGMIMG_ccimage_exists 
		MappedCSA 0 get/DeviceCMYK eq and
		currentdict/Components known and 
		Name()ne and 
		Name(All)ne and 
		Operator/image eq and
		AGMCORE_producing_seps not and
		level2 not and
		{
			Width Height BitsPerComponent ImageMatrix 
			[
			/DataSource load/exec cvx
			{
				0 1 2 index length 1 sub{
					1 index exch
					2 copy get 255 xor put
				}for
			}/exec cvx
			]cvx bind
			MappedCSA 0 get/DeviceCMYK eq{
				Components aload pop
			}{
				0 0 0 Components aload pop 1 exch sub
			}ifelse
			Name findcmykcustomcolor
			customcolorimage
		}{
			AGMCORE_producing_seps not{
				level2{
 					//Adobe_AGM_Core/AGMCORE_pattern_paint_type get 2 ne AGMCORE_avoid_L2_sep_space not and currentcolorspace 0 get/Separation ne and{
						[/Separation Name MappedCSA sep_proc_name exch dup 0 get 15 string cvs(/Device)anchorsearch{pop pop 0 get}{pop}ifelse exch load]setcolorspace_opt
						/sep_tint AGMCORE_gget setcolor
					}if
					currentdict imageormask
				}{
					currentdict
					Operator/imagemask eq{
						imageormask
					}{
						sep_imageormask_lev1
					}ifelse
				}ifelse
 			}{
				AGMCORE_host_sep{
					Operator/knockout eq{
						currentdict/ImageMatrix get concat
						knockout_unitsq
					}{
						currentgray 1 ne{
 							AGMCORE_is_cmyk_sep Name(All)ne and{
 								level2{
 									Name AGMCORE_IsSeparationAProcessColor 
 									{
 										Operator/imagemask eq{
 											//Adobe_AGM_Core/AGMCORE_pattern_paint_type get 2 ne{
 												/sep_tint AGMCORE_gget 1 exch sub AGMCORE_&setcolor
 											}if
 										}{
											invert_image_samples
 										}ifelse
	 								}{
	 									//Adobe_AGM_Core/AGMCORE_pattern_paint_type get 2 ne{
	 										[/Separation Name[/DeviceGray]
	 										{
	 											sep_colorspace_proc AGMCORE_get_ink_data
												1 exch sub
	 										}bind
											]AGMCORE_&setcolorspace
											/sep_tint AGMCORE_gget AGMCORE_&setcolor
										}if
 									}ifelse
 									currentdict imageormask_sys
	 							}{
	 								currentdict
									Operator/imagemask eq{
										imageormask_sys
									}{
										sep_image_lev1_sep
									}ifelse
	 							}ifelse
 							}{
 								Operator/imagemask ne{
									invert_image_samples
 								}if
		 						currentdict imageormask_sys
 							}ifelse
 						}{
 							currentoverprint not Name(All)eq or Operator/imagemask eq and{
								currentdict imageormask_sys 
								}{
								currentoverprint not
									{
 									gsave 
 									knockout_unitsq
 									grestore
									}if
								currentdict consumeimagedata 
		 					}ifelse
 						}ifelse
		 			}ifelse
 				}{
					//Adobe_AGM_Core/AGMCORE_pattern_paint_type get 2 ne{
						currentcolorspace 0 get/Separation ne{
							[/Separation Name MappedCSA sep_proc_name exch 0 get exch load]setcolorspace_opt
							/sep_tint AGMCORE_gget setcolor
						}if
					}if
					currentoverprint 
					MappedCSA 0 get/DeviceCMYK eq and 
					Name AGMCORE_IsSeparationAProcessColor not and
					//Adobe_AGM_Core/AGMCORE_pattern_paint_type get 2 ne{Name inRip_spot_has_ink not and}{false}ifelse 
					Name(All)ne and{
						imageormask_l2_overprint
					}{
						currentdict imageormask
 					}ifelse
				}ifelse
			}ifelse
		}ifelse
		cleartomark restore
	}ifelse
	currentdict/_Filters known{_Filters AGMIMG_flushfilters}if
	end
	end
}def
/colorSpaceElemCnt
{
	mark currentcolor counttomark dup 2 add 1 roll cleartomark
}bdf
/devn_sep_datasource
{
	1 dict begin
	/dataSource xdf
	[
		0 1 dataSource length 1 sub{
			dup currentdict/dataSource get/exch cvx/get cvx/exec cvx
			/exch cvx names_index/ne cvx[/pop cvx]cvx/if cvx
		}for
	]cvx bind
	end
}bdf		
/devn_alt_datasource
{
	11 dict begin
	/convProc xdf
	/origcolorSpaceElemCnt xdf
	/origMultipleDataSources xdf
	/origBitsPerComponent xdf
	/origDecode xdf
	/origDataSource xdf
	/dsCnt origMultipleDataSources{origDataSource length}{1}ifelse def
	/DataSource origMultipleDataSources
		{
			[
			BitsPerComponent 8 idiv origDecode length 2 idiv mul string
			0 1 origDecode length 2 idiv 1 sub
				{
				dup 7 mul 1 add index exch dup BitsPerComponent 8 idiv mul exch
				origDataSource exch get 0()/SubFileDecode filter
				BitsPerComponent 8 idiv string/readstring cvx/pop cvx/putinterval cvx
				}for 
			]bind cvx
		}{origDataSource}ifelse 0()/SubFileDecode filter def		
	[
		origcolorSpaceElemCnt string
		0 2 origDecode length 2 sub
			{
			dup origDecode exch get dup 3 -1 roll 1 add origDecode exch get exch sub 2 BitsPerComponent exp 1 sub div
			1 BitsPerComponent 8 idiv{DataSource/read cvx/not cvx{0}/if cvx/mul cvx}repeat/mul cvx/add cvx
			}for
		/convProc load/exec cvx
		origcolorSpaceElemCnt 1 sub -1 0
			{
			/dup cvx 2/add cvx/index cvx
			3 1/roll cvx/exch cvx 255/mul cvx/cvi cvx/put cvx
			}for
	]bind cvx 0()/SubFileDecode filter
	end
}bdf
/devn_imageormask
{
 	/devicen_colorspace_dict AGMCORE_gget begin
	CSA map_csa
	2 dict begin
	dup
	/srcDataStrs[3 -1 roll begin
		AGMIMG_init_common
		currentdict/MultipleDataSources known{MultipleDataSources{DataSource length}{1}ifelse}{1}ifelse
		{
			Width Decode length 2 div mul cvi
			{
				dup 65535 gt{1 add 2 div cvi}{exit}ifelse
			}loop
			string
		}repeat
		end]def
	/dstDataStr srcDataStrs 0 get length string def
	begin
	AGMIMG_init_common
	SkipImageProc{
		currentdict consumeimagedata
	}{
		save mark 
		AGMCORE_producing_seps not{
			level3 not{
				Operator/imagemask ne{
					/DataSource[[
						DataSource Decode BitsPerComponent currentdict/MultipleDataSources known{MultipleDataSources}{false}ifelse
						colorSpaceElemCnt/devicen_colorspace_dict AGMCORE_gget/TintTransform get 
						devn_alt_datasource 1/string cvx/readstring cvx/pop cvx]cvx colorSpaceElemCnt 1 sub{dup}repeat]def				
					/MultipleDataSources true def
					/Decode colorSpaceElemCnt[exch{0 1}repeat]def
				}if
			}if
			currentdict imageormask
 		}{
			AGMCORE_host_sep{
				Names convert_to_process{
					CSA get_csa_by_name 0 get/DeviceCMYK eq{
						/DataSource
							Width BitsPerComponent mul 7 add 8 idiv Height mul 4 mul 
							DataSource Decode BitsPerComponent currentdict/MultipleDataSources known{MultipleDataSources}{false}ifelse
							4/devicen_colorspace_dict AGMCORE_gget/TintTransform get 
							devn_alt_datasource
						filter_cmyk 0()/SubFileDecode filter def
						/MultipleDataSources false def
						/Decode[1 0]def
						/DeviceGray setcolorspace
			 			currentdict imageormask_sys
 					}{
						AGMCORE_report_unsupported_color_space
						AGMCORE_black_plate{
							/DataSource
								DataSource Decode BitsPerComponent currentdict/MultipleDataSources known{MultipleDataSources}{false}ifelse
								CSA get_csa_by_name 0 get/DeviceRGB eq{3}{1}ifelse/devicen_colorspace_dict AGMCORE_gget/TintTransform get
								devn_alt_datasource
							/MultipleDataSources false def
							/Decode colorSpaceElemCnt[exch{0 1}repeat]def
				 			currentdict imageormask_sys
				 		}{
	 						gsave 
	 						knockout_unitsq
	 						grestore
							currentdict consumeimagedata 
						}ifelse
 					}ifelse
				}
				{	
					/devicen_colorspace_dict AGMCORE_gget/names_index known{
	 					Operator/imagemask ne{
	 						MultipleDataSources{
		 						/DataSource[DataSource devn_sep_datasource/exec cvx]cvx def
								/MultipleDataSources false def
	 						}{
								/DataSource/DataSource load dstDataStr srcDataStrs 0 get filter_devn def
	 						}ifelse
							invert_image_samples
	 					}if
			 			currentdict imageormask_sys
	 				}{
	 					currentoverprint not Operator/imagemask eq and{
							currentdict imageormask_sys 
							}{
							currentoverprint not
								{
	 							gsave 
	 							knockout_unitsq
	 							grestore
								}if
							currentdict consumeimagedata 
			 			}ifelse
	 				}ifelse
	 			}ifelse
 			}{
				currentdict imageormask
			}ifelse
		}ifelse
		cleartomark restore
	}ifelse
	currentdict/_Filters known{_Filters AGMIMG_flushfilters}if
	end
	end
	end
}def
/imageormask_l2_overprint
{
	currentdict
	currentcmykcolor add add add 0 eq{
		currentdict consumeimagedata
	}{
		level3{			
			currentcmykcolor 
			/AGMIMG_k xdf 
			/AGMIMG_y xdf 
			/AGMIMG_m xdf 
			/AGMIMG_c xdf
			Operator/imagemask eq{
				[/DeviceN[
				AGMIMG_c 0 ne{/Cyan}if
				AGMIMG_m 0 ne{/Magenta}if
				AGMIMG_y 0 ne{/Yellow}if
				AGMIMG_k 0 ne{/Black}if
				]/DeviceCMYK{}]setcolorspace
				AGMIMG_c 0 ne{AGMIMG_c}if
				AGMIMG_m 0 ne{AGMIMG_m}if
				AGMIMG_y 0 ne{AGMIMG_y}if
				AGMIMG_k 0 ne{AGMIMG_k}if
				setcolor			
			}{	
				/Decode[Decode 0 get 255 mul Decode 1 get 255 mul]def
				[/Indexed 				
					[
						/DeviceN[
							AGMIMG_c 0 ne{/Cyan}if
							AGMIMG_m 0 ne{/Magenta}if
							AGMIMG_y 0 ne{/Yellow}if
							AGMIMG_k 0 ne{/Black}if
						]
						/DeviceCMYK{
							AGMIMG_k 0 eq{0}if
							AGMIMG_y 0 eq{0 exch}if
							AGMIMG_m 0 eq{0 3 1 roll}if
							AGMIMG_c 0 eq{0 4 1 roll}if						
						}
					]
					255
					{
						255 div 
						mark exch
						dup	dup dup
						AGMIMG_k 0 ne{
							/sep_tint AGMCORE_gget mul MappedCSA sep_proc_name exch pop load exec 4 1 roll pop pop pop		
							counttomark 1 roll
						}{
							pop
						}ifelse
						AGMIMG_y 0 ne{
							/sep_tint AGMCORE_gget mul MappedCSA sep_proc_name exch pop load exec 4 2 roll pop pop pop		
							counttomark 1 roll
						}{
							pop
						}ifelse
						AGMIMG_m 0 ne{
							/sep_tint AGMCORE_gget mul MappedCSA sep_proc_name exch pop load exec 4 3 roll pop pop pop		
							counttomark 1 roll
						}{
							pop
						}ifelse
						AGMIMG_c 0 ne{
							/sep_tint AGMCORE_gget mul MappedCSA sep_proc_name exch pop load exec pop pop pop		
							counttomark 1 roll
						}{
							pop
						}ifelse
						counttomark 1 add -1 roll pop
					}
				]setcolorspace
			}ifelse
			imageormask_sys
		}{
	write_image_file{
		currentcmykcolor
		0 ne{
			[/Separation/Black/DeviceGray{}]setcolorspace
			gsave
			/Black
			[{1 exch sub/sep_tint AGMCORE_gget mul}/exec cvx MappedCSA sep_proc_name cvx exch pop{4 1 roll pop pop pop 1 exch sub}/exec cvx]
			cvx modify_halftone_xfer
			Operator currentdict read_image_file
			grestore
		}if
		0 ne{
			[/Separation/Yellow/DeviceGray{}]setcolorspace
			gsave
			/Yellow
			[{1 exch sub/sep_tint AGMCORE_gget mul}/exec cvx MappedCSA sep_proc_name cvx exch pop{4 2 roll pop pop pop 1 exch sub}/exec cvx]
			cvx modify_halftone_xfer
			Operator currentdict read_image_file
			grestore
		}if
		0 ne{
			[/Separation/Magenta/DeviceGray{}]setcolorspace
			gsave
			/Magenta
			[{1 exch sub/sep_tint AGMCORE_gget mul}/exec cvx MappedCSA sep_proc_name cvx exch pop{4 3 roll pop pop pop 1 exch sub}/exec cvx]
			cvx modify_halftone_xfer
			Operator currentdict read_image_file
			grestore
		}if
		0 ne{
			[/Separation/Cyan/DeviceGray{}]setcolorspace
			gsave
			/Cyan 
			[{1 exch sub/sep_tint AGMCORE_gget mul}/exec cvx MappedCSA sep_proc_name cvx exch pop{pop pop pop 1 exch sub}/exec cvx]
			cvx modify_halftone_xfer
			Operator currentdict read_image_file
			grestore
		}if
				close_image_file
			}{
				imageormask
			}ifelse
		}ifelse
	}ifelse
}def
/indexed_imageormask
{
	begin
		AGMIMG_init_common
		save mark 
 		currentdict
 		AGMCORE_host_sep{
			Operator/knockout eq{
				/indexed_colorspace_dict AGMCORE_gget dup/CSA known{
					/CSA get get_csa_by_name
				}{
					/Names get
				}ifelse
				overprint_plate not{
					knockout_unitsq
				}if
			}{
				Indexed_DeviceN{
					/devicen_colorspace_dict AGMCORE_gget dup/names_index known exch/Names get convert_to_process or{
			 			indexed_image_lev2_sep
					}{
						currentoverprint not{
							knockout_unitsq
			 			}if
			 			currentdict consumeimagedata
					}ifelse
				}{
		 			AGMCORE_is_cmyk_sep{
						Operator/imagemask eq{
							imageormask_sys
						}{
							level2{
								indexed_image_lev2_sep
							}{
								indexed_image_lev1_sep
							}ifelse
						}ifelse
					}{
						currentoverprint not{
							knockout_unitsq
			 			}if
			 			currentdict consumeimagedata
					}ifelse
				}ifelse
			}ifelse
 		}{
			level2{
				Indexed_DeviceN{
					/indexed_colorspace_dict AGMCORE_gget begin
				}{
					/indexed_colorspace_dict AGMCORE_gget dup null ne
					{
						begin
						currentdict/CSDBase known{CSDBase/CSD get_res/MappedCSA get}{CSA}ifelse
						get_csa_by_name 0 get/DeviceCMYK eq ps_level 3 ge and ps_version 3015.007 lt and
						AGMCORE_in_rip_sep and{
							[/Indexed[/DeviceN[/Cyan/Magenta/Yellow/Black]/DeviceCMYK{}]HiVal Lookup]
							setcolorspace
						}if
						end
					}
					{pop}ifelse
				}ifelse
				imageormask
				Indexed_DeviceN{
					end
				}if
			}{
				Operator/imagemask eq{
					imageormask
				}{
					indexed_imageormask_lev1
				}ifelse
			}ifelse
 		}ifelse
		cleartomark restore
	currentdict/_Filters known{_Filters AGMIMG_flushfilters}if
	end
}def
/indexed_image_lev2_sep
{
	/indexed_colorspace_dict AGMCORE_gget begin
	begin
		Indexed_DeviceN not{
			currentcolorspace 
			dup 1/DeviceGray put
			dup 3
			currentcolorspace 2 get 1 add string
			0 1 2 3 AGMCORE_get_ink_data 4 currentcolorspace 3 get length 1 sub
			{
			dup 4 idiv exch currentcolorspace 3 get exch get 255 exch sub 2 index 3 1 roll put
			}for 
			put	setcolorspace
		}if
		currentdict 
		Operator/imagemask eq{
			AGMIMG_&imagemask
		}{
			use_mask{
				process_mask AGMIMG_&image
			}{
				AGMIMG_&image
			}ifelse
		}ifelse
	end end
}def
 /OPIimage
 {
 	dup type/dicttype ne{
 		10 dict begin
 			/DataSource xdf
 			/ImageMatrix xdf
 			/BitsPerComponent xdf
 			/Height xdf
 			/Width xdf
 			/ImageType 1 def
 			/Decode[0 1 def]
 			currentdict
 		end
 	}if
 	dup begin
 		/NComponents 1 cdndf
 		/MultipleDataSources false cdndf
 		/SkipImageProc{false}cdndf
 		/Decode[
 				0 
 				currentcolorspace 0 get/Indexed eq{
 					2 BitsPerComponent exp 1 sub
 				}{
 					1
 				}ifelse
 		]cdndf
 		/Operator/image cdndf
 	end
 	/sep_colorspace_dict AGMCORE_gget null eq{
 		imageormask
 	}{
 		gsave
 		dup begin invert_image_samples end
 		sep_imageormask
 		grestore
 	}ifelse
 }def
/cachemask_level2
{
	3 dict begin
	/LZWEncode filter/WriteFilter xdf
	/readBuffer 256 string def
	/ReadFilter
		currentfile
		0(%EndMask)/SubFileDecode filter
		/ASCII85Decode filter
		/RunLengthDecode filter
	def
	{
		ReadFilter readBuffer readstring exch
		WriteFilter exch writestring
		not{exit}if
	}loop
	WriteFilter closefile
	end
}def
/spot_alias
{
	/mapto_sep_imageormask 
	{
		dup type/dicttype ne{
			12 dict begin
				/ImageType 1 def
				/DataSource xdf
				/ImageMatrix xdf
				/BitsPerComponent xdf
				/Height xdf
				/Width xdf
				/MultipleDataSources false def
		}{
			begin
		}ifelse
				/Decode[/customcolor_tint AGMCORE_gget 0]def
				/Operator/image def
				/SkipImageProc{false}def
				currentdict 
			end
		sep_imageormask
	}bdf
	/customcolorimage
	{
		Adobe_AGM_Image/AGMIMG_colorAry xddf
		/customcolor_tint AGMCORE_gget
		<<
			/Name AGMIMG_colorAry 4 get
			/CSA[/DeviceCMYK]
			/TintMethod/Subtractive
			/TintProc null
			/MappedCSA null
			/NComponents 4 
			/Components[AGMIMG_colorAry aload pop pop]
		>>
		setsepcolorspace
		mapto_sep_imageormask
	}ndf
	Adobe_AGM_Image/AGMIMG_&customcolorimage/customcolorimage load put
	/customcolorimage
	{
		Adobe_AGM_Image/AGMIMG_override false put
		current_spot_alias{dup 4 get map_alias}{false}ifelse
		{
			false set_spot_alias
			/customcolor_tint AGMCORE_gget exch setsepcolorspace
			pop
			mapto_sep_imageormask
			true set_spot_alias
		}{
			//Adobe_AGM_Image/AGMIMG_&customcolorimage get exec
		}ifelse			
	}bdf
}def
/snap_to_device
{
	6 dict begin
	matrix currentmatrix
	dup 0 get 0 eq 1 index 3 get 0 eq and
	1 index 1 get 0 eq 2 index 2 get 0 eq and or exch pop
	{
		1 1 dtransform 0 gt exch 0 gt/AGMIMG_xSign? exch def/AGMIMG_ySign? exch def
		0 0 transform
		AGMIMG_ySign?{floor 0.1 sub}{ceiling 0.1 add}ifelse exch
		AGMIMG_xSign?{floor 0.1 sub}{ceiling 0.1 add}ifelse exch
		itransform/AGMIMG_llY exch def/AGMIMG_llX exch def
		1 1 transform
		AGMIMG_ySign?{ceiling 0.1 add}{floor 0.1 sub}ifelse exch
		AGMIMG_xSign?{ceiling 0.1 add}{floor 0.1 sub}ifelse exch
		itransform/AGMIMG_urY exch def/AGMIMG_urX exch def			
		[AGMIMG_urX AGMIMG_llX sub 0 0 AGMIMG_urY AGMIMG_llY sub AGMIMG_llX AGMIMG_llY]concat
	}{
	}ifelse
	end
}def
level2 not{
	/colorbuf
	{
		0 1 2 index length 1 sub{
			dup 2 index exch get 
			255 exch sub 
			2 index 
			3 1 roll 
			put
		}for
	}def
	/tint_image_to_color
	{
		begin
			Width Height BitsPerComponent ImageMatrix 
			/DataSource load
		end
		Adobe_AGM_Image begin
			/AGMIMG_mbuf 0 string def
			/AGMIMG_ybuf 0 string def
			/AGMIMG_kbuf 0 string def
			{
				colorbuf dup length AGMIMG_mbuf length ne
					{
					dup length dup dup
					/AGMIMG_mbuf exch string def
					/AGMIMG_ybuf exch string def
					/AGMIMG_kbuf exch string def
					}if
				dup AGMIMG_mbuf copy AGMIMG_ybuf copy AGMIMG_kbuf copy pop
			}
			addprocs
			{AGMIMG_mbuf}{AGMIMG_ybuf}{AGMIMG_kbuf}true 4 colorimage	
		end
	}def			
	/sep_imageormask_lev1
	{
		begin
			MappedCSA 0 get dup/DeviceRGB eq exch/DeviceCMYK eq or has_color not and{
				{
					255 mul round cvi GrayLookup exch get
				}currenttransfer addprocs settransfer
				currentdict imageormask
			}{
				/sep_colorspace_dict AGMCORE_gget/Components known{
					MappedCSA 0 get/DeviceCMYK eq{
						Components aload pop
					}{
						0 0 0 Components aload pop 1 exch sub
					}ifelse
					Adobe_AGM_Image/AGMIMG_k xddf 
					Adobe_AGM_Image/AGMIMG_y xddf 
					Adobe_AGM_Image/AGMIMG_m xddf 
					Adobe_AGM_Image/AGMIMG_c xddf 
					AGMIMG_y 0.0 eq AGMIMG_m 0.0 eq and AGMIMG_c 0.0 eq and{
						{AGMIMG_k mul 1 exch sub}currenttransfer addprocs settransfer
						currentdict imageormask
					}{
						currentcolortransfer
						{AGMIMG_k mul 1 exch sub}exch addprocs 4 1 roll
						{AGMIMG_y mul 1 exch sub}exch addprocs 4 1 roll
						{AGMIMG_m mul 1 exch sub}exch addprocs 4 1 roll
						{AGMIMG_c mul 1 exch sub}exch addprocs 4 1 roll
						setcolortransfer
						currentdict tint_image_to_color
					}ifelse
				}{
					MappedCSA 0 get/DeviceGray eq{
						{255 mul round cvi ColorLookup exch get 0 get}currenttransfer addprocs settransfer
						currentdict imageormask
					}{
						MappedCSA 0 get/DeviceCMYK eq{
							currentcolortransfer
							{255 mul round cvi ColorLookup exch get 3 get 1 exch sub}exch addprocs 4 1 roll
							{255 mul round cvi ColorLookup exch get 2 get 1 exch sub}exch addprocs 4 1 roll
							{255 mul round cvi ColorLookup exch get 1 get 1 exch sub}exch addprocs 4 1 roll
							{255 mul round cvi ColorLookup exch get 0 get 1 exch sub}exch addprocs 4 1 roll
							setcolortransfer 
							currentdict tint_image_to_color
						}{
							currentcolortransfer
							{pop 1}exch addprocs 4 1 roll
							{255 mul round cvi ColorLookup exch get 2 get}exch addprocs 4 1 roll
							{255 mul round cvi ColorLookup exch get 1 get}exch addprocs 4 1 roll
							{255 mul round cvi ColorLookup exch get 0 get}exch addprocs 4 1 roll
							setcolortransfer 
							currentdict tint_image_to_color
						}ifelse
					}ifelse
				}ifelse
			}ifelse
		end
	}def
	/sep_image_lev1_sep
	{
		begin
			/sep_colorspace_dict AGMCORE_gget/Components known{
				Components aload pop
				Adobe_AGM_Image/AGMIMG_k xddf 
				Adobe_AGM_Image/AGMIMG_y xddf 
				Adobe_AGM_Image/AGMIMG_m xddf 
				Adobe_AGM_Image/AGMIMG_c xddf 
				{AGMIMG_c mul 1 exch sub}
				{AGMIMG_m mul 1 exch sub}
				{AGMIMG_y mul 1 exch sub}
				{AGMIMG_k mul 1 exch sub}
			}{
				{255 mul round cvi ColorLookup exch get 0 get 1 exch sub}
				{255 mul round cvi ColorLookup exch get 1 get 1 exch sub}
				{255 mul round cvi ColorLookup exch get 2 get 1 exch sub}
				{255 mul round cvi ColorLookup exch get 3 get 1 exch sub}
			}ifelse
			AGMCORE_get_ink_data currenttransfer addprocs settransfer
			currentdict imageormask_sys
		end
	}def
	/indexed_imageormask_lev1
	{
		/indexed_colorspace_dict AGMCORE_gget begin
		begin
			currentdict
			MappedCSA 0 get dup/DeviceRGB eq exch/DeviceCMYK eq or has_color not and{
				{HiVal mul round cvi GrayLookup exch get HiVal div}currenttransfer addprocs settransfer
				imageormask
			}{
				MappedCSA 0 get/DeviceGray eq{
					{HiVal mul round cvi Lookup exch get HiVal div}currenttransfer addprocs settransfer
					imageormask
				}{
					MappedCSA 0 get/DeviceCMYK eq{
						currentcolortransfer
						{4 mul HiVal mul round cvi 3 add Lookup exch get HiVal div 1 exch sub}exch addprocs 4 1 roll
						{4 mul HiVal mul round cvi 2 add Lookup exch get HiVal div 1 exch sub}exch addprocs 4 1 roll
						{4 mul HiVal mul round cvi 1 add Lookup exch get HiVal div 1 exch sub}exch addprocs 4 1 roll
						{4 mul HiVal mul round cvi		 Lookup exch get HiVal div 1 exch sub}exch addprocs 4 1 roll
						setcolortransfer 
						tint_image_to_color
					}{
						currentcolortransfer
						{pop 1}exch addprocs 4 1 roll
						{3 mul HiVal mul round cvi 2 add Lookup exch get HiVal div}exch addprocs 4 1 roll
						{3 mul HiVal mul round cvi 1 add Lookup exch get HiVal div}exch addprocs 4 1 roll
						{3 mul HiVal mul round cvi 		Lookup exch get HiVal div}exch addprocs 4 1 roll
						setcolortransfer 
						tint_image_to_color
					}ifelse
				}ifelse
			}ifelse
		end end
	}def
	/indexed_image_lev1_sep
	{
		/indexed_colorspace_dict AGMCORE_gget begin
		begin
			{4 mul HiVal mul round cvi		 Lookup exch get HiVal div 1 exch sub}
			{4 mul HiVal mul round cvi 1 add Lookup exch get HiVal div 1 exch sub}
			{4 mul HiVal mul round cvi 2 add Lookup exch get HiVal div 1 exch sub}
			{4 mul HiVal mul round cvi 3 add Lookup exch get HiVal div 1 exch sub}
			AGMCORE_get_ink_data currenttransfer addprocs settransfer
			currentdict imageormask_sys
		end end
	}def
}if
end
systemdict/setpacking known
{setpacking}if
%%EndResource
currentdict Adobe_AGM_Utils eq {end} if
%%EndProlog
%%BeginSetup
Adobe_AGM_Utils begin
2 2010 Adobe_AGM_Core/ds gx
Adobe_CoolType_Core/ds get exec
Adobe_AGM_Image/ds gx
[/NamespacePush pdfmark_5
[/_objdef {Doc_Metadata} /type /stream /OBJ pdfmark_5
[{Doc_Metadata} 1059 (% &end XMP packet& %) ReadBypdfmark_5_string
<?xpacket begin='﻿' id='W5M0MpCehiHzreSzNTczkc9d'?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 9.0-c000 79.cca54b0, 2022/11/26-09:29:55        ">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:pdf="http://ns.adobe.com/pdf/1.3/"
    xmlns:xmp="http://ns.adobe.com/xap/1.0/"
    xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
   pdf:Producer="GPL Ghostscript 9.55.0"
   xmp:ModifyDate="2025-02-07T11:18:57+08:00"
   xmp:CreateDate="2025-02-07T11:17:37+08:00"
   xmp:CreatorTool="Adobe Acrobat 23.1.0"
   xmp:MetadataDate="2025-02-07T11:18:57+08:00"
   xmpMM:DocumentID="uuid:94aeceb6-e75d-11ef-0000-76237c9c065a"
   xmpMM:InstanceID="uuid:f1f6c9b6-129c-4783-902b-6951b299c1c1"
   dc:format="application/pdf">
   <dc:title>
    <rdf:Alt>
     <rdf:li xml:lang="x-default">Figure4.pdf</rdf:li>
    </rdf:Alt>
   </dc:title>
   <dc:creator>
    <rdf:Seq>
     <rdf:li>winchy</rdf:li>
    </rdf:Seq>
   </dc:creator>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
                                                                                                                                
<?xpacket end='w'?>


% &end XMP packet& %

[{Doc_Metadata} 2 dict begin /Type /Metadata def /Subtype /XML def currentdict end /PUT pdfmark_5
[/Document 1 dict begin /Metadata {Doc_Metadata} def currentdict end /BDC pdfmark_5
[/NamespacePop pdfmark_5
currentdict Adobe_AGM_Utils eq {end} if
%%EndSetup
%%Page: 1 1
%%EndPageComments
%%BeginPageSetup
Adobe_AGM_Utils begin
Adobe_AGM_Core/ps gx
Adobe_AGM_Core/capture_mysetup gx
Adobe_AGM_Utils/capture_cpd gx
Adobe_CoolType_Core/ps get exec
Adobe_AGM_Image/ps gx
Adobe_AGM_Core/ps gx
gsave
/0 
<<
/Name (Black)
/0 
[/DeviceCMYK] /CSA add_res
/CSA /0 get_csa_by_name
/MappedCSA /0 /CSA get_res
/TintMethod /Subtractive
/TintProc null
/NComponents 4 
/Components [ 0 0 0 1 ] 
>>
/CSD add_res
grestore
Adobe_AGM_Core/pt gx
%%EndPageSetup
1 -1 scale 0 -570 translate
pgsv
[1 0 0 1 0 0 ]ct
gsave
np
gsave
0 0 mo
0 570 li
757 570 li
757 0 li
cp
clp
gsave
0 570 mo
756.961 570 li
756.961 .893066 li
0 .893066 li
cp
eclp
.25 lw
2 lc
0 lj
10 ml
[] 0 dsh
true sadj
-49.9094 594.783 mo
791.981 594.783 li
791.981 -.496826 li
-49.9094 -.496826 li
cp
false sop
1 /0 /CSD get_res sepcs
.216 sep
@
430.561 173.837 mo
731.031 173.837 li
734.171 173.837 736.701 171.297 736.701 168.167 cv
736.701 30.687 li
736.701 27.557 734.171 25.017 731.031 25.017 cv
430.561 25.017 li
427.431 25.017 424.891 27.557 424.891 30.687 cv
424.891 168.167 li
424.891 171.297 427.431 173.837 430.561 173.837 cv
.007 .036 .229 0 cmyk
ef
497.831 529.755 mo
520.76 529.755 li
521.541 529.755 522.181 529.121 522.181 528.338 cv
522.181 513.206 li
522.181 512.423 521.541 511.788 520.76 511.788 cv
497.831 511.788 li
497.051 511.788 496.411 512.423 496.411 513.206 cv
496.411 528.338 li
496.411 529.121 497.051 529.755 497.831 529.755 cv
.444 .272 0 0 cmyk
ef
1 lc
1 lj
497.831 529.755 mo
520.76 529.755 li
521.541 529.755 522.181 529.121 522.181 528.338 cv
522.181 513.206 li
522.181 512.423 521.541 511.788 520.76 511.788 cv
497.831 511.788 li
497.051 511.788 496.411 512.423 496.411 513.206 cv
496.411 528.338 li
496.411 529.121 497.051 529.755 497.831 529.755 cv
cp
1 /0 /CSD get_res sepcs
1 sep
@
548.851 530.258 mo
571.791 530.258 li
572.57 530.258 573.201 529.623 573.201 528.841 cv
573.201 513.708 li
573.201 512.925 572.57 512.291 571.791 512.291 cv
548.851 512.291 li
548.07 512.291 547.431 512.925 547.431 513.708 cv
547.431 528.841 li
547.431 529.623 548.07 530.258 548.851 530.258 cv
.444 .272 0 0 cmyk
ef
548.851 530.258 mo
571.791 530.258 li
572.57 530.258 573.201 529.623 573.201 528.841 cv
573.201 513.708 li
573.201 512.925 572.57 512.291 571.791 512.291 cv
548.851 512.291 li
548.07 512.291 547.431 512.925 547.431 513.708 cv
547.431 528.841 li
547.431 529.623 548.07 530.258 548.851 530.258 cv
cp
1 /0 /CSD get_res sepcs
1 sep
@
587.25 530.24 mo
610.181 530.24 li
610.961 530.24 611.601 529.605 611.601 528.822 cv
611.601 513.69 li
611.601 512.907 610.961 512.272 610.181 512.272 cv
587.25 512.272 li
586.461 512.272 585.831 512.907 585.831 513.69 cv
585.831 528.822 li
585.831 529.605 586.461 530.24 587.25 530.24 cv
.377 .016 .604 0 cmyk
ef
587.25 530.24 mo
610.181 530.24 li
610.961 530.24 611.601 529.605 611.601 528.822 cv
611.601 513.69 li
611.601 512.907 610.961 512.272 610.181 512.272 cv
587.25 512.272 li
586.461 512.272 585.831 512.907 585.831 513.69 cv
585.831 528.822 li
585.831 529.605 586.461 530.24 587.25 530.24 cv
cp
1 /0 /CSD get_res sepcs
1 sep
@
627.401 530.721 mo
650.341 530.721 li
651.121 530.721 651.76 530.087 651.76 529.304 cv
651.76 514.171 li
651.76 513.389 651.121 512.754 650.341 512.754 cv
627.401 512.754 li
626.621 512.754 625.991 513.389 625.991 514.171 cv
625.991 529.304 li
625.991 530.087 626.621 530.721 627.401 530.721 cv
.377 .016 .604 0 cmyk
ef
627.401 530.721 mo
650.341 530.721 li
651.121 530.721 651.76 530.087 651.76 529.304 cv
651.76 514.171 li
651.76 513.389 651.121 512.754 650.341 512.754 cv
627.401 512.754 li
626.621 512.754 625.991 513.389 625.991 514.171 cv
625.991 529.304 li
625.991 530.087 626.621 530.721 627.401 530.721 cv
cp
1 /0 /CSD get_res sepcs
1 sep
@
666.621 530.721 mo
689.551 530.721 li
690.331 530.721 690.971 530.087 690.971 529.304 cv
690.971 514.171 li
690.971 513.389 690.331 512.754 689.551 512.754 cv
666.621 512.754 li
665.831 512.754 665.201 513.389 665.201 514.171 cv
665.201 529.304 li
665.201 530.087 665.831 530.721 666.621 530.721 cv
.377 .016 .604 0 cmyk
ef
666.621 530.721 mo
689.551 530.721 li
690.331 530.721 690.971 530.087 690.971 529.304 cv
690.971 514.171 li
690.971 513.389 690.331 512.754 689.551 512.754 cv
666.621 512.754 li
665.831 512.754 665.201 513.389 665.201 514.171 cv
665.201 529.304 li
665.201 530.087 665.831 530.721 666.621 530.721 cv
cp
1 /0 /CSD get_res sepcs
1 sep
@
717.231 530.825 mo
740.161 530.825 li
740.951 530.825 741.581 530.19 741.581 529.408 cv
741.581 514.275 li
741.581 513.492 740.951 512.858 740.161 512.858 cv
717.231 512.858 li
716.451 512.858 715.81 513.492 715.81 514.275 cv
715.81 529.408 li
715.81 530.19 716.451 530.825 717.231 530.825 cv
.377 .016 .604 0 cmyk
ef
717.231 530.825 mo
740.161 530.825 li
740.951 530.825 741.581 530.19 741.581 529.408 cv
741.581 514.275 li
741.581 513.492 740.951 512.858 740.161 512.858 cv
717.231 512.858 li
716.451 512.858 715.81 513.492 715.81 514.275 cv
715.81 529.408 li
715.81 530.19 716.451 530.825 717.231 530.825 cv
cp
1 /0 /CSD get_res sepcs
1 sep
@
458.871 530.332 mo
481.801 530.332 li
482.581 530.332 483.221 529.698 483.221 528.915 cv
483.221 513.782 li
483.221 513 482.581 512.365 481.801 512.365 cv
458.871 512.365 li
458.081 512.365 457.451 513 457.451 513.782 cv
457.451 528.915 li
457.451 529.698 458.081 530.332 458.871 530.332 cv
.444 .272 0 0 cmyk
ef
458.871 530.332 mo
481.801 530.332 li
482.581 530.332 483.221 529.698 483.221 528.915 cv
483.221 513.782 li
483.221 513 482.581 512.365 481.801 512.365 cv
458.871 512.365 li
458.081 512.365 457.451 513 457.451 513.782 cv
457.451 528.915 li
457.451 529.698 458.081 530.332 458.871 530.332 cv
cp
1 /0 /CSD get_res sepcs
1 sep
@
grestore
gsave
463.76 531.038 mo
479.496 531.038 li
479.496 510.496 li
463.76 510.496 li
cp
eclp
false sop
1 /0 /CSD get_res sepcs
1 sep
%ADOBeginSubsetFont: FBAAAA+TimesNewRomanPSMT Initial
ct_T42Dict begin
-0.566 -0.305 2.043 1.039
 256 array 0 1 255 {1 index exch /.notdef put} for  /FBAAAA+TimesNewRomanPSMT
Type42DictBegin
[<00010000000c000c000c000c4f532f3200000000000000cc000000566376
74201d6402d700000124000010846670676d6d591b53000011a800000a59
676c7966000000000000a548000075e468656164f36427bb00001c040000
003668686561134d1a9000001c3c00000024686d74780000000000001c60
000025aa6c6f6361000000000000420c000024f26d6178701940135d0000
6700000000206e616d65185574b60000672000002e9470726570b3329291
000095b400000f9367646972000000000000000000000000000100000190
000500080000000000000000000000000000000000000000000000000000
00000000000000000000000000080000000000000000000000000000f000
f0ff0000000000000000000000000001000000000000058e0000054c001f
054c001c0394001b0000ffe10000ffe40000ffe8fe4afffc056b0023fe6a
ffe00313000000ad000000ad0000000000250096009f002400f0013100c2
00c0004a00a6004100500094004700cf00af000e007901cb000400230044
00a80025011f0002004600170105009900d9005c007200e500e00028004b
00de011200240045007000160039ffe90016004b0088ffb900d9000a0043
00ae00ba016c0153002f00430048022c012b0025008fffc000170028ffcd
ffd80025009d00e50124ffb10048009d00e600110027007f00910012006a
00cafffc00000024006200a7017c01e900210060008b0434048aff6b003b
00b500d5014bff6b004d007905d809b5006c009100a3011701c0ffdfffe7
00be04010065007f00820088009900b200c0022e034305a000200026003d
004e00610065007b00d9011301310340ff27ff42ff99004e00a700f2022b
02c603070011002b0049005f008d00a100af00d600e400f5010b0135019d
01ab01ab01d101ee05d80000004b0075007a0080009d00a600a700ac00b9
013101310217021700020017002900550080008f00a500b200b300d0014b
015901c001c103a50530fe3fff14ff15ffe7ffff002a00580099009f00c1
00e400f40130015901ab01ab03220374041e04740532fd81004d0064009c
00d000d100d600de00e500f500f8012a012a01e1027e027fff57ffa8ffe5
00000008001f00380051005a006f0076007700a200c000c200c400f101fb
0209027e02cf04c5057a05f0ff92001200260042004b004f005100530064
008b00ae00b200b800b800d600f50111012001310138014e01520167018f
019601b801d901d902060221027102ea03b003cb03dc04360505ff3a0012
0016001e001f002300570068006c007e0088009200a500a800c500c90115
0126012d013001d601d901f6023b0244024402a302cf02de0385038f04fc
0586fee0feebfefbff8a0007004400470058007500aa00e400ef01160120
0129016a017301e3027e029002b4030e0310032303350341035403590388
039403c803ce047204ab04da0549056105ab0761fe6efed1ff4bff840000
00010006001e0027002c0034003700620066006a006b006c007000700072
007c0081008a008e0091009200a000ab00b800bf00c900d500dd00ec00f4
0100012101300169016a016d017c0185018e018e019901ac01c101c501c9
01e101f601f601f60222022202280236023f024302460267028502850294
02d002d602e8031c0363037f03800380039e03b603d90400040404ff0532
05320548058b05a706cb07280748076208ccfcedfd2afd59fddefe00fe1a
fe5bfe96fec1fee7ff56ff7900010025002d002e007c00870091009900a1
00a500a500aa00af00b600c600cc00d700dd00ec00f20102010501170118
0123012a012c0131013f014701490149014d01510151015501550157015a
015a0161016201680168017f0180018201830184018d0195019501950198
019901a501a901b601b601b701ba01ba01d501df01e601ea01f202000200
0203021702250227022f0239024302430247024f025202520267026f026f
027002720276027e02a702b302b902d603130325032d03610371039903ae
03c203d403f90402042c042f043c04560467048304cf04d104d804fb051f
05450568059e05c2061b06340655066a069806af06e806fc070607500762
077c07d407ff082500ad00c700aa00b5000000000000000000000000002f
06cf01730514047802df009c0018037005870155002500060254036c038e
03d2056601f0032001da018a0369036bffa3034602f8036f015602bf0122
031f053a0366008c00ff01ab02e102f402e70415015402e90128049101b7
026f034302060000000005d30415048305e8000002d7003a027d01c002c5
03830383ffbd003a059e01df059e02d1002004e0021300df01c001870297
000000ce0269028b0058043405fb0069015a01a905780182013e0288012a
03d4049e00e5032302f301f00196007a00cd014a0424025e023901ab00cf
00fd011e00ed017100700195004001bb01dd01b8000101a803a7014c020c
018d01b0020d0137010000cd032101d4030a005900000000012602150150
02f0025503bc06d00335010100d000d2007a01030130007c000000000000
000000fe006e006600940227002b0045004d00d3013200180097004100f4
febcffe9001605d8058b009100a1032c00520030005d02cb003a009200e5
00e500580086003200ba0099008800300298007cff8001640028004d0065
000200b8016a002f010b001100170100007f00040016022200a6005f0000
00f8000a00ca0043004b01ee0077012000f401c00028045f0000008c0445
00c20060007b008b008b0064005d00c2009c009206b505d3004f01170000
0420fe9e00cc00dc005e004600e30032001a003c0091005a00a1042c0041
002000490071009c009cfe4800400040008600cb0102007d003a003e006a
0050044800290096ff6a0097006900e0004c001b00c90069ff970043ffbd
0052ff83ff8b005fffa1ff5c00670053ffa8002a0076ffb2003600870559
0256052b043400de00c901c4004800db018b00b3004800da011601250118
00ea00ea00ae0000003e05bb008a04d70053003fff8cffd5001500280022
00990062004a00e4006d00ee00e5004803c00033fe4e02b1ff4603700079
05df0051ffa7ff1f010a0068ff6c004f00bc00a5070500ab0080001e05a5
0025008b04660230006900290016012f0080005c059f03d703f104700000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000160016001700180018001a001b00210029002a002a002c002d002e
002f003200340036003700380039003a003b003c003d003e004200460046
004a004c004d004f004f00530053005500570059005c005c005d005d005e
005f0061006400650067006800690069006b006e006f0071007600760077
0077007d007e007f008000810082008600870087008a008d008e00960096
00970097009c00a000a200a300a600ac00b300b300b600b800b900be00bf
00c100c200c400c500c600c700ca00ca00cb00cc00cc00ce00d100d200d3
00d700da00db00dc00de00df00e000e000e300e640578574737271706f6e
6d6c6b6a6968676665625d55544f4e403f3e3d3c3b3a3938373635343332
31302f2e2d2c2b2a292827262524232221201f1e1d1c1b1a191817161413
1211100f0e0d0c0b0a090807060504030201002c4523466020b02660b004
262348482d2c452346236120b02661b004262348482d2c45234660b02061
20b04660b004262348482d2c4523462361b0206020b02661b02061b00426
2348482d2c45234660b0406120b06660b004262348482d2c4523462361b0
406020b02661b04061b004262348482d2c0110203c003c2d2c20452320b0
cd442320b8015a51582320b08d44235920b0ed51582320b04d44235920b0
9051582320b00d44235921212d2c20204518684420b001602045b0467668
8a4560442d2c01b10b0a432343650a2d2c00b10a0b4323430b2d2c00b017
2370b101173e01b0172370b10217453ab10200080d2d2c45b01a234445b0
1923442d2c2045b00325456164b050515845441b2121592d2cb001436323
62b0002342b00f2b2d2c2045b0004360442d2c01b00643b00743650a2d2c
2069b04061b0008b20b12cc08a8cb8100062602b0c642364615c58b00361
592d2c45b0112bb0172344b0177ae4182d2c45b0112bb01723442d2cb012
43588745b0112bb0172344b0177ae41b038a45186920b01723448a8a8720
b0a05158b0112bb0172344b0177ae41b21b0177ae45959182d2cb0022546
608a46b040618c482d2c4b53205c58b002855958b00185592d2c20b00325
45b019234445b01a23444565234520b00325606a20b009234223688a6a60
6120b01a8ab000527921b21a1a40b9ffe0001a45208a54582321b03f1b23
5961441cb114008a5279b31940201945208a54582321b03f1b235961442d
2cb110114323430b2d2cb10e0f4323430b2d2cb10c0d4323430b2d2cb10c
0d432343650b2d2cb10e0f432343650b2d2cb11011432343650b2d2c4b52
5845441b2121592d2c0120b003252349b04060b0206320b000525823b002
253823b002256538008a63381b212121212159012d2c4bb06451584569b0
0943608a103a1b212110592d2c01b005251023208af500b0016023edec2d
2c01b005251023208af500b0016123edec2d2c01b0062510f500edec2d2c
20b001600110203c003c2d2c20b001610110203c003c2d2cb02b2bb02a2a
2d2c00b00743b006430b2d2c3eb02a2a2d2c352d2c76b802b023701020b8
02b04520b0005058b00161593a2f182d2c21210c6423648bb84000622d2c
21b08051580c6423648bb82000621bb200402f2b59b002602d2c21b0c051
580c6423648bb81555621bb200802f2b59b002602d2c0c6423648bb84000
626023212d2cb4000100000015b00826b00826b00826b008260f10161345
683ab001162d2cb4000100000015b00826b00826b00826b008260f101613
4568653ab001162d2c4b53234b515a5820458a60441b2121592d2c4b5458
20458a60441b2121592d2c4b53234b515a58381b2121592d2c4b5458381b
2121592d2c014b53234b515ab00225b00425b006254923451869525a58b0
0225b00225b00525462345696048592121212d2cb0134358031b02592d2c
b0134358021b03592d2c4b54b012435c5a58381b2121592d2cb012435c58
0cb00425b00425060c6423646164b807085158b00425b00425012046b010
60482046b0106048590a21211b2121592d2cb012435c580cb00425b00425
060c6423646164b807085158b00425b00425012046b8fff060482046b8ff
f06048590a21211b2121592d2c4b53234b515a58b03a2b1b2121592d2c4b
53234b515a58b03b2b1b2121592d2c4b53234b515ab012435c5a58381b21
21592d2c0c8a034b54b00426024b545a8a8a0ab012435c5a58381b212159
2d2c462346608a8a462320468a608a61b8ff8062232010238ab903580358
8a70456020b0005058b00161b8ffba8b1bb0468c59b0106068013a2d2c23
20b000508a8a64b10003255458b0401bb10103255458b037438b59b04f2b
5923b0622b2321235865592d2cb13a000c215460432d2cb1020042b12301
8851b1400188535a58b910000020885458b202010243604259b124018851
58b920000040885458b2020202436042b12401885458b202200243604200
4b014b5258b2020802436042591bb940000080885458b202040243604259
b94000008063b80100885458b202080243604259b94000010063b8020088
5458b202100243604259b12601885158b94000020063b80400885458b202
400243604259b94000040063b80800885458b202800243604259b1280188
5158b94000080063b81000885458ba000201000002436042595959595959
59b10002435458400a37403a403b403e023f021bb10102435458b237403a
ba0100003b0100b33e013f011bb18002435258b237403ab80180b13b401b
b901000002435258b237403aba0180003b01401bb901800002435258b237
403ab80200b13b401bb237403aba0100003b0100595959b9400000808855
b94000020063b8040088555a58b33e003f011bb33e003f01595959424242
42422d2cb0024354584b53234b515a58381b2121591b21212121592d2c01
2d2cb0022563b0206066b00225b82000626023622d2c234ab1024e2b2d2c
234ab1014e2b2d2c238a4a234564b0022564b002256164b0354352582120
6459b1024e2b23b000505865592d2c238a4a234564b0022564b002256164
b03543525821206459b1014e2b23b000505865592d2c20b003254ab1024e
2b8a103b2d2c20b003254ab1014e2b8a103b2d2cb00325b003258ab0672b
8a103b2d2cb00325b003258ab0682b8a103b2d2cb0032546b003254660b0
04252eb00425b00425b0042620b000505821b06a1bb06c592bb0032546b0
0325466061b08062208a2010233a232010233a2d2cb0032547b003254760
b0052547b0806361b00225b00625496323b005254ab080632058621b2159
b0042646608a468a4660b02063612d2cb00426b00425b00425b00426b06e
2b208a2010233a232010233a2d2c2320b001545821b00225b1024e2bb080
5020605920606020b001515821211b20b005515821206661b0402361b100
032550b00325b00325505a5820b00325618a535821b000591b21591bb007
54582066616523211b2121b000595959b1024e2b2d2cb00225b004254ab0
005358b0001b8a8a238ab00159b004254620666120b00526b0062649b005
26b00526b0702b236165b02060206661b02061652d2cb0022546208a20b0
00505821b1024e2b1b452321596165b00225103b2d2cb0042620b8020062
20b80200638a236120b05d602bb00525118a128a20398a58ba005d100000
04266356602b23212010204620b1024e2b23611b2321208a201049b1024e
2b593b2d2cba005d10000009256356602bb00525b00525b00526b06d2bb1
5d0725602bb00525b00525b00525b00525b06f2bba005d10000008266356
602b20b0005258b0502bb00525b00525b00725b00725b00525b0712bb002
1738b00052b00225b001525a58b00425b0062549b00325b00525496020b0
405258211bb000525820b0025458b00425b00425b00725b0072549b00217
381bb00425b00425b00425b0062549b0021738595959595921212121212d
2cb12501885058b94000020063b8040088545cb0134b525b1bb001592d00
000000010000000707aeb1b0afba5f0f3cf50819080000000000a2e31dc2
00000000dd7cb770fb74fd8c105e08510000000900010000000000000001
00000721fe4500571000fb74f9d2105e0001000000000000000000000000
0000005c0639011c0639011c0639011c0200000002000000020000000200
00000200000002000000020000000200000002aa005402aa002e02aa002e
02aa002e02aa002e02aa0053020000910200009102000091040000f00400
002c0400002c0400002c0400002c0400002c0400002c0400002c0400002c
0400002c0400002c0400002c0400002c0400002c0400002c0400002c05c7
001005c700100556004a0556004a0556004a0473002105c7004805c70023
05c7002305c7002305c7002204e30029071d002205c7ffe605c7ffe60473
002205c70048055600230473008004e3003e04e3003e05c7001205c70012
05c7001205c7001205c7001205c7001205c7001205c7001205c7001205c7
001205c70012038d0049038d0049038d004604000044038d004c02aa004f
0400003d0400000d0239003c0239003c040000110239003d063900110400
000c040000450400fffa0400fffa02aa000d031d00640239001404000002
0400001105c7000d0400001b000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c000c000c000c000c000c000c000c
000c000c000c000c000c000c000c000c00000000004b004b004b004b004b
004b004b004b004b004b004b009600e000e000e000e00117014b014b014b
01ca02c902c902c902c902c902c902c902c902c902c902c902c902c902c9
02c9042b042b050405040504060307230861086108610a3b0adf0c2a0d62
0d620e7c0f5710cc126a132b132b147e147e147e147e147e147e147e147e
147e147e147e169c169c17e2195f1b6b1cc91f4820f72265226524b725b2
283229ff2b452cc32cc32ded306a31aa331034bc370539793af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af23af23af2
3af23af23af23af23af23af23af23af23af23af23af23af23af200000001
0000127802b5003c00d100070002001000400086000005e90f9300050002
00>
<0000003a02be0000000300000000021a00000000000300000001001e021a
0000000300000002000e0238000000030000000300580246000000030000
0004001e021a00000003000000050018029e0000000300000006002202b6
0000000300000007007602d800000003000000080030000e000000030000
00090086034e000000030000000d0e0403d40001000000000000010d11d8
0001000000000001000f12e50001000000000002000712f4000100000000
0003002c12fb0001000000000004000f12e50001000000000005000c1327
0001000000000006001113330001000000000007003b1344000100000000
0008001811df00010000000000090043137f000100000000000d070213c2
0003000104030002000c1ac4000300010405000200101ad0000300010406
0002000c1ae0000300010407000200101aec000300010408000200101afc
000300010409000002221b0c0003000104090001001e021a000300010409
0002000e02380003000104090003005802460003000104090004001e021a
00030001040900050018029e0003000104090006002202b6000300010409
0007007602d800030001040900080030000e00030001040900090086034e
000300010409000d0e141d2e00030001040a0002000c1ac400030001040b
000200102b4200030001040c0002000c1ac400030001040e0002000c2b52
0003000104100002000e2b5e000300010413000200122b6c000300010414
0002000c1ac4000300010415000200102b7e0003000104160002000c1ac4
0003000104190002000e2b8e00030001041b000200102b9c00030001041d
0002000c1ac400030001041f0002000c1ac40003000104240002000e2bac
00030001042a0002000e2bba00030001042d0002000e2bc800030001080a
0002000c1ac40003000108160002000c1ac4000300010c0a0002000c1ac4
000300010c0c0002000c1ac400a900200032003000320030002000540068
00650020004d006f006e006f007400790070006500200043006f00720070
006f0072006100740069006f006e002e00200041006c006c002000520069
0067006800740073002000520065007300650072007600650064002e0020
000d000d0048006500620072006500770020004f00700065006e00540079
007000650020004c00610079006f007500740020006c006f006700690063
00200063006f0070007900720069006700680074002000a9002000320030
003000330020002600200032003000300037002c002000520061006c0070
0068002000480061006e0063006f0063006b002000260020004a006f0068
006e00200048007500640073006f006e002e002000540068006900730020
006c00610079006f007500740020006c006f00670069006300200066006f
00720020004200690062006c006900630061006c00200048006500620072
006500770020006900730020006f00700065006e00200073006f00750072
0063006500200073006f00660074007700610072006500200075006e0064
0065007200200074006800650020004d004900540020004c006900630065
006e00730065003b002000730065006500200065006d0062006500640064
006500640020006c006900630065006e0073006500200064006500730063
00720069007000740069006f006e00200066006f00720020006400650074
00610069006c0073002e00540069006d006500730020004e006500770020
0052006f006d0061006e0052006500670075006c00610072004d006f006e
006f0074007900700065003a00540069006d006500730020004e00650077
00200052006f006d0061006e00200052006500670075006c006100720020
0028004d006900630072006f0073006f0066007400290056006500720073
0069006f006e00200037002e0030003300540069006d00650073004e0065
00770052006f006d0061006e00500053004d005400540069006d00650073
0020004e0065007700200052006f006d0061006e00200069007300200061
002000740072006100640065006d00610072006b0020006f006600200054
006800650020004d006f006e006f007400790070006500200043006f0072
0070006f0072006100740069006f006e002e004d006f006e006f00740079
0070006500200054007900700065002000440072006100770069006e0067
0020004f006600660069006300650020002d0020005300740061006e006c
006500790020004d006f007200690073006f006e002c0020005600690063
0074006f00720020004c0061007200640065006e00740020003100390033
0032004d006900630072006f0073006f0066007400200073007500700070
006c00690065006400200066006f006e0074002e00200059006f00750020
006d0061007900200075007300650020007400680069007300200066006f
006e007400200074006f0020006300720065006100740065002c00200064
006900730070006c00610079002c00200061006e00640020007000720069
006e007400200063006f006e00740065006e007400200061007300200070
00650072006d006900740074006500640020006200790020007400680065
0020006c006900630065006e007300650020007400650072006d00730020
006f00720020007400650072006d00730020006f00660020007500730065
002c0020006f006600200074006800650020004d006900630072006f0073
006f00660074002000700072006f0064007500630074002c002000730065
00720076006900630065002c0020006f007200200063006f006e00740065
006e007400200069006e0020007700680069006300680020007400680069
007300200066006f006e0074002000770061007300200069006e0063006c
0075006400650064002e00200059006f00750020006d006100790020006f
006e006c0079002000280069002900200065006d00620065006400200074
00680069007300200066006f006e007400200069006e00200063006f006e
00740065006e00740020006100730020007000650072006d006900740074
00650064002000620079002000740068006500200065006d006200650064
00640069006e00670020007200650073007400720069006300740069006f
006e007300200069006e0063006c007500640065006400200069006e0020
007400680069007300200066006f006e0074003b00200061006e00640020
0028006900690029002000740065006d0070006f0072006100720069006c
007900200064006f0077006e006c006f0061006400200074006800690073
00200066006f006e007400200074006f002000610020007000720069006e
0074006500720020006f00720020006f00740068006500720020006f0075
0074007000750074002000640065007600690063006500200074006f0020
00680065006c00700020007000720069006e007400200063006f006e0074
0065006e0074002e00200041006e00790020006f00740068006500720020
007500730065002000690073002000700072006f00680069006200690074
00650064002e000d000d00540068006500200066006f006c006c006f0077
0069006e00670020006c006900630065006e00730065002c002000620061
0073006500640020006f006e00200074006800650020004d004900540020
006c006900630065006e00730065002000280068007400740070003a002f
002f0065006e002e00770069006b006900700065006400690061002e006f
00720067002f00770069006b0069002f004d00490054005f004c00690063
0065006e007300650029002c0020006100700070006c0069006500730020
0074006f00200074006800650020004f00700065006e0054007900700065
0020004c00610079006f007500740020006c006f00670069006300200066
006f00720020004200690062006c006900630061006c0020004800650062
0072006500770020201c004c00610079006f007500740020004c006f0067
00690063201d0020006100730020006a006f0069006e0074006c00790020
0064006500760065006c006f007000650064002000620079002000520061
006c00700068002000480061006e0063006f0063006b00200061006e0064
0020004a006f0068006e00200048007500640073006f006e002e0020000d
000d005000650072006d0069007300730069006f006e0020006900730020
0068006500720065006200790020006700720061006e007400650064002c
002000660072006500650020006f00660020006300680061007200670065
002c00200074006f00200061006e007900200070006500720073006f006e
0020006f0062007400610069006e0069006e00670020006100200063006f
007000790020006f006600200074006800650020004f00700065006e0054
0079007000650020004c00610079006f007500740020006c006f00670069
006300200066006f00720020004200690062006c006900630061006c0020
00480065006200720065007700200061006e00640020006100730073006f
00630069006100740065006400200064006f00630075006d0065006e0074
006100740069006f006e002000660069006c006500730020002800740068
00650020201c004c00610079006f007500740020004c006f006700690063
00200053006f006600740077006100720065201d0029002c00200074006f
0020006400650061006c00200069006e00200074006800650020004c0061
0079006f007500740020004c006f00670069006300200053006f00660074
007700610072006500200077006900740068006f00750074002000720065
0073007400720069006300740069006f006e002c00200069006e0063006c
007500640069006e006700200077006900740068006f007500740020006c
0069006d00690074006100740069006f006e002000740068006500200072
0069006700680074007300200074006f0020007500730065002c00200063
006f00700079002c0020006d006f0064006900660079002c0020006d0065
007200670065002c0020007000750062006c006900730068002c00200064
006900730074007200690062007500740065002c0020007300750062006c
006900630065006e00730065002c00200061006e0064002f006f00720020
00730065006c006c00200063006f00700069006500730020006f00660020
0074006800650020004c00610079006f007500740020004c006f00670069
006300200053006f006600740077006100720065002c00200061006e0064
00200074006f0020007000650072006d0069007400200070006500720073
006f006e007300200074006f002000770068006f006d0020007400680065
0020004c00610079006f007500740020004c006f00670069006300200053
006f0066007400770061007200650020006900730020006600750072006e
0069007300680065006400200074006f00200064006f00200073006f002c
0020007300750062006a00650063007400200074006f0020007400680065
00200066006f006c006c006f00770069006e006700200063006f006e0064
006900740069006f006e0073003a000d000d005400680065002000610062
006f0076006500200063006f00700079007200690067006800740020006e
006f007400690063006500200061006e0064002000740068006900730020
007000650072006d0069007300730069006f006e0020006e006f00740069
006300650020007300680061006c006c00200062006500200069006e0063
006c007500640065006400200069006e00200061006c006c00200063006f
00700069006500730020006f00720020007300750062007300740061006e
007400690061006c00200070006f007200740069006f006e00730020006f
006600200074006800650020004c00610079006f007500740020004c006f
00670069006300200053006f006600740077006100720065002e000d000d
00540048004500200053004f004600540057004100520045002000490053
002000500052004f00560049004400450044002000270041005300200049
00530027002c00200057004900540048004f005500540020005700410052
00520041004e005400590020004f004600200041004e00590020004b0049
004e0044002c002000450058005000520045005300530020004f00520020
0049004d0050004c004900450044002c00200049004e0043004c00550044
0049004e004700200042005500540020004e004f00540020004c0049004d
004900540045004400200054004f00200054004800450020005700410052
00520041004e00540049004500530020004f00460020004d004500520043
00480041004e0054004100420049004c004900540059002c002000460049
0054004e00450053005300200046004f0052002000410020005000410052
0054004900430055004c0041005200200050005500520050004f00530045
00200041004e00440020004e004f004e0049004e004600520049004e0047
0045004d0045004e0054002e00200049004e0020004e004f002000450056
0045004e00540020005300480041004c004c002000540048004500200041
005500540048004f005200530020004f005200200043004f005000590052
004900470048005400200048004f004c0044004500520053002000420045
0020004c004900410042004c004500200046004f005200200041004e0059
00200043004c00410049004d002c002000440041004d0041004700450053
0020004f00520020004f00540048004500520020004c0049004100420049
004c004900540059002c0020005700480045005400480045005200200049
004e00200041004e00200041004300540049004f004e0020004f00460020
0043004f004e00540052004100430054002c00200054004f005200540020
004f00520020004f00540048004500520057004900530045002c00200041
0052004900530049004e0047002000460052004f004d002c0020004f0055
00540020004f00460020004f005200200049004e00200043004f004e004e
0045004300540049004f004e002000570049005400480020005400480045
00200053004f0046005400570041005200450020004f0052002000540048
004500200055005300450020004f00520020004f00540048004500520020
004400450041004c0049004e0047005300200049004e0020005400480045
00200053004f004600540057004100520045002ea9203230323020546865
204d6f6e6f7479706520436f72706f726174696f6e2e20416c6c20526967
6874732052657365727665642e200d0d486562726577204f70656e547970
65204c61796f7574206c6f67696320636f7079726967687420a920323030
33202620323030372c2052616c70682048616e636f636b2026204a6f686e
20487564736f6e2e2054686973206c61796f7574206c6f67696320666f72
204269626c6963616c20486562726577206973206f70656e20736f757263
6520736f66747761726520756e64657220746865204d4954204c6963656e
73653b2073656520656d626564646564206c6963656e7365206465736372
697074696f6e20666f722064657461696c732e54696d6573204e65772052
6f6d616e526567756c61724d6f6e6f747970653a54696d6573204e657720
526f6d616e20526567756c617220284d6963726f736f6674295665727369
6f6e20372e303354696d65734e6577526f6d616e50534d5454696d657320
4e657720526f6d616e20697320612074726164656d61726b206f66205468
65204d6f6e6f7479706520436f72706f726174696f6e2e4d6f6e6f747970
6520547970652044726177696e67204f6666696365202d205374616e6c65
79204d6f7269736f6e2c20566963746f72204c617264656e742031393332
4d6963726f736f667420737570706c69656420666f6e742e20596f75206d
617920757365207468697320666f6e7420746f206372656174652c206469
73706c61792c20616e64207072696e7420636f6e74656e74206173207065
726d697474656420627920746865206c6963656e7365207465726d73206f
72207465726d73206f66207573652c206f6620746865204d6963726f736f
66742070726f647563742c20736572766963652c206f7220636f6e74656e
7420696e207768696368207468697320666f6e742077617320696e636c75
6465642e20596f75206d6179206f6e6c792028692920656d626564207468
697320666f6e7420696e20636f6e74656e74206173207065726d69747465
642062792074686520656d62656464696e67207265737472696374696f6e
7320696e636c7564656420696e207468697320666f6e743b20616e642028
6969292074656d706f726172696c7920646f776e6c6f6164207468697320
666f6e7420746f2061207072696e746572206f72206f74686572206f7574
7075742064657669636520746f2068656c70207072696e7420636f6e7465
6e742e20416e79206f74686572207573652069732070726f686962697465
642e0d0d54686520666f6c6c6f77696e67206c6963656e73652c20626173
6564206f6e20746865204d4954206c6963656e73652028687474703a2f2f
656e2e77696b6970656469612e6f72672f77696b692f4d49545f4c696365
6e7365292c206170706c69657320746f20746865204f70656e5479706520
4c61796f7574206c6f67696320666f72204269626c6963616c2048656272
657720d24c61796f7574204c6f676963d3206173206a6f696e746c792064
6576656c6f7065642062792052616c70682048616e636f636b20616e6420
4a6f686e20487564736f6e2e200d0d5065726d697373696f6e2069732068
6572656279206772616e7465642c2066726565206f66206368617267652c
20746f20616e7920706572736f6e206f627461696e696e67206120636f70
79206f6620746865204f70656e54797065204c61796f7574206c6f676963
20666f72204269626c6963616c2048656272657720616e64206173736f63
696174656420646f63756d656e746174696f6e2066696c65732028746865
20d24c61796f7574204c6f67696320536f667477617265d3292c20746f20
6465616c20696e20746865204c61796f7574204c6f67696320536f667477
61726520776974686f7574207265737472696374696f6e2c20696e636c75
64696e6720776974686f7574206c696d69746174696f6e20746865207269
6768747320746f207573652c20636f70792c206d6f646966792c206d6572
67652c207075626c6973682c20646973747269627574652c207375626c69
63656e73652c20616e642f6f722073656c6c20636f70696573206f662074
6865204c61796f7574204c6f67696320536f6674776172652c20616e6420
746f207065726d697420706572736f6e7320746f2077686f6d2074686520
4c61796f7574204c6f67696320536f667477617265206973206675726e69
7368656420746f20646f20736f2c207375626a65637420746f2074686520
666f6c6c6f77696e6720636f6e646974696f6e733a0d0d5468652061626f
766520636f70797269676874206e6f7469636520616e6420746869732070
65726d697373696f6e206e6f74696365207368616c6c20626520696e636c
7564656420696e20616c6c20636f70696573206f72207375627374616e74
69616c20706f7274696f6e73206f6620746865204c61796f7574204c6f67
696320536f6674776172652e0d0d54484520534f46545741524520495320
50524f564944454420274153204953272c20574954484f55542057415252
414e5459204f4620414e59204b494e442c2045585052455353204f522049
4d504c4945442c20494e434c5544494e4720425554204e4f54204c494d49
54454420544f205448452057415252414e54494553204f46204d45524348
414e544142494c4954592c204649544e45535320464f5220412050415254
4943554c415220505552504f534520414e44204e4f4e494e4652494e4745
4d454e542e20494e204e4f204556454e54205348414c4c20544845204155
54484f5253204f5220434f5059524947485420484f4c4445525320424520
4c4941424c4520464f5220414e5920434c41494d2c2044414d4147455320
4f52204f54484552204c494142494c4954592c205748455448455220494e
20414e20414354494f4e204f4620434f4e54524143542c20544f5254204f
52204f54484552574953452c2041524953494e472046524f4d2c204f5554
204f46204f5220494e20434f4e4e454354494f4e20574954482054484520
534f465457415245204f522054484520555345204f52204f544845522044
45414c494e475320494e2054484520534f4654574152452e004e006f0072
006d0061006c006f00620079010d0065006a006e00e9006e006f0072006d
0061006c005300740061006e0064006100720064039a03b103bd03bf03bd
03b903ba03ac00a90020003200300032003000200054006800650020004d
006f006e006f007400790070006500200043006f00720070006f00720061
00740069006f006e002e00200041006c006c002000520069006700680074
0073002000520065007300650072007600650064002e0020000d000a000d
000a0048006500620072006500770020004f00700065006e005400790070
00650020004c00610079006f007500740020006c006f0067006900630020
0063006f0070007900720069006700680074002000a90020003200300030
00330020002600200032003000300037002c002000520061006c00700068
002000480061006e0063006f0063006b002000260020004a006f0068006e
00200048007500640073006f006e002e002000540068006900730020006c
00610079006f007500740020006c006f00670069006300200066006f0072
0020004200690062006c006900630061006c002000480065006200720065
00770020006900730020006f00700065006e00200073006f007500720063
006500200073006f00660074007700610072006500200075006e00640065
007200200074006800650020004d004900540020004c006900630065006e
00730065003b002000730065006500200065006d00620065006400640065
00640020006c006900630065006e00730065002000640065007300630072
0069007000740069006f006e00200066006f007200200064006500740061
0069006c0073002e000d000a004d006900630072006f0073006f00660074
00200073007500700070006c00690065006400200066006f006e0074002e
00200059006f00750020006d006100790020007500730065002000740068
0069007300200066006f006e007400200074006f00200063007200650061
00740065002c00200064006900730070006c00610079002c00200061006e
00640020007000720069006e007400200063006f006e00740065006e0074
0020006100730020007000650072006d0069007400740065006400200062
007900200074006800650020006c006900630065006e0073006500200074
00650072006d00730020006f00720020007400650072006d00730020006f
00660020007500730065002c0020006f006600200074006800650020004d
006900630072006f0073006f00660074002000700072006f006400750063
0074002c00200073006500720076006900630065002c0020006f00720020
0063006f006e00740065006e007400200069006e00200077006800690063
00680020007400680069007300200066006f006e00740020007700610073
00200069006e0063006c0075006400650064002e00200059006f00750020
006d006100790020006f006e006c0079002000280069002900200065006d
0062006500640020007400680069007300200066006f006e007400200069
006e00200063006f006e00740065006e0074002000610073002000700065
0072006d0069007400740065006400200062007900200074006800650020
0065006d00620065006400640069006e0067002000720065007300740072
0069006300740069006f006e007300200069006e0063006c007500640065
006400200069006e0020007400680069007300200066006f006e0074003b
00200061006e006400200028006900690029002000740065006d0070006f
0072006100720069006c007900200064006f0077006e006c006f00610064
0020007400680069007300200066006f006e007400200074006f00200061
0020007000720069006e0074006500720020006f00720020006f00740068
006500720020006f00750074007000750074002000640065007600690063
006500200074006f002000680065006c00700020007000720069006e0074
00200063006f006e00740065006e0074002e00200041006e00790020006f
00740068006500720020007500730065002000690073002000700072006f
0068006900620069007400650064002e000d000a000d000a005400680065
00200066006f006c006c006f00770069006e00670020006c006900630065
006e00730065002c0020006200610073006500640020006f006e00200074
006800650020004d004900540020006c006900630065006e007300650020
00280068007400740070003a002f002f0065006e002e00770069006b0069
00700065006400690061002e006f00720067002f00770069006b0069002f
004d00490054005f004c006900630065006e007300650029002c00200061
00700070006c00690065007300200074006f00200074006800650020004f
00700065006e00540079007000650020004c00610079006f007500740020
006c006f00670069006300200066006f00720020004200690062006c0069
00630061006c00200048006500620072006500770020201c004c00610079
006f007500740020004c006f006700690063201d0020006100730020006a
006f0069006e0074006c007900200064006500760065006c006f00700065
0064002000620079002000520061006c00700068002000480061006e0063
006f0063006b00200061006e00640020004a006f0068006e002000480075
00640073006f006e002e0020000d000a000d000a005000650072006d0069
007300730069006f006e0020006900730020006800650072006500620079
0020006700720061006e007400650064002c002000660072006500650020
006f00660020006300680061007200670065002c00200074006f00200061
006e007900200070006500720073006f006e0020006f0062007400610069
006e0069006e00670020006100200063006f007000790020006f00660020
0074006800650020004f00700065006e00540079007000650020004c0061
0079006f007500740020006c006f00670069006300200066006f00720020
004200690062006c006900630061006c0020004800650062007200650077
00200061006e00640020006100730073006f006300690061007400650064
00200064006f00630075006d0065006e0074006100740069006f006e0020
00660069006c00650073002000280074006800650020201c004c00610079
006f007500740020004c006f00670069006300200053006f006600740077
006100720065201d0029002c00200074006f0020006400650061006c0020
0069006e00200074006800650020004c00610079006f007500740020004c
006f00670069006300200053006f00660074007700610072006500200077
006900740068006f00750074002000720065007300740072006900630074
0069006f006e002c00200069006e0063006c007500640069006e00670020
0077006900740068006f007500740020006c0069006d0069007400610074
0069006f006e002000740068006500200072006900670068007400730020
0074006f0020007500730065002c00200063006f00700079002c0020006d
006f0064006900660079002c0020006d0065007200670065002c00200070
00750062006c006900730068002c00200064006900730074007200690062
007500740065002c0020007300750062006c006900630065006e00730065
002c00200061006e0064002f006f0072002000730065006c006c00200063
006f00700069006500730020006f006600200074006800650020004c0061
0079006f007500740020004c006f00670069006300200053006f00660074
0077006100720065002c00200061006e006400200074006f002000700065
0072006d0069007400200070006500720073006f006e007300200074006f
002000770068006f006d00200074006800650020004c00610079006f0075
00740020004c006f00670069006300200053006f00660074007700610072
00650020006900730020006600750072006e006900730068006500640020
0074006f00200064006f00200073006f002c0020007300750062006a0065
0063007400200074006f002000740068006500200066006f006c006c006f
00770069006e006700200063006f006e0064006900740069006f006e0073
003a000d000a000d000a005400680065002000610062006f007600650020
0063006f00700079007200690067006800740020006e006f007400690063
006500200061006e0064002000740068006900730020007000650072006d
0069007300730069006f006e0020006e006f007400690063006500200073
00680061006c006c00200062006500200069006e0063006c007500640065
006400200069006e00200061006c006c00200063006f0070006900650073
0020006f00720020007300750062007300740061006e007400690061006c
00200070006f007200740069006f006e00730020006f0066002000740068
00650020004c00610079006f007500740020004c006f0067006900630020
0053006f006600740077006100720065002e000d000a000d000a00540048
004500200053004f00460054005700410052004500200049005300200050
0052004f0056004900440045004400200027004100530020004900530027
002c00200057004900540048004f00550054002000570041005200520041
004e005400590020004f004600200041004e00590020004b0049004e0044
002c002000450058005000520045005300530020004f005200200049004d
0050004c004900450044002c00200049004e0043004c005500440049004e
004700200042005500540020004e004f00540020004c0049004d00490054
0045004400200054004f0020005400480045002000570041005200520041
004e00540049004500530020004f00460020004d00450052004300480041
004e0054004100420049004c004900540059002c0020004600490054004e
00450053005300200046004f005200200041002000500041005200540049
00430055004c0041005200200050005500520050004f0053004500200041
004e00440020004e004f004e0049004e004600520049004e00470045004d
0045004e0054002e00200049004e0020004e004f0020004500560045004e
00540020005300480041004c004c00200054004800450020004100550054
0048004f005200530020004f005200200043004f00500059005200490047
0048005400200048004f004c00440045005200530020004200450020004c
004900410042004c004500200046004f005200200041004e005900200043
004c00410049004d002c002000440041004d00410047004500530020004f
00520020004f00540048004500520020004c0049004100420049004c0049
00540059002c0020005700480045005400480045005200200049004e0020
0041004e00200041004300540049004f004e0020004f004600200043004f
004e00540052004100430054002c00200054004f005200540020004f0052
0020004f00540048004500520057004900530045002c0020004100520049
00530049004e0047002000460052004f004d002c0020004f005500540020
004f00460020004f005200200049004e00200043004f004e004e00450043
00540049004f004e00200057004900540048002000540048004500200053
004f0046005400570041005200450020004f005200200054004800450020
0055005300450020004f00520020004f0054004800450052002000440045
0041004c0049004e0047005300200049004e002000540048004500200053
004f004600540057004100520045002e004e006f0072006d00610061006c
0069004e006f0072006d00e1006c004e006f0072006d0061006c00650053
00740061006e00640061006100720064004e006f0072006d0061006c006e
0079041e0431044b0447043d044b0439004e006f0072006d00e1006c006e
0065004e0061007600610064006e006f0074006801b001a10300006e0067
0041007200720075006e00740061410a005403ef02ad001d001f03ee03ed
003c001f03edb2061d1fb803ecb3032a1f3f411503e4006003e9009f03e5
00df03e50004001003e4001003e5003f03e5007003e400ff03e40005ffc0
03e1b345453240b803e1b32b2e3240b803e1b2282932b9ffc003e1b21a1c
32bd03e102ac0027001fffc003dfb2161b32b9ffc003deb2424232b9ffc0
03deb2363832b9ffc003deb32a2d32df410a03de00ef03de000203de03df
0028001fffc003dfb3282e32f0410d03df0001037e000f0101001f00a003
dd00b003dd0002004003dab32426329fbf03cc000103ca03c90064001fff
c003c9b20d1132410a03c703b70012001f03b603b50064001fffc003b5b3
0e1132004173038d000100c0038d00d0038d00e0038d00f0038d0004006f
03a7007f03a7008f03a700af03a70004000f03a7001f03a7002f03a7004f
03a7000403ab03ab00ef03a50001000f03a5002f03a5006f03a5008f03a5
0004005403aa0001006b03aa000103a8036a0022001f038c03940015001f
038b03930015001f03a40393001a001f03a20394001e001f03a10393001e
001f039f0394001e001f039b0394001a001f039a0393001e001f03990394
0016001f039803940016001f03970393001b001f03960394001b001f0395
0393001b001f03760375001a001f03740375001a001f03a00373b21e1f10
411e03930020039300300393000300200394003003940040039400030000
039400010383036c001e001f03b1036c0032001f036d036c0032001fffc0
037db2212332b9ffc0037db3171932a0410a037d00b0037d00c0037d00d0
037d0004ffc0037cb2212332b9ffc0037cb3171932a0412d037c00b0037c
00c0037c00d0037c00040030037300400373000200000373001003730020
0373000300e0037300f00373000200b0037300c0037300d0037300030084
03730090037300a0037300030377036a0029001f0389036ab2281f40b803
67b33940323fbb0366000100400366b3191d328fbb0366000100400366b3
090a3240b80366b3090e3240b80366b3090f323fbb0365000100400365b3
090c3240b80365b31a1d3240b80365b3090e326b410e0363007b03630002
0014036300240363003403630044036300040363b2242f1fba034e006d08
00400e1f7f027f037f047f050430440112bf033200500800001f0012032d
003c0800b61f5f3c013785a0418503620001000003620010036200700362
00900362000400f0035f00010020035e0020035f0030035f0040035e0004
0000035e0000035f0010035f00d0035e00e0035f00050010030f0020030f
0030030f00d0030f00e0030f00050000030f0010030f0050030f0060030f
0070030f00d0030f00060000030f0010030f0020030f0030030f00e0030f
00f0030f0006030f00270000030e0030030e000200e0030e00f0030e0002
030e004a00e0030d00f0030d0002030d002700d002fc0001001002fc0020
02fc005002fc000300d002fc00e002fc0002000002fc001002fc002002fc
003002fc005002fc006002fc000600e002fc00f002fc0002002002fc0030
02fc004002fc000302fc402c27c02901b02901a02901902901403c3f4132
40223f4132121212858f4caf4cbf4ccf4c045f4c6f4c7f4c0337b8ffc0b3
b22b3032b8ffc0b3b2222532b8ffc0b5b2191a32370f413b02af0001005f
02af009f02af00df02af0003001f02af002f02af003f02af006f02af0004
02af02af001f02ad002f02ad003f02ad004f02ad005f02ad000500df02ad
0001000f02ad001f02ad003f02ad005f02ad009f02ad0005005f02ad00df
02ad0002000f02ad001f02ad003f02ad0003004002acb23a334f414d02ac
005f02ac009f02ac0003002f02ac003f02ac0002000f02ac003f02ac00af
02ac000300b002ac00e002ac0002004f02ac005f02ac00a002ac0003001f
02ac002f02ac003f02ac0003000f02ac0001000f035a0001000f035a001f
035a003f035a005f035a0070035a000500cf035700df03570002000f0357
001f03570070035700af03570004035a035a0357035702ad02ad02ac02ac
032c400d31151f001616000000121108104110020c004a000d01a8004a00
0d0198004a000d0189004a000d013f004a000d0124400e4a0df64a0dbe4a
0d864a0d274a0dbe02280041000d01940041000d0121400b410db4410d4f
410d29410d411002170021000d02150021000d02060021000d01eb002100
0d014e0021000d012c4014210df9210df3210df1210d9d210d71210d3d21
0d4110021c001f000d0214001f000d020b001f000d0196001f000d014a00
1f000d0126400b1f0dc61f0d571f0d371f0d410d019e0141000d00420141
000d001e0141000d001b0141000d01f2b40f440f0009bb01f20044000d02
01b23c291fb80200b23c291fb801ffb23c411fb801feb23c471fb801fdb2
3c9e1fb801fab23c931fbc01f9010f0101001f01f6b224e41f411501f401
490401001f01f301490401001f01f1014900ab001f01f001490067001f01
a6003c0125001f01a4b23c811f411501a3010f019a001f01a20022080100
1f01a100500401001f019f0149019a001f019d01490067001f019cb22c62
1fb8019bb22c791fbc019a002c0101001f0197b22ce41fb80193b22c891f
b80192b22c6c1fb8018fb2259e1fb8016ab23c2a1f411101670024020100
1f0163002502ab001f014c010f019a001f01480149006c001f0147b22c89
1fb80145b22c9e1fb80144b22c791fb80143b223311fb80127b23c811fbc
012300500101001f011fb223e41f4115011d0023019a001f011c00230801
001f011b00250801001f010e010f0401001f010d00220401001f0108b223
811fb80106b425e41ff73cbb0125001f00f5010fb29e1fe3bc0149015600
1f00e20149b2ab1fd1b901490401b21fcf2cb80125b61fce23bb1fc524b8
0156b21fc02cb80801b21fbf2cb80201b51fb124e41fb0b901490201b61f
af2c671fad23b80801b21fa523b80201400b1f9f3c2d1f9b235a1f9925b8
0201b21f812cbc0401001f006d010f0156400b1f592c3e1f4c3cab1f4625
b80101b21f403cb80125400a1f3a23721f393cab1f38b80149b3ab1f3124
b80401b21f3025b802abb61f2a24e41f2623b80156b41f35555537ba0235
00070175402c0774076207560751073b0733072d0720071d071c07140812
0810080e080c080a080808060804080208000814b8ffe0402b0000010014
061000000100060400000100041000000100100200000100020000000100
0002010802004a00b013034b024b534201b0124b004b5442b0372b4bb807
ff52b0382b4bb008505b58b101018e59b0382bb00288b801005458b801ff
b101018e851bb0124358b90001012f858d1bb90001017c858d5959014bb0
c063004b6220b0f65323b8010a515ab0052342180016763f183f123e1139
46443e113946443e113946443e113946443e11394660443e11394660442b
2b2b2b2b2b2b2b2b2b2b182b2b2b2b2b2b2b2b2b2b2b2b2b181d42b0964b
5358b235aaaa1d4259b0324b5358b235ffff1d42594bb04753205c58b902
71026f4544b90270026f45445958b9017a0271455258b90271017a445959
4bb04753205c58b9002202704544b9003c027045445958b901b300224552
58b9002201b34459594bb04c53205c58b9014900224544b1222245445958
b901c20149455258b9014901c24459594bb06753205c58b9002402714544
b90050027145445958b9021e0024455258b90024021e4459594bb8020153
205c58b9010f00224544b1222245445958b90c00010f455258b9010f0c00
4459594bb01c53205c58b125254544b12c2545445958b13725455258b125
374459594bb0ab53205c58b125254544b1232545445958b9015900254552
58b9002501594459594bb8010153205c58b125254544b1282545445958b9
02080025455258b9002502084459592b2b2b2b2b2b2b2b2b2b2b2b2b2b2b
2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b
2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b
2b2b65422b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b
2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b01b361dc646345652345602345
6560234560b08b766818b080622020b164dc4565234520b0032660626368
20b003266165b0dc236544b064234420b161634565234520b00326606263
6820b003266165b063236544b0612344b10063455458b163406544b26140
614523614459b3a67f434b456523456023456560234560b089766818b080
622020b1437f4565234520b003266062636820b003266165b07f236544b0
43234420b1a64b4565234520b003266062636820b003266165b04b236544
b0a62344b1004b455458b14b406544b2a640a645236144594b5242014b50
58b108004259435c58b108004259b3020b0a124358601b2159421610703e
b0124358b93b21187e1bba040001a8000b2b59b00c2342b00d2342b01243
58b92d412d411bba04000400000b2b59b00e2342b00f2342b0124358b918
7e3b211bba01a80400000b2b59b0102342b0112342002b00184569444569
4445694445694473737374737373737475752b7373747475184569447373
742b4bb021534bb046515a58b03cb03c45b040604459012b2b2b2b75752b
5840365f235f255f285fa5046f236f256f286fa5044f234f254f284fa504
3f233f253f283fa5042f232f252f282fa5041f231f251f281fa504757575
7575755943584010bf3ccf3c026f3c7f3c8f3c9f3caf3c05757559435840
12bf22cf22025f226f227f228f229f22af2206757559435c58b6403c9f22
ef220375592b2b0174747474454473737474757545447345447374454473
747573737373732b5840246009700980090310092009300940095009056f
037f038f03031f032f033f034f035f0305b8ffc0b2073a33b8ffc0404606
3a33900ba00bb00bc00bd00b05b006c006d006e006f00605200630064006
50066006700680069006a006099006900702600b700b800b03100b200b30
0b400b500b051f070100757575737575752b2b757575751b40100706441f
0b0a441f0302441f0908441f2b2b2b2b592b752b435841220063032d0001
0003032d0013032d0023032d0033032d0053032d000500c3032d00d3032d
00e3032d00f3032d00040083032d0093032d00a3032d00b3032d0004032d
032d4518694474747575592b4358b900180332b330353238b80332b36166
3238b80332b3535a3238b80332b3454e3238b80332b33c413218b80332b2
3f330a410f0332000100ba033200ca033200da033200ea033200fa033200
05033203324518694474752b2b2b2b2b2b597300732b012b7575002b2b2b
74002b2b2b732b74012b002b2b017373737474732b2b00732b2b002b2b2b
017374732b012b2b012b2b2b2b2b2b2b2b2b2b2b2b2b2b00017375007373
004569440073730173742b2b2b2b2b732b00732b752b2b732b2b2b2b2b2b
2b2b2b73742b002b2b2b2b0000>
[16017 14165 ] AllocGlyphStorage
]def 
124 60 
PrepFor2015
Type42DictEnd
2 662 20 <000100f0000003060568001600b2b0852b58401440186018a018e0180400
1840180276008600020e411301690141000901a000220003016901410008
01a00023000001f8000f016900160141000001f2400e010f0f0209020105
09080c020300ba01f70003014940120e0e0f401135300f7f0f900fa00f04
0f1917ba022401e400182b4e10f45d2b3c4d10ede4103c003f3c3f3c1112
3901113900f5edfc01f52b2b3130005d01715d1bb4010507090ab803e2b2
6c090c00183f2b323f30315913253311141616171521353e023511342726
26232207f0014a21133c5cfe026038160a07251a254204c7a1fb8772381e
022525021d317a02dc942a201e1f>FBAAAA+TimesNewRomanPSMT AddT42Char 
2 0 0 <0002011c0000051c050000030007006cb0852b58b10201bb02be00060007
02bfb2000504b802beb403000a0704b802beb5010019080605bf02be0002
000301290009016b015e00182b10f63cfd3c4e10f43c4dfd3c003f3cfd3c
10fc3cfd3c31301bb10004b807d7b36c000107b807d7b16c0100182f2b2f
2b3031592111211125211121011c0400fc2003c0fc400500fb002004c000
>FBAAAA+TimesNewRomanPSMT AddT42Char 
FBAAAA+TimesNewRomanPSMT /CharStrings get begin
/g20 20 def
end
FBAAAA+TimesNewRomanPSMT /Encoding get
dup 49 /g20 put
pop
end
%ADOEndSubsetFont
/RVGGZC+TimesNewRomanPSMT /FBAAAA+TimesNewRomanPSMT findfont ct_VMDictPut
/RVGGZC+TimesNewRomanPSMT*1 
[49{/.notdef}rp /g20 206{/.notdef}rp]
RVGGZC+TimesNewRomanPSMT nf
RVGGZC+TimesNewRomanPSMT*1 [7.50449 0 0 -7.509 0 0 ]msf
469.839 527.897 mo
(1)sh
%ADOBeginSubsetFont: HBAAAA+TimesNewRomanPS-ItalicMT Initial
ct_T42Dict begin
-0.496 -0.305 1.332 1.023
 256 array 0 1 255 {1 index exch /.notdef put} for  /HBAAAA+TimesNewRomanPS-ItalicMT
Type42DictBegin
[<00010000000c000c000c000c4f532f3200000000000000cc000000566376
742008fab09e000001240000079c6670676d4d5f5868000008c000000634
676c796600000000000087300000101068656164ee7fc29e00000ef40000
0036686865610e31118b00000f2c00000024686d74780000000000000f50
00001d026c6f63610000000000002c5400001c4c6d61787013bf0cd70000
48a0000000206e616d651447e8f1000048c00000335370726570ab1cb91f
00007c1400000b1b67646972000000000000000000000000000100000190
000500080000000000000000000000000000000000000000000000000000
00000000000000000000000000080000000000000000000000000000f000
f0ff0000000000000000000000000001000000000000058e0000054c001f
054c001c037100180000ffe10000ffe80000ffe8fe4afffc056b0023fe68
ffe2033e00000095000000950000000000000000002500a8008e010b007d
00820045003200a400ca006b0070005100af003c00f001d7004700040025
00770029004000fd00160161004601370029008e0017ffca0025005bffe9
02e600020099008100f2007500d6006300c60006009a01330024003800cc
003dff67001305d8003600860095ffdb0007043400a500d8ffdcfffe0048
00a200d8013c01530380053e0057007a007c008c0117012a0138017c0026
003c007800bd00c0021009b5000c004d004e00540058006700b404010002
0005005000af01d5034300240058008b013501c0ffac002000250026002d
00410136022bffba001e002a0034003b003f00850094009800d7012e013d
033104b900170040006100b9010e0116012201bfff9c001f001f004d005c
0086008c009600aa00cb00cb011f0154022f036005a9fee8000e006f007c
007d008b00d500f1010a0157017802b803adfe3fff6affb3ffc4001f0037
003f0044004a0078007d009700a200a700b600c000c100c600d8011d0150
019701ee04740532fd81fed1fee0ff16fff1000f002d00550068006e007f
00890095009e00c200da00e400f801040108011101c2023002da030e049e
0517ff00ff8700000020002f00410057007800870088008800b900c200c5
012001280133017401d6020e020f026c027e02ab02ec038903b103e304e7
ff43ffa8ffc3ffdcffe9000700230023002600520077007d0081008f0099
00ac00ae00b500b800c800ea00f000f40135016a018b01b101b501f70214
02ad02d504fc05d805f0ff9dfffc000b00240025002c0030003000330040
004700490057006e009a00bd00c900cd00dc00fa00fa011b0139017e0187
018a018e0195019601df01f6028602cf02de039603a903b003c804010432
046a058b05e006510761fe96fe9aff4bff870013002500340038003e004a
0065006b0073007a009c00a200b200b700bf00f000f700fb010401130120
0124013b01520178017c0181018f01a001d90248026a026f02700301031d
032303270388041f04ab04d104da057a058bfe26fe59ff2e00010002000a
003b003b004700580058005f0066006b007a007a008b009900af00bc00c0
00c700cc00e900f200f500fb00fb0102010a010b01150121012701450145
015501570158015e01610168017d01a301ab01da01ee021002180222028f
029402a302d202e703710393039b03b303d303fe04ff050b05320532054b
0559058b05ab05f2065506890742076207a708ccfd2afdc8fddefe0cfe15
fe27fe53fe84febbff58ff76ff77ffa1ffa7ffadffafffc0000000000003
0094001d001f002000200027002e0048004b004c005e005f006b0071007c
008a00900091009100a700af00b300b400c400c600d100d200de00df00df
00e600e800ea00eb00f200f500f500fc010201180123013101330137015c
016201660170017a017a017a018201980199019b01b001bf01c001ca01d3
01d701d801e001e001f601f701f802120213022f023702440247024f0252
026302650270027f0298029b02a602b702ba02c502cf02d602d702e502fe
031c031d03450348035d035e03710379038103a103b703d403d503d803e1
03f803fe0404041f042104230425043a0467048304e00528054b0564056a
059f059f05c2060b066a06af06b306cb06e8070607280748075007a607b2
07ff009500af00920096000000000000000000000000017e01a80129025b
0212020301c302b4019301cd02b204ed020e0159017a0300022d042c00c8
004d00e602890325013e0378011b00f1018d00490203007c000e029d0247
0024000000000052004400330038005405d3041501a70000028601680050
00cf0002004b0024008800ba0025ffd800110091ff6b00b5011700260065
ff9900490080014b01c000f40167027102ea04fc0310017c01e103d90155
01e601ee0434019606cb005c022b0099003d009f00160039002700de0079
0120022e005a00990388009400210019002a046c05e8000001f203b200aa
0296028902b4ffc9020000ec0005005a0447010004e00000052a001f01eb
00ae016800ca02d3028901b5040601a1014f014b011c0308005e00c70024
029d006503750104028002f304d800d90239025a032c01f2043103030050
02e50283005901eb010800ac019602f8012100950180004400e501eb02e5
007400f301ff02fd038f026801c801c70116022b0142033000fe02e10162
0200002400ee05170108023700660006010201e602aa0366019b00d305c2
03dc044d03b6000401be013702fc03200244014d0338ffed002506f8030d
fed5ff43004402ffff92040bfdef0155017100d9ffc4032d0461044afbb5
fbcf02170192036d0558fff2fe7d0583023e006605e9073d007902430025
00cf00fd00af002a01ef021a0026001f0025003a000001170490fbfb0251
001d02f001f50078018f005f00240044005400bf00af006701a800260005
0006003f009800fa02ab00c2004d0375004a00b600c401bf017c006f0013
0263000c006801520002012e0104001f001f009a000000f1046900790080
005000bd056b00ab0080001e05a5fe4000ce006e0056004800db018b00b3
004802390458005300820082002203d703f1047040425554403f3e3d3c3b
3a3938373534333231302f2e2d2c2b2a292827262524232221201f1e1d1c
1b1a191817161514131211100f0e0d0c0b0a090807060504030201002c45
23466020b02660b004262348482d2c452346236120b02661b00426234848
2d2c45234660b0206120b04660b004262348482d2c4523462361b0206020
b02661b02061b004262348482d2c45234660b0406120b06660b004262348
482d2c4523462361b0406020b02661b04061b004262348482d2c0110203c
003c2d2c20452320b0cd442320b8015a51582320b08d44235920b0ed5158
2320b04d44235920b09051582320b00d44235921212d2c20204518684420
b001602045b04676688a4560442d2c01b10b0a432343650a2d2c00b10a0b
4323430b2d2c00b0172370b101173e01b0172370b10217453ab10200080d
2d2c45b01a234445b01923442d2c2045b00325456164b050515845441b21
21592d2cb00143632362b0002342b00f2b2d2c2045b0004360442d2c01b0
0643b00743650a2d2c2069b04061b0008b20b12cc08a8cb8100062602b0c
642364615c58b00361592d2c45b0112bb0172344b0177ae4182d2c45b011
2bb01723442d2cb01243588745b0112bb0172344b0177ae41b038a451869
20b01723448a8a8720b0a05158b0112bb0172344b0177ae41b21b0177ae4
5959182d2c2d2cb0022546608a46b040618c482d2c01182f2d2c20b00325
45b019234445b01a23444565234520b00325606a20b009234223688a6a60
6120b01a8ab000527921b21a1a40b9ffe0001a45208a54582321b03f1b23
5961441cb114008a5279b31940201945208a54582321b03f1b235961442d
2cb110114323430b2d2cb10e0f4323430b2d2cb10c0d4323430b2d2cb10c
0d432343650b2d2cb10e0f432343650b2d2cb11011432343650b2d2c4b52
5845441b2121592d2c0120b003252349b04060b0206320b000525823b002
253823b002256538008a63381b212121212159012d2c4bb06451584569b0
0943608a103a1b212121592d2c01b005251023208af500b0016023edec2d
2c01b005251023208af500b0016123edec2d2c01b0062510f500edec2d2c
20b001600110203c003c2d2c20b001610110203c003c2d2cb02b2bb02a2a
2d2c00b00743b006430b2d2c3eb02a2a2d2c352d2c76b802ee23701020b8
02ee4520b0005058b00161593a2f182d2c21210c6423648bb84000622d2c
21b08051580c6423648bb82000621bb200402f2b59b002602d2c21b0c051
580c6423648bb81555621bb200802f2b59b002602d2c0c6423648bb84000
626023212d2cb4000100000015b00826b00826b00826b008260f10161345
683ab001162d2cb4000100000015b00826b00826b00826b008260f101613
4568653ab001162d2c4b53234b515a5820458a60441b2121592d2c4b5458
20458a60441b2121592d2c4b53234b515a58381b2121592d2c4b5458381b
2121592d2cb0134358031b02592d2cb0134358021b03592d2c4b54b01243
5c5a58381b2121592d2cb012435c580cb00425b00425060c6423646164b8
07085158b00425b00425012046b01060482046b0106048590a21211b2121
592d2cb012435c580cb00425b00425060c6423646164b807085158b00425
b00425012046b8fff060482046b8fff06048590a21211b2121592d2c4b53
234b515a58b03a2b1b2121592d2c4b53234b515a58b03b2b1b2121592d2c
4b53234b515ab012435c5a58381b2121592d2c0c8a034b54b00426024b54
5a8a8a0ab012435c5a58381b2121592d2c462346608a8a462320468a608a
61b8ff8062232010238ab903b003b08a70456020b0005058b00161b8ffba
8b1bb0468c59b0106068013a2d2cb1020042b123018851b1400188535a58
b910000020885458b202010243604259b12401885158b920000040885458
b2020202436042b12401885458b2022002436042004b014b5258b2020802
436042591bb940000080885458b202040243604259b94000008063b80100
885458b202080243604259b94000010063b80200885458b2021002436042
59b12601885158b94000020063b80400885458b202400243604259b94000
040063b80800885458b202800243604259b12801885158b94000080063b8
1000885458ba000201000002436042595959595959592d2cb0024354584b
53234b515a58381b2121591b21212121592d00010000000707aeb1b0afba
5f0f3cf50819080000000000a31fb8bd00000000dd7cb779fc05fd8c0aaa
0830000200090001000000000000000100000721fe4500570ab9fc05fa50
0aaa00180007000000000000000000000000005a0639011c0639011c0639
011c0639011c0639011c0639011c0639011c0639011c0639011c0639011c
0639011c0639011c0639011c0639011c0639011c0639011c0639011c0639
011c0639011c0639011c0639011c0639011c0639011c0639011c0639011c
0639011c0639011c0639011c0639011c0639011c0639011c0639011c0639
011c0639011c0639011c0639011c0639011c0639011c0556008a0556008a
0556008a0556008a0556008a0556008a0556008a0556008a0556008a0473
ffbf0473ffbf0473ffbf0473ffbf0473ffbf0473ffbf0473ffbf0400000e
0400000e0400000e0400000e0400000e0400000e0400000e0400000e0400
000e0400000e0400000e0400000e0400000e0400000e0400000e0400000e
0400000e0400000e0400000e0400000e0400000e0400000e023900580239
fea10239fea10239fea105c7002305c7002305c7002305c7002305c70023
05c7002305c700230239005402390054038d002c002cffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9ffb9
ffb9ffb9ffb9000000000034003400340034003400340034003400340034
003400340034003400340034003400340034003400340034003400340034
003400340034003400340034003400340034003400340034003400b900b9
00b900b900b900b900b900b900b9017e017e017e017e017e017e017e027e
027e027e027e027e027e027e027e027e027e027e027e027e027e027e027e
027e027e027e027e027e027e0350040d040d040d05aa05aa05aa05aa05aa
05aa05aa06600660071b071b080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
080808080808080808080808080808080808080808080808080808080808
08080808080808080808080808080808080808080808000100000e2500f2
003c0097000600020010002f0056000004ed0b1b000400020000005303ea
0000000300000000021a00000000000300000001001e021a000000030000
0002000c02380000000300000003005602440000000300000004002c0256
00000003000000050018029a0000000300000006003002b2000000030000
0007007602e200000003000000080030000e000000030000000900860358
000000030000000d0e0403de0001000000000000010d11e2000100000000
0001000f12ef0001000000000002000612fe0001000000000003002b1304
00010000000000040016130d0001000000000005000c132f000100000000
00060018133b0001000000000007003b13530001000000000008001811e9
00010000000000090043138e000100000000000d070213d1000300010403
0002000e1ad30003000104030004002e1ae10003000104050002000e1b0f
0003000104050004002e1b1d0003000104060002000c1b4b000300010406
0004002c1b570003000104070002000c1b830003000104070004002c1b8f
0003000104080002000c1bbb0003000104080004002c1bc7000300010409
000002221bf30003000104090001001e021a0003000104090002000c0238
0003000104090003005602440003000104090004002c0256000300010409
00050018029a0003000104090006003002b20003000104090007007602e2
00030001040900080030000e000300010409000900860358000300010409
000d0e141e1500030001040a0002000e2c2900030001040a0004002e2c37
00030001040b000200142c6500030001040b000400342c7900030001040c
000200102cad00030001040c000400302cbd00030001040e000200082ced
00030001040e000400282cf50003000104100002000e2d1d000300010410
0004002e2d2b0003000104130002000e2d590003000104130004002e2d67
0003000104140002000c1b830003000104140004002c1b8f000300010415
0002000e2d950003000104150004002e2da30003000104160002000e2dd1
0003000104160004002e2ddf0003000104190002000c2e0d000300010419
0004002c2e1900030001041b0002000e2e4500030001041b0004002e2e53
00030001041d0002000c1b8300030001041d0004002c1b8f00030001041f
0002000c2e8100030001041f0004002c2e8d0003000104240002000e2eb9
0003000104240004002e2ec700030001042a0002000e2ef500030001042a
0004002e2f0300030001042d0002000c2f3100030001042d0004002c2f3d
00030001080a0002000e2c2900030001080a0004002e2c37000300010816
0002000e2dd10003000108160004002e2ddf000300010c0a0002000e2c29
000300010c0a0004002e2c37000300010c0c000200102cad000300010c0c
000400302cbd00a90020003200300032003000200054006800650020004d
006f006e006f007400790070006500200043006f00720070006f00720061
00740069006f006e002e00200041006c006c002000520069006700680074
0073002000520065007300650072007600650064002e0020000d000d0048
006500620072006500770020004f00700065006e00540079007000650020
004c00610079006f007500740020006c006f00670069006300200063006f
0070007900720069006700680074002000a9002000320030003000330020
002600200032003000300037002c002000520061006c0070006800200048
0061006e0063006f0063006b002000260020004a006f0068006e00200048
007500640073006f006e002e002000540068006900730020006c00610079
006f007500740020006c006f00670069006300200066006f007200200042
00690062006c006900630061006c00200048006500620072006500770020
006900730020006f00700065006e00200073006f00750072006300650020
0073006f00660074007700610072006500200075006e0064006500720020
0074006800650020004d004900540020004c006900630065006e00730065
003b002000730065006500200065006d0062006500640064006500640020
006c006900630065006e0073006500200064006500730063007200690070
00740069006f006e00200066006f0072002000640065007400610069006c
0073002e00540069006d006500730020004e0065007700200052006f006d
0061006e004900740061006c00690063004d006f006e006f007400790070
0065003a00540069006d006500730020004e0065007700200052006f006d
0061006e0020004900740061006c0069006300200028004d006900630072
006f0073006f00660074002900560065007200730069006f006e00200037
002e0030003300540069006d00650073004e006500770052006f006d0061
006e00500053002d004900740061006c00690063004d005400540069006d
006500730020004e0065007700200052006f006d0061006e002000690073
00200061002000740072006100640065006d00610072006b0020006f0066
00200054006800650020004d006f006e006f007400790070006500200043
006f00720070006f0072006100740069006f006e002e004d006f006e006f
007400790070006500200054007900700065002000440072006100770069
006e00670020004f006600660069006300650020002d0020005300740061
006e006c006500790020004d006f007200690073006f006e002c00200056
006900630074006f00720020004c0061007200640065006e007400200031
003900330032004d006900630072006f0073006f00660074002000730075
00700070006c00690065006400200066006f006e0074002e00200059006f
00750020006d006100790020007500730065002000740068006900730020
0066006f006e007400200074006f0020006300720065006100740065002c
00200064006900730070006c00610079002c00200061006e006400200070
00720069006e007400200063006f006e00740065006e0074002000610073
0020007000650072006d0069007400740065006400200062007900200074
006800650020006c006900630065006e007300650020007400650072006d
00730020006f00720020007400650072006d00730020006f006600200075
00730065002c0020006f006600200074006800650020004d006900630072
006f0073006f00660074002000700072006f0064007500630074002c0020
0073006500720076006900630065002c0020006f007200200063006f006e
00740065006e007400200069006e00200077006800690063006800200074
00680069007300200066006f006e0074002000770061007300200069006e
0063006c0075006400650064002e00200059006f00750020006d00610079
0020006f006e006c0079002000280069002900200065006d006200650064
0020007400680069007300200066006f006e007400200069006e00200063
006f006e00740065006e00740020006100730020007000650072006d0069
0074007400650064002000620079002000740068006500200065006d0062
0065006400640069006e0067002000720065007300740072006900630074
0069006f006e007300200069006e0063006c007500640065006400200069
006e0020007400680069007300200066006f006e0074003b00200061006e
006400200028006900690029002000740065006d0070006f007200610072
0069006c007900200064006f0077006e006c006f00610064002000740068
0069007300200066006f006e007400200074006f00200061002000700072
0069006e0074006500720020006f00720020006f00740068006500720020
006f00750074007000750074002000640065007600690063006500200074
006f002000680065006c00700020007000720069006e007400200063006f
006e00740065006e0074002e00200041006e00790020006f007400680065
00720020007500730065002000690073002000700072006f006800690062
0069007400650064002e000d000d00540068006500200066006f006c006c
006f00770069006e00670020006c006900630065006e00730065002c0020
006200610073006500640020006f006e00200074006800650020004d0049
00540020006c006900630065006e00730065002000280068007400740070
003a002f002f0065006e002e00770069006b006900700065006400690061
002e006f00720067002f00770069006b0069002f004d00490054005f004c
006900630065006e007300650029002c0020006100700070006c00690065
007300200074006f00200074006800650020004f00700065006e00540079
007000650020004c00610079006f007500740020006c006f006700690063
00200066006f00720020004200690062006c006900630061006c00200048
006500620072006500770020201c004c00610079006f007500740020004c
006f006700690063201d0020006100730020006a006f0069006e0074006c
007900200064006500760065006c006f0070006500640020006200790020
00520061006c00700068002000480061006e0063006f0063006b00200061
006e00640020004a006f0068006e00200048007500640073006f006e002e
0020000d000d005000650072006d0069007300730069006f006e00200069
007300200068006500720065006200790020006700720061006e00740065
0064002c002000660072006500650020006f006600200063006800610072
00670065002c00200074006f00200061006e007900200070006500720073
006f006e0020006f0062007400610069006e0069006e0067002000610020
0063006f007000790020006f006600200074006800650020004f00700065
006e00540079007000650020004c00610079006f007500740020006c006f
00670069006300200066006f00720020004200690062006c006900630061
006c002000480065006200720065007700200061006e0064002000610073
0073006f00630069006100740065006400200064006f00630075006d0065
006e0074006100740069006f006e002000660069006c0065007300200028
0074006800650020201c004c00610079006f007500740020004c006f0067
0069006300200053006f006600740077006100720065201d0029002c0020
0074006f0020006400650061006c00200069006e00200074006800650020
004c00610079006f007500740020004c006f00670069006300200053006f
00660074007700610072006500200077006900740068006f007500740020
007200650073007400720069006300740069006f006e002c00200069006e
0063006c007500640069006e006700200077006900740068006f00750074
0020006c0069006d00690074006100740069006f006e0020007400680065
002000720069006700680074007300200074006f0020007500730065002c
00200063006f00700079002c0020006d006f0064006900660079002c0020
006d0065007200670065002c0020007000750062006c006900730068002c
00200064006900730074007200690062007500740065002c002000730075
0062006c006900630065006e00730065002c00200061006e0064002f006f
0072002000730065006c006c00200063006f00700069006500730020006f
006600200074006800650020004c00610079006f007500740020004c006f
00670069006300200053006f006600740077006100720065002c00200061
006e006400200074006f0020007000650072006d00690074002000700065
00720073006f006e007300200074006f002000770068006f006d00200074
006800650020004c00610079006f007500740020004c006f006700690063
00200053006f006600740077006100720065002000690073002000660075
0072006e0069007300680065006400200074006f00200064006f00200073
006f002c0020007300750062006a00650063007400200074006f00200074
0068006500200066006f006c006c006f00770069006e006700200063006f
006e0064006900740069006f006e0073003a000d000d0054006800650020
00610062006f0076006500200063006f0070007900720069006700680074
0020006e006f007400690063006500200061006e00640020007400680069
00730020007000650072006d0069007300730069006f006e0020006e006f
00740069006300650020007300680061006c006c00200062006500200069
006e0063006c007500640065006400200069006e00200061006c006c0020
0063006f00700069006500730020006f0072002000730075006200730074
0061006e007400690061006c00200070006f007200740069006f006e0073
0020006f006600200074006800650020004c00610079006f007500740020
004c006f00670069006300200053006f006600740077006100720065002e
000d000d00540048004500200053004f0046005400570041005200450020
00490053002000500052004f005600490044004500440020002700410053
0020004900530027002c00200057004900540048004f0055005400200057
0041005200520041004e005400590020004f004600200041004e00590020
004b0049004e0044002c002000450058005000520045005300530020004f
005200200049004d0050004c004900450044002c00200049004e0043004c
005500440049004e004700200042005500540020004e004f00540020004c
0049004d004900540045004400200054004f002000540048004500200057
0041005200520041004e00540049004500530020004f00460020004d0045
0052004300480041004e0054004100420049004c004900540059002c0020
004600490054004e00450053005300200046004f00520020004100200050
004100520054004900430055004c0041005200200050005500520050004f
0053004500200041004e00440020004e004f004e0049004e004600520049
004e00470045004d0045004e0054002e00200049004e0020004e004f0020
004500560045004e00540020005300480041004c004c0020005400480045
00200041005500540048004f005200530020004f005200200043004f0050
00590052004900470048005400200048004f004c00440045005200530020
004200450020004c004900410042004c004500200046004f005200200041
004e005900200043004c00410049004d002c002000440041004d00410047
004500530020004f00520020004f00540048004500520020004c00490041
00420049004c004900540059002c00200057004800450054004800450052
00200049004e00200041004e00200041004300540049004f004e0020004f
004600200043004f004e00540052004100430054002c00200054004f0052
00540020004f00520020004f00540048004500520057004900530045002c
002000410052004900530049004e0047002000460052004f004d002c0020
004f005500540020004f00460020004f005200200049004e00200043004f
004e004e0045004300540049004f004e0020005700490054004800200054
0048004500200053004f0046005400570041005200450020004f00520020
00540048004500200055005300450020004f00520020004f005400480045
00520020004400450041004c0049004e0047005300200049004e00200054
0048004500200053004f004600540057004100520045002ea92032303230
20546865204d6f6e6f7479706520436f72706f726174696f6e2e20416c6c
205269676874732052657365727665642e200d0d486562726577204f7065
6e54797065204c61796f7574206c6f67696320636f7079726967687420a9
2032303033202620323030372c2052616c70682048616e636f636b202620
4a6f686e20487564736f6e2e2054686973206c61796f7574206c6f676963
20666f72204269626c6963616c20486562726577206973206f70656e2073
6f7572636520736f66747761726520756e64657220746865204d4954204c
6963656e73653b2073656520656d626564646564206c6963656e73652064
65736372697074696f6e20666f722064657461696c732e54696d6573204e
657720526f6d616e4974616c69634d6f6e6f747970653a54696d6573204e
657720526f6d616e204974616c696320284d6963726f736f667429566572
73696f6e20372e303354696d65734e6577526f6d616e50532d4974616c69
634d5454696d6573204e657720526f6d616e20697320612074726164656d
61726b206f6620546865204d6f6e6f7479706520436f72706f726174696f
6e2e4d6f6e6f7479706520547970652044726177696e67204f6666696365
202d205374616e6c6579204d6f7269736f6e2c20566963746f72204c6172
64656e7420313933324d6963726f736f667420737570706c69656420666f
6e742e20596f75206d617920757365207468697320666f6e7420746f2063
72656174652c20646973706c61792c20616e64207072696e7420636f6e74
656e74206173207065726d697474656420627920746865206c6963656e73
65207465726d73206f72207465726d73206f66207573652c206f66207468
65204d6963726f736f66742070726f647563742c20736572766963652c20
6f7220636f6e74656e7420696e207768696368207468697320666f6e7420
77617320696e636c756465642e20596f75206d6179206f6e6c7920286929
20656d626564207468697320666f6e7420696e20636f6e74656e74206173
207065726d69747465642062792074686520656d62656464696e67207265
737472696374696f6e7320696e636c7564656420696e207468697320666f
6e743b20616e6420286969292074656d706f726172696c7920646f776e6c
6f6164207468697320666f6e7420746f2061207072696e746572206f7220
6f74686572206f75747075742064657669636520746f2068656c70207072
696e7420636f6e74656e742e20416e79206f746865722075736520697320
70726f686962697465642e0d0d54686520666f6c6c6f77696e67206c6963
656e73652c206261736564206f6e20746865204d4954206c6963656e7365
2028687474703a2f2f656e2e77696b6970656469612e6f72672f77696b69
2f4d49545f4c6963656e7365292c206170706c69657320746f2074686520
4f70656e54797065204c61796f7574206c6f67696320666f72204269626c
6963616c2048656272657720d24c61796f7574204c6f676963d320617320
6a6f696e746c7920646576656c6f7065642062792052616c70682048616e
636f636b20616e64204a6f686e20487564736f6e2e200d0d5065726d6973
73696f6e20697320686572656279206772616e7465642c2066726565206f
66206368617267652c20746f20616e7920706572736f6e206f627461696e
696e67206120636f7079206f6620746865204f70656e54797065204c6179
6f7574206c6f67696320666f72204269626c6963616c2048656272657720
616e64206173736f63696174656420646f63756d656e746174696f6e2066
696c6573202874686520d24c61796f7574204c6f67696320536f66747761
7265d3292c20746f206465616c20696e20746865204c61796f7574204c6f
67696320536f66747761726520776974686f757420726573747269637469
6f6e2c20696e636c7564696e6720776974686f7574206c696d6974617469
6f6e207468652072696768747320746f207573652c20636f70792c206d6f
646966792c206d657267652c207075626c6973682c206469737472696275
74652c207375626c6963656e73652c20616e642f6f722073656c6c20636f
70696573206f6620746865204c61796f7574204c6f67696320536f667477
6172652c20616e6420746f207065726d697420706572736f6e7320746f20
77686f6d20746865204c61796f7574204c6f67696320536f667477617265
206973206675726e697368656420746f20646f20736f2c207375626a6563
7420746f2074686520666f6c6c6f77696e6720636f6e646974696f6e733a
0d0d5468652061626f766520636f70797269676874206e6f746963652061
6e642074686973207065726d697373696f6e206e6f74696365207368616c
6c20626520696e636c7564656420696e20616c6c20636f70696573206f72
207375627374616e7469616c20706f7274696f6e73206f6620746865204c
61796f7574204c6f67696320536f6674776172652e0d0d54484520534f46
54574152452049532050524f564944454420274153204953272c20574954
484f55542057415252414e5459204f4620414e59204b494e442c20455850
52455353204f5220494d504c4945442c20494e434c5544494e4720425554
204e4f54204c494d4954454420544f205448452057415252414e54494553
204f46204d45524348414e544142494c4954592c204649544e4553532046
4f52204120504152544943554c415220505552504f534520414e44204e4f
4e494e4652494e47454d454e542e20494e204e4f204556454e5420534841
4c4c2054484520415554484f5253204f5220434f5059524947485420484f
4c44455253204245204c4941424c4520464f5220414e5920434c41494d2c
2044414d41474553204f52204f54484552204c494142494c4954592c2057
48455448455220494e20414e20414354494f4e204f4620434f4e54524143
542c20544f5254204f52204f54484552574953452c2041524953494e4720
46524f4d2c204f5554204f46204f5220494e20434f4e4e454354494f4e20
574954482054484520534f465457415245204f522054484520555345204f
52204f54484552204445414c494e475320494e2054484520534f46545741
52452e006300750072007300690076006100540069006d00650073002000
4e0065007700200052006f006d0061006e00200063007500720073006900
760061006b00750072007a00ed0076006100540069006d00650073002000
4e0065007700200052006f006d0061006e0020006b00750072007a00ed00
760061006b0075007200730069007600540069006d006500730020004e00
65007700200052006f006d0061006e0020006b0075007200730069007600
4b0075007200730069007600540069006d006500730020004e0065007700
200052006f006d0061006e0020004b0075007200730069007603a003bb03
ac03b303b903b100540069006d006500730020004e006500770020005200
6f006d0061006e002003a003bb03ac03b303b903b100a900200032003000
32003000200054006800650020004d006f006e006f007400790070006500
200043006f00720070006f0072006100740069006f006e002e0020004100
6c006c002000520069006700680074007300200052006500730065007200
7600650064002e0020000d000a000d000a00480065006200720065007700
20004f00700065006e00540079007000650020004c00610079006f007500
740020006c006f00670069006300200063006f0070007900720069006700
680074002000a90020003200300030003300200026002000320030003000
37002c002000520061006c00700068002000480061006e0063006f006300
6b002000260020004a006f0068006e00200048007500640073006f006e00
2e002000540068006900730020006c00610079006f007500740020006c00
6f00670069006300200066006f00720020004200690062006c0069006300
61006c00200048006500620072006500770020006900730020006f007000
65006e00200073006f007500720063006500200073006f00660074007700
610072006500200075006e00640065007200200074006800650020004d00
4900540020004c006900630065006e00730065003b002000730065006500
200065006d0062006500640064006500640020006c006900630065006e00
7300650020006400650073006300720069007000740069006f006e002000
66006f0072002000640065007400610069006c0073002e000d000a004d00
6900630072006f0073006f0066007400200073007500700070006c006900
65006400200066006f006e0074002e00200059006f00750020006d006100
7900200075007300650020007400680069007300200066006f006e007400
200074006f0020006300720065006100740065002c002000640069007300
70006c00610079002c00200061006e00640020007000720069006e007400
200063006f006e00740065006e0074002000610073002000700065007200
6d0069007400740065006400200062007900200074006800650020006c00
6900630065006e007300650020007400650072006d00730020006f007200
20007400650072006d00730020006f00660020007500730065002c002000
6f006600200074006800650020004d006900630072006f0073006f006600
74002000700072006f0064007500630074002c0020007300650072007600
6900630065002c0020006f007200200063006f006e00740065006e007400
200069006e00200077006800690063006800200074006800690073002000
66006f006e0074002000770061007300200069006e0063006c0075006400
650064002e00200059006f00750020006d006100790020006f006e006c00
79002000280069002900200065006d006200650064002000740068006900
7300200066006f006e007400200069006e00200063006f006e0074006500
6e00740020006100730020007000650072006d0069007400740065006400
2000620079002000740068006500200065006d0062006500640064006900
6e00670020007200650073007400720069006300740069006f006e007300
200069006e0063006c007500640065006400200069006e00200074006800
69007300200066006f006e0074003b00200061006e006400200028006900
690029002000740065006d0070006f0072006100720069006c0079002000
64006f0077006e006c006f00610064002000740068006900730020006600
6f006e007400200074006f002000610020007000720069006e0074006500
720020006f00720020006f00740068006500720020006f00750074007000
750074002000640065007600690063006500200074006f00200068006500
6c00700020007000720069006e007400200063006f006e00740065006e00
74002e00200041006e00790020006f007400680065007200200075007300
65002000690073002000700072006f006800690062006900740065006400
2e000d000a000d000a00540068006500200066006f006c006c006f007700
69006e00670020006c006900630065006e00730065002c00200062006100
73006500640020006f006e00200074006800650020004d00490054002000
6c006900630065006e00730065002000280068007400740070003a002f00
2f0065006e002e00770069006b006900700065006400690061002e006f00
720067002f00770069006b0069002f004d00490054005f004c0069006300
65006e007300650029002c0020006100700070006c006900650073002000
74006f00200074006800650020004f00700065006e005400790070006500
20004c00610079006f007500740020006c006f0067006900630020006600
6f00720020004200690062006c006900630061006c002000480065006200
72006500770020201c004c00610079006f007500740020004c006f006700
690063201d0020006100730020006a006f0069006e0074006c0079002000
64006500760065006c006f00700065006400200062007900200052006100
6c00700068002000480061006e0063006f0063006b00200061006e006400
20004a006f0068006e00200048007500640073006f006e002e0020000d00
0a000d000a005000650072006d0069007300730069006f006e0020006900
7300200068006500720065006200790020006700720061006e0074006500
64002c002000660072006500650020006f00660020006300680061007200
670065002c00200074006f00200061006e00790020007000650072007300
6f006e0020006f0062007400610069006e0069006e006700200061002000
63006f007000790020006f006600200074006800650020004f0070006500
6e00540079007000650020004c00610079006f007500740020006c006f00
670069006300200066006f00720020004200690062006c00690063006100
6c002000480065006200720065007700200061006e006400200061007300
73006f00630069006100740065006400200064006f00630075006d006500
6e0074006100740069006f006e002000660069006c006500730020002800
74006800650020201c004c00610079006f007500740020004c006f006700
69006300200053006f006600740077006100720065201d0029002c002000
74006f0020006400650061006c00200069006e0020007400680065002000
4c00610079006f007500740020004c006f00670069006300200053006f00
660074007700610072006500200077006900740068006f00750074002000
7200650073007400720069006300740069006f006e002c00200069006e00
63006c007500640069006e006700200077006900740068006f0075007400
20006c0069006d00690074006100740069006f006e002000740068006500
2000720069006700680074007300200074006f0020007500730065002c00
200063006f00700079002c0020006d006f0064006900660079002c002000
6d0065007200670065002c0020007000750062006c006900730068002c00
200064006900730074007200690062007500740065002c00200073007500
62006c006900630065006e00730065002c00200061006e0064002f006f00
72002000730065006c006c00200063006f00700069006500730020006f00
6600200074006800650020004c00610079006f007500740020004c006f00
670069006300200053006f006600740077006100720065002c0020006100
6e006400200074006f0020007000650072006d0069007400200070006500
720073006f006e007300200074006f002000770068006f006d0020007400
6800650020004c00610079006f007500740020004c006f00670069006300
200053006f00660074007700610072006500200069007300200066007500
72006e0069007300680065006400200074006f00200064006f0020007300
6f002c0020007300750062006a00650063007400200074006f0020007400
68006500200066006f006c006c006f00770069006e006700200063006f00
6e0064006900740069006f006e0073003a000d000a000d000a0054006800
65002000610062006f0076006500200063006f0070007900720069006700
6800740020006e006f007400690063006500200061006e00640020007400
68006900730020007000650072006d0069007300730069006f006e002000
6e006f00740069006300650020007300680061006c006c00200062006500
200069006e0063006c007500640065006400200069006e00200061006c00
6c00200063006f00700069006500730020006f0072002000730075006200
7300740061006e007400690061006c00200070006f007200740069006f00
6e00730020006f006600200074006800650020004c00610079006f007500
740020004c006f00670069006300200053006f0066007400770061007200
65002e000d000a000d000a00540048004500200053004f00460054005700
4100520045002000490053002000500052004f0056004900440045004400
200027004100530020004900530027002c00200057004900540048004f00
550054002000570041005200520041004e005400590020004f0046002000
41004e00590020004b0049004e0044002c00200045005800500052004500
5300530020004f005200200049004d0050004c004900450044002c002000
49004e0043004c005500440049004e004700200042005500540020004e00
4f00540020004c0049004d004900540045004400200054004f0020005400
480045002000570041005200520041004e00540049004500530020004f00
460020004d00450052004300480041004e0054004100420049004c004900
540059002c0020004600490054004e00450053005300200046004f005200
20004100200050004100520054004900430055004c004100520020005000
5500520050004f0053004500200041004e00440020004e004f004e004900
4e004600520049004e00470045004d0045004e0054002e00200049004e00
20004e004f0020004500560045004e00540020005300480041004c004c00
2000540048004500200041005500540048004f005200530020004f005200
200043004f005000590052004900470048005400200048004f004c004400
45005200530020004200450020004c004900410042004c00450020004600
4f005200200041004e005900200043004c00410049004d002c0020004400
41004d00410047004500530020004f00520020004f005400480045005200
20004c0049004100420049004c004900540059002c002000570048004500
5400480045005200200049004e00200041004e0020004100430054004900
4f004e0020004f004600200043004f004e00540052004100430054002c00
200054004f005200540020004f00520020004f0054004800450052005700
4900530045002c002000410052004900530049004e004700200046005200
4f004d002c0020004f005500540020004f00460020004f00520020004900
4e00200043004f004e004e0045004300540049004f004e00200057004900
540048002000540048004500200053004f00460054005700410052004500
20004f0052002000540048004500200055005300450020004f0052002000
4f00540048004500520020004400450041004c0049004e00470053002000
49004e002000540048004500200053004f00460054005700410052004500
2e004300750072007300690076006100540069006d006500730020004e00
65007700200052006f006d0061006e002000430075007200730069007600
61004b00750072007300690076006f00690074007500540069006d006500
730020004e0065007700200052006f006d0061006e0020004b0075007200
7300690076006f006900740075004900740061006c006900710075006500
540069006d006500730020004e0065007700200052006f006d0061006e00
20004900740061006c006900710075006500440151006c00740054006900
6d006500730020004e0065007700200052006f006d0061006e0020004401
51006c00740043006f0072007300690076006f00540069006d0065007300
20004e0065007700200052006f006d0061006e00200043006f0072007300
690076006f004300750072007300690065006600540069006d0065007300
20004e0065007700200052006f006d0061006e0020004300750072007300
6900650066006b00750072007300790077006100540069006d0065007300
20004e0065007700200052006f006d0061006e0020006b00750072007300
79007700610049007400e1006c00690063006f00540069006d0065007300
20004e0065007700200052006f006d0061006e00200049007400e1006c00
690063006f041a0443044004410438043200540069006d00650073002000
4e0065007700200052006f006d0061006e0020041a044304400441043804
32004b00750072007a00ed0076006100540069006d006500730020004e00
65007700200052006f006d0061006e0020004b00750072007a00ed007600
61013000740061006c0069006b00540069006d006500730020004e006500
7700200052006f006d0061006e0020013000740061006c0069006b005000
6f016100650076006e006f00540069006d006500730020004e0065007700
200052006f006d0061006e00200050006f016100650076006e006f006e00
670068006900ea006e006700540069006d006500730020004e0065007700
200052006f006d0061006e0020006e00670068006900ea006e0067004500
74007a0061006e006100540069006d006500730020004e00650077002000
52006f006d0061006e002000450074007a0061006e00610000>
<410c005403cd02b0001d001f03cd03cd03cc03cb003c001f03cbb3061d1f
00410c03bc003003bc004003bc00a003bc00b003bc0005ffc003bbb34545
3240b803bbb32b2e3240b803bbb2282932b9ffc003bbb31a263280411303
bb009f03bb00af03bb00cf03bb0004000003bb001f03bb000203bb02af00
27001fffc003b9b2161b32b9ffc003b8b2424232b9ffc003b8b2363832b9
ffc003b8b32a2d32df410a03b800ef03b8000203b803b90028001fffc003
b9b3282e32f0410f03b90001000003b7000103b700030800001f03be03bf
002b001fffc003bfb2242a32b903b60381b23a1f0f411703b3001003b200
2003b2005003b2007003b200e003b2000600cf03b300df03b300ef03b300
ff03b30004001203a8b2e2891fbe039f016b019a001f039800930801400c
1f7f047f05027f027f03025fbb02b00001ffc00117b2196632b8ffc0b365
1a6632b9ff800173b2196632bd038401170800001fffc002afb2313340b8
02afb22e3340b802afb328293240b802afb326273240b802afb321253240
b802afb31c203240b802afb2233340b802afb21933a0bc02af00b002af00
e002afb5034003212932b8fff2b33a263d32bc038203820382003a0800b5
1f40255c331eb80381b25c6432b8ffeeb3252e3314b80381b32b2e3269be
03810001008a03810001000e0381b32b2f3210b80381b3515b320cb80381
b34e513222b80381b3474d320eb80381b246330ab8038140092647321225
4358320cb80381b2323310b80381b22a3312b80381b3373d3212bb038100
3d0033fff44015253d331825355b32102526343206252a330c252e33b8ff
fe4024252d330c3a2f33329925aa25ba25c92504052536330c2532383219
3a293a383a03182517b80381b42825382504bc0381038103810025080040
101f0f1f2b2e32691f781f020b1f303332b8fff1b31f263d32bc03800380
0380001f080040151f375f07af07025f06af060222ac2b2e3209ac2f33b8
ffdc400aac1f223222232b52320eb8037fb229330eb8037fb2223314b803
7fb21e2032b8ffe7b71e2b33321e2b2f32b9ffc0037fb64c4f3232262c33
410affee037f00390033fff8037f002b0033ffea037fb23a3320b8037fb3
3f46321eb8037fb32f3a3212b8037fb22e331eb8037fb32a2d320eb8037f
b2263304b8037fb3494a3404b8037fb2463304b8037fb2213318b8037f40
0c1d3322263032322226333832b8fff8400a262b2f3209261b21328abe03
7f0001037f037f037f00260800402e1f371f062f063f06039f02af02bf02
cf02049f03af03bf03cf03046f037f038f03031f032f033f034f035f0305
0f413a02ed0001005f02ed009f02ed00df02ed0003002f02ed003f02ed00
6f02ed000300af02af0001004f02af009f02af0002002f02af003f02af00
02003f02b00001000f02b0001f02b00002004f02af005f02af0002002f02
af003f02af0002007003b2000103b203b202ed02ed02b002b002af02af40
1a3701003001400102010100090102000800171700000012110840410b02
7b02230034000d013d0034000d01370034000d011b401a340d8f340d8434
0d68340d59340d54340d48340d2c340d28340d411002350020000d021b00
20000d01fc0020000d01c30020000d01500020000d012c401a200df0200d
be200d94200d79200d6a200d61200d5f200d44200d410d013e0138000d00
3d0138000d00300138000d001d0138000d01fdb40f4d0f0009bf01fd004d
000d03b1037f0015001f0215b226341fb80214b2263f1fb80208b21ebb1f
41190206001e0801001f0205001f02ab001f0204001f02ab001f0203001f
0401001f02010031019a001f01fb00230156001f01aeb2262a1fb801adb2
262a1fb801abb226341f411501a8002602ab001f01a5001e0125001f01a4
00ab02ab001f01a2003102ab001f01a1003102ab001f019db2236c1fb801
9cb2236c1f4109019b00230401001f019a0033019a001f0176b2262e1fb8
016cb231721f4111016b0023019a001f016800240401001f014500260801
001f013f00230401001f0123b21e9e1fbc0121001e0201001f0100b42679
1ffd1fb80125b21ffa33b80801b21ff924b802abb21fe826b80101b21fe5
1fb8019ab21fe431b80101400b1fe331e41fe231891fd226b80201b61fd0
26cd1fcd25b80401b21fb731b8019ab21fae26b80801b21fac1eb8040140
0b1f9e315e1f97269e1f9333b80801b21f8a24b8019ab21f831fb802ab40
131f82236c1f7523e41f7026cd1f6423721f5e25b80401b21f5d23b802ab
b21f55e6b80401b21f5324b80201b21f4f33b802abb21f4e26b804014013
1f4731671f4626ab1f4331cd1f3e235e1f3a1fb80401b61f3924e41f3723
b80801b21f2e23b80401b21f2a1eb80125400b1f2923ab1f2731ab1f5537
bc01c60007018a0007012b402e077f077107690766074b07400738073607
2d07220721071408120810080e080c080a080808060804080208000814b8
ffe0402b0000010014061000000100060400000100041000000100100200
0001000200000001000002010802004a00b013034b024b5342b0372b4bb8
07ff52b0382b4bb009505b58b101018e59014bb0c063004b6220b0f65323
b8010a515ab005234201b0124b004b544218b0382bb00288b801005458b8
01ffb101018e851bb0124358b900010140858d1bb900010159858d595900
16763f183f123e113946443e113946443e113946443e113946443e113946
60443e11394660442b2b2b2b2b2b2b2b2b2b2b182b2b2b2b2b2b2b2b2b2b
2b2b2b2b2b181db0964b5358b0aa1d59b0324b5358b0ff1d594bb0475320
5c58b9027d027b4544b9027c027b45445958b90146027d455258b9027d01
464459594bb04753205c58b9001e027c4544b90026027c45445958b9017f
001e455258b9001e017f4459594bb05e53205c58b9001f027d4544b90025
027d45445958b901a8001f455258b9001f01a84459594bb8010153205c58
b1ab1f4544b11f1f45445958b9047000ab455258b900ab04704459594bb8
012553205c58b1e61f4544b11f1f45445958b9051000e6455258b900e605
104459594bb01753205c58b124244544b1312445445958b12224455258b1
24224459594bb05153205c58b124244544b1232445445958b17d24455258
b1247d4459594bb06e53205c58b124244544b1332445445958b1aa244552
58b124aa4459592b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b
2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b
2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b65422b2b2b2b2b2b2b2b2b
2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b45695342014b50
58b108004259435c58b1080042591610703eb0124358b911b53d801bba01
1c03d9000b2b59b00a2342b00b2342003f3f182b103c012f5d060cb00623
42b0072342b0124358b93b21187e1bba040001a8000b2b59b00c2342b00d
2342b0124358b92d412d411bba04000400000b2b59b00e2342b00f2342b0
124358b9187e3b211bba01a80400000b2b59b0102342b0112342002b4bb0
2e5358b8016b45b02a60b8016b2344590018456944456944184569444569
44737373737375757573737475757575752b4bb026534bb03d515a58b126
2645b0196044592b45186944742b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b
2b2b2b2b2b2b2b2b2b2b004bb02a534bb03f515a58b1070745b040604459
73732b2b451869442b2b752b2b4518694475752b2b752b2b2b2b2b2b2b2b
2b2b2b2b2b2b2b2b2b2b74752b2b2b2b2b451869442b002b732b2b2b2b2b
2b2b2b2b012b2b2b007373732b2b2b01435c58b8ffdeb31e1c3318b8037f
b52b3318262b33b9fff00381b112332b2b2b2b590173742b2b2b002b7375
2b2b732b2b2b2b2b73752b2b2b2b73002b2b4569442b2b0000>
[4113 ] AllocGlyphStorage
]def 
124 60 
PrepFor2015
Type42DictEnd
2 2900 87 <00010054ffe802630481001e0106b90005ffde40710f390f400f39a405ef
02fb0e03551b8a00f60103241d3a005b0e030f201d20027f20ef20021e00
0e0f0104050707001d1c1e1b011a1c1d1e18051904010800161a19190404
039300a0020106130b0007071f161914161619161f2819161002490f031f
0302ff0301036c2000af070f8a0eba010100070203400c121640363934c0
16d0160216b8013b400a1f091617161f0a774c182b2b103c2b2b10f65d2b
435c58400f164028143f16401c113f16401e123f2b2b2b5901fdf6ed10e4
10f45d71e42b103c2b10c0870e2e2b057d10c400183f3f3ce4fd3c103c10
3c011112173900111239113939870e7d10c4053c3c0110c910c93130015d
715d5d5d2b2b010333072303061514163332373637170607062322263534
3713233736363702144e9d119cac1c100b19291853215c5238392c3820a7
970a6e925a0481fef03ffdb25f1c111223146719863726372b366f024327
1e779300>HBAAAA+TimesNewRomanPS-ItalicMT AddT42Char 
2 3264 89 <0001002cffe8038a0389002600fb4041b701012840103528400c3528400e
3559025803b604d92104291c3b1c49020338220108090a010c0d0e071807
070120248a00c61501071f200b1f122f123f120312b8019fb70f27184017
0e3f18b8ffc0b22a3518b8ffc0401b2635ef18ff18022018401880189018
cf1805181a281f8a20004926b8ffc0400c14353f264f265f26bf260426bc
0323000702030020ffc0b32c2e3420b8ffc0b22a3520b8ffc04019252934
2040170e3f502080209020a020042020302040200320b8021cb32732de18
2b10f65d5d2b2b2b2bedf65d2be410ed4e10f65d5d2b2b2b4dfde45d003f
3c3f3cf4ed191112392f01121739313001715d5d2b2b2b005d1325161716
171617363736373637363534263534363332161514070606070607230227
262322072c01211f131b11080e7d188414210d0b5d33232a40101a8e9e14
ca25184c193a192e034b3e4a4d719b4efc8a21b31f35281e1b1a442a2032
4533332f4cdbb817d102799d3309>HBAAAA+TimesNewRomanPS-ItalicMT AddT42Char 
2 0 0 <0002011c0000051c050000030007003fb40201f80607b802664013000504
f803000a0704f8010019080605f80203b8014ab309a2dc182b10f63cfd3c
4e10f43c4dfd3c003f3cfd3c10fc3cfd3c31302111211125211121011c04
00fc2003c0fc400500fb002004c0>HBAAAA+TimesNewRomanPS-ItalicMT AddT42Char 
HBAAAA+TimesNewRomanPS-ItalicMT /CharStrings get begin
/g87 87 def
/g89 89 def
end
HBAAAA+TimesNewRomanPS-ItalicMT /Encoding get
dup 116 /g87 put
dup 118 /g89 put
pop
end
%ADOEndSubsetFont
/RVGGZD+TimesNewRomanPS-ItalicMT /HBAAAA+TimesNewRomanPS-ItalicMT findfont ct_VMDictPut
/RVGGZD+TimesNewRomanPS-ItalicMT*1 
[116{/.notdef}rp /g87 /.notdef /g89 137{/.notdef}rp]
RVGGZD+TimesNewRomanPS-ItalicMT nf
RVGGZD+TimesNewRomanPS-ItalicMT*1 [7.50449 0 0 -7.509 0 0 ]msf
471.985 518.741 mo
(v)sh
RVGGZD+TimesNewRomanPS-ItalicMT*1 [12.9812 0 0 -12.989 0 0 ]msf
465.817 524.552 mo
(t)sh
grestore
gsave
503.26 529.737 mo
517.804 529.737 li
517.804 511.77 li
503.26 511.77 li
cp
clp
false sop
1 /0 /CSD get_res sepcs
1 sep
%ADOBeginSubsetFont: FBAAAA+TimesNewRomanPSMT AddGlyphs
ct_T42Dict begin
systemdict /gcheck known {currentglobal RVGGZC+TimesNewRomanPSMT gcheck setglobal} if
2 916 21 <0001002c000003ab0568001e0195b0852b58408207180b3917181c3d3418
401c3d3419401c3d340f1e161629073c074907a9070640205b045a085b17
5a186b08741174129c0b9d0e9911ac0bac0ec905c917c818d917d918e020
f904f9171515011d0419051b15191619171d180709170b180b1d34194719
89178f200718190202171a190c19060d031902050618171615140713040d
b8016840090940140c3f80090109b80333400c10051a8f19019f19af1902
19ba03330003018db301020c1eb8018d400d0006e24f135f136f137f1304
13b801074013400001001a002040208020036020a020022019bb01f90003
000d014040145f026f027f028f02bf02cf02df02ef020802191fba018e01
0100182b4e10f45d4de43ced4e105d71f65d4df45ded10ed003f3cedfd5d
713c3ffd71b10602435458b78f0901bf09cf0902005d71592be411121739
11123901111239390210b10602435458b47d198d1902005d590e3c871005
7dc40ec431300171725d005d012b2b2b002b1bb70d0d101e1e021009b808
1ab46c10050219b8081ab26c020c00183f2b3f2b12392f11392f30315901
032135000035342623220607233636333216151407060702072132363637
03ab5ffce0016101209e6e649f262519cf9ba5dd304aa6f93e01626c5746
1a0105fefb2501420198a981a67571b9c6d4906767a2b5fef03810312d00
>RVGGZC+TimesNewRomanPSMT AddT42Char 
RVGGZC+TimesNewRomanPSMT /CharStrings get begin
/g21 21 def
end
RVGGZC+TimesNewRomanPSMT /Encoding get
dup 50 /g21 put
pop
systemdict /gcheck known {setglobal} if
end
%ADOEndSubsetFont
/RVGGZC+TimesNewRomanPSMT*1 
[49{/.notdef}rp /g20 /g21 205{/.notdef}rp]
RVGGZC+TimesNewRomanPSMT nf
RVGGZC+TimesNewRomanPSMT*1 [6.57371 0 0 -6.577 0 0 ]msf
509.878 527.01 mo
(2)sh
RVGGZD+TimesNewRomanPS-ItalicMT*1 [6.57371 0 0 -6.577 0 0 ]msf
510.87 518.991 mo
(v)sh
RVGGZD+TimesNewRomanPS-ItalicMT*1 [11.3713 0 0 -11.377 0 0 ]msf
505.163 524.081 mo
(t)sh
grestore
false sop
1 /0 /CSD get_res sepcs
1 sep
%ADOBeginSubsetFont: FBAAAA+TimesNewRomanPSMT AddGlyphs
ct_T42Dict begin
systemdict /gcheck known {currentglobal RVGGZC+TimesNewRomanPSMT gcheck setglobal} if
2 558 17 <00010091ffe4016f00c2000b003bb0852b58401c0040060b034009403a35
09403f355f09019f09af090209850c6a7a182b10f671722b2bed003fed31
301bb200060b00183f3330315925321615140623222635343601002f4041
2e2e4141c2412e2e41412e2f4000>RVGGZC+TimesNewRomanPSMT AddT42Char 
RVGGZC+TimesNewRomanPSMT /CharStrings get begin
/g17 17 def
end
RVGGZC+TimesNewRomanPSMT /Encoding get
dup 46 /g17 put
pop
systemdict /gcheck known {setglobal} if
end
%ADOEndSubsetFont
/RVGGZC+TimesNewRomanPSMT*1 
[46{/.notdef}rp /g17 2{/.notdef}rp /g20 /g21 205{/.notdef}rp]
RVGGZC+TimesNewRomanPSMT nf
RVGGZC+TimesNewRomanPSMT*1 [18 0 0 -18 0 0 ]msf
528.841 522.157 mo
(...)
[4.52502 4.52496 0 ]xsh
gsave
556.05 530.752 mo
567.049 530.752 li
567.049 511.759 li
556.05 511.759 li
cp
clp
%ADOBeginSubsetFont: HBAAAA+TimesNewRomanPS-ItalicMT AddGlyphs
ct_T42Dict begin
systemdict /gcheck known {currentglobal RVGGZD+TimesNewRomanPS-ItalicMT gcheck setglobal} if
2 1276 76 <00020058ffe8022e0516000b002901244027176e3a3516763a35122b4012
352b40191b34590c0119230116172945215a282830294d0c007006b8039c
401a0c07280c0f0c290f1f1e21141e1e211b0b1e2a28211e10178a16b801
43b40f0970030cb80147b203600fb80123b7296c121e401b351eb8ffc0b3
3a3b341eb8ffc0b32a34341eb8ffc040092324341e401f20341eb8ffc040
13131634301e8f1e021e192a1e171e2a0a7786182b2b103c2b4e10f45d2b
2b2b2b2b2b435c58400b1e401c113f1e400d113f1eb8ffc0b3160d3f1eb8
ffc0b117392b2b2b2b594de4fde4e610ed10f6ed2b103c2b10c0003f870e
2e2b087d10c42b183f00f6ed10f5ed2bfc01f510c9313001715d2b2b435c
58b517400c143f0db8ffdeb61339172213390db8ffdeb50f3917400f392b
2b2b2b2b59012b2b01321615140623222635343613030615141633323736
371706070623222635343713363534262322073501ca2a3a3b29293b3a37
c614130d0f15393a23445c443e29341982201f1b164505163a2a293b3b29
2a3afe73fd43470e1014102d53176847353125255601c06e1c161c0b2700
>RVGGZD+TimesNewRomanPS-ItalicMT AddT42Char 
RVGGZD+TimesNewRomanPS-ItalicMT /CharStrings get begin
/g76 76 def
end
RVGGZD+TimesNewRomanPS-ItalicMT /Encoding get
dup 105 /g76 put
pop
systemdict /gcheck known {setglobal} if
end
%ADOEndSubsetFont
/RVGGZD+TimesNewRomanPS-ItalicMT*1 
[105{/.notdef}rp /g76 10{/.notdef}rp /g87 /.notdef /g89 137{/.notdef}rp]
RVGGZD+TimesNewRomanPS-ItalicMT nf
RVGGZD+TimesNewRomanPS-ItalicMT*1 [6.94227 0 0 -6.952 0 0 ]msf
561.813 519.393 mo
(v)sh
560.843 527.87 mo
(i)sh
RVGGZD+TimesNewRomanPS-ItalicMT*1 [12.0092 0 0 -12.026 0 0 ]msf
557.491 524.773 mo
(t)sh
grestore
gsave
589.401 528.002 mo
615.169 528.002 li
615.169 514.509 li
589.4 514.509 li
589.401 528.002 li
clp
%ADOBeginSubsetFont: HBAAAA+TimesNewRomanPS-ItalicMT AddGlyphs
ct_T42Dict begin
systemdict /gcheck known {currentglobal RVGGZD+TimesNewRomanPS-ItalicMT gcheck setglobal} if
2 104 38 <0001008affe105a1056b0027008f40242410430b43105c06670b740a760b
771e86109610a700b600b40c0da612c61202060f0102b8014d4009082492
083327200315b80213b71164180900150115b8031eb2028801b80142b227
8800b8ffc0b4143900f40eb8037f40121c40474b341c4014399f1c011c65
28657d182b4e10f45d2b2b4de9fd2bedf4ede45d003ffde43f3cedec10e4
3130005d71015d010323272e032322070607061514163332363733060423
22242635341224333217163332363705a16524040524486e43b386ab6150
e6b88bd95d2f6efef4bba6ff0086ee019fd3637b361818242a056bfe496e
3c5e4527627de4bcc1c5eb7c81afa58bfc91de01a4f02f14142f>RVGGZD+TimesNewRomanPS-ItalicMT AddT42Char 
2 370 47 <0001ffbe0000042f054c00280109403309131828021255168f268b278b28
a400b700b61b0727280108021d011218131d121109101d111819191e0809
14080809232028b801064021202e01121102010828272300042a08292809
081000a90028102820280328c42a19bd030100090345001200080173b629
09081708290ab80173b1c4182b2b103c2b2b4e10f4435c58b90008ff80b3
26173f08b8ffc0b328183f08b8ff80b62d173f088018392b2b2b2b59014d
e4ed4e10f6714de42b103c2b10c001121739003f3f3c10eded1139870e2e
2b0e7d10c4180010ed0110c00010ed0110c00010ed0110c010c93130015d
435c58b5244011143e19b8ffe8b2113915b8ffdeb30f133e16b8ffdeb20f
133e2b2b2b2b59015d212137363736373637133635342623222737210722
060706070306151417163333323736373637373303abfc130e501b2a141f
23ef1e374c110a0c0229085d4e1a1229eb1b1b113c838f543e341c471a25
25020b121d2e7803396630262a01252524291b8dfcd55c2418160f241b36
1e772d00>RVGGZD+TimesNewRomanPS-ItalicMT AddT42Char 
2 764 54 <0001000effe10456056b003b01554085852c812f025e0d5e0e5e0f6a0d6f
0e6f0f6f107d0d7f0e7f0f7b10802d802e9c0d9d0e9c0f1028002a0d342d
542d6721642d7c087b0e722e8908862a862d9b0c9a0e9a109533a800ad0c
af0eaf0fac10a52ea92fb901be0cbc0ebf10b32eb62ff42e1e162e510b50
0c530d5b2d542f06061417144a0c480e4a10842e060f2d0d2e0407281db8
031e400a28641523ef2121150302bb012e00000039031e40110733343400
09102b120aac203030300230b8031eb5238822208822b80142b51f21e021
0221b8ffc0b2133921b8ffc0b3191b3421b8ffc0401b2227342f213f2180
2103211a3d2bac12402e3512cc0288013b8801b80142b59f00e0000200b8
ffc0b72227340040173500ba0136003c0136b17d182b4e10f42b2b5d4de4
ed10edf42bed4e10f65d2b2b2b5d4de4ed10edf45ded111239003f3c10ed
ec10ed3f3c10ed10edec111217393130005d72015d007101711713330615
141633323635342726272627263534363332171617161716333236373303
233635342623220615141600161514060623222627262322070e702207af
8d83881f2fcc631c2ed4a638321f523a060e111d2a1c26682204a0836882
53012b586dcc793c6872271a3b211f01f7493089aca169443853d1643151
598eca0b06221702031e31fe3e3c25799a7a50467ffee1a15b67c16a162b
0f50>RVGGZD+TimesNewRomanPS-ItalicMT AddT42Char 
2 2074 80 <00010023ffe8056e038900530245408419010112382d0159095b0c5f0d57
145c385d3a5d3b5e3c5552681369166a2c790c79167a2c783c89038b2c8b
3c89439d039b0e9b369d43a701ab0da137a938af39af3aaf3bae3caa44a3
45b538b63ab648256b3668376a4403520059445252038936884498450365
397a36753a7b447648a339062801253927472f556f5405212253fe4bb801
1c4054285230534d000d3a070149410d0a3a01004b343111114131070753
c600071419191f2930142929300a3a3a1f3b3e143b3b3e00480053481f49
4b1449494b260b4948483b3b3a0a29542830293e3b4b4910228a21b80143
b319142530b80124400c192529400e356029df290229b80234b66f3a01af
3a013ab8020340153b4023353b401b1c346f3b013b500a010a253ead3bba
01c000480203b44bad52c949b8ffc0b2173949b8ffc0b2233549b8ffc0b2
1f3549b8ffc0b31b1c3449b8ffc0b2193549b8ffc0b32a2c3449b8ffc040
172f34346f49ef490249195429173b17491729540a3286182b2b103c2b2b
2b4e10f45d2b2b2b2b2b2b2b4de4e4edf4f4ed5d10712b2bed5d71f45d2b
edf4ed10f6ed2b103c103c103c2b10c0003f3c103c103c3f87052e2b087d
10c487052e182b0e7d10c4870e2e182b7d10c400183fe43c10ed3c10ed01
1112391112390011123911123910f5ed2bfc01f510c93130015d5d5d5d5d
5d0171435c5840110d180c393c180c3900220c394a180c3936b8ffc0b20f
390fb8ffdeb20f3904b8ffdeb20f3900b8ffc0b20f3953b8ffc0b20f3917
b8ffdeb613143e222213392b2b2b2b2b2b2b2b2b2b2b59005d0103363736
373633321615140707123736333216151407030615141716333237363717
0e0223222635343713363736353427262322070607060723133635342623
22070602070603231337363534262322072701bc82573d5f5a353a324217
47a392514f2e3b126e2409060a0a19393221197f5a26232f295b1f02030b
0c0f2a2f8a784f4597ab1c161021253cbd34195e94b91807281f0d3b0903
89fe3d9f507c38204032314ffe01317b443f423a41fe7b7f0e0e0a07132c
4815288c323023309101416f0c1312190e0e2b7fe597ec025d62211b1a18
27ff007537fed6028854130916230c25>RVGGZD+TimesNewRomanPS-ItalicMT AddT42Char 
RVGGZD+TimesNewRomanPS-ItalicMT /CharStrings get begin
/g38 38 def
/g47 47 def
/g54 54 def
/g80 80 def
end
RVGGZD+TimesNewRomanPS-ItalicMT /Encoding get
dup 67 /g38 put
dup 76 /g47 put
dup 83 /g54 put
dup 109 /g80 put
pop
systemdict /gcheck known {setglobal} if
end
%ADOEndSubsetFont
/RVGGZD+TimesNewRomanPS-ItalicMT*1 
[67{/.notdef}rp /g38 8{/.notdef}rp /g47 6{/.notdef}rp /g54 21{/.notdef}rp /g76 
3{/.notdef}rp /g80 6{/.notdef}rp /g87 /.notdef /g89 137{/.notdef}rp]
RVGGZD+TimesNewRomanPS-ItalicMT nf
RVGGZD+TimesNewRomanPS-ItalicMT*1 [5.02497 0 0 -6.631 0 0 ]msf
604.158 520.402 mo
(m)sh
RVGGZD+TimesNewRomanPS-ItalicMT*1 [8.69121 0 0 -11.469 0 0 ]msf
589.401 525.534 mo
(CLS)
[5.34973 4.48895 0 ]xsh
grestore
gsave
633.67 529.497 mo
646.653 529.497 li
646.653 510.504 li
633.67 510.504 li
cp
clp
RVGGZC+TimesNewRomanPSMT*1 [6.94574 0 0 -6.952 0 0 ]msf
637.924 526.615 mo
(1)sh
RVGGZD+TimesNewRomanPS-ItalicMT*1 [6.94574 0 0 -6.952 0 0 ]msf
639.52 518.138 mo
(m)sh
RVGGZD+TimesNewRomanPS-ItalicMT*1 [12.0152 0 0 -12.026 0 0 ]msf
635.11 523.518 mo
(t)sh
grestore
gsave
672.701 529.824 mo
685.683 529.824 li
685.683 510.831 li
672.701 510.831 li
cp
clp
RVGGZC+TimesNewRomanPSMT*1 [6.94574 0 0 -6.952 0 0 ]msf
677.705 526.942 mo
(2)sh
RVGGZD+TimesNewRomanPS-ItalicMT*1 [6.94574 0 0 -6.952 0 0 ]msf
678.55 518.465 mo
(m)sh
RVGGZD+TimesNewRomanPS-ItalicMT*1 [12.0152 0 0 -12.026 0 0 ]msf
674.14 523.845 mo
(t)sh
grestore
RVGGZC+TimesNewRomanPSMT*1 [18.025 0 0 -18.025 0 0 ]msf
697.69 522.707 mo
(...)sh
gsave
723.72 530.329 mo
736.703 530.329 li
736.703 510.344 li
723.72 510.344 li
cp
clp
%ADOBeginSubsetFont: HBAAAA+TimesNewRomanPS-ItalicMT AddGlyphs
ct_T42Dict begin
systemdict /gcheck known {currentglobal RVGGZD+TimesNewRomanPS-ItalicMT gcheck setglobal} if
2 1696 77 <0002fea4fe46023e0515000b003000e7b61232400f103432b8ffc0b31b27
3432b8ffc0401d0d355f0d5f255b265b279330051a29013045265a282f30
304d0c007006b8039c40210c070c0d0c300d1f25261425252616b8222410
0f25400f39253128262510097003b8ffc0400e2a35900301400350030203
57320cb8032bb34f260126b8019fb5261ee4133a1ab80335400b26eb3125
1725310a3286182b2b103c2b10f6f6fded10e45ded10f45d712bed2b103c
2b10c02b003ffde4870e2e2b087d10c400183ff6ed10f5ed2bfc01f53130
01715d2b2b2b435c5840140d400f390e400f3925400f390c400f3926400f
392b2b2b2b2b590132161514062322263534361301060623222635343633
321716151407061517161633323637133635342623220706073501d92a3b
3b2a2a3b3b3afefd45f18c3f4131201d1612190e02030c0c51732de0212b
210d110d1905153b2a2a3b3b2a2a3bfe74fc81f0d43a281f2f130f131a13
0b07050404679a0300710c18260302042300>RVGGZD+TimesNewRomanPS-ItalicMT AddT42Char 
RVGGZD+TimesNewRomanPS-ItalicMT /CharStrings get begin
/g77 77 def
end
RVGGZD+TimesNewRomanPS-ItalicMT /Encoding get
dup 106 /g77 put
pop
systemdict /gcheck known {setglobal} if
end
%ADOEndSubsetFont
/RVGGZD+TimesNewRomanPS-ItalicMT*1 
[67{/.notdef}rp /g38 8{/.notdef}rp /g47 6{/.notdef}rp /g54 21{/.notdef}rp /g76 
/g77 2{/.notdef}rp /g80 6{/.notdef}rp /g87 /.notdef /g89 137{/.notdef}rp]
RVGGZD+TimesNewRomanPS-ItalicMT nf
RVGGZD+TimesNewRomanPS-ItalicMT*1 [6.94235 0 0 -6.95 0 0 ]msf
729.565 517.974 mo
(m)sh
730.004 526.448 mo
(j)sh
RVGGZD+TimesNewRomanPS-ItalicMT*1 [12.0088 0 0 -12.022 0 0 ]msf
725.158 523.353 mo
(t)sh
grestore
420.001 530.738 mo
442.941 530.738 li
443.721 530.738 444.351 530.103 444.351 529.32 cv
444.351 514.188 li
444.351 513.405 443.721 512.77 442.941 512.77 cv
420.001 512.77 li
419.221 512.77 418.591 513.405 418.591 514.188 cv
418.591 529.32 li
418.591 530.103 419.221 530.738 420.001 530.738 cv
.444 .272 0 0 cmyk
ef
.25 lw
1 lc
1 lj
10 ml
[] 0 dsh
true sadj
420.001 530.738 mo
442.941 530.738 li
443.721 530.738 444.351 530.103 444.351 529.32 cv
444.351 514.188 li
444.351 513.405 443.721 512.77 442.941 512.77 cv
420.001 512.77 li
419.221 512.77 418.591 513.405 418.591 514.188 cv
418.591 529.32 li
418.591 530.103 419.221 530.738 420.001 530.738 cv
cp
1 /0 /CSD get_res sepcs
1 sep
@
2 lc
0 lj
2 ml
[2 1 ] 0 dsh
414.331 534.927 mo
577.32 534.927 li
577.32 506.581 li
414.331 506.581 li
cp
@
gsave
419.861 527.905 mo
443.869 527.905 li
443.869 514.412 li
419.861 514.412 li
cp
clp
RVGGZD+TimesNewRomanPS-ItalicMT*1 [4.37978 0 0 -6.631 0 0 ]msf
433.552 520.305 mo
(v)sh
RVGGZD+TimesNewRomanPS-ItalicMT*1 [7.57527 0 0 -11.469 0 0 ]msf
419.862 525.437 mo
(CLS)
[4.98849 4.1777 0 ]xsh
grestore
gsave
0 570 mo
756.961 570 li
756.961 .893066 li
0 .893066 li
cp
clp
[2 1 ] 0 dsh
581.581 534.793 mo
745.42 534.793 li
745.42 506.447 li
581.581 506.447 li
cp
@
429.921 488.567 mo
730.401 488.567 li
733.531 488.567 736.07 486.037 736.07 482.907 cv
736.07 457.777 li
736.07 454.647 733.531 452.107 730.401 452.107 cv
429.921 452.107 li
426.791 452.107 424.261 454.647 424.261 457.777 cv
424.261 482.907 li
424.261 486.037 426.791 488.567 429.921 488.567 cv
.111 0 .177 0 cmyk
ef
[] 0 dsh
429.921 488.567 mo
730.401 488.567 li
733.531 488.567 736.07 486.037 736.07 482.907 cv
736.07 457.777 li
736.07 454.647 733.531 452.107 730.401 452.107 cv
429.921 452.107 li
426.791 452.107 424.261 454.647 424.261 457.777 cv
424.261 482.907 li
424.261 486.037 426.791 488.567 429.921 488.567 cv
cp
@
1 /0 /CSD get_res sepcs
1 sep
%ADOBeginSubsetFont: FBAAAA+TimesNewRomanPSMT AddGlyphs
ct_T42Dict begin
systemdict /gcheck known {currentglobal RVGGZC+TimesNewRomanPSMT gcheck setglobal} if
2 5238 47 <00010029000004b7054c002000e1b0852b58401b10001001200020014022
5702670277028a209920a920b9200c0122b8018e40330e643655025c1e02
091f1b03212216371b113d220a1f1b102123201f2000300040000300e71c
1110021c2302030800ac016c02b802c4402f16170613130255170c0f0f02
55170c0d0d0255172209090a0c101002550a0c0f0f02550a1a0d0d02550a
9e21615d182b4e10f42b2b2b3c4d10fd2b2b2b3cf4f4ed003f3ced3f3c10
e45d39392b2b2b313001722b015d1bb500000312100fb803e2b46c100203
1cb807f4b26c0304b803e2b26c030800183f2b2b3f2b3212392f30315901
170321353332373635113427262323352115260606151114171616333332
363604962174fbe6335625151c274d3302666c5720100c3283639c7e6801
7707fe9025382074036b7f202c2525012a4079fcac531f15142e7500>RVGGZC+TimesNewRomanPSMT AddT42Char 
2 5566 48 <00010022000006f2054c00300204b0852b5840e80f18010e0008170e190d
280f290f2a043007123d013d2f59186f0168186d2f791897019a2fcb18da
18e801eb180d0d18010a1706304630033618363047180316302718263003
061805301717032b00291826303b003a173918351935303f324f3268007a
007618791974308a008918853099009730a900a630a032b032cc17c918c0
32dc17d918d032ed17ea18ea19e032f600fa17f7302548014917462f5a01
5917562f6a177819c618c530d618d630e518e5300e0f1f1b092122201f1b
1a21222e1f1b282122021f1b082123101f1b162123211f1b272123171818
220001140018190001191818b802c9403e302f14301817302f182f012f18
0316171a1919170209080800003030272808305b000002192f2e22202021
a021b021c021d021e02106219e403201320102b802c9400d100f200f1102
550f9e3161dc182b4e10f42b3c4dfd3c4d105df65d3c4dfd3c3c11392ffe
003f3c3c103c103c103c3f3c103c103c173901113987082e2b057d10c487
082e182b057d10c4182b2b2b2b2b2b3130015d5d7171717100715d435c58
401b2f10140c3f0110140c3f0110103918181139181012390008183917b8
ffd0b5173917301439012b2b2b002b2b2b002b2b59015d005d1b400c0118
2f03091916020008191cb803e240096c190206252903090ab803e2b36c28
090800183f332b17323f2b3f3f1112173930315921011114171633331521
353332373635113427262623352101012115232207061511141716333315
2135333237363511010346fdf41b255030fe2830562416140e4b53018001
ec01e401802f5724161c25502ffdc030572316fdf50475fc767d1f2a2525
34207203765a281d2725fbdb042525342072fc8a7d1f2a2525342072038a
fb8b>RVGGZC+TimesNewRomanPSMT AddT42Char 
2 6852 51 <000200220000042b054c001f002c01b1b0852b58b9002effc040933a352f
2e7518741b741c7c28702e951c077918b724ba28db1bdb1cda2406192710
2e2826392539273b28302e5a276927702e802e0bc600011a1c291c4b1cd7
19db1b05a82801ca24d917da24d927d828eb24061c40231d28080e1f1b08
2122011f1b0721230f1f1b152123001d202c2a1d283f234f230223230715
2a281616150208070812001a101a301a401a701a051a492eb8ffc0403e3f
35002e01402eb02e029f2ec02ed02e032e2c010613130255010c0f0f0255
010c0d0d025501220f0e0c101002550e0c0f0f02550e1a0d0d02550e9e2d
2eb80177b3216163182b2b4ef42b2b2b3c4dfd2b2b2b3c4d105d71722bf6
5d4d4358b90026032de91bb90026032ded59003f3c3f3c10ed1112392f5d
ed12393912392b2b2b31304379401c2429171c182528262917263301241c
26330127192a3301251b2333002b2b012b2b2b2b81810049547940101e22
211f233b04221e203b0021201f0001103c103c2b002b8101715d00717201
72005d015d2b1bb11d23b807eab56c1d1d08152ab807f1b26c1514b803e2
b56c1502050809b803e2b26c080800183f2b323f2b2b12392f2b30315901
111417163333152135333237363511342726232335213216161514062322
262716163332363534262623220701a41c264d34fdbb335625141b274d33
01f1b6d290dbc831724135521d68974884543350027bfe75801f2c252538
1f74036c801f2c254bb27aa6d00e470a0aa18058974b1300>RVGGZC+TimesNewRomanPSMT AddT42Char 
RVGGZC+TimesNewRomanPSMT /CharStrings get begin
/g47 47 def
/g48 48 def
/g51 51 def
end
RVGGZC+TimesNewRomanPSMT /Encoding get
dup 76 /g47 put
dup 77 /g48 put
dup 80 /g51 put
pop
systemdict /gcheck known {setglobal} if
end
%ADOEndSubsetFont
/RVGGZC+TimesNewRomanPSMT*1 
[46{/.notdef}rp /g17 2{/.notdef}rp /g20 /g21 25{/.notdef}rp /g47 /g48 
2{/.notdef}rp /g51 175{/.notdef}rp]
RVGGZC+TimesNewRomanPSMT nf
RVGGZC+TimesNewRomanPSMT*1 [12.025 0 0 -12.025 0 0 ]msf
568.391 474.527 mo
(PLM)
[6.73401 7.49139 0 ]xsh
1.5 lw
678.081 512.754 mo
677.981 493.547 li
@
673.961 493.627 mo
677.961 489.577 li
682 493.577 li
673.961 493.627 li
cp
ef
431.471 512.77 mo
431.471 494.956 li
@
427.451 495.01 mo
431.471 490.987 li
435.491 495.01 li
427.451 495.01 li
cp
ef
470.331 512.365 mo
470.331 494.55 li
@
466.31 494.604 mo
470.331 490.587 li
474.351 494.604 li
466.31 494.604 li
cp
ef
509.291 511.788 mo
509.291 493.977 li
@
505.271 494.027 mo
509.291 490.007 li
513.31 494.027 li
505.271 494.027 li
cp
ef
560.32 512.291 mo
560.32 494.476 li
@
556.301 494.53 mo
560.32 490.507 li
564.341 494.53 li
556.301 494.53 li
cp
ef
598.711 512.272 mo
598.711 493.537 li
@
594.69 493.597 mo
598.711 489.577 li
602.731 493.597 li
594.69 493.597 li
cp
ef
638.871 512.754 mo
638.851 493.797 li
@
634.831 493.857 mo
638.851 489.827 li
642.871 493.847 li
634.831 493.857 li
cp
ef
728.701 512.858 mo
728.701 495.043 li
@
724.681 495.097 mo
728.701 491.077 li
732.721 495.097 li
724.681 495.097 li
cp
ef
587.25 434.527 mo
610.181 434.527 li
610.961 434.527 611.601 433.897 611.601 433.107 cv
611.601 417.977 li
611.601 417.197 610.961 416.557 610.181 416.557 cv
587.25 416.557 li
586.461 416.557 585.831 417.197 585.831 417.977 cv
585.831 433.107 li
585.831 433.897 586.461 434.527 587.25 434.527 cv
.377 .016 .604 0 cmyk
ef
.25 lw
1 lc
1 lj
587.25 434.527 mo
610.181 434.527 li
610.961 434.527 611.601 433.897 611.601 433.107 cv
611.601 417.977 li
611.601 417.197 610.961 416.557 610.181 416.557 cv
587.25 416.557 li
586.461 416.557 585.831 417.197 585.831 417.977 cv
585.831 433.107 li
585.831 433.897 586.461 434.527 587.25 434.527 cv
cp
1 /0 /CSD get_res sepcs
1 sep
@
627.401 435.007 mo
650.341 435.007 li
651.121 435.007 651.76 434.377 651.76 433.587 cv
651.76 418.457 li
651.76 417.677 651.121 417.037 650.341 417.037 cv
627.401 417.037 li
626.621 417.037 625.991 417.677 625.991 418.457 cv
625.991 433.587 li
625.991 434.377 626.621 435.007 627.401 435.007 cv
.377 .016 .604 0 cmyk
ef
627.401 435.007 mo
650.341 435.007 li
651.121 435.007 651.76 434.377 651.76 433.587 cv
651.76 418.457 li
651.76 417.677 651.121 417.037 650.341 417.037 cv
627.401 417.037 li
626.621 417.037 625.991 417.677 625.991 418.457 cv
625.991 433.587 li
625.991 434.377 626.621 435.007 627.401 435.007 cv
cp
1 /0 /CSD get_res sepcs
1 sep
@
666.621 435.007 mo
689.551 435.007 li
690.331 435.007 690.971 434.377 690.971 433.587 cv
690.971 418.457 li
690.971 417.677 690.331 417.037 689.551 417.037 cv
666.621 417.037 li
665.831 417.037 665.201 417.677 665.201 418.457 cv
665.201 433.587 li
665.201 434.377 665.831 435.007 666.621 435.007 cv
.377 .016 .604 0 cmyk
ef
666.621 435.007 mo
689.551 435.007 li
690.331 435.007 690.971 434.377 690.971 433.587 cv
690.971 418.457 li
690.971 417.677 690.331 417.037 689.551 417.037 cv
666.621 417.037 li
665.831 417.037 665.201 417.677 665.201 418.457 cv
665.201 433.587 li
665.201 434.377 665.831 435.007 666.621 435.007 cv
cp
1 /0 /CSD get_res sepcs
1 sep
@
717.231 435.107 mo
740.161 435.107 li
740.951 435.107 741.581 434.477 741.581 433.697 cv
741.581 418.567 li
741.581 417.777 740.951 417.147 740.161 417.147 cv
717.231 417.147 li
716.451 417.147 715.81 417.777 715.81 418.567 cv
715.81 433.697 li
715.81 434.477 716.451 435.107 717.231 435.107 cv
.377 .016 .604 0 cmyk
ef
717.231 435.107 mo
740.161 435.107 li
740.951 435.107 741.581 434.477 741.581 433.697 cv
741.581 418.567 li
741.581 417.777 740.951 417.147 740.161 417.147 cv
717.231 417.147 li
716.451 417.147 715.81 417.777 715.81 418.567 cv
715.81 433.697 li
715.81 434.477 716.451 435.107 717.231 435.107 cv
cp
1 /0 /CSD get_res sepcs
1 sep
@
grestore
gsave
591.121 433.527 mo
607.108 433.527 li
607.108 414.534 li
591.12 414.534 li
591.121 433.527 li
clp
%ADOBeginSubsetFont: HBAAAA+TimesNewRomanPS-ItalicMT AddGlyphs
ct_T42Dict begin
systemdict /gcheck known {currentglobal RVGGZD+TimesNewRomanPS-ItalicMT gcheck setglobal} if
2 3638 91 <0001ffb8ffe8038003890046010840630d40120b3f0700072a003d013e14
001601240023014a1b56018919a301a919aa2aa83daf3f10484010351017
63217321c919cb210509230c2a52230304191a1a022a2a2b3e403e3c4028
2122021a1a1f2840142828403e2a1904041135428a46c60011b80395401f
153a0a0a000735c639272e2e260b042a193e218a9f22cf220222c90d02e4
45ba014700400124b21a8228b8019f401d19e43e403b4b343e401d353e3e
47200d400d8f0daf0d040d1a48321947b80114b1de182b4e10e410e65d12
392f2b2b4dedf4edf4e6ed10f45ded11123939003f3c10fde43f3c10fde4
10f4ed11121739870e2e2b0e7d10c40110c90708103c083c870e10c4c431
30005d5d012b5d2b01161716173736363736333216151407062322272623
220706071316163332373637170607062322272603020706232227263534
363332171633323736363726272626232207350163311912295823642618
1d2b330f1c2415182f1018213e5652131a0d151c3727233f613726382115
429c5e3d392821182c2020241a0e0c132fa2193e05174a48171e03893434
2499843057100a2e21260e1909101c3495fea84f1f172e4a12764e2c3f27
0129fef14e321d1625212c20171026fc38f30e4136022400>RVGGZD+TimesNewRomanPS-ItalicMT AddT42Char 
RVGGZD+TimesNewRomanPS-ItalicMT /CharStrings get begin
/g91 91 def
end
RVGGZD+TimesNewRomanPS-ItalicMT /Encoding get
dup 120 /g91 put
pop
systemdict /gcheck known {setglobal} if
end
%ADOEndSubsetFont
/RVGGZD+TimesNewRomanPS-ItalicMT*1 
[67{/.notdef}rp /g38 8{/.notdef}rp /g47 6{/.notdef}rp /g54 21{/.notdef}rp /g76 
/g77 2{/.notdef}rp /g80 6{/.notdef}rp /g87 /.notdef /g89 /.notdef 
/g91 135{/.notdef}rp]
RVGGZD+TimesNewRomanPS-ItalicMT nf
RVGGZD+TimesNewRomanPS-ItalicMT*1 [6.94922 0 0 -6.952 0 0 ]msf
599.402 422.168 mo
(m)sh
598.496 430.645 mo
(C)sh
RVGGZD+TimesNewRomanPS-ItalicMT*1 [12.0212 0 0 -12.026 0 0 ]msf
593.496 427.548 mo
(x)sh
grestore
gsave
632.171 433.787 mo
648.158 433.787 li
648.158 414.794 li
632.171 414.794 li
cp
clp
RVGGZC+TimesNewRomanPSMT*1 [6.94922 0 0 -6.952 0 0 ]msf
639.015 430.905 mo
(1)sh
RVGGZD+TimesNewRomanPS-ItalicMT*1 [6.94922 0 0 -6.952 0 0 ]msf
640.451 422.428 mo
(m)sh
RVGGZD+TimesNewRomanPS-ItalicMT*1 [12.0212 0 0 -12.026 0 0 ]msf
634.546 427.808 mo
(x)sh
grestore
gsave
671.19 434.107 mo
687.178 434.107 li
687.178 415.114 li
671.19 415.114 li
cp
clp
RVGGZC+TimesNewRomanPSMT*1 [6.94922 0 0 -6.952 0 0 ]msf
678.784 431.225 mo
(2)sh
RVGGZD+TimesNewRomanPS-ItalicMT*1 [6.94922 0 0 -6.952 0 0 ]msf
679.472 422.748 mo
(m)sh
RVGGZD+TimesNewRomanPS-ItalicMT*1 [12.0212 0 0 -12.026 0 0 ]msf
673.566 428.128 mo
(x)sh
grestore
RVGGZC+TimesNewRomanPSMT*1 [18.025 0 0 -18.025 0 0 ]msf
697.69 426.877 mo
(...)sh
gsave
722.221 434.617 mo
738.208 434.617 li
738.208 414.632 li
722.22 414.632 li
722.221 434.617 li
clp
RVGGZD+TimesNewRomanPS-ItalicMT*1 [6.94652 0 0 -6.95 0 0 ]msf
730.502 422.262 mo
(m)sh
731.096 430.736 mo
(j)sh
RVGGZD+TimesNewRomanPS-ItalicMT*1 [12.016 0 0 -12.022 0 0 ]msf
724.596 427.641 mo
(x)sh
grestore
gsave
0 570 mo
756.961 570 li
756.961 .893066 li
0 .893066 li
cp
clp
[2 1 ] 0 dsh
581.581 439.077 mo
745.42 439.077 li
745.42 410.731 li
581.581 410.731 li
cp
@
1.5 lw
[] 0 dsh
431.471 450.557 mo
431.471 438.987 li
@
427.451 439.047 mo
431.471 435.027 li
435.491 439.047 li
427.451 439.047 li
cp
ef
470.331 450.147 mo
470.331 438.587 li
@
466.31 438.637 mo
470.331 434.617 li
474.351 438.637 li
466.31 438.637 li
cp
ef
509.291 449.567 mo
509.291 438.007 li
@
505.271 438.067 mo
509.291 434.047 li
513.31 438.067 li
505.271 438.067 li
cp
ef
560.32 450.077 mo
560.32 438.507 li
@
556.301 438.567 mo
560.32 434.547 li
564.341 438.567 li
556.301 438.567 li
cp
ef
598.711 450.057 mo
598.711 438.497 li
@
594.69 438.547 mo
598.711 434.527 li
602.731 438.547 li
594.69 438.547 li
cp
ef
638.871 450.537 mo
638.871 438.977 li
@
634.851 439.027 mo
638.871 435.007 li
642.891 439.027 li
634.851 439.027 li
cp
ef
678.081 450.537 mo
678.081 438.977 li
@
674.06 439.027 mo
678.081 435.007 li
682.101 439.027 li
674.06 439.027 li
cp
ef
728.701 450.637 mo
728.701 439.077 li
@
724.681 439.127 mo
728.701 435.107 li
732.721 439.127 li
724.681 439.127 li
cp
ef
612.481 394.447 mo
714.521 394.447 li
717.651 394.447 720.19 391.917 720.19 388.777 cv
720.19 376.217 li
720.19 373.087 717.651 370.547 714.521 370.547 cv
612.481 370.547 li
609.341 370.547 606.81 373.087 606.81 376.217 cv
606.81 388.777 li
606.81 391.917 609.341 394.447 612.481 394.447 cv
.111 0 .177 0 cmyk
ef
.25 lw
612.481 394.447 mo
714.521 394.447 li
717.651 394.447 720.19 391.917 720.19 388.777 cv
720.19 376.217 li
720.19 373.087 717.651 370.547 714.521 370.547 cv
612.481 370.547 li
609.341 370.547 606.81 373.087 606.81 376.217 cv
606.81 388.777 li
606.81 391.917 609.341 394.447 612.481 394.447 cv
cp
@
1 /0 /CSD get_res sepcs
1 sep
%ADOBeginSubsetFont: FBAAAA+TimesNewRomanPSMT AddGlyphs
ct_T42Dict begin
systemdict /gcheck known {currentglobal RVGGZC+TimesNewRomanPSMT gcheck setglobal} if

2 0 3 <> RVGGZC+TimesNewRomanPSMT AddT42Char 
2 1426 36 <00020010000005b0056b001c001f0254b0852b58b102024354584012011f
1e021e1d001c1e1c001d1f011e1c0214be03e2001703e2000703e2000a03
e2401708021c1e030f081c161d001f70018001020101080f0208002f3f12
392f5dcdd0cd2f2f1112173910ededeeec012f2f2f2f2f2f2f107d87c4c4
1087c4c431301b401b080e0f0f0d100a1e091f502106150f13101a111a1b
1b1c181d0621b8ffc0b2253521b8ffc0b330583421b8ffc0b32b2e3421b8
ffc0b2293521b8ffc0b320263421b8ffc0b31a1e3421b8ffc0b2173521b8
ffc0b2153521b8ffc040971013340d0f0b100a1e390f4a0f4610491e4f21
590f57105514581e6a0f6710681e76108004870e8a0f87108712891e881f
9b0f9b1099119b1eb90fb910bd1ab91ecb0fca10c81dca1edb0fd810eb0f
e810e81ef90ff810f91df91e2c090f4b1b021f1e01011f1e02001d1e1e1c
090e0a1b09161c171b160802071b081511141b15781e0f1020101e1c1c22
1110141170110111100f0e0eb802c94011021e1402021e1f1da500007001
80010201b801b5400c08100f03151616080809081cb801fa40090f110111
02a50e4011b80230b34f1e011eb802ec400e20400e500ef00e030ea7206b
8a182b10f65d191afd5ded181a10ed105ded003f3c103c103c3f3c10f45d
3c10fd3c870e2e2b057d10c4875d0e2e182b87057dc42b180010ed0110c0
0010ed0110c00010ed0110c00010ed0110c087107dc43c073c3c073c3130
01715d2b2b2b2b2b2b2b2b2b01725d591bb71e0f1d1d090f1f01b807ed40
0c6c1f1f090f0307171403090ab803e2b36c16090800183f332b17323f12
392f2b1112392f1139303159012107061514161715213536373637013301
16161715213536363534270b0203a9fdf35c223b62fe555519333e01dd23
01d8395d53fde95139286ee6ec01c6d64f271f2f0725250f183093045cfb
988851052525042e212c5f010d0224fddc00>RVGGZC+TimesNewRomanPSMT AddT42Char 
2 8600 54 <00010080ffe10405056b00380299b0852b58401912952c010f010f020b03
000f04280029052b4f014f0209113ab8014640d03638361a031b045f185f
195f1a5f1b06050d050e002ac03a04740b740d740e760f701e701f702f70
308908860b870d870e840f872ba804a83310120d330d340d351d331d341d
352f012f022d04201e201f29292d333e013e023f043019301e301f30213d
343d35480d482a540b560d57105629562b1d1f011f021b331f351b365418
5419541a59325c335c345c355c365a370e030b0b29130b1b29230b203a3b
29303a7212721389249807982f9930a82fc028c12ac62bc03af03a144e08
381b006f021baf01cf0102017f010101ba00b8034b400d359a311c1b1d6f
1f1b1e1eba1db8034b4034199a142a2b2b3c0c0e140c0c0e2b0c2a0e0426
092b0c2a0e04062301fd0000062831032328140902ac01401e223401011f
260126b8012340102f11bf1102df11012011af11df110311b80287b71fac
1e2b10090109b80123401f9f2e01bf2eef2eff2e032e404735402ecf2eef
2e03002e202e302ec02e042ebc014600390146011800182b4e10f45d5d2b
71724ded72f4edfd5d7172fd72392f2bed003fed3fed3c10ed1112173901
11121739870e2e2b0e7d10c4180010ecf4ed0110edf4ed0010ecf4ed5d01
1071edf4ed3130437940362430071328260b2c093300290f263301241326
330107300933000a2d0c33000b0c2c2b27102a33010f0e292a2512233300
082f063301002b2b103c103c2b103c103c2b012b2b2b2b2b8181015d0072
5d43584009630b660d6710632b045d595d0171722b0071005d435c58400c
0b180f3904300f3933300f39002b2b2b591b40133535311919310202311e
1e143138031d093106b807f1b46c31031423b807efb26c140900183f2b3f
2b3f3f1112392f11392f11392f11392f3031590111232e02232206151417
16171e021514062322272626232206072311331e02333236353426272624
2626353436333217163332363703ab25125dac5c68882b3ee9be8b4befbc
3b341fc31a191d0725251a58b56c7d91373a27fea4934ce0ad6c7938171a
210a056bfe2b87a05e7f513e334b7d666d94519adf09053f1e2f01d19291
60845a32662c1ec3748c5492d335191f2f00>RVGGZC+TimesNewRomanPSMT AddT42Char 
2 12990 72 <0002004cffe4035303b00014001d03b4b0852b58b1020243545840280816
1415000c0f100255000e0c0f1002550e0c0d0d02550e1530400001200030
0002000010000200b8ffc0b41314025500b8ffc040111111025500000b1b
251107000710070207b8ffc0b40f10025507b8ffc0b5131402550704b8ff
d6b41314025504b8ffcab71212025504310b0b003fed2b2bc42b2b5d3fed
12392f2b2b5d5d5ded012f2b2bdd2bc02fcdc031301bb10602435458401d
158000a000b0000320003000400003000010000200000b1b2511070807b8
ffc040241010065510072007b00703000760078007a00704079204a204b2
040304310b0b07081614b8fff440260d0d065514141f1e15000c0d0d0655
000c0f0f0655000e0c0f0f06550e160d0d06550e0e1f1e1112392f2b2bdd
2b2bc01112392f2bcdd0cd003fed5dc45d5d2b323fed12392f5d5d5dcd31
301b4019125f185d1960006014d6030519201c3917201c3916401c391fb8
ffc0400a434a34081f430d5d361fb8ffc0b32828341fb8ffc040532a2e34
1b06190958135e165f175a185b1a07010309060709080c0515490689028c
06870c8a10851da302ab18b513d402d90fda10f402f30313126007600870
0780078909c107c80ff007080401070d84020309baffe00006ffe0404a36
09460247094f1f5402540962027202891389199913a409a40ab808b509b0
0ac702e702e00cf40a1408d007010007d007027107010007100720079007
a007b00706077d041400301615b8ffc040131239125f157f159f15df1504
15151bd3040104b8ffd0b2143904b8ffe8b2133904b8ffd8404812390431
0b0b5c1b011b25110707cc0816281b390f16016f167f168f160316f41414
800801300890080230088f08df08031008400860087008b008e0080608aa
0e15040089000200b8032c4012300e400e500e03000e100e200e03f00e01
0eb8ffc04009434a340e431e434b182b4e10f42b7172724dfd713c10fd5d
715d713c10ed5d712b10ed003fed723fed2b2b2b7211392f5d4358b26f15
015d592b3cfd3c10f45d5d7172393130015d00383800715d014358b40600
010202715971722b2b2b2b2b2b2b0072435c58b90007ffc0400b23390c40
2d390d402d3908b8ffc0b2283907b8ffc0b2283906b8ffc0b21b3907b8ff
c0b21b3908b8ffc0b21b3907b8ffc0b20a3908b8ffc0b20a3907b8ffc0b2
093908b8ffc0400e093915101939192011390d201139002b2b012b002b2b
2b2b2b2b2b2b2b2b2b2b5959591bb507070b111500b807e5b56c15150b11
1bb807ebb46c11070b04b8081fb26c0b0b00183f2b3f2b12392f2b111239
2f3031591306171633323637170606232202353412333216152521262726
26232206da016464875a852d1f15ca98a5ebf1b69ac6fd8701a805101963
365383023bcc747463781489e10101d9eb0107cbaa3a582438408100>RVGGZC+TimesNewRomanPSMT AddT42Char 
2 14038 73 <0001004f0000037a058c002b0241b0852b58b1020243545840252d401010
02552d400f0f02552d400d0d02551b2b01100e0601080e2901080d0d0255
01120eb8ffea4012121202550e120d0d02550e0c0f0f02550e06ba03e200
0903e2400a0824251e1700000f290fb8011bb2120608002f3fedc010c03f
cded10eded012f2b2b2bc0dd2bc010c410c610c610c6c431302b2b2b1bb1
0602435458b9000f011bb2120600b8011b401d2906241e17000829010c0d
0d065501060f0f065501021010065501120eb8ffd8400b0d0d06550e060f
0f06550eb8ffdab7101006550e0e2d2c1112392f2b2b2bc0dd2b2b2bc000
2f3fcdcd3fed3fed31301b403e8b2099159926034403440c48198503850c
059a04012f2d7f21900690079f089f099e109e11b02d0910061007025f2a
5f2b021c080eb41e08922201b41e07b80308401f231e9f1ebf1e021e1124
2517012b50100110302a2912110608070a101b011bb80152b38f2d012db8
02f6b2012a2bb80110400d282901120f1110920f0f01240eb8ffc0b36060
340eb8ffc0b33a3a340eb8ffc0b33f3f340eb8ffc0b32431340eb8ffc040
161c2134900e01000e100e5f0e700ec00ed00e060e192cba030603070018
2b4e10f45d722b2b2b2b2b4ded3c10f43c103c103c3cf43c10e65de47200
3f3c3f3c3c3cfd723c3ffd11395d2f2b2b31304379401225271416262515
262516281c002714241c012b012b2b2b81810172715d0072715d59591bb1
1724b807ec40096c1e1e111700001110b807ebb66c291106050809b803e2
b26c080a00183f2b323f332b323f12392f2b303159011114171633331521
353332363635112335333534363633321716151406232226262726232206
061515331501a61c253e53fddd29284219b2b258b57169583a341e17334a
1f1f262e401cec034cfda680222c2424284462025a483c89be75442d381e
35216d13133167d64248>RVGGZC+TimesNewRomanPSMT AddT42Char 
3 862 76 <0002003c00000207058e000b0022026fb0852b58b10202435458b90024ff
c0401d0d0d0255120d080d0d02550d21181010025521180f0f0255211318
0309b8ffeeb41313025509b8ffe0b40d0d025509b8ffd6b40f0f025509b8
ffceb610100255090d18b8fff4b41313025518b8ffe2b40d0d025518b8ff
e0b40f0f025518b8ffd6b5101002551820b803e240174f216f217f210321
226f00010060060106400f0f025506b8ffc0b71313025506220613002f3f
d62b2b5dcd5d10dd5ded012f2b2b2b2bcd2f2b2b2b2bcd10c4c62b2b102b
c43130012b1bb10602435458400d20121010065521121010065506b8ffc0
b44b4b065506b8ffc0b44141065506b8ffc04019373706554006010006a0
060260060106000020212207130309b8fff6401c10100655090924230d02
101006550d020f0f06550d0c0d0d06550d18b8fff0b41010065518b8fff6
b40f0f065518b8fff0b70d0d0655181824231112392f2b2b2bcd2b2b2b11
12392f2bcd002f3fddcd3fcd5d71722b2b2b3130012b2b1b401990240160
2470249024a024f024052024502402402450240224b8ffc0b332323424b8
ffc0b3383a3424b8ffc0b32d303424b8ffc0b323253424b8ffc0402e191a
3418291e134a220d291e124a2321271941201e21440c190c139006010639
0000220c0713120a900901093903b8ffc0b2433503b8ffc0400f3f35036b
0c0c0d190d2418402b3918b8ffc0401a363a349018015018016018701890
18a018f0180518b223b2a3182b10f65d71722b2bed3c103c10f42b2bed72
003f3c3f3c3fed7211123910f5edfc01f52b2b3130012b2b2b2b2b015d71
5d017259591bb900060831b74000002207111314b803e2b26c130a00183f
2b323f3f1aed303159013216151406232226353436131114161633152135
323636351134272626232207272501292a3b3b2a2a3c3b7e193141fe4343
2e1b09071e1a1c280e0114058e3b2a2a3c3c2a2a3bfe21fd2056391c2424
1a3c550161952c20190f2470>RVGGZC+TimesNewRomanPSMT AddT42Char 
3 2782 79 <0001003d0000020f058e001501acb0852b58b10202435458b90017fff640
1d0d0d0255140c06010701080d0d025501040f0f025501060c0c0255010c
b8fff2b4131302550cb8ffeab40c0c02550cb8ffe2b40d0d02550cb8ffd6
b4101002550cb8ffdeb50f0f02550c05bd03e2000803e20007001303e240
0b131440090d025514150007002f3fdd2b32ed10eded012f2b2b2b2b2bcd
2b2b2bc410c410c631302b1bb10602435458402713121010065514141010
065513141500000007010c0d0d065501021010065501040f0f0655010cb8
fff0b4101006550cb8fff4b40f0f06550cb8fff0b70d0d06550c0c171611
12392f2b2b2bcd2b2b2b002f3f3fddcd3130012b2b1bb79017c017f01703
17b8ffc0b33f463417b8ffc0403a393b340117b20d643650170140175017
601770179017a017f017070c291e074a2201291e06272314270d41131e14
4415000007060a0001240d0cb8ffc0b33f46340cb8ffc0401a353b34900c
01500c01600c700c900ca00cf00c050cb216b2a3182b10f65d71722b2b3c
fd3c003f3c3f3cf5edfc01f52b2b3130015d0171012b012b2b017259591b
b41500050708b803e2b26c070a00183f2b323f3031590111141616331521
3532363635113426262322072725017b193447fe3f3f2e1a0e1f181a2811
0111058efb4156381d24241a3c5503409b471a102370>RVGGZC+TimesNewRomanPSMT AddT42Char 
3 4564 81 <0001000c000003f703af00330304b0852b58b10202435458401735401212
0255300c10100255310c101002550e080f1623b8ffea402e10100255231d
242908080d0d025508040f0f025508060c0c025508162412120255161a0d
0d0255160c1313025516b8fff4b40f0f025516b8ffdeb41010025516b8ff
ee40260c0c025516001d040f0f02551d080d0d02551d060c0c02551d2918
12120255290e1313025529b8ffeeb41010025529b8fff0b40f0f025529b8
fff6b40d0d025529b8fffa400a0c0c025529001c022430b803e240093140
0910025531320dbe03e2001003e2002203e2002503e24009240f2432071a
2c0207003fed3f2f2f10ededecec10dd2bed11123939012f2b2b2b2b2b2b
dd2b2b2bc02f2b2b2b2b2b2bcd2b2b2b10c410c42b10c410c431302b2b2b
1bb10602435458405e2f1610100655300c10100655311610100655001c02
24303132071a2c02070f24080c0d0d065508021010065508060f0f065508
16020d0d065516021010065516080f0f065516163534001d0c0d0d06551d
080f0f06551d02101006551d29b8fff0b40d0d065529b8fff0b410100655
29b8fff2b70f0f0655292935341112392f2b2b2bdd2b2b2bc01112392f2b
2b2bcd2b2b2b002f2f3fed3fddcd111239393130012b2b2b1b403a35402a
350835600d5d3630355035603570359035052d0401403560357035803590
35b03506b035d03502b0350160358035c035031d0816291e0fb8030f4011
2229291e244a2208291e0e4a231d291e23b8030e402e2331272a41301e31
441c00233233071a2c02072423230f0f0e0a17162407900801b008010f08
70089f08cf080408b802bd401b29331d242a1f2950296029702904802990
29b02903002910290229b8ffc04009141634296034a67f182b10f62b5d71
723cfd3c10fd5d71723cfd3c003f3c103c103c3fed3f3c113939f5edfc01
f52b2b2b2b3130437940121819030604251903171c01050618051a1c012b
01103c2b2b8181015d71015d71005d01722b2b59591bb532070f0a021ab8
080c40096c020722100d032425b803e2b46c0f0a240a00183f3f2b17323f
2b3f3f303159013633321617161511141716163315213533323637363511
34262322071114171616331521353332363511342626232207272533014b
a1924b6c20160e0b3142fe3b1340330a04414d77760b0e314bfe3b144631
0f1f1a1c270f01142b02edc24b563c7cfe79571f191c242427260f4f0177
7d7182fe1d5d161d1b242447640154a5481a0f247000>RVGGZC+TimesNewRomanPSMT AddT42Char 
3 5486 82 <00020045ffe403b903af000f001d022db0852b58b10202435458401c140c
06101002550c0c0f0f02550c0c0d0d02550c100b0b02550c1a04b8fff4b4
1010025504b8fff440130b0b0255040c0f0f0255041725080b1025000700
3fed3fed012f2b2b2bcd2f2b2b2b2bcd31301bb106024354584009102500
071725080b1ab8fff4401b0d0d06551a04140c0d0d0655140c100f0f0655
0c100d0d06550c04b8fff0400b0d0d065504041e0c0c1f1e1112392f1139
2f2b102b2bcd2b10cd2b003fed3fed31301b404512801501a716b616c501
c909c41dd9090612e70a0148094516571585018c09890fd91b071f403235
041f430d5d369f1f01c615c91a02401f014908102500071725080b1204b8
ffc0402b120b3f4f0401400401d0040140045004600470049004b0040604
ec0c40120b3f400c9f0c020c431e434b182b4e10f4722b4ded5d5d71722b
4bb028534bb050515ab10c1e49b11f0449525a58bd000cffc00004ffc000
1fffc0383838594358bc001a0332000400140332e910e91bbc001a033200
0400140332ed10ed59003fed3fed313043794036011d12250e2602251c26
0a250626110f1420001d011a2001160914200018071a2001130d1020011b
03102001150b17200019051720002b2b2b2b012b2b2b2b2b2b2b2b2b2b81
01720171722b2b71015d0143584011750275067a0a7a0e7a127816751875
1c085d595d005d435c5840091c1011391b10113915b8fff0b10b39002b2b
2b5959591bb10010b807eab46c00070817b807ebb26c080b00183f2b3f2b
303159013217161514060623222726353436361722060615141233323635
3427260200d07e6b76cf7fcf7a677dcc53356b429f82617e694703af9e87
af7bfc80a58bad7ef977413f9e7cc8fedea0c3f48c60>RVGGZC+TimesNewRomanPSMT AddT42Char 
3 8772 87 <00010014fff1023c04c1001b0228b0852b58b1020243545840251d401213
02551d40101002550b0c18121202550c15130105131812120255130e1313
025513b8fff8b40f0f025513b8fff4b40d0d025513b8fff0400c10100255
130b082c0f161404b8011bb2000106003fcdfdd0cd2fedc4012f2b2b2b2b
2bddc010c62f2bcd31302b2b1bb106024354584019170c10100655160c10
100655150c10100655160c101006551bb8ffe8b4101006551ab8ffe8b410
10065519b8ffe8401410100655700b010b0f1b01156914014914011404b8
011b401c0106082c0f0b1b0105021010065505080f0f0655050c0d0d0655
0513b8ffeeb41010065513b8fff0b40f0f065513b8fffab70d0d06551313
1d1c1112392f2b2b2bdd2b2b2bd0cd003fed3ffdd05d5dc010cd10c45d31
30012b2b2b2b2b002b2b1bb9000dffe840410c395f015f02023f1d991199
19bf15bf16b819e819079f1d01891a014f0c4f0d5f0c5f0df51805061815
18271803161518191a030118191a03141ba00103153004b8011b401c0103
30020201060c35082c0f0b16cf15df15ef15031565141bcc000bb801ec40
2c200c010c2e2f1db01d021d000101040405241450130180130100131013
b013c013d013e0130613601cab89182b10f65d71723cfd3c103c103c105d
f45ded10ed10f45d3c003ffde43f3c10ed10edfd3c10e401111739001117
391239313000715d0171725d00722b59591bb61b014014160104b807ecb4
6c01060f08b80809b26c0f0b00183f2b3f2b39391a10cd30315901113315
231114163332363733060623222626351123353636373637014ad6d63328
213e11272380442e582a9137732d172904c1fed346fdae593e2928626333
5f630268211669482665>RVGGZC+TimesNewRomanPSMT AddT42Char 
RVGGZC+TimesNewRomanPSMT /CharStrings get begin
/g3 3 def
/g36 36 def
/g54 54 def
/g72 72 def
/g73 73 def
/g76 76 def
/g79 79 def
/g81 81 def
/g82 82 def
/g87 87 def
end
RVGGZC+TimesNewRomanPSMT /Encoding get
dup 32 /g3 put
dup 65 /g36 put
dup 83 /g54 put
dup 101 /g72 put
dup 102 /g73 put
dup 105 /g76 put
dup 108 /g79 put
dup 110 /g81 put
dup 111 /g82 put
dup 116 /g87 put
pop
systemdict /gcheck known {setglobal} if
end
%ADOEndSubsetFont
/RVGGZC+TimesNewRomanPSMT*1 
[32{/.notdef}rp /g3 13{/.notdef}rp /g17 2{/.notdef}rp /g20 /g21 14{/.notdef}rp 
/g36 10{/.notdef}rp /g47 /g48 2{/.notdef}rp /g51 2{/.notdef}rp /g54 
17{/.notdef}rp /g72 /g73 2{/.notdef}rp /g76 2{/.notdef}rp /g79 /.notdef 
/g81 /g82 4{/.notdef}rp /g87 139{/.notdef}rp]
RVGGZC+TimesNewRomanPSMT nf
RVGGZC+TimesNewRomanPSMT*1 [14.275 0 0 -14.275 0 0 ]msf
624.641 387.187 mo
(Self Attention)
[7.49438 6.73779 3.75439 4.49634 3.74005 9.77844 3.75415 4.48248 5.99548 6.75208 3.75427 4.48236 
6.75208 0 ]xsh
431.981 354.257 mo
732.451 354.257 li
735.581 354.257 738.121 351.727 738.121 348.597 cv
738.121 195.407 li
738.121 192.277 735.581 189.737 732.451 189.737 cv
431.981 189.737 li
428.851 189.737 426.311 192.277 426.311 195.407 cv
426.311 348.597 li
426.311 351.727 428.851 354.257 431.981 354.257 cv
1 /0 /CSD get_res sepcs
.071 sep
ef
1.5 lw
663.5 410.737 mo
663.5 398.417 li
1 /0 /CSD get_res sepcs
1 sep
@
659.481 398.467 mo
663.5 394.447 li
667.521 398.467 li
659.481 398.467 li
cp
ef
495.831 410.867 mo
495.831 360.957 li
@
491.81 361.007 mo
495.831 356.987 li
499.851 361.007 li
491.81 361.007 li
cp
ef
%ADOBeginSubsetFont: FBAAAA+TimesNewRomanPSMT AddGlyphs
ct_T42Dict begin
systemdict /gcheck known {currentglobal RVGGZC+TimesNewRomanPSMT gcheck setglobal} if
2 7854 53 <0002002300000568054c00280034024db0852b5840b224180f0f0255250c
0f0f0255872201128526c523c52d034924a72d02181f172e662403090109
252625470058016f026f247b017b02731f7320762278258a018720982dab
01ab25b726bc2dff2415062084018c2484279a24a501a402a624af2dbf2d
d830ef2dff2d0d120016011a0212281a301a313a2e3a306624692f0a2a08
021c1c01151f1b0f21220025281b00081f1b0e2123161f1b1c212340022c
2524242202011402020124ac022002072a29a507b8ffc040170f0f025507
100750076007039007a0070207001bac1c34b80191400f32281d1d1c020f
0e0e010100081221b8ffc0b2583521b8ffc040454f350021af21024f21a0
210221b510360140367036d036033634080613130255080c0f0f0255080c
0d0d0255082216150c10100255150c0f0f0255151a0d0d0255159e3561b9
011900182b4e10f42b2b2b3c4dfd2b2b2b3c105d72f45d712b2b4358b900
2f032de91bb9002f032ded59003f3c103c103c3f3c10eded10ed12395d72
2f2bfd3c103c191a10ed870e2e182b7d10c40112391a182b2b10ed0110c0
2b8710057dc43130184379401c2d311e231f252d232f3301311e2f33012e
222c330023243020323301002b103c2b012b2b2b81810172715d0072715d
435c58b90025ffe0b20c3901b8fff0b2143928b8ffe0b614390210193928
b8fff0b5103930100f39002b012b2b2b2b002b59015d2b2b1bb2242c04b8
07e940096c2c2c0f1c01081c34b807fcb26c1c32b807eeb26c1c1bb803e2
b66c1c02280c0f10b803e2b26c0f0800183f2b32323f2b2b2b3f1112392f
2b3230315921210106232226271114171633331521353332373635113427
262323352132161615140607011616170132163332363534262322070568
fe96fe3533200d1e101c264c35fdbb335625151c274d3301eed8cd8fa3ab
0118608a6ffc3d131c09c2c59f833a63027a020101fe76801f2c2525381f
74036c801f2c253fa9757db826fe7b86580c029401a8827f9f13>RVGGZC+TimesNewRomanPSMT AddT42Char 
2 12228 71 <00020044ffe40405058e001f002d0272b0852b58b1020243545840262f40
101002552906180d0d025506080f0f0255060c101002550600201d160a0d
0d0255160b20b8fff4401112120255200c1313025520180d0d025520b8ff
f8400c0f0f0255201810100255201cba03e2001dffc0b6091002551d1f12
b803e240101340090e0255131400252509072c2c03002fed3fed3fdd2bed
2fdd2bed012f2b2b2b2b2bc0dd2bc410c02f2b2b2bcd31302b1bb1060243
545840521213140000200b0303252509071c701d01401d601d021d1f0b2c
2c030b160c0d0d0655160410100655160b20141010065520040f0f065520
020d0d065520202f2e290c0d0d06552906180d0d065506062f2e1112392f
2bcd2b1112392f2b2b2bc0cd2b2b003fed3fdd5d5dcd3fed1217393fddcd
31301bb9002fffc0b34747342fb8ffc040422b2e34602f7c047c058a0480
2faf2fc02f07402f802f02002f162a152b55055508542b96070748070120
2f370a470a560a9804a72aa02f07c02ff02b022020002021baffe0000bff
e040453c204f205e20660a6c207a209f009f20aa07b907c62a0b26081327
0c41121e1344151d2716411c1e1d441f0020210b042c1500252509071f2c
012c2c1f030b1f000b210c20b8016740121560168016af16031f16901602
16eb295006b8ffc0b3282e3406b8ffc0b7473506432e437f182b4e10f42b
2b4dedfd725d3cfd3c3c3c3c3c003f3ced723fed3f11173910f5edfc01f5
0010f5edfc01f531304379401a262b0408272526082920002b0429200028
072520012a052c2000002b2b012b2b2b8181005d3838383801715d007101
72715d2b2b59591bb514001f0b0925b807e9b46c0907032cb80805b26c03
0b00183f2b3f2b3f3f303159250606232226353412333217353426262322
072725331114161633323717052335112e0223220706151416333202c743
804a96e0f8c3794f0f20181a2b0d01112d0f21161b2d0bfef02e063c632f
58455bb06c5b67463dfbc5c501474da99d481a102370fbdda1471c112371
c901d84470394f68c8cad700>RVGGZC+TimesNewRomanPSMT AddT42Char 
3 0 75 <0001000d000003f3058e003602bdb0852b58b10202435458401d38401212
0255100a110a080d0d02550a182412120255181a0d0d025518b8fff8b40f
0f025518b8ffe0400c10100255180e131302551826b8ffea401f10100255
26213435272d0121040c0c025521080d0d0255212d18121202552db8fffa
b40c0c02552db8fff6b40d0d02552db8fff4b40f0f02552db8ffec400f10
1002552d0e131302552d0120040f410a03e2001203e2002503e2002803e2
0027003403e2400f3540090d025535360027111d2c0407003fed2f2f3fdd
2bed10ededecec123939012f2b2b2b2b2b2bdd2b2bc010c4c63210c42b2f
2b2b2b2b2bcd2bc410c431302b1bb1060243545840583412101006553512
1010065501200427343536001d2c040711270a02101006550a060f0f0655
0a0c0d0d06550a18021010065518060f0f0655180c0d0d06551818383701
21021010065521060f0f0655210c0d0d0655212db8fff0b4101006552db8
fff2b40f0f06552db8fffcb70d0d06552d2d38371112392f2b2b2bdd2b2b
2bc01112392f2b2b2bcd2b2b2b002f2f3fed3fddcd111239393130012b2b
1b402f38402a350a38600d5d360f250f268038903804b038c038d038032b
0601503860387038903804403801200818291e11b8030f4011222d291e27
4a220a291e104a2321291e26b8030e402e2335272e41341e354401202736
00001d2c04072726261111100a19182409900a01b00a010f0a700a9f0acf
0a040ab802bd40252d0021242e1f2d502d602d702d04802d902d02b02d01
002d102dc02dd02d042d6037a67f182b10f65d5d71723cfd3c10fd5d7172
3cfd3c003f3c103c103c3fed3f3c113939f5edfc01f52b2b2b2b31304379
40141a1c050806251b261c05191c0107081a071d1c012b01103c2b2b2b81
81017172005d015d712b2b59591bb53600270a041db8080a40096c04070f
2528031112b803e2b26c110a00183f2b17323f2b3f3f3031590111363633
321617161511141716163315213533323637363511342626232206071114
1616331521353237363635113426262322072725014d6f82414e701b130e
0a3040fe3e1540320a031f4430316a4a153946fe3a3d2314180f1f1a152f
0e0112058efd627a45565c40aafebc5720181c24242726104e0144965e2f
344ffe1c5e2e1f2424130a3856033d9d481a10237000>RVGGZC+TimesNewRomanPSMT AddT42Char 
3 10128 89 <00010011ffe403ed0394002002eab0852b58b10202435458b60909001a12
0614be03e2001103e2002003e2000203e2b10006003fededecec3f2f1239
012f31301bb106024354584031180a091b080909222109001a0b14161010
0655141306112a1010065511120602161010065502010620161010065520
0006003fcd2b3fcd2b3fcd2b3fcd2b3f1239011112392fddcd10ddcd3130
1b400912530a58185b190319b8ffd8b20b3522b8ffc0406115351419141a
2309220a2111201224182019201a3a09390a3a12391835193a1a4a084909
440a45184519491a69089c0899099d1a9a1b9f22a900a808a509a219a21a
a81bbe08b509b60ab618b719ba1abb1bc022d518f60af618fb1a2d9f0901
22b8ffc0b332603422b8ffc0b32b313422b8ffc0b31e293422b8ffc0b347
473422b8ffc0b327273422b8ffc0b323233422b8ffc0b311113422b8ffc0
4040191c340f227c007201720270057c20810585118f22093a08340a3418
391bc606c021d81a07880a891887190337124818021318141e13001b201e
00120a111e12b8ff86402c091a192018191930090a1409090a1b1a1a2409
0814090908070605040408021e01131212010100061a190b18b8011d4012
5f0a01100a240a9f0ab60ad40a050a7d091bb80167401040062fa008b908
ce0803087d0919751abb011b00200009ffc0b30f123409b8ffc0b3191d34
09b8ffc0b2323509b8ffc0b70c350009c0090209b801bfb6102201802201
22b8ffc0b3191d3422b8ffc0b60f133421ab89182b19102b2b7172f45d2b
2b2b2b1afd18e61910f45d18f41aed1910f45d7218ed003f3c3f3c103c10
3c10ed01111739872e2b0e7d10c487052e182b0e7d10c42b180010ed0110
c00010ed0110c00010ed0110c03130015d5d5d712b2b2b2b2b2b2b2b005d
015d2b2b0172435c58b50a20160d3f08b8ffe8b7160d3f09240b3918b8ff
e0b213390ab8ffe0400a1339082013391b201339012b2b2b2b002b012b2b
5959591b400d091a0012061a0b201114030003b803e2b26c000600183f2b
17323f3f1112393031591321152322061514171313363534272626233521
150607060701230126262726271101af1c272915d5d617080b2234012b34
14231cfebb29feb916281f113203942526202330fe06020d381d0e090f0b
252504111e46fcee0305362f10090800>RVGGZC+TimesNewRomanPSMT AddT42Char 
3 10984 90 <0001000dffe405b40394002c03fdb0852b58b10202435458b626211e110e
022cb803e2400e00092618080428251f060f060006003f3f3f2f2f173910
fdd0d0d0d0c0012f31301bb10602435458b90026ffe840440d0d0655181c
0d0d0655081c0d0d06551810101006550810101006550818260904002821
1e110e02792c012c00752501250b752801280b1f060f0600062c2c2d2121
2e2d1112392f11392f003f3f3f3f5d3f5d10dd5dd0d0d0d0c01112173931
302b2b2b2b2b1bb1122eb8ffc0401c3f351627201020112527202e5f2e69
09702ee925e928f825f8280c2eb8ffc0b213352eb8ffc040c81b1f34212e
2e2964361d19191f1b23102e040a261d262c2639265517a717a718a72608
0b25372437274f004c014d074908472446274d284d298807801080118d25
88288829802e9a109417a718a725bb10b925b928bf2ec825c828d925d928
d02e1f000504070615041709250727092806293517431043115005520756
185229890b8f1088188919892388258826802e17870986178726030d0959
01771077110409090826262725250a0107021e011017111e102023211e20
00292c1e000f0a0e1e0f1f191e1e1fb8ff86b308282720b8ff7d40401825
242008070809072429281429292826272625273008091408080918151819
15240a25140a0a25232424301819141818192926231918170a0908070a00
2821bb01ec0020001e01ecb31f010f11bb01ec0010000e01ec400a0f0f10
101f1f20200002bb01ec0001002c01ecb301000618bb016a0025000801a6
400f28402725252424280b20fc0f650a01b801b1b4c000652923b8010840
15401b2f501901a01901bd19cf19df19031992242f18b8011bb7200f2501
10250125b8ffc0b30b0c3425bb0110002600150167400c400a2f5f260140
2680260226b801ecb4097d272f08ba011b0008011b400a200028018028f0
280228b8ffc0b50b0c3428a007b80167401b502901802901002910292029
4029b029c029d0290729602dab89182b10f65d7172edf42b5d71191aedfd
e4f4ed5d7118f41aed1910f42b5d711afde4f45d717218e41aed10f41aed
10f4ed003f3c103c103c1a10ed10ed3f3ced10ed103c103c103c103c10ed
10ed103c10ed10ed1112173987052e2b0e7d10c4870e2e182b087d10c487
052e182b087d10c4870e2e182b087d10c42b2b180010ed0110c00010ed01
10c00010ed0110c00010ed0110c00010ed0110c00010ed0110c00710083c
083c3130015d5d71015d005d01722b2b2b015d2b435c58b52610140c3f24
b8fff0b3140c3f13b8ffe0b21d3917b8ffe0b21d3917b8ffe0b2143917b8
fff0b2173925b8fff0b2153917b8fff0b11539012b2b2b2b2b2b2b2b5959
591b400d0818260328020e111e2105002cb803e2b76c1f0f000625280b00
183f333f33332b1732121739303159132115060615141713132726272627
352115060706151417131336353426273521150607012303012301262627
0d0180352111c4c5341827163c01b4481e1408d0c114273901215729fece
29e5fef525feda1d383c039425041e1c1f2cfdf101ad873c170e03252503
1710231415fdf201fb3620131e0225250d69fceb0249fdb7030249330d00
>RVGGZC+TimesNewRomanPSMT AddT42Char 
RVGGZC+TimesNewRomanPSMT /CharStrings get begin
/g53 53 def
/g71 71 def
/g75 75 def
/g89 89 def
/g90 90 def
end
RVGGZC+TimesNewRomanPSMT /Encoding get
dup 82 /g53 put
dup 100 /g71 put
dup 104 /g75 put
dup 118 /g89 put
dup 119 /g90 put
pop
systemdict /gcheck known {setglobal} if
end
%ADOEndSubsetFont
/RVGGZC+TimesNewRomanPSMT*1 
[32{/.notdef}rp /g3 13{/.notdef}rp /g17 2{/.notdef}rp /g20 /g21 14{/.notdef}rp 
/g36 10{/.notdef}rp /g47 /g48 2{/.notdef}rp /g51 /.notdef /g53 
/g54 16{/.notdef}rp /g71 /g72 /g73 /.notdef /g75 /g76 
2{/.notdef}rp /g79 /.notdef /g81 /g82 4{/.notdef}rp /g87 /.notdef 
/g89 /g90 136{/.notdef}rp]
RVGGZC+TimesNewRomanPSMT nf
RVGGZC+TimesNewRomanPSMT*1 [12 0 0 -12 0 0 ]msf
477.991 348.307 mo
(Review)
[8.24417 5.24402 6 3 5.24408 0 ]xsh
645.472 348.307 mo
(Method)
[10.5002 5.24402 3.59497 6 6 0 ]xsh
663.221 337.147 mo
639.75 337.147 li
639.921 322.967 li
.025 .361 .527 0 cmyk
@
635.901 322.977 mo
639.971 318.997 li
643.94 323.067 li
635.901 322.977 li
cp
ef
663.221 337.147 mo
687.25 337.147 li
687.25 324.097 li
@
683.231 324.157 mo
687.25 320.137 li
691.271 324.157 li
683.231 324.157 li
cp
ef
496.541 337.147 mo
496.541 322.297 li
@
492.521 322.347 mo
496.541 318.327 li
500.56 322.347 li
492.521 322.347 li
cp
ef
663.5 370.547 mo
663.5 358.227 li
1 /0 /CSD get_res sepcs
1 sep
@
659.481 358.277 mo
663.5 354.257 li
667.521 358.277 li
659.481 358.277 li
cp
ef
%ADOBeginSubsetFont: FBAAAA+TimesNewRomanPSMT AddGlyphs
ct_T42Dict begin
systemdict /gcheck known {currentglobal RVGGZC+TimesNewRomanPSMT gcheck setglobal} if
2 4290 46 <00010022000005d8054c004302eeb0852b5840b87b0ebe0e026c00017f00
75027b0e763079357a36bf0aba0d086d00011204452e1164363602550265
028002894090029940b30db40eba33ba43d50dd7320d120b01030e020602
05328b0087329e00ac01a00ed132080b0001010002050c1f091e0d2a0025
012f093f094f098c00c634d900f2340f090b190b30013502334042405045
a601a302a540b602b60ab042cd00dc00d001d402d603eb00eb01f001f50a
f00cf20d18163316343432303454019900940d9632953409b10602435458
40212f0f221e3c1e454415001530020e300003271816191b180618082926
1b273b2702003f3c10fdc53f3c10fdc5111217397101111239392ffd3c1b
4039060d071b061e1f1b1821222f1f1b2821223c413d1b3c0504041b050f
1f1b1721231f1f1b2721233b343a1b3b010000220e0d140e0e0d410000b8
02c9405430341430303400010d3441054530004134043a0d01020c0b0a09
07070e700ebf0e020e2607040707161619ac183c3b3b2828273d3a3a2929
26ac27181717060605270205083c93040e30302f0480050170050105b802
38400c400d500d02800d01b00d010db802f9402c2f0f06131302550f0c0f
0f02550f0c0d0d02550f221f1e0c101002551e0c0f0f02551e1a0d0d0255
1e9e4445bc013c00210061011900182b2b4ef42b2b2b3c4dfd2b2b2b3cf6
5d7172fd5d713c103c103c10e4003f3f103c103c103c10fd3c103c103c10
3c103c103c10fd3c103c103c1112395d2f12173912173901121739870e2e
2b7d10c4870e2e182b7d10c4180010ed0110c02b2b10ed0110c00010ed01
10c02b2b10ed0110c059313001725d71007172435840092f332d412f422d
43045d595d2b435c58400a3618160d3f0a20143932b8ffe0b6103940100e
3901b8ffe8b20e3900b8ffe0b20e3901b8ffc0b2103900b8ffc0b1103900
2b2b2b2b2b2b012b2b5901715d00715d1b400e300e0003182706082a3a3d
032726b803e2400a6c3b2702150704031819b803e2b26c180800183f2b17
323f332b17323f1112173930315901011616171521353236353426270111
141716171633331521353332373635113427262726232335211523220706
061511363700373635342623233521150e02070607026401f47bae57fd7b
3a331335fe2c0d0a202b302efdbe305426180d0a1f2c303002422e2f2c1f
18147501293e1b2a321f01f22c48684c16b502f0fe0f7b59062525271818
263401cffe4b6721191218252531207a036c6722181218252517104064fe
61136c01105b281e1723252501163f4614b9>RVGGZC+TimesNewRomanPSMT AddT42Char 
2 7416 52 <00020048fe6f0579056b00150026012cb0852b5840294501580795010306
0e015701580766017601860190009608c70fe50009040f40004201035608
039704b802d0402f0816281003001eac0808200030007000800004005208
080d032b223c1f132f13020013101320133013401305134928b8ffc0401a
3f352028402802281a3c100d200d020f0d1f0d020d49276463182b4e10f4
5d724ded4d10712bf65d724dede412392fed5d003fed3c3fed10f4ed3130
43794040092620251c260b0c0a0c020618252423252302061f15222d011d
091a2d00170f1a2d002611222d0121141e2d0015001b0c1e2d000908190e
162d012312162d012b2b103c2b103c2b012b2b2b2b2a2b2a2b2b8101715d
00715d1bb10403b807d7b46c0400001eb807e0b56c0800091016b807efb2
6c100300183f2b3f332b10c42b3031590516161715262424272627260235
10002120001114000122070611101716333237361134272626038666ed97
8afec6fee76690547a87018a0118010a0185feebfe7ab66f8c8e6eb5bc73
874a39bd0fb0a60c200565b3653a4161011bc101300192fe6dfecdf9fe88
04ea82a3feb0feb7b28989a2013cf3a68079>RVGGZC+TimesNewRomanPSMT AddT42Char 
2 9814 57 <00010012ffe105ae054c001f0237b0852b58b40a0f061f02b10202435458
b416011e100db803e2b70e1f0216070e0207002f3f12393f10fdd0d0c001
2f31301b400c1210210116080b39a9160121b8ffc0b2183521b8ffc0b333
353421b8ffc0b32c2f3421b8ffc04083202334f312fb1ff02103ba17b918
bb1ab021f90705a919ac1abc05b606b90705aa05a706a907aa15a716059b
07900f90129a16902105691564177404790a8021055a1657175021650669
07055b0759085b0a5e0e5915054021500054035705530605202134043815
4600490e0525062907280828152816050021202130216021d02105b10602
435458401c000e21200a161a162a160316070d011e100d1b0e0607010708
1f0e02003f3c3f5d10fdc5c5c51112395d01111239391b40140005011b00
0f15101b0f0e080d1b0e1f171e1b1fb8ff87401116070620080707221615
14161615050606b802c940351617141616171f0f0f0e0e0002070609fb17
0117e7301640169016f0160416e8301540155015b015f015052015601570
1580150415b802ebb6202196216b8a182b2bf45d5d19f45de45d00183f3c
3f3c103c103c87052e2b0e7d10c487052e182b0e7d10c42b180010ed0110
c00010ed0110c00010ed0110c00010ed0110c059313001715d5d5d5d5d5d
5d5d5d5d5d2b2b2b2b005d2b0172435c5840090a1812390f40123904b8ff
e8b610390808133907b8ffd8b613390a28133904b8ffd8b10f39012b2b2b
2b2b2b2b5959015d1bb71607101e01030e0db803e2b56c1f0e0207090018
3f3f332b1732123930315901150607060701230126272626273521150606
1514170101363534262726273505ae48253529fe2725fe04271019493e02
2a5e382e015901402f3a45050c054c250d213165fb7e04915a141f230525
25092e24326afce50311742d1d350b010225>RVGGZC+TimesNewRomanPSMT AddT42Char 
RVGGZC+TimesNewRomanPSMT /CharStrings get begin
/g46 46 def
/g52 52 def
/g57 57 def
end
RVGGZC+TimesNewRomanPSMT /Encoding get
dup 75 /g46 put
dup 81 /g52 put
dup 86 /g57 put
pop
systemdict /gcheck known {setglobal} if
end
%ADOEndSubsetFont
/RVGGZC+TimesNewRomanPSMT*1 
[32{/.notdef}rp /g3 13{/.notdef}rp /g17 2{/.notdef}rp /g20 /g21 14{/.notdef}rp 
/g36 9{/.notdef}rp /g46 /g47 /g48 2{/.notdef}rp /g51 /g52 
/g53 /g54 2{/.notdef}rp /g57 13{/.notdef}rp /g71 /g72 /g73 
/.notdef /g75 /g76 2{/.notdef}rp /g79 /.notdef /g81 /g82 
4{/.notdef}rp /g87 /.notdef /g89 /g90 136{/.notdef}rp]
RVGGZC+TimesNewRomanPSMT nf
RVGGZC+TimesNewRomanPSMT*1 [12 0 0 -12 0 0 ]msf
492.57 311.457 mo
(Q)sh
RVGGZC+TimesNewRomanPSMT*1 [12.025 0 0 -12.025 0 0 ]msf
635.861 311.427 mo
(K)sh
RVGGZC+TimesNewRomanPSMT*1 [12 0 0 -12 0 0 ]msf
684.091 311.307 mo
(V)sh
516.041 283.287 mo
576.171 283.287 li
579.301 283.287 581.831 280.747 581.831 277.617 cv
581.831 270.987 li
581.831 267.857 579.301 265.317 576.171 265.317 cv
516.041 265.317 li
512.911 265.317 510.371 267.857 510.371 270.987 cv
510.371 277.617 li
510.371 280.747 512.911 283.287 516.041 283.287 cv
.129 .073 0 0 cmyk
ef
.25 lw
516.041 283.287 mo
576.171 283.287 li
579.301 283.287 581.831 280.747 581.831 277.617 cv
581.831 270.987 li
581.831 267.857 579.301 265.317 576.171 265.317 cv
516.041 265.317 li
512.911 265.317 510.371 267.857 510.371 270.987 cv
510.371 277.617 li
510.371 280.747 512.911 283.287 516.041 283.287 cv
cp
.115 .032 .005 0 cmyk
@
1 /0 /CSD get_res sepcs
1 sep
%ADOBeginSubsetFont: FBAAAA+TimesNewRomanPSMT AddGlyphs
ct_T42Dict begin
systemdict /gcheck known {currentglobal RVGGZC+TimesNewRomanPSMT gcheck setglobal} if
2 10492 68 <00020049ffed038903af0032003d038bb0852b58b1020243545840203f40
0d0d02553f4013130255151b072e25080b0b0255250c0d0d025525000c33
b8fff0400b1212025533161313025533b8ffdeb41010025533b8fff44015
0f0f0255330c0d0d02553339070c0d0d0255072d2eb8ffc0402009120255
2e33001e04292c30340c40090b02550c401d1d02550c40111202550cb8ff
d4401e091202550c0c047f180118401112025518401d1d02551810251e07
3c2c04002fed3fedc42b2b5d12392f2b2b2b2bcd2ffd11123939d42bcd01
2f2bcd2f2b2b2b2b2bc0c0dd2b2bc410d4cd31302b2b1b406f0b1c8a3302
1253360112201f39803fa809b60a03122b127d007d3386008b0b8b35061d
12163a103f803f04091c4c054c06452045224c3a403f891d080a0e072000
2249014b0a490b49354b37433a493d570b670b8509840a840b0f54168316
021f3f5f3f0260083300343c2e292d34bb011b000c000cffc0b609390c28
0b390cb8ffc0401a3a35100c500c02400c500c600c03200c500c600c760c
040c3c18b8ffd840290b394f185f186f18032f187f1802187e1f10011025
1e07303c403c023c2c04702d802d022d35292c30b803464011040b2ec02d
012d602500330d0c0c343433b8fffcb41010065533bb016700240025ffc0
401a0e3900251f2580259025044025f0250280250125101010065525bb02
4300070015ffc0b21f3915b80167401e1b2f393107400e39200750078007
03100701f0070150070107433e436e182b4e10f45d7172722b4dedf4ed2b
10fd2b5d71722b3cfd2b3c103c103c103c10f65d3c003ff4fde45d10ed71
3fed72fd5d712b11395d71722b2b2b2fb10602435458b2030c01005d59ed
11123911123939313043794047353b1c23051337383638020609080a0802
06212220220206350b392000111d131c0012130f1f0d1c0122233b05391c
00380834200135340b121c101c010e22101c013a063c1c002b2b2b3c103c
2b012b103c2b103c2b2b2a2a2a818181017201710071017172005d4358b2
3f12015d59015d2b0072435c58b431400e392eb8ffe0b210392eb8ffe0b6
0e3937200e3920b8ffe8b20c3920b8ffe0400b0b3918200b3917200b391c
b8fff0401a0b390a280b3937280b390a280a3937280a390a280939372809
39002b2b2b2b2b2b2b2b2b2b2b2b2b2b2b59005d591bb51818041e0c34b8
07e8b56c0c0c301e10b807e8b46c1e073029b8080db46c300b043cb80809
b26c040b00183f2b3f2b3f2b12392f2b1112392f30315925060706232226
353437363637353426232207061517140623222635343633321716171615
1114161633323736371506232226271106070606151416333202478d2436
3d5f7b1e29cbec57533f2526022f26252fb09f7a4e3b1c120a170f100c15
3c7066313a01972c4f4456384c846d1119826a433144785624896622222c
3a2e32342d5690291f422b85fec9833b14070d3c38964493015d3c192c60
39485f00>RVGGZC+TimesNewRomanPSMT AddT42Char 
3 9412 88 <00010002ffe403fd039400250258b0852b58b10202435458401627401212
02550801080d0d0255010b20281212025520b8fffc400b0f0f0255201e0d
0d025520b8ffe4401310100255201a080d0d02551a121c1212025512b8ff
f8b40f0f025512b8fffab40d0d025512b8fff4b5101002551224ba03e200
1703e2400e1825060b200e18061d2c0e0b0708b8ffc0b509100255080a00
2fdd2bcd3fed3f1239393f10edec012f2b2b2b2bcd2b2f2b2b2b2bc0dd2b
c431302b1bb1060243545840570740086008700803080a0b200b180e2425
1718250618061d2c0e0b0b010810100655010a0f0f0655010c0d0d065501
201a040f0f06551a04101006551a0a0d0d06551a1208082620080f0f0655
20060d0d065520202612b8fff2b41010065512b8fff6b40f0f065512b8ff
f6b70d0d0655121227261112392f2b2b2b11392f2b2b11392f10cd2b2b2b
10cd2b2b2bc0003fed3f3f10cd10cd111239393fdd5dcd31301b40350127
600d5d36202760277027b02704340b371f3a20481f4820051a08134f1e18
2723214f1e25272308270141071e0844200b251d08b8014540130a002525
191918061d2c0e0e0a0b0a0b0b2120b80167400e00b001010f0170019f01
cf010401b802bd402512191a241212501390130280139013b01303001310
132013b013c013d01306136026c27f182b4e10f45d71723c4d10fd3c10fd
5d713cfd3c3c103c003f3c10ed3f3c103c103c10ed11123939f5edfc01f5
2b2b3130437940101b1c0f111c0f1a1c0010111b101d1c002b01103c2b81
81005d015d2b59591bb2241817b803e2b76c2518060a0b0e1db8080cb26c
0e0b00183f2b3f3f332b3230315901111416163332371705233506062322
2626351134262607352111141633323637113426273503630f21161f270e
feee2d767c454d712c1c37480141593f2b6d4b395a0394fdd59f471c1123
71c28042598c80019941321b0125fd9b8050364c02074e370225>RVGGZC+TimesNewRomanPSMT AddT42Char 
RVGGZC+TimesNewRomanPSMT /CharStrings get begin
/g68 68 def
/g88 88 def
end
RVGGZC+TimesNewRomanPSMT /Encoding get
dup 97 /g68 put
dup 117 /g88 put
pop
systemdict /gcheck known {setglobal} if
end
%ADOEndSubsetFont
/RVGGZC+TimesNewRomanPSMT*1 
[32{/.notdef}rp /g3 13{/.notdef}rp /g17 2{/.notdef}rp /g20 /g21 14{/.notdef}rp 
/g36 9{/.notdef}rp /g46 /g47 /g48 2{/.notdef}rp /g51 /g52 
/g53 /g54 2{/.notdef}rp /g57 10{/.notdef}rp /g68 2{/.notdef}rp /g71 
/g72 /g73 /.notdef /g75 /g76 2{/.notdef}rp /g79 /.notdef 
/g81 /g82 4{/.notdef}rp /g87 /g88 /g89 /g90 136{/.notdef}rp]
RVGGZC+TimesNewRomanPSMT nf
RVGGZC+TimesNewRomanPSMT*1 [12.025 0 0 -12.025 0 0 ]msf
526.971 278.257 mo
(MatMul)
[10.498 5.25494 3.73975 10.4979 6.01251 0 ]xsh
1.5 lw
505.041 308.957 mo
509.31 309.007 li
525.661 308.857 li
525.681 292.027 li
@
521.661 292.067 mo
525.69 288.057 li
529.701 292.087 li
521.661 292.067 li
cp
ef
630.94 308.707 mo
624.101 308.797 li
568.82 308.797 li
568.82 291.507 li
@
564.801 291.557 mo
568.82 287.537 li
572.841 291.557 li
564.801 291.557 li
cp
ef
546.101 265.317 mo
546.13 254.657 li
@
542.111 254.697 mo
546.151 250.687 li
550.151 254.717 li
542.111 254.697 li
cp
ef
615 231.717 mo
675.121 231.717 li
678.25 231.717 680.791 229.177 680.791 226.047 cv
680.791 219.417 li
680.791 216.287 678.25 213.747 675.121 213.747 cv
615 213.747 li
611.861 213.747 609.331 216.287 609.331 219.417 cv
609.331 226.047 li
609.331 229.177 611.861 231.717 615 231.717 cv
.129 .073 0 0 cmyk
ef
.25 lw
615 231.717 mo
675.121 231.717 li
678.25 231.717 680.791 229.177 680.791 226.047 cv
680.791 219.417 li
680.791 216.287 678.25 213.747 675.121 213.747 cv
615 213.747 li
611.861 213.747 609.331 216.287 609.331 219.417 cv
609.331 226.047 li
609.331 229.177 611.861 231.717 615 231.717 cv
cp
.115 .032 .005 0 cmyk
@
1 /0 /CSD get_res sepcs
1 sep
RVGGZC+TimesNewRomanPSMT*1 [12.025 0 0 -12.025 0 0 ]msf
626.01 226.607 mo
(MatMul)
[10.498 5.25494 3.73975 10.4979 6.01245 0 ]xsh
1.5 lw
686.461 297.297 mo
686.461 273.927 li
645.361 273.927 li
645.091 235.677 li
@
641.07 235.767 mo
645.06 231.717 li
649.111 235.707 li
641.07 235.767 li
cp
ef
520.181 205.547 mo
528.12 205.547 li
528.12 197.608 li
520.181 197.608 li
cp
.115 .032 .005 0 cmyk
ef
.25 lw
520.181 205.547 mo
528.12 205.547 li
528.12 197.608 li
520.181 197.608 li
cp
@
528.88 205.547 mo
536.82 205.547 li
536.82 197.608 li
528.88 197.608 li
cp
.172 0 .038 0 cmyk
ef
528.88 205.547 mo
536.82 205.547 li
536.82 197.608 li
528.88 197.608 li
cp
@
537.591 205.547 mo
545.53 205.547 li
545.53 197.608 li
537.591 197.608 li
cp
.115 .032 .005 0 cmyk
ef
537.591 205.547 mo
545.53 205.547 li
545.53 197.608 li
537.591 197.608 li
cp
@
546.301 205.547 mo
554.24 205.547 li
554.24 197.608 li
546.301 197.608 li
cp
ef
546.301 205.547 mo
554.24 205.547 li
554.24 197.608 li
546.301 197.608 li
cp
@
563.721 205.547 mo
571.66 205.547 li
571.66 197.608 li
563.721 197.608 li
cp
ef
563.721 205.547 mo
571.66 205.547 li
571.66 197.608 li
563.721 197.608 li
cp
@
555.01 205.547 mo
562.95 205.547 li
562.95 197.608 li
555.01 197.608 li
cp
.172 0 .038 0 cmyk
ef
555.01 205.547 mo
562.95 205.547 li
562.95 197.608 li
555.01 197.608 li
cp
@
520.181 214.007 mo
528.12 214.007 li
528.12 206.068 li
520.181 206.068 li
cp
.115 .032 .005 0 cmyk
ef
520.181 214.007 mo
528.12 214.007 li
528.12 206.068 li
520.181 206.068 li
cp
@
537.591 214.007 mo
545.53 214.007 li
545.53 206.068 li
537.591 206.068 li
cp
.172 0 .038 0 cmyk
ef
537.591 214.007 mo
545.53 214.007 li
545.53 206.068 li
537.591 206.068 li
cp
@
528.88 214.007 mo
536.82 214.007 li
536.82 206.068 li
528.88 206.068 li
cp
.115 .032 .005 0 cmyk
ef
528.88 214.007 mo
536.82 214.007 li
536.82 206.068 li
528.88 206.068 li
cp
@
555.01 214.007 mo
562.95 214.007 li
562.95 206.068 li
555.01 206.068 li
cp
ef
555.01 214.007 mo
562.95 214.007 li
562.95 206.068 li
555.01 206.068 li
cp
@
563.721 214.007 mo
571.66 214.007 li
571.66 206.068 li
563.721 206.068 li
cp
ef
563.721 214.007 mo
571.66 214.007 li
571.66 206.068 li
563.721 206.068 li
cp
@
546.301 214.007 mo
554.24 214.007 li
554.24 206.068 li
546.301 206.068 li
cp
.172 0 .038 0 cmyk
ef
546.301 214.007 mo
554.24 214.007 li
554.24 206.068 li
546.301 206.068 li
cp
@
520.181 222.467 mo
528.12 222.467 li
528.12 214.528 li
520.181 214.528 li
cp
.115 .032 .005 0 cmyk
ef
520.181 222.467 mo
528.12 222.467 li
528.12 214.528 li
520.181 214.528 li
cp
@
528.88 222.467 mo
536.82 222.467 li
536.82 214.528 li
528.88 214.528 li
cp
ef
528.88 222.467 mo
536.82 222.467 li
536.82 214.528 li
528.88 214.528 li
cp
@
537.591 222.467 mo
545.53 222.467 li
545.53 214.528 li
537.591 214.528 li
cp
ef
537.591 222.467 mo
545.53 222.467 li
545.53 214.528 li
537.591 214.528 li
cp
@
546.301 222.467 mo
554.24 222.467 li
554.24 214.528 li
546.301 214.528 li
cp
.172 0 .038 0 cmyk
ef
546.301 222.467 mo
554.24 222.467 li
554.24 214.528 li
546.301 214.528 li
cp
@
555.01 222.467 mo
562.95 222.467 li
562.95 214.528 li
555.01 214.528 li
cp
.115 .032 .005 0 cmyk
ef
555.01 222.467 mo
562.95 222.467 li
562.95 214.528 li
555.01 214.528 li
cp
@
563.721 222.467 mo
571.66 222.467 li
571.66 214.528 li
563.721 214.528 li
cp
.172 0 .038 0 cmyk
ef
563.721 222.467 mo
571.66 222.467 li
571.66 214.528 li
563.721 214.528 li
cp
@
520.181 230.927 mo
528.12 230.927 li
528.12 222.988 li
520.181 222.988 li
cp
ef
520.181 230.927 mo
528.12 230.927 li
528.12 222.988 li
520.181 222.988 li
cp
@
528.88 230.927 mo
536.82 230.927 li
536.82 222.988 li
528.88 222.988 li
cp
.115 .032 .005 0 cmyk
ef
528.88 230.927 mo
536.82 230.927 li
536.82 222.988 li
528.88 222.988 li
cp
@
537.591 230.927 mo
545.53 230.927 li
545.53 222.988 li
537.591 222.988 li
cp
ef
537.591 230.927 mo
545.53 230.927 li
545.53 222.988 li
537.591 222.988 li
cp
@
546.301 230.927 mo
554.24 230.927 li
554.24 222.988 li
546.301 222.988 li
cp
ef
546.301 230.927 mo
554.24 230.927 li
554.24 222.988 li
546.301 222.988 li
cp
@
555.01 230.927 mo
562.95 230.927 li
562.95 222.988 li
555.01 222.988 li
cp
ef
555.01 230.927 mo
562.95 230.927 li
562.95 222.988 li
555.01 222.988 li
cp
@
563.721 230.927 mo
571.66 230.927 li
571.66 222.988 li
563.721 222.988 li
cp
ef
563.721 230.927 mo
571.66 230.927 li
571.66 222.988 li
563.721 222.988 li
cp
@
520.181 239.387 mo
528.12 239.387 li
528.12 231.448 li
520.181 231.448 li
cp
ef
520.181 239.387 mo
528.12 239.387 li
528.12 231.448 li
520.181 231.448 li
cp
@
528.88 239.387 mo
536.82 239.387 li
536.82 231.448 li
528.88 231.448 li
cp
.172 0 .038 0 cmyk
ef
528.88 239.387 mo
536.82 239.387 li
536.82 231.448 li
528.88 231.448 li
cp
@
546.301 239.387 mo
554.24 239.387 li
554.24 231.448 li
546.301 231.448 li
cp
ef
546.301 239.387 mo
554.24 239.387 li
554.24 231.448 li
546.301 231.448 li
cp
@
537.591 239.387 mo
545.53 239.387 li
545.53 231.448 li
537.591 231.448 li
cp
.115 .032 .005 0 cmyk
ef
537.591 239.387 mo
545.53 239.387 li
545.53 231.448 li
537.591 231.448 li
cp
@
555.01 239.387 mo
562.95 239.387 li
562.95 231.448 li
555.01 231.448 li
cp
ef
555.01 239.387 mo
562.95 239.387 li
562.95 231.448 li
555.01 231.448 li
cp
@
563.721 239.387 mo
571.66 239.387 li
571.66 231.448 li
563.721 231.448 li
cp
.172 0 .038 0 cmyk
ef
563.721 239.387 mo
571.66 239.387 li
571.66 231.448 li
563.721 231.448 li
cp
@
520.181 247.857 mo
528.12 247.857 li
528.12 239.918 li
520.181 239.918 li
cp
.115 .032 .005 0 cmyk
ef
520.181 247.857 mo
528.12 247.857 li
528.12 239.918 li
520.181 239.918 li
cp
@
528.88 247.857 mo
536.82 247.857 li
536.82 239.918 li
528.88 239.918 li
cp
ef
528.88 247.857 mo
536.82 247.857 li
536.82 239.918 li
528.88 239.918 li
cp
@
537.591 247.857 mo
545.53 247.857 li
545.53 239.918 li
537.591 239.918 li
cp
ef
537.591 247.857 mo
545.53 247.857 li
545.53 239.918 li
537.591 239.918 li
cp
@
546.301 247.857 mo
554.24 247.857 li
554.24 239.918 li
546.301 239.918 li
cp
ef
546.301 247.857 mo
554.24 247.857 li
554.24 239.918 li
546.301 239.918 li
cp
@
555.01 247.857 mo
562.95 247.857 li
562.95 239.918 li
555.01 239.918 li
cp
ef
555.01 247.857 mo
562.95 247.857 li
562.95 239.918 li
555.01 239.918 li
cp
@
563.721 247.857 mo
571.66 247.857 li
571.66 239.918 li
563.721 239.918 li
cp
ef
563.721 247.857 mo
571.66 247.857 li
571.66 239.918 li
563.721 239.918 li
cp
@
520.181 205.547 mo
528.12 205.547 li
528.12 197.608 li
520.181 197.608 li
cp
ef
520.181 205.547 mo
528.12 205.547 li
528.12 197.608 li
520.181 197.608 li
cp
@
528.88 205.547 mo
536.82 205.547 li
536.82 197.608 li
528.88 197.608 li
cp
.172 0 .038 0 cmyk
ef
528.88 205.547 mo
536.82 205.547 li
536.82 197.608 li
528.88 197.608 li
cp
@
537.591 205.547 mo
545.53 205.547 li
545.53 197.608 li
537.591 197.608 li
cp
.115 .032 .005 0 cmyk
ef
537.591 205.547 mo
545.53 205.547 li
545.53 197.608 li
537.591 197.608 li
cp
@
546.301 205.547 mo
554.24 205.547 li
554.24 197.608 li
546.301 197.608 li
cp
ef
546.301 205.547 mo
554.24 205.547 li
554.24 197.608 li
546.301 197.608 li
cp
@
563.721 205.547 mo
571.66 205.547 li
571.66 197.608 li
563.721 197.608 li
cp
ef
563.721 205.547 mo
571.66 205.547 li
571.66 197.608 li
563.721 197.608 li
cp
@
555.01 205.547 mo
562.95 205.547 li
562.95 197.608 li
555.01 197.608 li
cp
.172 0 .038 0 cmyk
ef
555.01 205.547 mo
562.95 205.547 li
562.95 197.608 li
555.01 197.608 li
cp
@
520.181 214.007 mo
528.12 214.007 li
528.12 206.068 li
520.181 206.068 li
cp
.115 .032 .005 0 cmyk
ef
520.181 214.007 mo
528.12 214.007 li
528.12 206.068 li
520.181 206.068 li
cp
@
537.591 214.007 mo
545.53 214.007 li
545.53 206.068 li
537.591 206.068 li
cp
.172 0 .038 0 cmyk
ef
537.591 214.007 mo
545.53 214.007 li
545.53 206.068 li
537.591 206.068 li
cp
@
528.88 214.007 mo
536.82 214.007 li
536.82 206.068 li
528.88 206.068 li
cp
.115 .032 .005 0 cmyk
ef
528.88 214.007 mo
536.82 214.007 li
536.82 206.068 li
528.88 206.068 li
cp
@
555.01 214.007 mo
562.95 214.007 li
562.95 206.068 li
555.01 206.068 li
cp
ef
555.01 214.007 mo
562.95 214.007 li
562.95 206.068 li
555.01 206.068 li
cp
@
563.721 214.007 mo
571.66 214.007 li
571.66 206.068 li
563.721 206.068 li
cp
ef
563.721 214.007 mo
571.66 214.007 li
571.66 206.068 li
563.721 206.068 li
cp
@
546.301 214.007 mo
554.24 214.007 li
554.24 206.068 li
546.301 206.068 li
cp
.172 0 .038 0 cmyk
ef
546.301 214.007 mo
554.24 214.007 li
554.24 206.068 li
546.301 206.068 li
cp
@
520.181 222.467 mo
528.12 222.467 li
528.12 214.528 li
520.181 214.528 li
cp
.115 .032 .005 0 cmyk
ef
520.181 222.467 mo
528.12 222.467 li
528.12 214.528 li
520.181 214.528 li
cp
@
528.88 222.467 mo
536.82 222.467 li
536.82 214.528 li
528.88 214.528 li
cp
ef
528.88 222.467 mo
536.82 222.467 li
536.82 214.528 li
528.88 214.528 li
cp
@
537.591 222.467 mo
545.53 222.467 li
545.53 214.528 li
537.591 214.528 li
cp
ef
537.591 222.467 mo
545.53 222.467 li
545.53 214.528 li
537.591 214.528 li
cp
@
546.301 222.467 mo
554.24 222.467 li
554.24 214.528 li
546.301 214.528 li
cp
.172 0 .038 0 cmyk
ef
546.301 222.467 mo
554.24 222.467 li
554.24 214.528 li
546.301 214.528 li
cp
@
555.01 222.467 mo
562.95 222.467 li
562.95 214.528 li
555.01 214.528 li
cp
.115 .032 .005 0 cmyk
ef
555.01 222.467 mo
562.95 222.467 li
562.95 214.528 li
555.01 214.528 li
cp
@
563.721 222.467 mo
571.66 222.467 li
571.66 214.528 li
563.721 214.528 li
cp
.172 0 .038 0 cmyk
ef
563.721 222.467 mo
571.66 222.467 li
571.66 214.528 li
563.721 214.528 li
cp
@
520.181 230.927 mo
528.12 230.927 li
528.12 222.988 li
520.181 222.988 li
cp
ef
520.181 230.927 mo
528.12 230.927 li
528.12 222.988 li
520.181 222.988 li
cp
@
528.88 230.927 mo
536.82 230.927 li
536.82 222.988 li
528.88 222.988 li
cp
.115 .032 .005 0 cmyk
ef
528.88 230.927 mo
536.82 230.927 li
536.82 222.988 li
528.88 222.988 li
cp
@
537.591 230.927 mo
545.53 230.927 li
545.53 222.988 li
537.591 222.988 li
cp
ef
537.591 230.927 mo
545.53 230.927 li
545.53 222.988 li
537.591 222.988 li
cp
@
546.301 230.927 mo
554.24 230.927 li
554.24 222.988 li
546.301 222.988 li
cp
ef
546.301 230.927 mo
554.24 230.927 li
554.24 222.988 li
546.301 222.988 li
cp
@
555.01 230.927 mo
562.95 230.927 li
562.95 222.988 li
555.01 222.988 li
cp
ef
555.01 230.927 mo
562.95 230.927 li
562.95 222.988 li
555.01 222.988 li
cp
@
563.721 230.927 mo
571.66 230.927 li
571.66 222.988 li
563.721 222.988 li
cp
ef
563.721 230.927 mo
571.66 230.927 li
571.66 222.988 li
563.721 222.988 li
cp
@
520.181 239.387 mo
528.12 239.387 li
528.12 231.448 li
520.181 231.448 li
cp
ef
520.181 239.387 mo
528.12 239.387 li
528.12 231.448 li
520.181 231.448 li
cp
@
528.88 239.387 mo
536.82 239.387 li
536.82 231.448 li
528.88 231.448 li
cp
.172 0 .038 0 cmyk
ef
528.88 239.387 mo
536.82 239.387 li
536.82 231.448 li
528.88 231.448 li
cp
@
546.301 239.387 mo
554.24 239.387 li
554.24 231.448 li
546.301 231.448 li
cp
ef
546.301 239.387 mo
554.24 239.387 li
554.24 231.448 li
546.301 231.448 li
cp
@
537.591 239.387 mo
545.53 239.387 li
545.53 231.448 li
537.591 231.448 li
cp
.115 .032 .005 0 cmyk
ef
537.591 239.387 mo
545.53 239.387 li
545.53 231.448 li
537.591 231.448 li
cp
@
555.01 239.387 mo
562.95 239.387 li
562.95 231.448 li
555.01 231.448 li
cp
ef
555.01 239.387 mo
562.95 239.387 li
562.95 231.448 li
555.01 231.448 li
cp
@
563.721 239.387 mo
571.66 239.387 li
571.66 231.448 li
563.721 231.448 li
cp
.172 0 .038 0 cmyk
ef
563.721 239.387 mo
571.66 239.387 li
571.66 231.448 li
563.721 231.448 li
cp
@
520.181 247.857 mo
528.12 247.857 li
528.12 239.918 li
520.181 239.918 li
cp
.115 .032 .005 0 cmyk
ef
520.181 247.857 mo
528.12 247.857 li
528.12 239.918 li
520.181 239.918 li
cp
@
528.88 247.857 mo
536.82 247.857 li
536.82 239.918 li
528.88 239.918 li
cp
ef
528.88 247.857 mo
536.82 247.857 li
536.82 239.918 li
528.88 239.918 li
cp
@
537.591 247.857 mo
545.53 247.857 li
545.53 239.918 li
537.591 239.918 li
cp
ef
537.591 247.857 mo
545.53 247.857 li
545.53 239.918 li
537.591 239.918 li
cp
@
546.301 247.857 mo
554.24 247.857 li
554.24 239.918 li
546.301 239.918 li
cp
ef
546.301 247.857 mo
554.24 247.857 li
554.24 239.918 li
546.301 239.918 li
cp
@
555.01 247.857 mo
562.95 247.857 li
562.95 239.918 li
555.01 239.918 li
cp
ef
555.01 247.857 mo
562.95 247.857 li
562.95 239.918 li
555.01 239.918 li
cp
@
563.721 247.857 mo
571.66 247.857 li
571.66 239.918 li
563.721 239.918 li
cp
ef
563.721 247.857 mo
571.66 247.857 li
571.66 239.918 li
563.721 239.918 li
cp
@
.031 .641 1 .003 cmyk
%ADOBeginSubsetFont: FBAAAA+TimesNewRomanPSMT AddGlyphs
ct_T42Dict begin
systemdict /gcheck known {currentglobal RVGGZC+TimesNewRomanPSMT gcheck setglobal} if
2 448 16 <0001005301800258021700030054b0852b5840200205801d64367f050101
000200b0030300021001500160019001a001d0010601b80134b500800454
5a182b10f6fd5d3c103c002fed3c103c3130015d2b1bb10003b8081ab16c
0000182f2b30315913211521530205fdfb021797>RVGGZC+TimesNewRomanPSMT AddT42Char 
2 14738 74 <0003003dfe4603db03af003b0049005903fdb0852b584082121650972699
3603002d105b02762a765302002a062e06528b20043f374f5b6f37752670
5b8f048f05831784188f358a3e83458f4b864f95179518994fb804b905b4
17b418c934c94bc05bd05be05bf05b1b1a201533103514361f5b05a7084a
363f1b00160336214a1b0019431211100f0e0d0c0b0a0909131314090880
25011225b8ffdeb41214025525b8ffc0b3140c3f25b8ffc0400b120b3f9f
25af25bf250325b8019eb5582b80210121b8ffde400d12140255129f21af
21bf210321b8ffc0b3140c3f21b8ffc0b3120b3f21b8019e4018904a014a
40140c3f4a40120b3f4a2c121202554a50140114b8010840136f08017f08
0108401114025508350699430143b80331400c194a0a2f19015019801902
19bd02d200060009034d003c0331400a0607195101512c2c0f4dbe033000
30001e03300039004d0330401f1030016f308f309f300330180f10025530
0c101006553035392e0380540154b8ffdeb40d0f025554b8ffcab4101402
5554b8ffdeb41010065554b8fff0400a0d0f065554251f280128b8ffc040
16171a348f28014f287028c028d02804280e1010065528b8fff4b40f0f02
5528b8ffee4012101002552875205b305b405ba05bd05b055bb8ffc0401c
0b0c345b0e8f96460146101010065546312016010f167016cf160316b8ff
f2401110100255160c11110255160c1010065516b802bd4013993f013f31
3003500302500301000310030203b8ffc0b3191d3403b8ffc0b30b0c3403
b8fff4b41313025503b8fff4b70f10025503695a5bba01780021010ab189
182b2bf62b2b2b2b5d7172ed72fd2b2b2b5d71ed2b72e4102b71f62b2b2b
5d712b72ed2b2b2b2b7110e4f42b2b5d72ed10ed10ed003fed723ffde610
ed5d713f10ed7210f42b5d5ded72102b2b2b5ded2b2b5d4358b4cf21df21
025d592b72f4ed5d2b2b2b4358b4cf25df25025d5972103c103c11121739
11123939111239011112393912393931304379407a4b573a4524351c1d17
1801052625323133313431030641264f262e252a265625541c011c3b1e1c
004b354d200042013f20003d053f1c00502d4d1c00522b5420014418461c
015527571c0156571d3a1b1c011c1b3b004c314a20014b4a353640024320
0001003e043c1c014e2f511c0053295120004517431c00002b2b2b2b103c
2b103c103c2b103c103c2b103c2b012b2b2b2b2b2b2b2b2b2b2b2b2a2b81
818181818101725d00715d01710072435c58400a2e10120b3f351012392e
b8fff0b11239002b2b2b591bb10814b807f640256c7f08016f08015f0801
4f08013f08012f08011f08010f08011203080640364a2c001b1943b807df
b56c19194a063cb807dfb56c0607512c0f00183f333f2b12392f2b393912
39391a10cd5f5e5d5d5d5d5d5d5d5d2b3031590126263534363332173332
161716151407060623231615140623222706061514161716171617161615
140706232227263534373637363726263534360122061514171633323635
342726010606151417163332363534272627260135545acda08360c22b0e
030605030f2b7738c4a544472c1f21301c70ce3d5d6f6a9cfbc1854b0b11
35075f342b3901154a644434504c624533fef82f303a64bdb4ab33349ae1
014e29935988c440050609171a0a0506487080b614263914112007040305
090d70527163925732361818254209631f311f235e0287767a9e5742727a
9f5a42fc8133582530243e7f483416160406>RVGGZC+TimesNewRomanPSMT AddT42Char 
3 3284 80 <000100110000063003af00570408b0852b58b10202435458401759401212
025559400d0d02551711080d0d025511554c30b8fff4b40f0f025530b8ff
eab41010025530b8fff4400f13130255302b080d0d02552b313746b8fff4
b40f0f025546b8ffeab41010025546b8fff440211313025546414741080d
0d025541040f0f025541060c0c0255414c14121202554cb8fff4b40f0f02
554cb8fff6b40d0d02554cb8ffeab4101002554cb8fffa40190c0c02554c
0a131302554c2b040f0f02552b060c0c02552b37b8fff0400b0f0f025537
100d0d025537b8ffd4400b10100255371c1212025537b8ffea401f0c0c02
5537020d0d02553702131302553711040f0f025511060c0c02551120b8ff
e8400b0f0f025520300d0d025520b8ffc2400b10100255202a1212025520
b8ffda400b0c0c025520020d0d025520b8fffc400b131302552016192f32
4548b803e24020475455400c0c02552f55014f556f557f55035556064731
18252c0b073c2c0507003fed3fed2f2f2f3fdd5d5d2bcd10fdc0c0c0c0c0
012f2b2b2b2b2b2b2bcd2b2b2f2b2b2b2b2b2b2bcd2b2b2f2b2b2b2b2b2b
cd2b2b2bc410c42b2b2b10c4102bc42b2b2b10c6102bc431302b2b1bb106
02435458403c252c0b3c2c050b0705075455560718314711021010065511
200410100655202b060f0f06552b02101006552b3741060f0f0655410210
100655414c20b8ffeab70d0d065520205837b8fff8b41010065537b8fff8
b40f0f065537b8fff2b70d0d06553737584cb8ffeeb40f0f06554cb8fff0
b4101006554cb8fff8b70d0d06554c4c59581112392f2b2b2b11392f2b2b
2b11392f2b10cd2b2b10cd2b2b102bcd2b002f2f2f3fddcd3f3f10ed10ed
313001b00d4b5458bf0046ffe80045ffe8002fffe80030ffe8b51a181918
181838383838383838591b401c3407d059ef16038059011159600d5d362b
0d01905901200820291e18b802fcb42237291e31b802fc400b224c291e47
4a2211291e17b8030eb4232b291e30b8030db42341291e46b8030d403e23
55274d41541e55440829374d4039292808000725475657073c2c05252c0c
0a0b07060405074746313018170a5917171a101124213020017020b02002
20b80135400f37292e2b24383037017037b0370237b8013540164d574124
4c4c1f4d504d02804d904d02004d104d024db8ffc0b61416344d605859b8
025ab321a67f18b80164852b2b4ef42b5d71723c4d10fd3c10f471723cfd
e410f471723cfd3c4e456544e6003f3c3c3c3c3c3f3c3c3f3c3c4ded10ed
3f3c111217390111123900f5edfc01f52b2b2b2b2b2b3130437940142224
0c0f0d252326240c211c010e0f220e251c012b01103c2b2b2b8181017200
5d2b01715d59591b400a560745322f1916054748b803e2b76c3118470a25
053cb8080ab36c0b050700183f332b323f33332b17323f30315901363736
363332161736363332161716151114171616331521353332373637363511
342726232206070717111416163315213532363736351134272623220706
071114161633152135323636351134272626232207272533015064122d68
33567c15678e4b497121160d0a363dfe3c133b21170a041b2756356b4c02
02153a46fe314c390b05212c4f3635532d19314bfe3b3f321a09071e1a1c
270f01142b02ec640f262a645f784b4b553a7cfe765620161f2424171023
1150018a702e4035480b2bfe4b5e2e1f242424241152018a7031401d2c37
fe155a361b24241b3b55015e972c21190f247000>RVGGZC+TimesNewRomanPSMT AddT42Char 
3 6902 85 <0001000d000002b703af002801dab0852b58b1020243545840282a401313
0255061f171127040f0f025527181f0111080d0d025511040f0f02551106
0c0c0255111fb8fff4b40f0f02551fb8fff6b40d0d02551fb8ffee401110
1002551f14121202551f0e131302551fb8fffc400b0f0f02551f01100318
1619bb03e20018002603e2400e4f276f277f2703272807180c0307003fcd
2f3fdd5ded10fdc011123939012f2b2b2b2b2b2bdd2b2b2bc010c4c62b10
c410c431302b1bb10602435458402301100318262728076f097f0902090c
030718061f01110c0d0d0655110410100655111fb8fffab40d0d06551fb8
ffeab40f0f06551fb8ffeab7101006551f1f2a291112392f2b2b2bdd2b2b
c010c4002f3fcdcd5d3fddcd1112393931301b406f2002200f3202320f40
02400f820407402a015f2a011f291e18272211291e17862327272041261e
2744000a0b2a111420100104188009010939100c010c590303000718170a
5f0601400601062e1f2a012a0011241f1f1f2001802090200200201020b0
20c020d02005206029a66e182b4e10f45d71723c4d10fd3c1072e4717200
3f3c3f3c10ed72ed5d11173901111239390010f5edfc01f52b2b31300172
71005d59591bb2161819b803e2b46c180a280cb80813b36b03280700183f
332b3f2b3230315901153633321615140623222623220706071114171616
33152135323736373635113426262322072725014c737937483424235715
12152d30130d423efe2b4622190a050d231a1f270a011503afcece432c27
364514295efe494c271b24242416102311500163a03d1c0f2470>RVGGZC+TimesNewRomanPSMT AddT42Char 
3 12154 91 <0001001b000003e7039400380440b0852b58b10202435458400c260a1834
26042d001c1f2c2fb803e2b42d13100238b803e2b6002d1e11060006003f
3f2f2f10fdd0d0c010fdd0d0c011121739012f31301b408712450a018f0d
8f0e8f1187268734d60bd617da27da33090f2e260a250b240c720a750be6
32071c3a2e0f5a36042e3f053f103f1138263f283934303a490b4f104f11
461e49264c284b34403a56195625503a75077f0b7f107f117f167f179507
9f109f11a718bb261e0e050f100f110f2c1f101f111f2c290a29172f3a0a
103a55095a36503a04b10602435458402413100279380138001c1f2c762f
012f2e2634180a04002e110600061e2e1d1d392e2e3a391112392f11392f
002f2f3f3f1112173910dd5dd0d0c010dd5dd0d0c031301b408126181819
171616273434350a0b0c0c33180a0907071926343534333525128f162f11
0111350c0d0d160c1d7d19501e011e2f256f237f2302238f23012319252e
2e39332df229292733500001007d35013505050725190707243525143535
250c16272730330c1433330c35342618090c17332725190b382f26180a03
0c3407351cb8ffc0402c090942550f1c011c1f1f2c2f2f2e131002381e00
121111010100062e2d2009094255042d012d2d1e1e1d0a0cb80145b56f16
01162e25b8010eb320190119b8ffc0400c10354019b019e019f0190419b8
ffc0b30f123419bb0236003300070167b2352e27b80108b300330133bb02
c10039003a024db321cd89182b2bf65dedf4ed10fd2b5d2b71edf45ded00
3f3c103c105d2b3c3f3c103c103c10fd3c3c3c10fd3c3c103c5d2b011112
391117390011121739870e2e2b870e7dc4870e2e182b870e7dc401181239
7d2f18ec10e45d1112392fe41112392f1112395d2f5d10e45d10e4111239
2f107cec5d10e40708103c0e3c870e103c7dc4c4870e103cc408c4070e10
3c083c0e3c59313001725d5d2b005d01710071435c58b9000bfff0b20a39
0bb8fff8b7093917201e123f0bb8ffe8b31e123f15b8ffe840091c113f0d
401b103f18b8ffe8b31c113f18b8ffe84013170e3f0540120b3f0718120b
3f3640120b3f3ab8ffc0b7120b3f29280f390bb8fff0b60f3925200f390a
b8ffd8b20f3907b8ffe0b20f3932b8ffe0b60d3925200d3907b8ffe0400f
12392620123926201139252011390bb8ffd8b20b390ab8ffe0b212390ab8
ffe0b211390ab8ffe0401b0d3910181239111812391740123910100f3911
100f392c40153913b8fff0b2153916b8fff0b2153912b8ffc0b215391ab8
fff0401315393608153928301439293014391108163909b8ffe0401b1639
29401139294015393240153932201139172011390b20113912b8ffc0b111
39012b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b002b2b2b2b2b
2b2b2b2b2b2b2b2b2b2b012b2b2b2b2b2b2b2b002b2b2b2b59591b400c0a
182634042e021013030038b803e2400a6c1100062c1f1c032e2fb803e2b3
6c1e2e0a00183f332b17323f332b17321217393031591321152206151417
161717373635342623352115060706070713161617152135323736353427
270706151416171521353637363737272626231b01af2921230b16414b48
22260136312431557de4544839fe502d1913408693442d2dfed5241b265a
c0ae4a513d0394251c17183210226868631a151d252503182272a7feb879
31032424140e17175dc4c45b11182702242405141d77fffc6c37>RVGGZC+TimesNewRomanPSMT AddT42Char 
RVGGZC+TimesNewRomanPSMT /CharStrings get begin
/g16 16 def
/g74 74 def
/g80 80 def
/g85 85 def
/g91 91 def
end
RVGGZC+TimesNewRomanPSMT /Encoding get
dup 45 /g16 put
dup 103 /g74 put
dup 109 /g80 put
dup 114 /g85 put
dup 120 /g91 put
pop
systemdict /gcheck known {setglobal} if
end
%ADOEndSubsetFont
/RVGGZC+TimesNewRomanPSMT*1 
[32{/.notdef}rp /g3 12{/.notdef}rp /g16 /g17 2{/.notdef}rp /g20 /g21 
14{/.notdef}rp /g36 9{/.notdef}rp /g46 /g47 /g48 2{/.notdef}rp /g51 
/g52 /g53 /g54 2{/.notdef}rp /g57 10{/.notdef}rp /g68 2{/.notdef}rp 
/g71 /g72 /g73 /g74 /g75 /g76 2{/.notdef}rp /g79 
/g80 /g81 /g82 2{/.notdef}rp /g85 /.notdef /g87 /g88 
/g89 /g90 /g91 135{/.notdef}rp]
RVGGZC+TimesNewRomanPSMT nf
RVGGZC+TimesNewRomanPSMT*1 [12.025 0 0 -12.025 0 0 ]msf
461.921 212.807 mo
(Knowledge)
[8.98276 6.01248 6.01251 8.22516 3.73975 5.25491 6.01248 6.01248 0 ]xsh
471.241 227.237 mo
(-)sh
475.241 227.237 mo
(gui)sh
490.322 227.237 mo
(ded )
[6.01251 6.02451 6.01251 0 ]xsh
RVGGZC+TimesNewRomanPSMT*1 [12 0 0 -12 0 0 ]msf
473.921 241.657 mo
(matrix)
[9 5.98801 3 3.7439 3.7439 0 ]xsh
1.5 lw
573.07 222.737 mo
593.771 222.737 li
598.021 222.647 li
605.361 222.707 li
1 /0 /CSD get_res sepcs
1 sep
@
605.341 218.687 mo
609.331 222.737 li
605.281 226.727 li
605.341 218.687 li
cp
ef
645.06 213.747 mo
645.07 206.247 li
645.07 198.247 li
@
641.051 198.307 mo
645.06 194.277 li
649.091 198.287 li
641.051 198.307 li
cp
ef
RVGGZC+TimesNewRomanPSMT*1 [12.025 0 0 -12.025 0 0 ]msf
631.971 555.057 mo
(LLM Knowledge)
[7.49139 7.49139 10.498 3.00629 8.24915 6.01251 6.01245 8.95868 2.99426 5.25488 6.01251 6.01251 
0 ]xsh
643.32 77.457 mo
676.88 77.457 li
679.201 77.457 681.081 75.577 681.081 73.267 cv
681.081 50.187 li
681.081 47.8669 679.201 45.987 676.88 45.987 cv
643.32 45.987 li
641 45.987 639.121 47.8669 639.121 50.187 cv
639.121 73.267 li
639.121 75.577 641 77.457 643.32 77.457 cv
.008 .104 .143 0 cmyk
ef
.25 lw
643.32 77.457 mo
676.88 77.457 li
679.201 77.457 681.081 75.577 681.081 73.267 cv
681.081 50.187 li
681.081 47.8669 679.201 45.987 676.88 45.987 cv
643.32 45.987 li
641 45.987 639.121 47.8669 639.121 50.187 cv
639.121 73.267 li
639.121 75.577 641 77.457 643.32 77.457 cv
cp
1 /0 /CSD get_res sepcs
1 sep
@
%ADOBeginSubsetFont: FBAAAA+TimesNewRomanPSMT AddGlyphs
ct_T42Dict begin
systemdict /gcheck known {currentglobal RVGGZC+TimesNewRomanPSMT gcheck setglobal} if
2 6228 49 <0001ffe5ffea05aa054c002701f7b0852b58404b8a1201128f010102404f
358f0201121d020127022d13381378139802df02ff020713222212101f1b
0a2122211f1b1b2122031f1b092123141f1b1a2123121211010202221222
1412122222b801a2400f27ac010a090901021b1a0812090302b802c9400c
125311112010301040100310b8ffe0b41111025510b8fff4b40f0f025510
b8fff4b60d0d0255109e29b8ffc040103f35402901202901a029e0290229
1314b802c940152121302201c02201220c1010025522100f0f025522b8ff
f0400a0d0d025522192861a2182b4e10f42b2b2b5d713c4d10fd3c4d105d
71722bf62b2b2b5d3c4d10e6fd3c003f3f3c3f3c103c10eded872e2b057d
10c40012390139182b2b2b2b07103c3130005d7243584028091219122901
3f0039124f004a125f005a126f006a127a129b01a901bb01b512cb01fa01
12ef0201005d015d5900712b0171435c58b90002ffa8b31e123f02b8ffc0
b3160d3f12b8ffe8b6173901401c3912b8ffe8b21c3912b8ffe8b21b3912
b8ffe8b619390108183912b8ffd8400f1239121612390210153902101939
13b8ffd8b20b3902b8ffd0b20b3902b8fff8b5143902401139002b2b2b2b
2b2b2b012b2b2b2b2b2b2b002b2b59005d1b400c13021b0900021209270c
0908b803e2b56c0902181b1cb803e2b26c1b0800183f2b323f2b32323f3f
111239393031590321011134272623233521152322070615112301111417
16333315213533323736351126262726231b0170033d1c25502f01d83056
241624fc821b264f30fe282f5724163b3d3b1d3b054cfc07030e7d1f2a25
25342072fb890444fcbd7d1f2a252534207203af452c1309>RVGGZC+TimesNewRomanPSMT AddT42Char 
3 13410 92 <0001000cfe4603f4039400320255b0852b58b10202435458401409092b2a
0300782701271d120614181010025514b803e2b611181010025511b803e2
b602181010025502b803e2b632181010025532b803e2b10006003fed2bed
2bec2bec2b3f2fcd5d121739012f31301bb10602435458401e092b001d14
11027a3201320012060006237a2701271d0f141433000034331112392f11
392f003fdd5dc43f3f10dd5dd0d0c0111239393130b0104b5458bd001bff
f80019fff0001afff0b10a1038383838591b40ab0910120b3f0e2b952902
13342e1664368305850602090905120819081a092b141a26092412241a26
2b38013612351b47126809680a6919661a631b682c7808790a7919771a74
1b782c890a891998009809971a962bbb00d034e506230909082b2b2c2a2a
0a0108021e011319141e13002c321e00120a111e12260820191a1a302a0a
142a2a0a2c2b2b24090814092b2a09082b2a1a09040a082c2b2a1a190a09
0808231312120101000627b8ffc0400e120b3f272f23391d0f3417171a19
b80108401b8f0a01df0af00a02600a700aef0a030a7d3f094f095f090309
7d08b8010e401d2bd60f20010f209f2002208f5f2c012f2c3f2c022c1933
34a921a67f182b2b4ef45d724de45d71e4fdf45df45d5d71fd4e456544e6
003f4dfde42b3f3c103c103c121739011112173987082e2b0e7d10c4870e
2e182b7d10c401111239180010ed0110c00010ed0110c00010ed0110c000
10ed0110c00710083c083c3130015d01712b005d012b59591b400c2b091d
001206321114030003b803e2b46c00061d27b80820b26c1d0f00183f2b3f
2b17323f1112393930315913211523220615141713133635342726262335
211506060706070106062322263534363332171633323637370126272627
26270c01ab152d2d21dfcd110708222b012a2528180919fe8b36af513b4c
37302139280a1e472441feb70f2119101733039425271d2745fe3201fa29
2812090b0d25250418210e3ffc6e8588442c2a33160f3e599f02b31f2e23
0c100c00>RVGGZC+TimesNewRomanPSMT AddT42Char 
RVGGZC+TimesNewRomanPSMT /CharStrings get begin
/g49 49 def
/g92 92 def
end
RVGGZC+TimesNewRomanPSMT /Encoding get
dup 78 /g49 put
dup 121 /g92 put
pop
systemdict /gcheck known {setglobal} if
end
%ADOEndSubsetFont
/RVGGZC+TimesNewRomanPSMT*1 
[32{/.notdef}rp /g3 12{/.notdef}rp /g16 /g17 2{/.notdef}rp /g20 /g21 
14{/.notdef}rp /g36 9{/.notdef}rp /g46 /g47 /g48 /g49 /.notdef 
/g51 /g52 /g53 /g54 2{/.notdef}rp /g57 10{/.notdef}rp /g68 
2{/.notdef}rp /g71 /g72 /g73 /g74 /g75 /g76 2{/.notdef}rp 
/g79 /g80 /g81 /g82 2{/.notdef}rp /g85 /.notdef /g87 
/g88 /g89 /g90 /g91 /g92 134{/.notdef}rp]
RVGGZC+TimesNewRomanPSMT nf
RVGGZC+TimesNewRomanPSMT*1 [9.025 0 0 -9.025 0 0 ]msf
653.641 57.6769 mo
(Low)
[5.25238 4.51251 0 ]xsh
RVGGZC+TimesNewRomanPSMT*1 [9 0 0 -9 0 0 ]msf
647.387 68.5069 mo
(N)sh
654.132 68.5069 mo
(ove)sh
666.885 68.5069 mo
(lty)
[2.25 2.98804 0 ]xsh
643.32 77.457 mo
676.88 77.457 li
679.201 77.457 681.081 75.577 681.081 73.267 cv
681.081 50.187 li
681.081 47.8669 679.201 45.987 676.88 45.987 cv
643.32 45.987 li
641 45.987 639.121 47.8669 639.121 50.187 cv
639.121 73.267 li
639.121 75.577 641 77.457 643.32 77.457 cv
.008 .104 .143 0 cmyk
ef
643.32 77.457 mo
676.88 77.457 li
679.201 77.457 681.081 75.577 681.081 73.267 cv
681.081 50.187 li
681.081 47.8669 679.201 45.987 676.88 45.987 cv
643.32 45.987 li
641 45.987 639.121 47.8669 639.121 50.187 cv
639.121 73.267 li
639.121 75.577 641 77.457 643.32 77.457 cv
cp
1 /0 /CSD get_res sepcs
1 sep
@
RVGGZC+TimesNewRomanPSMT*1 [9.025 0 0 -9.025 0 0 ]msf
653.641 57.6769 mo
(Low)
[5.25238 4.51251 0 ]xsh
RVGGZC+TimesNewRomanPSMT*1 [9 0 0 -9 0 0 ]msf
647.387 68.5069 mo
(N)sh
654.132 68.5069 mo
(ove)sh
666.885 68.5069 mo
(lty)
[2.25 2.98804 0 ]xsh
643.32 151.447 mo
676.88 151.447 li
679.201 151.447 681.081 149.567 681.081 147.247 cv
681.081 124.177 li
681.081 121.857 679.201 119.977 676.88 119.977 cv
643.32 119.977 li
641 119.977 639.121 121.857 639.121 124.177 cv
639.121 147.247 li
639.121 149.567 641 151.447 643.32 151.447 cv
.008 .104 .143 0 cmyk
ef
643.32 151.447 mo
676.88 151.447 li
679.201 151.447 681.081 149.567 681.081 147.247 cv
681.081 124.177 li
681.081 121.857 679.201 119.977 676.88 119.977 cv
643.32 119.977 li
641 119.977 639.121 121.857 639.121 124.177 cv
639.121 147.247 li
639.121 149.567 641 151.447 643.32 151.447 cv
cp
1 /0 /CSD get_res sepcs
1 sep
@
%ADOBeginSubsetFont: FBAAAA+TimesNewRomanPSMT AddGlyphs
ct_T42Dict begin
systemdict /gcheck known {currentglobal RVGGZC+TimesNewRomanPSMT gcheck setglobal} if
2 3654 43 <000100230000059d054c004501bab0852b58b10202435458b747400d0d02
550025b8fff6b5131302552534b8fffc401213130255341a0d0d0255340c
0f0f02553413b8fff64013131302551301220c13130255220c0d0d025522
b8ffe8400c10100255220c0f0f0255221a411003e2001d03e2002c03e200
2f03e2002e000c03e2000903e2003f03e2003c03e2400b3d0024242e3d02
2e1c0a02003f2f2f3f12392fcd10ededecec10ededecec012f2b2b2b2bc0
cd2b2f2b2b2bdd2bc031302b1b40717047a047d047e0470413479e1c4036
5047e04702121f1b0b2122221f1b1c2122341f1b2e2122451f1b3e212202
1f1b0a2123131f1b1b2123251f1b2d2123351f1b3d21230100232324241b
3e3d3d0b0b0a022e2d2d1c1c1b0812132202402201df2201202230227022
a022d022e0220622b80220401a10476047c0470320470147452522355034
603402349e4661dc182b4d10f4723c4dfd3c107172f45d71723cfd3c003f
3c103c103c3f3c103c103c12392f3cfd3c2b2b2b2b2b2b2b2b3130015d2b
015d591bb53f090c033e3cb803e2b66c1d2c2f031b1ab803e2b26c2400b8
07ed400d6c24241b0a3e020a022d081b08003f3f3f3f1112392f2b2b1732
2b1732303159012111342726272623233521152322070606151114171617
163333152135333237363511211114171617163333152135333237363511
3427262726232335211523220706061501a502760d0a202b303002443030
2b20170d0a1f2c3030fdbc30532619fd8a0d0a202b3031fdbb305426180d
0a1f2c3030024531302b1f1802d701846821191218252517104164fc9567
21191218252531207a019dfe636721191218252531207a036b6821191218
252517104164>RVGGZC+TimesNewRomanPSMT AddT42Char 
RVGGZC+TimesNewRomanPSMT /CharStrings get begin
/g43 43 def
end
RVGGZC+TimesNewRomanPSMT /Encoding get
dup 72 /g43 put
pop
systemdict /gcheck known {setglobal} if
end
%ADOEndSubsetFont
/RVGGZC+TimesNewRomanPSMT*1 
[32{/.notdef}rp /g3 12{/.notdef}rp /g16 /g17 2{/.notdef}rp /g20 /g21 
14{/.notdef}rp /g36 6{/.notdef}rp /g43 2{/.notdef}rp /g46 /g47 /g48 
/g49 /.notdef /g51 /g52 /g53 /g54 2{/.notdef}rp /g57 
10{/.notdef}rp /g68 2{/.notdef}rp /g71 /g72 /g73 /g74 /g75 
/g76 2{/.notdef}rp /g79 /g80 /g81 /g82 2{/.notdef}rp /g85 
/.notdef /g87 /g88 /g89 /g90 /g91 /g92 134{/.notdef}rp]
RVGGZC+TimesNewRomanPSMT nf
RVGGZC+TimesNewRomanPSMT*1 [9.025 0 0 -9.025 0 0 ]msf
652.341 132.037 mo
(High )
[6.74164 2.24725 4.51251 4.51251 0 ]xsh
RVGGZC+TimesNewRomanPSMT*1 [9 0 0 -9 0 0 ]msf
646.837 142.857 mo
(N)sh
653.582 142.857 mo
(ove)sh
666.335 142.857 mo
(lty)
[2.25 2.98804 0 ]xsh
643.32 151.447 mo
676.88 151.447 li
679.201 151.447 681.081 149.567 681.081 147.247 cv
681.081 124.177 li
681.081 121.857 679.201 119.977 676.88 119.977 cv
643.32 119.977 li
641 119.977 639.121 121.857 639.121 124.177 cv
639.121 147.247 li
639.121 149.567 641 151.447 643.32 151.447 cv
.008 .104 .143 0 cmyk
ef
643.32 151.447 mo
676.88 151.447 li
679.201 151.447 681.081 149.567 681.081 147.247 cv
681.081 124.177 li
681.081 121.857 679.201 119.977 676.88 119.977 cv
643.32 119.977 li
641 119.977 639.121 121.857 639.121 124.177 cv
639.121 147.247 li
639.121 149.567 641 151.447 643.32 151.447 cv
cp
1 /0 /CSD get_res sepcs
1 sep
@
RVGGZC+TimesNewRomanPSMT*1 [9.025 0 0 -9.025 0 0 ]msf
652.341 132.037 mo
(High )
[6.74164 2.24725 4.51251 4.51251 0 ]xsh
RVGGZC+TimesNewRomanPSMT*1 [9 0 0 -9 0 0 ]msf
646.837 142.857 mo
(N)sh
653.582 142.857 mo
(ove)sh
666.335 142.857 mo
(lty)
[2.25 2.98804 0 ]xsh
grestore
gsave
210.88 304.158 mo
262.361 304.158 li
262.361 252.677 li
210.88 252.677 li
cp
clp
210.49 252.29 mo
262.81 252.29 li
262.81 304.61 li
210.49 304.61 li
cp
/0 /CSA get_res setcolorspace
gsave
clp
[1 0 0 -1 0 570 ]ct
[52.32 0 0 -52.32 210.49 317.71 ]ct
snap_to_device
Adobe_AGM_Image/AGMIMG_fl cf /ASCII85Decode fl /RunLengthDecode filter ddf
<<
/T 1
/W 145 
/H 145 
/M[145 0 0 -145 0 145 ]
/BC 8 
/D[0 1 0 1 0 1 0 1 ]
/DS [
[AGMIMG_fl 145 string /rs cvx /pop cvx] cvx
[AGMIMG_fl 145 string /rs cvx /pop cvx] cvx
[AGMIMG_fl 145 string /rs cvx /pop cvx] cvx
[AGMIMG_fl 145 string /rs cvx /pop cvx] cvx
]
/O 3
>>
%%BeginBinary: 1
img
\c<<K/lZnOTs2)A]XY,9M/Q0>#MT6W!"fJd9PAs>T;\ikVO`cqA4IsNm/WFP'*p$YA:'<)U8F`ZR#6,s
73r-<!/(=Q$TJZ.MQ4PChrNeQdCuH2?S_tN!:^%$#qf1uNM3Se^:^tYSr%A].L2aLhZ+5o.SON+P+S\S
Whu>JHt5_o#.=NV!"fJc8S!1-R\H[TTU:U]@7;IHa8igP&IUR0MQ4PChrNeQdCuH2?S_uA!3?/&+C(,A
n\519NE."e!1Eli*E.ZjnZ;njJ5-r;!!O?>J>/s>o;;\`HV53?!;-<o-Z?9Jn`Br0Wb<NP!9O7`$rWV0
lb<P9Q:qUs!7UuN$VHD[l`C8jLd_To!5\^<$:foLl_ai^K0fk$!3cG*%V!*4lfJ<1Zs*q.!2';n'5Fr;
^B;6VA.Xn(!YSn:poWtd!hig/QiR!`!YJ\/jei0L=:V>2kl:c$J(j#H!nMW2]E$Ub!X`MJiP,H%?O5!Y
`rH/I>c-J^!i/j%iW-@d!XVu%iMQaK;[;ppUAt?)HJIQC"Qnk#Ese66!C3aX^[&W8WB6OK!rr<^S)(1I
R5V,Hm/R/HQJJG>P;KuRgAh7Kce[^ab=C%^`rH,MJ(hX=^3^:P!4;e-%<L7*!j$;Jq>d8j!=Wo+Vtm4l
VJ?O/!!*\!o]G?!!p,XVT)\rn!%=et^B(2YZ2j7l!@=,bXT=_4_uSNl!@*f[VZDo'ec<el!AVaKjoNLT
kQ&*m!COEJ^B(i2qZ*Jn!BmC=XnSpuVECLO!B[%GVrafWTK8_G!E%b)joO:6Z2j@o!E[#)^C.6'Dcob&
78-p*Nj8)g!PVUR!8[\V:TX&f$_DfX;+3Z478d`JT^]&aXA7@IbQ%Z;VXUJkR<i::69I@t:LedAn>?;a
9BcGf!!-fpnE(,,W.f"k;c?q<LoT"pjoOOVqZ*Sq!*o*0"M9Uh*!,d6"9BTCO1kP-otLK5U]:BnnuW%p
In:OZpAb<s*(tmanuVmlU]:HnVl00b"Jg?5)$0I3"9BH5IAQM4!)p3(nc/Z.o&^)6WF6tOpAb<t-"O+;
o&]pm`;oE.&HN\/=E&nTR[fh0Kl^H])caWE^B1KB'CPo&(h0]?^AqBg!8dbg!>RFfAp8odNJiI8BMpf,
9s!uh!h3.%mf3D)=eG;f!)Mk[blA=V'J`BlF+8q#L4FDW:Gs%_VY$bfQ;J7_!!3m9RId<V:&G"'!"f5O
7;@ULYIV<VYb?qk8g%d.o]?5$E#7sC"<D[7k2u@!!,B%E";+4SXM4;@!5A-@!jGW/q>g'd!XW&;otLOA
7_/R&&41E,XRiOoXSo9sXTG+g#O;?k#Z7AiXT>Lf\c;mE5]2mbVt?keVY-hgRRmbM!!3F%Sb8l]VEMp!
o`,+0=.%=qoB$&7p#Z>*AI7Z&!Xihsp#Z;9<87K5!!<HqNP+>e!kradk5YPqI(o<h!P']K!71]J#![X<
jK/KbBas5*!YB=Pp8n@o-GBH^#!I=/jJN'VAdmo("98E4Co6p(!MUmS!!<L+WoE+%!p#:PqZ-!`!Yq!^
p>uD51V`tl&7_p/^\PVFY;bJA!C3sa^B(;E_#ONI>+b_pkH+cV1?/?83hc8L!LXG@!;?Hp%T]"WVZE2>
irB*>SG&i]P7?=JjT#>rGLPR6!Ra?q!!,gGp>uD!'(5hN!!3O<[c+t%].MtA!?7^*^Aric!Q4s>$<j:b
XT>FNjT,5Z!>psmXT<PF_uKiG<hJ?K!Mh+;!:'Uc(lS*c!HA.Y!!3XSgZR_rjoOF!i;`m$_"QmkS,pV0
!Wb`lpV5q,!k;YEiW&ugPP2`k6d#K-!!30bS_gIMVH=)_!!*L^p8n<Xh#Q^?!WbEMhPUFJ<!VC_!=OGO
VZ8gI!8%8Q!E7A%joX@\$K;$d&$bij!)^c:!>C:C^B1B%!U'O]!!*ChpV-a3%*/DL&pr?7!gu.Oq>fd\
!=4AQXT=t#a8c5QGN,OrVZN&C!TO.\#_;ZI!LO58!!*n2o]G?!!m=C@irB)fYkR8\d14>"!rr<ZYLgMi
Osf8i!=YOn^Ar$)!:9ae0q[("!JD]X!!*IfpT4F'mf;)B!ABkmVZD;lirB)eMYF"K>fcsH6.=HJ!O+6@
!;lft%__W!!.W/l!WcK<e\;1!FqX]Qkl:`%Z1u'7\JNHi!Wc0!hlZXT!ip)Jj8]2rT_PViW"mMV!Wc)n
nYbKH!i9N@j8]2rS+rl^U(kfO!!*+:j438nj,Oo9!!+.kpuVV7*8pnb!!*1Cn%T4DWK)=DCMe6MT=F=(
!jl&5jT#<B^A,GCE:X(a!!*18n#ZquR=K3d@:F"uOJhNK!i&NpjT#<<XS].!XT2qW!!*15n#$MiPC..S
?=.>gMkTR:!hE$hmf<(^!A^PIVZ:2N!!*4\n)au<bGpe\JV0#X^Y\D@!n_5ljT#<MjnRs<L<]c""FfpV
"MUF<1_'3["9g)OMn8Dm!i%dWjo>C'pqHj>&C1=W"*3t7!3?9_>V?N\!!EHL9n'&1XTF_E!Tj@^C&"e2
V@LoP!<[61VZ`lS==t$W!!EHK8p[6$VZMo8!Tj@^B)&8)TFTo\mf3@lR.BABjh5t)&GQ5."taGci:,k1
`C9mj!!%uQjoO9Oo)RVI!<IT>^B:fW+T_*5!YA8'n@o!^+Qi_*%BoZDrkAG9ci=(IE:^16U0o#CnGiV#
99SeH!Ic'Z!;?Ho%%m<s!)_)C!<I$.VZWJp*<G[1!Y.b\n>?;4*9R;&$^pdf!)Cl@!<SPXjoa7c-iri<
!>ArC_XQ[gV^LX-!>!ZSjoB2D!!$m.^B1ZC$N:%o!!30aSajGr]PS/B!!#gi^B()1d/X2VXnAdtTMZ$^
!!30\Nq'4QWacM%!!#RbXT=Udi;iBJ!+5Ar!h2pkli7(f2N%%&!i034kPtTOpnn.Q!V6<K!!%ZDjoX(K
%.!rq!_U/rjoXOq&a02p@/B!fk2sS_dJs8CotLRBE";(3!Wu-"n\5.0:BU4hpAb3tW;++-.FJ1r8+itc
XC_q*!!36kT(B&eXf\3d"6oje"do(e!%$%n!(HRY!iBE8kl:ec"%&FGVZN;U"6oje"dA_Z!$otm!+5E]
!p#+KqZ-$a!X)`Un`Bo&?j,`p!=$^Ajo@0c!!+R\rkJ9D!N@d6!!3RD]CEW:SMKI1!*/g/"M0k//d(/7
oDen=W:m=oR4I=u!XiD8nZ;hP/a<<9:&(gnW/"S+"82`S!!+C?p87qT.c^R2$='@rVZDZ+l2UfWqPOOq
VkScF-j/'$!Ai[-joNXdj8]5kJ)Tq[!PLVf!;?HnBDCTli3R\f"P<\T$E!O3!K.HH!!40r^@o>?^B2-%
)XIG)%_22H!j6Adg&M-[QM.E]ILYB=r;Zm;HE?\>!j$S_li7%qVtI.nSRWhs!!*Cgp87q;%/0bf!!4'^
VXgVdVK3R?!!*M%oqqkY?m+/'!=d*Ik549AW"Itg![FH$o&^#8SfmA"!>42]joWq`/Em0*!!%'5^B&K\
hZ*]Y2kfcV!kDkLm/R-;o=kCAP<AsG!8mhWBD/G.CBNGo!Wb'>nZ;kk>RBct!-S:Cp8nFuKf9%g!!$R'
VZCE4hZ*]Y0TGV#!hrd'qZ-3f!-.V."/^T+!Sm_UM>$'4Ns4D@!WbX)qW@S8!oJ;4m/R-UoB$/:Yt5#R
!!+[cpV-`J!TjCV!!3:&ZLP[2X@NE]!!#CU^B0oa!T3qY.BN9G!G)<,!9F1^"AGNZXTG"Y!q-*h4n,QT
NA:Om!!+IErhoUj!Fc)b!!39pSFNKYQTkQ?!!#+MVZMZ.!UTmZ!!,"=pZ;L2!SdYV"_H<UjoWk1"7H3i
;=N]N]L)]"!94%[!h/ku!IFk#!!3^O]^``;QRhP*!>*!E^[f,?L`,1P!<S5SXT<>@f`2'`AubC'!Ji-%
!;$6l%]o-$!IGXB!!*.VpSS%-!SIGS%V)=5VtHqgKI60g!=l!qVZCuWiW&u]](b=fPQKnGp&G.-LuRse
!OXcR!!*bon)aYG+6!8#8,'b!P6U[[iW'!(O7Bsd^3UOa!!&\[^B1i@!TX4\5l7\^XT=+Zec5^nK(5rE
XD\dB!!&/LXTG=j!Ug$^!!#4WVZD;Oec5^mIIX3:VJ?h7!!%uGVZNJ\!TX4\<qk_WYm8h[!@k2@joXV-
)=[\,_>WNejoX:G!p'C_"K(t/!O*<g!!30bVX_D'[Ts+<oDel=m(WRU%H[Wk"IAhb!M:%T!!E<^Q`[C]
XTG=u#P.oqE9s\-Gmrg8!<eP[VZE5!i;iKM!Wb3AnYZG\;$Z[m!,V#"!Heh5!!*8DpuVV,)=mjf!!30o
aRSBogMdJj!!&;NjoM.ejo>BMq7d!G^Hg0H!XDu=n\5+%3qNCP?L,?,U`](+p](:XpT4EVd/X4P;l0#d
!LGY8!!$$bXT4Ud*9R;%4SP`R37.^-##V#_VZDo8oDekhr29%^!KS5`!!#sljoA-'!!3FEg[XD-a@-+%
!!%$)joNIKkPtVaRJ=MsL!BZ!'RBbno"P4>8bE&`7d@_hZ7bAA!<J)QXT3V&!:^$j&oXlBXT>Lio`+tW
lE()\.d6p6!J^BI!-I]1hZ*]jCSp[#!N&-T!!#4JVZE;:kl:_b\G51dT[!N=(mF%OjoORGo`+tllK/-!
3:m4E!!"DA^B(nbkPtbt=FPNe#3u6i/!fb@!O`R5!!"tF^\tnJ\2<IN!$h9@!N6k!!!Nj/Ec+2IlMpr5
M"7YKV%32!!]$m[l`C2b0BrN;,5A&:U)<(o"V+7EC-Vsg!!+BuoVVehVk4Im!!"_;VZEGCl2Uf;puVV8
+Qre/'5Ent=9n6orVusT[.<>[gCs8\!(6#5!Sp!*!!$m2^Ar<=!!3:'Zi.W>V*+eZli7(f7]c3r!(lka
!&+,^!`4]eoY1F:0^A]=@ed&*BCZ&t!!39tUA_1qPrJg2!!30dS+E`^6M:BZ/,64J8UIQ2XT>:LlMpol
qPOCmVe##l!X)/erMK^Y2?E.E!WbKNo;;RRp&G(Apnn0_GGb#1!MCq8!;?HnKD=R/M<P!A"_ZKdjoWOp
!UKdf!`dS<joAKV!!#%SjoStejS7m9joO:!li7%eX80L2]c-2:!Wb9Tq7crj,O5=2$=p[>^AqX7!!"SL
^\bbK)#tk4^@f5AZm+l;!<J\cXT>I>lMpte1R%X:!Iu<Y!!3I1Vt[:pXfYXt!!"GBXTTF?+*F[XXT>1=
m/R.fQ2.<YV&/Ft!Wb$8q547@+7K:.!!3I.U%P;`;t^1k-hsSB('#@pVY-hfSK7(t!<URBjoOKblMpte
7)Si_!3-#KlMptpGi&,U!-@i6!&aQ6"<RUmSE0A*!SAjg!!"DA^As&Y!;lft+,KX*!k`I_lMpu(J\Lln
!+>L#!%do[!#bb9!A:#;^B(2CmJm53poOOBlMpr*HhOQCWb)b,!!3sZXS8gs=7uUo./9nE(]FC8.Zj>*
!LF;i!;QTp,5A&9G3],/)gD"R!i097lMpu%EMiK.!*&Xl!%7Q>!#GP6!@`s'Vu3FnOUgdZ!&+-0!2AcZ
!@=Q8joXOt''fN!+.MBdjoBJr!!"nTk5=?A+8u6@35>.K!QYrB!!$6u^ApOd!!3UF]CWc=Z;Unl!!+gE
q7csF@.jR#/GQs[)>sO:#&(aE^B'2mmf3>cpoONWm/R1r@B&k#!hi6ho)SRd!A0<+XT2Gr!!"GBXT019
!!3=1XS/asI0&d:!)NBf!''?G!Xi>0oVVehRn3_J!!+U+pnn*kp&G(?pnn*-r;Zm&>Gh+l!I4_7!!$m2
joA-E!!E9%%tW^2joX+E"mZ-h4M:IO!-@i6!&aQ6!$D.>!XF/7p>uCQ!q-*hM#"dd\-_U(!Wu0#n%Smr
2X:>E"&H,s^Aq[8!!"SF^Ao/K!!,0hp:gT/p&Oph!.4OD!N$.k!!36lT'rc^OYQ/%!WtrbqQ0a!p&G(@
poON4qZ$XTV#7@lXT2/c!!%6=VZEFrmf3Ck6^dD@!K/Vs!!36kRJNf]<;$:l-iBn@VZ7M0!!+pJp87ma
mf3?`q;q_6$h"&s"C9IEjoN7`lMpth?dnl6!-@i6!&aQ6!$D(<!Cti:joB,b!!*,(q7coemf3ACS*[lk
^4dR"!;?Ho%;u'X!+>L#!%do[!#bV5!@4c@^B(kenGiRjT)#JgII@.:/<'&"riH7'GoGuK!=WN9XT2Gr
!!"GBXT016!!+75pT4Ip*:X"0!L`b]!."#5!@rumVZN`<)=%8'$t/t1!*&Xl!%7Q>!#GD2!?[[&VZEM2
nGiRkdeW#,V>pVd!!,0nm,eB2Td&e&!>'t^joBJr!!"nOjo?M"!!+UrpZ;M6-2IW:!!*bIq7co6nGiV.
J\LB`!kW+Sli7"eqnE,=p&G(DpqHeHq#CF8XS9I1NreeO!>;L0XT28h!!3pYXQchgWEou!!!!)tXT2Gr
!!4RNXno."(\n%3)OpK'!J1@C!!*\/q543gnGiV+EMhuu!i&s,li7"erhoan!*&Xl!%7Q>!#GA1!?%3t
VZD2Hnc/\,jn\$=D=IT-*h29UjoXLi%f-1s!!!,ujoBJr!!"nOjo?M!!!+:ipZ;LX!V-3j0_iB_2"L\K
$"LL8^B(OPpV-d39*4M]!!<&4!+>L#!%do[!#bP3!@"lE^ApOi!!"PEXT1$G!!3F0Vt$kiT<.dh!hD^\
mJm4gqlKj"p&G(@poON4p](=:UA(bi3q<7N.eonA0(T&E#ZdYhVZE3_pSS(Z5m$HS!!<%q!*&Xl!%7Q>
!#G>0!?Ia*VZ8^Q!;QTp3r%h;5P"jV$[:ItjoNrmpZ;P(=p+0m!!E,\!-@i6!&aQ6!$Ct9!@c[qjoA-H
!!#L`^Ao#A!!30iX7<q-Zr[D_R.e8qRP+%/!!<&4!+>L#!%e,aqnE+KpAb4P]_K5BU]g8h!'p=]!#,#*
!WbKSnZ;qh:B`2)p8n@R.IR6:!r]5&XfY[u!!"GBXT013!!+gSpoOR^"7lKm55;#U'(l5+!BcY;VZ`Pa
"Xf#tVZDN#quH?h!!<%q!*&Xl!%7Q>!#G;/!AC8DVZDh\o)JbjpuVPoo`,$p;pOpq"P@Dm2RiDB!P(/X
!!!,ujoBJr!!"nOjo?Lt!!,CFpuVUs"nM]o=S]]4])hU*!@a92^\5DD]late!!33nXnTR3^4$mg!!!)t
^Aq[8!!"SF^Ao/F!!$C#^Apmt!!#jkXT>C%p&G+>L@MAIX(i4F!!33gSbK5fXE#'G!!!)tXT2Gr!!"GB
XT012!!$'oXT1`b!;ZZq:&1[fUB1&g!@39eVZN],&H2Y2!^N+HVZN`5'_)/'!rJkq<;$:l-hsS>(A7_.
;tm0i61Y'VCAHumi<&]Q!A_"OjoXS&(B+:8"'EqEjoXY3*:X"/"8h3\F7oS62>u\8jo?Ls!!%*7joAQU
!!$R*^AtA0!!3gZ^@Ar=Os^#*!XiYPpV-d=@0cB(!!<)5!P`%9!!"SF^Ao/F!!*1gpqHj'!qZHm>PYB$
S+cma&oF`?XT=)"q>^R(?)[M""K#9+!!)Zl!!<&"!*Ajo!%@WE!#P>/!<\/QXT=RdoDeknq544YpAb7,
Br:Eu!Iu?i!!3L2UA(PeTMu0f!!!)tVZ9]i!!"DAVZ7M+!!*1Tpnn.P!qZHmH26S&ch@D@(QmeTk4n'>
YV,bP!Y0V9pZ;P4F:%O=!!E,\!-@i6!&aQ6!$Cn7!<fh*joN=$oDel-q7d!*!!)lr!XDr<n\5.)636f\
!ZQg,pV-d/6NQi[!!<&4!+>L#!%do[!#bG0!@5;P^Ap7i!;c`r@em,+PPG1[##_;fXTFnQ!VZQq(jE(U
XTFnQ!VHEm!rK)"=7uUo./9nE(\Ib.+TSP;XT10L!!$@$VZ;_P!!3@#TCJf\P<&a=!!4!YVY?tiPWAj<
!!!)tVZ9]i!!"DEVu<Ln(A.Y.+/J\0!&=*G!.t%/!5nU4!XNYtn`Bnr:BC1i![+,spZ;P$:]g:i!!E,\
!-@i6!&aQ6!$Ck6!A!.(jo@gA!!$m3^Asr(!!30aV=D;%\6fO5!!+pKp:gWk-h[N?!rK_4@.jR#/GQs[
)>!n/F83KMK_,6EA,35,Oo#+[!B6;6XTGA##PJ/s!!+a7p8n@K,PD*;!rK)"=7uUo./9nE(\@\-B_\\0
GOtk8@/6]#Mu*JU!B#u3Vu<LpTMl*e!!+^1p87qA,5)!:!rJkq<;$:l-hsS>(A%S,AGE&&F7]G4K_aa1
_#=?5!!30m`pr0mh/`qp!!,=!p>uC[0D5AG"8h3\F7oS62>H;6+7oO5MYQ<6TD\cb!!$a/^At,.!!+:'
n\5.>I2;;P!X)B*pV-dCFqXQM!!<&4!+>L#!%do[!#bM2rVus6](s)A]+=Q7!+5Q(!1!H^!?Zj^XTGSD
'^u)("%f0[XTGP=&GQ5*!rK)"=7uUq.'9WJXT010!!*b3q5j[s%eTf%>kt8tOSf(Z*ddFT!iBfKn,NLl
8"97N!i9N@p](9qrhoan!*&Xl!%7Q>!#G2,!>;.&VZEP%o`+u@q;q[squ?aHWq#3Qjd-qU!!3=4ebS>1
k2t]a(AIk0"8h3\F7oS62>H;6+7oO6);t>Q!T=[a!!$F&^AtP<!!3^N]^``;R4e.4p](=)FS<HN[9*V/
!!!)t^Aq[8!!"SF^Ao/C!!%0:^Apju!!$*rXT5$n!!3XAWqELmXT=;.li7%qC%eY1Ueh6k!!!)tXT2Gr
!!"GBXT01/!!$d/XT1]\!!$!oVZ<4c!!3X>V"(>`L+)Bg!=WT6VZNGa"o83!!rJkq<;$:l-hsS>(@qM+
B)&8(5lC]Y!!%*9joEs2!!3ggipl.3\2WaS!>1:ajoX4N#5S<""8h3\F7oS62>H;6+8,^6!!&#RjoANV
!!#pm^BD7U"B)Pq^B1Q1!p]ge3hu>^!M_^Q!!!)t^Aq[8!!"SL^\bbG)=mh.-2>4TKCo3E9)5RlX9Jc"
U%,5dSO3JE!!+sAoW8.Y2>[@R!r]5&XfY[u!!"GBXT01/!!"5<XT3S<!!#ObVZ`k$"%\pOVZN5O!p]ge
1QV@0r20RV1]%.P!rJkq<;$:l-hsS>(@qM++o%r8F7fM5@eo-hj9Pp!f(%l(d9-SC!;QTq7`G#^!Q@P*
!!!,ujoBJr!!"nOjo?Lp!!"VGjoD"G!!#1W^B%3)n\5(8!GDi+!!+4#n@o!^+oMB@!rK_4@.jR#/GQs[
)=mh/!M0&$!ODn%!!#"RXT1omOn#OTW*Ter!!+*hn>u_?*rQ'=!rK)"=7uUo./9nE(\7V-!KQuX!MT\p
!;ZZq2Ya0N7uQo8!hrm*lMpr*HLRg5H6)qa!!<%q!*&Xl!%7Q>!#G5-!rr<%M>=%MSHJQc!)!%K!F`e6
joXIh%I3up-`HOs!N7FF!!!,ujoBJr!!"nTk5=?A+7fI5!PS<k!S@PK!!";-^B'$.lMptrD7f5N"hSX^
!!!)u^B))Wp&G(DpqHeHnc/YspqHeSp&G(9kH+c1)X@A)%:cF2Xno.'WalP=!!<&"!*Ajo!%@WE!#P2+
!*8ls!$V%9!$CC%!Hf:J!<)s"$t,n!VZil($ig8/qkjEnp&G(?pnn*-nc/Ygpnn*6p&G(CkN2i>+ops0
!YL+EmcF]3Kb4:b"8h3\F7oS62>H;6+7]C3F84kt/+rrD$+orHoY1F"2<t5D"&H/q^B2-5^A#AEYttN(
qnE,=p&G(DpqHeHnc/Y<pqHf&quHTo!=5[iXT=P<lMptg8>#XY!j%*WpT4Oj8HT%kXT2Gr!!"GBXT010
!!3-#-2=SB7J6]^#c$[_!K/Sr!!36kReN]]VLYQ<VZWDX!s8@t!*&Xl!%7]BrMKW2nc/Y7pnn*Yp&G+$
iTfP+^d.2c!X)o\pZ;P<Z/kZA"4^f_"8h3\F7oS62>H;6+7]C31&0l2>P.srTBs;oZ;Unl!!+mHp:gcq
-ibZZ^\>JDSMg;Z!+>L#!%do[!#b>-!<fh+^Ar0E!!&,IXTG1h"7#pe/c^q*XTXA)!%!?mXT=G9qlKj"
p&G(@poON4nc/[mV"q+mAG#p&MsR>CRn3_[!:Tsh/W08""G%ct,CoKc!K&N,VZ9]i!!"DAVZ7M'!!*1n
q544#o`,!,p?),3!nLlclMprK^%URkZ7u>6Z1d;\]g2JW!-@i6!&aQ6!$Cb3!<q3QjoU5:!;?HnFRHmF
]PnGJ!!4'j^A#ADW^Qsf!!30hWqX7.^AGYF@.jR#/GQs[)>=..!!&2X^As2b!!$a$XTGM7%dO)r(j<"T
XTFqT!WE'#!ButHXT5I"XT2Gr!!4RNXno."(\%J*K___MIe<[@B'uPuUgai"!!3sWVY?tiPro*H!!30`
Q1q0VVZ*LmVZ9]i!!"DAVZ7M&!!%QFVZ;#8!!%uGjoXOt'C,W"+J%Wgjoiq-!WW3&!!6'CpZ;J;qrRm"
p&G(MpuVPunGiQnq;q[To`+t[n%Sm`,O5=1$=s4JpV-d>@L;l2!XN5Eo"P04p&G(DpqHeHnGiQ1q7cp'
o`+tUn#ZV@+Su0/!!3I3W;!CqVHF3$!!3C-VXghh=7uUo./9nE(\%J*B_eb1P4\eT4SboLVZD/elMptm
=JGPf!h`R"q>^R%<M8o\!*&Xl!%7Q>!#G))!+ku(!0-sXp](:ln)aYN.dI'9%=6q+joX@^$i0i)$?b1q
joBJr!!"nOjo?Ls!;lfsMtuK8_Y!m0&A@YL!iA-^li7(f8?DR#!ks.$p&G.2J%kQi!+>L#!%e,aqnE+K
nGiPoq7d!:!<Mop!=u7%XTFeJ!UKdf!C<4LXTGSF(A7_0(3?SNXTGW,=7uUo./9nE(\%J*;u*NsT`G2g
!!*S+ntuPO2?E.E!WbNOpSS(iD\`*Kr;Zm6Dl30)!*&Xl!%7Q>!#G))!)`Qi!h02kpAb4.j7;=6a%HI"
!!E@)cfXBcjoXY4*VKI7*LPs\joBJr!!"nOjo?Ln!!$s5joX*7!VZQp"/ke+!k);<pAjjd!@sN1^B'fX
nc/\DRe=Dq@.jR#/GQs[)=[\,9DQ=(\crB5!!*1gq5sRs!i8g"lMpr5M"[qON%=H!!@s-%XT2Gr!!"GB
XT01-!!#F_XTYR+"TSPu!!*1boVVb_:^64c!@EKnVZDT'nc/\>L\7PF<;$:l-hsS>(A.\+!!#=\VZNRr
"nqut"Ng;u!o%SulMprB[J&_`]/oK_!BIaajoBJr!!"nTk5=?A+7T=2>5@:^i!0M]!!%!2^B2,r'^G`#
(4<jj^B1T4!q60k!_fcl^B))Wp&G(DpqHeHnGiPUq7d!F#RL/)!+to+!j$;QlMpu#E3/f9!hMg^p&Osi
!Wkf]pT4Esp&G(@poON4nGiPOq5j_"#7'u'!+PW!!iB`GlMpu"Co7*-rMK^b63?WV!Wk]UpSS!jp&G(?
pnn*-nGiPMq54:k#7'u'!/L70!p,X`oDnXd!ZI?cpZ;P*>6F?p!WuZSpZ;Hsp&G(MpuVPunGiPbq;qb>
$4?P.!)3+$!l(]klMptk?FKUC!kW1Uli7(qBtO2U!+>L#!%do[!#b;,!'p=orsAZ)qZ$UborS7_0C&T>
#$%MoXTGJ0$g[ip$X]n/XT2Gr!!"GBXT010!<)ru3r#iW#l"B"6hR>XP:l/$!X;PppSS(f>RKft!X`2-
q543lp&G(?r29Lk!#G))!''bOrs8B"!*o3Z!R!^n!!3FGg\9h3iI;@(!!3XZiVDU9F7oS62>H;6+7T=2
:AEuO$i'c',e<W`!JM!L!!30dVt[q-^5!d"!;HNq*J_B+^Aq[8!!"SF^Ao/A!!#La^B2(R#Pe?#+fP+:
!I5+?!!30^QhRT^X9!VdkPtZ&HE@"G!*Ajo!%@WE!#P/*!'g:]!ilP2q#CF;U@tJcFU[a>r;Zm"30O$6
!iC,ZkPtZ&G,G/7!*&Xl!%7Q>!#G))!'U.U!i6,,q#CFGhtH14T`>Yj!!30ranOp!je=$a!!4C>jnn0?
F7oS62>H;6+7T=2<;GYXis?%g!!*:ppV-dDB*.E"!@<j#^Ap7S!!"tT^Aq[8!!"SF^Ao/G!;c`r;Ye'/
\-)s2!!*7`pT4Lu>ls?m!@!-gXT10<!!"eOXT2Gr!!4RNXno."(\%J*9)5RjV?6qs!!*7\pSS(i=p"$j
!?lpbVZ8I4!!"_PVuERo<;$:l-hsS>(@_A)8,9%aTE>;m!!*><pZ;P=Hir^8!A1GHjo@g?!:p0j6i6!G
F7oS62>H;6+7T=2@eo-fh$!uY!!$I$^AqC&!!3^Q^%T2B^V9m3!!!,u^Aq[8!!"SF^Ao/A!!$U+^AtA1
!!$-pXT2/d!;um!%qr$9XT/Ia!!!,uXT2Gr!!"GBXT01-!!$:"XT4md!!$!lVZ9HX!!3XAV=^Yc"69F^
"8etr<;$:l-hsS>(@_A)=S\ipQi7!^!!%-7joB/_!!3jmj7MI6"QTO_"T.<]F7oS62>H;6+8,^4!!%?@
joEa'!!+(NpV-]5m/R1k<jVA3!!D9^!!E,5!+>L#!%e,aqnE+KnGiQ=q7couq#CF6W;!Co;saPd"\tf_
XT/Ia!!!-"XTGW,=7uUo./9nE(\%J*F8;p<Mtm>R)5?l'!)`+`!X25fntuHinGr1]!!E+r!*&Xl!%7Q>
!#G))!,q\2!/C:L!@$IrjoB>e!!3@<f^n5+joj`F!!N2]!-@i6!&aQ6!$C_2!1EZF!4hn*!.ss[!HS;0
!!,'Qn@nr*j8]/^qnE,=p&G(DpqHeHnGiQ`q7co[q#CD<pT4L1!<DQg!Afo.XT/Ia!!!,uXT2Gr!!"GB
XT01-!!&5YXT3JA!;ultEqcI4A-))u!ATT'VZ6h[!!!,uVZ9]i!!"DAVZ7M*!;ultNVTIPE;9J6SbM7I
M?3,F!CXfojo>PF!!!0!joBJr!!"nTk5=?A+7T=2_tiEpRed!b.),Jk!L3iW!!+0up:gX*OSccm"69F^
"8on7^L6a8!%do[!#b>-!=um>^Aq^=!!+@HpoORP"n)El*.7I^!LJE8XT/Im!;-<l"8f2#=7uUo./9nE
(\.P,%]fE-!*K't!@+K:VZDAQmf3A-GkS$9Oad2*!!D9^!!E+r!*&Xl!%7Q>!#G,*!=bn$VZ9`n!!+e8
puVU`#4DNn-)KbujoNQ*qrRk]j8]/_qrRm"p&G(MpuVPunc/\'j8%g;Fnu(<KD<1^[2JoCoDeq%CV0>U
"1DJ?AGa+A"69F^"8fh5@.jR#/GQs[)=db-4nubl4o>9]!!%6<XT>46n,NLu@B'"'"/Ss%>5PE%"69F^
"8f2#=7uUo./9nE(\@\/!!#"RXT1?W!!%*8VZEA)n,NLt?DI7m".rEq=8Slq"69F^"8etr<;$:l-iBn@
VZ7M'!!"qPVZ8XO!!&VcjoO0Xn,NM#J`6@c"5@c$Gl-V'"QTO_"T.<]F7oS62>H;6+7]C39).NK9)ASh
*52-^!)i=e!Wl-#pV-mGHPHM\AGa+A"7H6`!!!,u^Aq[8!!"SF^Ao/B!!%3<^B)%`qZ$X7X8&ds9CVu`
!_8mWXTbeE'*&#9qlKi#j8]/^qlKj"p&G(@poON4nc/Z*q5j\!'Dhb1(o@#*!(cV[!WkcXr29Ij"f?&J
!!$*tVZ6h[!!!,uVZ9]i!!"DAVZ7M'!!$[-VZEY-qZ$X?j7qa:A,?9#!!37/e+_u.jcgV_!-nD'!!M?_
!!N2]!-@i6!&aQ6!$Cb3!0?s<"6CC#!;ultB_]=CS-/<^!AU/=^B'WNr;Zh.qnE+5j8]/^qnE,=p&G(b
pqHeBpAk-l!=,q+^At)+!!$@#XT=C`nc/\BNqTRULaW-$!*]9%!!D9^!!E,#!*Ajo!^j)lqQ0`1o)Jdq
U%tejQ21I\>PP)sL]d2J!@s$#VZDDrr;Zh!qkjDrj8]/^rhoan!*&Xl!($CX!"nf&!=#%hVZ;eS!!%HB
joN*tnc/\Q^%URhZnqX\!-nD'!!Mimo)JanqrRm"p&G(qpuVPmo)Jdsf(nG.`qo`:"K_C5!'0WN!Wd/P
pV-d27fiMf!+c&C!l)JPj8]/^qnE,=p](@5K"h&q!NH1l!!#C]^Ar3L!!*1lpoONQo)Jgm@]]L0r2g$i
5QUc_!*]9%!!D9^!!E,#!*Apq!Z-!\q5j[d!V69k4nu,ZAGZ?-"./e\!&FKQpAb6q?`*Rq!gZ"Nqu?^u
qkjDrj8]/^qkjEnp](@2EMiQ0!L3]W!!#+UVZ:0(!!<3$"jcu+!(HJZ!Wn#9pZ;P'<W`1!!-nD'!!M?_
!!N2]!-@o8![!roq;q_&!VQNm!!#mkjoC,4!!"eL^B'c(o)JbfpV-d?AIA86!+Yo@!!D9^!!E,5!+>X'
!X`JJr4i0E!)i@f!1*Dp!&OKP!%muJ!K7'N!!#UbXTGG+$2OW%>5PE%"69F^"9#>'XfY\$!!3I1Vt[:n
9(Dr^M"n(P0)GVK/GQ+DLB6uH!(Zd]!hrd'q>^LrqkjDrnGr1]!!E+r!*&dp!XVr%pSS!]nc/ZBpnn*D
qZ$UYpuVUg!V69k@JAmchg,_-!!%6@joOTIj8]/_qrRm"q>^R*Gi&2W!+PL!!4;O`!'U2Z!,_MG!(c\]
!<K4r^B2-$)Ya:4A,F"@"69F^"8fh5@/L!+!Cj-a^B2,e!V69k2#+fdXT\M$!+Yf+!($J^q#CErRea&e
XE>BT!!$4"XT/Ia!!!,uXT2H#!!30dS+j#dXCMA'!!"\IXT=spqu?`t@/-W"5P"jU!L<JY!iBrRp](:p
qkjDrj8]/^qkjEnqu?d!5*bl?!iB?+oDeml/bl4EQNR*b!/1.0!*Aal!<LI@joXY7+SYp:GPgM&"QTO_
"T.<]F8Q">!`dPAjoji/jb3d-!!#4XjoNg4qZ$Vkq7cs<#kJ#r'_oEC8G3#`A,F"@"69F^"8on7^L7!?
!@jE/^B'l]nc/[lR/"DrCAIo1PPM<]U^-Jk!##(/!($;Y!*]9%!!D]jo`+soqlKj"r;ZjFM"[qON\9l&
!<S/RXT2c*!!&&TVZE@oo)Jb'pnn*Vp&G(nqkjDrj8]/^qkjEnr;ZjEKD)2DMCnB!!<RuMVZ9uu!!'t5
joO-Bo)Jb-puVQXp&G):qrRk]j8]/_qrRm"r;ZjS[.`V_]fkod!<]h+joBo.!!*eJq7coVq#L6k!#kXI
!%@O@!+Yo@!!D9^!!E,5"^h<1'R@Fe^B1W9"7Z?k9_c@']cHtM!"o:5q5jX8nc/Y,poONAp&G(rqlKi#
j8]/^qlL$'!!!XLXS8guT1K.T!!#I_XT>I@qZ$X0VYR+iC[qH*(\jm.,PD*;<r8cp"69F^"8eu";ucn2
C8Ua'!LcIX"7Z?k6hmP[V&K42!>sqojoCY:!!"/:jo@+/!!%6?jo>PF!!!0!joof+!#Um[pZ;P,@0H*#
!*o<]!TPF%!!#1W^ApUk!!!r4^Ao\U!!$O+^AnB)!;6Bm"8fh8?jBrEpV-dAD%?%8!>`$:^Arua!!"tQ
XT1KS!!!l2XT0X?!!$4"XT/Ia!!!,uXTMW/;l'/i!if`>n,NJ'UA1hjGkqC?2>F'L3q<7N(\jm/,67H<
!*8up!!D9^!!E+r"&oJ%T(f,aUgOW#!!*e)pnn+6q>^LepuVQPp]10k!$M(!!&4*H!-e>&!!M?_!!N2]
"*4`dg@s_2iIhg4!!+%kpuVRLqu?cu!+G]<!PT6<!!!r4^Ao\U!!$O+^AnAs!!!,u^B'=kp:gWd+n#C3
"H`Dn!PU#Z!!$-sXT>L8nc/Y,poONAp&G(rqlKi#j8]/^qlKmLQM.E]INIqX!<[rKXT>LLq>^Lpq547j
&Fof$(\jm.,PD*;<r8cp"69F^"9,4tVZD.,p87q;*U`t/"+L$C!N%.=!!%-:joONZnc/Y4puVQ1p&G):
qrRk]nc87]!!N2]!NO36joMD/mf3@lXn_#ZjYHZ4!.XgZ!2f8d!#kXI!%@O@!+YuB!l)JPj8]/^n@o"!
3pcnID>1dFK_YTJF8;p<Qgk%U)#:97XX*T?!*]9%!!D9^!!D_m!L,J/!!$L&XT3S@!!$s5VZ;kU!;HNo
(\jm.,PD*;<r8cp"69F^"7W2hO#-/'!+5Ju!-@u:!<AP`joEKm!!"/:jo@+/!!%6?jo>PF!!!/kjoNFj
m/R-=pZ;IJq#CD^q7co_nGiP-pqHeWp&G)&qnE+5j8]/^o"P76=9e^(nGiPipV-a?*Vf[8MYX@SGOYY5
)#135,k_3<>5PE%"69F^"9#@qXTG:o"ml9i:A:jkW#GI3!/:6H!-@Z1!#PF.!$h1;!*8up!!D`koDejn
ntuP\9a0na!)*'a!MUM.!!'M(joD%D!!"/:jo@+/!!%6@joOTIj8]/_o&^#,C'X,+!,2,h!T53u!!'+r
^Ar!<!!!r4^Ao\U!!$O+^AnAs!!!,n^B2)l''oT!;SMn?!+Yd(!1`ke!+5O%q#CC3poONAp&G(rqlKi#
j8]/^oW81qCCoh4!D9HfXT2Q"!!&A]VZ9ul!!!i1VZ7t8!!$'sVZ6h[!!!,nVZN]-&F9B!8#E2^q543n
p](<?q;q[+nGiP3puVQ1p&G):qrRk]j8]/_o]?58NY_Hko)Jf#jnIm;GPV:@"9c40^Aq:(!!!r4^Ao\U
!!$O+^Ap7S!!"tU^\Y\GOsfSr!Wc`DpV-a$#PnE%!s>FrXT2)c!!!l2XT0X?!!$4"XT10H!;-<l1A.aM
KHog`!WcE)pT4IX#5S<$!s>4lVZ9B[!!!i1VZ7t8!!$'sVZ8I4!!"_GVZD;lli7(f<2TDf!K.0Y!!3<-
h"g(4BCPs%+Sb(!0_PJHGPgM&7-"=J6M9IAYV5>C!WmK*pZ;Lk#l4N&#7%s<^Apk#!;ZZq)Yh&I./!W@
@f*nA^5!`m!!4-o^A#ADWC$^Q!!*IXp:gX=-2@NB#7%=*XT1]X!!!l2XT0X?!!$1!XTGSM)X%/&)L8FY
XTFnQ!UKde$?Z0Ir2g!u,5D3?#7%+$VZ9!P!!!i1VZ7t8!!$'sVZN`=)X%/&)0MhNVZN&C!VQNf!!*FG
p87qc+o)*>#moYfjoANR!!"/:jo@+/!!%3>joXY=,No+/,,+,qk5FEDb>89,!!*Rup>uD5/boAJ#RJ0?
^ApXk!!!r4^Ao\U!!$L(^B2#]%.aJq!!3RB]D'&A[p]O-!!+aMotLK&p](@##H[a'!'TiP!#YL5!$q7<
!*T0#"0JP0$g[ip$XTh,XTGA%#O;?j/!fk1!(Zea!XAt-q543SnGiP*pnn-;!;?Hn<r&WpUKe/m!!3L3
U\CYfTMu0^!!+O2oqqdYp](@&$K_*G!)`IjqZ$U=puVQ1p&G)9q;qb;ILb]E!Y0Y;pZ;P4F:%75!BJ3n
joAc`!!3E3^A5MD7I^?X)Yh&I./!W@@e[V=Y"Sod!!33pXnTR3^4$ma!!3aU^APbB^B&BVp](@##H[a'
!']oQ!#YL5!$q7<!*T&u!hDa]n,NLk7%O(S!j$DWo`4^d!YB.KorS7.!VcWr#7%.%VZ8jL!!!i1VZ7t8
!!$'oVZN5P!q60k!^W1LVuERqVJ[+6!!3[DVY-hfA-)H*!X]:qq;qZUnGiP3puVQ1p&G)9pZ;P)>6FX#
q#CHu>1!$+!p,dhlMpu$O6#ur!K$pQ!!3<-](s)@:[nDb)Yh&I./!W@@f=(;^B'cVnc/\CReFJsR4de*
!X2Z4oY1F*"SVlt"U1k#XT1l]!!!l3XT>OLp&G(qorS7R/+NZ@.Z=#&!K&>l!!3="U\(YhQim'_!X/b%
q543]q>g9j!#PF.!$h1;!*8cj!J`,p!!+O'p87qG.-gj7"\bKZVZDt`pAb0t!=%KXjoAcY!!"/:jo@+/
!!%38joN%Rnc/\M\b>.d\2W^R!X<Akq<%V;!QkT?!!30%ZMD68?h"*r)Yh&I./!W@@e@D:^4.!n!!3sc
^A#ADX\/`c!;c`s3hu8\!PB!<!!30%U%tej<q-.i)#135,k_3<=nJftXE,0N!!3mUXS8gsSH2+[lMprB
PObgVWXeb'!W`=kq543knGiP*pnn*:p&G(noVVbfD\`*Kr;Zm5DPm0+!gc1SlMpr@Nq0(KU^m,!!W`>Q
q;qZunGiP3puVQ1p&G)9r9!h;!p,dip&G.6R-"))!mk*QlMprS`:E$kiY1tb!295'!-[l4!#kXI!%@O@
!+PN6!k;YEq>^R&@CZ'H!kW+SlMpr-MXS:[6hLEZP523[C\[u+!!!l2XT0X?!!$0mXTGA%#PnE%#?[kt
XTGJ.$gRcn*.@:X!'TuT!0-fP!,(g%!#PF.!$h1;!*8Zg!h`Nuq>^R%<1ru`!i&s,lMpr*H1\$4VZ8gO
!!'n3joCJ4!!"/:jo@+/!!%35joX@]$Mj`($?Y+ujoXLi%dj>r!!+FDn)aUIo`+uMq7copnGiP-pqHeW
p&G)%qnE-FpV-d/6im8e!WbZfpV-dDKcL'lmJm:tD7f5N!-Il6!.OaG!/L(E!#YL5!$q7<!*T3$!3Gps
!gu4QrVup!!BceEXTGSL)X@A)$t?7)XT3).!!%<?VZ;>=!!!i1VZ7t8!!$'sVZ<UgVZN)F!WE'#!BQJ>
VZN`<)=%8($t#guVZ:?%!!&qmjoDaX!!"/:jo@+/!!%3>joFN;joWb)!r`0$!`7,8joXY<,3o41&;/s0
joCA5!!$p4^B(eIq#L6k!#kXI!%@O@!+Pi?!B6VD^BB`K!%3s'^B'uclMptg:Ts-"!1ri`!+bo-!N$%k
!!!l2XT0X?!!$1!XT:2<p8nIO,QK'Bp8n@X1$\f@"%]'RXo5@%O7`JQ@/6]$TEXld!#PF.!$h1;!*8up
!AKE)VZ_Mp!$ZseVZD]/lMpqf70&bBVZ;VI!!%`KjoO6Anc/Y4puVQ1p&G)9qrRoH^@p[lYqQ/2YkI2[
^d7htnGiUn@+4K)!5A++!)31&!%[U?!#kXI!%@O@!+Gc>!sA^&YkPm8^664F^\PVGZ;Lhk!!+jGlG!A3
#ke5u7JNtb-h76;)#135,k_3<=So3#!s/QrTD,GhXG!\LXTG1h"7#pf/WT+u!N?=t!!#@\VZ8%6!!!i1
VZA"BpAb1nqkjMu"%JaRVZN`GVY?tiRn*YI!!+X-lDFZX#PJ,t>PR=\1\^tI!!"/:jo@+/!!%0=joYbi
@FY&6!p$THpZ;P.@g2/u!Be'\joOEJp](?q!$q?S!+GEu!#kXI!%@O@!+Gc>"U"f*%W/iG^B2&e&F0;t
)M5]m^\PVE,PD*;+o&/>=RlFl)#135,k_3<=So3(!rr<1A#et!!ifiBlMpr&FTAN,XT0L;!!",9VZ9]e
!!!i1VZ7t8!!$$rVZd/&!"<82m\^,^@Li88nGiV,EMhrt!$Cn7!%[j,!-Ic3!$M(!!&4*H!-S2$"U+l+
&VT-;k4n'?ieJ35!!4:5jlkh,.eWiC"1.g<!M0>`!!!r4^Ao\U!!$I+^B20b"T8<$+cGj)!KJAi!!3L=
\adE8U/^p&!'U#U!<](lXT=I`o)Jb-q5j\",k_3<=So3#"8r3#*e*U\!Iu9X!!3I3W:?tjP>(bR!&sTO
!<\ngVZDYUquHKl!#PF.!$h1;!*/oo!!E0"!?HLUVZD/dlMptm=JG>`!KB\GVZ8UK!!3-'f_OY1^&dg*
!$M(!!&4*H!-S2$!!W<$!@Xo9joMJ2lMptpHJe8T"2e^4k5+3?8bE&`K)!(\-h@<<)Yh&I./!W@@Jde>
"T&0"3hu>^!MqsF!!30kXSop,^BClC":)[:^Aq.(!!%3;XT0U;!!!l2XT0X?!!$-uXT/J#!!+sAoW8.Z
2td7F!!30dS+3T`U.kaqXSJsu8bE&`EqlO4,4bd7(\jm.,PD*;<VrZo"8`'!1QV@0r20RW2<t5D!Buh>
VZ`P`":(h"VZ96[!!&Sbjo@(+!!"/:jo@+/!!%0>joOTJqZ$Xd`Ur9n`_#Ir!WlEKn`Bu,B*AV'q;qZc
o`+t`pqHfPo)Jb/pqHeWp&G)$qnE+6q>^R$=LIk;!H\h<!!+U9n\5.=EtSBO!4)F8!+5C!!(-I_!,MH3
q#CC3poONAp&G(pqlKi#q>^R#:o*fe!GN#0!!+I'nZ;knBFt.C!294j!*8dn!<>C[VZ:B$!!!i1VZ7t8
!!$$rVZ6hq!!3<uT(]&_Adn#+!@<BgVZN]+&,lP1S>W:^VZ9Zg!!$-rjoCJ6!!"/:jo@+/!!%0=jo>S]
!!3C?g%OP/N"PCV!Ah+Zk4n'?j,4ZO!!(XHjoBJq!!*VBq7csA(A%S,)Yh&I./!W@@Jde>"S_ru&pCt_
^B1Z;"SVom!!3m^^@Ar=OX9o*!2fS,!,;*+!=l+)XT>@7oDek.poONAp&G(pqlKi#p](@,CTIB8r2g$n
8H\G^!Y]LRnZ;hE,5_E@Qhd``?hFC"%AW`s!MU8"!!!i1VZ7t8!!$$rVZ6ho!!3^EV>$khRn!SM!!3dK
VX^PbINeUh!0R)T!*o0s!>=AejoOBYoDek6puVQ1p&G)8qrRk^p](@2NoTlr!nC]_n,NM-PiVAs!Nn$P
!!(+9joBl&!!%]I^Ar?P!;ZZq)Yh&I./!W@@Jde>"SMfr-^+2<!M2.>!!3C2[dh*6Va(:[!!&bh^Ar-D
!!*(DpoOO0oDek.poONAp&G(pqlKi#p&G+<K_DMKO"^))!X;W#nZ;kZ3W]*X!0dDar2fs.oDel4pnn+'
oDek-pnn*:p&G(mqkjDrp&G+;JG,lAMCnE"!X;Mop8@hd!g5MDqZ$VUq544"oDel`puVR7oDek6puVQ1
p&G)8qrRk^p&G+HYkI2[^-;8kr;Zm)E80pF!m+1<qZ$W6q;q[0oDekNpqHjA-1q6<)Yh&I./!W@@Jde>
"SD`r!CNjc^\Y\H^4[I"!!30cVX_D&[pB=8!!&kk^Ar'A!!"hMXT>FFo`+t/poONAp&G(pqlKi#o`,$o
4IPrG!j$S_pAb6q3LB9<!iAs&q#CD[q5jX*oDekGpnn.g+S>^7(\jm/,67H<!*/oo!!Dlo!Wb?HpSS(i
Eu=WO!Wb6BnYZG];@!!t!0I#S!+,9t!(?VE!T>U,!;c`r+Sb(!0_PJHFo1;$"n_is!`7,8joXY:+SPj;
!DLT)joX=X$2FQ$`qe`sJbT6D!!*.qpqHir"82]p)Yh&I./!W@@Jde>"S2Tp#@Y.:^B1uZ$i0i(-'7Z3
!ks$tpAb2rq7co?oDemnPPD6\L]d>N!#YL5!$q7<!*K-#!!Dfm!XDi)pT4Lq>mgE.!?m'fXo5@'XDemJ
!!&ScXT2St!!*.\pnn.G"82]p(\jm.,PD*;<VrZo"7lKo#?7AjVZNSr$N:&(!!+3knYZGcC_QOC!1<S[
!*Jjn!<^77joMjmp&G(8puVQ1p&G)8qrRk^o)Jas!Hd/ljoXIg%f-/+/?SI)!p#UbpAb3@q;q[&o)Jb_
pV-]8p&G(2pqHeWp&G)$rP&EK^BF',!Z-="pV-d38HSkk!YBFcn\5*k/G9&E"2+HE!*Jgm!(6L_!*8dn
!#YO6!NdX@!!$-uXT/In!!3mUXS8guSO*DW!!3[EWq!1lM(&&t!<]@tXT22h!!#=ZVZKcs!;HNo(\jm.
,PD*;<;WQn"7Z?m'Q0fBVZN2M!r`0$%V2C*VZDGup&G*qV"png:%nYd!!$0rjoBJr!!"/:jo@+/!!%-<
jo>ST!!4.-jnIm=cr^DL!!3jlipl.3[PdaY!X.NFqW7cmo)JdoV>.e+]J]E`!#kXI!%@O@!+Gc>!!M`j
!A9i7^BBoU"BDeu^B1K.!qcNn)#1iG7e6T\"-rY`!NIjJ!!!l2XT0X?!!$-uXT/Il!!+R-p8nCR.0KZG
U@G>eS3d;M!!!f0XT1WX!!*1`pnn.g0)#>G(\jm.,PD*;<;WQn"7Z?n!!"I&p88%I-Nm&4nYZGT5Q^TY
!#>:,!']uS!<pL<joOI,pAb19puVQ1p&G)7r8n%B"n)El34\bF"Lg8mB%ZY9!mapMo`+t4puVQVnc/YT
pV-a7+nu$;)Yh&I./!W@@Jde>"RZ6k!_]Zi^B)'On\5.9Ad\,0!&s\f!&*mC!'9kV!hgY8q#CC3poONA
p&G(pqlKi#mJm:i7%O(S!N_j^XTGG+$1e,s1AIsO/+ruA!!#"QVZE;.p](:1pnn*:p&G(lqkjDrmJm:i
6'q>D!N)7SVZNSq$1e,s0`J!IVZ81:!!#afjoO'^p](::puVQ1p&G)7qrRk^mJm:j>1!$+!Th`!joXFe
%J'Q"6hodD3V!.N!KZui!N[::!!!r4^Ao\U!!$I)^AnE'!!3OB]Cs#2^B'!,nGiPqq7csE'Cl,(!J:'J
!Lju&!!!l2XT0X?!!$-uXT/Im!;um!$=BdrXT<V_nGiPhq5j\!'(Q#'!Ia^?!L=Su!!!i1VZ7t8!!$!q
VZ6hc!!3L4UZeTVEu=EI!)r]k!N$J"!!*,%pZ;M&+o)*<+Sb(!0_PJHFSk2#"mc3j%Y!C#joM(snGiQ0
q;q_>(\%J++1_-\!N[OB!!!r4^Ao\U!!$I)^B&3]lMpu+L;*#h!M2+9!!&#S^B(J<o`4pj!?A'4XT=n6
q>^L4poONAp&G(pqlKm0%-mlp)L8FNXT=J8mf3?<rN6%#!M'8]!!+%5pSS%X+8Ps;(\jm.,PD*;<;WQo
?ju?$!Z?-Xm&'lA/c5V@!!%BAVZE.cnGiS9htQ76cRSbk!$M(!!&4*H!-J,#!JM*N!!4@<jnIp2joN1Z
mf3?fq;q_*!q60i=SBK1Zo\'a!#kXI!%@O@!+G`=!j>B%nc8Ld!B-V>^B1Z;"Rc<k$G#uI!/U(D!)N<j
!M_OL!!!l2XT0X?!!$-tXTG+b"7#pf0p1q,!h`*emf3@pW;3OqHg^q7:%kIcSMU-C!#PF.!@%U=!!$!p
VZN8T"7#pf08o:s!h2[^mf3@pUA:\eGOGM3CA-cjfLG`<!$M(!!&4*H!-J)"!n1KZlMprO_!gCeeR8XM
!!*Pdq;q[QpAk!h!<S2Q^B2,^"oSE$)Yh&I./!W@@JIS<S2'=0!X)E,o=k@>D[u.7!^j`;qS*#7mf3@i
IeKlFXBl)/!!!l2XT0X?!!$-rXT=D5lMptg9;1sZ!ifc?quH9f!'L%Y!)i7c!<RT@VZN`!"oSE$(\jm.
,PD*;<;<?lLb%ck!Wtu_rMTCf!i065m/R,Ipnn*fmf3@jW:o?TjEq11!!"/:jo@+/!!%-9joN+Wp&Odd
!X3)boB$,6Kb<\P!)WIQ!,_-(!>)1%^B'oYrVup:pqHeWp&G)$rP/3D!J26U!!3[M]_9)@M]qBd!/gQd
!%717!=tOiXT=J4rVup8q5j\",k_3<=SAitFVsEE!Y/hBp8n@E*pWe+IJBoE,OPO4%[-XcrMK[R.K0;I
(\jm.,PD*;<;*3jE>Rp@!Y&V7p87q;*U<\*H2+9;,5)$4!!*eUp#Z:h3;rmX+Sb(!0_PJHFS=htS07+t
!YU:Jp>uCS.-gj5VZ,`Tjo@(%!!+:OotLXDJKY"3pqHeWp&G)"otLR<A.%W&!@*X#^B12m!VcZe!!++R
q7cs2!UTjf+/JS3"KZ_e!#YL5!$q7<!*8cp!iK6/lMq#0J?>sNXTFbG!UB^d)QW\9!Lj,W!!+.4oqqqi
E?,#qpnn*:p&G(koqqkb=:+d'o)Je5I/0ZAO#-n'!!+"7q547Y!UTjf.G=CV"QZ%#!$M(!!&4*H!-A)#
qW7k9Gms!=!@k,FjoWOm!UB^d,NJU^!R:c5!!+gaoY1IALemf\!%[aC!(lds!j"lmli7(f4f/+l!ju/7
kl:^+pqHfGlMpr:Vu!OmXTGSN8GK:e-h[N?6M%;\Rm7#@!!30\Q2RfdUeq<[!!$d/XT2i&!;HNp/"uU5
!iC01pnn*<p&G(Xo;;YU4ot!M!Wb3@rMK^g:'Kk^!+u/,rMKX&lMprIhXoq3jJ-,Xjo@42!!$-mjoWk0
!pfmg!D:B1joX4O#5%uh!!&#RjoC&!!!,$gl+[3Rp&G+)[dq06Q7M8$!=)7"H[o<5kPtW(]D0,@-gC[4
18jB=!%mmE!=u$tXT=5*qZ--d"U7A5FA`\6!!+";poON@l2Ui=U$8HT/G9&E%\NZspSS%E-0kO7#!m$D
:Cu^i!?.a.VZ7q+!!,FCl/ht.p&G+-g[aJ-Znq"J"UJ:rRV`i(!!+>'puVQ0kl:`<ZhqN,^ApRm!!,[*
o"P7?H54a+!<IuN^B']&o)SLb!@so0XT1HU!!,EfnuVtpD\LFs!<INCXTP]-M?2rA!@jZ*VZ8aM!!,?^
ntuPdCD,8"p](<qG5.s9K`UE<!BSlujoA0L!!-3`o&^#7P8WWcjo>D_UA3jO[fP[m!@"E,^AqC.!!,-X
n\5.6>mL?/e,TJ8pV-\sk5YN)QKtXQ:\4Vf1me0CorS:l<!UeN!'L"X!']QG!?I<gVZBKlo`,"JOn#=N
T2>j@!!#(SVZ8jB!!+Ohqr[G2!,D-+!Cb*"joX:V$./_Q:\WuO;tU.]!!*Udm(WODo)Jgs?+0:<!iA3`
e,TLbZ2DB8^B(27jo>DlHgIj7C\%N-##qGhXTFhM!T*nN!!*e,poOR_"Qf[b%<q0:!,(m'!X;MonYZGN
3!&OLj8]2oS+rl^OTaeH!>;0ojoCG5!!3FFg[XD+a8o!9e,TLfebJ8-`s(Q)!Wc60m_8ajnGiV*HG8pa
!K\VY!!*:gpV-\uj8]5^9;_0[!Nh=N!!3gPXRWCnJg&\F!<n5PXT1WI!!30mT^J]XL[b?G&o4B7VZD5h
ec5^SK(l/C54\dF!!344h<sD*](#b%)3a.OjoMS8ec5^UZhih`joAHA!!+'sn%Sn9$h+,s/!f_?!k`Rd
i;iZR!<ITB^B'c)iW&usIIF9=WXA4q!@N]nXTGM9&G#nb!!*+>pT4IT!oa1\(jYSJ!Mg(l!!+BuntuSf
Uh((i!!*+:pSS%I!oa1\+f=_j!TFUZ!!3-V[.38[ienQ)!!*.dpZ;Lf"5s4]!BQhB^B))4mf3Cj8$)6q
!jbl0g].?UE;.*J^+J7C!!**WO797O3:?hK!^N7FXTG4k"P`tX!G;).!N[a?!:Tsi!A]Q%VZ8XD!!33c
QLUjSSP'+@!!*+0pSS%h-f=t+!Ca`ljoA$B!!37'cgg-!fOkBI!;c`s!f-O4!TZ/q!!<6dQ+lk)!.+#4
!X`JKn\5."3<AgRl2UhfG4rZNEnp]t!BGq:o;r"2m/R1o>H%4srN--b1]cJ6!<[-2XT3"i!!<6\Ju8.;
!,M'(rW!!+=JG>`!f\r9hZ*ZZBD/5'ADI4f!_fr^oB$%:m/R1rH/J/S!lIG-hZ*Z\O7q]9M;812!!4Qg
Yk>a3[0l7#!ZH[)n\5*\+5m2#%ZC%q!N$4m!:0[e,\E\AXT>4(li7)(G-(59!IGgF!!*OXp8n@]$/,@\
,@d28VZE@qli7)'Ei/B)!I#OE!<)s!%!qWF!Kd]B!!4j1eFhr)g(!BK![+&qn`BkJ-M@H+!!*\1p>uCr
%G1X`">OPW]D0,@:[.o\17e0SqnE3EC^oG*!ACDF^B(nqf)PpU/RF=6poONdn,W=c!A0?%XTGM3%-.Bh
/"$%4!N7?s!!EBS>)&gIVZ90N!!+X-nYZGa?4>lp!@a6+VZEM<gAq0P"9go8\Dd5F!+5!k!Be'cjoXLn
&EEfl3Qh'X!T5d(!94%Z.JUXYUBKi^!Wu6&n\5./:B]k]!Y01`otLK&dJs7npoOR]"6ojf"%T!RXTG+b
"7#sd!!3U@XS&[q8(%A;,l"8<Ns"YI!Wtl[nYZGV70EJgli7(q@]&gr!(G<9!&F?3!Q>6-!!3:1eGSJ&
joX"="m>pf&VfB>joAc:!!*+ppqHf#oDnOa!Y'"Yn\5-t56:*N!XVu5oY1BCd/X1JPPhQ]XT1]O!!3R<
Wq!1mO?!@.!!3F&TCf5c@b^tW!!*+[pnn*WkPtYm?_m4i!fJu<li7(m9q(^P!+5-oj8]2]_t`?o=6KVc
&;/s3joW:k!pfmg$Yn2`joL)7d/X/KpqHj2$KhBi+,]R&!i&^+nGiUk+DCh]o=k<R!RLfH;#%-nRgJ6X
!??OWXTOb\%fl/#!s'ELU%>AeE<4Dd!)<6d!L=&T!!+'brho@c!ffh^nGiXl**f$*VZCW8ci=&\puVV'
%.jPl!!+FDnE'ejAJFY7!s'cufCS,*Q3,D5!=u^<^\tnID<:g"!BR"F^BD0-<@.qF!!E]eA=^I*^B&fe
g&UgH!=l"%XT2hm!!30YPOP[WWIIVe"o&'#$SP_EXR`IoEs(b/j8]2iT_PDb?fh=i!Afc*VZ`c@8g+B5
!!EW\=G`pGVZC]<rW(@H!>=5`joC%r!!30j`:2mliMgEA#P\9'%R,0OjlY^tjoLhQc2[i`pqHjC1Z\T<
"^&/#^C.feT8.T+C2\EXW4hZ7!HS@f!!$U*XT>ITjT#>c:S[?[$E0&4CLU[^Dh+4Un#ZV("3gfG@eci%
V(M<>nc/^p9qC^M$DNH%B3nhOCO;8An#$1t"3gfGLAU-4joOL*jT#>dC=qt:$K&UmNe2b7PH)dcn)aY/
"P<_J!!*nHpqHj3($#>r&Tte;^B2)Q!U0UF!!*h5poORf'BB,p&8J8rXTGP$!W)lF!!*e.pnn.Z'''#o
%q_ZpVtd.kV,%-9!!+(spuVV()<:c!'oh8Ck2te-j)"h?!!$d.^B'`/irB*,Ok7>KY;aQ'!+>Q'!K%0U
!:Kmg,D=[N!M;-h!!$:$Vu<LoL'Zf>!?lsEVZE2>e,]1B!.Xb*!OrNt!!+^UfB*+_6L"R/!!*M2pV-`g
#NGdc!CEd>^B'-)qZ+nA!=PImXT<qVirB,]4IP94pT4IC'$(%R$CLRc!IG%2!!30^PP1p9VZCuSa8c5N
dJ)c(WX.bfr;Zm":WqJS!MgRQ!!#C[^B'?%q>fa[!XN2ChS0,o7KLL/!^*TepoORI$/tpd#?ReZXTG%X
!S%2@!!#(RVZD/OiW'#b<1r*G!gc%Nk5aE?!)WCO!NHUg!!3LKgtq/pcr:&A!6tQF!J:$[!Ljqb!!+X_
k.gi/!k)VI_uKf=FnVp<N#(@P!@XuCXm3"iV-=;F!!*+?p87qI($GYo!!+ICiMQaL=:2tH!<J_ajoN(7
q>f^Z!B&ipjoX:_%`88J&#m><^B(Q"irB*=YN!:uY[e?m!:g*j%[m$m!M;70!!+jHiiN9S=qKZnhuEce
PP1mTRPWt(!AKr$VZN;g&+fkI!!*_Up>uD*7cOIL6dk&X"QnjrGSS!o!@kYR^B2,m%d*fn%WoGX^[Su?
]oGPe^&S0\W:m=pXD8:1!<)s"%;Dp)XTPVS5R5"'!@=K6VZN`.%/^+l!!3R@VW=WWV0kH3^&S3jhra[q
!p,ITk5YPqN9''^"66C]$-`J?!!,R'otLR6<<qgi!XD`0otLL@o=kFBXFEeSg]643!C*[YXTG1j#O;?k
#>Li`XT5HoXTY_qF$^H+!6kKE4f7nM!h2gflMptk8t,FN!2f@c"f@W)5S*q-!!-'[p#Z>,B*ml(!XWJg
p#Z>;k2u@!"Qdss=;JFI!*Jj-!j,cCmf3A&?3%)!^Ce1[)a.DHKp.srRZW8C=?79"[K$;(o;r.d<>#93
nGiV'<Li]`&Ze\D3)XF8Ko:tLKQh$)2&65$!!,floVVbW;\JO!!YSCtoVW:u9,KQ_A9EEWM2$M$@ne`o
!QG-0!!$d*joWnM)".G+(idmojq6]f+A-L.Ts;/A\Z_W]C.93Eg]6%.!+,62"M9Xj*<Gm7"9BK=N4\Yq
!+"C\a8c3?nuW%pJ4UX[pAb<s)G,FYnuVmkmf9cr!)rHd"JgB7)?KR4"9BB0HDL,0!)]Nl!-7Ym"Q?@h
,6@N=!WaKR!NG&KjoB@q!!--7oY:@>$a5M.>"h@Q9Nl@mYOK:-^/q-2rVusoXRN>"T7:EL76Wn(;.P-J
n>u_m:U^>j!!,`in>?Y^H=BZ:4?Pr+@="@2VZEYgaT1#p!GLQ`jpTY;L2:'m;HmskW717u!T[tL!65'?
6FbR\!P(Vb!4;e-4JpZ2!N83]!2BMp3hYK1oVV_a4J2ZT:Yk[*ioU:!;PO6j!!+FCf=q?b.'s!?!!+=0
f<#(@-,or<!!+7)f;AY5,M3":!!+^lfB*+V1$SbG!!3RU^=p=&Ih)>UU&Y6&Dli$%pT4I;%@dD"$>ZO4
VrafWD[`9=r;Zm/Pi^W]!LXP*!9jIa4/q&N!j"Wf_Z89g!B-A%XTG"R!S%1h!!+p?h5:=@3!&1BZN("r
bMD:^cV=N:!2';n#[k(&^\khJ\7Q)6!!3C,V"h(WXTGA)$(M"m!!3C)T&HRKTNMT(!9jIb$?OnZjoX@c
%E&7o!!3^BZK8h&[;-K+!5AL8%pPahXTG;,''91r!!3X4SE6XMSmE')!1Nri'RA<rk549Bg4:*&!!EU%
QbL6$^B;3?;[o2roDet!7>S&2XTPYa9+7p&iW'&d6\M?&VZWfP8IN95ci=.U>d`\Zjoa_XA.R&f])VpP
=,sf\^B;'3>p8,+W;m#;:Oo>4XTPMV<$(T1QN.+)9RNN'VZ<FmJPdGD!!49WWW:lFjoaPIE%%%Qmf3q)
.o:2CT<Gf>^:UYENc\8S$DmgZ!"fD_8S*@4SuA`lWM#H*Bh^)a\,a\P&I'ON@X3m"U8Ff_RuMf-8gt(h
!4`(A#W#nDVn^[;jQ5@N_lAZ-3=O[CVZ7;6.o:2CT<Gf>^:UYENc\8S$LRnZ!"oJ`8S*@4SuA`lWM#H*
Bh^)a!.t7O"qW(M@X3m"U8Ff_RuMf-8gt(1!:Tt##W#nDVn^[;jQ5@N_lAZ-3=NJ!J,~>

%%EndBinary
grestore
np
grestore
149.911 527.283 mo
149.911 525.334 li
181.591 525.334 li
181.591 527.283 li
149.911 527.283 li
cp
149.911 519.487 mo
149.911 517.539 li
181.591 517.539 li
181.591 519.487 li
149.911 519.487 li
cp
149.911 511.692 mo
149.911 509.743 li
181.591 509.743 li
181.591 511.692 li
149.911 511.692 li
cp
149.911 503.897 mo
149.911 501.948 li
181.591 501.948 li
181.591 503.897 li
149.911 503.897 li
cp
149.911 496.101 mo
149.911 494.157 li
169.791 494.157 li
169.791 496.101 li
149.911 496.101 li
cp
187.531 537.027 mo
187.531 494.157 li
175.651 494.157 li
175.651 482.457 li
143.971 482.457 li
143.971 537.027 li
187.531 537.027 li
cp
187.041 492.207 mo
177.631 482.947 li
177.631 492.207 li
187.041 492.207 li
cp
179.121 478.557 mo
191.491 490.737 li
191.491 540.925 li
140.011 540.925 li
140.011 478.557 li
179.121 478.557 li
ef
.75 lw
0 lc
[] 0 dsh
149.911 527.283 mo
149.911 525.334 li
181.591 525.334 li
181.591 527.283 li
149.911 527.283 li
cp
149.911 519.487 mo
149.911 517.539 li
181.591 517.539 li
181.591 519.487 li
149.911 519.487 li
cp
149.911 511.692 mo
149.911 509.743 li
181.591 509.743 li
181.591 511.692 li
149.911 511.692 li
cp
149.911 503.897 mo
149.911 501.948 li
181.591 501.948 li
181.591 503.897 li
149.911 503.897 li
cp
149.911 496.101 mo
149.911 494.157 li
169.791 494.157 li
169.791 496.101 li
149.911 496.101 li
cp
187.531 537.027 mo
187.531 494.157 li
175.651 494.157 li
175.651 482.457 li
143.971 482.457 li
143.971 537.027 li
187.531 537.027 li
cp
187.041 492.207 mo
177.631 482.947 li
177.631 492.207 li
187.041 492.207 li
cp
179.121 478.557 mo
191.491 490.737 li
191.491 540.925 li
140.011 540.925 li
140.011 478.557 li
179.121 478.557 li
cp
@
gsave
2.1066 410.531 mo
44.0636 410.531 li
44.0636 353.277 li
2.1066 353.277 li
cp
clp
2.09 353.19 mo
44.11 353.19 li
44.11 410.61 li
2.09 410.61 li
cp
/0 /CSA get_res setcolorspace
gsave
clp
[1 0 0 -1 0 570 ]ct
[42.02 0 0 -57.42 2.09 216.81 ]ct
snap_to_device
Adobe_AGM_Image/AGMIMG_fl cf /ASCII85Decode fl /RunLengthDecode filter ddf
<<
/T 1
/W 116 
/H 159 
/M[116 0 0 -159 0 159 ]
/BC 8 
/I true
/D[0 1 0 1 0 1 0 1 ]
/DS [
[AGMIMG_fl 116 string /rs cvx /pop cvx] cvx
[AGMIMG_fl 116 string /rs cvx /pop cvx] cvx
[AGMIMG_fl 116 string /rs cvx /pop cvx] cvx
[AGMIMG_fl 116 string /rs cvx /pop cvx] cvx
]
/O 3
>>
%%BeginBinary: 1
img
jT#Da!WiH+o`PL'"U5/7"9S]%!#YhA"U#&9!!!*2&f2/c"U,8G&.]Eh&ISpOqu@$-!rr<&"UGA;!r`3"
!UBa_!;?Nn!rE*"!ri;i!!WK,"9SZ+!r`0&$4dg^"n;R!#nRII!W`<'!Wi9#"9AT."9S>urr`6%rrMZj
q#LEqrrW0#lMq=r#RUtN&I&4<$k3^Pn,O()%1*+="UGJC#Qt//!s8Z.!Wi9#quQTnncAIbqZ-EmmJmIq
"U"i/!WiT)!!WT2"p+c+"9&9%%LN=8!!<9)!WgjPrrN-$rWE0'rr`6%rrWN0"9eu6"Tnf,q#D96"U>88
!!3?4%L<FQ)DtN;ML]D>4=V9`%/g/+!W<#t!W2ot!TF+U!W3$!"9&B%!V$0f!!E<("9er,!!*-)rW!?2
*B7#1=[Fb^&I8RFrW!!#"TnT%!!3'!"9JZ.!s85trr`6%rrMBbq>oj]"To#=%hB!I!Vl^'(Go!#=[Ok`
&-`4<r;[0,!<<3)"U5,4!Wr<&!!;orq#L!emf<1bnc/gp!WW6$!WE'&('ss@&HMe1$N^D4!W`E($31&-
"oA9%!<N9&f)YdNrW<'$!<N<$!!rZ-!sAc3"p=u.rW)s!qu@T;"pYGB"qhpc,&sdEj42&T^<PKn_3.kI
"p5nV"9R$Pq>pEo!!2forrMusrrN&u*!$6K#6k;2!snr4;2VlmV3$1]Pc1jQD)`"*&Hqk/!<<0!!r`5r
!;lot!U0U_!VcWt!<N?*!VQL4!XK/A$3pP5#QOs$L:+@^Ndc\HVm)D"1^O-hqu?]trW!!#!Wr?'qZ6a!
quQQmp&X@WrW2Wk"9AZ2#6Ol)&-`+;!%b%bBKdFn>a)L:-5$1V"9Jc1"9SN%!W`?(mJuJOrW2s!!!2rs
#6=l/"U527!r`0%!<WE*qZ%Z=$P!mZ-]m&bSqDWIF(]]QH#AJ=c-sNo.ME%#&-;G(rW2Wkr;lfrq>g*f
q>^["!WrQ/!rDut!W2p?!X&c4"98[@XEnDH5s?e>/3P^;8ogAuS0/@C!!ir7!W<!#"9S]+rW)ouqZ-Nq
r;l?en,NUm!sAc3"7lL7!X8`/!!d5>HXoT34XqC#4"_mMD3UZW(^pBE&ebHMr;[$)"9S]+!Wr?'rrW-"
o`4jimf3@h!;QWo!VZR/!X&Q)":"r-!!302i&2>Z(B=F9"pk2.$l*Htf`2<i!<<6.!Wr?$!<WE#!!!&S
!;lln!!E?*"9o&2"9SQ&"p+o2"9JW*rW!uB!#-l8goQ$MEcc8>KU%FBK84DNB8*GRc#FO2*!c0;!!3'#
!!2cnq>p<jquQ<f"p+l1"pY83quH]s!!<3'rW"&F!!NsCY&ur],U+0F.QT4,.l8C^,=ZddUJ:dh&I&ID
rW!!("TnW&!W`?'qZ-Kpr;kgV#6=o0"pYD;!q?6m%:?8^(dg)-,oddO2_#dm//\d54DD$l:]h"B#mL8-
!X/].rW*!#rWE9)!Wh'V!s&E(!Vl`o!W2p9!<E0#"q(M5!!NB2!!.9X!WW3&#S.:H!s/W+#Q4W/#&mZS
!"]SH"pY&,!<`N&!;HTF!!E?*!s&E#!<WB*!s88u)](-FhJRseH[UL"Lk^S<Ljs]/SsG4SH$dlo4p)6J
$Np,'rW2]mq#U3irrMNf!!E3'rW<-%rW2`n*srgXY;8<c+s8*W-mg5h/LD]%:.[`)4@Z*X,lf;!#6"T)
"U"l,rW)ouqZ-Wsq?$Zti;`u^"9er3rW<6(!<N>r!$2T=X>E0k.OQSj,p40J*YoD<5<C\I0fY;n%KI@H
!r`0-"U+u1!WiH+"9S]+rW(jV!W`<'rW<0&!W2rs!VQKo!s\](!sSmA?2=O&!<WE#!"&c/!!!FMGQ7^J
"TAB(!<WH,!W2ro!VZTV!!NB)!s/K(rW3'#rW!-'!WiH,"9SK$.0]hm9C90"IpRGJH?OXdK7\AhH@pm%
I!9^OF'XXdYTjc!!WiH-!s&Gl!<*$!!r`5r!:'Uh!<WH,!<<0""9JZ-!Vl^<%5c4`.l[nV'bLli*?laM
)C-ph/h8>!-T!5X`g.,;&H2Y1"9\W(p&P$lqZ6`uli?n_$NU;1!<N?,"U"i+!rW9'"9S>u&LG/A-o___
*Z,J&()@Pj!XfeB(^qB&*X4?_C]FGH!!!)t"TAK(!Wh-XrW*<,!sAc2"9S]+!<3'!!Ug!n#GO3Y$31&.
rW)s$q?%?5#64r@$36_Y!"&]+"9\f0"9SH#rrN'"g].N\"U>89!s8H&rW!$&!<<,t!#l"G$kasFhj7;p
J9P^bKR\Q+Jq/5oI"6j&IsV*D%WlQ<b/%$h!sAi<"onW)nGrRir<!!"k5Ynl!W`9$!<WH+!!<H/pAb6t
(EFR2C)T2c(B>6`%hos)+X89]/1rS*,qCT)0euLrSN$KI!!N9$!<WDt!;urq!ri;b!"T)4"U5,4!sAc2
!WW?."Te>t$j$[7>7`bF*![Z*&J,Tf%LWID#7D%T&.TKq+;u.UMi]Xk!!ri3!!3B0!s/N)h#ITZ!<N?+
"o\]-"U"o+!WE'!!rW8u!"8l@"T\Ue%1ECD!!*3"!!iT,!s8T+!s8Z2!!!0+!!$1oqu?d%!s/2t!!<*$
qZ-TrjT#bm"pkVB"Tnc,!WW3%"TnZ'(^^up)%6j-BX-TGCgUdqKTC\<Lk^M4It.HH%XibTJ9l?bJ8&(g
Rb(:L"t:)q"TSN)nGrRir;us!kl;.n"9el/!<<0(!s/W1!r`0O!t,PH!!"$9QGQKU)\s2/*!Zlc()\/<
.5!5(.46Ml+WVm`*toZ+X!n#[!!<-"!<`N(!;HQn!W)ou!U'Ln!<i]7#R(>5"9el/"U>//!#>_I$jQb4
%6T-?4<tIL(*Fn9',1uc$2t/K"pG/7#RUb>(+C@F,\a;+!"],6!!!$*#6P#.q>fRV$ipA1!X&Z2"pY>:
"U+f+$ig8.":,>?"onW+#Qju*$3gKF`"rCR#R1M9q>^[#!sA]-!W2p*"98T*'USq%$NLD4p](<r"9&H#
!<*$!!9O80!WrQ/"pYA7!!392&Io-V%gN@g=g%>HWJ[-E?X.GiJqei0L4t5/IJeI*I=Hj"Isc^!Kk#7R
cCQ!b-PZdQ!<3)u!r`5r!:^$u!<N<*"U5/4!!*-+$O-G./.F_'d^4^;DBU/:)Aa>.$kO0l*$?LU/M&A!
,pjub+sJEl3Z^4LSok#5&dRn+rrMuu!!2`m!!2lqqu@0-!sAf5#R:G3!<NN8#Q=`B!!!KiM9)Q79i_Z6
#8.^j)\Wl!&If'Q#6tJ4"W.LP$4IOi1Hm!C7@S>u!#,b?!!EE,!s/M]!!<6'!X&B("9S`/"9\T("T\W(
!s8W(!"oSB!"/c,?-nri(CpoS#7:Y@!r;m#!<WH-!s8?""pPA6'aW&1oDf!q!s8Z/q>gNrn,WFgo`,F%
#7:kD!XB/C%2^E=1`(_ef?'k;>>\1p>[V#]G'\OcJV&H'I=(s='mb4SIY!0,Jp_WUE->9/nr+_4%1NC-
!<3*"!rW/^!#PkG$O[(;!<`B&!t5DG=eD^_G"aA-*-35J*>]e:(_dVu)BBqF,q(5m-mg2b,pjuc+rqUJ
0,6df@/pB0"8r3$!WiDt!<*#s!ri;q!;lli!$_UP$O[%:!<iK(#8%C]@&L/sE^UrZ#[IiI#o+0j'GV>s
'+c,n$OI(E#6tMA%1s9i(DRZ,/.t.\@/pH2"p+c*rW<-%m/[+dpAc$3!sAc3"p=u.!!!$"!!*0'!<`Q/
!WW<+r;[=:GZ,Fe!<i]8!!EK4#mU2*"T\Z,"9\i+!;lg&#n[@AK)bl["8Dir!rW5b!!NB)!WrK)pAd2U
$46k9!"^Cb!%`!"o"f`_<F'BUG&bB9BP2I1G'JFaIXQWjG^"=SG^4XaIt<3'IW8q@I;EP@hZQ%a'GL]=
!;QZf!<3)r!($\d!!*92%LW=<!!Eu9!"),S]n\cp'HAVS2_ot6*uQ:E)AsJ7+!DmU-7:2h-6sf[+X/*T
+r:b5/g;N'XV1^8#lO`)!X&Q)!VcZo!WE0"!VZTo!W<'"!VZQr!XB)>rW"&D'EA+D9:!S[7jo2n-6al^
D\`ik(DRVu(`*r&'+k]`r!O>M%M9?i(C^Tf.30NlX:kX8$NgA/!X&W.p&OmgquQTn#QXu0"pYD>"TnQ$
*<ZZT#QOi."pbS="HpQ"!!!'#'+"dK&.J[F#mUP,!!WH*!WrK*!W<!'!<<-#!!<50o`,!n!r`;l!;QU!
!<N?+"9S]"!$M@K%134R(CMO1^<![18kr`*C1^p\B5"npF)Q5CEcueVrd#K-G'.nLG'J=[I!g?jIt`]'
DKM7cUA#NJ)@HECrrM`lq>p3g!W`?'qZ%uF!!!*/%hT-K%1*"C;ja#(63dZ+(E=8,&fi'7,psf]+<;OK
,:"T6-5RsS,U4HT*ZZ4@+=Jfa(a;X+Bup>\%0le3!s8]/!VZTn!WN6#!VZQq!<E9$!rrDu!%@mJ"UY\C
!"&u3%9B!lLIr-i*$6:@&df6_@1sCg(_dSu)B'G/()7Jpr=Ai<'bM)p*[DR7*ChSl`rHAT#Qb#."9enr
!<3*!!WW8s!!iT-"9o):#R(8+!!`]<%1NLU!tGD<C6'P;!"B,;#Qt,-!WrQ-!<ri5o`,*q!<N?+r<3T4
"9JZ*%MAi2!!i]0q>^Krr;u6a#6=i,!s8Z-!VcX.!WrH'$OK%i_5i#h6;:cn?!UcQ$[HQ(CVOh/DK^&>
Fo6P(H$=FSFa&(VH@(!dI!pU"I<0"7A#&%#+:o%]!!*-%o)SRep&P'mq#CKt!s8W'!#R,;TS-/j#RqXc
%L`gd.30BLE[)hN,p=<?+XSQ`-R^>h,U4KV+<MXErYlLk,:F]S&JuL#Yt,*#$3L;/!X/]!!;HTk!<*!!
!r`9%!q?78."n:L<%JLm+<)%-%iQ].&J&:^'+Pcj&/?*%)&aA0(DRVtq%FDU)BK_-#S@e\X[NEq$O-_7
!sJer!!`N*!WiH+!Wi)s"p"f/"U>88qZ$s)!WWuE!!"j?8.#7qrs8T(!W`9$rW33*!sSu4oDeso!WrQ%
":>/0!"8i/EWuLJ"8W#t!WE/d!!!'!!r`9%!WE'S!WrE&"UkeH&./n>W5sci4[)SH>?,$EBOt^b@;Khs
DfBN7EGorEH?spbH?j^XGBeE3H4P@KH@:<gFGZE:BpZd_#7ge:rVus#!Ug$d!VQKn!WE'J!<N?'!!*<.
!!<3$15r,A,S(7u,8q.0*?,e0'bMB*E$$/@,Tn0R-n5-D$77#B+<M[H*?6";rYcCj+rhIT7Q2f-Sd,6&
#6Y#."p=c'q>g-grrDuu"9JW,!s/B$rrN*!,Qn/K!<<*SN2U;7&IfR'*>BA5)\`hm#7h;O%LrgZ&.T?k
)B8Yq!?)jT)#b?N().Gr()RVn-9Ee'?C:rs$jd+<!sShs!!<3%!<W6&!WiE(q#CR!!WrQ/!rN$3!<`E'
!!HEc%g)q7"pG)/!<`Q/rW!0)!<<3*"U"o"!;urr!Y#57!!!')!<Wfl!!N?'r;Zj!!;lla!!30&!r`9r
!WiB&!!*3,"pkYD"q2)7[]XOA4@)8%92SYi>[LfD@V91dDo-L4C3"93F*MtVH[L0dH$FRZH$Xa]G^+L[
I=HTgJVJDgGh=#L"p=i)rr_Zhr;lKi!!*-&"9\K#.kI!E80JHS%1Nj^'GM<!'b_<"',qs2*Zc1C+<Vs[
.k2tr-6jWS*?6%<)ZCTg)B0_@*?6F^/MKSs!<N9,!<<0+"S;]_!W<'"!WE*!!r;ls/-qT$8g=lZ%Ls*M
',_Ju&.AsW#7V/M%1EIQ%Lj'h)]Tn@+!)IDrYudp)AsA/()7T$&e>m++=0.L!!*--"98N/"7Z?t!<E6'
!s8Z.!Whro!W`?(r;[04%0-j=L&_8T!"8c+!!3-$qZ$j&"9er5"p>#,!WN6#!W)lr!W<!"!<WK(!"8u1
!XEfI"TSf0!!!'!!;urb!!**%r<!r>!W`9$!X8r@((_N85GuhP4\&7B92Sel<)rlt#$>5F@r$#$$#slt
E,KQ7G^4W7Hi\S?rcnisH$OXYG'J=\IXM-?#B5!!fbbb1!r`0%"U"i,n,W@eo`,$o!<W6'%gN(?%3L8%
:(S3\(_[]*)?(?b'G:rg'cIc)*,lr>(a'qE-S-eu.1%CK+s%^C)B'J2rYQ@f)]g+C*?HFN3A.N9%0-P3
!!3E0!V?Bg!WN5r!AOWW!<E0#!<N?+#QP/A,)3-q&fMf0'c7o-'+kcb$4$hC%L*:M?k!JI%1E[Y(`OJ;
r?2@f+<M[H*?5h5)&O/,(D@;i',<&CVuR2*#6=f+#6aPs#lt&.!WrQ.!s/Mq!#5P>#7LY:&-+))!!!E-
!!il>"p"c,qZ%*."pbM@"TeZ(!WrQ.!s8H&p&G-p!sJT'!<W</!">e+"TT#9!!!&]!&XcY!sAZ+!sAZ*
!sJo@"q;7dNp:j4-Vm8q6qpQZ;GU.h<``C,@;'.dDo?X6BQ%d+Ed)eSrd4Zkr-8p"GB\4SH$apbG^"CM
G%9GJ(^0d;!!N?*rW2KgrW2]m"p+c)!WrK/rW"DKDoPTR!$2gX$P=*h'+YZg',2&l()mo))f?Z8(EXbC
-S-eu.46Aa*?4tqq\U"b)]]k9*$HF]/[k]c!!<3$!XJu2quHKlpAt6n$ipA1!<<-&!!!$$!=&N'%Kg^l
;ZHe@(C(?]'bq;grX9JK#R1VG"q(iH$jm+G$k3gd)]^"Cr#m"%+<MXF)]BS1()7Ai$kX(!,Hq.P!!NB'
!sf&!!<3*"!r`9&!Whon!<NH(!!<<B^^U)?!s/T1!r)a,!sJl6"pG&.!!36*"9S]+!V??m!X&E%$j6P1
$EX:3!"K/4!!2orrW2Ee2us*a!W`E/"9AZ5"W%pm5LYic69@V076j@>;,C"^:fCG">[:fQ@r$##E,K?-
DJjK=G^+L[H$T72rHA]qH$X[WGC+1IC?-9E%/g2+"T8Aa!!iT*!!*3'!!*3V!"/u7-FRq9(_.8u%gNLU
&eGK\%1j3h'bhH'',VX))]BJ6+!E!_/1N%o,9ImD)?(KM(D@W'(D[r6*\T=\!!!6)!!!*,"Te,nqZ6Qo
"T\Z)!!*6%!"/l/$O-e_[r`c3&/QH.&I8gZ&Io-R#RUtL$OI1N"q(iG$OHqE$k3jf)]Tn@q]He!*Zc=A
)]0>)'+G9W'+cB;ZN't2"9JQ*#R'SrrrN'"rrMoq!W`9$rW*9)(^UY90)tt_o`4jh!<E<$":5)/!!*-'
!s/K(o)SdlrW!?3!!!7u!!N?2"98E&rW)s!rrDuumf4j=!X&T-"UG>;%2Kim&:rb;6S:,Q5t=C69iFtg
:f(%i=^><>@qfIhDo-H!DJ*m)DK9rGGQ)jaG5um`G7&J5FE_VGCZ-*@%K-8-"9\N%lMrgD!WrK)!sA]+
"Ukh?!,0;+*sMoT&/#H]&/5ci%Lip]'c7]#(E*r()Jg<1'cnG>-7gYr-6ra<*ZQ%7)#>'J((h5o(EX\S
1q*Gb#Qau+!sf&2jT%1>!W`9&!s/H+$k31:BuMnP#RCbL'FtWa'G:l`#mgtK%h&dR%L*:L?4.)C$k*RY
)&jM7*?P,#rZ;(['cRu)'+kTX$4mds/$T'S#m:;0":#%r!;llo!"T)3!WrK("on])!Sm_U$j?J.!s/Q,
!qlU"!<N<)!W`9%!WE0#!V-3q!<E0#!=/Z*#m?Xr!<<K1!!!'!!;HT`!&=TX"9f#:$P!I]&1#Sg1H?p<
4A&%,7o3/c<E)mq<**7/?!_#S@r#u!Df'-)D/F<;GPlXaFoHR]G7A_=F`VPCF`2S@h%^G.r;Zj$"8`,c
!!NB)!sA`/rWG+_!"Ao>[sSl*"9f8R&df*_()@Ss&J,Ng(E"#((E4#))Jg<0'cnD=-7^Pn,pFEO)]9J/
(Dcrc'G_Dt'G:ul*$@0rZ2ak0!rr<'#R1)*rrN*!mJo0H!<<-%!sAT5!"l_h()I/[&0)>j%MTWm&e>EZ
$OdLV%13LS#7M&K$jm+H$k3jf)B'P6*$$(!*rI#n*#KD'&.8^K%hpTHXT/>-"p4i.#6X8lp](a(!WrN-
"TSr2!7aaW$N1#(!!EE3#Qt5&!;6Hc!<3)s!"&`4!!!%["98E/"8`)s!WN6#!Ug!g!WE-S"ptJ5!"qE)
BKJOB2).0a76sIA<*!!t;GpFn=Bf!7@:s%aDS^7.B5VR'Ed)_NFo6@\Fnp1gF`VPCF`2P<gCju(r;cj"
q>p9i!!2rs#lt)0"9er2!WrT)!!NBNThHCI.hi?n$Pa0X%29Nl'G:uh&el-"(DRc,'H%g+)As50*?QRW
.4-8^*ZQ(8(]"m]'bhAt',)-&+?)!Z!!!9,!<<3-"oA;u!Vufo!VHEm!WE'1!@X[:*?c1-"Uu7Z#n7O^
'-7\p$jm@N%M'!U%1idS%U]_R"UtnN',_]+)&aD4*<$uV*#0D1'b_/f$4@F\/h*n&!"&o5!!EN/k5Ybg
!!!$$!!!*)qu?eb!!r<!"9\r5!Wi)srW)`pnGrRiqZ$X!$N:#/Mu`nY#m0u(r;lm!rrMHd$N^J>!"pc9
Z:$2b/H.U85=S(08l/Gd<)W]m&5uS2=BT!C@;0SoDJa$(D/BDrGB\1Or,_jZqK33iG'%eIGA_S7fFSAs
r;cj!rrN-$qZ6NnqZ/q^!!*0)"U,#2!WiN*";u3I-OKhW%13:I&.AjS&JGfj&J,Ne'GhW(()\,-)B3N4
)AO85*[E0^,U"3K)Aj8+!#GAF&f)5t'cA/<2(u-5!!`W-!!<H/qZ-WtrW2lr!W`?(rW2Wk.fpQ-ROARE
#S7FO%1s$U$kO!^%L`[N$4@:Q$jmFT#n@JS%L`OO%1X$h)?(HV)&aG5*$"qs"rnU%)&<r#&.]3\'c/DL
WrN,+#6b)1"p3ugr;dE2"98E&"onZ(#\seJ!X8i)!<*'#!qcQn!WN6"!U'La":P2/!/UUS!=8i*!;lls
!ri;u!;cfp!&joY!!Wl?!!"<D]i-"">;\H$4?u;(85)iX;c?Rk:f("f<E3++A70(e^i!t#DJa93GBS(L
EcM)!rcA!Z%s<#<GBJ"NH#7P:cjL6`!r`0%!Wi?&rW<'#rW2lr!!3'#r;dZ8!sJo4!=92?!!!`tUc&2S
1C=Np#RUJ<!t>eR')iIa&ebur)&O,-*Yo\7DB'Q0*?6(E-RBrY*#]\2()@Y_'`JgR(Dmr**$c[]2Q6TT
"UG21!XAl*!<*'"!W2rt!W3#o!!!3%!"T`,Uc/8V2@U0($OdIQ$P!(F!=TA8$5j3[%L`[R&IK$[@LinQ
%h9'_)&O/*()If*q\g7i)]BS1()7Gn',_T80VnaL!Xf24!sShj!!**%"9S`/"9\Q%!tF5i"8;cs!<N;q
!<*#s!r`5d!"Ar/!!Nc2!![`Q!!!9+qu?]tr;ls$rW<*#quHQo%0-A/!WrE&$5XKd%XZ;2-pK170KLdF
6:4+19MSA\;Gp@hr_O;+;H$S"@pWe`^MRe!DJa93GBS(Krc%jVr,NBjF*)PJGBS+RHYdJ=`s<1U"o\K,
!Wi?&!WiB'rW<*#qZ$Zu!Wr?%)$0jA"9o,6!"0JP!!$Z:$m#TX"UkA5$OR.>$iUV[%hK<b&ebro(E"&+
)BK\7*H)o:'ce87+snQX*?#b2()@Ya'GqJs'GM8t(`=20+=86_5G.uW!"/o0!X8c(!!!-#!WW8u!!!&t
!WW8t!#,GA#ljs:YRDTZ$4%.B#7_1M$k<dH%0$_7$5j3[%1<LQ&do6_@h9+U%h9*`(`4#''GVB"q\fAO
!#bbP&/5cn*#Kq^S,`Tj%gN(9"Tdif!W`?)qZIQ4"one"!!3H2(C'p?"Tnc,!s/Mt!<*#u!riB%!ri;e
!"Ar/!!Wi3!"N`P!!!6)qu?]tq#^Kqp])K>"9o)7":,;="p=pF^Gn5'/MT1F2*=5n6qC$J:f1+g;,R<h
'N%b,<Eis>B5>8"ChIX&DKC#FF)_2!rbqaSrG`BhF*)PKG'8.XD/4C.&Ie^DrVus$!rE#u"9/H&!VQL!
!X/f7#6bA>"9&9&?)Sb^rWb%_$3CG?#m^nK%h9*\&.oNg'GVH&(`+)4(E=H6*?,_6*$$4M,Tn'E(`*r&
'GUKZ%29Nl()Rr.)^-US/4Gj'!!N]3!!3?,qZ-WurrW3$p&G0q!WrN"!"rG2*#](h$4RFK$4[IO$kEgW
%/pVN$47.K$k3RO%MB-\&Ru@^#S.CT',VN#rY,AJ(AesJ)$h&q()@St(*".m,<q=i!!Nf9!!3<*k5YVd
!WrT0qu?_fr;[3,%L)n5!s/K)"9S]!!<3)u!riB%!ri;e!"8l.!!N`1!XW<@!!!3$!!3-#!Vlcs!W<'"
!Vud?!sf;E#mLqX#m_/V[n%i%0fM!K3Bf\q6q'[A:Jand;Gg<j:_ci+;cR(4?Y=/hDJWs(DJjN>G&qYA
qelCO"`SF#EcZ@%FpWJBDejg,)[cWJrW!$'!s&H$!!<?+!s8E%p])37#R_%F!t,\@!!6)l/I2ps%grXK
$4@4K#n-_B+qG1q&J>`k'c7f*(E4G4*$&r<)\jA5*?lgU+<;=:()7Pur=]t]'GVB!(`F;3+XeWg9T0&R
!!r],!<rZ'!<*'#!rW0!!;ca$!X/f5!!!$(rW!7!RjnUS%1isV$iUV@%1E[V%LijUq[45L%1<LQ&do6`
@h9+U%h9'_(Ddf#',2/sr"fk\(`=2-()7Mr&JZ6%,"%(`!!N`6!!3?+lMpncr;Zfu%06S:!!WE'`;fl@
!"925":"u.!!*-'!s//srW2cqrrMHd%06J0!!ET/"pJ-3"98Q&!!30$!VZZp!rrAu!"T8E&J,6K!"T/>
<m36K0.@G]0/P[N5!VG&7S6BN:f1+gr)"5-<)cn'A7'"d^i""%Df0K7G]n.JDf5Dg'5h]+E,fo>F`hkR
I;s+VWuDQL!r`0%"U"l-r;Zp&"9S`'!Vl^1"UtnJ!<<*#!!#9k'FbKS!X/i;$4Hh?!=K;9%fHn[&.fEe
'GVH&(`+,5(E=H6*?,b8*??=N,Tn*G(`!i#r"Bk\'c%Q$(`F;4+t+fl;MP>U!!`N)!<r](!!<?+!s8B$
q#CL"$4-k4!"(`h%gi[I!X8r?%K6hC%1NdX%h9$W%/^JM$k3UQ%MB-\&n;I_#S.@S&f2;t'+trm(&SgX
(Ddo*()7Ms&J,Wo(a;M"rW!*-!rrB,!pTah!W`9'"9\T&!s-XH!r`0."pP,2!s&B%!<N?)!VcZo!Vuls
!WW8i!"]/2!!**#!!<H,!tR[-!<<3"!<*#q!WiB("9&E'!r;m>#Se'e%13@_1`j8%2EaGa/13,54[)(s
6q9jD:/Fec;Z0H.;H$Rq=']?EBPbJ%D.dd)Dfg5IF)c'uD/B,c'PqT&DJsK6EccGJH[TsQN27@(!!3'!
!XAo2qu@!+"9S]+!<N<'q#D*6&Io'I!!!?H"J7:_)]oLk!!<W<rX&`8$k3^F%iu8n&J>cm(`=/,)BTb8
*H)r;(*4J;,:=c\*?#b1(&ejL&ebom'bqK#(Dn&0*?lp]0O021"oni-!!*9,qZ$a%"9S]+rW3'#q#CL#
%LN=:!"9M@QmWL_*=N#M":bq@%1*LT&.f?_%LigTr<jGO%1EUS&do6_@h9+T%h/s\()@St&ebomr"T2I
rYGkV'+tlf%h]Zq+UV"i!!*'(!<<0*"8)Wq!<E8t!!!-#"V:b;"UG).ScAuq!"B27!<N<#!!!'!!WW8r
!;urn!ri;k!;lj+!WW3&"T\T@.N&3d!WE*!!WN3!!rW-'!WrQ/"U"T$+9W8_)\No=,o,'E3'/WO2)6gA
3]oSk6:FF;9MSA\;H!Hj),aC5<``U=?taAlDJa'+Df9`BG&qV?ChmebBcCf%CMRa'DK'T:Fa&4^FDID:
'G:BH!!!$*"p4]&"9er3!Wi6#q#D$.$NLV:!#5e?\4%,J"VM7M!X8Q1!t,JF%K6k:%j)>o&J>`l(E"&+
)BTb8*cN,>(*4J;,:=c\*?#b1'GLHY)&!Yt()Ic()&aG8,:Y/rD0l6f!!WE'!<iW'!!i]1!s/K(!WiE!
!#Yb:#lk52!"8i-YWWL/!>#VD!X9#A%1WmZr=BqZ%h9$W$k!FO%1N^R%MB-\&n;I_#7_1P&Jc)prY#5E
r"KYV()@]$&ePZb%MBQo*aWa`!!NN,!!3?,p&P*nrrW&t$N^G2!<<?9"TSN*^AIs5#7(G6qZ$a"!<N9&
p]16np]CHrnc8Rg$3C80!!39)!YcgoqZ-TrquZft"p+l0"U5)1rW!`;"U>#@%O*i]]$JKq.R#pN2)mQU
3&iu+5=%Y*7nH?J:Jgpc3)W[T<`i[>?taAlDf06-DfBfCGB7_?CMIQsB4kmkBkhF"D/XE8Fa/=aF_RqA
&.nmD!!!',#6Xl(!sSo3!rW/s!#Ye?#65,4&0YSQXJC=J()%#_%1EUN#71bHrXJf9rsp.^&.oNg'c.`)
(E+A3*?K/?*#9V;*[<$Y+WVI;()6ZZ(_[W"(Dmu-)]TqG.P!*#F8uLF#6=f)"U"W%!sJf0!rN)s!"f88
"ono/$QEB7URZQ/&.SmMrX/i8#RV"Oq@Ec?%h9$WrX/i;%1EUS&eYQ`&n;I_#7_1P&JZ#o&eP]gq\'JS
'c%Q!&eGQ_%1s?l)K'-c!!NN,!!3?,p&G'nrW3'#r;[Q8#7(;0#6Or+:lM^p"98T,!WWB0"8`)t!VHHl
!WE0""8r9$!<</l!;urt!XJf,!<WB,&02>Z!<*#s!rW-M!WrQ0"pG,1!!39(!!!0QL!ZkY4taNK0eb@@
4$5Sb2`a,g6q0[;8k_uVr_X5':f1+i<`W=/ART:h^i++(rbr3eH$==KD/3iuAnE#pAnPaiBkqO&E-$2J
IXlTU\;^h,!!<3$!t#;9qu?g'"U"r+!W)is!W<!4)fN*@&/52.-j0YW$4dUT#mLYB%/gY=%1WjY&,m+g
&J>co)&F)-*u>q=E#ou8+!)LL-m^#W)Aa,%&eP]g&ebuq(`=20*"a26,qCQ"Mf/S"!!`N)!!EB)qu?g&
"9S`'!W2ot!rW*5(i$7,#Rg]j+TMKC"q1nJ#R:YF&,m1<&-<@O%/pVJ$k3RP%MB-]&nDO`#7_1O&/>ll
r=So>%hfWl'b_/i%LijY'c.d6?iC$/"T\T)"pFZ#$3://!s8T*!!!')qu@3]\L%^b!'CSg!!36&!sJN%
rW2TjrW3$#qucp"rW2Zlr;liurW*3)!Wa2O$N^/*rW2s!!!<'!/-?"Z#6kA8!WiH+#R<02Jj1hM5<Q5B
4t\WN5<_.h3''5h77Kd<8P;cR;,R<h3Di[R<``C1AmoCj_/F4*EH#l>H$==KChdWqARo=_AS,RgC2@d,
Ecu_WJ9YkGKa/+g"98E)$O?k4!!EK0"9JW%!;ca7"99aZBH@Bk%h!q(%KHV<&.]0T"pYJE%hB0L%06qL
r=Bn[&el)u(D[o2(EFQ9*ZPt<*ZlXU,p=9I(DRV^&K28q'c.]))B0Y;+=/Nj0U?AP"TSf/!!!-(!W2p"
"U"o/qZ6Qo"9ecM[q$3k!=K/8Gn:5]!!Nf@$4$hA$kEs`&c3+@%h9$I$Q'9]$OR@V$P="^&Io$U$k*[]
'G:uh&.oNO&e5Qh'G:re%1EXV'Gqa?=8i1'"T\T)"pFZ#)Z]s@!s8Z.!<<0)!<<*$Z2kI9!!EZG#64`+
!s&H(qZ$[!!<MclrW3$#qucp"r;lTlr;d$&!WrN+r;d!#/-Z=X!WE)t!W<'"!W<!E!X&]5#6kA<"UG)S
45<t!8O>Bf3k@dF0K2$W5<_.i4?l/$7RmYR8P;cR;,R9g%8p/+='/d?@;0SpDf0:gE$odRGB7\<BkM!f
@q0%[AS,RhCMe$2G'SOcH>UcH$jlt<!!!-0#Qsu)!sJf/!Vl^7!WW9%*A5K#)C64,!!S)i$igJ=&.]3W
#RLkJrXSo:!=fY=&-3@U2\[#E(D[o1(EFQ:*ZZ%=*ZlXU,p=9H().An&.oKe',;<#)&aG6*Zu^V0J]5&
!!*'*!WW3&!rDs""9S]+rW)ou,6.`H!<`BD0$-<o+;+_U!.P@\!!*94$k!@H#n.=V&J,Ka&,m+A%h/sH
$OI4N$OR@V$P=%`$5!dS%L`aX'bh8mrX])B')`CQ&eYik&eGN^$k*XZ)BF`,rW!*+!WW9+"82]r!<NB&
":58;!rr<&&tf4.qu?^<rW!$%!s/N#!!*-%nc8XirrW*#rW<$!rrDipquI3-!WrN+!<E0$!(6eirW2uu
r;liu!!3#u.KKVU#mLM<$k!RX2mu+K*\TZ:1/YbK68Uee5<hCs4[)/!77Kd;8P;cRqbR`"<*!(&?=dPZ
D8L70B`;rVG'\@QDJEisAGfp<A7Z!YBPVI(F*;m/HjjuAA.SqF"p"],$3p\2!!36(!W2p@!<<*%#6Y58
.ASLK!!a&?!#gUu%06eD%M'$X$471N%M&FH!=fY<&/l/p()Ri')''M6+)rAC(EOV>,Uar]*#KD(')iFP
&J5Zk(Dn#.)]Tk?+XJiE25WtE!!NT/!!!'%qZ$["!Wi6"+9;NE!!<K2#RDrW/2$u*$NU5@J,olT":#8B
$jm:K%1iFL!=o\=%j)8j$O[:L$k3RO%MB-^'P7sg#S%:Q&JYum&.]9_&JG'T!>#kB&do9_%h9$X%M0X(
P;rOA"9nr.!X/Q+o`,L'!sJf0$4[:@%0GVm!sJ`)!!*WRrVus"!r`5u!<3)i!<3*"!rN0"!rW/k!"]/4
!sA`/!<<*$!+,^/!WiE%!;QWq!W2pH!s]/:!<WZ8,8e0k3(,AL>pqm6[l[)?5<_:s5sR\$6:4.07Rp$C
9i(ab*D]I-;H-[u=C,NGBl:e,DJ4!-E-?POEc#N'ARo<L@MrZdAnYprE-$5LH[:*[gK"Ud!<rQ)":5;8
qu?a!!W2p"!<N6$)?9sD(^[6$)^>Ug/H?"mIfp>e$k*UU%h/pUq$d?7&,Ztl&ec#t()7]-(*+K;*uu+<
*ZlXU,p4-C'G:uh%hK9a&el)u)&aG6*?H:G0fH:!rW!B4!<<*$!<<*#!<<*$!W2ou!X/K&#mLMN%'MZ3
+pJ#\-ia5ZGQ8*O"pYGB$k*LP%1WmZr!ii?%LigSrX'SQ$k!CO&e#BfB+kg^%LijZ()7Gn%M'*_&eP`T
&.T9b&ePZc%LrpW%j*$g/H,VQ#6Or-"U"Dt'ESCA"9JZ1!>PU4"9nr.!!iW+%NYHI!!30&!W<#t!V$0i
!WE0!"9/H%!W<#o!W2p#!<WH."9&9*!W[KG!s/N)r;Zj!!;cfp!$).I$NpG1#6YTKV`Qpk9NXnS3D6V=
9Kkd-5<qM$r^-fV6q'R8"\D?\:/Fdd:HD<M<*!(&?"@>WDSg@1BQ%g.G'\@QD.mNl@q&nU@:E_WAS5ap
E-$5LH[1'\i^s:[!sJ]*!sf)5!VQKo!<`<$)[-3D:lQG2#9kW7%0.#c";M4Q%1NdX%h9'Y%K-\;%1NdX
r"&lA',VK$()7Z+(*+K;*uu+;*?QOU,p4*A'+kfT%g`dY&el)u)&aG6rZ)7c1,l`u!!*''rW!!#!<Dut
qZ$X!"o\K<"98U)Os(_K+X[p.!"*ZF%KZn@#RUqJrXJi:r=/`9&.K!S#mgqH$k!CO&e#EgBG;-l#nIIS
&f)2p%h9'\&J>Zf&.]<`rXfJK%hB-[%1XO.W$2-?"U>/1!X&W&!!!&t!#,J<#6Y#,!W`Z/7K<i*!XTDD
!=]qE!!NE+!W`9$rW2KgrrN*#rWE-$rW2uurrMrsqu?j#!sJi1rW!0*!0mNd!<WE#!;cfq!!E<*#n$n8
!#GqO\TKJf1dal+8NT\Q4A7q+5X7V%6UUf?#Xq3R8P;`P:Jh$d)c0F3<`W:-A70+h_f9R,Df9T<HZsIG
B4YR^@f9^:@UiscB52:&F*DtXG_'ql4pMK!"98E(#R1A3p&G*p"8r3;!W\oo#Sm^^)%mJ\'6jTo#S%:R
%M''[%Lr=E!t>\L&,Ztj&JGlq().T*'c\<:*ul%:*?QOU,p+!=&ePWb%M'']&el)u)&aG6*??+>1H,KE
-3+,J"8`&u!W<)s!!30("oSE;!Wo6'%N5]i((LZO$ZH(T!=/o9$4@7Nq[NQ6r=(+_$OR1H$4@7L#n7LU
',G<t&.&jV%MKWn&e>E]%hTEe&J,H`&.fHQ&-rdW&.T0q.&@aZ!!NQ/!!39*qZ$Tsqu@E3"9el-!WiH(
OUqQp#6>&<"p#2NquH]u!!<'!n,WFgrrW0%rW<*#r;ccsrrW0#qu?j#!sJl2rW!0+!42_-!!<<!!;llr
!!EB.#n$n8!#-(jd6ou]4?#Ag9fu:\5"e(,5s[j:6iKIY77Kd<8P;`Pr(e8.;H-[t=']?DBPtb.D.dd*
E-?SPEGK/s@U`dE?lEH`A7fRnE-$8OH[13beM@[E"TeZ(!XAl2!VZQq!<NB%!!3Q@Zk"/e'b(?P$53CS
H3=ld%Lr@I":bkM$k*%C!t>_M&,ZtW&JGlq'bhH('cS69*ubq8*?QRV,p!p;&J,KP%M]Kc&JGos)&aG6
*??(<1H;KV!!E<'qZ$Tsr;uls!s&H+"T8<0$l$9!'cISe"U,>8%<;XQ$igM;#n$Y>oaE#P$4-tE#n%.K
#n7LT&f5=!&.&jW%MKZp&e>E]%hTEe&J4pPq@F2M%hC!:T+1i$!<iN)!X&T+quH`tqu@B2!W`9'!X\ql
!!*B0!<WK,!=p+I!!!*""9JZ,!r`5i!<*#u!WW?%!r`6!!<*#t!ri;u!!<<-#6b#+#6b+P!!3-&"82`n
!<iN-"pbM<rW"/S.*+8,5<h7n5t""<[Q[>J6UF.-6pj=06q'O67n?3E9MSC^:HMBN<*!%$?"@;TDT$L2
AT2R,G'eFPC1Uj`@:3JM?XR;OA7fOmE-$8OI=-BdcR0G<"p"](!X8f1!Wi)sr;llt+oqr`V[3\>$j[(C
#Qtri";;"L%M'*^%LijU$k!FO$k3[Wq[`rD',;;u'Gi8>'H8-8*ubn8*?QRV,p!m9&.]6\%1WjY&JGlq
)&aG5*$$"?.m0^A#R1>+!!**%rWE*!"9AQ*!sAK%!XKUFrXoeR#Qt52!"X)M$NLA9#mq%J$MY#.$l'-W
#m^eC$4I7J%2''^(Macu#S@RX%MT`q&e>B[%hTEe&J#?]rX\r=&J5Wg'Hf)t"98K)!s&B'"9S]&!!*-%
p])98!WrG@!!!*)"9S]*!X9\G!<<-&"U,#3!s/N)mf<=frW3'%rW<*#quH]sr<!!"qZ$^#"pY;1!!if0
f)PmQ!X&Pu!$;4B!WiH,"pYD:!<EH6/[7&p4$Z/"5rqM;[m!JL6UL`>$U[<M77Ka:84cHJ:Adm):f:7o
='/a=?Y=2lDf'*)DfKrIG&M))@K'[5?O'tI@qB@kE,uA2I=HcgHcmEI%gW(6"9AZ0!s8H&qu?d"!Wi9#
'`eIG";m+"$3^bF#mLA8)0uAt"q;(A&.K*Y$k*LO$k*RS%M'*_r=BhY',;8t'Gh]&)BNl>)\a;5+!i?]
*>]:u%fHhN%M'*a'c.`+)]Kb;*?cXlUB_23!r;ls!rW6#!!!&t!Z:t<!XAfHPRJ35%1NOD!!*XO!"&]0
#7:hHr<i9,!=B/4#TX3Y$OR1L&e#BgC)%<e&J#Bd)&<hp$k3^Z'+tier=05H%hK9a&el#t)E!l^rWEE-
!<<0'!s/?#!rrB(!VZR,"9;6u!rrB-!rr<(!$VCF!!<B'"U"r1!WiDj!<3)r!ri<!!<3)t!ri;u!!<<-
#6b#+#RLO_!!E9'"Te>t#lt&.!WrQ/#6tAH!<<?519`N"5!_J"5WVG<\3NbQ6ppoA$UdEP7Rfm=8P2WL
:&[m+:JXeb<EE7(?=[GWC;"@rDej61GC"CLB4>9J?QWT\?!^lG@V'7jE--ASJ:M`bfFel.#6=f)!X/`0
!Wi,t!WiB'rW!9+"UbJRMZF1k$47+E"98`GHNXue%1`@K!Y5_Lr!Wc=%Ls!\&J>!R(_IDq()7N")\j;2
D&=*2)&s_E.3ooL&.\[K((:W]%M06f(E",1)]Tk<+<rnM!!`Z/q>^Krr<*$!!!3$"(BFL9!<rWJOp_p4
%134<!!*[P!"/c2#6G5?$iUM,$NUS@rWjMN$4@1J%MK9b'P7pf'+GH`'c@c!%LW[U&JGcg&,cqQ%M'*_
&JGlo)&k<-!!*0*"9JT*!s8T%!!33'!VcWs!<r[$r;[30!rr<(!$_IG!!<B'"U"r1!WiE%!:g-h!W)rt
!W)ls!W<'"!Vucu!sJo4rW!3/!6kKF!!3<*p&P'm.foeV"pY51!!E`e[5LB>69[Ru4@iVd5u0d86q'O6
7R]d97n6*@8P2WL:&[lh:JXh';cQn$>$kfKBP4bbB6S$+EHc\MD.[2S?63BW>[:ZC@:X%gE--ASJ:M`_
i!Kr&#6Fl*!X/]/!Vl`q!W2p3!sf)PO9?%%$3gV8!!jHi"V_1O%fR"A%h9$XrX8r>%1WmZ&Gm%H',22s
'Gh]')]3,o'GVr1*$?OU,9.F/q@"#H&/#]o)&aG5*$$"@+uZn1!!35u!!!&u"8r5u!WW9#!!rc2+I3HO
&I\jErW!<<ErZRJ"pYJB$O[=8$N^YB$2t22#n$Y>&.T?`'G=a^$lfTa&Jc3!&Ifok$k<j_&eGN^$k*RS
%M03b'G_H%*A=Vs!!3<-"9JZ.!s/<"!WrK)p](Bs$3t)>!##J9!!!-%+ohZE!WrQ/"9\f.!Wh`irW2lt
rW2lrrW3$#rrN&urW!$%"U5).!!i`.[K$=.!X/Yt!$qXH!sAf5!WW3(#qa"Q7n#d/5!V5%>.[-u6:XI6
7Ros<7n6*@r^eD.91qrQ:/4S];,^Is=^,6E@V]>PC1hL$DK0iEF)5Do?!LW?>lIq9?!h#NBPh^1H@LHt
E".BD%h&^J"9AK)"U"l-nc0@+#m(s8"qhFS"p4r-#TA'o'aP9ZrX]&?rXSo:":bnP%hSUM(D7Aq'bqE!
)]'M+>T":u)''hG-mKZF%K6_K$k!FO%1a'c(E",1)]Tk<+WWqGp](?q!!3$#r;cft!<N<$!!i]-)5@ZY
'+G-D!!j0X!"8i3#71b9$iCG3$iUJV#mgkD#mq(K$kF!_(CF1U%M]Hb&f)<!&I]!S%M9?e&.\XI$OmRW
&JGio(EFAWTDefq":#)4!sA],qu?a"!rDs+!<<*#!XJdr!!3-#!r`0)"TT_H!<<-%rWE?+!WiB'mf<=f
qZ?`tq>gEoq#CKu"9eo,!!ic2K`D/S!<iSr!!NE+"U5#.(B=UC,gJDA7RK@'5s7eD]L5Xb84H'=8,Z!X
8cD=(91qrQ9hnJ\;H-\!>$PHHA8GJBDeWg%E,g#EEb])ir*0/()I-TV@q]^uFF&FeKkum['ak0J"Te],
"p=u.nc0"!$31U;#o+$]#6YP?!!jKk"r.FT%hK<b&.]<L%f[(>&H!+B&eYilrY6(_)AjM(:EC>f*ZlLN
-R'HB$jm@>$P*XV&JQ$!)B0Y9*?6:A;N(JR!!2rs!<E9$"8i/t!WE')"99":&/u;m"oSE+&Te!^!!``8
!"/]5rX8c9rXAf7rX/Q0*=</_$k3a]&K(dF(_@)h&ec#t'bCc[$Om[]&e>HM$O[@Q&.oQi(De20:l,)N
!Wr]4rWE6(!W2ou!s8B#$3:2/!!33+!7UuRqZ$[%!$_@A!!3'$rrW0#r;cEhrW2ltrW2corrMlp!s&K,
!r`0*#RsT7"98E*"7cF2!<NE/!<<*%$QI;O91D<85smh.?G&^*77g!>rCHr[r(?r]#>@fc:/=_b<#8V=
>?tZKA8#S5EG0!&E,g#DEG8ic=]t`-r`L.D?!h&RCiFNCIt35iQE(Z+#R(>4!<WN0!Whil(]t$I#HA4M
&Io-Q"onoKHj1>m%hB3`&J4mO!"Su=rt,2Bq[roC'`JgO(`F2/(-<Z_(D\#5+XJKZ)%m;`#mq%I$4@7P
&JQ$!)B0Y9*?-1@<e'fC!<E9$"8W#t!WE'*!W`M-&f_Pp#6Xr*#S_=[%KQe>#n$Y>!"Af8rs\o8rX/Q0
%13IO$k3a^&eu$;)\<JX'*T-g'G(WX*"!,d'+k`a$OR4K$OmX['GVH%+;e./!!!$&#6t/1!WrK)r;Zj#
!rW*$!<N?(rW!'+!8.>WqZ$[&!@%IB"9AT,!Wr<$n,WCfqZ?`tmf3Lk!!*-'!r`0*#SAKm!rr<)"TAGo
!"8o3"T\T'!>,sb5>4KE70l@J9O>G&<(9LZ8H)3\9))%!9MJ8Y;,^Ir>$PBCARo=kG]IJ3D/XE9F`;#%
=oMP'=oMM4>$PEDB5DR1H[pX"E1.3,&./dL!W`<)"pG&/nc0@+"Ub=-&K22k%LNIA$6=O"(CCZ`rXf,A
q[`Z;rXo&@(D@Gr'GVB#)Aa,3-Qs9C*$6=M-6O-;$N:A1$4dLS&JPut)B0Y9*ZH7C>&s?;"TSQ)!WrPs
!#,Y<W"pBc%grRC!!*dU!"K#7#71b:$O@.M%1WgV$k*OC$N:A2$60E^%1Ws`&J6$.*"WYo',23!'FtQW
$4RO[&J#<K$5X'Z&/#Zm)&OJ9>BBiF"U5,6"9\l2!Wi6""9S]+!!!-%!<WH+rW!'-!7UuRqZ$['![IUC
rW<'"mK!1dqZ?`tli@"drW!60'+5*J!!!0*!r`5n!!rZ."9AK&!tGaZ%RNlV7S--A6rI%'8QA5Qr^m)]
"%u9\:&[ib9+FWi:/Fhf<`iO1?XdPWB)Z["C27X(EHH;?B4"bA='&L+='&L,>[ClPCiOTEJU`;oVLfKj
%L2t6!<`T1!s.rm%g3+D!2UGN%M9<`$3LhQK*2Js$4maI&c!":&cE@@'/(%6'c%T'(`+88*Z5k9+!N!W
+;bXr#RC_D$4.%I%1j0g(`F>5*?H+A+D+UR!!E#s!!3$"oDf!s!2^VTrXTAC"98Z6H2nEU#7(\8$NLS8
%K6h@%1N^R$4?b=rX&f:$OdIT&cNFt)]BS-&eYim(Dmhs$O6tI&/,Wd$jm:I$474R&el-#(EXf7=o\O/
#6P&2"U,#1!W<!"!s/N&!!<9*"TnZ'":,"c!!W6"!XSrRquH`urrM`lq>gEoquZftli7(f!Wi9#!X0&7
rW!'%"9\f.rW2Zl!<WK(!"oDB#fT5,5Y"OA8k2uVb"Gc*9`@Z`9,:2q9hnGX9h\5R92&&U:f:7n=B]!<
@KC"Prb4!"Ci!m)EHH;?AmJJ<<E<1&<`W:)>[ClPCiFNDJUN,pZXk!`&-`+7!<`T1!s.rm'EnaH!2^YT
%2'Hh$jIIRL^P"+&.ndPrXer=r=\u@%ho]m()If*)AsA1*#fh<+p]J@*u>Fn#6tP5#ndRS&/,fr)B0Y:
*uQ1IF#a4#"o/,u!W<)m!#5P9!2^_X%1j-["TSu3If^)\#7(YDrX/`8%K6hB%1N^R$47(GrX/W4)%6uc
&J>cn'bhAt'G;)q(`3qt$O6tI&/,ZX%h&gE#o<pX&/#]p)]'SDG<Z65$jQh8"9er3!s/?#!WrK)rW!$%
"U5).!!EN,li7.b!!3K0,Q%Q@!UKg`!W<)u!UKgd!<<0"!!3<4!WE'%!X&W."8r8o!!*0)rW!W7$jt0K
:d.BG9h\,^9[$44852`MrCd5d:B"&h:B+&f9H?i';,^Ir=Bf'=@Us+cBP2'rChmp.FEDD4>ujs*rDjV6
=B\s:@V9LrFF&IbJ:"q.)[m5\#64`)!sJf/!V-4/":#,2WuW8i&fD>l#8[]'$lB<_&.oNf&J,NP&c<::
',M>t()If*)Aj5-*#fh=+seQY(CpcU#7(56'+#!T&/,cq)B0Y;+;l:NI4,*r"Si&r!<<2s!!!&u!#,G6
WuiGk%hoHW!"ApX!Y,28#71b:$OR:O%1WjW$k*LN$N:A2$6BQ_$k3^Y&el)q&el)q&el-")AWnn#RV"Q
'+tfb$iLDJ%1j-e(`X;5.tKA]":PJ8!WrT0"9S]'!!*0'r;Zp$"9el+!!ET.n,NUh!!<6.![@OBrW2?c
q>pTtr;l6br;llt!XoeLrVup#rWE3&r;lWm!W`B+rW!3)%1pl\;*@HJ&Pl+n>>NI<=\;F_9heAW9hnL`
:]aEg:Amm+:/Fed<EE=-?!q,PB5)$lC2@^%DK9iADJ!3Ur`(%@<``@*>?tWHBP_U-H%:6kID\Pq$4I%;
!!*0)!s/Mo!#,J="oteL+:/Z"'FkBb$],9/$5!jK')W@>'(utF'GVB"(`=5/(E*2k#9P0;-6O-9#lY#D
#6tM@$4RLY'c.c-*$-7A+YJHh"98Mu!;urp!<3)u!#,J7Y9P1r%i#NX!"AsX!=f)7#71_9$3:MCrXAi9
!t5PE$N1;0$9/D$%1a!^',;/n'GV;q'c7l0(_R8a$P!a^&eGN]$OR4K%1j-e(`X;5/rCqb":>84!<WH.
"9JW&!!*-%r;Zp#!sA])!"B;9mf3Lk!s8Q(!=/]LquH`tm/[.doE":Y!s&H)!WE'#'.+7h!!E?*"9S`)
!W2ot!W2p!!<WN(!##n]b?@Y+7o`D]93b?>:g-Lg:/:a`#Z+>p;Gg:f:J^sb%o6#"<)m"&>?tWGA7fLg
BdRS1CM[p0F`hV7?<:**<E3($=B\s:@:X%fDK0oNH$t7b3ZeS6"9&9&!WrN+quQHj'*JRBW@](t&KDMr
#T*u,$lB?a&cE@B&cE@>'DrRD',)&o()If*)&O2.)]Kb=,:=i^(_@Mi"pG/7#6tPB%1a'c(E",2+!V^K
1lW+Qli7(f!Wr<#'*A66/fb9.(CgWL%0:nY%0-S:#lP&1$4He@rsSi6r!E</"Ub_K%hTHQ'E/[X()e/5
)AE\h$P!a^&eGN^$k!^V$OmX['c7o**]0#u'*8FA!!*3$"9AQ)r;Zj"!W2p!!WrK&!"BDAjo>Sc"U>/1
!=&TIquH`tl2^MYli7"drW3'#rVup/!C@7p!!NB*"9S]+q>gNrr;Zm""9n`()%dq0BM(W`<`2ag?;o0I
>>.mi:f("c:f1-i;Zfop:f.-e%o?,$<)m"&>?tTFA7fLhCAquSCi=?:F`1o!=8l/=<E<1(>?tWHASGsu
E-HbTI"KWu*sDlN!<<*#!r;uk!#PbD#bj?r%MBct%ga'^M@CF2&J5Wh'+toV')WF='`A[H'GVG`(_%?#
)B'P7+=&<_+rLptr<3i=#7(YF%hTKl)&aJ;,TJ$fPmRig!;c`t!<WH&!#YqEUH9;$%MoTZ!"AsX!=]#5
"pbJ@#m^hEr<rT3q$I$-"UkhN&.oQS'E/[W(E4D;)\rtn$kEp`&ePWa%K6bO%M06e(`X832OP3n!X8Z*
!<N?+!s/N%!!*-%qu?g"!W`93!!!N7fDl-W#7:Y:!!N?EqZ$TsklCGYm/R.f!r`9%!WE'##\+,<!<*'#
!Vl]r!Wi6"!W`E-rW!6+%Mm3.7n-KV;$p/q?rYNO>u"<q;>jDm;uT_u;c6Ljr_O)%;H$Oq='8a5?XdPX
BPIE\#]+F"F`hV8?<@))(KOU@>[LoMAnc'tDKUAOIs'9r('jsA!W<!"!<E9#"8)X.":#"+64j_K)&*Vh
)%DH4)%.&h'E8aE')`LA'EAmG'`Ja['GVB"(`4,/)B0V9+=&?`+rLpt"o\W<"U55>$kEp`()Rr/+=/'X
/Y<IQm/R4h!WrQ'!##D6VaM.-)%m>^!"AsX!"8i2"UFr2!"&Q1!"/H,0+&$o$k<dZ&J>`j'GM9!*$?CF
(D.)c%hTHg&J,H_%1EXT&.oQl*>ThLU)"4D!WE'!!r`9'!W`?$!<3)s!"o;4!!**-!7:cM!XK,;!WWB(
+6<M$!;QZ^!!**&rWEH,!!!$"M#[SU!<*$"!Vl]r!s8E$3roEe!!!$)$4G%,7nR/c;,U5!<mjrR:K14j
;cH[o<)lq!<E3!s;Gp@h;H$Op<`iL/?!h#NAnYppD#S5rDfTuCDe<<W<)Z^p<`iO2?t*\[BkqL#F*r.]
CYLQP$ig8/!W<!!!<`9'q#D33!!!')"9>An%h^6*'+bNi%Z:f7$PF'M'E8^F'DiLA(&epH',)&p()If)
)&aG5*$$1K-n$8W&-s$T"9S`/"pbPE%M9?h(`=56-6OleV[r\*rrM]k!s&H*"TAB?!<<+u:(Rs\%LNC?
%0:nX$igG7#6tM>#7(SAr<i3(*srAa%1Wm\&ebom'c%Z-+X8'H'+PK`&ebok&J,H_%1NaV&.oQl*>TnF
WYbsLr;Zs$!WrN+r;cp!!Vud/!<<*$!sAV6!!<9-#mC>0"99P$!;lla!!30&"9&H-!<<**!3#u!#lXi'
!VcWr!s/N%!#PeA!<<62#mdr#;c$Uq;GpA%=4:/V:fUKl<<-)!<u"b9<)cdp;H$Op<``C+>?tTE@qKCh
r+lXWEccD@AmJG:r_jY6=Bf*?@qKChCMIU)HZOIUg`m78!!!'$r;Zm"!sJT,q#D<6!!!*,"9=Wf(`+83
'G(Wk%uUo8$ka0d'GUKZr=o&Br=g"\',2/s(Dn#.)]Kb:*[)gX-mBN?#R120)?^6M$4ICU&eu3")B^CL
.5S",!!*'"!<N9&oDeso!X&Z*!##J8!0US*'cR_m"TT#5IK0cV"U4c.rs8*#(((EX%1a!^',2,q(E+>=
,Tn!>%hB3arY#nW&J,H_%1a!]&f2Q&+"s`)$4Qk5"9AQ+!s8?#pAb=!"98G'$31,."pY83!!E9D`;fr?
!X/K,#6Fo+#lqF7$iBu)!VcWr!s/N%!##G<!<<<7#RHom?<:!+<)ZY)=k+-c?rC'+<`W:&<``C*=]ea,
<`T)t2cWjY='/X1?!h#MAnYpqD/F**DfKi>D.QsP;c6Ll<ENL5@Us+cC27R!EdDYEK\R:Q#QOi,!rW*"
!<`<)!!`9"(]aX;!!<N1!deN&*#9P0&.9EfN"-a7&eb0XrY,8Fr"]/GrtYDF-l!I4(`=52*$$%@+XJKa
+W(^q"9S],"9o,>$k<g]'GhQ'+=J9W7'6@e!s&K*!VHF3!<E6)"T\T("onXLC*OW/'ak0F%KV"Y$igG7
r<EE/#7(V4$2t;3$N(2J$47.L%1Wp]',2/s(E4G@,Tn$@&.fEd'GUN[&.oHa%M'*_&f2Q$)F(D*%1<%6
!!3$"qZ6Bj%KZ_63"l]#!<iQ*!!E9EhuMm>!W`?*rWWT0!WWK+\cE0/!!36(!W<!8!sSc+#8%+BOfVVi
;HZst;Is%_=CP32=8Z2#=oMS-=]ea+<rH#3<``C+>$G9>@:WtaCMdp)Chmp-"`eTu@Tl_0;&N83=Bo6C
AS5^mD/F03G]7h[i"?G&!!!-(r;Zj!"8rE"!#P_<!!!'+!s<R_(a0\8'G(Wl&<.2=$kj9P'ESp^'`AdC
(B,'H'GhK"(Dn#/*#ot>*[)dU-Qj38#6Y,1!sB/>#R_(O&/#Zm(`FJB+"Kmgqu?g#!s/Mr!$2.B!sJl0
!!*9(!,lru*tf:r"TT#6IfTrX"U,,:#lY&/#lY/.$N:G0$5a-Y$k3[X&J>`k'c.f2+s\9L'G(ff',;8]
'F,6_&.]<a',1]g)\X;[ZiCI>r;Zfur;uiso)Jq;*!H<B!r`0$"99Ra!"K#2!sA`/!W`<%!X,Y1"o\Mp
!!*0'r;[c;"9nl,#8%%>LUBlc<`rC$;Is%a=^tH8=BSf*=pS>:>[(B8=]ec)<]F/^=BJ^0>[:`HA7oUl
D/F*)C2@d+DJ3EZ;,9ta;,gY&?t3b\Bl%^-F*)SFH\gSn#m1/-"U"l)!!<9*"U+l0q>_H9!WW3$#6G$C
GRc#;)\`hk*"e2B)@[>n'GM;]'`SpE(B53N(B5-J'F#9e(Dn#.)uL]s+<r0Y*Yo1g!s/N+"U58@%1Wp^
'G_Q+*[2a_9XO]t!s8Z.!VHEr!<N?,"p#P@!!N?&Apb.7'GLoY!"K*]!Y#,6"pbJ@rWrN1rX/T3rXAW2
((:T\%M'*_&ebro()e5;,9Id:%hB9erY?+]'b_2l&.oQj(Ddr)-UtHC"pFo*rW*!#q#U?mrrMus!>6aX
!<)s""TT_D!<*#E!!E<(!s8W%!!3Fo$N'o(!VcWq!Wi6")$'jF!WWH:!<RGV:gmC.<E)k->M34l<a8f.
>5_Y*>l@qn>[(B7=BJX+=BJ^/>$G6<?t3b\C2@a(Chma"CM[cs>Z=Hl9hnPb=Bo6DAS5apEHQMKFE2bo
eJSGk!!!3,!W;uu!rW9!!!30&"9&99"T\j3I1IS?)\`hl*"e5C)\!Go'GVA^'EAmH('#-I(]P9N(&emO
'c%T&)B0[o*??4G,9n0B$NpM4!sAc4#n%1P&/#Zm)''_>+uNT+qu?g%"9S\t!$2.B!sSu2!!!*$!*4X_
+qk\!"TT#7JHHA_#6tPA$N:A3$N:G3%/gY7%/gSL%1WjY&.oNg'GVB$*?ZLG(_R;h&et9\'c%Js&J5Wi
(E+,,(b/Lc"98N(!!*/u!W;uu!W2p!!<N?"!!3ET!W)iu"ookF!<*#Z!:0[f!<N?)qZ$a%"+1@Vnc/[l
!W<!;!<i]0!!a&8"(T/H?rgN5<E!I5fj&/l?!CQ=rET\8?XI,F?!LT;r)jP6>$G39?=@>TBPM@#D/<tc
B`i!U=A^,48kVlT;cd43@Us+dDK9uLGB.bOUqn)P!WW3*"p4`'"9AT,"9eW&!s&E("9&97"9Am%K+]@D
)\`hl*>+>E*"EYr'`JgL'GVB!pD<fE$PaBj'GVE$)&aG6*W7#k+!DdM)A3>Y!<N?,"pbPE%1WdX&ebut
*?,tD2Jnidr;Zp&"Tneu!$2.B":#26!!!'#!(2JT+;,Cs"oo,8JHQJb#m^kG$iUJ5$iUS5%JpY4%2B?_
%hB3_&J>cm()\)5*ubt-%1a'dr>5t['b_2l&el3'(`"#?AdF_/!!*'"!<N?$!W2rt!W<!"!<WH$!!30S
"8`'""ookG!!E<(!W`>J!!30&"8i-)!<<H/<Wr[-!W)ln!!!&t!#bnB#Qau1%fc`0a&ZSK>ut'*Am*hn
BNebK?2\(0?i=@8?X@#C>Pq\(>7"P??X[GVB5)*rrbNosC1q0f>?"<f84cKN;cd11@Us(bD/slLG]S%O
Z()^8!!!$*"p4`'!<E9$"8i0!!WN9$!##G8%QB4X+Vbq1&.BTkO:`HB'GL?Y!#GDIrtt_OrYGJJ.M`g;
)B'P7*$-1E+X%sM*>T.j!<E6("pYD@$k3^Y&eYin)B'SD1OO?Kr;Zp&"9S\t!!WH+":#26!#5J7!!"a4
'd"&'$jH\B!eLRf!t#ACrX8i9$k3+Er=8T5rsni8+qYM*)&jP9*#KA#$k<mc)&aA1(`!f!&eYlq)]0A5
.!9P6r;cfurW2lrrrN&u!W`B+q>^LYqu@$'!!WEL!!*'"!WE-#!R:]F!W)j#!<j,[!<VTf)?L*K!WWE8
!!PU3='o!7=]\R7>2!:t>[UlE!+5_5$=R@P@UW\Q?X@#CrEK8+1L4<o@Us(`BP;*qD/O6,An#"G:J!uD
7nQNS<a/p?A7fOlEHceUFEhi>E#&f]!!<K2"8r3"!W<)t!!<6&!sJT')Zg!M-]\ub'H7\s%3?(A&KMAs
'GV>u'bqK"(]>3K)#b?N('G?e()Rqf)C-7C+X86W+<;:3$O$M1!X&]5#mq(M%hK?c&/#]p*@ik%9E>4o
!!<?,!Whro*!$-F#RLP4!!*'"+H[H]&JbcZ!"]3_"VLtH$Om"D":P_K%M&FJpCR66)\3Gh%1Nma)''_;
)]0;%%1<XY(E+52)&O/)'E/UE(&f'S,:A(6!!N9$rW<'"qZ$Wu!W<!"!<WK&!!E<&9E54n!!3?)-2dfI
!<WE*!<M6]quH]sl2UfAkl;e,"pb81"V1S:1=0-1<a]*5<+BCg>&IYU?XR8M@:E^E@gHOP?sd5G?!LY5
>m=VA?t*YYB)ZENC2Im.CLg^O:eF/C*CE7e9i4no?=@;SB5;F.H?sgYG/uf^%0?S7#mLM0!;urr!!<6&
!sJT')Zg!N)NtpY',qVt$l^%@%3Q5t'GV>u()7T$(\\dG(]>*N(Dn%h)Aj>1*[2pZ,p+$>%L<+9!!3</
#mq%K%1WpX&J#<\&JuZ?2jbQd"o\K("9S]+o`,s4!sJr:!WW3$!!![t(EF&&%0lkB$@W!k#7M"Mr!r]:
rXf#?rY#&>rX^@c%1<RU(*"G=*#KD&%L`[S&f2K,)]BS1'bh;n&/,iu*[<7u('+C=rW)p!rW2lr!<N<#
!!30'"T/6&!Wu@("T/6%!XBbKrW!*'"9\f.!T3tU!V$-q!sS`*"UI?n#58,j!#ktD#m()0%KHY[dog$Z
@9cu8?u4"fE+*6b@:K4G$=m[YARo:[@:3GLqHa;3?X[GTram]mASH"#EGArb:eF/B5<qS+92JSj?!h#M
Anc(%G^4XUHHd0?%0lq=#mUP5r;ccsqu?g"!<WK(!#5P8%hG!C*toS-&I]L"IgRA5'bhAtr>#ALobdWD
!u;Xg)#bE^)&O53,:G#g*Z#=n"o\KB!X/i9$4@7O%M03]$4@@],UYdK!!EK.!!*3)!Whro"T\]/#RLS1
!!!68Ql$eR((CNL$5@O](^^`^%f?k;&H3:@')E:@')`Cs&.T*U$4n!p,9Rp@&Io3V$4RUa)]Te8)&F#%
'+bZd'cSA@24":C"9JQ'!s8T+!<N&t!<N<#!!<6("TeQ%"p509$3U>1r;Zj-(((?J!!*0)"9S]+!T=%V
!V$-k"ptP5!!K8$!s/Mq!!!&s!#ktD#Qau.$3C>If32K^A7/\G@!/S[DId<g@UoCJ!+l+@"_D4S@UW[D
?i+4d@Uit]An>L`BPh^.BjO\.6U*^r4[;D+9i4qq?=78SBP_X1G'7V>`tT3n"9A]6#Qt2,!;urr!<3*"
"8r33":P=&)BKM1()%2o.U`u4'c6iar>#ALpDEiGr"f>NrYc1_(Dn/;.4cec'++mErW!r?"UGDA$k3[X
&ebfb$kF1#,rhFq"9JT(!X/].!VHEr!<WK2#m0u(&"aaZ%MfN\!souJ#o3s]&,["<&cWLD'E/^F(&emK
'+trV&If9]$jm@S)'L=N)\WYfrWrZ9&Jc8`)@[Q$(D[`!&JGp!,9JV)qZ$d&"9S]+!W)it!Wi6"%flb9
!<<*$!!`XD"UP/4!WE'-$P*IB!!*0)"9S]+!T3tV!V$.!"9ni+$imR5"onZ(!!2lqrW2lr*ruNM!<<-)
$3C[k>?t<B@piVOHAlWTAnP[cA7]=aB)Q?FAn>L_@eX:J@q91aAn>L_B5DO+Am%em4?>G^3^#_s8Jt9%
=Bo3AA7oXpEH#i.E3^Mt"98E*$OHt<r;ccsqZ$Zu!X&B$'FY6IV&^Qg)]'2$(+qin*>fV/'c$Z_rtkJJ
!#PSNr>,JO)?(N](`*u/,Ut>k)@crK!"K&6#RLkI%1a$a'G:oe&I''r,s@1i"TAB(!X8f1!qZHq!X&`6
!r`02!<<+r*#]8$%grXM,;g,J&Gm(=')rXF'`SpI('bWk()7Ms&eY$Q'+PHZ$kjR)-mKWB#mU\@#n.@Z
(]"sT(DRW!(`OYB22(i,"U,&4!W`?!!!*-%qu@c?"9AK&"TSl0IK0cW#Qau+!<rl5!!!$%"9\f.!<M*Y
rW2Wk&ci(8!!**#!!`La":5&.!<N?)q>gNr!!2rs*ruKK!<<*'#ltFg>@(BFAn,CcF*;A8BkV*iAS,Oe
BDlKKB4b^dA7K(XqI;9kAS,ReARf4^CMn$"<(/f)1c70N3^#bu92S\k>?tTE@q]^lBksJo*tJ_]!!N`9
"9SN%r;l`p!WiE''`\47$NpI.+!(t5(_mi+-Rg,Y)]BOl(&f!A(]>3M(Ch9")B'J1(De):.4c\[$MsfD
!X&`7$OdLU&/#We$k<pc,;=7H#QtA6!!3?.!Whon"9J]2#Qaf&"K!1W$5EjX$k3dg*u,M('E&RC'E/[K
'c%Q$(]>0U(D[`"&ePZcrX]nW%1E[[*@3-Z)%QoS"U>>B%M9Bj(Dmu*rY?.\&eu9%+tRV5!<<3%!!*9-
!s/N"!<3)t!##G;!<<0,!"&^Z!=T#;"TSN(!X&E%!<E6("9S`-rW1pW!!2Zk"Tno/!!3E)!!t+r#R(A4
!!*3)qZ-NpqZ$X!"o\K>"U>#9fih`cCM7<qDej!$Chm`tAnG[gBP@?Y!,)IIB4b`QAH-6?A27_.B4kgf
@q0(`CM@'L5;OuI1,LjI3^#f"9Mnbi=^,-:@qo@[F4*`)%1rgG"UYJ:!WE)s!Vucs!<W6#('=jC!2q"^
&KDW')^$.=*ZuLB(`!i$rYG,BrYYVN!>l^R)@78u(`aeJ.3B3-qu@c=!X&`6$4ICS%hTEa$kO3h,!MtY
$j."E!!3?-!Whon"9JZ0#6F]%%]16a$5=![&f25n'G_Gur=f/E#8Ish()If))?(NY)&O/)'G:uV%g<LV
&.]6]'G_]8-m9B9"9Sf4#n%1Q&JGin()Hla'G:un*>]n\U*g*E$3C2."pG)1!<N&t!!2rs&HW(9!!<N-
#Qf\_$N^bA!!*0!!!NB)!s8T+rW1dSpAbj-"9nl,":P83#M]:\!"/i.!!NK%!;cfp!!*0)rW!0+#65(_
=C,V=BEi9kBjtajCA_cFC&D]LBk_6nAnM$Rs(;1?s(;7C(M78jA7AkD7QN4U0/57>2)dQZ5Xe7?<>8\H
@qBIr?rh3h0-Uc6"98N1#6Y,,!W<)q!!!'!!##GA!!&u?*ZQ"4()nA7'cS58)Ar;drYPDHrYGPOr>,SR
)&aG5rYu+`+<_gC%0QP/!s&H+"o\`:#RLnO()n/0+!hjG5c5>(&H`FE!!*6+!W`>p!!<6("U=f'%At-^
'b:`_',V>j&JZ&Z'`JjH(+0n8(`=52)]Th:)&F&%&J#?]%hK<c',20!*?ZLE'+4sI#71bH%1`=I&.fKj
)]p+B,q9uV4eWAn!!iK'"9o#3!Wi?&qZ$Tsqu@?1!sJ]*!XA]2!.k1Y!=K&2!!2ut"T\Z,!s/Q'!SIJQ
!W2p-!X/f1!!3B*!s[0\!!!6&!!*3)qZ$TsrW3*%!W2ou!X/K&%g<+:#Lup`E+WctD/O&tAc??CC&D`D
CB\HfBkV-lrFQ%Bq.;6mBkh?n?W^/q4uFrE/hf(;1c73O3]oYu;Hm[EBQ/#u96I3S+USJT!!3E2"9\H$
q#CHs!!!`6":5&.V]['.'GM9#*>oS/*#fb4(]G0M(\AL?(Ch9!)&aG7+!DgN*#TG##Q4WD!<WK/#6tG9
!sAoB)'C(H.4u\Y98Nle":,#.!!NN)!WW8p!!<6'"U=f'"f31U*=</\%2'Hi$kEsa',:?[#T"9o(`=52
)]\ht)B9Y4'b_/i%1NdX&JQ$"*#on9(D@;d#7(VDrXBSP%1ERM$4dmn,UOlk1EmW,KE2J]!r`0("U+u1
!WiE#!!!&t!"T)5"T\T'!rrN*GQ8$M#Qjc$!<N?)!s/Q&!S[VR!W<!-!<NE/!rr<%!!rX&!!N3"!<WE$
!!!&t!WW9!!!**&rW!B5!!!)GAR]CiCMI[&C&VWJAS5^mCi!m&r+uCK");OaB_c<=Ae&KiD/<]b:.%-%
0J+k/0`<dG1c70M3^6#*:JOV^>!G9W>o41Z"onW)#6k>1"8`/n!"o>=!WrFr/0Q)P'bhH&(`!o+)?(KO
(\8F@(Cq<!(`=52+!N$Y+W1ju"9JH$*WlTO#7(P=!s&E)#7M+P$kXHb'9#6^#6G)2!!!-(rW3'#p&G0q
!X&]'!"Y\N)AWbi$kX3e%Ls!]',CE]*#KM1)&aG6*??1C*ZZ.9'b_,g%1NdX&f)E/+s%jE'+PBX$47.L
%M''[%1<II"pG8?&/5`h(*EtuMEV"@qu?p)"U"o0!Whup!s/W1!W<!&!<?[2"98W"!!E?*!s/Q&!Sd\Q
!WE'-!<WK0!WW3$!X&K'"oA9"!W)is!rW3%!Wi3!(]a[<!!*H-!<C,[An,guCM[g%An,:\B57B^!,VRM
"DhmiCMN`\rFcXQB4bahCMdlr;aiZ$0`EX)0/<>Z"Z%tm2`Ni14#J`M59iSO'G^cR"9AK("pOu/q?-Ek
%0?n;#6:/P,o7O:',;A_(],'K(\ALB(C_2u)&X>2*$?LT.3K?3qZ$[!"UG#4!s]#4!Vl^"#QPjX!!`K,
!<iQ*!W3$#!Whup!W`E,rVup"rW!Iq2'!,;$k!RZ&eGN^%h]WS(bQ[D)B0Y9*?H7D*uu7:'bV&f$k3[X
',Vc8-6F!4"pG5<$k3^Y&.]6Z$4$h="8r<#!!Nc2*P;@RqZ$d&"U"r1!rrDs!!E<)"U5#*!!NC$!rr<&
pAb0or;uoug]73P&-)\2!sJl0!!!**$*F7.#R0r&!<E9#!s&H(rW!$#!!*3$!#Q"B!"?Y]CM%U*Ci+'*
BOt[bBPVL(DJj=gDZ=SQD#J/IC(tAqB4kmlBkL[G5W(5J/M&J+0JP<]0GlN"1Gh$M3B8oM4?aU6TF2&+
!<`H(!sJl,"T8H&!qlTs!=Af1!!e]G.2a*@',:B]rttYOrttbPqA/uFrYQ(^)&aG5*$$+F,U46>"oA9$
!X/i.#Qk;8!s/5u"9])4?\SFY!sJf.!WE-&!s8T*p&G-p!sJT'!!<-"$BQtc%hK*V%MKHe"V;1V',;>^
)#bBU)B'P7*;pm%)]9G+&eGQ`%hK?g)''kF*#&b`":#8B%M'*^%h/mQ#6k>0!s\l-!"'8;@"e@V!<E<%
"9JZ-!VQKq!X/c/qZ$ap!!3-$pAb0orW<'"!!1gS$NU80!W`<%!!*-'"8i-&#"&@o"TnDu!<E9#!s&H(
qu?a!"TAB7#64`@\o)G%F)Z#8Df'6%AnPjqrGV^RqeuFN!,_^Pr+lgXCM@HpAn,1J8Nnsb0)dF</h\n4
0.nk21,CdJ4?Yhf2+Tt]Zr.M8!!NK-!WrT0r<3-&r;uWl$O6Y5"H5/g*#fV+(&f!M(`E5iru(hRrtkYM
rYPPNr>>eX)B0Y9*?G)"!uhp^"8`'!!X8K,!X/Z,q>^[3%fhhV!r`0,"U+r/!<E6'!s/Ms!!30("TAB$
!r`0*M(^+e&.8jU'E&OH',22u(]G9M)?(QP)\j5,().An&.fEe'c.c.*?>t/$3^S=%LNUS%M''[$jm7F
"pG/7rW`W2";qsYQ95!E!W`9%quZs$!VQKq!X&Z-r;[$&!)!:p!!2fo!!3'#rW1^Q"9AQ*!s8E$rrN&u
"p=p@":>,1p&P*nr;ls"qZ$X!"o\K8"TSWAZ$pS+F`MG@EGoZ.BPM@$rc%aQpi-4Ns).gQ&8Z,rAmntH
:.79%0J>%1/M@#U%PB=b0/>@C3^#_o4ZPo#"&-'>')hn*"TJT&!r2fr!WE'0"TS].JjLn))\s)%(Dmu-
q\o_X)AsA/(DcudrttbRrYkbT!ur:$*r[5c*?#_-%0lq2!!33)#6"i="pG)1!<<*#!<<*2)CLmV#Q=]*
"U+u0!WW6%rW3'#pAb9r!X&Z*!!!'!!"49>+V>:p$P!d_',:E\rY>JMrYYAI(`4&)'b_2m&J5Zk(`F;1
)&Eqr$3g_A$P!%E!t>VE#lOu9#RUqJ$4.Rn/=HbHrW)ourW<'$!<N<#!;ZZt!<WH*qu?m+3=,Zc!quZt
!<E6&!S@AT!<N?*!rDs!!<WN)!!-L:nc8Xi!WiE(qu?g""9ni@!!!-%#8F/!CM\09EcQ5@Df'<,DK#Mo
qf)FPs)S*YrbrEeDJj<,BOY4G9h%?-1bg[;r@S+(0)dF90/>CF4?l5(6pNOa^K_HS!!!$%p]LR!quZ]p
rrN*!#Qk&5!-qKg)B/qt'GVH%)&jP9r>YqZ)]BS2rYGbU(`=20)]S_q!$2%[#p194*ubt-$jQn2!!33)
"oSW8"U"o/!<E9,"pY/8SO3S[!!`Q."9S]*!!3'#!!2fo!s&H+"TAB$!WE'0F\Wqh&If-Y&el&s(`4&)
!u2Od(\nmR(Ddi&'bqDr'E/UT',;?&)]BM,&Io3U#RLhHrXB8G%1ERM#R:VA$4@7RrY#DB&Yhf!r;Zfu
rW3'#quQj!p&GR'!WrH'!!*'"'djas!!;ior;l`phZ*c[!WrN*qZ$j&#Rgt?[K$R&!;urq!!30)#Q=]0
"TSW;Vj_:DF*7J("`n[&Df9UlEV4AMEW0tdE,96!>Z46]4?,/PqChq'0)dFE0/>FG4?uJ55rh#/^`*@_
!rr<%!WrQ0"pG/5"9S],rW2iq!<E9$!##D6#lo'N+XIp>'GVE$)B9e>*?G,!%3$6))&O/+(`4,/)]Tjr
*<I9)+oWYh+WhU:%L<(<!W)j8!<NB-"pP;;"p>#0!<EE6!s&c`U':T%!W`?$!r`6"!ri;q!!<6'"9e](
!!E3#'6$qh*"EDd%M9?i)&jJ2'bh>s(B,-V)&X8-()7Ms')iIQ&.oNg'c%W()]KV.&.ApE#ltDBr=0MN
$jm:H#RLhG$k=$m&e5[;W!WM-qu?]tqZ6`uoDemm!rDs$'-%Sa!!;iorW2WkrW2-]!s&H)!W2p'!X8l5
!sm6[&a',q!X/i.!"T>8!"Pj"BS(8IF`qqNFE@;!rH&!\s)\-Zqf)UVrcAHcCLpgO8j>6j0`E^+0JWP^
(,7Kr/hJY/1H%9V5Y4g<68buD$jI4Ir;[-*"U>8:"U"r1!rW/r!<3-"!!iT*#QSdN+"e9,'aPQl)BBnA
*Zc@$*!7,u)&`Dj"W80r)]Tms*Xs59,UF]\+W_I5$O-\6qZ$a"!sAc3rWa#>"U"o.!!Wo7$j_bJ!!!H6
!W;uu!W3!!!VQKq!<N?+rVup%rW![L>Sndr%1NdY',MT/*#TJ(',22u)#bBW(D[\t&J,KO%Km:T'GhYd
)?^om&I]!F#TX3Y$k3^X%LrpV$OR1H$4I@Q%i6<$)AJGu!!!H4qu?]urW<3'!Wi/uq#CBqr;[''!tH%P
!!!&n!<3)l!;cfd!<*#q!;urt!!r]3!t>?G#6b)1kPt_e"pb50#m(G6!!f7#DLH^,GQ)akF`__HEcZ;D
FSp7_FE;L"EW:(YF")*GB44q<5rC2B.4Ql$0JbRC1G^a>0.nk32*4#b3^#l*951.<%g<:Ar;[0+"pkP?
"p>#0!<Mrq!W`?(qu?s-!,6*l-l<^+'bqK$)BL"D+!1D%!ur:")Z1H[)B0Y:*ZlLI+X/-0,6oD9*uGRs
"9JB""p"c-"9eu7r<N]9#QXo*!>$#0Jc5WM$O-G.!!<-%!WiE(p&G<u!WrQ*!!3E)!"`dS*?c"*%1Wm^
(`ab@)&3_d&ebur)#bC4(DRSp%LidQ$OdLV&el)u)&aD2'b:TS"U55>$OmRW&.]6\$k!CL$P!a^%LW[Z
+XKa=#6b)7"T8<)!<WH-!s/Mj!!NK4%h]!HkQ(S^p]:$fquQTn%flb9"p"](!s/]-?5*G@!U'Lo!X8o2
!!EZ0!!8UtFEVtUqfiBjG'.nJF*)MHr,r3cFE;JCrc.jV.<'-;@9QMs3@uL#,UY&n0Jk[G2)@!B0J>(8
3'BPg1c76i3TNO:$3LG0!"&`/#71\A"p>#0!VZQq!<NB$!##V<@<*h@*>fP-(E"27+sA'N*Zk;$!?<'V
)@.9%*$$(C+X/-0,7,P<+Wh[>%gW7<qZ.*,!WrQ."pYD?$471Lr;Zp8#J28\!!*<*r;[''!sA`/!W`>q
!!`N+!sAT(!t"r,4C;tN)ANen%M0<l+!MdF'G(fg'c.]()&O/(&e>EZ$4.%J%hTHi()If*)&Eqq#Qt87
#R_(O&.oHa%LiCHrX08H&/5li"pYMa(<A*.!s/].r;[$&!sJf0!WhZg"pPMI%gWCBr;ciuli?\Zq#L9m
q#CU#"UGD9!!!6)"U(P"$j-On!#YhA#6=f,$31&3L:;8JG^4R\H[9s^GBS+OrH/!\q0"E6F)c,8DfTr?
B3Iql2(g7$,:"Tb/MK">2)?s@0JP=<1c@9P1GD*W2NY0a!"/o.!"8i-!<`T4#R1G7!WiDs!!30&"9&9X
!<<9';gBu@*>o\3)]^"D,9nBU+<VaJ*ZZ7@)]Kb:*??1C+!)ID*?caZ/1)DQ%13=D"9\W)q#M-3#7(YC
#R:J4!!`Q,A;pWj!<<3!!!`N,"9S]+!<Dfn#6=i-"9AK*$2soH;0=3)'+YTb',DK-+<;:4&.fEe'c%Q$
(D[`!&ePWbr=0\V'cS8@*uGRt#m^b@#RUqK%hK<c&.T*V$iUP7%K6hF#mM1Z&osBJ!!NH+r;[$&!WrQ.
!Whonqu?`u!r`9/"U,nM"98E&!<N;f!;Z`m!<3)i!!NB)"9\f/rW!*('e04g!p0Ih!<`T-!!3E+!"TKT
\T2n:G^=acI!U$\r,qjX"*Sp7HN&7EH?O:EBkqX-E+)O)/1)Yg,palc.4d//2)I'A/MJt<2Dm9E/hJ_E
3_\3[(^(*Fqu@')!sJo6"Tnf-!<Mlo!<NB&!"K)2!WYQ=0I[t\)]g+F+qGqF,pX`\+sA*P+!)ID*Zk2#
$6:*))B^C[0I@VDrW!''"pG,2quQ`r"p"o7$4$e9rW!*6#U$Je!r)a!!<N?)!<Mcl"p"f/!<<6.rW!Zu
I4--I%M09i)&jS:)AWqr%hTEf'EAjA'fcp?&J>p'-S$AV$31&/#Rh1Q%hB6b',(re$3pkG%1N^Q#R1J=
*Yp?B)[QKI!<<*#!!!$$!WrK)p](9pq>^X!!WiQ2r;[*j!X/W,!<N?)l2^GVrW2Wk"9JZ-!Wi9##Qt,.
%FkR`!!E3#rrMBb*<QHG!!*9*#7aGLC3O]BH[^KoHZsRRF`qqNF`_^'EY<M>H[^ElI!^0aG&hD0>>dsR
1&rd&-N5A6-n6c$1GgmA/LrJ13'&oM/1NtV,X0mP+US>P!<`K&!!NE,"U"o/rW2Zl!<NB&!!!0$!!k*E
/h@t^+!N$--3bbB,U4KV+T<H#+<_pO*ZZ4A+X89X+<;:3$NpG0!X/f5"9\W(rrN#t%0QtG#6=f)'c[2h
[42L]!!3<,!rW*#!<N;l!!WH*"9AK*#lXf<.?u/#$k3da)]Th:)Aa,$&.]<a&cNCF',23!r#$%b*[)^M
*?#\*$jQn>#n7IZrXfPO',2,l$j["A$4[RS#mLM7*@(_0^G6B"!!E<,"Tnf)!!30&!VZTo!W2p+!<WB)
#7:V7"TY4u%/p5/!X&T+h>mNUoDf7#"pY//!!EB3!!(IH!!`N1"T\W*!WhTe!<NE'!&4T\%1Or<Ap/-;
I"6ctHZsOPFEVkOF`_\GEcQ5EH@:<oIscTjI=6?R<C&>i.Ochrr[8p=.4Qi"0/>=</hAJ)1cdcX/Lr;,
2B/31+q>7g!!!B4"9&9$!<N?*!s/Mo!"]26!!!$'!<<*8X=l4I+!W-3.0(do-Pe$T,U4KV+<VgO,:"ER
)]BhG/1r4b$N:#2!X&Z2#6tG:"8r8t!"K&9$jH\3!=TP?ITm3\"o\K'$O?k4!!!&o!;QU3!X&Q)!sSi/
!#)1S*srGj)''_:)&<o!&H*.=&-WXY'GhZ-rZ)Lj,:P6!,o6mg!!3?4%1j0N'GqJt'c%Mr$jQn=#n7FQ
!s8`?(BB.t&HN4;!!<W:"9J#mrrW)u!WiH*#lt5<#m:Y:i!'_k!!<9*!s.6YrW2Wk!WrZ6rW!K<!"BQ&
&/5*S$47"@!s8T*nc/XjqZ$Wt"9&9+!X9)E*klW8Esd5DKReJrG&qbJGQ)gmGB\:WH$XjeJGt-WJ:;fe
De<$<1*dtb+XA?[-RgMr/MAe41,:R</hSk93BB#N2*s):CRcIe%M&[B!t#88!WE'$!<N<'nGj1'!s&B&
!s/K($_9I8+sSHa-78U9"XPE>,9e?0,Q8qp,9e<W,pt#['+"R;$j$P8"pP;:"U"o/!Wi/u%KQ\;"9AoO
&HG[`%1WFDrW!!*"p4&i"T\].!WW<$":kP@Q80Ki%i--()&<nu&.e^K#7_4T&ebrp)&4)3+X89\.4Qep
*>/PV!!3?4%M06erY5GL(]G6i'bC`Y#RLhG#6YMY'ED*h&.esM!!!'-#Qt1u!!39*!W<!,!<N9&"ptJ5
%LLDc%/p8+!qu]k!VQNg!!!&l!!30&!Vl]t3sl,nrX&c5"9S]+nGiOiqZ$Wt!r`0@!<iiA'q0hsGCG:#
IsZE_FEMbOH$XgaI"$TsJqAXRJe<Q^FD+lQ5Vj`-)B'S:+<r3^"Y;8\1G^fc0c;`&1Gq*N3Ar`B4>:Ej
0E;@a%LE7A#6b21rW)ounGj:)!sAZ*!!*-'"p]QW0de>".3fuY,5ibc+p/u3+sZt1$RR5L-mg,Y)&!Je
#6"c#"Tnl0!Wi9#rW!Q3!sAi/)A>rX,QIfG#R(51"9Rff:]UY%!s&B&!sJr8G=`kf&fVf.'bLrc$k!CL
$OdIS&/,cp)&aJ9,:G)q.jcAV&e"sF!X&`8%1a$b'c%Q$)&aG4(_mVl$OI(D#71DL'2T+I,6.]F#mCA5
"pG&/nGiXp"9S]%!!<6*#6Ff(#!rb!!<E6&rW)ltrW)s!qZ?cuiW/rZ!!2ut%06G4df:9i#m^hC"p+i*
!V$-i!Vucr!W<!6!sf/I?FOcnJW,21H?XLRFa&(VH[UDCJj"dAKnP)0J:2`cAl_A[.j5cE',;B)+<r6`
/ho4B2)?s@0f(^J2Dm`g2_Ha(?ca_t!!!**"pG28"Tnf,q#L$e'`eC>!s&B%!<`K57Z/oH.l/Ip*ZcI'
+UB24+!;^N+Wqs-,7>bC-7:/f+W;"'$4?b=rWiN0#5n]>"pP55!W`<'!sAT(#7Ue:#lmN,+T;?B!X&Z*
!WW8i!;ca4!<WK-!<<*$#6kW'IiAk4+W)%0%LWUMrWiQ3$4ZtG0G>3>)]^%H-nHnr*>Ane"Tnf."pk\I
%hTEg'c%W()]Tk;(`!bn"qD7N!snrs[N,5GrW<9+"9S]+nGiXq"U"o(!!!$;!sAW)!!<6Q$ig80!WW3%
!sA`/!<<*#!Wr?'rW3'#iW'#^"9JH$"9SW+"cWE\#Qb27#6k;4!<MfmquQWo!!2ut#6b)D-e*6[ISQ2R
JU;WbF`qtRH@('nM1g>/KnP#+HZjCE@T,WL,T@I1%hKEl*?c^W/2/k=3B&cL0JPCE4ZG8c:HU`n*4A<P
$31M<!!!0,"U,#1!UKdh!<WH,!WE'3"TT/JXZ7g\4rY^f*ZlOJ+<MX2*ZlXU+W;@E+sR"20d7b^(_?uV
"9o/?$k*LO#m^_<"9eu6"U"o/!WrW4!<<HD$5!^JUcT4u!>#J9!!<;m!;urq!!E<*"U"o+!"K58'Fpf`
&JZl/*"rei$2k,:#n%@^&e#?g)&jSN+<i'W,TRO*!WW3$!sJr;%1Wm[&J>cm(Dn&1*ZQ(9(C^Q\*"<Jg
!2)4Z"oo#5!!*!#!WiE(nGi[s"p>#/quHWq#64c3`W-&?!r`0+!sJl4!s&B%!<W0$!WiE(p&OI[('=a@
!!<T/#64b\#6Y,0!WrT0"9SZ*oDnahnc1BT)3V48RVAF5G^F^ZGBnL^IXZBUJ<GnDI<TR>>#7[N1bC'u
*#B;%'Gqf5-7LK!1)i&-2)[BM1Gh$L3BK8W1H[WT_Fk%8!!!6*!!)s"!WiB'li7+g!WrN&!"8o/%1$lu
+%m;;&f`(n,7u1H,pXBB,r[S.-RBlS((gr\r<<<.#RUJ;&ISsR#mUV;"pG,5"pG)3"U"u@"pFu,%M9MX
49,H`"UkS8!!2TiquQZp"9AT-!s/B$)$C$Q"_DBS3!MMT'bq>k%M'-a'GCcU(Fgg3+;,_7(_mYo$k!@I
#6k>8#7(\H&,m+?')iRF(]G<_)&O)%&IedD%hTPT2ZNg_!!!6*!!!$#m/R7n"p>#0q#CEr!r`0./0tE!
#QOo+!!*3)!rN#u!W<*!!TO.^!s])7r;Zp#!3m@=!<3-#!WE0#!VHHi!V-4^#89>\JT6okM1BtuF`r%V
H@($jK6_?UGB%4s8N\XO)]B\<+s7pG)B9kE-S$f'1,LjD0/GRI2E3]S1d",Q1bC8[LEI'8!s8E$quQKk
qZ$TsqZ$Zu!Wi/u*X;lmYsBa)(,%$],U=]a-n-Vr0f1@&-7gVl)\NGXr;['*#mptF#RCb9$6BKZ"pYA8
!!<K2"9eu2!=9><#6bKtF;,#j#RCV;!V$0d!W2p#!!!'%!W2pW":>8LUbEZH&1f"F(DIW%)B9_;,:4EG
*$cgS*#/qg!<<*'$4dUT$4."G$4I@R%hB9d&.T?j(]G-[&.K9i!!rf9O)Y^6#6P&/kPtbi"U"o/!Vl]r
!<io;!<@KI!X\o7!<<*$!S.5_!X8o;"p4i4!!#k+!!*'*"9JH$"9AT+!<Mloq>p0f$3UYfRIb$GGBnk$
4FqX!H$OUOAnGasG&qA!6T?_H+rqO:'GD,q)BL(K-7:/i.k`\4/i>aM1,_3S2`NTI0Jt+@c;"?S'bgQH
!s&H(!UKgd!V6:+"oo<S\Ka3_,;(u1-RpZ!/0u>[,q]N_1bKm`$j[%?!s8B#-NO;Q"pP24!<E9+!WWK9
#QY&5"U"u0!<W]0+0mj+$P='Q!sAc1!qlWi!<E0$q#LEqqZ%c@$31TJXV`r?+tPQ!*$6@M,TIL5)'^X_
-QNg2%h9!U$7lGf"pG5<$OdFN#6b56#R^tH',qYq%M93]&.AjN%KIQT2?4!l&-)\2!WiDg!!WQ/!s/N)
!Vl^$!XA]*#cdq+"oSE%"9IN_o`,=#!<<9/!WW3$!3,kr!XJr1r;Zs$!s8T*p&Opio)LZP"ro\El?Zoj
M2lsuCi3ruCik&QA4S^6.4$&T)]^%E*>]>"(Eb1`2E!BG/hJqD4#S`A.k_Gm4ZYJ_0JZBH;8ZHC*!.&`
rW!$%"9S\k!<*#k!$V[K"r<K-2]+>45r'Z3.4$2i2aTqd('t$C!W`<*$4daX"8r3.":5DB"p+c)":PVA
!WE'+":,25#lk/V!&CJ\5l_Dq(^C$@"9o&5pAk!imJor`%0-MBNMnZM1cdfP*?ZUN+"&d(4=:XB!!*<2
$kF!e(_R2Z!!3E9&ePTY!<<*%$Od@I"9Sc5%1<IT#n8?a0W%&7%KI4H!!!$&"98Pi!<30#!r`5r!"9,:
%00?q!"9#7!!<DV!!*-)rW!B1#RUP5TE"s%!"&u9"T/6&!<`N-!rW,q!;cff!(R7q!$<DuXI4!=ATE06
?>"1d9JdtE2(p:#+<27<*[2s_1,qKf9iYD*AoN-SO+D+P9fjgW3&icI-m(fG3*jF&'EA4>'*\@8!s&K*
!UTje!<*#l!'(5k!!!-%OEb+d-RUf=1+"\90H15s!Y5V?!sAZ+!X&]5$4IFX()\,9,:>3.8l7u2,8:4[
!!NQ0rW!-:*"tQ:63R8f#8%.?!!*0*"8;fk!V6<h!&Fuo!<<-#Mfi;Z,pb<0/gE#10,Xil!"KDB$4[RW
%1<FG#RV%R'cA#7+!)XV2a/r<'F=[<$j?nC!WW3@,8WSB4otW_!=o>4!!33)!qcQl!W)lr!rN)p!!!'!
!!!6+4<4P+f)YgOqZ$j-%Kd.PV#U`!!!<<-"pFi("Tef0!s/Mt!;cfg!"]29!<N6N,)>,i4!$+:-n$8u
+!W*\-mBZQ+<_mM*[3!b2ap_YF*`7cKT2:fSskt5S=#M(MI\n).5`eF4$dB!.hE9t&e>6Kr;ciulN$nb
p&G-r#RgV3#SI8N\N:9$"qLP2#Qb5<"p+o4#RDsc!s&B%!=Thn1,_'N3C$)-9hS)U=&i'o8gt&H!"&iB
%N.X=)$1!B$OR(>r;Zj"!VcZi!Up("!XK8I!rr<4!F`Dr$NL59qu@-.#R^qE%2'Hp(_dD_rW!$/)'p^T
.kE8*0J+b$,V(W+1,q-1!WW?:%NcQ37^3[.!WWQ6"TeQ%!<N;q!;cfp!;uri!"K)2"p+tU#6b\?!!!''
"5s4^!<WN3q>^s3$O>_u$kNFE!<<-("8i-&!X&T-!Wi#qquQ<f3s,H_"W@da+fgi3,oJ9\*Z#G2(_I5e
&/5s$*[3@-<b?E%LQ@XaQC+>DY-P40UnOWbUS`0$1+F(r+U]`k]+u;')\ND]!s/5uq>p0frW2]m!W`H0
rW!H>!!3LiGs;W9&IAL=!!i`+!##G<"p>#6%MTg+.l9:L4Zttr8PT1](K+79?W^Sj%0Zn8$NL0RT*#Q9
'FOsE!V?Bc!Ug"]!X9#B!rr<2!!!4]F?9[,&.8XA!"B5<"ptnX)]]k6'b_,g&f;]:.4d)*0.eY#+WMFA
,qgl4)up*M!#G_EK;/GR%1igI!s/K(p]10kq>oj]#6Y,3!!iR$3;`a^!<`E'!<<-%!rN)j!<3)u!$hXO
$k3FA!!*6-!!"`a&Hi.9!=&c.!<WB(!!!$$!WrN+!W`>u!<3&s!UTkP#6PMO'f;SS7M[*\'E]No#mCG:
$kaF#.n!fnP+%o2S"-%?Sti9gZEC-uS#X-%[>.4*+>b3Fa-dMa&e#Te!r`0"!W2p$!<N?*!Wr?%oDnjk
o`,!n"9&93"onu=$7M+!3!Tut"TT>I!W<!(!X&W2&g/bb48h8^4[)(s77g0I9hJ)`CKY48%KuhH!&gNr
!#5nJ'ajm>!!2rs!!3$"p]9pc!W`9$8,rVj!s]/9!!<H+"pP/QNf5k%'+#'I*YSkf%MK^"*ZZ4C,UY#h
-6sf`.kWM-.3ouP&ISpa0-`D!!!*<I$Uh.L!##P<&-r17!s&K*!VHHi!U0Re":,GG#8$qM!!'!4!!!?+
"Tno1!<N?*rW<*#pAk-mrrW-"(^13U&.A[H$NL/.[Ntnn!!!91#6k>6!<N0$r<*$#rrMoqqZ6$`$N^D2
$kX=0Wh(4K">_k7#n%(I$k<pk018r\KTqgfOGo-XNfTBkSY;aMSt2INWR./C3\iOD`*!KY!t5SO$N^5,
rrN&u!<E9$"9/H%!VHHl!V??n!WW6"!Yk_9"ptniU6ZN+!%n6T#R1D7!W`?1%i-?A3^cA&5<M.t7nZTS
<;]c);cd"J;^W(h)/-$8rW!$+$5!XD!<3)t!!!&r!rE#c!!iW."pbA6"Tnf)!#>\G-)$YC(^;ht#n.:V
(E+22,:P#d,Q8hg+<M^L*$Z[M)]'5*)]]t=+!*s'%0RCgEjeU@!WW3&$jZb3!s&N,!VHHk!TsFb!sJo3
r;[36!Z$AW!rrN*!!38r!!!&h!#,M?#m1/2!!!GJ&c`%:!rrH-"9S`(!Vlfq!W)ln!UKeF!XB)F$5<dR
Kop'`$4da[%h]Ni(a;.KC3+o]LOjeqF`qtSI"6p-NKKEmXhLEqW(TBbYa?[@#8%%A#n.1H!r`3"!WE'#
!<N?%"9&B#!VZTm!VHHl!C6\c!X8l<":bP=JraRZ$4d^X$k3RL!<<`Z0K;El8OPg.6V1'R=^,0=?<piD
CiiEA?P!r@RYM[Z$31&1$47"?rVus#!WE)u!Vc`q!Ug$f!C-_i"U5/7!WW9(!sS`4!X=@CD]B<#&.8s_
)&a;,-T3V(,9nWk1,:R=0J=t+-RUZ44#oSr)A"\)"@/K9+9iAU!!<9*!s/B$rr`9%q>gHorW2Hfr;d*&
!<E0#!<W0!$j$D4$33&/$3gP:!!;lp!sAi4"7Q9r!<<f=!',f7%fQG1#6k20quHTprW;uur;cftqZ6Nn
!!2Zk4TP]p$3pP2!Z6rs2&60+$j[Lh*[*sdDf0`HI<p-\EG]E%BP_X1I"I6;OdE/kWFs9*9F1t.#QXr3
#R(;.!;lls!riB#!r`5p!;lld!(Htn"9SW(!umE+3Z7u3#m(GG"99&d1H%[#>$bTGA7fLiCi433F)l/2
>ZP9Y@P+(`3rfKm%0HV7"pG,2!<<-%!W`<'!rW/q!ri;i!!NB)!WrQ.!sA`/!W;uu!W<!Q"sBAD4r=8,
"9fJ^'*oX;2_cj1*>]bE.4Qi!/M8\0-mq2W5qO`W1^f&F2ZX<u&Hhe.r<!!"p]19on,W:c!WiE(q>^Qu
!!!H5"98F"fDl$S%0-A/!rDs!"UYY:$lfW]#R:P<"U,)9#mgb:"UPGC0>%8k!!EH*!!rl&!;HTp!;6Hk
!;uri!"K&8%1`^E"p,;pRZS[-(F';#.j?')DJj'#DJsK7EGArd<)m%*@VKe)IZU1dNO%b?+rC1X"9AZ4
"TeK#!!3'#!!DrsrW2coqZ6Wqr;lWm(]amM"TSf5(."[\+qt[m#9!aG&i)C)5trS&=^YfP@pr_P@Us%]
Anc%!DcK8IZm#b^!!!E6#mUV9!<E9$!W<'$!s/Q%!W)ru!Ug!h!<W3%!WiB'qZ%fC#m:5:%3J3=Or"</
!=U:e!#[d\6XYG/Up.DE`5]pFe^tPdb-[%8<_k7a8WsP_!rr<5%1*.4!<3*!!ri;t!<*#f!;cd!!WiH*
q#Cs5%LE4;!!*V.PlUjm!!W]3qu@'.$kO'e(D[\t&.eaM#nR^`'+G3I%2Rk'!!!c4!!<?0#mKo#nH&Ri
r;cZpo`.#S"UPM;!!X#=$iiPhJjU=q&eGgA@VKFa?X-c8;GKeP6:==;:fCFu?Z:URP*+9H#QYA;!!!-,
#R(2/q>^KrrW;our<!!"p]10lrW)isp&GR+"onW/'akWS7&GJt%1rL=.Mb$59NGJ/A7fLiCM[j*E,fl<
EGT<)De<QmYRgd7$k!@H$3p_9!!!'%r;cs$!X&H(r;l`rrrMQg!!3!!rrMrr2?F$^!"9e\*!AQtE\e(=
$j6YX8n<-qKoqq$WN`kE_9('RdCPp,H#@1l9i%;]!!!E=&.AsOp&P$lquHZr!!2QhquQcurWDrr!s],:
"TAB)"98V=&In[=$j6P1!=95J&J,B[$k<1G%h/sV%M'*^&J+pB#A=;H#6"T*":,;="76*a!W3!!!rW,u
!WN6#!VZR8!WrN."T\T'!s/H8$Nan[A/$!p(c5,s@9H;p5r^Y!0H;i*3'BMk4Zbi*BQ/-`S/)nA"98E(
#7(S=!W`?!!!!'!!r2rt!WW8r!;?Nm!W;uu!WE'%!<<*$!r`0Y"9SZ=$j'qS<s&X,!['g1@q/nS?X-c?
@V0@lDJsH1CM7@!G&M)PN!B[i!<WN3#mUS6!!*-&quQ]s!!2irrrMoqr;lcqqZ-g"!<E0#qu@c=!!!-0
%1=$\!*?[4$l9Bl4(O&?][#*]g"PHNnb<"^'CsYVO,/R9Cl4)R$315:%hB*T"7lNf!Up*e!WE0!!rrAu
!!WK-!s/W3$8Df%!!!&O!!!-,$O$M9&ekui#m1/-!sT&=#mgkC#m^hI'+ksMB*/SC!WiK0#m^\9m/["a
q#^KprrN'"rrMoq!<E9#"9JZ-!rW**&fq#Y(1k-j2%(?J;bobC2(pF*+WqjL+XJNg0J4n*.QgR.>D]!O
!"0)<!sJr:#R:M9!s/9!"p"c,!s8Z/qu[!%!Wi&ro)\di#QXr-!WrK*!<N&t'G)2`"V"M2:a5ub>@V/U
C27QuBPS/sEHHAKH$OXXF)cGSF`3P@rW!?0"9AT."9S]+!<N9&rW)ltp]:R#!WiB'q#L<noDejlpAcE=
"U>8J)ZTjE=gM[)-;TbsW3sF\bKnYjhrO"ho_8%Dg;^N4Z*'UVXL/<:!t>_K%1EOI"9J/qp]9mbqZ6Zt
quZs$!W)j$!<N?)!!3<%!"o_R]F4cG!"9;I$O-b:!<<*$"8rE&"q1Y>$P<dY-s$BN!"B/:!!*6,!s7ii
r;lWor;ciuquQj!qZ$Zu!X&B(4Tb`g"TSN(#mq(Q%g<k%WIn>C:,jOB*uc%5(D[`#()\)7,9e6M*@s<7
5^&e#!!3Q9#7(VB#RCY>"9JT#!!30&"8rB$!s/N*!VZTe!W<!"!<NB%"9\f-!!!'!!&"BV#7V(A$lG7T
>ZblU?Y==uF*)SLG^4U_IXcluIscToLO!p1]*869#Qk&,!<W6&!WiB'qZ-TrrW;lsrrMoqquQBhqZ/_X
!!*0%!!Wo@#RLV6&gjcQNg@,VUo:K*]uA7De(31+hr3SSi7ur9e%Da(h]NIA'bC`[$OR1F"TnAt!!3$"
rW2lrq>g6jrW<!"rWE6'!W<!!!X/H%%0Qn9!"9&3SQQU+'b:WL!#bk?!s/N)!<N<)!sA]/#7LS74h(S%
!#Gn@!;us!!U]sd!VZZo!<3)u!r`5u!!**%r<!0(!<<0(rW"eZ#7CnC!rrZ5EMPiO*Zc7=()%;m&J>`l
(E+87*?,k6+tPB,9m0\O&HE%H&.T!L"9er3!r;lu!<NB&"T/?'!WiDt!;6Hm!WE'"!<W3%!<N<$!!!&u
!"T)7#Qau+!s3\V@pW>LC2j,k#'+d-G'J=\rdG9'I"6p%J;BtF+W(1[rWN9(qZ6KmrrMiqrrMoqqZ69g
!<E2t!!`Q+!='#>#6Xr*'bVO[n>NOl['mQ\`QQWWe^rL1i8WhsjqQn;in)Gset+rS%h0$Z%L`XL"p>#%
!!!&u!r`5m!;?Nn!rN0""98N$!!**&r;[9,#6b)-$j-SMbm=aX#Q"N#!W<!3!<E6(!sAi/#V)_a!WWK-
!sAc0l2^eapB(<oquHd!r;lcq!s&H)!VcX&!<if1#T*dJ>*NM[.462X)]9G+&J,Nf()\#0*#on9)&aJ<
-8@,TNDp)e#87d`#QOi+!sA]%!!**%q?-]urrMlpmf<Om!WrK)pAbp/#65#J$OLIILi?s;BPM@"CM@Hr
CD^o,EH?8HG^4R\I=[*1H^2-](C^HQ#mpk7!!!&o!;urp!ri;s!<3-!!UB_3!<WK2$4-q;!#?.bK\42Q
]=u2%aNMoWeCN:+gu.5Ul0@Qul08rJlKQODl]a(E%M0-_%1*7D"Tnf#!!!'!!r`5l!;6Hl!rW6$!r;lt
!s8E$%0d(D"9o&1])VgD$j?\-!<3)u!"K#3"9\f-!$E2*#m:_>$j$bB"R6!d!VZZp!;?Nj!!!&n!#GY=
"W7:?'L%sD0c^rA)]9J.'b_2o(E38nr>beW'c\591GrE^+!:Rp%1`XC!!*-'!WW5t!!**%r<*!"rW2co
o`>'or;lm!!!2cn/cl+m!<XQG\R9&V?XRV^B4YU`@:EbZBPM@$E,p&DH%(@#Lld4TU,X_)"U#)7rW2Wk
rW2`oq>gKrrW2lrrrMZj3!9Kp$jm(M!!"K]foMu1\A-50b08/Wd*^:kf%]0Glg4!(m.'cEp$g>Xc<*@?
#mUnK$jm:G"U"N"!!3'#rrMlpqZ-KorW)ouqZ?cuq#LBq%KQP1!s/K'#QhgM!!!$#pAb3q!W2p)!sJ`+
!X&K'4LYXr!!EB,!s&Gh!;urn!rN*!!WE)u!Up(J!<<*,'aG3K"HY5g0e3\<)AsA.()7N")]g.F*uu=A
*ZuUJ)]95L$9h.C'En^J$j?V2!<N<'q#CKt!WrQ'!rW/o!;cfr!<3)t!rW0#!Vl^Q!<E0##o*a]!?JOQ
B68<'=D;;R?X?uA>[CcG@qB=gD/aQ?IY3H/ULJn-YUBbW!=&c0!Whonm/d.errN#tqZ6Ek('"=;#RUtP
('G*J.*I10[)BJabfRoHr5g&'bgG)#jlYailLXoQqu==R\Ca+`"9],B%1EUN#6Y)'!!!'!!ri;l!;llq
!;urt!WW8q!!rZ."9er2!<<*B$38QW!!<3.!WW3$qZ$Zu!Wi3!"Tno/!!<N+!"1'l!<<B.!!!*'!Wh]h
r;lcsrWE'!q>^Krn,O(%!!!99!!!4rCF1MD1(#?:(`FG5()7N")BBn@*?,q;*?QCF)]9>=%Q-dYH2nfp
%0HM/!s/T-!Vucr!W3#u!Vufi!W<#u!Vc]r!Vufq!?;(>"q^h<)o.bDB3'C]F&u^S>Zt94=^#':@:a-d
Ci402FEr=gJraSsKnGTi((1HNklCP\quQj#rW<*#quHQop&G[*"9\l<('=ghf!gF,R)uJT[/RfS]tCti
]tV7q]tM2#ce.7EpAOjfbR`CO]=\b#'+kNS"pYD>"p=]%rrN-$rrMWi!!<*"q>gBnpAbd+!WrH'!X8W1
#aR^U!!*0-"SVor!W<!#!<`Q-rW!0*%KICs[K$R2!!!&p!V?Bj!W3#u"8r8^!&"?W#m(*7N@H(]-l=i[
'H\//()7Mu(E"/2)AsD2*$$(@*#fh7)`B<+F*@Th'*nL:!s/W/!rDs#!!**%!rW/s!;$<i!!!'!!rW3&
!WiE"!!33(!WE'1!XoGJI'QmX9PI^X?<:N9=8c/)='8d9ASH"!rbi9gH%(<jFG=gLQ%o>C&I.J"rrE$!
quZg!rrW3$quH`tr;ls"nc1QT()S0ZeV9-AXes:HXLGC:Y,n\+Y->13Un4*T\&[(Zlgj`7i9JOlc)qTl
*";lJ!X8r:"9JE#rrN*#rrMcmrW*'$!Wr?%pAk3op&P'm&-)\4%0-DNRfE]o'Fb6M"Tn8q"9J]/!s/?#
#R)%]BiG]F#6Ff(!!<-%quZiupAk0nquZj"rrW3$qZ-NorrM]k)$UNP!<>$A/gMDO(G?mP,7#A.'bhAt
()Iec(]kQn*<$rl+!DRD/M/8=Rkt*X"T\T'!X8c/qZ-Hnq#LBpquZftqZ-WsrrW*#!<N<!!!*-(rW"SQ
!!WR#ZrgF2;H.F9=^=?s;c-Cj<E<4*?!q/RB4u$qDf^/MFEE%X?uWG8!##P3!!!&h!<3*"!r2ru!ri<!
!<3)t!WW8n!##J>'H1cALldmeRBiT_WK3pKS!s>G+Io!pTqnWi[CsQ*g#MA[k4%BC\`dE2+UeDP!!EW7
"9SQ&rrN$!rrMfnquQg!rW20^!W`?'rW!,7!X&K'#m1J;"9\8r!W`<'rW<H.!<E0#$PWR@`r,l@#6Y#-
"9eT(rrW3$p]16nr;us#rrW3$p&P*no)KO6(B=F<P]/&i-R'WH+!)@D&/#]n()7r,'GM8s()If*)B9b>
+s\9P+tG6(;3q7k!!r],!<rZ-qZ-NppAk3orW<'$r;lcq$3://!s8Z/!s8T*qZ%oD"98E'$NL/BZBnZi
@U3&-;Gg1g77^-K;,^Ir=^#!5?!h&PBFelrEccACG'e.AEMj*S!!i?#rW2QirrN-$rr`3&rW<3'!<N)u
#6=i,!WrN+!V?@B#lkPogW>V@WMH)EP`q5sLl..NNJi[ON0^3@\@K)V[CsZ1hW*hho@^ma%FljO#6t5/
!=9#7!s/N"!ri;p!<3)s!r`5`!!*0.rW!(12Zs*]rVus%!qZHm!W)p4"9o)5!!<H+"<YDZ"TT#9!!!0*
"8W*"!r`5r!<*#r!X&T,!W`>a!##VL"TT^".4QA^*ZGt:*?,n0',:E\!#5DG*#','(Dn#/*$$+E*uuLR
.PO;B:]LJ$!rr?*!s/<"quHctpAk3orW<'$r;lcq!W`<'rW<9+!s8T+qZ$Wu"TABT#6P2jW)R#'?WpE(
9hnAT6q0aA:/Fhf<E<1'>$PEEAnYprDfB`@I<'"<RpZ4!#l4Q!!V69l!<N<(!sAK)rW<3'!<N)urrN$!
!!2]l&HrR_=k/G!S#<!KOH#9[N.lubL*;8(K8,GUVQ[8.YHYORbh(e;oD.@`[a9^F%LE+8!=/l4q#gTt
!!2cnrrN'"rrW0#jT#Gg(_29##lFZ'!s8,qrrMuu('=[C!rr<%!!=:/+U.uV"onZ+!s/Q-r<*'$quQZp
rW2cqrrMrrm/Rb%#R(3TB-/?;*#TV5*#fb2'GLEZ#nmsb',)&p()Ikf)A=&1*#p+L-n[J]RfEHl!WW3&
!Wi9#quQEirrMuurW2iqrrN-$qu[!%!Wi3!!<E<%!&4N\$^H]H=]Sa.;G^(\8OZ!77S$-F9i"Vb<E<4+
?=@AUB5).!Ed<(UD/"C)":>D8qZ-TsquQKk"9AQ*!sAK)rW<3'!<N&trW3!"!!2]l!!3ZD,.P:>QC4J=
Q]d>cM1pT\JfoVpJV/fBR\H[XWiieFa3i`,p%mgq\$t3:(CC3D!<r`("TAN'!ri;q!<3)s!r`5^!!E<&
VCDlM!!**%!<N;p!<3)p!WW9#!!rfC"uW@[!"9,7rW*'%!sJT*r;ultquHZrq#^QsjT#et!%+$^.2<X9
(D[l,)&F"c'*8j]')iLI',)&p(E!)g$5sg%+!`*Y3^J]nqu?d"!s8E%rrW3$oDnjkquZiuq>gNrrrW'"
!<N<"!!**%rW")H!'.Je>YS1!<)?=_84Gp35sn%084lNL:Jk%k=^5<C@h*$\B5DR4I!'7IE3<CN#Q"K$
!Vulr!Vl`q!WN6#"9/N'!s/N)!Vufn!V?@(#RO>]KTh:ZSXPb(MMHn:J:INH(4CX^KoM@fTVJEdZb+-!
g#_f!k0CuO"5eJD%/p5."U,&-"o\Z(!s/N)!VZTo!W3#u!U9[b!WE'(!<<>I"onc,rW!!#!Wr#prrN*#
!s8W,!W)j"#7ge9SGiKm!<N9%!<NB&"8`/t!W<#r!W)rt!Ta:l#69*D0c(]A&eYin(`*o$r"K)CrXf;H
',))r(]G6S(Dn#.*W@/`4>LN5qu?m%!s8T*!W<'"!W<#m!<*#t!WW8r!<3*!!rN-$!Wi3!!<E9$!&+]]
P&=Z$;c6Li9hS&H69m^u5=%Y)7Rp$C:/Fhh=^>ED@Uit`Dg$DJCO^,_Z4I6;!!E<(!WrQ&!r`5s!!30%
!WW;t!s/N)!VZTm!VHFH$kTJ'O+WLVQ'78eLP12,I!^0cH[:!bI=d<;Q^aVCWNWeF`m`o6o&\6LZH1ZD
%K6>-"TAT)#6+l+"9\f/!WiDs!;uru!rW-"!:9dd!WN6#!!WT,2$a3a#Q+Q'!WiDt!;uru!r`9&!Wi6"
#lt,2"ona"S,ifl!!!&u"9/H%!WE0!!W<#q!W<)u!VHHe!!30&"9&92!XGGP-P@"%&.oQk(`!f!r"B#A
rX]eV&ebrn'c%T&)&X>2)]Tk@1H%ge+8l3=!s/N)!W<'"!V6<f!VZTo!W<)u!s&H(quH`urW"VX(VWpQ
8ki#T9M.iE69dRo4$5Yj5XIk.84lQO;H?t,?=.)LB5M[4FE)bSJ@dfFqZ$TsrW;s!rrW3$q>gNrrrW$!
!WiB'oDndiq#CR--.mU&JI73lOH,3QJUMihG5QJ$G'A4\KoD1\R\$:RYdV9ig?7kcg=sZ]jA6Bd!<**$
"o\]+"o\W-!s8T+!VZTg!U]pf!WE/u!!Wr6d/Xs_"T/9!!WN0!!;Z`q!r`9&!Wi3!#Qb&3"WA-"&H_n2
!<E9$!sAZ+!!*-!!rW0!!:p6W!!36+#5nN5+.5J+"q;"O&/,cp().Dp')iLC&H31@&.ofn&ebro(E"/3
)]BS3)^-Xm13?1i!!36*!s8H&rW3'#nGrFepAk0nquQs&!s/N%!!30&"9&9I#W'#06pO=98kDK?5s@@j
3&ioZ4$>en6:=:792AJe>$P?>?tF']DK9lEHA6L?CBX\?!W<!"!<N?!!s/N*!Vufr!WE/u"9/H&!V?Bg
!W)jO%7A[5GBnmuMMQq8H?XFMDf9N3E,]f;FaAUpNfoZpS>)sb[`$YPkih*ahR;$j&cr@D"9\f/"U>59
"oSQ,!s8T*!VZTh!Ug!k!<N?*!r`0*"TSc0Ym^s>"9&9#!W2rm!W<)u!s&H(qZ$j'#mV"Y?iUK2!!`N*
!WrK)!!!$"!W<)u!W<#j!UB^f!X8o6rW!F<E"s6"%1<OR&JQ#s'GLEW+V5.p%LimY&.oKe&ec$!*?Q:?
(DRf1,r%&HHN4-P"pG,,!<N<(!VZT[!;urr!WrN+!Wi6"'EJ:<!<<+HPXSMB8Oc-95sILn3&^an+Z;;?
4$>eo6UaO=:K(=t>$PBCB52=,I!gNmNM-CX#6b2.!!E<'!WiK&"9\f/!W`?!!<*#t!X8].!s/N)!V?Bl
!W<'$!<<-!!B^>dN3[AWJq\l0J:)T_E,B?(BP;*pCM[m-G(#%%Nf]HjS"Za`^!#'fkj%<h`PB,"%LWLE
!WiK0#6b;0"9\f/!W`>r!;QZl!;-<o!<WK.rW3K/!Wrre?j6c7!<<-$quH`trrW0#q?$Tt!<N<!!!WN0
"U#\QE;BP:!<WB(rW!!#!X&E'r;lltoE"F]qu@K6"pkP;!!&H<*YAnn$OI4Q',D;s&eY*S#S.CT%1E[U
%hS^P(D7K&+!MdG()%N,+s\okSH'!&#R1A2!<*!#!WiD]!;llo!WW9"!!E<*"U,)m!4>^%9MA)J5<V+j
3Ar]L0ekF>1c@9Q4$>eo6qC!J<*!+)>[V)TCNY&SH\QU_#Rq+H"T\T'!<E6'"8i9(!s/N)q>gNrquZm#
rrW3$oDf[.!<N<)!s&B%!X&]6#KUn4JVAi0HZsQ7E,0-!AH$$c@q9.`Bl%g8J;9#@NffTqTW#9:d+mgP
mGQNnkSk<J#mCA2":#/8qud-)!s/K(pAk!imJm[s"9el/"9nr."9>/,'E.t5!<N<"!!!&s!r;us!s&H(
q>^g&!sT8OaT)MG!W<!!!s8E$"T\Z,!s/Q&!W2ro!TsFt!XB);!!!(k,9.4'%LWRN%h]Qj&eY*Rrso&<
rX8f:%fHq=&Jc-#+!MdG(DI]++!E*YQQQJ:":,,1!W3!!!T=%T!W<*"!W<!4!<iT.#nsjB:J+5M6TdCi
2`3BG0E*R@0/,.;2)dNW5!VM-9i4hh='8j=AnlF8I1(@SG/>^7#m:J7!!*!"rWE-&"9S`-!<N#srrN$!
rr`9&rrM]k"9AN)!sJT''*A:>%NWi1H[pa$I<KUIBObFV?2e(R?!^lH@qKOuH@^a)MN*aaS"m4&bh2%E
n)i,roK3g!"pY20"9\u8"U+`*rrW3$pAk*llMq@p!sA],!sJ]*"TX_d%/g2+!W2p!!<WGp!WW8t!!rZ,
!Wif9Y5et3qu?a"!rN$"!WrQ)!rN)S!#>S@$j$D/+,hNh$k!IN#n%4T'+tlf%fHh@$k*LO$k3^G%il2n
'cJ,:*ul.7(`FD;,US+7!!3--"98H*!s/N)nGr(ZpAm_b!W`9%!<<*$#6=f10r[oG7n,p43]K#S1,(=3
.k3&"/1rS11Gq*P4[DP0:Jk"h='K*EC3"TGH%CII;ZR"$#m1/."9eN&!WiE(q#LEqquZm#rrW3$nc/am
!<WK(!"oA6!Y7H/E.<7bIX,sMAmeeE=8l5L<E<1'>$PHICiaoOJqf/CP*_cA]?&O^lgX2fWUjU1%Km%=
!!<N5"U"W'rrMioqZ6Bjo`,C%!s/H(!rr<("`+2Cp&G'orWDrtrW3!"!!2rsrW*3)!X]-P$4m"6!<WE$
!!E<)!s/Q%!V$0h!V69q!!!$"!!`u4!"_MB-QWa*$OI+I%1a$^%h/sE$RH,e$OdIS%hB3`'cA#7*uu:<
(`4,0.3i_K!!!'*"98K-"Tnf,iW/QN$31)-!!!',!!*+#30d6784>g-3&NKH0.e\'-mpAj-n6`!0/5:A
3^,o%9MSD^<*<R>C2nE>F,5C7GQ7^F#6Or-"pOi*rrW3$q>gKqquZm#rrW3$nGiUk!sJT'%g)e7$"U/X
I!g?gFDb_u<rc+s:B45j:FAt9;c[%.Ao2U7IY3H7O-?$1\&HePkO%KeVXB6M#7(P9!!EW7"9SN&!WiB'
pAk$jl2V.l!WW3$!rr<-$9[q\!!<*$rW<'#q>pHn$NU;1!<`W3#<tN["T/6#!s8B#!!3$"qZ66fr;lKi
"T\Z)!!Wo3!"WaO.NB$/$4.%I$k<gZ%1Dq<#R_%M%Ls![&JPHe*?Q@D*?,mq(Cr,A>E/[`"U+u.!s]#4
!Wh<]o)Ta0!!*-$!!3H,"9<ar:eXGJ4utSX0J4n+-RSd;(aULV.4Zu(1H.B\77p6J:Jt8"A86%(EGl>H
JV9<h!!WW0!!3B0!sAE%rrMoqrW2ourr`9&rrMTh!<WK(!#,J7"p0^LFEr:\F`;)(=AMIX7nH>O8Kpc$
:K(D'Ao2U7J;&i=OHuZI_9UfqlK.!&kGA^i%0Zb4"9Su:!s/B$rW2cop]9X[%06J0!!*-$!"C(`!!!&o
!!!*!"8i6#!VHF%!<WB("q1S@'n-,f!!E3#!<N<"!!!'!!r;rg!;uri!#Pb>!!!02!!*(S9J%.q$OI+I
$OdIS%1EUC#l=oP$4@7O%M''^'Gqf3*uu@A)&=)0,9KsS!<<B0"98N/"Te_n!;-?c!W)j6!WrE&!=8`2
!17Cs8Ol'.2`*3@.k)hl,Q&]3+sSB].4d/03Bff#8P;cR<*NdDCiFE9K7S?C!!!90"98K."Tni*!WN6$
!VcZo!W3!!"9&?%!WN2j!!*0)quAhc!iglsG'\=NCLpaJ7mK:(6:=4/6:+(08PN,d?tXA"I"R01NKTp9
]?&O[kiUX(l`Up&&-i7:!so/5quH`tqZ-9inGrCc!<NB&!!iZ,!"!ZL#64f!!!!'!"8i6"!VHF*!X&N(
"Ub;<&Y/n+!!iT*!!33!!!!'!!r;rg!;lli!!<9*!!!E0$31/.S3/GB&do!QrX8o=%1ERLr<N9,+peSa
$k3[W%hTKm*$64B*?5n3)^-%?:n@ml#RLY7!X8c.iW/ZQqZ$Wu"9&9,#QP/2Y#eOk76WOf1bp[6.4-;a
+<MXF*?H7D+X8<_/MT.F5t+:88ki2c?=[bfF*MnYG,5BC#mpk:!X8c/q#U9krW2`prW2Nh!<WN'!"o\C
_K:$CGB.M4@9-#d3&`i[4t&TX4?Pem6UsjL>%),bH@^a)M3"+([DL8Djlb1-l*D32&deaA!XAl"!;-B`
!<3)t!!30(#6"T."98o6_?:DM!WE'"!s8B#"9AT,!Wr6"rrD`m&H`1;!!<N-$PofD!rr]2!!!)t!!!'!
!r;rg!!E<'!WiDp!"f;9!!!$*!!<4u4=V*[$jd7Mr<r`8#m^G5'*\XG#7(SA$OdIS%hB6d(`XS<*>0>2
(`")9(aD&>%KHP>#64c."5s7V!VZQp!sJT'2$X*f!4Q!'5t!gm1,(7.-6s`V*?6":)B0V8*?QIP.PEV=
5!qb/84u`Y>@D/]F*VkQE2EsJ!!Ef<!!*6*!W<#t!VcZo!VZZo!V-3k!sST&3t)G?FE25@DeEQc;+3K!
0/>FG3&``R2`a,h7nlrfA8ZU@JqSo;QD:Xrak#>/gXF<]*t8Vh"onZ-!r`2o!;$<_!<3)t!"/f3#Qau+
"98E(ecP^K!<r])!!!'!!r;ri!"f><!WW</!!<Y'!!3--!WW3%qZ$TsrW;uurrMZj"9AN)!Whro!W`E-
rW#(d!!<5"5pR*X%1*@N%1EXQ#mUV:!sA`1"pP;<#mq(M%M'*_'Gqc1*ZQ.=(`+/:)^m#9'*/(F#QOl.
!pBX\!;cfj!!*0)rW#(c!!r\:=[kPA4#8QC.OHDa*ul4;(`4&+(`=53+<r9c1,h<]6UaL:9iG/#ASZ@3
EcQ/p$j-JC#lju/!rDrt!VcZn!VZZo!WN/l!!*3+quAee%aTB8Ble*$?Wg)f1Fah)0/G@<0JG4<3'9Mu
:KLq=FFA[kKSYe_Wj]mof\PNJXiht("VV+@!!E>p!;$<f!!!&s!<3)u!"8i/#7:P5!<`B&"kEeR!!<6-
"TeQ%!!3'#q>p6h%KQ\;!rrH1!!!(_#Qau2rVus#!W)ls!r2lf!!E<'!WiDq!!30("o\K("on`*&#h];
',:r_$4RCO$OR.D"9&?K!sAc2"pbMB$k3[W&/#]p*$-.@*#f_1)^61I/Z]Tf!"K/4!!ED_!;cfk!!30'
"TAB2"onr0\5YjY6TQtT/1;bs+W_U@(`!i$'GV>u(E+;;,q:Q*3^5nt77^-N=C5TREcuA:Kp`5N!"]A8
!<`K*quH`tq#L?opB(6no)Jdo#5eH;$k(C%BkML&@9cf(4>8*.-RgSs.Ocet,;1i34[Vh>>\A&&I=Hd#
O.</V_TpZ`hVl)`+Vk4o"onW,!qZKb!Vl]q!W2rs!W2p,!<i`1!!!$'!"%?^!!3#u!<r])!!!'!!r;ro
!;lg$!<i]1!!<N+!!J>h"TSc+!!*-%qZ-Wtq#U$d"9AN)!Whro!WiK.rW"ST!!<4s4!YLT%LEIN$OR4I
#6Y).!!**&"9eu7#RUqK%M'*`'c@u5*ZZ4>(`"#"+;uRgV@j"3#m(),"Tneb!;cfk!!30'"TAB8"onr0
Yu*kN6TQtS.OH;[)]9G,'E&Oe',2/t)]p:Q/Mf@L5XIk.9N,)%ASQ1+D.]2q"U+l7"98Q*"U"i,rW)ou
q#L<nq#^Hpo)Jgm"U=l)3t)A6DJ*R%C1(1A76)tH+sJ6W,9e<V-7LQ'3Bou/=_)DoH@1-lNLHcP_9C<V
g"=WZ*>Skj"98H,"8Mro!;-Ba!<*#r!!*0*r;[$1$Ob,^"UY,-!<WE$!!WH+!s/N)!WE-#!VHF&!<i]1
!!3B*!We8d$318/!!*-%qZ-Wtq#UHpo`,*q!<N<'p&G0q!X&]+!"B)3!<AEO+Vbb'$47.JrWrT0"8i-A
!WrQ/#7(YE%1Wm\&f)?)+!)FB)]0;,*ZZgmV%3_0"o\K'"U"ki!;ccn!VcWs!<E9*rW#+d!!`Lt<BiQ4
4#/B:,Te!D().An&.]9_&/#Wl)''kI/29(G5!VJ)9N,,'Anl4&DJPYs!!`K1!WW6*"TnK#q>gEoq?$Np
rW)Wl!WiN1qu@?9#.8G\Ao_Wn<_c"@/0l>Z*?G,!-6=<U.5!J?6VCHgCisuJH[gsAVmO7^c-Fnnb-;d#
"q1S6!XJr1oDnOboDngjqu?cu!<W6#$ipM<"cWWd"9nl,!!2rs!!3'$qZ6`uo`,I&"U>,0!X8W.#E&Zp
!!W?%!<N<!!<3,r!V-6g!VZQs!<N<+"o\K%"TAB$IKWFg()@G[$3^_B#RCS8qu@i?!WrT1#RUqK%hK<d
()e28*uu=?(DR`,+>c-O%0lk6rW!!'"9RQ_quQTnrW*'%!sJT'%gE"9!/FuE4@;1c/12V_)CQ@8&eGQ`
%1NdW&/#Zn)^$FV0JtmS5=.e4;d3^CC2@a+EKl%T#64u-!!<E/!s8E%!!<*"r;cZpqZ?Zro)Jjn!sT#.
!"fDAR<r4NEG8]X90bBd,9@a?rY>SP)&sbD,qC]05Y+g[BleHAG^YF9VR+%XaiW&d`2FCf"ptD3!so/5
g]76Qp&GC%!!<3l$NL/7#5A/u!WE2u!ri;t!;um-!X/f2!!*6'"r)Id'*8:8!!*-%qu?d!!Wr/unc8Rg
pAb<s!WrT0rW!B/!!!=&DAsB*%LNLL$2t22"TeK#(BFR?"pbPE%M'*`'GhZ/+<DL@(`!l(*X<rI98<r\
!!3'!!X&T+i;ifWq>gNrrW3*&"TAB_"TSN3=ar:k5<1GK-6X?G'bV#e$k*LO$k3[X',DK.,:P6%3BTMl
78$Q_?tO.jDfK]^DZBtA#6=f)"9\f.!Wi0"quHctq#UHrq>p6h"T\W+":#50!%Je!Qr[a6Am8,&4uFl:
*>]A#%hK?f(`X\H/i>d];-[aRFEMbQLR"X=]`,k[dalL$',Cf]"98N0"p+i(!!30$!94(X!VZR%!<`B&
!?O#s!!ri1q#CBqrWDuurrMio!s8`4"8r3("trLU%Kcb2!!*-%qu?d!!Wr/ur;cNkquQNl"9JZ."U4c'
#8SVE)&a"o$N:A2#QP#'!$21D"U>AC%M'-a'Gqc1+<DI='bqN(+Xf*RBb(=H"9&<#!TF+Z!<*#p!!!'!
!r`<$!'C>`!#[;V1HdcX0InFl)]'/!%L`^P#mq"I%1a'd)'0tM/Mf@J5!_S0;-7.9CN"35CReH."98`0
!!!*"!Vlf_!VZR#!!!$#!X&Z4#Qai'4<Z_j;IjEL=\hFJ1b9ml'b:ZZ$OmX](`jqQ1HS!#>@qeoFEMk_
PG#%g_o'=;d*H_H&d]'R!X&`3!Wi9#rW1pWrrMus!s&H'!"&c0!!!0(@fQQ6"o\Q"!!30&"8N#u!VcWt
!<WN2"TAB*!WuC8('as?!!*-%qu?d!!Wr/unGrOhpAb?t!WrQ/"oA9(%L\^H+:AMW$46V9!!N)t*WZ?H
#7:kL&.oQj(`XV@*Z5\+'c7u;/2;09'`\4:d/X4K!<W0$rW!W5!!!N>V`$n"1b^C)*ubt.%h/mQ,RF__
#n%.P&JZ0(+t"rt3'0;i77pEX?"IhmF)kZi2@9Ec$3^8,!!3'#r<*$#mK)q[#6=l."U55<!rN$<()snb
BOG.I9gUou/LDJP$jHk?$4RR_)^6^c3Z^X`=_2JjF*)Y[Oe/S^^qmb/`SF6)%1<aT"9\o3!r2lM!"o>8
!<<*#!<<<(RK*ft!<E6(!W2ot!VQTn!W)it!X&Q/#6b#+#6t6s!"fA<"9&9$!Wi3!!W`?(p]9mb!!2cn
"p"f/"9er0qu@!(!0o,_#m^nFr<NE/"Si$:!<WK1$4ICU&ebus*$6:D(_[Gp)B^@^1k$kj!rr<*!R^rK
!<W-#qu@?1!W\l\7kl_P.jQ5V((q,d$46\;+UJMb%h]Tp*?lj_1,h9Y5t+CB<a93QFEDP-Zkj2P!t,>1
!!!'#!rE*"!q-0^!!iT,!sAf5#RCP2!':5f$+!rQ>$4iu5rpkU-QNm."9Sf5$kO-l+Xf'*6V^cpD/jW=
H%_<NW3sCS]#_MB.iAU$'+G*J"U"Z(r;lfrhZ*`Z!sA])!!WN."TYqH)#aL;!WrK)r;Zfuo`G!krW!T5
!sJl3!<E0,!5edA":#,5!!!&s!!30&!q63j!U]ph!<NB&"98K!!!\-I+:\bh$N121"p=Z$*ruHI#7:kM
&/#Wk(E+86)AWnq(*4VF4[s]1%0-D4!SIJL!!**%qZH`r&HMk3O'=h+1Gg[1+WVC5%h/pF#pBWa%M09h
)BL+O/M]7H5!h_4;HI+8DfBQ;Cmt_7!!<N2qZ-Tsr<*$#mfE%\!s&H*"9\o6#RCP2!'LA`!2"@?>$+j"
5s.([-m'04"U##9%M9Hq+t59.6r$lqD/jZAI#!u[Wj][RZGsZ!)\<8_&.AaH"U"o0rW<'"f`2*T!sA]'
!!!$)!Djs?#Qk/1rW2osquQWqqZ6Zr!<E<$"9\`+!"a8O!!33+"TAH!!!30&!q-0X!!**%r<!$#qZ$s*
5'S1a%20-S"U5#3"9SE"+9;NH"U>AC%M06d'G_N')Aj2#%i?K6,Y;<R"TSN(!s-gM!W`?(r<!'%!W)j3
"%A)03AWZL-mToR'G1f`$OR4K$k=?j&eu6'+=/Hh1H.B[6UsjM=^Gc\CM&$KEruCB!<rZ(!!!&o!q66_
!!rZ,!WrQ/"pYA8qZ%`G;kI/q<EW'a4ukAJ+W(^r#RV"Q'Gql:.l9@X:g.CH'Q\JFJ;fqmXgl-RX2DoH
'*\^L%1<(=#6b54!s/N)!U]se!U]pl!<N?*!WiE%!!``7Du^CM#6OZ#quHp%!WrK*q>pNprW3-(#6=o/
!&kVj!!EH.!W`?!!!!'!!q66Y!!!&t!WW8u!!`u=SfSg`((L6H!X&T+qZ%f@!WrQ0#RUtM&.oNg'c%Q$
'b_,h)C?UR;1p\-!!!$$!<C[Nr;lp"rW<3'!Wi/u0FSGo2a',_1b0pu*#92!%L`aT%1a!_'c.f1+snfn
1cRT_6qC*T>@;2cARL"_3s>N_!<WE$!<3)t!r`8j!V?@!!<E6'!sAc2"pP2,!&Y?*^JA$6>#7XQ4>\T6
)\W\j%M9Em*$H[^2Es`1>@h\oH@LX3T;]!*^TaQIem9'l"pPA>rW`W3"U"o/!<Mfmq>gKqmJm7g!r`9&
!Wi6""sh#&#65&3o`,0s!<N<)!Wr6"qu@$(!<<<3!!Wn3$iL&-!sA]-qZ-WsrW;QimK!4e!!<-#qZ%',
%$i%](`<ee"9\f.!W2p-!<N?+"U55>$k<g\&ebrX'FPQe%hBX/,:?c`!sef*rW1[PrrDuuq?$Ztq>`/[
UcCe)5;t2D,p+!?'+bZa%hK?e'c.c/+XJQh0JtjR5t+CD=^>KOE+3()XUGC3!<3)u!9XCU!<*#u!WiH+
"9Sc1"9SH#2$+Z$9j:Y%;+O&<2_QO#(_[Mr()e29,UtN/6;(9`B5`!BKSu1lXL#OPXIm#P-Plac!sSu.
#6Y25!s/Mi!;ure!!WH*!WrN+!W<!&$?HFR!"&f"!<3)u!rE#r!!iT*!!Wl4$Qmdo!!<9)!s8?"!!3$"
n,_tXquQNl#6RAN(CM2q"TAH(!s/Q'!<E6(rWEQ3"U>AC%M'*_&JG'V&J5N_%NHrK.>1n/!!!$$!s8VV
!<*#q!r`5s!#5`8Shhrc4>895,9@a>'+kfh',;<#(`OJ<,Ub2s1,V'U6qL-Q>$bZQD.HY@C^^.@rrN&u
quHctmK)t\rW3!"r<!-)"9S`%!$D\SX[kib<D#\F3]&B6*Z5e4*$6@N-nR8=78?okBQ/8;K8YqaVm!J=
\Z:tCN$/T0!WiN0#6tM>"p>#0!UKgb!Up*g!<`H*!s8W&!!EG3!=K53!!36(!Vufh!W2p$!<N?*#Qb*(
4TGT`!!<6'!Wi3!rrN$!o`>!mnc8Ofq>^Krr;[95"0F'W*t\VU!!3<-"TAK'"T&?D#71bJ%hB3_&ebrm
%h&gT)_!^$R2->6!!*3,"TneX!<3)r!r`5r!%nWg^I9J=4>SQ<-6sZP()%>r(E",2*Zu[T.k`V62EF)n
9i>"q?=IS^Bi_J_'`A%2!VHEm!;urn!r`5o!<*$!!r2p!!Wi,t1(G#A<B48_9L_<23AN*1+!)OK,pt,n
0fVHj;HdODEd`b,S"m$h[C<HCOPE&I!<<*$rWWT4#R:P;!s/Mo!;cco!V-6h!WE-%!s/N&!!NE(f)PdU
r;Zp#"pG,'!<*!!!;cfq!"&c2!!!K9S,`ir!rW/t!<*#r!qlZm!WW9"!;HQk!Vud0!<N6$!<iZ4:43Wj
"UP51!XK&9rWNB."pYA3"U##9$OmUF%i,`j'bq5d$kX=$7V>p-"p+f*":,26!SIJP!<<3!!r`5r!&"?X
%pkJQ5;G5R-n-Vl*uPh0(`FD9+<i'Y.P<J52E*]a8l8\n>%)#P??(U6$jce3rrVclr;lQmp&P*nrrW*#
rW<*#rrDor0*`/&TKZ7E;G'5?5WLPK,pale/1iM12EaK(='fEQF+B7<UT(B'\Zhm5\!&*R"o\N$"pYA=
#6k>6!WhWf!!<*"nc8Of"p+i.!!!'(rVut,!;lg!!t,D<oDnjk('"=8!<N<&!!Nc2!!I4B!!39)!!!$#
quH`tq?$BlqZ?cup&P*nrW<*#q>_63!rr<)%KHYCW#?]W&Hi(9$OR.E#:9Z\#RCY>"pG5<$OmRU%hB6c
()IMh%i-$-=Gddm!"9&3"UYJ:!SIJQ!W)ru!VZR5#lkAS]f/;+68U,B0.J.d)&XA7+<i$V-Rp]&'Jq^,
3BT]'<Ei[2@VB+OI%MMa!!rQ(rrV`krrM`np&G-p!<W0$rrW0#q#D`F!"C*j6W6*M9gM*75;t;J/1iM1
1Gq*Q6:t-Z@:sJ$K92\'X/lW8\uM7-bsE?S$N:&)"pP;<#6k;5!p]jd!r`5k!;Z^"!WrE&#7pe6"2Y$<
!WE'$":Y_BoDnmlrW!K1!X&Z,!!a,:"VJi\&c`.:!rr<&!W2ot!Vlfl!Vult!VQKn!W<'"!Vl^5!<W?&
"UY;6!(;bU*t&2T#7(VC#mgkC#7(56*si8]$OdIS&/#Wk()IVq&K;`XI7OD>!"&o3"UPD9!W2rS!<3)t
!ri;p!&+WZ$3O>*01RrU0.ne),p=<M*ZlOM,pt,m/hf(=3'9Gq9iG.s>$Y]EEh$5=!!!6&!!*-%nc/^l
!<Voqp&GF#!WiH+"9S`-!<Mop0EM4]"^J5o>"qLV6pX%!2`*<H1c@<S4[DS5<Es$KEdEG$R\QaYWj&.u
c%%2U"U=r+rWNK1#6k>7!WhWf!WW9'rW2Bd'`e=:!s&B)#R:J4!1O&j!WW3%#R:M&!!!'!!XSr1!!!'4
!#.3rrW!*,!rr<&!W2rt!W)rm!Vult!Vl`q!<3)u!WW8r!"f85!<WK-!WWCU;A(8^%LE@GrX/]4rWa2E
$4I@Q$k!CN%MBKl()If))&OMP@#t9e#Qb27"9o)8!s.'TrrN$!!<E2o!&+HW#6bg/DDOs?1bC.)-mg/^
+<VgP-7LJt0/,+<3Boo'9i4nm>?bNKLoCX_!!*/g!<3)l!qlU#!<N<)!sA]-!Whup0E;(V"rEqY6XN8R
6U![u5!1kd3BKAh6qC$M=C,QUG(5:-Q(+A=TVJ9oe1)FK#6Ol)#m1;5"U5,5!s/Mh!<3-"!UKdg!<E6&
qZ$g%C+92g!!!-%!s/N)qZ$TsrW<*#rW!*&!s8T+!WE'$$P,5;rW!!#"9\W(qZ-*dq#^QspAk3or;ls"
pAc$2!X/c.!#5taT0!#j#6thN#n%.K#6kD>+Uenp&Io0U$P*sj(DIf5+sA3\0TnU#!!!'+#R1J:"9JVW
!<3)u!ri;p!"o>9!!"#X0==h&3[cC2/gi"p-2o(i,q(;B0*Esd3^ZLI8Ou]_>$>0;>I%-7rVus%"7?-h
!V?En!VZR#!<E6'!s8Z.!Whil-lj<c^LT#m4?Z/%5X@_%5!D4u7S?NU='K'FE-m:nLQS'pR@0D%h0'>W
&I8LA!<<*#!WrQ/"Tnf,l2^hcrW23_rW2uu":"tY"pt8/":,&/!!<*!"p"c."U"l-rW!*("T\T+$N:#.
!<ASk"TAB'"pG)0rW)fqncAOfrrMiorrN'"!!2cn3!'3d!Wi?7!*#<k'H.N&'+,'U$3pb?$4[[`'+YKX
$P+!m(D@oC/hK@LNGeh%!!!'-$3p_:!WhupirK)[r;ls"p&H]G!sJc2!#l/SX<9,R/NGO7.P*"p,U=`e
0/>:;0JPIJ7SZNE;I<d:De#u+&.SU=!X8f0n,WIhrrW0%rrW-#rW2`nrrN-$r<!'%!V6:E!rs>MD7D5`
83p$C6Uj[=77B[;9i>%r?!h,XFF]7'K8uCfPG45nW\#G&"Tno1r;[!%!sJf0!U0Ua!r`5a!!30("o\KL
!XSk"":P87%Kc\2!s&B%!<N?+"U"o/!<<*&"onW-&I/:E#/:ufr;Zp("p4o)!<3)k!;urr!r`<%!VcZo
!W<'"!VHEn!X&E%-NX8QBoatX.2*7'%h8pO"9Si9%h]E_#mUbF%MBX$,q:;o6][68(B+:=":#,6!s/K(
fDtpPr<!!"rrDfo/-?"V!!!<*&pL!;,XO.:0etO=/1Dts/i#=C2)I0N5!qh8;,p[q;eE//*$G4\!WiK+
mf<@grrW0%quZftpAk3orrW-$!<N;o!<)sL#lkclXAh&X7nHHR<E)gk:Jk.s?XdS[Cik&VLlIIWNeW.J
e&F=)%g`CA!rN$%!<WH-!WhNcrrW0#k5Ynl"98E)#QOuI8e_F/!t>G7!W<#t!WE'3!<E6&!<WE*!!!0&
!%25n%KHS0!!39*!W<#s!V?Bj!W<)u"9/Ds!<*#t!WW8o!!**%rW!Q7!!!Im<&6NX&Jl&i$O?k9":,nS
%LiaM"pYG=#TG<D-9Oh)RfETl(CL9G"9\K$g&V-Rr<!!"p&Gp2"98E&#QP&CSmk,a4>8fV3&WTI/MAn=
rAk*D5!hM#;@[&8:LIgYXpP[>(^g<D!Vucr!VQKp!<E9""8r<"!VZTo!WN6"!s&H(nGjsC!!sUBDcL=I
9j:n1?X?r>>@1oSCN"9<IY<E0Pb!qhNfTRN+X-q3!>5P2!!E?+!s/Mf!<3-"!TsFo!<N<*#n6q=%p/l;
#RLhF"TAB&!<WB#!!WH+"9\c+!r`0-!X(3d&c_n?"98E&qu?`u!ri?%!VHHl!W3#t"9/Dt!;urs!ri;o
!!E<&!!*0#!!Wh#J.<;7#Q>)H#mLM:$4RLR#RCbF$j[1U-R:<.CR>P0!!Wl="9S`-!W<#t!VcZU!<*#u
!r`5q!!WH+"9JQ*"9&9C%\o",/j([B3]oJa2`a)f6U<q'7S$0A85EAa;Hn^M(&e19$jQh7!Vufr!VZQq
!<N?#"9/H&!rW/p!<*$!!rW3&!W`>m!!!'!!%&G`SM`oA:L7XIC1q3nD/jZ?G^bC+OcPTgR"p<IUVS>b
#m_.O"8Mp"!WrN+!U0Ua!r`3#!U0S$!<N?+"9o)2!WWsQ=qV,E'F=a>!X/f3!W<!2!s],="9So>#QP&P
O9Q3q!"&r+!!NB)!s8T*o`4slr;um!rrMoqrW3!"rrW3$oDgTI!s&B,%0-A=>_OXI,8:=f%1<FK%1a!Y
#n.=U&.TBj0Ju.<Jfk3s%0ut9"U"o/!W<!#!<N9&g]7<SrW;osrr=kU!!*-("U,#0!!N]0!"rk-5WVD!
2EO5k5XIn18Ol3@:/=Y[:eb;%@#C'o"oo#8!!!'%q#LBpp](?r!Wr9%r;uoup]19orrW-$!WiB'nGiOl
-jfqU*-A,_=_h\\C3"?6F*;eTI"$g1PEqN&OdqPnY,sc!!>,Y?!<Mur"T\]-!W`>e!<3-!!U9Xh!<WH.
"9S`(!!iT5!3Q;2$NL/1!!NW8#6Ol)'`eLG$k*FK!!aPFKg,PG!#5kD!WrN%!!**%rW<3'!WhuprW2s!
qucs"q>gHpquZiuoDf@%!!!$%#7^_P40E0/!Y#&7#7CnH$k3a]%i,Tj+t+Q\&o4%I('"=9!sAW+!s8T+
!WE'%!<E6&!Sd\S!WE/s!W<!%!<N?+"9\T&*s2lN+@j4r0d\e:3''2e5X@e.8k)3D='SU"3/P"`+8l0A
!<<*#q#L?op](?r!Wr9%r;uoup]1<prW<$#!WiE(mf4U;&-sjjesTB-?!h#OBPD3tDg$MTI#4,XOGn"a
g6"<%#R1D7qZ-No"T\]-!W`>e!<3-!!U9Xh!<WH."U"o(!"/i8\gIX]!!a&C!s/?#"9AQ,%heg@$m;u6
%0-tH#mLP9!s/<"#6=l."9S`-!VQNm!W<)t"9&>u!;urr!r`5g!%J*W"s+CsUIYIk)]04u$4.(U*ubq-
'/276NK#b%!!N`4!!!'%!<N<'!WE'%!<E6&!V?BV!<*#t!rE#s!!NB)!s8T*qZ%]C#ppaH\mls65s[[r
3&s)j:.[`74&o<nVP-Bm"U583!!!&o!;urn!!30&!rN0!!r`3#!VcZp!WE0!"9/H&!Ug"6"qMG+0ppF>
6:kWq?sQu@?Yjn,DJX-ELm??,@kJW6'*eL;!quZu!<WE*!<MHcrrW-"r;c6c#6=o0"U,#3!r`0-!t#M<
!->OJ!"B;?r;[T8!WW6&"9\c+#EH%h'`\C=!rrH0"p=c'#QXu.!sA].!WhuprW2s!qucp!qZ-QqqZ?cu
mf3Fk":582!#I>[T4&EH+<i$R*uZ"<-ndhPMmRR+%1`78!<E8s!WN6$!Sd\S!W<)n!WN6$!rDs!!=/o/
!#Io)[<jS_6V'jC8jkp38PNDlT>Z9\'bg':r;lZn!W`?(qucm!r;lZnrrN*#r<*'$rrMTh!s8c>&L%Vh
&5pHiP"82M@:a%^@:!GZE.<>TkFiVC.0p:f"TSN(!VcWu!<WE*!<MHcrrW-"l2V%j!sJl4"9S`)!"Au6
$NLP;!1/cl"p#5A(^1-P$47:Y!!3@9dNA\o!WW?'!s&T4#6Xl(#QXu/!sA].!WhuprW2s!qucp!qZ-Qq
qZ?cun,O@.!Wr]:#mUe;!AnqrHpTJ4+!)OR4&g`uN&Ck?!#>P7&Hhq2pAt9qrrLmTrW2s!p&Y-orrMus
*X3#\$P<[S6AE+;?;=$Z6UXLJCm:lb4TPO#!!!W6r;Ziu!Vl`n!VcWr!<N?#"8r<"!VcZp!WE0!"9/H&
!V-4=!<WH0%M]]o*>TPiQ-6%D?s?]7=^Q*$Xhq>E)@eD3&L%ee!!36)!VcWu!WrK*!<MHcrrW-"l2V%j
"9eu5"9JW'!WrH+#6Ol)"Te[gi.r$D!#,J;)J6\A!rr<,!!!<-!!!0.#mUS1!!iT,!sA`/!s/N$!;ccq
!W<)t"9&>u!;urq!ri;j!!NB)":,>8r;[B9#7`b,J<,kUQ^<VP6P]Y2rW!$$#S."7!;HTo!ri;i!:Bjd
!W<)m!<N<(!W)j!!<ri4rW!N5'c%ofJXs!P[CEW@M,PT!&H2Y3!=')8qu?]tq#L<np](?r!Wr9%r;uou
p]1<prW<$#rrW3$nGj^6"UGSN$jd1D%j</L?')2(`lH9E\XmIo(aft)'+u-&%fQG0!<WAt!<!!!!U9[b
!rW/t!:Tt7!<NB-"pG,3!<N<'!!N]7"TSN0!!*35-!chE_RQ+P3=Gm*!!3#u#RLS5!!<H5#6Xl(#Qb)1
"9\f/!WhuprW2s!qucp!qZ-QqqZ6g"!<DTh!s/W3#lO`'!qH<s"TSN)":YnO!rN&n!WE0#!Sd\S!W<)m
!WN3$!W)j<!X/f0!!!00#m:55%LE:M)]05%&Hr.B!!*-'$kEdD!!!&q!;llm!!30&!rN0!!rW/p!<3*!
!rW6$!ri;k!!NB,#n7CP'EnaQ'bq8g'ce/-+Y5,j-RK`@+V4Pf"!/O&%K-8-!s//sr<!!"l2^hcr;l3a
)?BmB"U5,5!s/K(!!!66$j[1J#6b>C%13:A!<`N(!!Nc9!!!K0rW!6-#Qk&,!XB&<"8i-#!WrQ("9JZ,
!VQNm!W<)t"+U~>

%%EndBinary
grestore
np
grestore
gsave
44.6254 410.531 mo
86.5824 410.531 li
86.5824 353.277 li
44.6254 353.277 li
cp
clp
44.59 353.19 mo
86.61 353.19 li
86.61 410.61 li
44.59 410.61 li
cp
/0 /CSA get_res setcolorspace
gsave
clp
[1 0 0 -1 0 570 ]ct
[42.02 0 0 -57.42 44.59 216.81 ]ct
snap_to_device
Adobe_AGM_Image/AGMIMG_fl cf /ASCII85Decode fl /RunLengthDecode filter ddf
<<
/T 1
/W 116 
/H 159 
/M[116 0 0 -159 0 159 ]
/BC 8 
/I true
/D[0 1 0 1 0 1 0 1 ]
/DS [
[AGMIMG_fl 116 string /rs cvx /pop cvx] cvx
[AGMIMG_fl 116 string /rs cvx /pop cvx] cvx
[AGMIMG_fl 116 string /rs cvx /pop cvx] cvx
[AGMIMG_fl 116 string /rs cvx /pop cvx] cvx
]
/O 3
>>
%%BeginBinary: 1
img
jT#Da!WiH+o`PL'"U5/7"9S]%!#YhA"U#&9!!!*2&f2/c"U,8G&.]Eh&ISpOqu@$-!rr<&"UGA;!r`3"
!UBa_!;?Nn!rE*"!ri;i!!WK,"9SZ+!r`0&$4dg^"n;R!#nRII!W`<'!Wi9#"9AT."9S>urr`6%rrMZj
q#LEqrrW0#lMq=r#RUtN&I&4<$k3^Pn,O()%1*+="UGJC#Qt//!s8Z.!Wi9#quQTnncAIbqZ-EmmJmIq
"U"i/!WiT)!!WT2"p+c+"9&9%%LN=8!!<9)!WgjPrrN-$rWE0'rr`6%rrWN0"9eu6"Tnf,q#D96"U>88
!!3?4%L<FQ)DtN;ML]D>4=V9`%/g/+!W<#t!W2ot!TF+U!W3$!"9&B%!V$0f!!E<("9er,!!*-)rW!?2
*B7#1=[Fb^&I8RFrW!!#"TnT%!!3'!"9JZ.!s85trr`6%rrMBbq>oj]"To#=%hB!I!Vl^'(Go!#=[Ok`
&-`4<r;[0,!<<3)"U5,4!Wr<&!!;orq#L!emf<1bnc/gp!WW6$!WE'&('ss@&HMe1$N^D4!W`E($31&-
"oA9%!<N9&f)YdNrW<'$!<N<$!!rZ-!sAc3"p=u.rW)s!qu@T;"pYGB"qhpc,&sdEj42&T^<PKn_3.kI
"p5nV"9R$Pq>pEo!!2forrMusrrN&u*!$6K#6k;2!snr4;2VlmV3$1]Pc1jQD)`"*&Hqk/!<<0!!r`5r
!;lot!U0U_!VcWt!<N?*!VQL4!XK/A$3pP5#QOs$L:+@^Ndc\HVm)D"1^O-hqu?]trW!!#!Wr?'qZ6a!
quQQmp&X@WrW2Wk"9AZ2#6Ol)&-`+;!%b%bBKdFn>a)L:-5$1V"9Jc1"9SN%!W`?(mJuJOrW2s!!!2rs
#6=l/"U527!r`0%!<WE*qZ%Z=$P!mZ-]m&bSqDWIF(]]QH#AJ=c-sNo.ME%#&-;G(rW2Wkr;lfrq>g*f
q>^["!WrQ/!rDut!W2p?!X&c4"98[@XEnDH5s?e>/3P^;8ogAuS0/@C!!ir7!W<!#"9S]+rW)ouqZ-Nq
r;l?en,NUm!sAc3"7lL7!X8`/!!d5>HXoT34XqC#4"_mMD3UZW(^pBE&ebHMr;[$)"9S]+!Wr?'rrW-"
o`4jimf3@h!;QWo!VZR/!X&Q)":"r-!!302i&2>Z(B=F9"pk2.$l*Htf`2<i!<<6.!Wr?$!<WE#!!!&S
!;lln!!E?*"9o&2"9SQ&"p+o2"9JW*rW!uB!#-l8goQ$MEcc8>KU%FBK84DNB8*GRc#FO2*!c0;!!3'#
!!2cnq>p<jquQ<f"p+l1"pY83quH]s!!<3'rW"&F!!NsCY&ur],U+0F.QT4,.l8C^,=ZddUJ:dh&I&ID
rW!!("TnW&!W`?'qZ-Kpr;kgV#6=o0"pYD;!q?6m%:?8^(dg)-,oddO2_#dm//\d54DD$l:]h"B#mL8-
!X/].rW*!#rWE9)!Wh'V!s&E(!Vl`o!W2p9!<E0#"q(M5!!NB2!!.9X!WW3&#S.:H!s/W+#Q4W/#&mZS
!"]SH"pY&,!<`N&!;HTF!!E?*!s&E#!<WB*!s88u)](-FhJRseH[UL"Lk^S<Ljs]/SsG4SH$dlo4p)6J
$Np,'rW2]mq#U3irrMNf!!E3'rW<-%rW2`n*srgXY;8<c+s8*W-mg5h/LD]%:.[`)4@Z*X,lf;!#6"T)
"U"l,rW)ouqZ-Wsq?$Zti;`u^"9er3rW<6(!<N>r!$2T=X>E0k.OQSj,p40J*YoD<5<C\I0fY;n%KI@H
!r`0-"U+u1!WiH+"9S]+rW(jV!W`<'rW<0&!W2rs!VQKo!s\](!sSmA?2=O&!<WE#!"&c/!!!FMGQ7^J
"TAB(!<WH,!W2ro!VZTV!!NB)!s/K(rW3'#rW!-'!WiH,"9SK$.0]hm9C90"IpRGJH?OXdK7\AhH@pm%
I!9^OF'XXdYTjc!!WiH-!s&Gl!<*$!!r`5r!:'Uh!<WH,!<<0""9JZ-!Vl^<%5c4`.l[nV'bLli*?laM
)C-ph/h8>!-T!5X`g.,;&H2Y1"9\W(p&P$lqZ6`uli?n_$NU;1!<N?,"U"i+!rW9'"9S>u&LG/A-o___
*Z,J&()@Pj!XfeB(^qB&*X4?_C]FGH!!!)t"TAK(!Wh-XrW*<,!sAc2"9S]+!<3'!!Ug!n#GO3Y$31&.
rW)s$q?%?5#64r@$36_Y!"&]+"9\f0"9SH#rrN'"g].N\"U>89!s8H&rW!$&!<<,t!#l"G$kasFhj7;p
J9P^bKR\Q+Jq/5oI"6j&IsV*D%WlQ<b/%$h!sAi<"onW)nGrRir<!!"k5Ynl!W`9$!<WH+!!<H/pAb6t
(EFR2C)T2c(B>6`%hos)+X89]/1rS*,qCT)0euLrSN$KI!!N9$!<WDt!;urq!ri;b!"T)4"U5,4!sAc2
!WW?."Te>t$j$[7>7`bF*![Z*&J,Tf%LWID#7D%T&.TKq+;u.UMi]Xk!!ri3!!3B0!s/N)h#ITZ!<N?+
"o\]-"U"o+!WE'!!rW8u!"8l@"T\Ue%1ECD!!*3"!!iT,!s8T+!s8Z2!!!0+!!$1oqu?d%!s/2t!!<*$
qZ-TrjT#bm"pkVB"Tnc,!WW3%"TnZ'(^^up)%6j-BX-TGCgUdqKTC\<Lk^M4It.HH%XibTJ9l?bJ8&(g
Rb(:L"t:)q"TSN)nGrRir;us!kl;.n"9el/!<<0(!s/W1!r`0O!t,PH!!"$9QGQKU)\s2/*!Zlc()\/<
.5!5(.46Ml+WVm`*toZ+X!n#[!!<-"!<`N(!;HQn!W)ou!U'Ln!<i]7#R(>5"9el/"U>//!#>_I$jQb4
%6T-?4<tIL(*Fn9',1uc$2t/K"pG/7#RUb>(+C@F,\a;+!"],6!!!$*#6P#.q>fRV$ipA1!X&Z2"pY>:
"U+f+$ig8.":,>?"onW+#Qju*$3gKF`"rCR#R1M9q>^[#!sA]-!W2p*"98T*'USq%$NLD4p](<r"9&H#
!<*$!!9O80!WrQ/"pYA7!!392&Io-V%gN@g=g%>HWJ[-E?X.GiJqei0L4t5/IJeI*I=Hj"Isc^!Kk#7R
cCQ!b-PZdQ!<3)u!r`5r!:^$u!<N<*"U5/4!!*-+$O-G./.F_'d^4^;DBU/:)Aa>.$kO0l*$?LU/M&A!
,pjub+sJEl3Z^4LSok#5&dRn+rrMuu!!2`m!!2lqqu@0-!sAf5#R:G3!<NN8#Q=`B!!!KiM9)Q79i_Z6
#8.^j)\Wl!&If'Q#6tJ4"W.LP$4IOi1Hm!C7@S>u!#,b?!!EE,!s/M]!!<6'!X&B("9S`/"9\T("T\W(
!s8W(!"oSB!"/c,?-nri(CpoS#7:Y@!r;m#!<WH-!s8?""pPA6'aW&1oDf!q!s8Z/q>gNrn,WFgo`,F%
#7:kD!XB/C%2^E=1`(_ef?'k;>>\1p>[V#]G'\OcJV&H'I=(s='mb4SIY!0,Jp_WUE->9/nr+_4%1NC-
!<3*"!rW/^!#PkG$O[(;!<`B&!t5DG=eD^_G"aA-*-35J*>]e:(_dVu)BBqF,q(5m-mg2b,pjuc+rqUJ
0,6df@/pB0"8r3$!WiDt!<*#s!ri;q!;lli!$_UP$O[%:!<iK(#8%C]@&L/sE^UrZ#[IiI#o+0j'GV>s
'+c,n$OI(E#6tMA%1s9i(DRZ,/.t.\@/pH2"p+c*rW<-%m/[+dpAc$3!sAc3"p=u.!!!$"!!*0'!<`Q/
!WW<+r;[=:GZ,Fe!<i]8!!EK4#mU2*"T\Z,"9\i+!;lg&#n[@AK)bl["8Dir!rW5b!!NB)!WrK)pAd2U
$46k9!"^Cb!%`!"o"f`_<F'BUG&bB9BP2I1G'JFaIXQWjG^"=SG^4XaIt<3'IW8q@I;EP@hZQ%a'GL]=
!;QZf!<3)r!($\d!!*92%LW=<!!Eu9!"),S]n\cp'HAVS2_ot6*uQ:E)AsJ7+!DmU-7:2h-6sf[+X/*T
+r:b5/g;N'XV1^8#lO`)!X&Q)!VcZo!WE0"!VZTo!W<'"!VZQr!XB)>rW"&D'EA+D9:!S[7jo2n-6al^
D\`ik(DRVu(`*r&'+k]`r!O>M%M9?i(C^Tf.30NlX:kX8$NgA/!X&W.p&OmgquQTn#QXu0"pYD>"TnQ$
*<ZZT#QOi."pbS="HpQ"!!!'#'+"dK&.J[F#mUP,!!WH*!WrK*!W<!'!<<-#!!<50o`,!n!r`;l!;QU!
!<N?+"9S]"!$M@K%134R(CMO1^<![18kr`*C1^p\B5"npF)Q5CEcueVrd#K-G'.nLG'J=[I!g?jIt`]'
DKM7cUA#NJ)@HECrrM`lq>p3g!W`?'qZ%uF!!!*/%hT-K%1*"C;ja#(63dZ+(E=8,&fi'7,psf]+<;OK
,:"T6-5RsS,U4HT*ZZ4@+=Jfa(a;X+Bup>\%0le3!s8]/!VZTn!WN6#!VZQq!<E9$!rrDu!%@mJ"UY\C
!"&u3%9B!lLIr-i*$6:@&df6_@1sCg(_dSu)B'G/()7Jpr=Ai<'bM)p*[DR7*ChSl`rHAT#Qb#."9enr
!<3*!!WW8s!!iT-"9o):#R(8+!!`]<%1NLU!tGD<C6'P;!"B,;#Qt,-!WrQ-!<ri5o`,*q!<N?+r<3T4
"9JZ*%MAi2!!i]0q>^Krr;u6a#6=i,!s8Z-!VcX.!WrH'$OK%i_5i#h6;:cn?!UcQ$[HQ(CVOh/DK^&>
Fo6P(H$=FSFa&(VH@(!dI!pU"I<0"7A#&%#+:o%]!!*-%o)SRep&P'mq#CKt!s8W'!#R,;TS-/j#RqXc
%L`gd.30BLE[)hN,p=<?+XSQ`-R^>h,U4KV+<MXErYlLk,:F]S&JuL#Yt,*#$3L;/!X/]!!;HTk!<*!!
!r`9%!q?78."n:L<%JLm+<)%-%iQ].&J&:^'+Pcj&/?*%)&aA0(DRVtq%FDU)BK_-#S@e\X[NEq$O-_7
!sJer!!`N*!WiH+!Wi)s"p"f/"U>88qZ$s)!WWuE!!"j?8.#7qrs8T(!W`9$rW33*!sSu4oDeso!WrQ%
":>/0!"8i/EWuLJ"8W#t!WE/d!!!'!!r`9%!WE'S!WrE&"UkeH&./n>W5sci4[)SH>?,$EBOt^b@;Khs
DfBN7EGorEH?spbH?j^XGBeE3H4P@KH@:<gFGZE:BpZd_#7ge:rVus#!Ug$d!VQKn!WE'J!<N?'!!*<.
!!<3$15r,A,S(7u,8q.0*?,e0'bMB*E$$/@,Tn0R-n5-D$77#B+<M[H*?6";rYcCj+rhIT7Q2f-Sd,6&
#6Y#."p=c'q>g-grrDuu"9JW,!s/B$rrN*!,Qn/K!<<*SN2U;7&IfR'*>BA5)\`hm#7h;O%LrgZ&.T?k
)B8Yq!?)jT)#b?N().Gr()RVn-9Ee'?C:rs$jd+<!sShs!!<3%!<W6&!WiE(q#CR!!WrQ/!rN$3!<`E'
!!HEc%g)q7"pG)/!<`Q/rW!0)!<<3*"U"o"!;urr!Y#57!!!')!<Wfl!!N?'r;Zj!!;lla!!30&!r`9r
!WiB&!!*3,"pkYD"q2)7[]XOA4@)8%92SYi>[LfD@V91dDo-L4C3"93F*MtVH[L0dH$FRZH$Xa]G^+L[
I=HTgJVJDgGh=#L"p=i)rr_Zhr;lKi!!*-&"9\K#.kI!E80JHS%1Nj^'GM<!'b_<"',qs2*Zc1C+<Vs[
.k2tr-6jWS*?6%<)ZCTg)B0_@*?6F^/MKSs!<N9,!<<0+"S;]_!W<'"!WE*!!r;ls/-qT$8g=lZ%Ls*M
',_Ju&.AsW#7V/M%1EIQ%Lj'h)]Tn@+!)IDrYudp)AsA/()7T$&e>m++=0.L!!*--"98N/"7Z?t!<E6'
!s8Z.!Whro!W`?(r;[04%0-j=L&_8T!"8c+!!3-$qZ$j&"9er5"p>#,!WN6#!W)lr!W<!"!<WK(!"8u1
!XEfI"TSf0!!!'!!;urb!!**%r<!r>!W`9$!X8r@((_N85GuhP4\&7B92Sel<)rlt#$>5F@r$#$$#slt
E,KQ7G^4W7Hi\S?rcnisH$OXYG'J=\IXM-?#B5!!fbbb1!r`0%"U"i,n,W@eo`,$o!<W6'%gN(?%3L8%
:(S3\(_[]*)?(?b'G:rg'cIc)*,lr>(a'qE-S-eu.1%CK+s%^C)B'J2rYQ@f)]g+C*?HFN3A.N9%0-P3
!!3E0!V?Bg!WN5r!AOWW!<E0#!<N?+#QP/A,)3-q&fMf0'c7o-'+kcb$4$hC%L*:M?k!JI%1E[Y(`OJ;
r?2@f+<M[H*?5h5)&O/,(D@;i',<&CVuR2*#6=f+#6aPs#lt&.!WrQ.!s/Mq!#5P>#7LY:&-+))!!!E-
!!il>"p"c,qZ%*."pbM@"TeZ(!WrQ.!s8H&p&G-p!sJT'!<W</!">e+"TT#9!!!&]!&XcY!sAZ+!sAZ*
!sJo@"q;7dNp:j4-Vm8q6qpQZ;GU.h<``C,@;'.dDo?X6BQ%d+Ed)eSrd4Zkr-8p"GB\4SH$apbG^"CM
G%9GJ(^0d;!!N?*rW2KgrW2]m"p+c)!WrK/rW"DKDoPTR!$2gX$P=*h'+YZg',2&l()mo))f?Z8(EXbC
-S-eu.46Aa*?4tqq\U"b)]]k9*$HF]/[k]c!!<3$!XJu2quHKlpAt6n$ipA1!<<-&!!!$$!=&N'%Kg^l
;ZHe@(C(?]'bq;grX9JK#R1VG"q(iH$jm+G$k3gd)]^"Cr#m"%+<MXF)]BS1()7Ai$kX(!,Hq.P!!NB'
!sf&!!<3*"!r`9&!Whon!<NH(!!<<B^^U)?!s/T1!r)a,!sJl6"pG&.!!36*"9S]+!V??m!X&E%$j6P1
$EX:3!"K/4!!2orrW2Ee2us*a!W`E/"9AZ5"W%pm5LYic69@V076j@>;,C"^:fCG">[:fQ@r$##E,K?-
DJjK=G^+L[H$T72rHA]qH$X[WGC+1IC?-9E%/g2+"T8Aa!!iT*!!*3'!!*3V!"/u7-FRq9(_.8u%gNLU
&eGK\%1j3h'bhH'',VX))]BJ6+!E!_/1N%o,9ImD)?(KM(D@W'(D[r6*\T=\!!!6)!!!*,"Te,nqZ6Qo
"T\Z)!!*6%!"/l/$O-e_[r`c3&/QH.&I8gZ&Io-R#RUtL$OI1N"q(iG$OHqE$k3jf)]Tn@q]He!*Zc=A
)]0>)'+G9W'+cB;ZN't2"9JQ*#R'SrrrN'"rrMoq!W`9$rW*9)(^UY90)tt_o`4jh!<E<$":5)/!!*-'
!s/K(o)SdlrW!?3!!!7u!!N?2"98E&rW)s!rrDuumf4j=!X&T-"UG>;%2Kim&:rb;6S:,Q5t=C69iFtg
:f(%i=^><>@qfIhDo-H!DJ*m)DK9rGGQ)jaG5um`G7&J5FE_VGCZ-*@%K-8-"9\N%lMrgD!WrK)!sA]+
"Ukh?!,0;+*sMoT&/#H]&/5ci%Lip]'c7]#(E*r()Jg<1'cnG>-7gYr-6ra<*ZQ%7)#>'J((h5o(EX\S
1q*Gb#Qau+!sf&2jT%1>!W`9&!s/H+$k31:BuMnP#RCbL'FtWa'G:l`#mgtK%h&dR%L*:L?4.)C$k*RY
)&jM7*?P,#rZ;(['cRu)'+kTX$4mds/$T'S#m:;0":#%r!;llo!"T)3!WrK("on])!Sm_U$j?J.!s/Q,
!qlU"!<N<)!W`9%!WE0#!V-3q!<E0#!=/Z*#m?Xr!<<K1!!!'!!;HT`!&=TX"9f#:$P!I]&1#Sg1H?p<
4A&%,7o3/c<E)mq<**7/?!_#S@r#u!Df'-)D/F<;GPlXaFoHR]G7A_=F`VPCF`2S@h%^G.r;Zj$"8`,c
!!NB)!sA`/rWG+_!"Ao>[sSl*"9f8R&df*_()@Ss&J,Ng(E"#((E4#))Jg<0'cnD=-7^Pn,pFEO)]9J/
(Dcrc'G_Dt'G:ul*$@0rZ2ak0!rr<'#R1)*rrN*!mJo0H!<<-%!sAT5!"l_h()I/[&0)>j%MTWm&e>EZ
$OdLV%13LS#7M&K$jm+H$k3jf)B'P6*$$(!*rI#n*#KD'&.8^K%hpTHXT/>-"p4i.#6X8lp](a(!WrN-
"TSr2!7aaW$N1#(!!EE3#Qt5&!;6Hc!<3)s!"&`4!!!%["98E/"8`)s!WN6#!Ug!g!WE-S"ptJ5!"qE)
BKJOB2).0a76sIA<*!!t;GpFn=Bf!7@:s%aDS^7.B5VR'Ed)_NFo6@\Fnp1gF`VPCF`2P<gCju(r;cj"
q>p9i!!2rs#lt)0"9er2!WrT)!!NBNThHCI.hi?n$Pa0X%29Nl'G:uh&el-"(DRc,'H%g+)As50*?QRW
.4-8^*ZQ(8(]"m]'bhAt',)-&+?)!Z!!!9,!<<3-"oA;u!Vufo!VHEm!WE'1!@X[:*?c1-"Uu7Z#n7O^
'-7\p$jm@N%M'!U%1idS%U]_R"UtnN',_]+)&aD4*<$uV*#0D1'b_/f$4@F\/h*n&!"&o5!!EN/k5Ybg
!!!$$!!!*)qu?eb!!r<!"9\r5!Wi)srW)`pnGrRiqZ$X!$N:#/Mu`nY#m0u(r;lm!rrMHd$N^J>!"pc9
Z:$2b/H.U85=S(08l/Gd<)W]m&5uS2=BT!C@;0SoDJa$(D/BDrGB\1Or,_jZqK33iG'%eIGA_S7fFSAs
r;cj!rrN-$qZ6NnqZ/q^!!*0)"U,#2!WiN*";u3I-OKhW%13:I&.AjS&JGfj&J,Ne'GhW(()\,-)B3N4
)AO85*[E0^,U"3K)Aj8+!#GAF&f)5t'cA/<2(u-5!!`W-!!<H/qZ-WtrW2lr!W`?(rW2Wk.fpQ-ROARE
#S7FO%1s$U$kO!^%L`[N$4@:Q$jmFT#n@JS%L`OO%1X$h)?(HV)&aG5*$"qs"rnU%)&<r#&.]3\'c/DL
WrN,+#6b)1"p3ugr;dE2"98E&"onZ(#\seJ!X8i)!<*'#!qcQn!WN6"!U'La":P2/!/UUS!=8i*!;lls
!ri;u!;cfp!&joY!!Wl?!!"<D]i-"">;\H$4?u;(85)iX;c?Rk:f("f<E3++A70(e^i!t#DJa93GBS(L
EcM)!rcA!Z%s<#<GBJ"NH#7P:cjL6`!r`0%!Wi?&rW<'#rW2lr!!3'#r;dZ8!sJo4!=92?!!!`tUc&2S
1C=Np#RUJ<!t>eR')iIa&ebur)&O,-*Yo\7DB'Q0*?6(E-RBrY*#]\2()@Y_'`JgR(Dmr**$c[]2Q6TT
"UG21!XAl*!<*'"!W2rt!W3#o!!!3%!"T`,Uc/8V2@U0($OdIQ$P!(F!=TA8$5j3[%L`[R&IK$[@LinQ
%h9'_)&O/*()If*q\g7i)]BS1()7Gn',_T80VnaL!Xf24!sShj!!**%"9S`/"9\Q%!tF5i"8;cs!<N;q
!<*#s!r`5d!"Ar/!!Nc2!![`Q!!!9+qu?]tr;ls$rW<*#quHQo%0-A/!WrE&$5XKd%XZ;2-pK170KLdF
6:4+19MSA\;Gp@hr_O;+;H$S"@pWe`^MRe!DJa93GBS(Krc%jVr,NBjF*)PJGBS+RHYdJ=`s<1U"o\K,
!Wi?&!WiB'rW<*#qZ$Zu!Wr?%)$0jA"9o,6!"0JP!!$Z:$m#TX"UkA5$OR.>$iUV[%hK<b&ebro(E"&+
)BK\7*H)o:'ce87+snQX*?#b2()@Ya'GqJs'GM8t(`=20+=86_5G.uW!"/o0!X8c(!!!-#!WW8u!!!&t
!WW8t!#,GA#ljs:YRDTZ$4%.B#7_1M$k<dH%0$_7$5j3[%1<LQ&do6_@h9+U%h9*`(`4#''GVB"q\fAO
!#bbP&/5cn*#Kq^S,`Tj%gN(9"Tdif!W`?)qZIQ4"one"!!3H2(C'p?"Tnc,!s/Mt!<*#u!riB%!ri;e
!"Ar/!!Wi3!"N`P!!!6)qu?]tq#^Kqp])K>"9o)7":,;="p=pF^Gn5'/MT1F2*=5n6qC$J:f1+g;,R<h
'N%b,<Eis>B5>8"ChIX&DKC#FF)_2!rbqaSrG`BhF*)PKG'8.XD/4C.&Ie^DrVus$!rE#u"9/H&!VQL!
!X/f7#6bA>"9&9&?)Sb^rWb%_$3CG?#m^nK%h9*\&.oNg'GVH&(`+)4(E=H6*?,_6*$$4M,Tn'E(`*r&
'GUKZ%29Nl()Rr.)^-US/4Gj'!!N]3!!3?,qZ-WurrW3$p&G0q!WrN"!"rG2*#](h$4RFK$4[IO$kEgW
%/pVN$47.K$k3RO%MB-\&Ru@^#S.CT',VN#rY,AJ(AesJ)$h&q()@St(*".m,<q=i!!Nf9!!3<*k5YVd
!WrT0qu?_fr;[3,%L)n5!s/K)"9S]!!<3)u!riB%!ri;e!"8l.!!N`1!XW<@!!!3$!!3-#!Vlcs!W<'"
!Vud?!sf;E#mLqX#m_/V[n%i%0fM!K3Bf\q6q'[A:Jand;Gg<j:_ci+;cR(4?Y=/hDJWs(DJjN>G&qYA
qelCO"`SF#EcZ@%FpWJBDejg,)[cWJrW!$'!s&H$!!<?+!s8E%p])37#R_%F!t,\@!!6)l/I2ps%grXK
$4@4K#n-_B+qG1q&J>`k'c7f*(E4G4*$&r<)\jA5*?lgU+<;=:()7Pur=]t]'GVB!(`F;3+XeWg9T0&R
!!r],!<rZ'!<*'#!rW0!!;ca$!X/f5!!!$(rW!7!RjnUS%1isV$iUV@%1E[V%LijUq[45L%1<LQ&do6`
@h9+U%h9'_(Ddf#',2/sr"fk\(`=2-()7Mr&JZ6%,"%(`!!N`6!!3?+lMpncr;Zfu%06S:!!WE'`;fl@
!"925":"u.!!*-'!s//srW2cqrrMHd%06J0!!ET/"pJ-3"98Q&!!30$!VZZp!rrAu!"T8E&J,6K!"T/>
<m36K0.@G]0/P[N5!VG&7S6BN:f1+gr)"5-<)cn'A7'"d^i""%Df0K7G]n.JDf5Dg'5h]+E,fo>F`hkR
I;s+VWuDQL!r`0%"U"l-r;Zp&"9S`'!Vl^1"UtnJ!<<*#!!#9k'FbKS!X/i;$4Hh?!=K;9%fHn[&.fEe
'GVH&(`+,5(E=H6*?,b8*??=N,Tn*G(`!i#r"Bk\'c%Q$(`F;4+t+fl;MP>U!!`N)!<r](!!<?+!s8B$
q#CL"$4-k4!"(`h%gi[I!X8r?%K6hC%1NdX%h9$W%/^JM$k3UQ%MB-\&n;I_#S.@S&f2;t'+trm(&SgX
(Ddo*()7Ms&J,Wo(a;M"rW!*-!rrB,!pTah!W`9'"9\T&!s-XH!r`0."pP,2!s&B%!<N?)!VcZo!Vuls
!WW8i!"]/2!!**#!!<H,!tR[-!<<3"!<*#q!WiB("9&E'!r;m>#Se'e%13@_1`j8%2EaGa/13,54[)(s
6q9jD:/Fec;Z0H.;H$Rq=']?EBPbJ%D.dd)Dfg5IF)c'uD/B,c'PqT&DJsK6EccGJH[TsQN27@(!!3'!
!XAo2qu@!+"9S]+!<N<'q#D*6&Io'I!!!?H"J7:_)]oLk!!<W<rX&`8$k3^F%iu8n&J>cm(`=/,)BTb8
*H)r;(*4J;,:=c\*?#b1(&ejL&ebom'bqK#(Dn&0*?lp]0O021"oni-!!*9,qZ$a%"9S]+rW3'#q#CL#
%LN=:!"9M@QmWL_*=N#M":bq@%1*LT&.f?_%LigTr<jGO%1EUS&do6_@h9+T%h/s\()@St&ebomr"T2I
rYGkV'+tlf%h]Zq+UV"i!!*'(!<<0*"8)Wq!<E8t!!!-#"V:b;"UG).ScAuq!"B27!<N<#!!!'!!WW8r
!;urn!ri;k!;lj+!WW3&"T\T@.N&3d!WE*!!WN3!!rW-'!WrQ/"U"T$+9W8_)\No=,o,'E3'/WO2)6gA
3]oSk6:FF;9MSA\;H!Hj),aC5<``U=?taAlDJa'+Df9`BG&qV?ChmebBcCf%CMRa'DK'T:Fa&4^FDID:
'G:BH!!!$*"p4]&"9er3!Wi6#q#D$.$NLV:!#5e?\4%,J"VM7M!X8Q1!t,JF%K6k:%j)>o&J>`l(E"&+
)BTb8*cN,>(*4J;,:=c\*?#b1'GLHY)&!Yt()Ic()&aG8,:Y/rD0l6f!!WE'!<iW'!!i]1!s/K(!WiE!
!#Yb:#lk52!"8i-YWWL/!>#VD!X9#A%1WmZr=BqZ%h9$W$k!FO%1N^R%MB-\&n;I_#7_1P&Jc)prY#5E
r"KYV()@]$&ePZb%MBQo*aWa`!!NN,!!3?,p&P*nrrW&t$N^G2!<<?9"TSN*^AIs5#7(G6qZ$a"!<N9&
p]16np]CHrnc8Rg$3C80!!39)!YcgoqZ-TrquZft"p+l0"U5)1rW!`;"U>#@%O*i]]$JKq.R#pN2)mQU
3&iu+5=%Y*7nH?J:Jgpc3)W[T<`i[>?taAlDf06-DfBfCGB7_?CMIQsB4kmkBkhF"D/XE8Fa/=aF_RqA
&.nmD!!!',#6Xl(!sSo3!rW/s!#Ye?#65,4&0YSQXJC=J()%#_%1EUN#71bHrXJf9rsp.^&.oNg'c.`)
(E+A3*?K/?*#9V;*[<$Y+WVI;()6ZZ(_[W"(Dmu-)]TqG.P!*#F8uLF#6=f)"U"W%!sJf0!rN)s!"f88
"ono/$QEB7URZQ/&.SmMrX/i8#RV"Oq@Ec?%h9$WrX/i;%1EUS&eYQ`&n;I_#7_1P&JZ#o&eP]gq\'JS
'c%Q!&eGQ_%1s?l)K'-c!!NN,!!3?,p&G'nrW3'#r;[Q8#7(;0#6Or+:lM^p"98T,!WWB0"8`)t!VHHl
!WE0""8r9$!<</l!;urt!XJf,!<WB,&02>Z!<*#s!rW-M!WrQ0"pG,1!!39(!!!0QL!ZkY4taNK0eb@@
4$5Sb2`a,g6q0[;8k_uVr_X5':f1+i<`W=/ART:h^i++(rbr3eH$==KD/3iuAnE#pAnPaiBkqO&E-$2J
IXlTU\;^h,!!<3$!t#;9qu?g'"U"r+!W)is!W<!4)fN*@&/52.-j0YW$4dUT#mLYB%/gY=%1WjY&,m+g
&J>co)&F)-*u>q=E#ou8+!)LL-m^#W)Aa,%&eP]g&ebuq(`=20*"a26,qCQ"Mf/S"!!`N)!!EB)qu?g&
"9S`'!W2ot!rW*5(i$7,#Rg]j+TMKC"q1nJ#R:YF&,m1<&-<@O%/pVJ$k3RP%MB-]&nDO`#7_1O&/>ll
r=So>%hfWl'b_/i%LijY'c.d6?iC$/"T\T)"pFZ#$3://!s8T*!!!')qu@3]\L%^b!'CSg!!36&!sJN%
rW2TjrW3$#qucp"rW2Zlr;liurW*3)!Wa2O$N^/*rW2s!!!<'!/-?"Z#6kA8!WiH+#R<02Jj1hM5<Q5B
4t\WN5<_.h3''5h77Kd<8P;cR;,R<h3Di[R<``C1AmoCj_/F4*EH#l>H$==KChdWqARo=_AS,RgC2@d,
Ecu_WJ9YkGKa/+g"98E)$O?k4!!EK0"9JW%!;ca7"99aZBH@Bk%h!q(%KHV<&.]0T"pYJE%hB0L%06qL
r=Bn[&el)u(D[o2(EFQ9*ZPt<*ZlXU,p=9I(DRV^&K28q'c.]))B0Y;+=/Nj0U?AP"TSf/!!!-(!W2p"
"U"o/qZ6Qo"9ecM[q$3k!=K/8Gn:5]!!Nf@$4$hA$kEs`&c3+@%h9$I$Q'9]$OR@V$P="^&Io$U$k*[]
'G:uh&.oNO&e5Qh'G:re%1EXV'Gqa?=8i1'"T\T)"pFZ#)Z]s@!s8Z.!<<0)!<<*$Z2kI9!!EZG#64`+
!s&H(qZ$[!!<MclrW3$#qucp"r;lTlr;d$&!WrN+r;d!#/-Z=X!WE)t!W<'"!W<!E!X&]5#6kA<"UG)S
45<t!8O>Bf3k@dF0K2$W5<_.i4?l/$7RmYR8P;cR;,R9g%8p/+='/d?@;0SpDf0:gE$odRGB7\<BkM!f
@q0%[AS,RhCMe$2G'SOcH>UcH$jlt<!!!-0#Qsu)!sJf/!Vl^7!WW9%*A5K#)C64,!!S)i$igJ=&.]3W
#RLkJrXSo:!=fY=&-3@U2\[#E(D[o1(EFQ:*ZZ%=*ZlXU,p=9H().An&.oKe',;<#)&aG6*Zu^V0J]5&
!!*'*!WW3&!rDs""9S]+rW)ou,6.`H!<`BD0$-<o+;+_U!.P@\!!*94$k!@H#n.=V&J,Ka&,m+A%h/sH
$OI4N$OR@V$P=%`$5!dS%L`aX'bh8mrX])B')`CQ&eYik&eGN^$k*XZ)BF`,rW!*+!WW9+"82]r!<NB&
":58;!rr<&&tf4.qu?^<rW!$%!s/N#!!*-%nc8XirrW*#rW<$!rrDipquI3-!WrN+!<E0$!(6eirW2uu
r;liu!!3#u.KKVU#mLM<$k!RX2mu+K*\TZ:1/YbK68Uee5<hCs4[)/!77Kd;8P;cRqbR`"<*!(&?=dPZ
D8L70B`;rVG'\@QDJEisAGfp<A7Z!YBPVI(F*;m/HjjuAA.SqF"p"],$3p\2!!36(!W2p@!<<*%#6Y58
.ASLK!!a&?!#gUu%06eD%M'$X$471N%M&FH!=fY<&/l/p()Ri')''M6+)rAC(EOV>,Uar]*#KD(')iFP
&J5Zk(Dn#.)]Tk?+XJiE25WtE!!NT/!!!'%qZ$["!Wi6"+9;NE!!<K2#RDrW/2$u*$NU5@J,olT":#8B
$jm:K%1iFL!=o\=%j)8j$O[:L$k3RO%MB-^'P7sg#S%:Q&JYum&.]9_&JG'T!>#kB&do9_%h9$X%M0X(
P;rOA"9nr.!X/Q+o`,L'!sJf0$4[:@%0GVm!sJ`)!!*WRrVus"!r`5u!<3)i!<3*"!rN0"!rW/k!"]/4
!sA`/!<<*$!+,^/!WiE%!;QWq!W2pH!s]/:!<WZ8,8e0k3(,AL>pqm6[l[)?5<_:s5sR\$6:4.07Rp$C
9i(ab*D]I-;H-[u=C,NGBl:e,DJ4!-E-?POEc#N'ARo<L@MrZdAnYprE-$5LH[:*[gK"Ud!<rQ)":5;8
qu?a!!W2p"!<N6$)?9sD(^[6$)^>Ug/H?"mIfp>e$k*UU%h/pUq$d?7&,Ztl&ec#t()7]-(*+K;*uu+<
*ZlXU,p4-C'G:uh%hK9a&el)u)&aG6*?H:G0fH:!rW!B4!<<*$!<<*#!<<*$!W2ou!X/K&#mLMN%'MZ3
+pJ#\-ia5ZGQ8*O"pYGB$k*LP%1WmZr!ii?%LigSrX'SQ$k!CO&e#BfB+kg^%LijZ()7Gn%M'*_&eP`T
&.T9b&ePZc%LrpW%j*$g/H,VQ#6Or-"U"Dt'ESCA"9JZ1!>PU4"9nr.!!iW+%NYHI!!30&!W<#t!V$0i
!WE0!"9/H%!W<#o!W2p#!<WH."9&9*!W[KG!s/N)r;Zj!!;cfp!$).I$NpG1#6YTKV`Qpk9NXnS3D6V=
9Kkd-5<qM$r^-fV6q'R8"\D?\:/Fdd:HD<M<*!(&?"@>WDSg@1BQ%g.G'\@QD.mNl@q&nU@:E_WAS5ap
E-$5LH[1'\i^s:[!sJ]*!sf)5!VQKo!<`<$)[-3D:lQG2#9kW7%0.#c";M4Q%1NdX%h9'Y%K-\;%1NdX
r"&lA',VK$()7Z+(*+K;*uu+;*?QOU,p4*A'+kfT%g`dY&el)u)&aG6rZ)7c1,l`u!!*''rW!!#!<Dut
qZ$X!"o\K<"98U)Os(_K+X[p.!"*ZF%KZn@#RUqJrXJi:r=/`9&.K!S#mgqH$k!CO&e#EgBG;-l#nIIS
&f)2p%h9'\&J>Zf&.]<`rXfJK%hB-[%1XO.W$2-?"U>/1!X&W&!!!&t!#,J<#6Y#,!W`Z/7K<i*!XTDD
!=]qE!!NE+!W`9$rW2KgrrN*#rWE-$rW2uurrMrsqu?j#!sJi1rW!0*!0mNd!<WE#!;cfq!!E<*#n$n8
!#GqO\TKJf1dal+8NT\Q4A7q+5X7V%6UUf?#Xq3R8P;`P:Jh$d)c0F3<`W:-A70+h_f9R,Df9T<HZsIG
B4YR^@f9^:@UiscB52:&F*DtXG_'ql4pMK!"98E(#R1A3p&G*p"8r3;!W\oo#Sm^^)%mJ\'6jTo#S%:R
%M''[%Lr=E!t>\L&,Ztj&JGlq().T*'c\<:*ul%:*?QOU,p+!=&ePWb%M'']&el)u)&aG6*??+>1H,KE
-3+,J"8`&u!W<)s!!30("oSE;!Wo6'%N5]i((LZO$ZH(T!=/o9$4@7Nq[NQ6r=(+_$OR1H$4@7L#n7LU
',G<t&.&jV%MKWn&e>E]%hTEe&J,H`&.fHQ&-rdW&.T0q.&@aZ!!NQ/!!39*qZ$Tsqu@E3"9el-!WiH(
OUqQp#6>&<"p#2NquH]u!!<'!n,WFgrrW0%rW<*#r;ccsrrW0#qu?j#!sJl2rW!0+!42_-!!<<!!;llr
!!EB.#n$n8!#-(jd6ou]4?#Ag9fu:\5"e(,5s[j:6iKIY77Kd<8P;`Pr(e8.;H-[t=']?DBPtb.D.dd*
E-?SPEGK/s@U`dE?lEH`A7fRnE-$8OH[13beM@[E"TeZ(!XAl2!VZQq!<NB%!!3Q@Zk"/e'b(?P$53CS
H3=ld%Lr@I":bkM$k*%C!t>_M&,ZtW&JGlq'bhH('cS69*ubq8*?QRV,p!p;&J,KP%M]Kc&JGos)&aG6
*??(<1H;KV!!E<'qZ$Tsr;uls!s&H+"T8<0$l$9!'cISe"U,>8%<;XQ$igM;#n$Y>oaE#P$4-tE#n%.K
#n7LT&f5=!&.&jW%MKZp&e>E]%hTEe&J4pPq@F2M%hC!:T+1i$!<iN)!X&T+quH`tqu@B2!W`9'!X\ql
!!*B0!<WK,!=p+I!!!*""9JZ,!r`5i!<*#u!WW?%!r`6!!<*#t!ri;u!!<<-#6b#+#6b+P!!3-&"82`n
!<iN-"pbM<rW"/S.*+8,5<h7n5t""<[Q[>J6UF.-6pj=06q'O67n?3E9MSC^:HMBN<*!%$?"@;TDT$L2
AT2R,G'eFPC1Uj`@:3JM?XR;OA7fOmE-$8OI=-BdcR0G<"p"](!X8f1!Wi)sr;llt+oqr`V[3\>$j[(C
#Qtri";;"L%M'*^%LijU$k!FO$k3[Wq[`rD',;;u'Gi8>'H8-8*ubn8*?QRV,p!m9&.]6\%1WjY&JGlq
)&aG5*$$"?.m0^A#R1>+!!**%rWE*!"9AQ*!sAK%!XKUFrXoeR#Qt52!"X)M$NLA9#mq%J$MY#.$l'-W
#m^eC$4I7J%2''^(Macu#S@RX%MT`q&e>B[%hTEe&J#?]rX\r=&J5Wg'Hf)t"98K)!s&B'"9S]&!!*-%
p])98!WrG@!!!*)"9S]*!X9\G!<<-&"U,#3!s/N)mf<=frW3'%rW<*#quH]sr<!!"qZ$^#"pY;1!!if0
f)PmQ!X&Pu!$;4B!WiH,"pYD:!<EH6/[7&p4$Z/"5rqM;[m!JL6UL`>$U[<M77Ka:84cHJ:Adm):f:7o
='/a=?Y=2lDf'*)DfKrIG&M))@K'[5?O'tI@qB@kE,uA2I=HcgHcmEI%gW(6"9AZ0!s8H&qu?d"!Wi9#
'`eIG";m+"$3^bF#mLA8)0uAt"q;(A&.K*Y$k*LO$k*RS%M'*_r=BhY',;8t'Gh]&)BNl>)\a;5+!i?]
*>]:u%fHhN%M'*a'c.`+)]Kb;*?cXlUB_23!r;ls!rW6#!!!&t!Z:t<!XAfHPRJ35%1NOD!!*XO!"&]0
#7:hHr<i9,!=B/4#TX3Y$OR1L&e#BgC)%<e&J#Bd)&<hp$k3^Z'+tier=05H%hK9a&el#t)E!l^rWEE-
!<<0'!s/?#!rrB(!VZR,"9;6u!rrB-!rr<(!$VCF!!<B'"U"r1!WiDj!<3)r!ri<!!<3)t!ri;u!!<<-
#6b#+#RLO_!!E9'"Te>t#lt&.!WrQ/#6tAH!<<?519`N"5!_J"5WVG<\3NbQ6ppoA$UdEP7Rfm=8P2WL
:&[m+:JXeb<EE7(?=[GWC;"@rDej61GC"CLB4>9J?QWT\?!^lG@V'7jE--ASJ:M`bfFel.#6=f)!X/`0
!Wi,t!WiB'rW!9+"UbJRMZF1k$47+E"98`GHNXue%1`@K!Y5_Lr!Wc=%Ls!\&J>!R(_IDq()7N")\j;2
D&=*2)&s_E.3ooL&.\[K((:W]%M06f(E",1)]Tk<+<rnM!!`Z/q>^Krr<*$!!!3$"(BFL9!<rWJOp_p4
%134<!!*[P!"/c2#6G5?$iUM,$NUS@rWjMN$4@1J%MK9b'P7pf'+GH`'c@c!%LW[U&JGcg&,cqQ%M'*_
&JGlo)&k<-!!*0*"9JT*!s8T%!!33'!VcWs!<r[$r;[30!rr<(!$_IG!!<B'"U"r1!WiE%!:g-h!W)rt
!W)ls!W<'"!Vucu!sJo4rW!3/!6kKF!!3<*p&P'm.foeV"pY51!!E`e[5LB>69[Ru4@iVd5u0d86q'O6
7R]d97n6*@8P2WL:&[lh:JXh';cQn$>$kfKBP4bbB6S$+EHc\MD.[2S?63BW>[:ZC@:X%gE--ASJ:M`_
i!Kr&#6Fl*!X/]/!Vl`q!W2p3!sf)PO9?%%$3gV8!!jHi"V_1O%fR"A%h9$XrX8r>%1WmZ&Gm%H',22s
'Gh]')]3,o'GVr1*$?OU,9.F/q@"#H&/#]o)&aG5*$$"@+uZn1!!35u!!!&u"8r5u!WW9#!!rc2+I3HO
&I\jErW!<<ErZRJ"pYJB$O[=8$N^YB$2t22#n$Y>&.T?`'G=a^$lfTa&Jc3!&Ifok$k<j_&eGN^$k*RS
%M03b'G_H%*A=Vs!!3<-"9JZ.!s/<"!WrK)p](Bs$3t)>!##J9!!!-%+ohZE!WrQ/"9\f.!Wh`irW2lt
rW2lrrW3$#rrN&urW!$%"U5).!!i`.[K$=.!X/Yt!$qXH!sAf5!WW3(#qa"Q7n#d/5!V5%>.[-u6:XI6
7Ros<7n6*@r^eD.91qrQ:/4S];,^Is=^,6E@V]>PC1hL$DK0iEF)5Do?!LW?>lIq9?!h#NBPh^1H@LHt
E".BD%h&^J"9AK)"U"l-nc0@+#m(s8"qhFS"p4r-#TA'o'aP9ZrX]&?rXSo:":bnP%hSUM(D7Aq'bqE!
)]'M+>T":u)''hG-mKZF%K6_K$k!FO%1a'c(E",1)]Tk<+WWqGp](?q!!3$#r;cft!<N<$!!i]-)5@ZY
'+G-D!!j0X!"8i3#71b9$iCG3$iUJV#mgkD#mq(K$kF!_(CF1U%M]Hb&f)<!&I]!S%M9?e&.\XI$OmRW
&JGio(EFAWTDefq":#)4!sA],qu?a"!rDs+!<<*#!XJdr!!3-#!r`0)"TT_H!<<-%rWE?+!WiB'mf<=f
qZ?`tq>gEoq#CKu"9eo,!!ic2K`D/S!<iSr!!NE+"U5#.(B=UC,gJDA7RK@'5s7eD]L5Xb84H'=8,Z!X
8cD=(91qrQ9hnJ\;H-\!>$PHHA8GJBDeWg%E,g#EEb])ir*0/()I-TV@q]^uFF&FeKkum['ak0J"Te],
"p=u.nc0"!$31U;#o+$]#6YP?!!jKk"r.FT%hK<b&.]<L%f[(>&H!+B&eYilrY6(_)AjM(:EC>f*ZlLN
-R'HB$jm@>$P*XV&JQ$!)B0Y9*?6:A;N(JR!!2rs!<E9$"8i/t!WE')"99":&/u;m"oSE+&Te!^!!``8
!"/]5rX8c9rXAf7rX/Q0*=</_$k3a]&K(dF(_@)h&ec#t'bCc[$Om[]&e>HM$O[@Q&.oQi(De20:l,)N
!Wr]4rWE6(!W2ou!s8B#$3:2/!!33+!7UuRqZ$[%!$_@A!!3'$rrW0#r;cEhrW2ltrW2corrMlp!s&K,
!r`0*#RsT7"98E*"7cF2!<NE/!<<*%$QI;O91D<85smh.?G&^*77g!>rCHr[r(?r]#>@fc:/=_b<#8V=
>?tZKA8#S5EG0!&E,g#DEG8ic=]t`-r`L.D?!h&RCiFNCIt35iQE(Z+#R(>4!<WN0!Whil(]t$I#HA4M
&Io-Q"onoKHj1>m%hB3`&J4mO!"Su=rt,2Bq[roC'`JgO(`F2/(-<Z_(D\#5+XJKZ)%m;`#mq%I$4@7P
&JQ$!)B0Y9*?-1@<e'fC!<E9$"8W#t!WE'*!W`M-&f_Pp#6Xr*#S_=[%KQe>#n$Y>!"Af8rs\o8rX/Q0
%13IO$k3a^&eu$;)\<JX'*T-g'G(WX*"!,d'+k`a$OR4K$OmX['GVH%+;e./!!!$&#6t/1!WrK)r;Zj#
!rW*$!<N?(rW!'+!8.>WqZ$[&!@%IB"9AT,!Wr<$n,WCfqZ?`tmf3Lk!!*-'!r`0*#SAKm!rr<)"TAGo
!"8o3"T\T'!>,sb5>4KE70l@J9O>G&<(9LZ8H)3\9))%!9MJ8Y;,^Ir>$PBCARo=kG]IJ3D/XE9F`;#%
=oMP'=oMM4>$PEDB5DR1H[pX"E1.3,&./dL!W`<)"pG&/nc0@+"Ub=-&K22k%LNIA$6=O"(CCZ`rXf,A
q[`Z;rXo&@(D@Gr'GVB#)Aa,3-Qs9C*$6=M-6O-;$N:A1$4dLS&JPut)B0Y9*ZH7C>&s?;"TSQ)!WrPs
!#,Y<W"pBc%grRC!!*dU!"K#7#71b:$O@.M%1WgV$k*OC$N:A2$60E^%1Ws`&J6$.*"WYo',23!'FtQW
$4RO[&J#<K$5X'Z&/#Zm)&OJ9>BBiF"U5,6"9\l2!Wi6""9S]+!!!-%!<WH+rW!'-!7UuRqZ$['![IUC
rW<'"mK!1dqZ?`tli@"drW!60'+5*J!!!0*!r`5n!!rZ."9AK&!tGaZ%RNlV7S--A6rI%'8QA5Qr^m)]
"%u9\:&[ib9+FWi:/Fhf<`iO1?XdPWB)Z["C27X(EHH;?B4"bA='&L+='&L,>[ClPCiOTEJU`;oVLfKj
%L2t6!<`T1!s.rm%g3+D!2UGN%M9<`$3LhQK*2Js$4maI&c!":&cE@@'/(%6'c%T'(`+88*Z5k9+!N!W
+;bXr#RC_D$4.%I%1j0g(`F>5*?H+A+D+UR!!E#s!!3$"oDf!s!2^VTrXTAC"98Z6H2nEU#7(\8$NLS8
%K6h@%1N^R$4?b=rX&f:$OdIT&cNFt)]BS-&eYim(Dmhs$O6tI&/,Wd$jm:I$474R&el-#(EXf7=o\O/
#6P&2"U,#1!W<!"!s/N&!!<9*"TnZ'":,"c!!W6"!XSrRquH`urrM`lq>gEoquZftli7(f!Wi9#!X0&7
rW!'%"9\f.rW2Zl!<WK(!"oDB#fT5,5Y"OA8k2uVb"Gc*9`@Z`9,:2q9hnGX9h\5R92&&U:f:7n=B]!<
@KC"Prb4!"Ci!m)EHH;?AmJJ<<E<1&<`W:)>[ClPCiFNDJUN,pZXk!`&-`+7!<`T1!s.rm'EnaH!2^YT
%2'Hh$jIIRL^P"+&.ndPrXer=r=\u@%ho]m()If*)AsA1*#fh<+p]J@*u>Fn#6tP5#ndRS&/,fr)B0Y:
*uQ1IF#a4#"o/,u!W<)m!#5P9!2^_X%1j-["TSu3If^)\#7(YDrX/`8%K6hB%1N^R$47(GrX/W4)%6uc
&J>cn'bhAt'G;)q(`3qt$O6tI&/,ZX%h&gE#o<pX&/#]p)]'SDG<Z65$jQh8"9er3!s/?#!WrK)rW!$%
"U5).!!EN,li7.b!!3K0,Q%Q@!UKg`!W<)u!UKgd!<<0"!!3<4!WE'%!X&W."8r8o!!*0)rW!W7$jt0K
:d.BG9h\,^9[$44852`MrCd5d:B"&h:B+&f9H?i';,^Ir=Bf'=@Us+cBP2'rChmp.FEDD4>ujs*rDjV6
=B\s:@V9LrFF&IbJ:"q.)[m5\#64`)!sJf/!V-4/":#,2WuW8i&fD>l#8[]'$lB<_&.oNf&J,NP&c<::
',M>t()If*)Aj5-*#fh=+seQY(CpcU#7(56'+#!T&/,cq)B0Y;+;l:NI4,*r"Si&r!<<2s!!!&u!#,G6
WuiGk%hoHW!"ApX!Y,28#71b:$OR:O%1WjW$k*LN$N:A2$6BQ_$k3^Y&el)q&el)q&el-")AWnn#RV"Q
'+tfb$iLDJ%1j-e(`X;5.tKA]":PJ8!WrT0"9S]'!!*0'r;Zp$"9el+!!ET.n,NUh!!<6.![@OBrW2?c
q>pTtr;l6br;llt!XoeLrVup#rWE3&r;lWm!W`B+rW!3)%1pl\;*@HJ&Pl+n>>NI<=\;F_9heAW9hnL`
:]aEg:Amm+:/Fed<EE=-?!q,PB5)$lC2@^%DK9iADJ!3Ur`(%@<``@*>?tWHBP_U-H%:6kID\Pq$4I%;
!!*0)!s/Mo!#,J="oteL+:/Z"'FkBb$],9/$5!jK')W@>'(utF'GVB"(`=5/(E*2k#9P0;-6O-9#lY#D
#6tM@$4RLY'c.c-*$-7A+YJHh"98Mu!;urp!<3)u!#,J7Y9P1r%i#NX!"AsX!=f)7#71_9$3:MCrXAi9
!t5PE$N1;0$9/D$%1a!^',;/n'GV;q'c7l0(_R8a$P!a^&eGN]$OR4K%1j-e(`X;5/rCqb":>84!<WH.
"9JW&!!*-%r;Zp#!sA])!"B;9mf3Lk!s8Q(!=/]LquH`tm/[.doE":Y!s&H)!WE'#'.+7h!!E?*"9S`)
!W2ot!W2p!!<WN(!##n]b?@Y+7o`D]93b?>:g-Lg:/:a`#Z+>p;Gg:f:J^sb%o6#"<)m"&>?tWGA7fLg
BdRS1CM[p0F`hV7?<:**<E3($=B\s:@:X%fDK0oNH$t7b3ZeS6"9&9&!WrN+quQHj'*JRBW@](t&KDMr
#T*u,$lB?a&cE@B&cE@>'DrRD',)&o()If*)&O2.)]Kb=,:=i^(_@Mi"pG/7#6tPB%1a'c(E",2+!V^K
1lW+Qli7(f!Wr<#'*A66/fb9.(CgWL%0:nY%0-S:#lP&1$4He@rsSi6r!E</"Ub_K%hTHQ'E/[X()e/5
)AE\h$P!a^&eGN^$k!^V$OmX['c7o**]0#u'*8FA!!*3$"9AQ)r;Zj"!W2p!!WrK&!"BDAjo>Sc"U>/1
!=&TIquH`tl2^MYli7"drW3'#rVup/!C@7p!!NB*"9S]+q>gNrr;Zm""9n`()%dq0BM(W`<`2ag?;o0I
>>.mi:f("c:f1-i;Zfop:f.-e%o?,$<)m"&>?tTFA7fLhCAquSCi=?:F`1o!=8l/=<E<1(>?tWHASGsu
E-HbTI"KWu*sDlN!<<*#!r;uk!#PbD#bj?r%MBct%ga'^M@CF2&J5Wh'+toV')WF='`A[H'GVG`(_%?#
)B'P7+=&<_+rLptr<3i=#7(YF%hTKl)&aJ;,TJ$fPmRig!;c`t!<WH&!#YqEUH9;$%MoTZ!"AsX!=]#5
"pbJ@#m^hEr<rT3q$I$-"UkhN&.oQS'E/[W(E4D;)\rtn$kEp`&ePWa%K6bO%M06e(`X832OP3n!X8Z*
!<N?+!s/N%!!*-%qu?g"!W`93!!!N7fDl-W#7:Y:!!N?EqZ$TsklCGYm/R.f!r`9%!WE'##\+,<!<*'#
!Vl]r!Wi6"!W`E-rW!6+%Mm3.7n-KV;$p/q?rYNO>u"<q;>jDm;uT_u;c6Ljr_O)%;H$Oq='8a5?XdPX
BPIE\#]+F"F`hV8?<@))(KOU@>[LoMAnc'tDKUAOIs'9r('jsA!W<!"!<E9#"8)X.":#"+64j_K)&*Vh
)%DH4)%.&h'E8aE')`LA'EAmG'`Ja['GVB"(`4,/)B0V9+=&?`+rLpt"o\W<"U55>$kEp`()Rr/+=/'X
/Y<IQm/R4h!WrQ'!##D6VaM.-)%m>^!"AsX!"8i2"UFr2!"&Q1!"/H,0+&$o$k<dZ&J>`j'GM9!*$?CF
(D.)c%hTHg&J,H_%1EXT&.oQl*>ThLU)"4D!WE'!!r`9'!W`?$!<3)s!"o;4!!**-!7:cM!XK,;!WWB(
+6<M$!;QZ^!!**&rWEH,!!!$"M#[SU!<*$"!Vl]r!s8E$3roEe!!!$)$4G%,7nR/c;,U5!<mjrR:K14j
;cH[o<)lq!<E3!s;Gp@h;H$Op<`iL/?!h#NAnYppD#S5rDfTuCDe<<W<)Z^p<`iO2?t*\[BkqL#F*r.]
CYLQP$ig8/!W<!!!<`9'q#D33!!!')"9>An%h^6*'+bNi%Z:f7$PF'M'E8^F'DiLA(&epH',)&p()If)
)&aG5*$$1K-n$8W&-s$T"9S`/"pbPE%M9?h(`=56-6OleV[r\*rrM]k!s&H*"TAB?!<<+u:(Rs\%LNC?
%0:nX$igG7#6tM>#7(SAr<i3(*srAa%1Wm\&ebom'c%Z-+X8'H'+PK`&ebok&J,H_%1NaV&.oQl*>TnF
WYbsLr;Zs$!WrN+r;cp!!Vud/!<<*$!sAV6!!<9-#mC>0"99P$!;lla!!30&"9&H-!<<**!3#u!#lXi'
!VcWr!s/N%!#PeA!<<62#mdr#;c$Uq;GpA%=4:/V:fUKl<<-)!<u"b9<)cdp;H$Op<``C+>?tTE@qKCh
r+lXWEccD@AmJG:r_jY6=Bf*?@qKChCMIU)HZOIUg`m78!!!'$r;Zm"!sJT,q#D<6!!!*,"9=Wf(`+83
'G(Wk%uUo8$ka0d'GUKZr=o&Br=g"\',2/s(Dn#.)]Kb:*[)gX-mBN?#R120)?^6M$4ICU&eu3")B^CL
.5S",!!*'"!<N9&oDeso!X&Z*!##J8!0US*'cR_m"TT#5IK0cV"U4c.rs8*#(((EX%1a!^',2,q(E+>=
,Tn!>%hB3arY#nW&J,H_%1a!]&f2Q&+"s`)$4Qk5"9AQ+!s8?#pAb=!"98G'$31,."pY83!!E9D`;fr?
!X/K,#6Fo+#lqF7$iBu)!VcWr!s/N%!##G<!<<<7#RHom?<:!+<)ZY)=k+-c?rC'+<`W:&<``C*=]ea,
<`T)t2cWjY='/X1?!h#MAnYpqD/F**DfKi>D.QsP;c6Ll<ENL5@Us+cC27R!EdDYEK\R:Q#QOi,!rW*"
!<`<)!!`9"(]aX;!!<N1!deN&*#9P0&.9EfN"-a7&eb0XrY,8Fr"]/GrtYDF-l!I4(`=52*$$%@+XJKa
+W(^q"9S],"9o,>$k<g]'GhQ'+=J9W7'6@e!s&K*!VHF3!<E6)"T\T("onXLC*OW/'ak0F%KV"Y$igG7
r<EE/#7(V4$2t;3$N(2J$47.L%1Wp]',2/s(E4G@,Tn$@&.fEd'GUN[&.oHa%M'*_&f2Q$)F(D*%1<%6
!!3$"qZ6Bj%KZ_63"l]#!<iQ*!!E9EhuMm>!W`?*rWWT0!WWK+\cE0/!!36(!W<!8!sSc+#8%+BOfVVi
;HZst;Is%_=CP32=8Z2#=oMS-=]ea+<rH#3<``C+>$G9>@:WtaCMdp)Chmp-"`eTu@Tl_0;&N83=Bo6C
AS5^mD/F03G]7h[i"?G&!!!-(r;Zj!"8rE"!#P_<!!!'+!s<R_(a0\8'G(Wl&<.2=$kj9P'ESp^'`AdC
(B,'H'GhK"(Dn#/*#ot>*[)dU-Qj38#6Y,1!sB/>#R_(O&/#Zm(`FJB+"Kmgqu?g#!s/Mr!$2.B!sJl0
!!*9(!,lru*tf:r"TT#6IfTrX"U,,:#lY&/#lY/.$N:G0$5a-Y$k3[X&J>`k'c.f2+s\9L'G(ff',;8]
'F,6_&.]<a',1]g)\X;[ZiCI>r;Zfur;uiso)Jq;*!H<B!r`0$"99Ra!"K#2!sA`/!W`<%!X,Y1"o\Mp
!!*0'r;[c;"9nl,#8%%>LUBlc<`rC$;Is%a=^tH8=BSf*=pS>:>[(B8=]ec)<]F/^=BJ^0>[:`HA7oUl
D/F*)C2@d+DJ3EZ;,9ta;,gY&?t3b\Bl%^-F*)SFH\gSn#m1/-"U"l)!!<9*"U+l0q>_H9!WW3$#6G$C
GRc#;)\`hk*"e2B)@[>n'GM;]'`SpE(B53N(B5-J'F#9e(Dn#.)uL]s+<r0Y*Yo1g!s/N+"U58@%1Wp^
'G_Q+*[2a_9XO]t!s8Z.!VHEr!<N?,"p#P@!!N?&Apb.7'GLoY!"K*]!Y#,6"pbJ@rWrN1rX/T3rXAW2
((:T\%M'*_&ebro()e5;,9Id:%hB9erY?+]'b_2l&.oQj(Ddr)-UtHC"pFo*rW*!#q#U?mrrMus!>6aX
!<)s""TT_D!<*#E!!E<(!s8W%!!3Fo$N'o(!VcWq!Wi6")$'jF!WWH:!<RGV:gmC.<E)k->M34l<a8f.
>5_Y*>l@qn>[(B7=BJX+=BJ^/>$G6<?t3b\C2@a(Chma"CM[cs>Z=Hl9hnPb=Bo6DAS5apEHQMKFE2bo
eJSGk!!!3,!W;uu!rW9!!!30&"9&99"T\j3I1IS?)\`hl*"e5C)\!Go'GVA^'EAmH('#-I(]P9N(&emO
'c%T&)B0[o*??4G,9n0B$NpM4!sAc4#n%1P&/#Zm)''_>+uNT+qu?g%"9S\t!$2.B!sSu2!!!*$!*4X_
+qk\!"TT#7JHHA_#6tPA$N:A3$N:G3%/gY7%/gSL%1WjY&.oNg'GVB$*?ZLG(_R;h&et9\'c%Js&J5Wi
(E+,,(b/Lc"98N(!!*/u!W;uu!W2p!!<N?"!!3ET!W)iu"ookF!<*#Z!:0[f!<N?)qZ$a%"+1@Vnc/[l
!W<!;!<i]0!!a&8"(T/H?rgN5<E!I5fj&/l?!CQ=rET\8?XI,F?!LT;r)jP6>$G39?=@>TBPM@#D/<tc
B`i!U=A^,48kVlT;cd43@Us+dDK9uLGB.bOUqn)P!WW3*"p4`'"9AT,"9eW&!s&E("9&97"9Am%K+]@D
)\`hl*>+>E*"EYr'`JgL'GVB!pD<fE$PaBj'GVE$)&aG6*W7#k+!DdM)A3>Y!<N?,"pbPE%1WdX&ebut
*?,tD2Jnidr;Zp&"Tneu!$2.B":#26!!!'#!(2JT+;,Cs"oo,8JHQJb#m^kG$iUJ5$iUS5%JpY4%2B?_
%hB3_&J>cm()\)5*ubt-%1a'dr>5t['b_2l&el3'(`"#?AdF_/!!*'"!<N?$!W2rt!W<!"!<WH$!!30S
"8`'""ookG!!E<(!W`>J!!30&"8i-)!<<H/<Wr[-!W)ln!!!&t!#bnB#Qau1%fc`0a&ZSK>ut'*Am*hn
BNebK?2\(0?i=@8?X@#C>Pq\(>7"P??X[GVB5)*rrbNosC1q0f>?"<f84cKN;cd11@Us(bD/slLG]S%O
Z()^8!!!$*"p4`'!<E9$"8i0!!WN9$!##G8%QB4X+Vbq1&.BTkO:`HB'GL?Y!#GDIrtt_OrYGJJ.M`g;
)B'P7*$-1E+X%sM*>T.j!<E6("pYD@$k3^Y&eYin)B'SD1OO?Kr;Zp&"9S\t!!WH+":#26!#5J7!!"a4
'd"&'$jH\B!eLRf!t#ACrX8i9$k3+Er=8T5rsni8+qYM*)&jP9*#KA#$k<mc)&aA1(`!f!&eYlq)]0A5
.!9P6r;cfurW2lrrrN&u!W`B+q>^LYqu@$'!!WEL!!*'"!WE-#!R:]F!W)j#!<j,[!<VTf)?L*K!WWE8
!!PU3='o!7=]\R7>2!:t>[UlE!+5_5$=R@P@UW\Q?X@#CrEK8+1L4<o@Us(`BP;*qD/O6,An#"G:J!uD
7nQNS<a/p?A7fOlEHceUFEhi>E#&f]!!<K2"8r3"!W<)t!!<6&!sJT')Zg!M-]\ub'H7\s%3?(A&KMAs
'GV>u'bqK"(]>3K)#b?N('G?e()Rqf)C-7C+X86W+<;:3$O$M1!X&]5#mq(M%hK?c&/#]p*@ik%9E>4o
!!<?,!Whro*!$-F#RLP4!!*'"+H[H]&JbcZ!"]3_"VLtH$Om"D":P_K%M&FJpCR66)\3Gh%1Nma)''_;
)]0;%%1<XY(E+52)&O/)'E/UE(&f'S,:A(6!!N9$rW<'"qZ$Wu!W<!"!<WK&!!E<&9E54n!!3?)-2dfI
!<WE*!<M6]quH]sl2UfAkl;e,"pb81"V1S:1=0-1<a]*5<+BCg>&IYU?XR8M@:E^E@gHOP?sd5G?!LY5
>m=VA?t*YYB)ZENC2Im.CLg^O:eF/C*CE7e9i4no?=@;SB5;F.H?sgYG/uf^%0?S7#mLM0!;urr!!<6&
!sJT')Zg!N)NtpY',qVt$l^%@%3Q5t'GV>u()7T$(\\dG(]>*N(Dn%h)Aj>1*[2pZ,p+$>%L<+9!!3</
#mq%K%1WpX&J#<\&JuZ?2jbQd"o\K("9S]+o`,s4!sJr:!WW3$!!![t(EF&&%0lkB$@W!k#7M"Mr!r]:
rXf#?rY#&>rX^@c%1<RU(*"G=*#KD&%L`[S&f2K,)]BS1'bh;n&/,iu*[<7u('+C=rW)p!rW2lr!<N<#
!!30'"T/6&!Wu@("T/6%!XBbKrW!*'"9\f.!T3tU!V$-q!sS`*"UI?n#58,j!#ktD#m()0%KHY[dog$Z
@9cu8?u4"fE+*6b@:K4G$=m[YARo:[@:3GLqHa;3?X[GTram]mASH"#EGArb:eF/B5<qS+92JSj?!h#M
Anc(%G^4XUHHd0?%0lq=#mUP5r;ccsqu?g"!<WK(!#5P8%hG!C*toS-&I]L"IgRA5'bhAtr>#ALobdWD
!u;Xg)#bE^)&O53,:G#g*Z#=n"o\KB!X/i9$4@7O%M03]$4@@],UYdK!!EK.!!*3)!Whro"T\]/#RLS1
!!!68Ql$eR((CNL$5@O](^^`^%f?k;&H3:@')E:@')`Cs&.T*U$4n!p,9Rp@&Io3V$4RUa)]Te8)&F#%
'+bZd'cSA@24":C"9JQ'!s8T+!<N&t!<N<#!!<6("TeQ%"p509$3U>1r;Zj-(((?J!!*0)"9S]+!T=%V
!V$-k"ptP5!!K8$!s/Mq!!!&s!#ktD#Qau.$3C>If32K^A7/\G@!/S[DId<g@UoCJ!+l+@"_D4S@UW[D
?i+4d@Uit]An>L`BPh^.BjO\.6U*^r4[;D+9i4qq?=78SBP_X1G'7V>`tT3n"9A]6#Qt2,!;urr!<3*"
"8r33":P=&)BKM1()%2o.U`u4'c6iar>#ALpDEiGr"f>NrYc1_(Dn/;.4cec'++mErW!r?"UGDA$k3[X
&ebfb$kF1#,rhFq"9JT(!X/].!VHEr!<WK2#m0u(&"aaZ%MfN\!souJ#o3s]&,["<&cWLD'E/^F(&emK
'+trV&If9]$jm@S)'L=N)\WYfrWrZ9&Jc8`)@[Q$(D[`!&JGp!,9JV)qZ$d&"9S]+!W)it!Wi6"%flb9
!<<*$!!`XD"UP/4!WE'-$P*IB!!*0)"9S]+!T3tV!V$.!"9ni+$imR5"onZ(!!2lqrW2lr*ruNM!<<-)
$3C[k>?t<B@piVOHAlWTAnP[cA7]=aB)Q?FAn>L_@eX:J@q91aAn>L_B5DO+Am%em4?>G^3^#_s8Jt9%
=Bo3AA7oXpEH#i.E3^Mt"98E*$OHt<r;ccsqZ$Zu!X&B$'FY6IV&^Qg)]'2$(+qin*>fV/'c$Z_rtkJJ
!#PSNr>,JO)?(N](`*u/,Ut>k)@crK!"K&6#RLkI%1a$a'G:oe&I''r,s@1i"TAB(!X8f1!qZHq!X&`6
!r`02!<<+r*#]8$%grXM,;g,J&Gm(=')rXF'`SpI('bWk()7Ms&eY$Q'+PHZ$kjR)-mKWB#mU\@#n.@Z
(]"sT(DRW!(`OYB22(i,"U,&4!W`?!!!*-%qu@c?"9AK&"TSl0IK0cW#Qau+!<rl5!!!$%"9\f.!<M*Y
rW2Wk&ci(8!!**#!!`La":5&.!<N?)q>gNr!!2rs*ruKK!<<*'#ltFg>@(BFAn,CcF*;A8BkV*iAS,Oe
BDlKKB4b^dA7K(XqI;9kAS,ReARf4^CMn$"<(/f)1c70N3^#bu92S\k>?tTE@q]^lBksJo*tJ_]!!N`9
"9SN%r;l`p!WiE''`\47$NpI.+!(t5(_mi+-Rg,Y)]BOl(&f!A(]>3M(Ch9")B'J1(De):.4c\[$MsfD
!X&`7$OdLU&/#We$k<pc,;=7H#QtA6!!3?.!Whon"9J]2#Qaf&"K!1W$5EjX$k3dg*u,M('E&RC'E/[K
'c%Q$(]>0U(D[`"&ePZcrX]nW%1E[[*@3-Z)%QoS"U>>B%M9Bj(Dmu*rY?.\&eu9%+tRV5!<<3%!!*9-
!s/N"!<3)t!##G;!<<0,!"&^Z!=T#;"TSN(!X&E%!<E6("9S`-rW1pW!!2Zk"Tno/!!3E)!!t+r#R(A4
!!*3)qZ-NpqZ$X!"o\K>"U>#9fih`cCM7<qDej!$Chm`tAnG[gBP@?Y!,)IIB4b`QAH-6?A27_.B4kgf
@q0(`CM@'L5;OuI1,LjI3^#f"9Mnbi=^,-:@qo@[F4*`)%1rgG"UYJ:!WE)s!Vucs!<W6#('=jC!2q"^
&KDW')^$.=*ZuLB(`!i$rYG,BrYYVN!>l^R)@78u(`aeJ.3B3-qu@c=!X&`6$4ICS%hTEa$kO3h,!MtY
$j."E!!3?-!Whon"9JZ0#6F]%%]16a$5=![&f25n'G_Gur=f/E#8Ish()If))?(NY)&O/)'G:uV%g<LV
&.]6]'G_]8-m9B9"9Sf4#n%1Q&JGin()Hla'G:un*>]n\U*g*E$3C2."pG)1!<N&t!!2rs&HW(9!!<N-
#Qf\_$N^bA!!*0!!!NB)!s8T+rW1dSpAbj-"9nl,":P83#M]:\!"/i.!!NK%!;cfp!!*0)rW!0+#65(_
=C,V=BEi9kBjtajCA_cFC&D]LBk_6nAnM$Rs(;1?s(;7C(M78jA7AkD7QN4U0/57>2)dQZ5Xe7?<>8\H
@qBIr?rh3h0-Uc6"98N1#6Y,,!W<)q!!!'!!##GA!!&u?*ZQ"4()nA7'cS58)Ar;drYPDHrYGPOr>,SR
)&aG5rYu+`+<_gC%0QP/!s&H+"o\`:#RLnO()n/0+!hjG5c5>(&H`FE!!*6+!W`>p!!<6("U=f'%At-^
'b:`_',V>j&JZ&Z'`JjH(+0n8(`=52)]Th:)&F&%&J#?]%hK<c',20!*?ZLE'+4sI#71bH%1`=I&.fKj
)]p+B,q9uV4eWAn!!iK'"9o#3!Wi?&qZ$Tsqu@?1!sJ]*!XA]2!.k1Y!=K&2!!2ut"T\Z,!s/Q'!SIJQ
!W2p-!X/f1!!3B*!s[0\!!!6&!!*3)qZ$TsrW3*%!W2ou!X/K&%g<+:#Lup`E+WctD/O&tAc??CC&D`D
CB\HfBkV-lrFQ%Bq.;6mBkh?n?W^/q4uFrE/hf(;1c73O3]oYu;Hm[EBQ/#u96I3S+USJT!!3E2"9\H$
q#CHs!!!`6":5&.V]['.'GM9#*>oS/*#fb4(]G0M(\AL?(Ch9!)&aG7+!DgN*#TG##Q4WD!<WK/#6tG9
!sAoB)'C(H.4u\Y98Nle":,#.!!NN)!WW8p!!<6'"U=f'"f31U*=</\%2'Hi$kEsa',:?[#T"9o(`=52
)]\ht)B9Y4'b_/i%1NdX&JQ$"*#on9(D@;d#7(VDrXBSP%1ERM$4dmn,UOlk1EmW,KE2J]!r`0("U+u1
!WiE#!!!&t!"T)5"T\T'!rrN*GQ8$M#Qjc$!<N?)!s/Q&!S[VR!W<!-!<NE/!rr<%!!rX&!!N3"!<WE$
!!!&t!WW9!!!**&rW!B5!!!)GAR]CiCMI[&C&VWJAS5^mCi!m&r+uCK");OaB_c<=Ae&KiD/<]b:.%-%
0J+k/0`<dG1c70M3^6#*:JOV^>!G9W>o41Z"onW)#6k>1"8`/n!"o>=!WrFr/0Q)P'bhH&(`!o+)?(KO
(\8F@(Cq<!(`=52+!N$Y+W1ju"9JH$*WlTO#7(P=!s&E)#7M+P$kXHb'9#6^#6G)2!!!-(rW3'#p&G0q
!X&]'!"Y\N)AWbi$kX3e%Ls!]',CE]*#KM1)&aG6*??1C*ZZ.9'b_,g%1NdX&f)E/+s%jE'+PBX$47.L
%M''[%1<II"pG8?&/5`h(*EtuMEV"@qu?p)"U"o0!Whup!s/W1!W<!&!<?[2"98W"!!E?*!s/Q&!Sd\Q
!WE'-!<WK0!WW3$!X&K'"oA9"!W)is!rW3%!Wi3!(]a[<!!*H-!<C,[An,guCM[g%An,:\B57B^!,VRM
"DhmiCMN`\rFcXQB4bahCMdlr;aiZ$0`EX)0/<>Z"Z%tm2`Ni14#J`M59iSO'G^cR"9AK("pOu/q?-Ek
%0?n;#6:/P,o7O:',;A_(],'K(\ALB(C_2u)&X>2*$?LT.3K?3qZ$[!"UG#4!s]#4!Vl^"#QPjX!!`K,
!<iQ*!W3$#!Whup!W`E,rVup"rW!Iq2'!,;$k!RZ&eGN^%h]WS(bQ[D)B0Y9*?H7D*uu7:'bV&f$k3[X
',Vc8-6F!4"pG5<$k3^Y&.]6Z$4$h="8r<#!!Nc2*P;@RqZ$d&"U"r1!rrDs!!E<)"U5#*!!NC$!rr<&
pAb0or;uoug]73P&-)\2!sJl0!!!**$*F7.#R0r&!<E9#!s&H(rW!$#!!*3$!#Q"B!"?Y]CM%U*Ci+'*
BOt[bBPVL(DJj=gDZ=SQD#J/IC(tAqB4kmlBkL[G5W(5J/M&J+0JP<]0GlN"1Gh$M3B8oM4?aU6TF2&+
!<`H(!sJl,"T8H&!qlTs!=Af1!!e]G.2a*@',:B]rttYOrttbPqA/uFrYQ(^)&aG5*$$+F,U46>"oA9$
!X/i.#Qk;8!s/5u"9])4?\SFY!sJf.!WE-&!s8T*p&G-p!sJT'!!<-"$BQtc%hK*V%MKHe"V;1V',;>^
)#bBU)B'P7*;pm%)]9G+&eGQ`%hK?g)''kF*#&b`":#8B%M'*^%h/mQ#6k>0!s\l-!"'8;@"e@V!<E<%
"9JZ-!VQKq!X/c/qZ$ap!!3-$pAb0orW<'"!!1gS$NU80!W`<%!!*-'"8i-&#"&@o"TnDu!<E9#!s&H(
qu?a!"TAB7#64`@\o)G%F)Z#8Df'6%AnPjqrGV^RqeuFN!,_^Pr+lgXCM@HpAn,1J8Nnsb0)dF</h\n4
0.nk21,CdJ4?Yhf2+Tt]Zr.M8!!NK-!WrT0r<3-&r;uWl$O6Y5"H5/g*#fV+(&f!M(`E5iru(hRrtkYM
rYPPNr>>eX)B0Y9*?G)"!uhp^"8`'!!X8K,!X/Z,q>^[3%fhhV!r`0,"U+r/!<E6'!s/Ms!!30("TAB$
!r`0*M(^+e&.8jU'E&OH',22u(]G9M)?(QP)\j5,().An&.fEe'c.c.*?>t/$3^S=%LNUS%M''[$jm7F
"pG/7rW`W2";qsYQ95!E!W`9%quZs$!VQKq!X&Z-r;[$&!)!:p!!2fo!!3'#rW1^Q"9AQ*!s8E$rrN&u
"p=p@":>,1p&P*nr;ls"qZ$X!"o\K8"TSWAZ$pS+F`MG@EGoZ.BPM@$rc%aQpi-4Ns).gQ&8Z,rAmntH
:.79%0J>%1/M@#U%PB=b0/>@C3^#_o4ZPo#"&-'>')hn*"TJT&!r2fr!WE'0"TS].JjLn))\s)%(Dmu-
q\o_X)AsA/(DcudrttbRrYkbT!ur:$*r[5c*?#_-%0lq2!!33)#6"i="pG)1!<<*#!<<*2)CLmV#Q=]*
"U+u0!WW6%rW3'#pAb9r!X&Z*!!!'!!"49>+V>:p$P!d_',:E\rY>JMrYYAI(`4&)'b_2m&J5Zk(`F;1
)&Eqr$3g_A$P!%E!t>VE#lOu9#RUqJ$4.Rn/=HbHrW)ourW<'$!<N<#!;ZZt!<WH*qu?m+3=,Zc!quZt
!<E6&!S@AT!<N?*!rDs!!<WN)!!-L:nc8Xi!WiE(qu?g""9ni@!!!-%#8F/!CM\09EcQ5@Df'<,DK#Mo
qf)FPs)S*YrbrEeDJj<,BOY4G9h%?-1bg[;r@S+(0)dF90/>CF4?l5(6pNOa^K_HS!!!$%p]LR!quZ]p
rrN*!#Qk&5!-qKg)B/qt'GVH%)&jP9r>YqZ)]BS2rYGbU(`=20)]S_q!$2%[#p194*ubt-$jQn2!!33)
"oSW8"U"o/!<E9,"pY/8SO3S[!!`Q."9S]*!!3'#!!2fo!s&H+"TAB$!WE'0F\Wqh&If-Y&el&s(`4&)
!u2Od(\nmR(Ddi&'bqDr'E/UT',;?&)]BM,&Io3U#RLhHrXB8G%1ERM#R:VA$4@7RrY#DB&Yhf!r;Zfu
rW3'#quQj!p&GR'!WrH'!!*'"'djas!!;ior;l`phZ*c[!WrN*qZ$j&#Rgt?[K$R&!;urq!!30)#Q=]0
"TSW;Vj_:DF*7J("`n[&Df9UlEV4AMEW0tdE,96!>Z46]4?,/PqChq'0)dFE0/>FG4?uJ55rh#/^`*@_
!rr<%!WrQ0"pG/5"9S],rW2iq!<E9$!##D6#lo'N+XIp>'GVE$)B9e>*?G,!%3$6))&O/+(`4,/)]Tjr
*<I9)+oWYh+WhU:%L<(<!W)j8!<NB-"pP;;"p>#0!<EE6!s&c`U':T%!W`?$!r`6"!ri;q!!<6'"9e](
!!E3#'6$qh*"EDd%M9?i)&jJ2'bh>s(B,-V)&X8-()7Ms')iIQ&.oNg'c%W()]KV.&.ApE#ltDBr=0MN
$jm:H#RLhG$k=$m&e5[;W!WM-qu?]tqZ6`uoDemm!rDs$'-%Sa!!;iorW2WkrW2-]!s&H)!W2p'!X8l5
!sm6[&a',q!X/i.!"T>8!"Pj"BS(8IF`qqNFE@;!rH&!\s)\-Zqf)UVrcAHcCLpgO8j>6j0`E^+0JWP^
(,7Kr/hJY/1H%9V5Y4g<68buD$jI4Ir;[-*"U>8:"U"r1!rW/r!<3-"!!iT*#QSdN+"e9,'aPQl)BBnA
*Zc@$*!7,u)&`Dj"W80r)]Tms*Xs59,UF]\+W_I5$O-\6qZ$a"!sAc3rWa#>"U"o.!!Wo7$j_bJ!!!H6
!W;uu!W3!!!VQKq!<N?+rVup%rW![L>Sndr%1NdY',MT/*#TJ(',22u)#bBW(D[\t&J,KO%Km:T'GhYd
)?^om&I]!F#TX3Y$k3^X%LrpV$OR1H$4I@Q%i6<$)AJGu!!!H4qu?]urW<3'!Wi/uq#CBqr;[''!tH%P
!!!&n!<3)l!;cfd!<*#q!;urt!!r]3!t>?G#6b)1kPt_e"pb50#m(G6!!f7#DLH^,GQ)akF`__HEcZ;D
FSp7_FE;L"EW:(YF")*GB44q<5rC2B.4Ql$0JbRC1G^a>0.nk32*4#b3^#l*951.<%g<:Ar;[0+"pkP?
"p>#0!<Mrq!W`?(qu?s-!,6*l-l<^+'bqK$)BL"D+!1D%!ur:")Z1H[)B0Y:*ZlLI+X/-0,6oD9*uGRs
"9JB""p"c-"9eu7r<N]9#QXo*!>$#0Jc5WM$O-G.!!<-%!WiE(p&G<u!WrQ*!!3E)!"`dS*?c"*%1Wm^
(`ab@)&3_d&ebur)#bC4(DRSp%LidQ$OdLV&el)u)&aD2'b:TS"U55>$OmRW&.]6\$k!CL$P!a^%LW[Z
+XKa=#6b)7"T8<)!<WH-!s/Mj!!NK4%h]!HkQ(S^p]:$fquQTn%flb9"p"](!s/]-?5*G@!U'Lo!X8o2
!!EZ0!!8UtFEVtUqfiBjG'.nJF*)MHr,r3cFE;JCrc.jV.<'-;@9QMs3@uL#,UY&n0Jk[G2)@!B0J>(8
3'BPg1c76i3TNO:$3LG0!"&`/#71\A"p>#0!VZQq!<NB$!##V<@<*h@*>fP-(E"27+sA'N*Zk;$!?<'V
)@.9%*$$(C+X/-0,7,P<+Wh[>%gW7<qZ.*,!WrQ."pYD?$471Lr;Zp8#J28\!!*<*r;[''!sA`/!W`>q
!!`N+!sAT(!t"r,4C;tN)ANen%M0<l+!MdF'G(fg'c.]()&O/(&e>EZ$4.%J%hTHi()If*)&Eqq#Qt87
#R_(O&.oHa%LiCHrX08H&/5li"pYMa(<A*.!s/].r;[$&!sJf0!WhZg"pPMI%gWCBr;ciuli?\Zq#L9m
q#CU#"UGD9!!!6)"U(P"$j-On!#YhA#6=f,$31&3L:;8JG^4R\H[9s^GBS+OrH/!\q0"E6F)c,8DfTr?
B3Iql2(g7$,:"Tb/MK">2)?s@0JP=<1c@9P1GD*W2NY0a!"/o.!"8i-!<`T4#R1G7!WiDs!!30&"9&9X
!<<9';gBu@*>o\3)]^"D,9nBU+<VaJ*ZZ7@)]Kb:*??1C+!)ID*?caZ/1)DQ%13=D"9\W)q#M-3#7(YC
#R:J4!!`Q,A;pWj!<<3!!!`N,"9S]+!<Dfn#6=i-"9AK*$2soH;0=3)'+YTb',DK-+<;:4&.fEe'c%Q$
(D[`!&ePWbr=0\V'cS8@*uGRt#m^b@#RUqK%hK<c&.T*V$iUP7%K6hF#mM1Z&osBJ!!NH+r;[$&!WrQ.
!Whonqu?`u!r`9/"U,nM"98E&!<N;f!;Z`m!<3)i!!NB)"9\f/rW!*('e04g!p0Ih!<`T-!!3E+!"TKT
\T2n:G^=acI!U$\r,qjX"*Sp7HN&7EH?O:EBkqX-E+)O)/1)Yg,palc.4d//2)I'A/MJt<2Dm9E/hJ_E
3_\3[(^(*Fqu@')!sJo6"Tnf-!<Mlo!<NB&!"K)2!WYQ=0I[t\)]g+F+qGqF,pX`\+sA*P+!)ID*Zk2#
$6:*))B^C[0I@VDrW!''"pG,2quQ`r"p"o7$4$e9rW!*6#U$Je!r)a!!<N?)!<Mcl"p"f/!<<6.rW!Zu
I4--I%M09i)&jS:)AWqr%hTEf'EAjA'fcp?&J>p'-S$AV$31&/#Rh1Q%hB6b',(re$3pkG%1N^Q#R1J=
*Yp?B)[QKI!<<*#!!!$$!WrK)p](9pq>^X!!WiQ2r;[*j!X/W,!<N?)l2^GVrW2Wk"9JZ-!Wi9##Qt,.
%FkR`!!E3#rrMBb*<QHG!!*9*#7aGLC3O]BH[^KoHZsRRF`qqNF`_^'EY<M>H[^ElI!^0aG&hD0>>dsR
1&rd&-N5A6-n6c$1GgmA/LrJ13'&oM/1NtV,X0mP+US>P!<`K&!!NE,"U"o/rW2Zl!<NB&!!!0$!!k*E
/h@t^+!N$--3bbB,U4KV+T<H#+<_pO*ZZ4A+X89X+<;:3$NpG0!X/f5"9\W(rrN#t%0QtG#6=f)'c[2h
[42L]!!3<,!rW*#!<N;l!!WH*"9AK*#lXf<.?u/#$k3da)]Th:)Aa,$&.]<a&cNCF',23!r#$%b*[)^M
*?#\*$jQn>#n7IZrXfPO',2,l$j["A$4[RS#mLM7*@(_0^G6B"!!E<,"Tnf)!!30&!VZTo!W2p+!<WB)
#7:V7"TY4u%/p5/!X&T+h>mNUoDf7#"pY//!!EB3!!(IH!!`N1"T\W*!WhTe!<NE'!&4T\%1Or<Ap/-;
I"6ctHZsOPFEVkOF`_\GEcQ5EH@:<oIscTjI=6?R<C&>i.Ochrr[8p=.4Qi"0/>=</hAJ)1cdcX/Lr;,
2B/31+q>7g!!!B4"9&9$!<N?*!s/Mo!"]26!!!$'!<<*8X=l4I+!W-3.0(do-Pe$T,U4KV+<VgO,:"ER
)]BhG/1r4b$N:#2!X&Z2#6tG:"8r8t!"K&9$jH\3!=TP?ITm3\"o\K'$O?k4!!!&o!;QU3!X&Q)!sSi/
!#)1S*srGj)''_:)&<o!&H*.=&-WXY'GhZ-rZ)Lj,:P6!,o6mg!!3?4%1j0N'GqJt'c%Mr$jQn=#n7FQ
!s8`?(BB.t&HN4;!!<W:"9J#mrrW)u!WiH*#lt5<#m:Y:i!'_k!!<9*!s.6YrW2Wk!WrZ6rW!K<!"BQ&
&/5*S$47"@!s8T*nc/XjqZ$Wt"9&9+!X9)E*klW8Esd5DKReJrG&qbJGQ)gmGB\:WH$XjeJGt-WJ:;fe
De<$<1*dtb+XA?[-RgMr/MAe41,:R</hSk93BB#N2*s):CRcIe%M&[B!t#88!WE'$!<N<'nGj1'!s&B&
!s/K($_9I8+sSHa-78U9"XPE>,9e?0,Q8qp,9e<W,pt#['+"R;$j$P8"pP;:"U"o/!Wi/u%KQ\;"9AoO
&HG[`%1WFDrW!!*"p4&i"T\].!WW<$":kP@Q80Ki%i--()&<nu&.e^K#7_4T&ebrp)&4)3+X89\.4Qep
*>/PV!!3?4%M06erY5GL(]G6i'bC`Y#RLhG#6YMY'ED*h&.esM!!!'-#Qt1u!!39*!W<!,!<N9&"ptJ5
%LLDc%/p8+!qu]k!VQNg!!!&l!!30&!Vl]t3sl,nrX&c5"9S]+nGiOiqZ$Wt!r`0@!<iiA'q0hsGCG:#
IsZE_FEMbOH$XgaI"$TsJqAXRJe<Q^FD+lQ5Vj`-)B'S:+<r3^"Y;8\1G^fc0c;`&1Gq*N3Ar`B4>:Ej
0E;@a%LE7A#6b21rW)ounGj:)!sAZ*!!*-'"p]QW0de>".3fuY,5ibc+p/u3+sZt1$RR5L-mg,Y)&!Je
#6"c#"Tnl0!Wi9#rW!Q3!sAi/)A>rX,QIfG#R(51"9Rff:]UY%!s&B&!sJr8G=`kf&fVf.'bLrc$k!CL
$OdIS&/,cp)&aJ9,:G)q.jcAV&e"sF!X&`8%1a$b'c%Q$)&aG4(_mVl$OI(D#71DL'2T+I,6.]F#mCA5
"pG&/nGiXp"9S]%!!<6*#6Ff(#!rb!!<E6&rW)ltrW)s!qZ?cuiW/rZ!!2ut%06G4df:9i#m^hC"p+i*
!V$-i!Vucr!W<!6!sf/I?FOcnJW,21H?XLRFa&(VH[UDCJj"dAKnP)0J:2`cAl_A[.j5cE',;B)+<r6`
/ho4B2)?s@0f(^J2Dm`g2_Ha(?ca_t!!!**"pG28"Tnf,q#L$e'`eC>!s&B%!<`K57Z/oH.l/Ip*ZcI'
+UB24+!;^N+Wqs-,7>bC-7:/f+W;"'$4?b=rWiN0#5n]>"pP55!W`<'!sAT(#7Ue:#lmN,+T;?B!X&Z*
!WW8i!;ca4!<WK-!<<*$#6kW'IiAk4+W)%0%LWUMrWiQ3$4ZtG0G>3>)]^%H-nHnr*>Ane"Tnf."pk\I
%hTEg'c%W()]Tk;(`!bn"qD7N!snrs[N,5GrW<9+"9S]+nGiXq"U"o(!!!$;!sAW)!!<6Q$ig80!WW3%
!sA`/!<<*#!Wr?'rW3'#iW'#^"9JH$"9SW+"cWE\#Qb27#6k;4!<MfmquQWo!!2ut#6b)D-e*6[ISQ2R
JU;WbF`qtRH@('nM1g>/KnP#+HZjCE@T,WL,T@I1%hKEl*?c^W/2/k=3B&cL0JPCE4ZG8c:HU`n*4A<P
$31M<!!!0,"U,#1!UKdh!<WH,!WE'3"TT/JXZ7g\4rY^f*ZlOJ+<MX2*ZlXU+W;@E+sR"20d7b^(_?uV
"9o/?$k*LO#m^_<"9eu6"U"o/!WrW4!<<HD$5!^JUcT4u!>#J9!!<;m!;urq!!E<*"U"o+!"K58'Fpf`
&JZl/*"rei$2k,:#n%@^&e#?g)&jSN+<i'W,TRO*!WW3$!sJr;%1Wm[&J>cm(Dn&1*ZQ(9(C^Q\*"<Jg
!2)4Z"oo#5!!*!#!WiE(nGi[s"p>#/quHWq#64c3`W-&?!r`0+!sJl4!s&B%!<W0$!WiE(p&OI[('=a@
!!<T/#64b\#6Y,0!WrT0"9SZ*oDnahnc1BT)3V48RVAF5G^F^ZGBnL^IXZBUJ<GnDI<TR>>#7[N1bC'u
*#B;%'Gqf5-7LK!1)i&-2)[BM1Gh$L3BK8W1H[WT_Fk%8!!!6*!!)s"!WiB'li7+g!WrN&!"8o/%1$lu
+%m;;&f`(n,7u1H,pXBB,r[S.-RBlS((gr\r<<<.#RUJ;&ISsR#mUV;"pG,5"pG)3"U"u@"pFu,%M9MX
49,H`"UkS8!!2TiquQZp"9AT-!s/B$)$C$Q"_DBS3!MMT'bq>k%M'-a'GCcU(Fgg3+;,_7(_mYo$k!@I
#6k>8#7(\H&,m+?')iRF(]G<_)&O)%&IedD%hTPT2ZNg_!!!6*!!!$#m/R7n"p>#0q#CEr!r`0./0tE!
#QOo+!!*3)!rN#u!W<*!!TO.^!s])7r;Zp#!3m@=!<3-#!WE0#!VHHi!V-4^#89>\JT6okM1BtuF`r%V
H@($jK6_?UGB%4s8N\XO)]B\<+s7pG)B9kE-S$f'1,LjD0/GRI2E3]S1d",Q1bC8[LEI'8!s8E$quQKk
qZ$TsqZ$Zu!Wi/u*X;lmYsBa)(,%$],U=]a-n-Vr0f1@&-7gVl)\NGXr;['*#mptF#RCb9$6BKZ"pYA8
!!<K2"9eu2!=9><#6bKtF;,#j#RCV;!V$0d!W2p#!!!'%!W2pW":>8LUbEZH&1f"F(DIW%)B9_;,:4EG
*$cgS*#/qg!<<*'$4dUT$4."G$4I@R%hB9d&.T?j(]G-[&.K9i!!rf9O)Y^6#6P&/kPtbi"U"o/!Vl]r
!<io;!<@KI!X\o7!<<*$!S.5_!X8o;"p4i4!!#k+!!*'*"9JH$"9AT+!<Mloq>p0f$3UYfRIb$GGBnk$
4FqX!H$OUOAnGasG&qA!6T?_H+rqO:'GD,q)BL(K-7:/i.k`\4/i>aM1,_3S2`NTI0Jt+@c;"?S'bgQH
!s&H(!UKgd!V6:+"oo<S\Ka3_,;(u1-RpZ!/0u>[,q]N_1bKm`$j[%?!s8B#-NO;Q"pP24!<E9+!WWK9
#QY&5"U"u0!<W]0+0mj+$P='Q!sAc1!qlWi!<E0$q#LEqqZ%c@$31TJXV`r?+tPQ!*$6@M,TIL5)'^X_
-QNg2%h9!U$7lGf"pG5<$OdFN#6b56#R^tH',qYq%M93]&.AjN%KIQT2?4!l&-)\2!WiDg!!WQ/!s/N)
!Vl^$!XA]*#cdq+"oSE%"9IN_o`,=#!<<9/!WW3$!3,kr!XJr1r;Zs$!s8T*p&Opio)LZP"ro\El?Zoj
M2lsuCi3ruCik&QA4S^6.4$&T)]^%E*>]>"(Eb1`2E!BG/hJqD4#S`A.k_Gm4ZYJ_0JZBH;8ZHC*!.&`
rW!$%"9S\k!<*#k!$V[K"r<K-2]+>45r'Z3.4$2i2aTqd('t$C!W`<*$4daX"8r3.":5DB"p+c)":PVA
!WE'+":,25#lk/V!&CJ\5l_Dq(^C$@"9o&5pAk!imJor`%0-MBNMnZM1cdfP*?ZUN+"&d(4=:XB!!*<2
$kF!e(_R2Z!!3E9&ePTY!<<*%$Od@I"9Sc5%1<IT#n8?a0W%&7%KI4H!!!$&"98Pi!<30#!r`5r!"9,:
%00?q!"9#7!!<DV!!*-)rW!B1#RUP5TE"s%!"&u9"T/6&!<`N-!rW,q!;cff!(R7q!$<DuXI4!=ATE06
?>"1d9JdtE2(p:#+<27<*[2s_1,qKf9iYD*AoN-SO+D+P9fjgW3&icI-m(fG3*jF&'EA4>'*\@8!s&K*
!UTje!<*#l!'(5k!!!-%OEb+d-RUf=1+"\90H15s!Y5V?!sAZ+!X&]5$4IFX()\,9,:>3.8l7u2,8:4[
!!NQ0rW!-:*"tQ:63R8f#8%.?!!*0*"8;fk!V6<h!&Fuo!<<-#Mfi;Z,pb<0/gE#10,Xil!"KDB$4[RW
%1<FG#RV%R'cA#7+!)XV2a/r<'F=[<$j?nC!WW3@,8WSB4otW_!=o>4!!33)!qcQl!W)lr!rN)p!!!'!
!!!6+4<4P+f)YgOqZ$j-%Kd.PV#U`!!!<<-"pFi("Tef0!s/Mt!;cfg!"]29!<N6N,)>,i4!$+:-n$8u
+!W*\-mBZQ+<_mM*[3!b2ap_YF*`7cKT2:fSskt5S=#M(MI\n).5`eF4$dB!.hE9t&e>6Kr;ciulN$nb
p&G-r#RgV3#SI8N\N:9$"qLP2#Qb5<"p+o4#RDsc!s&B%!=Thn1,_'N3C$)-9hS)U=&i'o8gt&H!"&iB
%N.X=)$1!B$OR(>r;Zj"!VcZi!Up("!XK8I!rr<4!F`Dr$NL59qu@-.#R^qE%2'Hp(_dD_rW!$/)'p^T
.kE8*0J+b$,V(W+1,q-1!WW?:%NcQ37^3[.!WWQ6"TeQ%!<N;q!;cfp!;uri!"K)2"p+tU#6b\?!!!''
"5s4^!<WN3q>^s3$O>_u$kNFE!<<-("8i-&!X&T-!Wi#qquQ<f3s,H_"W@da+fgi3,oJ9\*Z#G2(_I5e
&/5s$*[3@-<b?E%LQ@XaQC+>DY-P40UnOWbUS`0$1+F(r+U]`k]+u;')\ND]!s/5uq>p0frW2]m!W`H0
rW!H>!!3LiGs;W9&IAL=!!i`+!##G<"p>#6%MTg+.l9:L4Zttr8PT1](K+79?W^Sj%0Zn8$NL0RT*#Q9
'FOsE!V?Bc!Ug"]!X9#B!rr<2!!!4]F?9[,&.8XA!"B5<"ptnX)]]k6'b_,g&f;]:.4d)*0.eY#+WMFA
,qgl4)up*M!#G_EK;/GR%1igI!s/K(p]10kq>oj]#6Y,3!!iR$3;`a^!<`E'!<<-%!rN)j!<3)u!$hXO
$k3FA!!*6-!!"`a&Hi.9!=&c.!<WB(!!!$$!WrN+!W`>u!<3&s!UTkP#6PMO'f;SS7M[*\'E]No#mCG:
$kaF#.n!fnP+%o2S"-%?Sti9gZEC-uS#X-%[>.4*+>b3Fa-dMa&e#Te!r`0"!W2p$!<N?*!Wr?%oDnjk
o`,!n"9&93"onu=$7M+!3!Tut"TT>I!W<!(!X&W2&g/bb48h8^4[)(s77g0I9hJ)`CKY48%KuhH!&gNr
!#5nJ'ajm>!!2rs!!3$"p]9pc!W`9$8,rVj!s]/9!!<H+"pP/QNf5k%'+#'I*YSkf%MK^"*ZZ4C,UY#h
-6sf`.kWM-.3ouP&ISpa0-`D!!!*<I$Uh.L!##P<&-r17!s&K*!VHHi!U0Re":,GG#8$qM!!'!4!!!?+
"Tno1!<N?*rW<*#pAk-mrrW-"(^13U&.A[H$NL/.[Ntnn!!!91#6k>6!<N0$r<*$#rrMoqqZ6$`$N^D2
$kX=0Wh(4K">_k7#n%(I$k<pk018r\KTqgfOGo-XNfTBkSY;aMSt2INWR./C3\iOD`*!KY!t5SO$N^5,
rrN&u!<E9$"9/H%!VHHl!V??n!WW6"!Yk_9"ptniU6ZN+!%n6T#R1D7!W`?1%i-?A3^cA&5<M.t7nZTS
<;]c);cd"J;^W(h)/-$8rW!$+$5!XD!<3)t!!!&r!rE#c!!iW."pbA6"Tnf)!#>\G-)$YC(^;ht#n.:V
(E+22,:P#d,Q8hg+<M^L*$Z[M)]'5*)]]t=+!*s'%0RCgEjeU@!WW3&$jZb3!s&N,!VHHk!TsFb!sJo3
r;[36!Z$AW!rrN*!!38r!!!&h!#,M?#m1/2!!!GJ&c`%:!rrH-"9S`(!Vlfq!W)ln!UKeF!XB)F$5<dR
Kop'`$4da[%h]Ni(a;.KC3+o]LOjeqF`qtSI"6p-NKKEmXhLEqW(TBbYa?[@#8%%A#n.1H!r`3"!WE'#
!<N?%"9&B#!VZTm!VHHl!C6\c!X8l<":bP=JraRZ$4d^X$k3RL!<<`Z0K;El8OPg.6V1'R=^,0=?<piD
CiiEA?P!r@RYM[Z$31&1$47"?rVus#!WE)u!Vc`q!Ug$f!C-_i"U5/7!WW9(!sS`4!X=@CD]B<#&.8s_
)&a;,-T3V(,9nWk1,:R=0J=t+-RUZ44#oSr)A"\)"@/K9+9iAU!!<9*!s/B$rr`9%q>gHorW2Hfr;d*&
!<E0#!<W0!$j$D4$33&/$3gP:!!;lp!sAi4"7Q9r!<<f=!',f7%fQG1#6k20quHTprW;uur;cftqZ6Nn
!!2Zk4TP]p$3pP2!Z6rs2&60+$j[Lh*[*sdDf0`HI<p-\EG]E%BP_X1I"I6;OdE/kWFs9*9F1t.#QXr3
#R(;.!;lls!riB#!r`5p!;lld!(Htn"9SW(!umE+3Z7u3#m(GG"99&d1H%[#>$bTGA7fLiCi433F)l/2
>ZP9Y@P+(`3rfKm%0HV7"pG,2!<<-%!W`<'!rW/q!ri;i!!NB)!WrQ.!sA`/!W;uu!W<!Q"sBAD4r=8,
"9fJ^'*oX;2_cj1*>]bE.4Qi!/M8\0-mq2W5qO`W1^f&F2ZX<u&Hhe.r<!!"p]19on,W:c!WiE(q>^Qu
!!!H5"98F"fDl$S%0-A/!rDs!"UYY:$lfW]#R:P<"U,)9#mgb:"UPGC0>%8k!!EH*!!rl&!;HTp!;6Hk
!;uri!"K&8%1`^E"p,;pRZS[-(F';#.j?')DJj'#DJsK7EGArd<)m%*@VKe)IZU1dNO%b?+rC1X"9AZ4
"TeK#!!3'#!!DrsrW2coqZ6Wqr;lWm(]amM"TSf5(."[\+qt[m#9!aG&i)C)5trS&=^YfP@pr_P@Us%]
Anc%!DcK8IZm#b^!!!E6#mUV9!<E9$!W<'$!s/Q%!W)ru!Ug!h!<W3%!WiB'qZ%fC#m:5:%3J3=Or"</
!=U:e!#[d\6XYG/Up.DE`5]pFe^tPdb-[%8<_k7a8WsP_!rr<5%1*.4!<3*!!ri;t!<*#f!;cd!!WiH*
q#Cs5%LE4;!!*V.PlUjm!!W]3qu@'.$kO'e(D[\t&.eaM#nR^`'+G3I%2Rk'!!!c4!!<?0#mKo#nH&Ri
r;cZpo`.#S"UPM;!!X#=$iiPhJjU=q&eGgA@VKFa?X-c8;GKeP6:==;:fCFu?Z:URP*+9H#QYA;!!!-,
#R(2/q>^KrrW;our<!!"p]10lrW)isp&GR+"onW/'akWS7&GJt%1rL=.Mb$59NGJ/A7fLiCM[j*E,fl<
EGT<)De<QmYRgd7$k!@H$3p_9!!!'%r;cs$!X&H(r;l`rrrMQg!!3!!rrMrr2?F$^!"9e\*!AQtE\e(=
$j6YX8n<-qKoqq$WN`kE_9('RdCPp,H#@1l9i%;]!!!E=&.AsOp&P$lquHZr!!2QhquQcurWDrr!s],:
"TAB)"98V=&In[=$j6P1!=95J&J,B[$k<1G%h/sV%M'*^&J+pB#A=;H#6"T*":,;="76*a!W3!!!rW,u
!WN6#!VZR8!WrN."T\T'!s/H8$Nan[A/$!p(c5,s@9H;p5r^Y!0H;i*3'BMk4Zbi*BQ/-`S/)nA"98E(
#7(S=!W`?!!!!'!!r2rt!WW8r!;?Nm!W;uu!WE'%!<<*$!r`0Y"9SZ=$j'qS<s&X,!['g1@q/nS?X-c?
@V0@lDJsH1CM7@!G&M)PN!B[i!<WN3#mUS6!!*-&quQ]s!!2irrrMoqr;lcqqZ-g"!<E0#qu@c=!!!-0
%1=$\!*?[4$l9Bl4(O&?][#*]g"PHNnb<"^'CsYVO,/R9Cl4)R$315:%hB*T"7lNf!Up*e!WE0!!rrAu
!!WK-!s/W3$8Df%!!!&O!!!-,$O$M9&ekui#m1/-!sT&=#mgkC#m^hI'+ksMB*/SC!WiK0#m^\9m/["a
q#^KprrN'"rrMoq!<E9#"9JZ-!rW**&fq#Y(1k-j2%(?J;bobC2(pF*+WqjL+XJNg0J4n*.QgR.>D]!O
!"0)<!sJr:#R:M9!s/9!"p"c,!s8Z/qu[!%!Wi&ro)\di#QXr-!WrK*!<N&t'G)2`"V"M2:a5ub>@V/U
C27QuBPS/sEHHAKH$OXXF)cGSF`3P@rW!?0"9AT."9S]+!<N9&rW)ltp]:R#!WiB'q#L<noDejlpAcE=
"U>8J)ZTjE=gM[)-;TbsW3sF\bKnYjhrO"ho_8%Dg;^N4Z*'UVXL/<:!t>_K%1EOI"9J/qp]9mbqZ6Zt
quZs$!W)j$!<N?)!!3<%!"o_R]F4cG!"9;I$O-b:!<<*$"8rE&"q1Y>$P<dY-s$BN!"B/:!!*6,!s7ii
r;lWor;ciuquQj!qZ$Zu!X&B(4Tb`g"TSN(#mq(Q%g<k%WIn>C:,jOB*uc%5(D[`#()\)7,9e6M*@s<7
5^&e#!!3Q9#7(VB#RCY>"9JT#!!30&"8rB$!s/N*!VZTe!W<!"!<NB%"9\f-!!!'!!&"BV#7V(A$lG7T
>ZblU?Y==uF*)SLG^4U_IXcluIscToLO!p1]*869#Qk&,!<W6&!WiB'qZ-TrrW;lsrrMoqquQBhqZ/_X
!!*0%!!Wo@#RLV6&gjcQNg@,VUo:K*]uA7De(31+hr3SSi7ur9e%Da(h]NIA'bC`[$OR1F"TnAt!!3$"
rW2lrq>g6jrW<!"rWE6'!W<!!!X/H%%0Qn9!"9&3SQQU+'b:WL!#bk?!s/N)!<N<)!sA]/#7LS74h(S%
!#Gn@!;us!!U]sd!VZZo!<3)u!r`5u!!**%r<!0(!<<0(rW"eZ#7CnC!rrZ5EMPiO*Zc7=()%;m&J>`l
(E+87*?,k6+tPB,9m0\O&HE%H&.T!L"9er3!r;lu!<NB&"T/?'!WiDt!;6Hm!WE'"!<W3%!<N<$!!!&u
!"T)7#Qau+!s3\V@pW>LC2j,k#'+d-G'J=\rdG9'I"6p%J;BtF+W(1[rWN9(qZ6KmrrMiqrrMoqqZ69g
!<E2t!!`Q+!='#>#6Xr*'bVO[n>NOl['mQ\`QQWWe^rL1i8WhsjqQn;in)Gset+rS%h0$Z%L`XL"p>#%
!!!&u!r`5m!;?Nn!rN0""98N$!!**&r;[9,#6b)-$j-SMbm=aX#Q"N#!W<!3!<E6(!sAi/#V)_a!WWK-
!sAc0l2^eapB(<oquHd!r;lcq!s&H)!VcX&!<if1#T*dJ>*NM[.462X)]9G+&J,Nf()\#0*#on9)&aJ<
-8@,TNDp)e#87d`#QOi+!sA]%!!**%q?-]urrMlpmf<Om!WrK)pAbp/#65#J$OLIILi?s;BPM@"CM@Hr
CD^o,EH?8HG^4R\I=[*1H^2-](C^HQ#mpk7!!!&o!;urp!ri;s!<3-!!UB_3!<WK2$4-q;!#?.bK\42Q
]=u2%aNMoWeCN:+gu.5Ul0@Qul08rJlKQODl]a(E%M0-_%1*7D"Tnf#!!!'!!r`5l!;6Hl!rW6$!r;lt
!s8E$%0d(D"9o&1])VgD$j?\-!<3)u!"K#3"9\f-!$E2*#m:_>$j$bB"R6!d!VZZp!;?Nj!!!&n!#GY=
"W7:?'L%sD0c^rA)]9J.'b_2o(E38nr>beW'c\591GrE^+!:Rp%1`XC!!*-'!WW5t!!**%r<*!"rW2co
o`>'or;lm!!!2cn/cl+m!<XQG\R9&V?XRV^B4YU`@:EbZBPM@$E,p&DH%(@#Lld4TU,X_)"U#)7rW2Wk
rW2`oq>gKrrW2lrrrMZj3!9Kp$jm(M!!"K]foMu1\A-50b08/Wd*^:kf%]0Glg4!(m.'cEp$g>Xc<*@?
#mUnK$jm:G"U"N"!!3'#rrMlpqZ-KorW)ouqZ?cuq#LBq%KQP1!s/K'#QhgM!!!$#pAb3q!W2p)!sJ`+
!X&K'4LYXr!!EB,!s&Gh!;urn!rN*!!WE)u!Up(J!<<*,'aG3K"HY5g0e3\<)AsA.()7N")]g.F*uu=A
*ZuUJ)]95L$9h.C'En^J$j?V2!<N<'q#CKt!WrQ'!rW/o!;cfr!<3)t!rW0#!Vl^Q!<E0##o*a]!?JOQ
B68<'=D;;R?X?uA>[CcG@qB=gD/aQ?IY3H/ULJn-YUBbW!=&c0!Whonm/d.errN#tqZ6Ek('"=;#RUtP
('G*J.*I10[)BJabfRoHr5g&'bgG)#jlYailLXoQqu==R\Ca+`"9],B%1EUN#6Y)'!!!'!!ri;l!;llq
!;urt!WW8q!!rZ."9er2!<<*B$38QW!!<3.!WW3$qZ$Zu!Wi3!"Tno/!!<N+!"1'l!<<B.!!!*'!Wh]h
r;lcsrWE'!q>^Krn,O(%!!!99!!!4rCF1MD1(#?:(`FG5()7N")BBn@*?,q;*?QCF)]9>=%Q-dYH2nfp
%0HM/!s/T-!Vucr!W3#u!Vufi!W<#u!Vc]r!Vufq!?;(>"q^h<)o.bDB3'C]F&u^S>Zt94=^#':@:a-d
Ci402FEr=gJraSsKnGTi((1HNklCP\quQj#rW<*#quHQop&G[*"9\l<('=ghf!gF,R)uJT[/RfS]tCti
]tV7q]tM2#ce.7EpAOjfbR`CO]=\b#'+kNS"pYD>"p=]%rrN-$rrMWi!!<*"q>gBnpAbd+!WrH'!X8W1
#aR^U!!*0-"SVor!W<!#!<`Q-rW!0*%KICs[K$R2!!!&p!V?Bj!W3#u"8r8^!&"?W#m(*7N@H(]-l=i[
'H\//()7Mu(E"/2)AsD2*$$(@*#fh7)`B<+F*@Th'*nL:!s/W/!rDs#!!**%!rW/s!;$<i!!!'!!rW3&
!WiE"!!33(!WE'1!XoGJI'QmX9PI^X?<:N9=8c/)='8d9ASH"!rbi9gH%(<jFG=gLQ%o>C&I.J"rrE$!
quZg!rrW3$quH`tr;ls"nc1QT()S0ZeV9-AXes:HXLGC:Y,n\+Y->13Un4*T\&[(Zlgj`7i9JOlc)qTl
*";lJ!X8r:"9JE#rrN*#rrMcmrW*'$!Wr?%pAk3op&P'm&-)\4%0-DNRfE]o'Fb6M"Tn8q"9J]/!s/?#
#R)%]BiG]F#6Ff(!!<-%quZiupAk0nquZj"rrW3$qZ-NorrM]k)$UNP!<>$A/gMDO(G?mP,7#A.'bhAt
()Iec(]kQn*<$rl+!DRD/M/8=Rkt*X"T\T'!X8c/qZ-Hnq#LBpquZftqZ-WsrrW*#!<N<!!!*-(rW"SQ
!!WR#ZrgF2;H.F9=^=?s;c-Cj<E<4*?!q/RB4u$qDf^/MFEE%X?uWG8!##P3!!!&h!<3*"!r2ru!ri<!
!<3)t!WW8n!##J>'H1cALldmeRBiT_WK3pKS!s>G+Io!pTqnWi[CsQ*g#MA[k4%BC\`dE2+UeDP!!EW7
"9SQ&rrN$!rrMfnquQg!rW20^!W`?'rW!,7!X&K'#m1J;"9\8r!W`<'rW<H.!<E0#$PWR@`r,l@#6Y#-
"9eT(rrW3$p]16nr;us#rrW3$p&P*no)KO6(B=F<P]/&i-R'WH+!)@D&/#]n()7r,'GM8s()If*)B9b>
+s\9P+tG6(;3q7k!!r],!<rZ-qZ-NppAk3orW<'$r;lcq$3://!s8Z/!s8T*qZ%oD"98E'$NL/BZBnZi
@U3&-;Gg1g77^-K;,^Ir=^#!5?!h&PBFelrEccACG'e.AEMj*S!!i?#rW2QirrN-$rr`3&rW<3'!<N)u
#6=i,!WrN+!V?@B#lkPogW>V@WMH)EP`q5sLl..NNJi[ON0^3@\@K)V[CsZ1hW*hho@^ma%FljO#6t5/
!=9#7!s/N"!ri;p!<3)s!r`5`!!*0.rW!(12Zs*]rVus%!qZHm!W)p4"9o)5!!<H+"<YDZ"TT#9!!!0*
"8W*"!r`5r!<*#r!X&T,!W`>a!##VL"TT^".4QA^*ZGt:*?,n0',:E\!#5DG*#','(Dn#/*$$+E*uuLR
.PO;B:]LJ$!rr?*!s/<"quHctpAk3orW<'$r;lcq!W`<'rW<9+!s8T+qZ$Wu"TABT#6P2jW)R#'?WpE(
9hnAT6q0aA:/Fhf<E<1'>$PEEAnYprDfB`@I<'"<RpZ4!#l4Q!!V69l!<N<(!sAK)rW<3'!<N)urrN$!
!!2]l&HrR_=k/G!S#<!KOH#9[N.lubL*;8(K8,GUVQ[8.YHYORbh(e;oD.@`[a9^F%LE+8!=/l4q#gTt
!!2cnrrN'"rrW0#jT#Gg(_29##lFZ'!s8,qrrMuu('=[C!rr<%!!=:/+U.uV"onZ+!s/Q-r<*'$quQZp
rW2cqrrMrrm/Rb%#R(3TB-/?;*#TV5*#fb2'GLEZ#nmsb',)&p()Ikf)A=&1*#p+L-n[J]RfEHl!WW3&
!Wi9#quQEirrMuurW2iqrrN-$qu[!%!Wi3!!<E<%!&4N\$^H]H=]Sa.;G^(\8OZ!77S$-F9i"Vb<E<4+
?=@AUB5).!Ed<(UD/"C)":>D8qZ-TsquQKk"9AQ*!sAK)rW<3'!<N&trW3!"!!2]l!!3ZD,.P:>QC4J=
Q]d>cM1pT\JfoVpJV/fBR\H[XWiieFa3i`,p%mgq\$t3:(CC3D!<r`("TAN'!ri;q!<3)s!r`5^!!E<&
VCDlM!!**%!<N;p!<3)p!WW9#!!rfC"uW@[!"9,7rW*'%!sJT*r;ultquHZrq#^QsjT#et!%+$^.2<X9
(D[l,)&F"c'*8j]')iLI',)&p(E!)g$5sg%+!`*Y3^J]nqu?d"!s8E%rrW3$oDnjkquZiuq>gNrrrW'"
!<N<"!!**%rW")H!'.Je>YS1!<)?=_84Gp35sn%084lNL:Jk%k=^5<C@h*$\B5DR4I!'7IE3<CN#Q"K$
!Vulr!Vl`q!WN6#"9/N'!s/N)!Vufn!V?@(#RO>]KTh:ZSXPb(MMHn:J:INH(4CX^KoM@fTVJEdZb+-!
g#_f!k0CuO"5eJD%/p5."U,&-"o\Z(!s/N)!VZTo!W3#u!U9[b!WE'(!<<>I"onc,rW!!#!Wr#prrN*#
!s8W,!W)j"#7ge9SGiKm!<N9%!<NB&"8`/t!W<#r!W)rt!Ta:l#69*D0c(]A&eYin(`*o$r"K)CrXf;H
',))r(]G6S(Dn#.*W@/`4>LN5qu?m%!s8T*!W<'"!W<#m!<*#t!WW8r!<3*!!rN-$!Wi3!!<E9$!&+]]
P&=Z$;c6Li9hS&H69m^u5=%Y)7Rp$C:/Fhh=^>ED@Uit`Dg$DJCO^,_Z4I6;!!E<(!WrQ&!r`5s!!30%
!WW;t!s/N)!VZTm!VHFH$kTJ'O+WLVQ'78eLP12,I!^0cH[:!bI=d<;Q^aVCWNWeF`m`o6o&\6LZH1ZD
%K6>-"TAT)#6+l+"9\f/!WiDs!;uru!rW-"!:9dd!WN6#!!WT,2$a3a#Q+Q'!WiDt!;uru!r`9&!Wi6"
#lt,2"ona"S,ifl!!!&u"9/H%!WE0!!W<#q!W<)u!VHHe!!30&"9&92!XGGP-P@"%&.oQk(`!f!r"B#A
rX]eV&ebrn'c%T&)&X>2)]Tk@1H%ge+8l3=!s/N)!W<'"!V6<f!VZTo!W<)u!s&H(quH`urW"VX(VWpQ
8ki#T9M.iE69dRo4$5Yj5XIk.84lQO;H?t,?=.)LB5M[4FE)bSJ@dfFqZ$TsrW;s!rrW3$q>gNrrrW$!
!WiB'oDndiq#CR--.mU&JI73lOH,3QJUMihG5QJ$G'A4\KoD1\R\$:RYdV9ig?7kcg=sZ]jA6Bd!<**$
"o\]+"o\W-!s8T+!VZTg!U]pf!WE/u!!Wr6d/Xs_"T/9!!WN0!!;Z`q!r`9&!Wi3!#Qb&3"WA-"&H_n2
!<E9$!sAZ+!!*-!!rW0!!:p6W!!36+#5nN5+.5J+"q;"O&/,cp().Dp')iLC&H31@&.ofn&ebro(E"/3
)]BS3)^-Xm13?1i!!36*!s8H&rW3'#nGrFepAk0nquQs&!s/N%!!30&"9&9I#W'#06pO=98kDK?5s@@j
3&ioZ4$>en6:=:792AJe>$P?>?tF']DK9lEHA6L?CBX\?!W<!"!<N?!!s/N*!Vufr!WE/u"9/H&!V?Bg
!W)jO%7A[5GBnmuMMQq8H?XFMDf9N3E,]f;FaAUpNfoZpS>)sb[`$YPkih*ahR;$j&cr@D"9\f/"U>59
"oSQ,!s8T*!VZTh!Ug!k!<N?*!r`0*"TSc0Ym^s>"9&9#!W2rm!W<)u!s&H(qZ$j'#mV"Y?iUK2!!`N*
!WrK)!!!$"!W<)u!W<#j!UB^f!X8o6rW!F<E"s6"%1<OR&JQ#s'GLEW+V5.p%LimY&.oKe&ec$!*?Q:?
(DRf1,r%&HHN4-P"pG,,!<N<(!VZT[!;urr!WrN+!Wi6"'EJ:<!<<+HPXSMB8Oc-95sILn3&^an+Z;;?
4$>eo6UaO=:K(=t>$PBCB52=,I!gNmNM-CX#6b2.!!E<'!WiK&"9\f/!W`?!!<*#t!X8].!s/N)!V?Bl
!W<'$!<<-!!B^>dN3[AWJq\l0J:)T_E,B?(BP;*pCM[m-G(#%%Nf]HjS"Za`^!#'fkj%<h`PB,"%LWLE
!WiK0#6b;0"9\f/!W`>r!;QZl!;-<o!<WK.rW3K/!Wrre?j6c7!<<-$quH`trrW0#q?$Tt!<N<!!!WN0
"U#\QE;BP:!<WB(rW!!#!X&E'r;lltoE"F]qu@K6"pkP;!!&H<*YAnn$OI4Q',D;s&eY*S#S.CT%1E[U
%hS^P(D7K&+!MdG()%N,+s\okSH'!&#R1A2!<*!#!WiD]!;llo!WW9"!!E<*"U,)m!4>^%9MA)J5<V+j
3Ar]L0ekF>1c@9Q4$>eo6qC!J<*!+)>[V)TCNY&SH\QU_#Rq+H"T\T'!<E6'"8i9(!s/N)q>gNrquZm#
rrW3$oDf[.!<N<)!s&B%!X&]6#KUn4JVAi0HZsQ7E,0-!AH$$c@q9.`Bl%g8J;9#@NffTqTW#9:d+mgP
mGQNnkSk<J#mCA2":#/8qud-)!s/K(pAk!imJm[s"9el/"9nr."9>/,'E.t5!<N<"!!!&s!r;us!s&H(
q>^g&!sT8OaT)MG!W<!!!s8E$"T\Z,!s/Q&!W2ro!TsFt!XB);!!!(k,9.4'%LWRN%h]Qj&eY*Rrso&<
rX8f:%fHq=&Jc-#+!MdG(DI]++!E*YQQQJ:":,,1!W3!!!T=%T!W<*"!W<!4!<iT.#nsjB:J+5M6TdCi
2`3BG0E*R@0/,.;2)dNW5!VM-9i4hh='8j=AnlF8I1(@SG/>^7#m:J7!!*!"rWE-&"9S`-!<N#srrN$!
rr`9&rrM]k"9AN)!sJT''*A:>%NWi1H[pa$I<KUIBObFV?2e(R?!^lH@qKOuH@^a)MN*aaS"m4&bh2%E
n)i,roK3g!"pY20"9\u8"U+`*rrW3$pAk*llMq@p!sA],!sJ]*"TX_d%/g2+!W2p!!<WGp!WW8t!!rZ,
!Wif9Y5et3qu?a"!rN$"!WrQ)!rN)S!#>S@$j$D/+,hNh$k!IN#n%4T'+tlf%fHh@$k*LO$k3^G%il2n
'cJ,:*ul.7(`FD;,US+7!!3--"98H*!s/N)nGr(ZpAm_b!W`9%!<<*$#6=f10r[oG7n,p43]K#S1,(=3
.k3&"/1rS11Gq*P4[DP0:Jk"h='K*EC3"TGH%CII;ZR"$#m1/."9eN&!WiE(q#LEqquZm#rrW3$nc/am
!<WK(!"oA6!Y7H/E.<7bIX,sMAmeeE=8l5L<E<1'>$PHICiaoOJqf/CP*_cA]?&O^lgX2fWUjU1%Km%=
!!<N5"U"W'rrMioqZ6Bjo`,C%!s/H(!rr<("`+2Cp&G'orWDrtrW3!"!!2rsrW*3)!X]-P$4m"6!<WE$
!!E<)!s/Q%!V$0h!V69q!!!$"!!`u4!"_MB-QWa*$OI+I%1a$^%h/sE$RH,e$OdIS%hB3`'cA#7*uu:<
(`4,0.3i_K!!!'*"98K-"Tnf,iW/QN$31)-!!!',!!*+#30d6784>g-3&NKH0.e\'-mpAj-n6`!0/5:A
3^,o%9MSD^<*<R>C2nE>F,5C7GQ7^F#6Or-"pOi*rrW3$q>gKqquZm#rrW3$nGiUk!sJT'%g)e7$"U/X
I!g?gFDb_u<rc+s:B45j:FAt9;c[%.Ao2U7IY3H7O-?$1\&HePkO%KeVXB6M#7(P9!!EW7"9SN&!WiB'
pAk$jl2V.l!WW3$!rr<-$9[q\!!<*$rW<'#q>pHn$NU;1!<`W3#<tN["T/6#!s8B#!!3$"qZ66fr;lKi
"T\Z)!!Wo3!"WaO.NB$/$4.%I$k<gZ%1Dq<#R_%M%Ls![&JPHe*?Q@D*?,mq(Cr,A>E/[`"U+u.!s]#4
!Wh<]o)Ta0!!*-$!!3H,"9<ar:eXGJ4utSX0J4n+-RSd;(aULV.4Zu(1H.B\77p6J:Jt8"A86%(EGl>H
JV9<h!!WW0!!3B0!sAE%rrMoqrW2ourr`9&rrMTh!<WK(!#,J7"p0^LFEr:\F`;)(=AMIX7nH>O8Kpc$
:K(D'Ao2U7J;&i=OHuZI_9UfqlK.!&kGA^i%0Zb4"9Su:!s/B$rW2cop]9X[%06J0!!*-$!"C(`!!!&o
!!!*!"8i6#!VHF%!<WB("q1S@'n-,f!!E3#!<N<"!!!'!!r;rg!;uri!#Pb>!!!02!!*(S9J%.q$OI+I
$OdIS%1EUC#l=oP$4@7O%M''^'Gqf3*uu@A)&=)0,9KsS!<<B0"98N/"Te_n!;-?c!W)j6!WrE&!=8`2
!17Cs8Ol'.2`*3@.k)hl,Q&]3+sSB].4d/03Bff#8P;cR<*NdDCiFE9K7S?C!!!90"98K."Tni*!WN6$
!VcZo!W3!!"9&?%!WN2j!!*0)quAhc!iglsG'\=NCLpaJ7mK:(6:=4/6:+(08PN,d?tXA"I"R01NKTp9
]?&O[kiUX(l`Up&&-i7:!so/5quH`tqZ-9inGrCc!<NB&!!iZ,!"!ZL#64f!!!!'!"8i6"!VHF*!X&N(
"Ub;<&Y/n+!!iT*!!33!!!!'!!r;rg!;lli!!<9*!!!E0$31/.S3/GB&do!QrX8o=%1ERLr<N9,+peSa
$k3[W%hTKm*$64B*?5n3)^-%?:n@ml#RLY7!X8c.iW/ZQqZ$Wu"9&9,#QP/2Y#eOk76WOf1bp[6.4-;a
+<MXF*?H7D+X8<_/MT.F5t+:88ki2c?=[bfF*MnYG,5BC#mpk:!X8c/q#U9krW2`prW2Nh!<WN'!"o\C
_K:$CGB.M4@9-#d3&`i[4t&TX4?Pem6UsjL>%),bH@^a)M3"+([DL8Djlb1-l*D32&deaA!XAl"!;-B`
!<3)t!!30(#6"T."98o6_?:DM!WE'"!s8B#"9AT,!Wr6"rrD`m&H`1;!!<N-$PofD!rr]2!!!)t!!!'!
!r;rg!!E<'!WiDp!"f;9!!!$*!!<4u4=V*[$jd7Mr<r`8#m^G5'*\XG#7(SA$OdIS%hB6d(`XS<*>0>2
(`")9(aD&>%KHP>#64c."5s7V!VZQp!sJT'2$X*f!4Q!'5t!gm1,(7.-6s`V*?6":)B0V8*?QIP.PEV=
5!qb/84u`Y>@D/]F*VkQE2EsJ!!Ef<!!*6*!W<#t!VcZo!VZZo!V-3k!sST&3t)G?FE25@DeEQc;+3K!
0/>FG3&``R2`a,h7nlrfA8ZU@JqSo;QD:Xrak#>/gXF<]*t8Vh"onZ-!r`2o!;$<_!<3)t!"/f3#Qau+
"98E(ecP^K!<r])!!!'!!r;ri!"f><!WW</!!<Y'!!3--!WW3%qZ$TsrW;uurrMZj"9AN)!Whro!W`E-
rW#(d!!<5"5pR*X%1*@N%1EXQ#mUV:!sA`1"pP;<#mq(M%M'*_'Gqc1*ZQ.=(`+/:)^m#9'*/(F#QOl.
!pBX\!;cfj!!*0)rW#(c!!r\:=[kPA4#8QC.OHDa*ul4;(`4&+(`=53+<r9c1,h<]6UaL:9iG/#ASZ@3
EcQ/p$j-JC#lju/!rDrt!VcZn!VZZo!WN/l!!*3+quAee%aTB8Ble*$?Wg)f1Fah)0/G@<0JG4<3'9Mu
:KLq=FFA[kKSYe_Wj]mof\PNJXiht("VV+@!!E>p!;$<f!!!&s!<3)u!"8i/#7:P5!<`B&"kEeR!!<6-
"TeQ%!!3'#q>p6h%KQ\;!rrH1!!!(_#Qau2rVus#!W)ls!r2lf!!E<'!WiDq!!30("o\K("on`*&#h];
',:r_$4RCO$OR.D"9&?K!sAc2"pbMB$k3[W&/#]p*$-.@*#f_1)^61I/Z]Tf!"K/4!!ED_!;cfk!!30'
"TAB2"onr0\5YjY6TQtT/1;bs+W_U@(`!i$'GV>u(E+;;,q:Q*3^5nt77^-N=C5TREcuA:Kp`5N!"]A8
!<`K*quH`tq#L?opB(6no)Jdo#5eH;$k(C%BkML&@9cf(4>8*.-RgSs.Ocet,;1i34[Vh>>\A&&I=Hd#
O.</V_TpZ`hVl)`+Vk4o"onW,!qZKb!Vl]q!W2rs!W2p,!<i`1!!!$'!"%?^!!3#u!<r])!!!'!!r;ro
!;lg$!<i]1!!<N+!!J>h"TSc+!!*-%qZ-Wtq#U$d"9AN)!Whro!WiK.rW"ST!!<4s4!YLT%LEIN$OR4I
#6Y).!!**&"9eu7#RUqK%M'*`'c@u5*ZZ4>(`"#"+;uRgV@j"3#m(),"Tneb!;cfk!!30'"TAB8"onr0
Yu*kN6TQtS.OH;[)]9G,'E&Oe',2/t)]p:Q/Mf@L5XIk.9N,)%ASQ1+D.]2q"U+l7"98Q*"U"i,rW)ou
q#L<nq#^Hpo)Jgm"U=l)3t)A6DJ*R%C1(1A76)tH+sJ6W,9e<V-7LQ'3Bou/=_)DoH@1-lNLHcP_9C<V
g"=WZ*>Skj"98H,"8Mro!;-Ba!<*#r!!*0*r;[$1$Ob,^"UY,-!<WE$!!WH+!s/N)!WE-#!VHF&!<i]1
!!3B*!We8d$318/!!*-%qZ-Wtq#UHpo`,*q!<N<'p&G0q!X&]+!"B)3!<AEO+Vbb'$47.JrWrT0"8i-A
!WrQ/#7(YE%1Wm\&f)?)+!)FB)]0;,*ZZgmV%3_0"o\K'"U"ki!;ccn!VcWs!<E9*rW#+d!!`Lt<BiQ4
4#/B:,Te!D().An&.]9_&/#Wl)''kI/29(G5!VJ)9N,,'Anl4&DJPYs!!`K1!WW6*"TnK#q>gEoq?$Np
rW)Wl!WiN1qu@?9#.8G\Ao_Wn<_c"@/0l>Z*?G,!-6=<U.5!J?6VCHgCisuJH[gsAVmO7^c-Fnnb-;d#
"q1S6!XJr1oDnOboDngjqu?cu!<W6#$ipM<"cWWd"9nl,!!2rs!!3'$qZ6`uo`,I&"U>,0!X8W.#E&Zp
!!W?%!<N<!!<3,r!V-6g!VZQs!<N<+"o\K%"TAB$IKWFg()@G[$3^_B#RCS8qu@i?!WrT1#RUqK%hK<d
()e28*uu=?(DR`,+>c-O%0lk6rW!!'"9RQ_quQTnrW*'%!sJT'%gE"9!/FuE4@;1c/12V_)CQ@8&eGQ`
%1NdW&/#Zn)^$FV0JtmS5=.e4;d3^CC2@a+EKl%T#64u-!!<E/!s8E%!!<*"r;cZpqZ?Zro)Jjn!sT#.
!"fDAR<r4NEG8]X90bBd,9@a?rY>SP)&sbD,qC]05Y+g[BleHAG^YF9VR+%XaiW&d`2FCf"ptD3!so/5
g]76Qp&GC%!!<3l$NL/7#5A/u!WE2u!ri;t!;um-!X/f2!!*6'"r)Id'*8:8!!*-%qu?d!!Wr/unc8Rg
pAb<s!WrT0rW!B/!!!=&DAsB*%LNLL$2t22"TeK#(BFR?"pbPE%M'*`'GhZ/+<DL@(`!l(*X<rI98<r\
!!3'!!X&T+i;ifWq>gNrrW3*&"TAB_"TSN3=ar:k5<1GK-6X?G'bV#e$k*LO$k3[X',DK.,:P6%3BTMl
78$Q_?tO.jDfK]^DZBtA#6=f)"9\f.!Wi0"quHctq#UHrq>p6h"T\W+":#50!%Je!Qr[a6Am8,&4uFl:
*>]A#%hK?f(`X\H/i>d];-[aRFEMbQLR"X=]`,k[dalL$',Cf]"98N0"p+i(!!30$!94(X!VZR%!<`B&
!?O#s!!ri1q#CBqrWDuurrMio!s8`4"8r3("trLU%Kcb2!!*-%qu?d!!Wr/ur;cNkquQNl"9JZ."U4c'
#8SVE)&a"o$N:A2#QP#'!$21D"U>AC%M'-a'Gqc1+<DI='bqN(+Xf*RBb(=H"9&<#!TF+Z!<*#p!!!'!
!r`<$!'C>`!#[;V1HdcX0InFl)]'/!%L`^P#mq"I%1a'd)'0tM/Mf@J5!_S0;-7.9CN"35CReH."98`0
!!!*"!Vlf_!VZR#!!!$#!X&Z4#Qai'4<Z_j;IjEL=\hFJ1b9ml'b:ZZ$OmX](`jqQ1HS!#>@qeoFEMk_
PG#%g_o'=;d*H_H&d]'R!X&`3!Wi9#rW1pWrrMus!s&H'!"&c0!!!0(@fQQ6"o\Q"!!30&"8N#u!VcWt
!<WN2"TAB*!WuC8('as?!!*-%qu?d!!Wr/unGrOhpAb?t!WrQ/"oA9(%L\^H+:AMW$46V9!!N)t*WZ?H
#7:kL&.oQj(`XV@*Z5\+'c7u;/2;09'`\4:d/X4K!<W0$rW!W5!!!N>V`$n"1b^C)*ubt.%h/mQ,RF__
#n%.P&JZ0(+t"rt3'0;i77pEX?"IhmF)kZi2@9Ec$3^8,!!3'#r<*$#mK)q[#6=l."U55<!rN$<()snb
BOG.I9gUou/LDJP$jHk?$4RR_)^6^c3Z^X`=_2JjF*)Y[Oe/S^^qmb/`SF6)%1<aT"9\o3!r2lM!"o>8
!<<*#!<<<(RK*ft!<E6(!W2ot!VQTn!W)it!X&Q/#6b#+#6t6s!"fA<"9&9$!Wi3!!W`?(p]9mb!!2cn
"p"f/"9er0qu@!(!0o,_#m^nFr<NE/"Si$:!<WK1$4ICU&ebus*$6:D(_[Gp)B^@^1k$kj!rr<*!R^rK
!<W-#qu@?1!W\l\7kl_P.jQ5V((q,d$46\;+UJMb%h]Tp*?lj_1,h9Y5t+CB<a93QFEDP-Zkj2P!t,>1
!!!'#!rE*"!q-0^!!iT,!sAf5#RCP2!':5f$+!rQ>$4iu5rpkU-QNm."9Sf5$kO-l+Xf'*6V^cpD/jW=
H%_<NW3sCS]#_MB.iAU$'+G*J"U"Z(r;lfrhZ*`Z!sA])!!WN."TYqH)#aL;!WrK)r;Zfuo`G!krW!T5
!sJl3!<E0,!5edA":#,5!!!&s!!30&!q63j!U]ph!<NB&"98K!!!\-I+:\bh$N121"p=Z$*ruHI#7:kM
&/#Wk(E+86)AWnq(*4VF4[s]1%0-D4!SIJL!!**%qZH`r&HMk3O'=h+1Gg[1+WVC5%h/pF#pBWa%M09h
)BL+O/M]7H5!h_4;HI+8DfBQ;Cmt_7!!<N2qZ-Tsr<*$#mfE%\!s&H*"9\o6#RCP2!'LA`!2"@?>$+j"
5s.([-m'04"U##9%M9Hq+t59.6r$lqD/jZAI#!u[Wj][RZGsZ!)\<8_&.AaH"U"o0rW<'"f`2*T!sA]'
!!!$)!Djs?#Qk/1rW2osquQWqqZ6Zr!<E<$"9\`+!"a8O!!33+"TAH!!!30&!q-0X!!**%r<!$#qZ$s*
5'S1a%20-S"U5#3"9SE"+9;NH"U>AC%M06d'G_N')Aj2#%i?K6,Y;<R"TSN(!s-gM!W`?(r<!'%!W)j3
"%A)03AWZL-mToR'G1f`$OR4K$k=?j&eu6'+=/Hh1H.B[6UsjM=^Gc\CM&$KEruCB!<rZ(!!!&o!q66_
!!rZ,!WrQ/"pYA8qZ%`G;kI/q<EW'a4ukAJ+W(^r#RV"Q'Gql:.l9@X:g.CH'Q\JFJ;fqmXgl-RX2DoH
'*\^L%1<(=#6b54!s/N)!U]se!U]pl!<N?*!WiE%!!``7Du^CM#6OZ#quHp%!WrK*q>pNprW3-(#6=o/
!&kVj!!EH.!W`?!!!!'!!q66Y!!!&t!WW8u!!`u=SfSg`((L6H!X&T+qZ%f@!WrQ0#RUtM&.oNg'c%Q$
'b_,h)C?UR;1p\-!!!$$!<C[Nr;lp"rW<3'!Wi/u0FSGo2a',_1b0pu*#92!%L`aT%1a!_'c.f1+snfn
1cRT_6qC*T>@;2cARL"_3s>N_!<WE$!<3)t!r`8j!V?@!!<E6'!sAc2"pP2,!&Y?*^JA$6>#7XQ4>\T6
)\W\j%M9Em*$H[^2Es`1>@h\oH@LX3T;]!*^TaQIem9'l"pPA>rW`W3"U"o/!<Mfmq>gKqmJm7g!r`9&
!Wi6""sh#&#65&3o`,0s!<N<)!Wr6"qu@$(!<<<3!!Wn3$iL&-!sA]-qZ-WsrW;QimK!4e!!<-#qZ%',
%$i%](`<ee"9\f.!W2p-!<N?+"U55>$k<g\&ebrX'FPQe%hBX/,:?c`!sef*rW1[PrrDuuq?$Ztq>`/[
UcCe)5;t2D,p+!?'+bZa%hK?e'c.c/+XJQh0JtjR5t+CD=^>KOE+3()XUGC3!<3)u!9XCU!<*#u!WiH+
"9Sc1"9SH#2$+Z$9j:Y%;+O&<2_QO#(_[Mr()e29,UtN/6;(9`B5`!BKSu1lXL#OPXIm#P-Plac!sSu.
#6Y25!s/Mi!;ure!!WH*!WrN+!W<!&$?HFR!"&f"!<3)u!rE#r!!iT*!!Wl4$Qmdo!!<9)!s8?"!!3$"
n,_tXquQNl#6RAN(CM2q"TAH(!s/Q'!<E6(rWEQ3"U>AC%M'*_&JG'V&J5N_%NHrK.>1n/!!!$$!s8VV
!<*#q!r`5s!#5`8Shhrc4>895,9@a>'+kfh',;<#(`OJ<,Ub2s1,V'U6qL-Q>$bZQD.HY@C^^.@rrN&u
quHctmK)t\rW3!"r<!-)"9S`%!$D\SX[kib<D#\F3]&B6*Z5e4*$6@N-nR8=78?okBQ/8;K8YqaVm!J=
\Z:tCN$/T0!WiN0#6tM>"p>#0!UKgb!Up*g!<`H*!s8W&!!EG3!=K53!!36(!Vufh!W2p$!<N?*#Qb*(
4TGT`!!<6'!Wi3!rrN$!o`>!mnc8Ofq>^Krr;[95"0F'W*t\VU!!3<-"TAK'"T&?D#71bJ%hB3_&ebrm
%h&gT)_!^$R2->6!!*3,"TneX!<3)r!r`5r!%nWg^I9J=4>SQ<-6sZP()%>r(E",2*Zu[T.k`V62EF)n
9i>"q?=IS^Bi_J_'`A%2!VHEm!;urn!r`5o!<*$!!r2p!!Wi,t1(G#A<B48_9L_<23AN*1+!)OK,pt,n
0fVHj;HdODEd`b,S"m$h[C<HCOPE&I!<<*$rWWT4#R:P;!s/Mo!;cco!V-6h!WE-%!s/N&!!NE(f)PdU
r;Zp#"pG,'!<*!!!;cfq!"&c2!!!K9S,`ir!rW/t!<*#r!qlZm!WW9"!;HQk!Vud0!<N6$!<iZ4:43Wj
"UP51!XK&9rWNB."pYA3"U##9$OmUF%i,`j'bq5d$kX=$7V>p-"p+f*":,26!SIJP!<<3!!r`5r!&"?X
%pkJQ5;G5R-n-Vl*uPh0(`FD9+<i'Y.P<J52E*]a8l8\n>%)#P??(U6$jce3rrVclr;lQmp&P*nrrW*#
rW<*#rrDor0*`/&TKZ7E;G'5?5WLPK,pale/1iM12EaK(='fEQF+B7<UT(B'\Zhm5\!&*R"o\N$"pYA=
#6k>6!WhWf!!<*"nc8Of"p+i.!!!'(rVut,!;lg!!t,D<oDnjk('"=8!<N<&!!Nc2!!I4B!!39)!!!$#
quH`tq?$BlqZ?cup&P*nrW<*#q>_63!rr<)%KHYCW#?]W&Hi(9$OR.E#:9Z\#RCY>"pG5<$OmRU%hB6c
()IMh%i-$-=Gddm!"9&3"UYJ:!SIJQ!W)ru!VZR5#lkAS]f/;+68U,B0.J.d)&XA7+<i$V-Rp]&'Jq^,
3BT]'<Ei[2@VB+OI%MMa!!rQ(rrV`krrM`np&G-p!<W0$rrW0#q#D`F!"C*j6W6*M9gM*75;t;J/1iM1
1Gq*Q6:t-Z@:sJ$K92\'X/lW8\uM7-bsE?S$N:&)"pP;<#6k;5!p]jd!r`5k!;Z^"!WrE&#7pe6"2Y$<
!WE'$":Y_BoDnmlrW!K1!X&Z,!!a,:"VJi\&c`.:!rr<&!W2ot!Vlfl!Vult!VQKn!W<'"!Vl^5!<W?&
"UY;6!(;bU*t&2T#7(VC#mgkC#7(56*si8]$OdIS&/#Wk()IVq&K;`XI7OD>!"&o3"UPD9!W2rS!<3)t
!ri;p!&+WZ$3O>*01RrU0.ne),p=<M*ZlOM,pt,m/hf(=3'9Gq9iG.s>$Y]EEh$5=!!!6&!!*-%nc/^l
!<Voqp&GF#!WiH+"9S`-!<Mop0EM4]"^J5o>"qLV6pX%!2`*<H1c@<S4[DS5<Es$KEdEG$R\QaYWj&.u
c%%2U"U=r+rWNK1#6k>7!WhWf!WW9'rW2Bd'`e=:!s&B)#R:J4!1O&j!WW3%#R:M&!!!'!!XSr1!!!'4
!#.3rrW!*,!rr<&!W2rt!W)rm!Vult!Vl`q!<3)u!WW8r!"f85!<WK-!WWCU;A(8^%LE@GrX/]4rWa2E
$4I@Q$k!CN%MBKl()If))&OMP@#t9e#Qb27"9o)8!s.'TrrN$!!<E2o!&+HW#6bg/DDOs?1bC.)-mg/^
+<VgP-7LJt0/,+<3Boo'9i4nm>?bNKLoCX_!!*/g!<3)l!qlU#!<N<)!sA]-!Whup0E;(V"rEqY6XN8R
6U![u5!1kd3BKAh6qC$M=C,QUG(5:-Q(+A=TVJ9oe1)FK#6Ol)#m1;5"U5,5!s/Mh!<3-"!UKdg!<E6&
qZ$g%C+92g!!!-%!s/N)qZ$TsrW<*#rW!*&!s8T+!WE'$$P,5;rW!!#"9\W(qZ-*dq#^QspAk3or;ls"
pAc$2!X/c.!#5taT0!#j#6thN#n%.K#6kD>+Uenp&Io0U$P*sj(DIf5+sA3\0TnU#!!!'+#R1J:"9JVW
!<3)u!ri;p!"o>9!!"#X0==h&3[cC2/gi"p-2o(i,q(;B0*Esd3^ZLI8Ou]_>$>0;>I%-7rVus%"7?-h
!V?En!VZR#!<E6'!s8Z.!Whil-lj<c^LT#m4?Z/%5X@_%5!D4u7S?NU='K'FE-m:nLQS'pR@0D%h0'>W
&I8LA!<<*#!WrQ/"Tnf,l2^hcrW23_rW2uu":"tY"pt8/":,&/!!<*!"p"c."U"l-rW!*("T\T+$N:#.
!<ASk"TAB'"pG)0rW)fqncAOfrrMiorrN'"!!2cn3!'3d!Wi?7!*#<k'H.N&'+,'U$3pb?$4[[`'+YKX
$P+!m(D@oC/hK@LNGeh%!!!'-$3p_:!WhupirK)[r;ls"p&H]G!sJc2!#l/SX<9,R/NGO7.P*"p,U=`e
0/>:;0JPIJ7SZNE;I<d:De#u+&.SU=!X8f0n,WIhrrW0%rrW-#rW2`nrrN-$r<!'%!V6:E!rs>MD7D5`
83p$C6Uj[=77B[;9i>%r?!h,XFF]7'K8uCfPG45nW\#G&"Tno1r;[!%!sJf0!U0Ua!r`5a!!30("o\KL
!XSk"":P87%Kc\2!s&B%!<N?+"U"o/!<<*&"onW-&I/:E#/:ufr;Zp("p4o)!<3)k!;urr!r`<%!VcZo
!W<'"!VHEn!X&E%-NX8QBoatX.2*7'%h8pO"9Si9%h]E_#mUbF%MBX$,q:;o6][68(B+:=":#,6!s/K(
fDtpPr<!!"rrDfo/-?"V!!!<*&pL!;,XO.:0etO=/1Dts/i#=C2)I0N5!qh8;,p[q;eE//*$G4\!WiK+
mf<@grrW0%quZftpAk3orrW-$!<N;o!<)sL#lkclXAh&X7nHHR<E)gk:Jk.s?XdS[Cik&VLlIIWNeW.J
e&F=)%g`CA!rN$%!<WH-!WhNcrrW0#k5Ynl"98E)#QOuI8e_F/!t>G7!W<#t!WE'3!<E6&!<WE*!!!0&
!%25n%KHS0!!39*!W<#s!V?Bj!W<)u"9/Ds!<*#t!WW8o!!**%rW!Q7!!!Im<&6NX&Jl&i$O?k9":,nS
%LiaM"pYG=#TG<D-9Oh)RfETl(CL9G"9\K$g&V-Rr<!!"p&Gp2"98E&#QP&CSmk,a4>8fV3&WTI/MAn=
rAk*D5!hM#;@[&8:LIgYXpP[>(^g<D!Vucr!VQKp!<E9""8r<"!VZTo!WN6"!s&H(nGjsC!!sUBDcL=I
9j:n1?X?r>>@1oSCN"9<IY<E0Pb!qhNfTRN+X-q3!>5P2!!E?+!s/Mf!<3-"!TsFo!<N<*#n6q=%p/l;
#RLhF"TAB&!<WB#!!WH+"9\c+!r`0-!X(3d&c_n?"98E&qu?`u!ri?%!VHHl!W3#t"9/Dt!;urs!ri;o
!!E<&!!*0#!!Wh#J.<;7#Q>)H#mLM:$4RLR#RCbF$j[1U-R:<.CR>P0!!Wl="9S`-!W<#t!VcZU!<*#u
!r`5q!!WH+"9JQ*"9&9C%\o",/j([B3]oJa2`a)f6U<q'7S$0A85EAa;Hn^M(&e19$jQh7!Vufr!VZQq
!<N?#"9/H&!rW/p!<*$!!rW3&!W`>m!!!'!!%&G`SM`oA:L7XIC1q3nD/jZ?G^bC+OcPTgR"p<IUVS>b
#m_.O"8Mp"!WrN+!U0Ua!r`3#!U0S$!<N?+"9o)2!WWsQ=qV,E'F=a>!X/f3!W<!2!s],="9So>#QP&P
O9Q3q!"&r+!!NB)!s8T*o`4slr;um!rrMoqrW3!"rrW3$oDgTI!s&B,%0-A=>_OXI,8:=f%1<FK%1a!Y
#n.=U&.TBj0Ju.<Jfk3s%0ut9"U"o/!W<!#!<N9&g]7<SrW;osrr=kU!!*-("U,#0!!N]0!"rk-5WVD!
2EO5k5XIn18Ol3@:/=Y[:eb;%@#C'o"oo#8!!!'%q#LBpp](?r!Wr9%r;uoup]19orrW-$!WiB'nGiOl
-jfqU*-A,_=_h\\C3"?6F*;eTI"$g1PEqN&OdqPnY,sc!!>,Y?!<Mur"T\]-!W`>e!<3-!!U9Xh!<WH.
"9S`(!!iT5!3Q;2$NL/1!!NW8#6Ol)'`eLG$k*FK!!aPFKg,PG!#5kD!WrN%!!**%rW<3'!WhuprW2s!
qucs"q>gHpquZiuoDf@%!!!$%#7^_P40E0/!Y#&7#7CnH$k3a]%i,Tj+t+Q\&o4%I('"=9!sAW+!s8T+
!WE'%!<E6&!Sd\S!WE/s!W<!%!<N?+"9\T&*s2lN+@j4r0d\e:3''2e5X@e.8k)3D='SU"3/P"`+8l0A
!<<*#q#L?op](?r!Wr9%r;uoup]1<prW<$#!WiE(mf4U;&-sjjesTB-?!h#OBPD3tDg$MTI#4,XOGn"a
g6"<%#R1D7qZ-No"T\]-!W`>e!<3-!!U9Xh!<WH."U"o(!"/i8\gIX]!!a&C!s/?#"9AQ,%heg@$m;u6
%0-tH#mLP9!s/<"#6=l."9S`-!VQNm!W<)t"9&>u!;urr!r`5g!%J*W"s+CsUIYIk)]04u$4.(U*ubq-
'/276NK#b%!!N`4!!!'%!<N<'!WE'%!<E6&!V?BV!<*#t!rE#s!!NB)!s8T*qZ%]C#ppaH\mls65s[[r
3&s)j:.[`74&o<nVP-Bm"U583!!!&o!;urn!!30&!rN0!!r`3#!VcZp!WE0!"9/H&!Ug"6"qMG+0ppF>
6:kWq?sQu@?Yjn,DJX-ELm??,@kJW6'*eL;!quZu!<WE*!<MHcrrW-"r;c6c#6=o0"U,#3!r`0-!t#M<
!->OJ!"B;?r;[T8!WW6&"9\c+#EH%h'`\C=!rrH0"p=c'#QXu.!sA].!WhuprW2s!qucp!qZ-QqqZ?cu
mf3Fk":582!#I>[T4&EH+<i$R*uZ"<-ndhPMmRR+%1`78!<E8s!WN6$!Sd\S!W<)n!WN6$!rDs!!=/o/
!#Io)[<jS_6V'jC8jkp38PNDlT>Z9\'bg':r;lZn!W`?(qucm!r;lZnrrN*#r<*'$rrMTh!s8c>&L%Vh
&5pHiP"82M@:a%^@:!GZE.<>TkFiVC.0p:f"TSN(!VcWu!<WE*!<MHcrrW-"l2V%j!sJl4"9S`)!"Au6
$NLP;!1/cl"p#5A(^1-P$47:Y!!3@9dNA\o!WW?'!s&T4#6Xl(#QXu/!sA].!WhuprW2s!qucp!qZ-Qq
qZ?cun,O@.!Wr]:#mUe;!AnqrHpTJ4+!)OR4&g`uN&Ck?!#>P7&Hhq2pAt9qrrLmTrW2s!p&Y-orrMus
*X3#\$P<[S6AE+;?;=$Z6UXLJCm:lb4TPO#!!!W6r;Ziu!Vl`n!VcWr!<N?#"8r<"!VcZp!WE0!"9/H&
!V-4=!<WH0%M]]o*>TPiQ-6%D?s?]7=^Q*$Xhq>E)@eD3&L%ee!!36)!VcWu!WrK*!<MHcrrW-"l2V%j
"9eu5"9JW'!WrH+#6Ol)"Te[gi.r$D!#,J;)J6\A!rr<,!!!<-!!!0.#mUS1!!iT,!sA`/!s/N$!;ccq
!W<)t"9&>u!;urq!ri;j!!NB)":,>8r;[B9#7`b,J<,kUQ^<VP6P]Y2rW!$$#S."7!;HTo!ri;i!:Bjd
!W<)m!<N<(!W)j!!<ri4rW!N5'c%ofJXs!P[CEW@M,PT!&H2Y3!=')8qu?]tq#L<np](?r!Wr9%r;uou
p]1<prW<$#rrW3$nGj^6"UGSN$jd1D%j</L?')2(`lH9E\XmIo(aft)'+u-&%fQG0!<WAt!<!!!!U9[b
!rW/t!:Tt7!<NB-"pG,3!<N<'!!N]7"TSN0!!*35-!chE_RQ+P3=Gm*!!3#u#RLS5!!<H5#6Xl(#Qb)1
"9\f/!WhuprW2s!qucp!qZ-QqqZ6g"!<DTh!s/W3#lO`'!qH<s"TSN)":YnO!rN&n!WE0#!Sd\S!W<)m
!WN3$!W)j<!X/f0!!!00#m:55%LE:M)]05%&Hr.B!!*-'$kEdD!!!&q!;llm!!30&!rN0!!rW/p!<3*!
!rW6$!ri;k!!NB,#n7CP'EnaQ'bq8g'ce/-+Y5,j-RK`@+V4Pf"!/O&%K-8-!s//sr<!!"l2^hcr;l3a
)?BmB"U5,5!s/K(!!!66$j[1J#6b>C%13:A!<`N(!!Nc9!!!K0rW!6-#Qk&,!XB&<"8i-#!WrQ("9JZ,
!VQNm!W<)t"+U~>

%%EndBinary
grestore
np
grestore
gsave
125.841 410.531 mo
167.798 410.531 li
167.798 353.277 li
125.841 353.277 li
cp
clp
125.79 353.19 mo
167.81 353.19 li
167.81 410.61 li
125.79 410.61 li
cp
/0 /CSA get_res setcolorspace
gsave
clp
[1 0 0 -1 0 570 ]ct
[42.02 0 0 -57.42 125.79 216.81 ]ct
snap_to_device
Adobe_AGM_Image/AGMIMG_fl cf /ASCII85Decode fl /RunLengthDecode filter ddf
<<
/T 1
/W 116 
/H 159 
/M[116 0 0 -159 0 159 ]
/BC 8 
/I true
/D[0 1 0 1 0 1 0 1 ]
/DS [
[AGMIMG_fl 116 string /rs cvx /pop cvx] cvx
[AGMIMG_fl 116 string /rs cvx /pop cvx] cvx
[AGMIMG_fl 116 string /rs cvx /pop cvx] cvx
[AGMIMG_fl 116 string /rs cvx /pop cvx] cvx
]
/O 3
>>
%%BeginBinary: 1
img
jT#Da!WiH+o`PL'"U5/7"9S]%!#YhA"U#&9!!!*2&f2/c"U,8G&.]Eh&ISpOqu@$-!rr<&"UGA;!r`3"
!UBa_!;?Nn!rE*"!ri;i!!WK,"9SZ+!r`0&$4dg^"n;R!#nRII!W`<'!Wi9#"9AT."9S>urr`6%rrMZj
q#LEqrrW0#lMq=r#RUtN&I&4<$k3^Pn,O()%1*+="UGJC#Qt//!s8Z.!Wi9#quQTnncAIbqZ-EmmJmIq
"U"i/!WiT)!!WT2"p+c+"9&9%%LN=8!!<9)!WgjPrrN-$rWE0'rr`6%rrWN0"9eu6"Tnf,q#D96"U>88
!!3?4%L<FQ)DtN;ML]D>4=V9`%/g/+!W<#t!W2ot!TF+U!W3$!"9&B%!V$0f!!E<("9er,!!*-)rW!?2
*B7#1=[Fb^&I8RFrW!!#"TnT%!!3'!"9JZ.!s85trr`6%rrMBbq>oj]"To#=%hB!I!Vl^'(Go!#=[Ok`
&-`4<r;[0,!<<3)"U5,4!Wr<&!!;orq#L!emf<1bnc/gp!WW6$!WE'&('ss@&HMe1$N^D4!W`E($31&-
"oA9%!<N9&f)YdNrW<'$!<N<$!!rZ-!sAc3"p=u.rW)s!qu@T;"pYGB"qhpc,&sdEj42&T^<PKn_3.kI
"p5nV"9R$Pq>pEo!!2forrMusrrN&u*!$6K#6k;2!snr4;2VlmV3$1]Pc1jQD)`"*&Hqk/!<<0!!r`5r
!;lot!U0U_!VcWt!<N?*!VQL4!XK/A$3pP5#QOs$L:+@^Ndc\HVm)D"1^O-hqu?]trW!!#!Wr?'qZ6a!
quQQmp&X@WrW2Wk"9AZ2#6Ol)&-`+;!%b%bBKdFn>a)L:-5$1V"9Jc1"9SN%!W`?(mJuJOrW2s!!!2rs
#6=l/"U527!r`0%!<WE*qZ%Z=$P!mZ-]m&bSqDWIF(]]QH#AJ=c-sNo.ME%#&-;G(rW2Wkr;lfrq>g*f
q>^["!WrQ/!rDut!W2p?!X&c4"98[@XEnDH5s?e>/3P^;8ogAuS0/@C!!ir7!W<!#"9S]+rW)ouqZ-Nq
r;l?en,NUm!sAc3"7lL7!X8`/!!d5>HXoT34XqC#4"_mMD3UZW(^pBE&ebHMr;[$)"9S]+!Wr?'rrW-"
o`4jimf3@h!;QWo!VZR/!X&Q)":"r-!!302i&2>Z(B=F9"pk2.$l*Htf`2<i!<<6.!Wr?$!<WE#!!!&S
!;lln!!E?*"9o&2"9SQ&"p+o2"9JW*rW!uB!#-l8goQ$MEcc8>KU%FBK84DNB8*GRc#FO2*!c0;!!3'#
!!2cnq>p<jquQ<f"p+l1"pY83quH]s!!<3'rW"&F!!NsCY&ur],U+0F.QT4,.l8C^,=ZddUJ:dh&I&ID
rW!!("TnW&!W`?'qZ-Kpr;kgV#6=o0"pYD;!q?6m%:?8^(dg)-,oddO2_#dm//\d54DD$l:]h"B#mL8-
!X/].rW*!#rWE9)!Wh'V!s&E(!Vl`o!W2p9!<E0#"q(M5!!NB2!!.9X!WW3&#S.:H!s/W+#Q4W/#&mZS
!"]SH"pY&,!<`N&!;HTF!!E?*!s&E#!<WB*!s88u)](-FhJRseH[UL"Lk^S<Ljs]/SsG4SH$dlo4p)6J
$Np,'rW2]mq#U3irrMNf!!E3'rW<-%rW2`n*srgXY;8<c+s8*W-mg5h/LD]%:.[`)4@Z*X,lf;!#6"T)
"U"l,rW)ouqZ-Wsq?$Zti;`u^"9er3rW<6(!<N>r!$2T=X>E0k.OQSj,p40J*YoD<5<C\I0fY;n%KI@H
!r`0-"U+u1!WiH+"9S]+rW(jV!W`<'rW<0&!W2rs!VQKo!s\](!sSmA?2=O&!<WE#!"&c/!!!FMGQ7^J
"TAB(!<WH,!W2ro!VZTV!!NB)!s/K(rW3'#rW!-'!WiH,"9SK$.0]hm9C90"IpRGJH?OXdK7\AhH@pm%
I!9^OF'XXdYTjc!!WiH-!s&Gl!<*$!!r`5r!:'Uh!<WH,!<<0""9JZ-!Vl^<%5c4`.l[nV'bLli*?laM
)C-ph/h8>!-T!5X`g.,;&H2Y1"9\W(p&P$lqZ6`uli?n_$NU;1!<N?,"U"i+!rW9'"9S>u&LG/A-o___
*Z,J&()@Pj!XfeB(^qB&*X4?_C]FGH!!!)t"TAK(!Wh-XrW*<,!sAc2"9S]+!<3'!!Ug!n#GO3Y$31&.
rW)s$q?%?5#64r@$36_Y!"&]+"9\f0"9SH#rrN'"g].N\"U>89!s8H&rW!$&!<<,t!#l"G$kasFhj7;p
J9P^bKR\Q+Jq/5oI"6j&IsV*D%WlQ<b/%$h!sAi<"onW)nGrRir<!!"k5Ynl!W`9$!<WH+!!<H/pAb6t
(EFR2C)T2c(B>6`%hos)+X89]/1rS*,qCT)0euLrSN$KI!!N9$!<WDt!;urq!ri;b!"T)4"U5,4!sAc2
!WW?."Te>t$j$[7>7`bF*![Z*&J,Tf%LWID#7D%T&.TKq+;u.UMi]Xk!!ri3!!3B0!s/N)h#ITZ!<N?+
"o\]-"U"o+!WE'!!rW8u!"8l@"T\Ue%1ECD!!*3"!!iT,!s8T+!s8Z2!!!0+!!$1oqu?d%!s/2t!!<*$
qZ-TrjT#bm"pkVB"Tnc,!WW3%"TnZ'(^^up)%6j-BX-TGCgUdqKTC\<Lk^M4It.HH%XibTJ9l?bJ8&(g
Rb(:L"t:)q"TSN)nGrRir;us!kl;.n"9el/!<<0(!s/W1!r`0O!t,PH!!"$9QGQKU)\s2/*!Zlc()\/<
.5!5(.46Ml+WVm`*toZ+X!n#[!!<-"!<`N(!;HQn!W)ou!U'Ln!<i]7#R(>5"9el/"U>//!#>_I$jQb4
%6T-?4<tIL(*Fn9',1uc$2t/K"pG/7#RUb>(+C@F,\a;+!"],6!!!$*#6P#.q>fRV$ipA1!X&Z2"pY>:
"U+f+$ig8.":,>?"onW+#Qju*$3gKF`"rCR#R1M9q>^[#!sA]-!W2p*"98T*'USq%$NLD4p](<r"9&H#
!<*$!!9O80!WrQ/"pYA7!!392&Io-V%gN@g=g%>HWJ[-E?X.GiJqei0L4t5/IJeI*I=Hj"Isc^!Kk#7R
cCQ!b-PZdQ!<3)u!r`5r!:^$u!<N<*"U5/4!!*-+$O-G./.F_'d^4^;DBU/:)Aa>.$kO0l*$?LU/M&A!
,pjub+sJEl3Z^4LSok#5&dRn+rrMuu!!2`m!!2lqqu@0-!sAf5#R:G3!<NN8#Q=`B!!!KiM9)Q79i_Z6
#8.^j)\Wl!&If'Q#6tJ4"W.LP$4IOi1Hm!C7@S>u!#,b?!!EE,!s/M]!!<6'!X&B("9S`/"9\T("T\W(
!s8W(!"oSB!"/c,?-nri(CpoS#7:Y@!r;m#!<WH-!s8?""pPA6'aW&1oDf!q!s8Z/q>gNrn,WFgo`,F%
#7:kD!XB/C%2^E=1`(_ef?'k;>>\1p>[V#]G'\OcJV&H'I=(s='mb4SIY!0,Jp_WUE->9/nr+_4%1NC-
!<3*"!rW/^!#PkG$O[(;!<`B&!t5DG=eD^_G"aA-*-35J*>]e:(_dVu)BBqF,q(5m-mg2b,pjuc+rqUJ
0,6df@/pB0"8r3$!WiDt!<*#s!ri;q!;lli!$_UP$O[%:!<iK(#8%C]@&L/sE^UrZ#[IiI#o+0j'GV>s
'+c,n$OI(E#6tMA%1s9i(DRZ,/.t.\@/pH2"p+c*rW<-%m/[+dpAc$3!sAc3"p=u.!!!$"!!*0'!<`Q/
!WW<+r;[=:GZ,Fe!<i]8!!EK4#mU2*"T\Z,"9\i+!;lg&#n[@AK)bl["8Dir!rW5b!!NB)!WrK)pAd2U
$46k9!"^Cb!%`!"o"f`_<F'BUG&bB9BP2I1G'JFaIXQWjG^"=SG^4XaIt<3'IW8q@I;EP@hZQ%a'GL]=
!;QZf!<3)r!($\d!!*92%LW=<!!Eu9!"),S]n\cp'HAVS2_ot6*uQ:E)AsJ7+!DmU-7:2h-6sf[+X/*T
+r:b5/g;N'XV1^8#lO`)!X&Q)!VcZo!WE0"!VZTo!W<'"!VZQr!XB)>rW"&D'EA+D9:!S[7jo2n-6al^
D\`ik(DRVu(`*r&'+k]`r!O>M%M9?i(C^Tf.30NlX:kX8$NgA/!X&W.p&OmgquQTn#QXu0"pYD>"TnQ$
*<ZZT#QOi."pbS="HpQ"!!!'#'+"dK&.J[F#mUP,!!WH*!WrK*!W<!'!<<-#!!<50o`,!n!r`;l!;QU!
!<N?+"9S]"!$M@K%134R(CMO1^<![18kr`*C1^p\B5"npF)Q5CEcueVrd#K-G'.nLG'J=[I!g?jIt`]'
DKM7cUA#NJ)@HECrrM`lq>p3g!W`?'qZ%uF!!!*/%hT-K%1*"C;ja#(63dZ+(E=8,&fi'7,psf]+<;OK
,:"T6-5RsS,U4HT*ZZ4@+=Jfa(a;X+Bup>\%0le3!s8]/!VZTn!WN6#!VZQq!<E9$!rrDu!%@mJ"UY\C
!"&u3%9B!lLIr-i*$6:@&df6_@1sCg(_dSu)B'G/()7Jpr=Ai<'bM)p*[DR7*ChSl`rHAT#Qb#."9enr
!<3*!!WW8s!!iT-"9o):#R(8+!!`]<%1NLU!tGD<C6'P;!"B,;#Qt,-!WrQ-!<ri5o`,*q!<N?+r<3T4
"9JZ*%MAi2!!i]0q>^Krr;u6a#6=i,!s8Z-!VcX.!WrH'$OK%i_5i#h6;:cn?!UcQ$[HQ(CVOh/DK^&>
Fo6P(H$=FSFa&(VH@(!dI!pU"I<0"7A#&%#+:o%]!!*-%o)SRep&P'mq#CKt!s8W'!#R,;TS-/j#RqXc
%L`gd.30BLE[)hN,p=<?+XSQ`-R^>h,U4KV+<MXErYlLk,:F]S&JuL#Yt,*#$3L;/!X/]!!;HTk!<*!!
!r`9%!q?78."n:L<%JLm+<)%-%iQ].&J&:^'+Pcj&/?*%)&aA0(DRVtq%FDU)BK_-#S@e\X[NEq$O-_7
!sJer!!`N*!WiH+!Wi)s"p"f/"U>88qZ$s)!WWuE!!"j?8.#7qrs8T(!W`9$rW33*!sSu4oDeso!WrQ%
":>/0!"8i/EWuLJ"8W#t!WE/d!!!'!!r`9%!WE'S!WrE&"UkeH&./n>W5sci4[)SH>?,$EBOt^b@;Khs
DfBN7EGorEH?spbH?j^XGBeE3H4P@KH@:<gFGZE:BpZd_#7ge:rVus#!Ug$d!VQKn!WE'J!<N?'!!*<.
!!<3$15r,A,S(7u,8q.0*?,e0'bMB*E$$/@,Tn0R-n5-D$77#B+<M[H*?6";rYcCj+rhIT7Q2f-Sd,6&
#6Y#."p=c'q>g-grrDuu"9JW,!s/B$rrN*!,Qn/K!<<*SN2U;7&IfR'*>BA5)\`hm#7h;O%LrgZ&.T?k
)B8Yq!?)jT)#b?N().Gr()RVn-9Ee'?C:rs$jd+<!sShs!!<3%!<W6&!WiE(q#CR!!WrQ/!rN$3!<`E'
!!HEc%g)q7"pG)/!<`Q/rW!0)!<<3*"U"o"!;urr!Y#57!!!')!<Wfl!!N?'r;Zj!!;lla!!30&!r`9r
!WiB&!!*3,"pkYD"q2)7[]XOA4@)8%92SYi>[LfD@V91dDo-L4C3"93F*MtVH[L0dH$FRZH$Xa]G^+L[
I=HTgJVJDgGh=#L"p=i)rr_Zhr;lKi!!*-&"9\K#.kI!E80JHS%1Nj^'GM<!'b_<"',qs2*Zc1C+<Vs[
.k2tr-6jWS*?6%<)ZCTg)B0_@*?6F^/MKSs!<N9,!<<0+"S;]_!W<'"!WE*!!r;ls/-qT$8g=lZ%Ls*M
',_Ju&.AsW#7V/M%1EIQ%Lj'h)]Tn@+!)IDrYudp)AsA/()7T$&e>m++=0.L!!*--"98N/"7Z?t!<E6'
!s8Z.!Whro!W`?(r;[04%0-j=L&_8T!"8c+!!3-$qZ$j&"9er5"p>#,!WN6#!W)lr!W<!"!<WK(!"8u1
!XEfI"TSf0!!!'!!;urb!!**%r<!r>!W`9$!X8r@((_N85GuhP4\&7B92Sel<)rlt#$>5F@r$#$$#slt
E,KQ7G^4W7Hi\S?rcnisH$OXYG'J=\IXM-?#B5!!fbbb1!r`0%"U"i,n,W@eo`,$o!<W6'%gN(?%3L8%
:(S3\(_[]*)?(?b'G:rg'cIc)*,lr>(a'qE-S-eu.1%CK+s%^C)B'J2rYQ@f)]g+C*?HFN3A.N9%0-P3
!!3E0!V?Bg!WN5r!AOWW!<E0#!<N?+#QP/A,)3-q&fMf0'c7o-'+kcb$4$hC%L*:M?k!JI%1E[Y(`OJ;
r?2@f+<M[H*?5h5)&O/,(D@;i',<&CVuR2*#6=f+#6aPs#lt&.!WrQ.!s/Mq!#5P>#7LY:&-+))!!!E-
!!il>"p"c,qZ%*."pbM@"TeZ(!WrQ.!s8H&p&G-p!sJT'!<W</!">e+"TT#9!!!&]!&XcY!sAZ+!sAZ*
!sJo@"q;7dNp:j4-Vm8q6qpQZ;GU.h<``C,@;'.dDo?X6BQ%d+Ed)eSrd4Zkr-8p"GB\4SH$apbG^"CM
G%9GJ(^0d;!!N?*rW2KgrW2]m"p+c)!WrK/rW"DKDoPTR!$2gX$P=*h'+YZg',2&l()mo))f?Z8(EXbC
-S-eu.46Aa*?4tqq\U"b)]]k9*$HF]/[k]c!!<3$!XJu2quHKlpAt6n$ipA1!<<-&!!!$$!=&N'%Kg^l
;ZHe@(C(?]'bq;grX9JK#R1VG"q(iH$jm+G$k3gd)]^"Cr#m"%+<MXF)]BS1()7Ai$kX(!,Hq.P!!NB'
!sf&!!<3*"!r`9&!Whon!<NH(!!<<B^^U)?!s/T1!r)a,!sJl6"pG&.!!36*"9S]+!V??m!X&E%$j6P1
$EX:3!"K/4!!2orrW2Ee2us*a!W`E/"9AZ5"W%pm5LYic69@V076j@>;,C"^:fCG">[:fQ@r$##E,K?-
DJjK=G^+L[H$T72rHA]qH$X[WGC+1IC?-9E%/g2+"T8Aa!!iT*!!*3'!!*3V!"/u7-FRq9(_.8u%gNLU
&eGK\%1j3h'bhH'',VX))]BJ6+!E!_/1N%o,9ImD)?(KM(D@W'(D[r6*\T=\!!!6)!!!*,"Te,nqZ6Qo
"T\Z)!!*6%!"/l/$O-e_[r`c3&/QH.&I8gZ&Io-R#RUtL$OI1N"q(iG$OHqE$k3jf)]Tn@q]He!*Zc=A
)]0>)'+G9W'+cB;ZN't2"9JQ*#R'SrrrN'"rrMoq!W`9$rW*9)(^UY90)tt_o`4jh!<E<$":5)/!!*-'
!s/K(o)SdlrW!?3!!!7u!!N?2"98E&rW)s!rrDuumf4j=!X&T-"UG>;%2Kim&:rb;6S:,Q5t=C69iFtg
:f(%i=^><>@qfIhDo-H!DJ*m)DK9rGGQ)jaG5um`G7&J5FE_VGCZ-*@%K-8-"9\N%lMrgD!WrK)!sA]+
"Ukh?!,0;+*sMoT&/#H]&/5ci%Lip]'c7]#(E*r()Jg<1'cnG>-7gYr-6ra<*ZQ%7)#>'J((h5o(EX\S
1q*Gb#Qau+!sf&2jT%1>!W`9&!s/H+$k31:BuMnP#RCbL'FtWa'G:l`#mgtK%h&dR%L*:L?4.)C$k*RY
)&jM7*?P,#rZ;(['cRu)'+kTX$4mds/$T'S#m:;0":#%r!;llo!"T)3!WrK("on])!Sm_U$j?J.!s/Q,
!qlU"!<N<)!W`9%!WE0#!V-3q!<E0#!=/Z*#m?Xr!<<K1!!!'!!;HT`!&=TX"9f#:$P!I]&1#Sg1H?p<
4A&%,7o3/c<E)mq<**7/?!_#S@r#u!Df'-)D/F<;GPlXaFoHR]G7A_=F`VPCF`2S@h%^G.r;Zj$"8`,c
!!NB)!sA`/rWG+_!"Ao>[sSl*"9f8R&df*_()@Ss&J,Ng(E"#((E4#))Jg<0'cnD=-7^Pn,pFEO)]9J/
(Dcrc'G_Dt'G:ul*$@0rZ2ak0!rr<'#R1)*rrN*!mJo0H!<<-%!sAT5!"l_h()I/[&0)>j%MTWm&e>EZ
$OdLV%13LS#7M&K$jm+H$k3jf)B'P6*$$(!*rI#n*#KD'&.8^K%hpTHXT/>-"p4i.#6X8lp](a(!WrN-
"TSr2!7aaW$N1#(!!EE3#Qt5&!;6Hc!<3)s!"&`4!!!%["98E/"8`)s!WN6#!Ug!g!WE-S"ptJ5!"qE)
BKJOB2).0a76sIA<*!!t;GpFn=Bf!7@:s%aDS^7.B5VR'Ed)_NFo6@\Fnp1gF`VPCF`2P<gCju(r;cj"
q>p9i!!2rs#lt)0"9er2!WrT)!!NBNThHCI.hi?n$Pa0X%29Nl'G:uh&el-"(DRc,'H%g+)As50*?QRW
.4-8^*ZQ(8(]"m]'bhAt',)-&+?)!Z!!!9,!<<3-"oA;u!Vufo!VHEm!WE'1!@X[:*?c1-"Uu7Z#n7O^
'-7\p$jm@N%M'!U%1idS%U]_R"UtnN',_]+)&aD4*<$uV*#0D1'b_/f$4@F\/h*n&!"&o5!!EN/k5Ybg
!!!$$!!!*)qu?eb!!r<!"9\r5!Wi)srW)`pnGrRiqZ$X!$N:#/Mu`nY#m0u(r;lm!rrMHd$N^J>!"pc9
Z:$2b/H.U85=S(08l/Gd<)W]m&5uS2=BT!C@;0SoDJa$(D/BDrGB\1Or,_jZqK33iG'%eIGA_S7fFSAs
r;cj!rrN-$qZ6NnqZ/q^!!*0)"U,#2!WiN*";u3I-OKhW%13:I&.AjS&JGfj&J,Ne'GhW(()\,-)B3N4
)AO85*[E0^,U"3K)Aj8+!#GAF&f)5t'cA/<2(u-5!!`W-!!<H/qZ-WtrW2lr!W`?(rW2Wk.fpQ-ROARE
#S7FO%1s$U$kO!^%L`[N$4@:Q$jmFT#n@JS%L`OO%1X$h)?(HV)&aG5*$"qs"rnU%)&<r#&.]3\'c/DL
WrN,+#6b)1"p3ugr;dE2"98E&"onZ(#\seJ!X8i)!<*'#!qcQn!WN6"!U'La":P2/!/UUS!=8i*!;lls
!ri;u!;cfp!&joY!!Wl?!!"<D]i-"">;\H$4?u;(85)iX;c?Rk:f("f<E3++A70(e^i!t#DJa93GBS(L
EcM)!rcA!Z%s<#<GBJ"NH#7P:cjL6`!r`0%!Wi?&rW<'#rW2lr!!3'#r;dZ8!sJo4!=92?!!!`tUc&2S
1C=Np#RUJ<!t>eR')iIa&ebur)&O,-*Yo\7DB'Q0*?6(E-RBrY*#]\2()@Y_'`JgR(Dmr**$c[]2Q6TT
"UG21!XAl*!<*'"!W2rt!W3#o!!!3%!"T`,Uc/8V2@U0($OdIQ$P!(F!=TA8$5j3[%L`[R&IK$[@LinQ
%h9'_)&O/*()If*q\g7i)]BS1()7Gn',_T80VnaL!Xf24!sShj!!**%"9S`/"9\Q%!tF5i"8;cs!<N;q
!<*#s!r`5d!"Ar/!!Nc2!![`Q!!!9+qu?]tr;ls$rW<*#quHQo%0-A/!WrE&$5XKd%XZ;2-pK170KLdF
6:4+19MSA\;Gp@hr_O;+;H$S"@pWe`^MRe!DJa93GBS(Krc%jVr,NBjF*)PJGBS+RHYdJ=`s<1U"o\K,
!Wi?&!WiB'rW<*#qZ$Zu!Wr?%)$0jA"9o,6!"0JP!!$Z:$m#TX"UkA5$OR.>$iUV[%hK<b&ebro(E"&+
)BK\7*H)o:'ce87+snQX*?#b2()@Ya'GqJs'GM8t(`=20+=86_5G.uW!"/o0!X8c(!!!-#!WW8u!!!&t
!WW8t!#,GA#ljs:YRDTZ$4%.B#7_1M$k<dH%0$_7$5j3[%1<LQ&do6_@h9+U%h9*`(`4#''GVB"q\fAO
!#bbP&/5cn*#Kq^S,`Tj%gN(9"Tdif!W`?)qZIQ4"one"!!3H2(C'p?"Tnc,!s/Mt!<*#u!riB%!ri;e
!"Ar/!!Wi3!"N`P!!!6)qu?]tq#^Kqp])K>"9o)7":,;="p=pF^Gn5'/MT1F2*=5n6qC$J:f1+g;,R<h
'N%b,<Eis>B5>8"ChIX&DKC#FF)_2!rbqaSrG`BhF*)PKG'8.XD/4C.&Ie^DrVus$!rE#u"9/H&!VQL!
!X/f7#6bA>"9&9&?)Sb^rWb%_$3CG?#m^nK%h9*\&.oNg'GVH&(`+)4(E=H6*?,_6*$$4M,Tn'E(`*r&
'GUKZ%29Nl()Rr.)^-US/4Gj'!!N]3!!3?,qZ-WurrW3$p&G0q!WrN"!"rG2*#](h$4RFK$4[IO$kEgW
%/pVN$47.K$k3RO%MB-\&Ru@^#S.CT',VN#rY,AJ(AesJ)$h&q()@St(*".m,<q=i!!Nf9!!3<*k5YVd
!WrT0qu?_fr;[3,%L)n5!s/K)"9S]!!<3)u!riB%!ri;e!"8l.!!N`1!XW<@!!!3$!!3-#!Vlcs!W<'"
!Vud?!sf;E#mLqX#m_/V[n%i%0fM!K3Bf\q6q'[A:Jand;Gg<j:_ci+;cR(4?Y=/hDJWs(DJjN>G&qYA
qelCO"`SF#EcZ@%FpWJBDejg,)[cWJrW!$'!s&H$!!<?+!s8E%p])37#R_%F!t,\@!!6)l/I2ps%grXK
$4@4K#n-_B+qG1q&J>`k'c7f*(E4G4*$&r<)\jA5*?lgU+<;=:()7Pur=]t]'GVB!(`F;3+XeWg9T0&R
!!r],!<rZ'!<*'#!rW0!!;ca$!X/f5!!!$(rW!7!RjnUS%1isV$iUV@%1E[V%LijUq[45L%1<LQ&do6`
@h9+U%h9'_(Ddf#',2/sr"fk\(`=2-()7Mr&JZ6%,"%(`!!N`6!!3?+lMpncr;Zfu%06S:!!WE'`;fl@
!"925":"u.!!*-'!s//srW2cqrrMHd%06J0!!ET/"pJ-3"98Q&!!30$!VZZp!rrAu!"T8E&J,6K!"T/>
<m36K0.@G]0/P[N5!VG&7S6BN:f1+gr)"5-<)cn'A7'"d^i""%Df0K7G]n.JDf5Dg'5h]+E,fo>F`hkR
I;s+VWuDQL!r`0%"U"l-r;Zp&"9S`'!Vl^1"UtnJ!<<*#!!#9k'FbKS!X/i;$4Hh?!=K;9%fHn[&.fEe
'GVH&(`+,5(E=H6*?,b8*??=N,Tn*G(`!i#r"Bk\'c%Q$(`F;4+t+fl;MP>U!!`N)!<r](!!<?+!s8B$
q#CL"$4-k4!"(`h%gi[I!X8r?%K6hC%1NdX%h9$W%/^JM$k3UQ%MB-\&n;I_#S.@S&f2;t'+trm(&SgX
(Ddo*()7Ms&J,Wo(a;M"rW!*-!rrB,!pTah!W`9'"9\T&!s-XH!r`0."pP,2!s&B%!<N?)!VcZo!Vuls
!WW8i!"]/2!!**#!!<H,!tR[-!<<3"!<*#q!WiB("9&E'!r;m>#Se'e%13@_1`j8%2EaGa/13,54[)(s
6q9jD:/Fec;Z0H.;H$Rq=']?EBPbJ%D.dd)Dfg5IF)c'uD/B,c'PqT&DJsK6EccGJH[TsQN27@(!!3'!
!XAo2qu@!+"9S]+!<N<'q#D*6&Io'I!!!?H"J7:_)]oLk!!<W<rX&`8$k3^F%iu8n&J>cm(`=/,)BTb8
*H)r;(*4J;,:=c\*?#b1(&ejL&ebom'bqK#(Dn&0*?lp]0O021"oni-!!*9,qZ$a%"9S]+rW3'#q#CL#
%LN=:!"9M@QmWL_*=N#M":bq@%1*LT&.f?_%LigTr<jGO%1EUS&do6_@h9+T%h/s\()@St&ebomr"T2I
rYGkV'+tlf%h]Zq+UV"i!!*'(!<<0*"8)Wq!<E8t!!!-#"V:b;"UG).ScAuq!"B27!<N<#!!!'!!WW8r
!;urn!ri;k!;lj+!WW3&"T\T@.N&3d!WE*!!WN3!!rW-'!WrQ/"U"T$+9W8_)\No=,o,'E3'/WO2)6gA
3]oSk6:FF;9MSA\;H!Hj),aC5<``U=?taAlDJa'+Df9`BG&qV?ChmebBcCf%CMRa'DK'T:Fa&4^FDID:
'G:BH!!!$*"p4]&"9er3!Wi6#q#D$.$NLV:!#5e?\4%,J"VM7M!X8Q1!t,JF%K6k:%j)>o&J>`l(E"&+
)BTb8*cN,>(*4J;,:=c\*?#b1'GLHY)&!Yt()Ic()&aG8,:Y/rD0l6f!!WE'!<iW'!!i]1!s/K(!WiE!
!#Yb:#lk52!"8i-YWWL/!>#VD!X9#A%1WmZr=BqZ%h9$W$k!FO%1N^R%MB-\&n;I_#7_1P&Jc)prY#5E
r"KYV()@]$&ePZb%MBQo*aWa`!!NN,!!3?,p&P*nrrW&t$N^G2!<<?9"TSN*^AIs5#7(G6qZ$a"!<N9&
p]16np]CHrnc8Rg$3C80!!39)!YcgoqZ-TrquZft"p+l0"U5)1rW!`;"U>#@%O*i]]$JKq.R#pN2)mQU
3&iu+5=%Y*7nH?J:Jgpc3)W[T<`i[>?taAlDf06-DfBfCGB7_?CMIQsB4kmkBkhF"D/XE8Fa/=aF_RqA
&.nmD!!!',#6Xl(!sSo3!rW/s!#Ye?#65,4&0YSQXJC=J()%#_%1EUN#71bHrXJf9rsp.^&.oNg'c.`)
(E+A3*?K/?*#9V;*[<$Y+WVI;()6ZZ(_[W"(Dmu-)]TqG.P!*#F8uLF#6=f)"U"W%!sJf0!rN)s!"f88
"ono/$QEB7URZQ/&.SmMrX/i8#RV"Oq@Ec?%h9$WrX/i;%1EUS&eYQ`&n;I_#7_1P&JZ#o&eP]gq\'JS
'c%Q!&eGQ_%1s?l)K'-c!!NN,!!3?,p&G'nrW3'#r;[Q8#7(;0#6Or+:lM^p"98T,!WWB0"8`)t!VHHl
!WE0""8r9$!<</l!;urt!XJf,!<WB,&02>Z!<*#s!rW-M!WrQ0"pG,1!!39(!!!0QL!ZkY4taNK0eb@@
4$5Sb2`a,g6q0[;8k_uVr_X5':f1+i<`W=/ART:h^i++(rbr3eH$==KD/3iuAnE#pAnPaiBkqO&E-$2J
IXlTU\;^h,!!<3$!t#;9qu?g'"U"r+!W)is!W<!4)fN*@&/52.-j0YW$4dUT#mLYB%/gY=%1WjY&,m+g
&J>co)&F)-*u>q=E#ou8+!)LL-m^#W)Aa,%&eP]g&ebuq(`=20*"a26,qCQ"Mf/S"!!`N)!!EB)qu?g&
"9S`'!W2ot!rW*5(i$7,#Rg]j+TMKC"q1nJ#R:YF&,m1<&-<@O%/pVJ$k3RP%MB-]&nDO`#7_1O&/>ll
r=So>%hfWl'b_/i%LijY'c.d6?iC$/"T\T)"pFZ#$3://!s8T*!!!')qu@3]\L%^b!'CSg!!36&!sJN%
rW2TjrW3$#qucp"rW2Zlr;liurW*3)!Wa2O$N^/*rW2s!!!<'!/-?"Z#6kA8!WiH+#R<02Jj1hM5<Q5B
4t\WN5<_.h3''5h77Kd<8P;cR;,R<h3Di[R<``C1AmoCj_/F4*EH#l>H$==KChdWqARo=_AS,RgC2@d,
Ecu_WJ9YkGKa/+g"98E)$O?k4!!EK0"9JW%!;ca7"99aZBH@Bk%h!q(%KHV<&.]0T"pYJE%hB0L%06qL
r=Bn[&el)u(D[o2(EFQ9*ZPt<*ZlXU,p=9I(DRV^&K28q'c.]))B0Y;+=/Nj0U?AP"TSf/!!!-(!W2p"
"U"o/qZ6Qo"9ecM[q$3k!=K/8Gn:5]!!Nf@$4$hA$kEs`&c3+@%h9$I$Q'9]$OR@V$P="^&Io$U$k*[]
'G:uh&.oNO&e5Qh'G:re%1EXV'Gqa?=8i1'"T\T)"pFZ#)Z]s@!s8Z.!<<0)!<<*$Z2kI9!!EZG#64`+
!s&H(qZ$[!!<MclrW3$#qucp"r;lTlr;d$&!WrN+r;d!#/-Z=X!WE)t!W<'"!W<!E!X&]5#6kA<"UG)S
45<t!8O>Bf3k@dF0K2$W5<_.i4?l/$7RmYR8P;cR;,R9g%8p/+='/d?@;0SpDf0:gE$odRGB7\<BkM!f
@q0%[AS,RhCMe$2G'SOcH>UcH$jlt<!!!-0#Qsu)!sJf/!Vl^7!WW9%*A5K#)C64,!!S)i$igJ=&.]3W
#RLkJrXSo:!=fY=&-3@U2\[#E(D[o1(EFQ:*ZZ%=*ZlXU,p=9H().An&.oKe',;<#)&aG6*Zu^V0J]5&
!!*'*!WW3&!rDs""9S]+rW)ou,6.`H!<`BD0$-<o+;+_U!.P@\!!*94$k!@H#n.=V&J,Ka&,m+A%h/sH
$OI4N$OR@V$P=%`$5!dS%L`aX'bh8mrX])B')`CQ&eYik&eGN^$k*XZ)BF`,rW!*+!WW9+"82]r!<NB&
":58;!rr<&&tf4.qu?^<rW!$%!s/N#!!*-%nc8XirrW*#rW<$!rrDipquI3-!WrN+!<E0$!(6eirW2uu
r;liu!!3#u.KKVU#mLM<$k!RX2mu+K*\TZ:1/YbK68Uee5<hCs4[)/!77Kd;8P;cRqbR`"<*!(&?=dPZ
D8L70B`;rVG'\@QDJEisAGfp<A7Z!YBPVI(F*;m/HjjuAA.SqF"p"],$3p\2!!36(!W2p@!<<*%#6Y58
.ASLK!!a&?!#gUu%06eD%M'$X$471N%M&FH!=fY<&/l/p()Ri')''M6+)rAC(EOV>,Uar]*#KD(')iFP
&J5Zk(Dn#.)]Tk?+XJiE25WtE!!NT/!!!'%qZ$["!Wi6"+9;NE!!<K2#RDrW/2$u*$NU5@J,olT":#8B
$jm:K%1iFL!=o\=%j)8j$O[:L$k3RO%MB-^'P7sg#S%:Q&JYum&.]9_&JG'T!>#kB&do9_%h9$X%M0X(
P;rOA"9nr.!X/Q+o`,L'!sJf0$4[:@%0GVm!sJ`)!!*WRrVus"!r`5u!<3)i!<3*"!rN0"!rW/k!"]/4
!sA`/!<<*$!+,^/!WiE%!;QWq!W2pH!s]/:!<WZ8,8e0k3(,AL>pqm6[l[)?5<_:s5sR\$6:4.07Rp$C
9i(ab*D]I-;H-[u=C,NGBl:e,DJ4!-E-?POEc#N'ARo<L@MrZdAnYprE-$5LH[:*[gK"Ud!<rQ)":5;8
qu?a!!W2p"!<N6$)?9sD(^[6$)^>Ug/H?"mIfp>e$k*UU%h/pUq$d?7&,Ztl&ec#t()7]-(*+K;*uu+<
*ZlXU,p4-C'G:uh%hK9a&el)u)&aG6*?H:G0fH:!rW!B4!<<*$!<<*#!<<*$!W2ou!X/K&#mLMN%'MZ3
+pJ#\-ia5ZGQ8*O"pYGB$k*LP%1WmZr!ii?%LigSrX'SQ$k!CO&e#BfB+kg^%LijZ()7Gn%M'*_&eP`T
&.T9b&ePZc%LrpW%j*$g/H,VQ#6Or-"U"Dt'ESCA"9JZ1!>PU4"9nr.!!iW+%NYHI!!30&!W<#t!V$0i
!WE0!"9/H%!W<#o!W2p#!<WH."9&9*!W[KG!s/N)r;Zj!!;cfp!$).I$NpG1#6YTKV`Qpk9NXnS3D6V=
9Kkd-5<qM$r^-fV6q'R8"\D?\:/Fdd:HD<M<*!(&?"@>WDSg@1BQ%g.G'\@QD.mNl@q&nU@:E_WAS5ap
E-$5LH[1'\i^s:[!sJ]*!sf)5!VQKo!<`<$)[-3D:lQG2#9kW7%0.#c";M4Q%1NdX%h9'Y%K-\;%1NdX
r"&lA',VK$()7Z+(*+K;*uu+;*?QOU,p4*A'+kfT%g`dY&el)u)&aG6rZ)7c1,l`u!!*''rW!!#!<Dut
qZ$X!"o\K<"98U)Os(_K+X[p.!"*ZF%KZn@#RUqJrXJi:r=/`9&.K!S#mgqH$k!CO&e#EgBG;-l#nIIS
&f)2p%h9'\&J>Zf&.]<`rXfJK%hB-[%1XO.W$2-?"U>/1!X&W&!!!&t!#,J<#6Y#,!W`Z/7K<i*!XTDD
!=]qE!!NE+!W`9$rW2KgrrN*#rWE-$rW2uurrMrsqu?j#!sJi1rW!0*!0mNd!<WE#!;cfq!!E<*#n$n8
!#GqO\TKJf1dal+8NT\Q4A7q+5X7V%6UUf?#Xq3R8P;`P:Jh$d)c0F3<`W:-A70+h_f9R,Df9T<HZsIG
B4YR^@f9^:@UiscB52:&F*DtXG_'ql4pMK!"98E(#R1A3p&G*p"8r3;!W\oo#Sm^^)%mJ\'6jTo#S%:R
%M''[%Lr=E!t>\L&,Ztj&JGlq().T*'c\<:*ul%:*?QOU,p+!=&ePWb%M'']&el)u)&aG6*??+>1H,KE
-3+,J"8`&u!W<)s!!30("oSE;!Wo6'%N5]i((LZO$ZH(T!=/o9$4@7Nq[NQ6r=(+_$OR1H$4@7L#n7LU
',G<t&.&jV%MKWn&e>E]%hTEe&J,H`&.fHQ&-rdW&.T0q.&@aZ!!NQ/!!39*qZ$Tsqu@E3"9el-!WiH(
OUqQp#6>&<"p#2NquH]u!!<'!n,WFgrrW0%rW<*#r;ccsrrW0#qu?j#!sJl2rW!0+!42_-!!<<!!;llr
!!EB.#n$n8!#-(jd6ou]4?#Ag9fu:\5"e(,5s[j:6iKIY77Kd<8P;`Pr(e8.;H-[t=']?DBPtb.D.dd*
E-?SPEGK/s@U`dE?lEH`A7fRnE-$8OH[13beM@[E"TeZ(!XAl2!VZQq!<NB%!!3Q@Zk"/e'b(?P$53CS
H3=ld%Lr@I":bkM$k*%C!t>_M&,ZtW&JGlq'bhH('cS69*ubq8*?QRV,p!p;&J,KP%M]Kc&JGos)&aG6
*??(<1H;KV!!E<'qZ$Tsr;uls!s&H+"T8<0$l$9!'cISe"U,>8%<;XQ$igM;#n$Y>oaE#P$4-tE#n%.K
#n7LT&f5=!&.&jW%MKZp&e>E]%hTEe&J4pPq@F2M%hC!:T+1i$!<iN)!X&T+quH`tqu@B2!W`9'!X\ql
!!*B0!<WK,!=p+I!!!*""9JZ,!r`5i!<*#u!WW?%!r`6!!<*#t!ri;u!!<<-#6b#+#6b+P!!3-&"82`n
!<iN-"pbM<rW"/S.*+8,5<h7n5t""<[Q[>J6UF.-6pj=06q'O67n?3E9MSC^:HMBN<*!%$?"@;TDT$L2
AT2R,G'eFPC1Uj`@:3JM?XR;OA7fOmE-$8OI=-BdcR0G<"p"](!X8f1!Wi)sr;llt+oqr`V[3\>$j[(C
#Qtri";;"L%M'*^%LijU$k!FO$k3[Wq[`rD',;;u'Gi8>'H8-8*ubn8*?QRV,p!m9&.]6\%1WjY&JGlq
)&aG5*$$"?.m0^A#R1>+!!**%rWE*!"9AQ*!sAK%!XKUFrXoeR#Qt52!"X)M$NLA9#mq%J$MY#.$l'-W
#m^eC$4I7J%2''^(Macu#S@RX%MT`q&e>B[%hTEe&J#?]rX\r=&J5Wg'Hf)t"98K)!s&B'"9S]&!!*-%
p])98!WrG@!!!*)"9S]*!X9\G!<<-&"U,#3!s/N)mf<=frW3'%rW<*#quH]sr<!!"qZ$^#"pY;1!!if0
f)PmQ!X&Pu!$;4B!WiH,"pYD:!<EH6/[7&p4$Z/"5rqM;[m!JL6UL`>$U[<M77Ka:84cHJ:Adm):f:7o
='/a=?Y=2lDf'*)DfKrIG&M))@K'[5?O'tI@qB@kE,uA2I=HcgHcmEI%gW(6"9AZ0!s8H&qu?d"!Wi9#
'`eIG";m+"$3^bF#mLA8)0uAt"q;(A&.K*Y$k*LO$k*RS%M'*_r=BhY',;8t'Gh]&)BNl>)\a;5+!i?]
*>]:u%fHhN%M'*a'c.`+)]Kb;*?cXlUB_23!r;ls!rW6#!!!&t!Z:t<!XAfHPRJ35%1NOD!!*XO!"&]0
#7:hHr<i9,!=B/4#TX3Y$OR1L&e#BgC)%<e&J#Bd)&<hp$k3^Z'+tier=05H%hK9a&el#t)E!l^rWEE-
!<<0'!s/?#!rrB(!VZR,"9;6u!rrB-!rr<(!$VCF!!<B'"U"r1!WiDj!<3)r!ri<!!<3)t!ri;u!!<<-
#6b#+#RLO_!!E9'"Te>t#lt&.!WrQ/#6tAH!<<?519`N"5!_J"5WVG<\3NbQ6ppoA$UdEP7Rfm=8P2WL
:&[m+:JXeb<EE7(?=[GWC;"@rDej61GC"CLB4>9J?QWT\?!^lG@V'7jE--ASJ:M`bfFel.#6=f)!X/`0
!Wi,t!WiB'rW!9+"UbJRMZF1k$47+E"98`GHNXue%1`@K!Y5_Lr!Wc=%Ls!\&J>!R(_IDq()7N")\j;2
D&=*2)&s_E.3ooL&.\[K((:W]%M06f(E",1)]Tk<+<rnM!!`Z/q>^Krr<*$!!!3$"(BFL9!<rWJOp_p4
%134<!!*[P!"/c2#6G5?$iUM,$NUS@rWjMN$4@1J%MK9b'P7pf'+GH`'c@c!%LW[U&JGcg&,cqQ%M'*_
&JGlo)&k<-!!*0*"9JT*!s8T%!!33'!VcWs!<r[$r;[30!rr<(!$_IG!!<B'"U"r1!WiE%!:g-h!W)rt
!W)ls!W<'"!Vucu!sJo4rW!3/!6kKF!!3<*p&P'm.foeV"pY51!!E`e[5LB>69[Ru4@iVd5u0d86q'O6
7R]d97n6*@8P2WL:&[lh:JXh';cQn$>$kfKBP4bbB6S$+EHc\MD.[2S?63BW>[:ZC@:X%gE--ASJ:M`_
i!Kr&#6Fl*!X/]/!Vl`q!W2p3!sf)PO9?%%$3gV8!!jHi"V_1O%fR"A%h9$XrX8r>%1WmZ&Gm%H',22s
'Gh]')]3,o'GVr1*$?OU,9.F/q@"#H&/#]o)&aG5*$$"@+uZn1!!35u!!!&u"8r5u!WW9#!!rc2+I3HO
&I\jErW!<<ErZRJ"pYJB$O[=8$N^YB$2t22#n$Y>&.T?`'G=a^$lfTa&Jc3!&Ifok$k<j_&eGN^$k*RS
%M03b'G_H%*A=Vs!!3<-"9JZ.!s/<"!WrK)p](Bs$3t)>!##J9!!!-%+ohZE!WrQ/"9\f.!Wh`irW2lt
rW2lrrW3$#rrN&urW!$%"U5).!!i`.[K$=.!X/Yt!$qXH!sAf5!WW3(#qa"Q7n#d/5!V5%>.[-u6:XI6
7Ros<7n6*@r^eD.91qrQ:/4S];,^Is=^,6E@V]>PC1hL$DK0iEF)5Do?!LW?>lIq9?!h#NBPh^1H@LHt
E".BD%h&^J"9AK)"U"l-nc0@+#m(s8"qhFS"p4r-#TA'o'aP9ZrX]&?rXSo:":bnP%hSUM(D7Aq'bqE!
)]'M+>T":u)''hG-mKZF%K6_K$k!FO%1a'c(E",1)]Tk<+WWqGp](?q!!3$#r;cft!<N<$!!i]-)5@ZY
'+G-D!!j0X!"8i3#71b9$iCG3$iUJV#mgkD#mq(K$kF!_(CF1U%M]Hb&f)<!&I]!S%M9?e&.\XI$OmRW
&JGio(EFAWTDefq":#)4!sA],qu?a"!rDs+!<<*#!XJdr!!3-#!r`0)"TT_H!<<-%rWE?+!WiB'mf<=f
qZ?`tq>gEoq#CKu"9eo,!!ic2K`D/S!<iSr!!NE+"U5#.(B=UC,gJDA7RK@'5s7eD]L5Xb84H'=8,Z!X
8cD=(91qrQ9hnJ\;H-\!>$PHHA8GJBDeWg%E,g#EEb])ir*0/()I-TV@q]^uFF&FeKkum['ak0J"Te],
"p=u.nc0"!$31U;#o+$]#6YP?!!jKk"r.FT%hK<b&.]<L%f[(>&H!+B&eYilrY6(_)AjM(:EC>f*ZlLN
-R'HB$jm@>$P*XV&JQ$!)B0Y9*?6:A;N(JR!!2rs!<E9$"8i/t!WE')"99":&/u;m"oSE+&Te!^!!``8
!"/]5rX8c9rXAf7rX/Q0*=</_$k3a]&K(dF(_@)h&ec#t'bCc[$Om[]&e>HM$O[@Q&.oQi(De20:l,)N
!Wr]4rWE6(!W2ou!s8B#$3:2/!!33+!7UuRqZ$[%!$_@A!!3'$rrW0#r;cEhrW2ltrW2corrMlp!s&K,
!r`0*#RsT7"98E*"7cF2!<NE/!<<*%$QI;O91D<85smh.?G&^*77g!>rCHr[r(?r]#>@fc:/=_b<#8V=
>?tZKA8#S5EG0!&E,g#DEG8ic=]t`-r`L.D?!h&RCiFNCIt35iQE(Z+#R(>4!<WN0!Whil(]t$I#HA4M
&Io-Q"onoKHj1>m%hB3`&J4mO!"Su=rt,2Bq[roC'`JgO(`F2/(-<Z_(D\#5+XJKZ)%m;`#mq%I$4@7P
&JQ$!)B0Y9*?-1@<e'fC!<E9$"8W#t!WE'*!W`M-&f_Pp#6Xr*#S_=[%KQe>#n$Y>!"Af8rs\o8rX/Q0
%13IO$k3a^&eu$;)\<JX'*T-g'G(WX*"!,d'+k`a$OR4K$OmX['GVH%+;e./!!!$&#6t/1!WrK)r;Zj#
!rW*$!<N?(rW!'+!8.>WqZ$[&!@%IB"9AT,!Wr<$n,WCfqZ?`tmf3Lk!!*-'!r`0*#SAKm!rr<)"TAGo
!"8o3"T\T'!>,sb5>4KE70l@J9O>G&<(9LZ8H)3\9))%!9MJ8Y;,^Ir>$PBCARo=kG]IJ3D/XE9F`;#%
=oMP'=oMM4>$PEDB5DR1H[pX"E1.3,&./dL!W`<)"pG&/nc0@+"Ub=-&K22k%LNIA$6=O"(CCZ`rXf,A
q[`Z;rXo&@(D@Gr'GVB#)Aa,3-Qs9C*$6=M-6O-;$N:A1$4dLS&JPut)B0Y9*ZH7C>&s?;"TSQ)!WrPs
!#,Y<W"pBc%grRC!!*dU!"K#7#71b:$O@.M%1WgV$k*OC$N:A2$60E^%1Ws`&J6$.*"WYo',23!'FtQW
$4RO[&J#<K$5X'Z&/#Zm)&OJ9>BBiF"U5,6"9\l2!Wi6""9S]+!!!-%!<WH+rW!'-!7UuRqZ$['![IUC
rW<'"mK!1dqZ?`tli@"drW!60'+5*J!!!0*!r`5n!!rZ."9AK&!tGaZ%RNlV7S--A6rI%'8QA5Qr^m)]
"%u9\:&[ib9+FWi:/Fhf<`iO1?XdPWB)Z["C27X(EHH;?B4"bA='&L+='&L,>[ClPCiOTEJU`;oVLfKj
%L2t6!<`T1!s.rm%g3+D!2UGN%M9<`$3LhQK*2Js$4maI&c!":&cE@@'/(%6'c%T'(`+88*Z5k9+!N!W
+;bXr#RC_D$4.%I%1j0g(`F>5*?H+A+D+UR!!E#s!!3$"oDf!s!2^VTrXTAC"98Z6H2nEU#7(\8$NLS8
%K6h@%1N^R$4?b=rX&f:$OdIT&cNFt)]BS-&eYim(Dmhs$O6tI&/,Wd$jm:I$474R&el-#(EXf7=o\O/
#6P&2"U,#1!W<!"!s/N&!!<9*"TnZ'":,"c!!W6"!XSrRquH`urrM`lq>gEoquZftli7(f!Wi9#!X0&7
rW!'%"9\f.rW2Zl!<WK(!"oDB#fT5,5Y"OA8k2uVb"Gc*9`@Z`9,:2q9hnGX9h\5R92&&U:f:7n=B]!<
@KC"Prb4!"Ci!m)EHH;?AmJJ<<E<1&<`W:)>[ClPCiFNDJUN,pZXk!`&-`+7!<`T1!s.rm'EnaH!2^YT
%2'Hh$jIIRL^P"+&.ndPrXer=r=\u@%ho]m()If*)AsA1*#fh<+p]J@*u>Fn#6tP5#ndRS&/,fr)B0Y:
*uQ1IF#a4#"o/,u!W<)m!#5P9!2^_X%1j-["TSu3If^)\#7(YDrX/`8%K6hB%1N^R$47(GrX/W4)%6uc
&J>cn'bhAt'G;)q(`3qt$O6tI&/,ZX%h&gE#o<pX&/#]p)]'SDG<Z65$jQh8"9er3!s/?#!WrK)rW!$%
"U5).!!EN,li7.b!!3K0,Q%Q@!UKg`!W<)u!UKgd!<<0"!!3<4!WE'%!X&W."8r8o!!*0)rW!W7$jt0K
:d.BG9h\,^9[$44852`MrCd5d:B"&h:B+&f9H?i';,^Ir=Bf'=@Us+cBP2'rChmp.FEDD4>ujs*rDjV6
=B\s:@V9LrFF&IbJ:"q.)[m5\#64`)!sJf/!V-4/":#,2WuW8i&fD>l#8[]'$lB<_&.oNf&J,NP&c<::
',M>t()If*)Aj5-*#fh=+seQY(CpcU#7(56'+#!T&/,cq)B0Y;+;l:NI4,*r"Si&r!<<2s!!!&u!#,G6
WuiGk%hoHW!"ApX!Y,28#71b:$OR:O%1WjW$k*LN$N:A2$6BQ_$k3^Y&el)q&el)q&el-")AWnn#RV"Q
'+tfb$iLDJ%1j-e(`X;5.tKA]":PJ8!WrT0"9S]'!!*0'r;Zp$"9el+!!ET.n,NUh!!<6.![@OBrW2?c
q>pTtr;l6br;llt!XoeLrVup#rWE3&r;lWm!W`B+rW!3)%1pl\;*@HJ&Pl+n>>NI<=\;F_9heAW9hnL`
:]aEg:Amm+:/Fed<EE=-?!q,PB5)$lC2@^%DK9iADJ!3Ur`(%@<``@*>?tWHBP_U-H%:6kID\Pq$4I%;
!!*0)!s/Mo!#,J="oteL+:/Z"'FkBb$],9/$5!jK')W@>'(utF'GVB"(`=5/(E*2k#9P0;-6O-9#lY#D
#6tM@$4RLY'c.c-*$-7A+YJHh"98Mu!;urp!<3)u!#,J7Y9P1r%i#NX!"AsX!=f)7#71_9$3:MCrXAi9
!t5PE$N1;0$9/D$%1a!^',;/n'GV;q'c7l0(_R8a$P!a^&eGN]$OR4K%1j-e(`X;5/rCqb":>84!<WH.
"9JW&!!*-%r;Zp#!sA])!"B;9mf3Lk!s8Q(!=/]LquH`tm/[.doE":Y!s&H)!WE'#'.+7h!!E?*"9S`)
!W2ot!W2p!!<WN(!##n]b?@Y+7o`D]93b?>:g-Lg:/:a`#Z+>p;Gg:f:J^sb%o6#"<)m"&>?tWGA7fLg
BdRS1CM[p0F`hV7?<:**<E3($=B\s:@:X%fDK0oNH$t7b3ZeS6"9&9&!WrN+quQHj'*JRBW@](t&KDMr
#T*u,$lB?a&cE@B&cE@>'DrRD',)&o()If*)&O2.)]Kb=,:=i^(_@Mi"pG/7#6tPB%1a'c(E",2+!V^K
1lW+Qli7(f!Wr<#'*A66/fb9.(CgWL%0:nY%0-S:#lP&1$4He@rsSi6r!E</"Ub_K%hTHQ'E/[X()e/5
)AE\h$P!a^&eGN^$k!^V$OmX['c7o**]0#u'*8FA!!*3$"9AQ)r;Zj"!W2p!!WrK&!"BDAjo>Sc"U>/1
!=&TIquH`tl2^MYli7"drW3'#rVup/!C@7p!!NB*"9S]+q>gNrr;Zm""9n`()%dq0BM(W`<`2ag?;o0I
>>.mi:f("c:f1-i;Zfop:f.-e%o?,$<)m"&>?tTFA7fLhCAquSCi=?:F`1o!=8l/=<E<1(>?tWHASGsu
E-HbTI"KWu*sDlN!<<*#!r;uk!#PbD#bj?r%MBct%ga'^M@CF2&J5Wh'+toV')WF='`A[H'GVG`(_%?#
)B'P7+=&<_+rLptr<3i=#7(YF%hTKl)&aJ;,TJ$fPmRig!;c`t!<WH&!#YqEUH9;$%MoTZ!"AsX!=]#5
"pbJ@#m^hEr<rT3q$I$-"UkhN&.oQS'E/[W(E4D;)\rtn$kEp`&ePWa%K6bO%M06e(`X832OP3n!X8Z*
!<N?+!s/N%!!*-%qu?g"!W`93!!!N7fDl-W#7:Y:!!N?EqZ$TsklCGYm/R.f!r`9%!WE'##\+,<!<*'#
!Vl]r!Wi6"!W`E-rW!6+%Mm3.7n-KV;$p/q?rYNO>u"<q;>jDm;uT_u;c6Ljr_O)%;H$Oq='8a5?XdPX
BPIE\#]+F"F`hV8?<@))(KOU@>[LoMAnc'tDKUAOIs'9r('jsA!W<!"!<E9#"8)X.":#"+64j_K)&*Vh
)%DH4)%.&h'E8aE')`LA'EAmG'`Ja['GVB"(`4,/)B0V9+=&?`+rLpt"o\W<"U55>$kEp`()Rr/+=/'X
/Y<IQm/R4h!WrQ'!##D6VaM.-)%m>^!"AsX!"8i2"UFr2!"&Q1!"/H,0+&$o$k<dZ&J>`j'GM9!*$?CF
(D.)c%hTHg&J,H_%1EXT&.oQl*>ThLU)"4D!WE'!!r`9'!W`?$!<3)s!"o;4!!**-!7:cM!XK,;!WWB(
+6<M$!;QZ^!!**&rWEH,!!!$"M#[SU!<*$"!Vl]r!s8E$3roEe!!!$)$4G%,7nR/c;,U5!<mjrR:K14j
;cH[o<)lq!<E3!s;Gp@h;H$Op<`iL/?!h#NAnYppD#S5rDfTuCDe<<W<)Z^p<`iO2?t*\[BkqL#F*r.]
CYLQP$ig8/!W<!!!<`9'q#D33!!!')"9>An%h^6*'+bNi%Z:f7$PF'M'E8^F'DiLA(&epH',)&p()If)
)&aG5*$$1K-n$8W&-s$T"9S`/"pbPE%M9?h(`=56-6OleV[r\*rrM]k!s&H*"TAB?!<<+u:(Rs\%LNC?
%0:nX$igG7#6tM>#7(SAr<i3(*srAa%1Wm\&ebom'c%Z-+X8'H'+PK`&ebok&J,H_%1NaV&.oQl*>TnF
WYbsLr;Zs$!WrN+r;cp!!Vud/!<<*$!sAV6!!<9-#mC>0"99P$!;lla!!30&"9&H-!<<**!3#u!#lXi'
!VcWr!s/N%!#PeA!<<62#mdr#;c$Uq;GpA%=4:/V:fUKl<<-)!<u"b9<)cdp;H$Op<``C+>?tTE@qKCh
r+lXWEccD@AmJG:r_jY6=Bf*?@qKChCMIU)HZOIUg`m78!!!'$r;Zm"!sJT,q#D<6!!!*,"9=Wf(`+83
'G(Wk%uUo8$ka0d'GUKZr=o&Br=g"\',2/s(Dn#.)]Kb:*[)gX-mBN?#R120)?^6M$4ICU&eu3")B^CL
.5S",!!*'"!<N9&oDeso!X&Z*!##J8!0US*'cR_m"TT#5IK0cV"U4c.rs8*#(((EX%1a!^',2,q(E+>=
,Tn!>%hB3arY#nW&J,H_%1a!]&f2Q&+"s`)$4Qk5"9AQ+!s8?#pAb=!"98G'$31,."pY83!!E9D`;fr?
!X/K,#6Fo+#lqF7$iBu)!VcWr!s/N%!##G<!<<<7#RHom?<:!+<)ZY)=k+-c?rC'+<`W:&<``C*=]ea,
<`T)t2cWjY='/X1?!h#MAnYpqD/F**DfKi>D.QsP;c6Ll<ENL5@Us+cC27R!EdDYEK\R:Q#QOi,!rW*"
!<`<)!!`9"(]aX;!!<N1!deN&*#9P0&.9EfN"-a7&eb0XrY,8Fr"]/GrtYDF-l!I4(`=52*$$%@+XJKa
+W(^q"9S],"9o,>$k<g]'GhQ'+=J9W7'6@e!s&K*!VHF3!<E6)"T\T("onXLC*OW/'ak0F%KV"Y$igG7
r<EE/#7(V4$2t;3$N(2J$47.L%1Wp]',2/s(E4G@,Tn$@&.fEd'GUN[&.oHa%M'*_&f2Q$)F(D*%1<%6
!!3$"qZ6Bj%KZ_63"l]#!<iQ*!!E9EhuMm>!W`?*rWWT0!WWK+\cE0/!!36(!W<!8!sSc+#8%+BOfVVi
;HZst;Is%_=CP32=8Z2#=oMS-=]ea+<rH#3<``C+>$G9>@:WtaCMdp)Chmp-"`eTu@Tl_0;&N83=Bo6C
AS5^mD/F03G]7h[i"?G&!!!-(r;Zj!"8rE"!#P_<!!!'+!s<R_(a0\8'G(Wl&<.2=$kj9P'ESp^'`AdC
(B,'H'GhK"(Dn#/*#ot>*[)dU-Qj38#6Y,1!sB/>#R_(O&/#Zm(`FJB+"Kmgqu?g#!s/Mr!$2.B!sJl0
!!*9(!,lru*tf:r"TT#6IfTrX"U,,:#lY&/#lY/.$N:G0$5a-Y$k3[X&J>`k'c.f2+s\9L'G(ff',;8]
'F,6_&.]<a',1]g)\X;[ZiCI>r;Zfur;uiso)Jq;*!H<B!r`0$"99Ra!"K#2!sA`/!W`<%!X,Y1"o\Mp
!!*0'r;[c;"9nl,#8%%>LUBlc<`rC$;Is%a=^tH8=BSf*=pS>:>[(B8=]ec)<]F/^=BJ^0>[:`HA7oUl
D/F*)C2@d+DJ3EZ;,9ta;,gY&?t3b\Bl%^-F*)SFH\gSn#m1/-"U"l)!!<9*"U+l0q>_H9!WW3$#6G$C
GRc#;)\`hk*"e2B)@[>n'GM;]'`SpE(B53N(B5-J'F#9e(Dn#.)uL]s+<r0Y*Yo1g!s/N+"U58@%1Wp^
'G_Q+*[2a_9XO]t!s8Z.!VHEr!<N?,"p#P@!!N?&Apb.7'GLoY!"K*]!Y#,6"pbJ@rWrN1rX/T3rXAW2
((:T\%M'*_&ebro()e5;,9Id:%hB9erY?+]'b_2l&.oQj(Ddr)-UtHC"pFo*rW*!#q#U?mrrMus!>6aX
!<)s""TT_D!<*#E!!E<(!s8W%!!3Fo$N'o(!VcWq!Wi6")$'jF!WWH:!<RGV:gmC.<E)k->M34l<a8f.
>5_Y*>l@qn>[(B7=BJX+=BJ^/>$G6<?t3b\C2@a(Chma"CM[cs>Z=Hl9hnPb=Bo6DAS5apEHQMKFE2bo
eJSGk!!!3,!W;uu!rW9!!!30&"9&99"T\j3I1IS?)\`hl*"e5C)\!Go'GVA^'EAmH('#-I(]P9N(&emO
'c%T&)B0[o*??4G,9n0B$NpM4!sAc4#n%1P&/#Zm)''_>+uNT+qu?g%"9S\t!$2.B!sSu2!!!*$!*4X_
+qk\!"TT#7JHHA_#6tPA$N:A3$N:G3%/gY7%/gSL%1WjY&.oNg'GVB$*?ZLG(_R;h&et9\'c%Js&J5Wi
(E+,,(b/Lc"98N(!!*/u!W;uu!W2p!!<N?"!!3ET!W)iu"ookF!<*#Z!:0[f!<N?)qZ$a%"+1@Vnc/[l
!W<!;!<i]0!!a&8"(T/H?rgN5<E!I5fj&/l?!CQ=rET\8?XI,F?!LT;r)jP6>$G39?=@>TBPM@#D/<tc
B`i!U=A^,48kVlT;cd43@Us+dDK9uLGB.bOUqn)P!WW3*"p4`'"9AT,"9eW&!s&E("9&97"9Am%K+]@D
)\`hl*>+>E*"EYr'`JgL'GVB!pD<fE$PaBj'GVE$)&aG6*W7#k+!DdM)A3>Y!<N?,"pbPE%1WdX&ebut
*?,tD2Jnidr;Zp&"Tneu!$2.B":#26!!!'#!(2JT+;,Cs"oo,8JHQJb#m^kG$iUJ5$iUS5%JpY4%2B?_
%hB3_&J>cm()\)5*ubt-%1a'dr>5t['b_2l&el3'(`"#?AdF_/!!*'"!<N?$!W2rt!W<!"!<WH$!!30S
"8`'""ookG!!E<(!W`>J!!30&"8i-)!<<H/<Wr[-!W)ln!!!&t!#bnB#Qau1%fc`0a&ZSK>ut'*Am*hn
BNebK?2\(0?i=@8?X@#C>Pq\(>7"P??X[GVB5)*rrbNosC1q0f>?"<f84cKN;cd11@Us(bD/slLG]S%O
Z()^8!!!$*"p4`'!<E9$"8i0!!WN9$!##G8%QB4X+Vbq1&.BTkO:`HB'GL?Y!#GDIrtt_OrYGJJ.M`g;
)B'P7*$-1E+X%sM*>T.j!<E6("pYD@$k3^Y&eYin)B'SD1OO?Kr;Zp&"9S\t!!WH+":#26!#5J7!!"a4
'd"&'$jH\B!eLRf!t#ACrX8i9$k3+Er=8T5rsni8+qYM*)&jP9*#KA#$k<mc)&aA1(`!f!&eYlq)]0A5
.!9P6r;cfurW2lrrrN&u!W`B+q>^LYqu@$'!!WEL!!*'"!WE-#!R:]F!W)j#!<j,[!<VTf)?L*K!WWE8
!!PU3='o!7=]\R7>2!:t>[UlE!+5_5$=R@P@UW\Q?X@#CrEK8+1L4<o@Us(`BP;*qD/O6,An#"G:J!uD
7nQNS<a/p?A7fOlEHceUFEhi>E#&f]!!<K2"8r3"!W<)t!!<6&!sJT')Zg!M-]\ub'H7\s%3?(A&KMAs
'GV>u'bqK"(]>3K)#b?N('G?e()Rqf)C-7C+X86W+<;:3$O$M1!X&]5#mq(M%hK?c&/#]p*@ik%9E>4o
!!<?,!Whro*!$-F#RLP4!!*'"+H[H]&JbcZ!"]3_"VLtH$Om"D":P_K%M&FJpCR66)\3Gh%1Nma)''_;
)]0;%%1<XY(E+52)&O/)'E/UE(&f'S,:A(6!!N9$rW<'"qZ$Wu!W<!"!<WK&!!E<&9E54n!!3?)-2dfI
!<WE*!<M6]quH]sl2UfAkl;e,"pb81"V1S:1=0-1<a]*5<+BCg>&IYU?XR8M@:E^E@gHOP?sd5G?!LY5
>m=VA?t*YYB)ZENC2Im.CLg^O:eF/C*CE7e9i4no?=@;SB5;F.H?sgYG/uf^%0?S7#mLM0!;urr!!<6&
!sJT')Zg!N)NtpY',qVt$l^%@%3Q5t'GV>u()7T$(\\dG(]>*N(Dn%h)Aj>1*[2pZ,p+$>%L<+9!!3</
#mq%K%1WpX&J#<\&JuZ?2jbQd"o\K("9S]+o`,s4!sJr:!WW3$!!![t(EF&&%0lkB$@W!k#7M"Mr!r]:
rXf#?rY#&>rX^@c%1<RU(*"G=*#KD&%L`[S&f2K,)]BS1'bh;n&/,iu*[<7u('+C=rW)p!rW2lr!<N<#
!!30'"T/6&!Wu@("T/6%!XBbKrW!*'"9\f.!T3tU!V$-q!sS`*"UI?n#58,j!#ktD#m()0%KHY[dog$Z
@9cu8?u4"fE+*6b@:K4G$=m[YARo:[@:3GLqHa;3?X[GTram]mASH"#EGArb:eF/B5<qS+92JSj?!h#M
Anc(%G^4XUHHd0?%0lq=#mUP5r;ccsqu?g"!<WK(!#5P8%hG!C*toS-&I]L"IgRA5'bhAtr>#ALobdWD
!u;Xg)#bE^)&O53,:G#g*Z#=n"o\KB!X/i9$4@7O%M03]$4@@],UYdK!!EK.!!*3)!Whro"T\]/#RLS1
!!!68Ql$eR((CNL$5@O](^^`^%f?k;&H3:@')E:@')`Cs&.T*U$4n!p,9Rp@&Io3V$4RUa)]Te8)&F#%
'+bZd'cSA@24":C"9JQ'!s8T+!<N&t!<N<#!!<6("TeQ%"p509$3U>1r;Zj-(((?J!!*0)"9S]+!T=%V
!V$-k"ptP5!!K8$!s/Mq!!!&s!#ktD#Qau.$3C>If32K^A7/\G@!/S[DId<g@UoCJ!+l+@"_D4S@UW[D
?i+4d@Uit]An>L`BPh^.BjO\.6U*^r4[;D+9i4qq?=78SBP_X1G'7V>`tT3n"9A]6#Qt2,!;urr!<3*"
"8r33":P=&)BKM1()%2o.U`u4'c6iar>#ALpDEiGr"f>NrYc1_(Dn/;.4cec'++mErW!r?"UGDA$k3[X
&ebfb$kF1#,rhFq"9JT(!X/].!VHEr!<WK2#m0u(&"aaZ%MfN\!souJ#o3s]&,["<&cWLD'E/^F(&emK
'+trV&If9]$jm@S)'L=N)\WYfrWrZ9&Jc8`)@[Q$(D[`!&JGp!,9JV)qZ$d&"9S]+!W)it!Wi6"%flb9
!<<*$!!`XD"UP/4!WE'-$P*IB!!*0)"9S]+!T3tV!V$.!"9ni+$imR5"onZ(!!2lqrW2lr*ruNM!<<-)
$3C[k>?t<B@piVOHAlWTAnP[cA7]=aB)Q?FAn>L_@eX:J@q91aAn>L_B5DO+Am%em4?>G^3^#_s8Jt9%
=Bo3AA7oXpEH#i.E3^Mt"98E*$OHt<r;ccsqZ$Zu!X&B$'FY6IV&^Qg)]'2$(+qin*>fV/'c$Z_rtkJJ
!#PSNr>,JO)?(N](`*u/,Ut>k)@crK!"K&6#RLkI%1a$a'G:oe&I''r,s@1i"TAB(!X8f1!qZHq!X&`6
!r`02!<<+r*#]8$%grXM,;g,J&Gm(=')rXF'`SpI('bWk()7Ms&eY$Q'+PHZ$kjR)-mKWB#mU\@#n.@Z
(]"sT(DRW!(`OYB22(i,"U,&4!W`?!!!*-%qu@c?"9AK&"TSl0IK0cW#Qau+!<rl5!!!$%"9\f.!<M*Y
rW2Wk&ci(8!!**#!!`La":5&.!<N?)q>gNr!!2rs*ruKK!<<*'#ltFg>@(BFAn,CcF*;A8BkV*iAS,Oe
BDlKKB4b^dA7K(XqI;9kAS,ReARf4^CMn$"<(/f)1c70N3^#bu92S\k>?tTE@q]^lBksJo*tJ_]!!N`9
"9SN%r;l`p!WiE''`\47$NpI.+!(t5(_mi+-Rg,Y)]BOl(&f!A(]>3M(Ch9")B'J1(De):.4c\[$MsfD
!X&`7$OdLU&/#We$k<pc,;=7H#QtA6!!3?.!Whon"9J]2#Qaf&"K!1W$5EjX$k3dg*u,M('E&RC'E/[K
'c%Q$(]>0U(D[`"&ePZcrX]nW%1E[[*@3-Z)%QoS"U>>B%M9Bj(Dmu*rY?.\&eu9%+tRV5!<<3%!!*9-
!s/N"!<3)t!##G;!<<0,!"&^Z!=T#;"TSN(!X&E%!<E6("9S`-rW1pW!!2Zk"Tno/!!3E)!!t+r#R(A4
!!*3)qZ-NpqZ$X!"o\K>"U>#9fih`cCM7<qDej!$Chm`tAnG[gBP@?Y!,)IIB4b`QAH-6?A27_.B4kgf
@q0(`CM@'L5;OuI1,LjI3^#f"9Mnbi=^,-:@qo@[F4*`)%1rgG"UYJ:!WE)s!Vucs!<W6#('=jC!2q"^
&KDW')^$.=*ZuLB(`!i$rYG,BrYYVN!>l^R)@78u(`aeJ.3B3-qu@c=!X&`6$4ICS%hTEa$kO3h,!MtY
$j."E!!3?-!Whon"9JZ0#6F]%%]16a$5=![&f25n'G_Gur=f/E#8Ish()If))?(NY)&O/)'G:uV%g<LV
&.]6]'G_]8-m9B9"9Sf4#n%1Q&JGin()Hla'G:un*>]n\U*g*E$3C2."pG)1!<N&t!!2rs&HW(9!!<N-
#Qf\_$N^bA!!*0!!!NB)!s8T+rW1dSpAbj-"9nl,":P83#M]:\!"/i.!!NK%!;cfp!!*0)rW!0+#65(_
=C,V=BEi9kBjtajCA_cFC&D]LBk_6nAnM$Rs(;1?s(;7C(M78jA7AkD7QN4U0/57>2)dQZ5Xe7?<>8\H
@qBIr?rh3h0-Uc6"98N1#6Y,,!W<)q!!!'!!##GA!!&u?*ZQ"4()nA7'cS58)Ar;drYPDHrYGPOr>,SR
)&aG5rYu+`+<_gC%0QP/!s&H+"o\`:#RLnO()n/0+!hjG5c5>(&H`FE!!*6+!W`>p!!<6("U=f'%At-^
'b:`_',V>j&JZ&Z'`JjH(+0n8(`=52)]Th:)&F&%&J#?]%hK<c',20!*?ZLE'+4sI#71bH%1`=I&.fKj
)]p+B,q9uV4eWAn!!iK'"9o#3!Wi?&qZ$Tsqu@?1!sJ]*!XA]2!.k1Y!=K&2!!2ut"T\Z,!s/Q'!SIJQ
!W2p-!X/f1!!3B*!s[0\!!!6&!!*3)qZ$TsrW3*%!W2ou!X/K&%g<+:#Lup`E+WctD/O&tAc??CC&D`D
CB\HfBkV-lrFQ%Bq.;6mBkh?n?W^/q4uFrE/hf(;1c73O3]oYu;Hm[EBQ/#u96I3S+USJT!!3E2"9\H$
q#CHs!!!`6":5&.V]['.'GM9#*>oS/*#fb4(]G0M(\AL?(Ch9!)&aG7+!DgN*#TG##Q4WD!<WK/#6tG9
!sAoB)'C(H.4u\Y98Nle":,#.!!NN)!WW8p!!<6'"U=f'"f31U*=</\%2'Hi$kEsa',:?[#T"9o(`=52
)]\ht)B9Y4'b_/i%1NdX&JQ$"*#on9(D@;d#7(VDrXBSP%1ERM$4dmn,UOlk1EmW,KE2J]!r`0("U+u1
!WiE#!!!&t!"T)5"T\T'!rrN*GQ8$M#Qjc$!<N?)!s/Q&!S[VR!W<!-!<NE/!rr<%!!rX&!!N3"!<WE$
!!!&t!WW9!!!**&rW!B5!!!)GAR]CiCMI[&C&VWJAS5^mCi!m&r+uCK");OaB_c<=Ae&KiD/<]b:.%-%
0J+k/0`<dG1c70M3^6#*:JOV^>!G9W>o41Z"onW)#6k>1"8`/n!"o>=!WrFr/0Q)P'bhH&(`!o+)?(KO
(\8F@(Cq<!(`=52+!N$Y+W1ju"9JH$*WlTO#7(P=!s&E)#7M+P$kXHb'9#6^#6G)2!!!-(rW3'#p&G0q
!X&]'!"Y\N)AWbi$kX3e%Ls!]',CE]*#KM1)&aG6*??1C*ZZ.9'b_,g%1NdX&f)E/+s%jE'+PBX$47.L
%M''[%1<II"pG8?&/5`h(*EtuMEV"@qu?p)"U"o0!Whup!s/W1!W<!&!<?[2"98W"!!E?*!s/Q&!Sd\Q
!WE'-!<WK0!WW3$!X&K'"oA9"!W)is!rW3%!Wi3!(]a[<!!*H-!<C,[An,guCM[g%An,:\B57B^!,VRM
"DhmiCMN`\rFcXQB4bahCMdlr;aiZ$0`EX)0/<>Z"Z%tm2`Ni14#J`M59iSO'G^cR"9AK("pOu/q?-Ek
%0?n;#6:/P,o7O:',;A_(],'K(\ALB(C_2u)&X>2*$?LT.3K?3qZ$[!"UG#4!s]#4!Vl^"#QPjX!!`K,
!<iQ*!W3$#!Whup!W`E,rVup"rW!Iq2'!,;$k!RZ&eGN^%h]WS(bQ[D)B0Y9*?H7D*uu7:'bV&f$k3[X
',Vc8-6F!4"pG5<$k3^Y&.]6Z$4$h="8r<#!!Nc2*P;@RqZ$d&"U"r1!rrDs!!E<)"U5#*!!NC$!rr<&
pAb0or;uoug]73P&-)\2!sJl0!!!**$*F7.#R0r&!<E9#!s&H(rW!$#!!*3$!#Q"B!"?Y]CM%U*Ci+'*
BOt[bBPVL(DJj=gDZ=SQD#J/IC(tAqB4kmlBkL[G5W(5J/M&J+0JP<]0GlN"1Gh$M3B8oM4?aU6TF2&+
!<`H(!sJl,"T8H&!qlTs!=Af1!!e]G.2a*@',:B]rttYOrttbPqA/uFrYQ(^)&aG5*$$+F,U46>"oA9$
!X/i.#Qk;8!s/5u"9])4?\SFY!sJf.!WE-&!s8T*p&G-p!sJT'!!<-"$BQtc%hK*V%MKHe"V;1V',;>^
)#bBU)B'P7*;pm%)]9G+&eGQ`%hK?g)''kF*#&b`":#8B%M'*^%h/mQ#6k>0!s\l-!"'8;@"e@V!<E<%
"9JZ-!VQKq!X/c/qZ$ap!!3-$pAb0orW<'"!!1gS$NU80!W`<%!!*-'"8i-&#"&@o"TnDu!<E9#!s&H(
qu?a!"TAB7#64`@\o)G%F)Z#8Df'6%AnPjqrGV^RqeuFN!,_^Pr+lgXCM@HpAn,1J8Nnsb0)dF</h\n4
0.nk21,CdJ4?Yhf2+Tt]Zr.M8!!NK-!WrT0r<3-&r;uWl$O6Y5"H5/g*#fV+(&f!M(`E5iru(hRrtkYM
rYPPNr>>eX)B0Y9*?G)"!uhp^"8`'!!X8K,!X/Z,q>^[3%fhhV!r`0,"U+r/!<E6'!s/Ms!!30("TAB$
!r`0*M(^+e&.8jU'E&OH',22u(]G9M)?(QP)\j5,().An&.fEe'c.c.*?>t/$3^S=%LNUS%M''[$jm7F
"pG/7rW`W2";qsYQ95!E!W`9%quZs$!VQKq!X&Z-r;[$&!)!:p!!2fo!!3'#rW1^Q"9AQ*!s8E$rrN&u
"p=p@":>,1p&P*nr;ls"qZ$X!"o\K8"TSWAZ$pS+F`MG@EGoZ.BPM@$rc%aQpi-4Ns).gQ&8Z,rAmntH
:.79%0J>%1/M@#U%PB=b0/>@C3^#_o4ZPo#"&-'>')hn*"TJT&!r2fr!WE'0"TS].JjLn))\s)%(Dmu-
q\o_X)AsA/(DcudrttbRrYkbT!ur:$*r[5c*?#_-%0lq2!!33)#6"i="pG)1!<<*#!<<*2)CLmV#Q=]*
"U+u0!WW6%rW3'#pAb9r!X&Z*!!!'!!"49>+V>:p$P!d_',:E\rY>JMrYYAI(`4&)'b_2m&J5Zk(`F;1
)&Eqr$3g_A$P!%E!t>VE#lOu9#RUqJ$4.Rn/=HbHrW)ourW<'$!<N<#!;ZZt!<WH*qu?m+3=,Zc!quZt
!<E6&!S@AT!<N?*!rDs!!<WN)!!-L:nc8Xi!WiE(qu?g""9ni@!!!-%#8F/!CM\09EcQ5@Df'<,DK#Mo
qf)FPs)S*YrbrEeDJj<,BOY4G9h%?-1bg[;r@S+(0)dF90/>CF4?l5(6pNOa^K_HS!!!$%p]LR!quZ]p
rrN*!#Qk&5!-qKg)B/qt'GVH%)&jP9r>YqZ)]BS2rYGbU(`=20)]S_q!$2%[#p194*ubt-$jQn2!!33)
"oSW8"U"o/!<E9,"pY/8SO3S[!!`Q."9S]*!!3'#!!2fo!s&H+"TAB$!WE'0F\Wqh&If-Y&el&s(`4&)
!u2Od(\nmR(Ddi&'bqDr'E/UT',;?&)]BM,&Io3U#RLhHrXB8G%1ERM#R:VA$4@7RrY#DB&Yhf!r;Zfu
rW3'#quQj!p&GR'!WrH'!!*'"'djas!!;ior;l`phZ*c[!WrN*qZ$j&#Rgt?[K$R&!;urq!!30)#Q=]0
"TSW;Vj_:DF*7J("`n[&Df9UlEV4AMEW0tdE,96!>Z46]4?,/PqChq'0)dFE0/>FG4?uJ55rh#/^`*@_
!rr<%!WrQ0"pG/5"9S],rW2iq!<E9$!##D6#lo'N+XIp>'GVE$)B9e>*?G,!%3$6))&O/+(`4,/)]Tjr
*<I9)+oWYh+WhU:%L<(<!W)j8!<NB-"pP;;"p>#0!<EE6!s&c`U':T%!W`?$!r`6"!ri;q!!<6'"9e](
!!E3#'6$qh*"EDd%M9?i)&jJ2'bh>s(B,-V)&X8-()7Ms')iIQ&.oNg'c%W()]KV.&.ApE#ltDBr=0MN
$jm:H#RLhG$k=$m&e5[;W!WM-qu?]tqZ6`uoDemm!rDs$'-%Sa!!;iorW2WkrW2-]!s&H)!W2p'!X8l5
!sm6[&a',q!X/i.!"T>8!"Pj"BS(8IF`qqNFE@;!rH&!\s)\-Zqf)UVrcAHcCLpgO8j>6j0`E^+0JWP^
(,7Kr/hJY/1H%9V5Y4g<68buD$jI4Ir;[-*"U>8:"U"r1!rW/r!<3-"!!iT*#QSdN+"e9,'aPQl)BBnA
*Zc@$*!7,u)&`Dj"W80r)]Tms*Xs59,UF]\+W_I5$O-\6qZ$a"!sAc3rWa#>"U"o.!!Wo7$j_bJ!!!H6
!W;uu!W3!!!VQKq!<N?+rVup%rW![L>Sndr%1NdY',MT/*#TJ(',22u)#bBW(D[\t&J,KO%Km:T'GhYd
)?^om&I]!F#TX3Y$k3^X%LrpV$OR1H$4I@Q%i6<$)AJGu!!!H4qu?]urW<3'!Wi/uq#CBqr;[''!tH%P
!!!&n!<3)l!;cfd!<*#q!;urt!!r]3!t>?G#6b)1kPt_e"pb50#m(G6!!f7#DLH^,GQ)akF`__HEcZ;D
FSp7_FE;L"EW:(YF")*GB44q<5rC2B.4Ql$0JbRC1G^a>0.nk32*4#b3^#l*951.<%g<:Ar;[0+"pkP?
"p>#0!<Mrq!W`?(qu?s-!,6*l-l<^+'bqK$)BL"D+!1D%!ur:")Z1H[)B0Y:*ZlLI+X/-0,6oD9*uGRs
"9JB""p"c-"9eu7r<N]9#QXo*!>$#0Jc5WM$O-G.!!<-%!WiE(p&G<u!WrQ*!!3E)!"`dS*?c"*%1Wm^
(`ab@)&3_d&ebur)#bC4(DRSp%LidQ$OdLV&el)u)&aD2'b:TS"U55>$OmRW&.]6\$k!CL$P!a^%LW[Z
+XKa=#6b)7"T8<)!<WH-!s/Mj!!NK4%h]!HkQ(S^p]:$fquQTn%flb9"p"](!s/]-?5*G@!U'Lo!X8o2
!!EZ0!!8UtFEVtUqfiBjG'.nJF*)MHr,r3cFE;JCrc.jV.<'-;@9QMs3@uL#,UY&n0Jk[G2)@!B0J>(8
3'BPg1c76i3TNO:$3LG0!"&`/#71\A"p>#0!VZQq!<NB$!##V<@<*h@*>fP-(E"27+sA'N*Zk;$!?<'V
)@.9%*$$(C+X/-0,7,P<+Wh[>%gW7<qZ.*,!WrQ."pYD?$471Lr;Zp8#J28\!!*<*r;[''!sA`/!W`>q
!!`N+!sAT(!t"r,4C;tN)ANen%M0<l+!MdF'G(fg'c.]()&O/(&e>EZ$4.%J%hTHi()If*)&Eqq#Qt87
#R_(O&.oHa%LiCHrX08H&/5li"pYMa(<A*.!s/].r;[$&!sJf0!WhZg"pPMI%gWCBr;ciuli?\Zq#L9m
q#CU#"UGD9!!!6)"U(P"$j-On!#YhA#6=f,$31&3L:;8JG^4R\H[9s^GBS+OrH/!\q0"E6F)c,8DfTr?
B3Iql2(g7$,:"Tb/MK">2)?s@0JP=<1c@9P1GD*W2NY0a!"/o.!"8i-!<`T4#R1G7!WiDs!!30&"9&9X
!<<9';gBu@*>o\3)]^"D,9nBU+<VaJ*ZZ7@)]Kb:*??1C+!)ID*?caZ/1)DQ%13=D"9\W)q#M-3#7(YC
#R:J4!!`Q,A;pWj!<<3!!!`N,"9S]+!<Dfn#6=i-"9AK*$2soH;0=3)'+YTb',DK-+<;:4&.fEe'c%Q$
(D[`!&ePWbr=0\V'cS8@*uGRt#m^b@#RUqK%hK<c&.T*V$iUP7%K6hF#mM1Z&osBJ!!NH+r;[$&!WrQ.
!Whonqu?`u!r`9/"U,nM"98E&!<N;f!;Z`m!<3)i!!NB)"9\f/rW!*('e04g!p0Ih!<`T-!!3E+!"TKT
\T2n:G^=acI!U$\r,qjX"*Sp7HN&7EH?O:EBkqX-E+)O)/1)Yg,palc.4d//2)I'A/MJt<2Dm9E/hJ_E
3_\3[(^(*Fqu@')!sJo6"Tnf-!<Mlo!<NB&!"K)2!WYQ=0I[t\)]g+F+qGqF,pX`\+sA*P+!)ID*Zk2#
$6:*))B^C[0I@VDrW!''"pG,2quQ`r"p"o7$4$e9rW!*6#U$Je!r)a!!<N?)!<Mcl"p"f/!<<6.rW!Zu
I4--I%M09i)&jS:)AWqr%hTEf'EAjA'fcp?&J>p'-S$AV$31&/#Rh1Q%hB6b',(re$3pkG%1N^Q#R1J=
*Yp?B)[QKI!<<*#!!!$$!WrK)p](9pq>^X!!WiQ2r;[*j!X/W,!<N?)l2^GVrW2Wk"9JZ-!Wi9##Qt,.
%FkR`!!E3#rrMBb*<QHG!!*9*#7aGLC3O]BH[^KoHZsRRF`qqNF`_^'EY<M>H[^ElI!^0aG&hD0>>dsR
1&rd&-N5A6-n6c$1GgmA/LrJ13'&oM/1NtV,X0mP+US>P!<`K&!!NE,"U"o/rW2Zl!<NB&!!!0$!!k*E
/h@t^+!N$--3bbB,U4KV+T<H#+<_pO*ZZ4A+X89X+<;:3$NpG0!X/f5"9\W(rrN#t%0QtG#6=f)'c[2h
[42L]!!3<,!rW*#!<N;l!!WH*"9AK*#lXf<.?u/#$k3da)]Th:)Aa,$&.]<a&cNCF',23!r#$%b*[)^M
*?#\*$jQn>#n7IZrXfPO',2,l$j["A$4[RS#mLM7*@(_0^G6B"!!E<,"Tnf)!!30&!VZTo!W2p+!<WB)
#7:V7"TY4u%/p5/!X&T+h>mNUoDf7#"pY//!!EB3!!(IH!!`N1"T\W*!WhTe!<NE'!&4T\%1Or<Ap/-;
I"6ctHZsOPFEVkOF`_\GEcQ5EH@:<oIscTjI=6?R<C&>i.Ochrr[8p=.4Qi"0/>=</hAJ)1cdcX/Lr;,
2B/31+q>7g!!!B4"9&9$!<N?*!s/Mo!"]26!!!$'!<<*8X=l4I+!W-3.0(do-Pe$T,U4KV+<VgO,:"ER
)]BhG/1r4b$N:#2!X&Z2#6tG:"8r8t!"K&9$jH\3!=TP?ITm3\"o\K'$O?k4!!!&o!;QU3!X&Q)!sSi/
!#)1S*srGj)''_:)&<o!&H*.=&-WXY'GhZ-rZ)Lj,:P6!,o6mg!!3?4%1j0N'GqJt'c%Mr$jQn=#n7FQ
!s8`?(BB.t&HN4;!!<W:"9J#mrrW)u!WiH*#lt5<#m:Y:i!'_k!!<9*!s.6YrW2Wk!WrZ6rW!K<!"BQ&
&/5*S$47"@!s8T*nc/XjqZ$Wt"9&9+!X9)E*klW8Esd5DKReJrG&qbJGQ)gmGB\:WH$XjeJGt-WJ:;fe
De<$<1*dtb+XA?[-RgMr/MAe41,:R</hSk93BB#N2*s):CRcIe%M&[B!t#88!WE'$!<N<'nGj1'!s&B&
!s/K($_9I8+sSHa-78U9"XPE>,9e?0,Q8qp,9e<W,pt#['+"R;$j$P8"pP;:"U"o/!Wi/u%KQ\;"9AoO
&HG[`%1WFDrW!!*"p4&i"T\].!WW<$":kP@Q80Ki%i--()&<nu&.e^K#7_4T&ebrp)&4)3+X89\.4Qep
*>/PV!!3?4%M06erY5GL(]G6i'bC`Y#RLhG#6YMY'ED*h&.esM!!!'-#Qt1u!!39*!W<!,!<N9&"ptJ5
%LLDc%/p8+!qu]k!VQNg!!!&l!!30&!Vl]t3sl,nrX&c5"9S]+nGiOiqZ$Wt!r`0@!<iiA'q0hsGCG:#
IsZE_FEMbOH$XgaI"$TsJqAXRJe<Q^FD+lQ5Vj`-)B'S:+<r3^"Y;8\1G^fc0c;`&1Gq*N3Ar`B4>:Ej
0E;@a%LE7A#6b21rW)ounGj:)!sAZ*!!*-'"p]QW0de>".3fuY,5ibc+p/u3+sZt1$RR5L-mg,Y)&!Je
#6"c#"Tnl0!Wi9#rW!Q3!sAi/)A>rX,QIfG#R(51"9Rff:]UY%!s&B&!sJr8G=`kf&fVf.'bLrc$k!CL
$OdIS&/,cp)&aJ9,:G)q.jcAV&e"sF!X&`8%1a$b'c%Q$)&aG4(_mVl$OI(D#71DL'2T+I,6.]F#mCA5
"pG&/nGiXp"9S]%!!<6*#6Ff(#!rb!!<E6&rW)ltrW)s!qZ?cuiW/rZ!!2ut%06G4df:9i#m^hC"p+i*
!V$-i!Vucr!W<!6!sf/I?FOcnJW,21H?XLRFa&(VH[UDCJj"dAKnP)0J:2`cAl_A[.j5cE',;B)+<r6`
/ho4B2)?s@0f(^J2Dm`g2_Ha(?ca_t!!!**"pG28"Tnf,q#L$e'`eC>!s&B%!<`K57Z/oH.l/Ip*ZcI'
+UB24+!;^N+Wqs-,7>bC-7:/f+W;"'$4?b=rWiN0#5n]>"pP55!W`<'!sAT(#7Ue:#lmN,+T;?B!X&Z*
!WW8i!;ca4!<WK-!<<*$#6kW'IiAk4+W)%0%LWUMrWiQ3$4ZtG0G>3>)]^%H-nHnr*>Ane"Tnf."pk\I
%hTEg'c%W()]Tk;(`!bn"qD7N!snrs[N,5GrW<9+"9S]+nGiXq"U"o(!!!$;!sAW)!!<6Q$ig80!WW3%
!sA`/!<<*#!Wr?'rW3'#iW'#^"9JH$"9SW+"cWE\#Qb27#6k;4!<MfmquQWo!!2ut#6b)D-e*6[ISQ2R
JU;WbF`qtRH@('nM1g>/KnP#+HZjCE@T,WL,T@I1%hKEl*?c^W/2/k=3B&cL0JPCE4ZG8c:HU`n*4A<P
$31M<!!!0,"U,#1!UKdh!<WH,!WE'3"TT/JXZ7g\4rY^f*ZlOJ+<MX2*ZlXU+W;@E+sR"20d7b^(_?uV
"9o/?$k*LO#m^_<"9eu6"U"o/!WrW4!<<HD$5!^JUcT4u!>#J9!!<;m!;urq!!E<*"U"o+!"K58'Fpf`
&JZl/*"rei$2k,:#n%@^&e#?g)&jSN+<i'W,TRO*!WW3$!sJr;%1Wm[&J>cm(Dn&1*ZQ(9(C^Q\*"<Jg
!2)4Z"oo#5!!*!#!WiE(nGi[s"p>#/quHWq#64c3`W-&?!r`0+!sJl4!s&B%!<W0$!WiE(p&OI[('=a@
!!<T/#64b\#6Y,0!WrT0"9SZ*oDnahnc1BT)3V48RVAF5G^F^ZGBnL^IXZBUJ<GnDI<TR>>#7[N1bC'u
*#B;%'Gqf5-7LK!1)i&-2)[BM1Gh$L3BK8W1H[WT_Fk%8!!!6*!!)s"!WiB'li7+g!WrN&!"8o/%1$lu
+%m;;&f`(n,7u1H,pXBB,r[S.-RBlS((gr\r<<<.#RUJ;&ISsR#mUV;"pG,5"pG)3"U"u@"pFu,%M9MX
49,H`"UkS8!!2TiquQZp"9AT-!s/B$)$C$Q"_DBS3!MMT'bq>k%M'-a'GCcU(Fgg3+;,_7(_mYo$k!@I
#6k>8#7(\H&,m+?')iRF(]G<_)&O)%&IedD%hTPT2ZNg_!!!6*!!!$#m/R7n"p>#0q#CEr!r`0./0tE!
#QOo+!!*3)!rN#u!W<*!!TO.^!s])7r;Zp#!3m@=!<3-#!WE0#!VHHi!V-4^#89>\JT6okM1BtuF`r%V
H@($jK6_?UGB%4s8N\XO)]B\<+s7pG)B9kE-S$f'1,LjD0/GRI2E3]S1d",Q1bC8[LEI'8!s8E$quQKk
qZ$TsqZ$Zu!Wi/u*X;lmYsBa)(,%$],U=]a-n-Vr0f1@&-7gVl)\NGXr;['*#mptF#RCb9$6BKZ"pYA8
!!<K2"9eu2!=9><#6bKtF;,#j#RCV;!V$0d!W2p#!!!'%!W2pW":>8LUbEZH&1f"F(DIW%)B9_;,:4EG
*$cgS*#/qg!<<*'$4dUT$4."G$4I@R%hB9d&.T?j(]G-[&.K9i!!rf9O)Y^6#6P&/kPtbi"U"o/!Vl]r
!<io;!<@KI!X\o7!<<*$!S.5_!X8o;"p4i4!!#k+!!*'*"9JH$"9AT+!<Mloq>p0f$3UYfRIb$GGBnk$
4FqX!H$OUOAnGasG&qA!6T?_H+rqO:'GD,q)BL(K-7:/i.k`\4/i>aM1,_3S2`NTI0Jt+@c;"?S'bgQH
!s&H(!UKgd!V6:+"oo<S\Ka3_,;(u1-RpZ!/0u>[,q]N_1bKm`$j[%?!s8B#-NO;Q"pP24!<E9+!WWK9
#QY&5"U"u0!<W]0+0mj+$P='Q!sAc1!qlWi!<E0$q#LEqqZ%c@$31TJXV`r?+tPQ!*$6@M,TIL5)'^X_
-QNg2%h9!U$7lGf"pG5<$OdFN#6b56#R^tH',qYq%M93]&.AjN%KIQT2?4!l&-)\2!WiDg!!WQ/!s/N)
!Vl^$!XA]*#cdq+"oSE%"9IN_o`,=#!<<9/!WW3$!3,kr!XJr1r;Zs$!s8T*p&Opio)LZP"ro\El?Zoj
M2lsuCi3ruCik&QA4S^6.4$&T)]^%E*>]>"(Eb1`2E!BG/hJqD4#S`A.k_Gm4ZYJ_0JZBH;8ZHC*!.&`
rW!$%"9S\k!<*#k!$V[K"r<K-2]+>45r'Z3.4$2i2aTqd('t$C!W`<*$4daX"8r3.":5DB"p+c)":PVA
!WE'+":,25#lk/V!&CJ\5l_Dq(^C$@"9o&5pAk!imJor`%0-MBNMnZM1cdfP*?ZUN+"&d(4=:XB!!*<2
$kF!e(_R2Z!!3E9&ePTY!<<*%$Od@I"9Sc5%1<IT#n8?a0W%&7%KI4H!!!$&"98Pi!<30#!r`5r!"9,:
%00?q!"9#7!!<DV!!*-)rW!B1#RUP5TE"s%!"&u9"T/6&!<`N-!rW,q!;cff!(R7q!$<DuXI4!=ATE06
?>"1d9JdtE2(p:#+<27<*[2s_1,qKf9iYD*AoN-SO+D+P9fjgW3&icI-m(fG3*jF&'EA4>'*\@8!s&K*
!UTje!<*#l!'(5k!!!-%OEb+d-RUf=1+"\90H15s!Y5V?!sAZ+!X&]5$4IFX()\,9,:>3.8l7u2,8:4[
!!NQ0rW!-:*"tQ:63R8f#8%.?!!*0*"8;fk!V6<h!&Fuo!<<-#Mfi;Z,pb<0/gE#10,Xil!"KDB$4[RW
%1<FG#RV%R'cA#7+!)XV2a/r<'F=[<$j?nC!WW3@,8WSB4otW_!=o>4!!33)!qcQl!W)lr!rN)p!!!'!
!!!6+4<4P+f)YgOqZ$j-%Kd.PV#U`!!!<<-"pFi("Tef0!s/Mt!;cfg!"]29!<N6N,)>,i4!$+:-n$8u
+!W*\-mBZQ+<_mM*[3!b2ap_YF*`7cKT2:fSskt5S=#M(MI\n).5`eF4$dB!.hE9t&e>6Kr;ciulN$nb
p&G-r#RgV3#SI8N\N:9$"qLP2#Qb5<"p+o4#RDsc!s&B%!=Thn1,_'N3C$)-9hS)U=&i'o8gt&H!"&iB
%N.X=)$1!B$OR(>r;Zj"!VcZi!Up("!XK8I!rr<4!F`Dr$NL59qu@-.#R^qE%2'Hp(_dD_rW!$/)'p^T
.kE8*0J+b$,V(W+1,q-1!WW?:%NcQ37^3[.!WWQ6"TeQ%!<N;q!;cfp!;uri!"K)2"p+tU#6b\?!!!''
"5s4^!<WN3q>^s3$O>_u$kNFE!<<-("8i-&!X&T-!Wi#qquQ<f3s,H_"W@da+fgi3,oJ9\*Z#G2(_I5e
&/5s$*[3@-<b?E%LQ@XaQC+>DY-P40UnOWbUS`0$1+F(r+U]`k]+u;')\ND]!s/5uq>p0frW2]m!W`H0
rW!H>!!3LiGs;W9&IAL=!!i`+!##G<"p>#6%MTg+.l9:L4Zttr8PT1](K+79?W^Sj%0Zn8$NL0RT*#Q9
'FOsE!V?Bc!Ug"]!X9#B!rr<2!!!4]F?9[,&.8XA!"B5<"ptnX)]]k6'b_,g&f;]:.4d)*0.eY#+WMFA
,qgl4)up*M!#G_EK;/GR%1igI!s/K(p]10kq>oj]#6Y,3!!iR$3;`a^!<`E'!<<-%!rN)j!<3)u!$hXO
$k3FA!!*6-!!"`a&Hi.9!=&c.!<WB(!!!$$!WrN+!W`>u!<3&s!UTkP#6PMO'f;SS7M[*\'E]No#mCG:
$kaF#.n!fnP+%o2S"-%?Sti9gZEC-uS#X-%[>.4*+>b3Fa-dMa&e#Te!r`0"!W2p$!<N?*!Wr?%oDnjk
o`,!n"9&93"onu=$7M+!3!Tut"TT>I!W<!(!X&W2&g/bb48h8^4[)(s77g0I9hJ)`CKY48%KuhH!&gNr
!#5nJ'ajm>!!2rs!!3$"p]9pc!W`9$8,rVj!s]/9!!<H+"pP/QNf5k%'+#'I*YSkf%MK^"*ZZ4C,UY#h
-6sf`.kWM-.3ouP&ISpa0-`D!!!*<I$Uh.L!##P<&-r17!s&K*!VHHi!U0Re":,GG#8$qM!!'!4!!!?+
"Tno1!<N?*rW<*#pAk-mrrW-"(^13U&.A[H$NL/.[Ntnn!!!91#6k>6!<N0$r<*$#rrMoqqZ6$`$N^D2
$kX=0Wh(4K">_k7#n%(I$k<pk018r\KTqgfOGo-XNfTBkSY;aMSt2INWR./C3\iOD`*!KY!t5SO$N^5,
rrN&u!<E9$"9/H%!VHHl!V??n!WW6"!Yk_9"ptniU6ZN+!%n6T#R1D7!W`?1%i-?A3^cA&5<M.t7nZTS
<;]c);cd"J;^W(h)/-$8rW!$+$5!XD!<3)t!!!&r!rE#c!!iW."pbA6"Tnf)!#>\G-)$YC(^;ht#n.:V
(E+22,:P#d,Q8hg+<M^L*$Z[M)]'5*)]]t=+!*s'%0RCgEjeU@!WW3&$jZb3!s&N,!VHHk!TsFb!sJo3
r;[36!Z$AW!rrN*!!38r!!!&h!#,M?#m1/2!!!GJ&c`%:!rrH-"9S`(!Vlfq!W)ln!UKeF!XB)F$5<dR
Kop'`$4da[%h]Ni(a;.KC3+o]LOjeqF`qtSI"6p-NKKEmXhLEqW(TBbYa?[@#8%%A#n.1H!r`3"!WE'#
!<N?%"9&B#!VZTm!VHHl!C6\c!X8l<":bP=JraRZ$4d^X$k3RL!<<`Z0K;El8OPg.6V1'R=^,0=?<piD
CiiEA?P!r@RYM[Z$31&1$47"?rVus#!WE)u!Vc`q!Ug$f!C-_i"U5/7!WW9(!sS`4!X=@CD]B<#&.8s_
)&a;,-T3V(,9nWk1,:R=0J=t+-RUZ44#oSr)A"\)"@/K9+9iAU!!<9*!s/B$rr`9%q>gHorW2Hfr;d*&
!<E0#!<W0!$j$D4$33&/$3gP:!!;lp!sAi4"7Q9r!<<f=!',f7%fQG1#6k20quHTprW;uur;cftqZ6Nn
!!2Zk4TP]p$3pP2!Z6rs2&60+$j[Lh*[*sdDf0`HI<p-\EG]E%BP_X1I"I6;OdE/kWFs9*9F1t.#QXr3
#R(;.!;lls!riB#!r`5p!;lld!(Htn"9SW(!umE+3Z7u3#m(GG"99&d1H%[#>$bTGA7fLiCi433F)l/2
>ZP9Y@P+(`3rfKm%0HV7"pG,2!<<-%!W`<'!rW/q!ri;i!!NB)!WrQ.!sA`/!W;uu!W<!Q"sBAD4r=8,
"9fJ^'*oX;2_cj1*>]bE.4Qi!/M8\0-mq2W5qO`W1^f&F2ZX<u&Hhe.r<!!"p]19on,W:c!WiE(q>^Qu
!!!H5"98F"fDl$S%0-A/!rDs!"UYY:$lfW]#R:P<"U,)9#mgb:"UPGC0>%8k!!EH*!!rl&!;HTp!;6Hk
!;uri!"K&8%1`^E"p,;pRZS[-(F';#.j?')DJj'#DJsK7EGArd<)m%*@VKe)IZU1dNO%b?+rC1X"9AZ4
"TeK#!!3'#!!DrsrW2coqZ6Wqr;lWm(]amM"TSf5(."[\+qt[m#9!aG&i)C)5trS&=^YfP@pr_P@Us%]
Anc%!DcK8IZm#b^!!!E6#mUV9!<E9$!W<'$!s/Q%!W)ru!Ug!h!<W3%!WiB'qZ%fC#m:5:%3J3=Or"</
!=U:e!#[d\6XYG/Up.DE`5]pFe^tPdb-[%8<_k7a8WsP_!rr<5%1*.4!<3*!!ri;t!<*#f!;cd!!WiH*
q#Cs5%LE4;!!*V.PlUjm!!W]3qu@'.$kO'e(D[\t&.eaM#nR^`'+G3I%2Rk'!!!c4!!<?0#mKo#nH&Ri
r;cZpo`.#S"UPM;!!X#=$iiPhJjU=q&eGgA@VKFa?X-c8;GKeP6:==;:fCFu?Z:URP*+9H#QYA;!!!-,
#R(2/q>^KrrW;our<!!"p]10lrW)isp&GR+"onW/'akWS7&GJt%1rL=.Mb$59NGJ/A7fLiCM[j*E,fl<
EGT<)De<QmYRgd7$k!@H$3p_9!!!'%r;cs$!X&H(r;l`rrrMQg!!3!!rrMrr2?F$^!"9e\*!AQtE\e(=
$j6YX8n<-qKoqq$WN`kE_9('RdCPp,H#@1l9i%;]!!!E=&.AsOp&P$lquHZr!!2QhquQcurWDrr!s],:
"TAB)"98V=&In[=$j6P1!=95J&J,B[$k<1G%h/sV%M'*^&J+pB#A=;H#6"T*":,;="76*a!W3!!!rW,u
!WN6#!VZR8!WrN."T\T'!s/H8$Nan[A/$!p(c5,s@9H;p5r^Y!0H;i*3'BMk4Zbi*BQ/-`S/)nA"98E(
#7(S=!W`?!!!!'!!r2rt!WW8r!;?Nm!W;uu!WE'%!<<*$!r`0Y"9SZ=$j'qS<s&X,!['g1@q/nS?X-c?
@V0@lDJsH1CM7@!G&M)PN!B[i!<WN3#mUS6!!*-&quQ]s!!2irrrMoqr;lcqqZ-g"!<E0#qu@c=!!!-0
%1=$\!*?[4$l9Bl4(O&?][#*]g"PHNnb<"^'CsYVO,/R9Cl4)R$315:%hB*T"7lNf!Up*e!WE0!!rrAu
!!WK-!s/W3$8Df%!!!&O!!!-,$O$M9&ekui#m1/-!sT&=#mgkC#m^hI'+ksMB*/SC!WiK0#m^\9m/["a
q#^KprrN'"rrMoq!<E9#"9JZ-!rW**&fq#Y(1k-j2%(?J;bobC2(pF*+WqjL+XJNg0J4n*.QgR.>D]!O
!"0)<!sJr:#R:M9!s/9!"p"c,!s8Z/qu[!%!Wi&ro)\di#QXr-!WrK*!<N&t'G)2`"V"M2:a5ub>@V/U
C27QuBPS/sEHHAKH$OXXF)cGSF`3P@rW!?0"9AT."9S]+!<N9&rW)ltp]:R#!WiB'q#L<noDejlpAcE=
"U>8J)ZTjE=gM[)-;TbsW3sF\bKnYjhrO"ho_8%Dg;^N4Z*'UVXL/<:!t>_K%1EOI"9J/qp]9mbqZ6Zt
quZs$!W)j$!<N?)!!3<%!"o_R]F4cG!"9;I$O-b:!<<*$"8rE&"q1Y>$P<dY-s$BN!"B/:!!*6,!s7ii
r;lWor;ciuquQj!qZ$Zu!X&B(4Tb`g"TSN(#mq(Q%g<k%WIn>C:,jOB*uc%5(D[`#()\)7,9e6M*@s<7
5^&e#!!3Q9#7(VB#RCY>"9JT#!!30&"8rB$!s/N*!VZTe!W<!"!<NB%"9\f-!!!'!!&"BV#7V(A$lG7T
>ZblU?Y==uF*)SLG^4U_IXcluIscToLO!p1]*869#Qk&,!<W6&!WiB'qZ-TrrW;lsrrMoqquQBhqZ/_X
!!*0%!!Wo@#RLV6&gjcQNg@,VUo:K*]uA7De(31+hr3SSi7ur9e%Da(h]NIA'bC`[$OR1F"TnAt!!3$"
rW2lrq>g6jrW<!"rWE6'!W<!!!X/H%%0Qn9!"9&3SQQU+'b:WL!#bk?!s/N)!<N<)!sA]/#7LS74h(S%
!#Gn@!;us!!U]sd!VZZo!<3)u!r`5u!!**%r<!0(!<<0(rW"eZ#7CnC!rrZ5EMPiO*Zc7=()%;m&J>`l
(E+87*?,k6+tPB,9m0\O&HE%H&.T!L"9er3!r;lu!<NB&"T/?'!WiDt!;6Hm!WE'"!<W3%!<N<$!!!&u
!"T)7#Qau+!s3\V@pW>LC2j,k#'+d-G'J=\rdG9'I"6p%J;BtF+W(1[rWN9(qZ6KmrrMiqrrMoqqZ69g
!<E2t!!`Q+!='#>#6Xr*'bVO[n>NOl['mQ\`QQWWe^rL1i8WhsjqQn;in)Gset+rS%h0$Z%L`XL"p>#%
!!!&u!r`5m!;?Nn!rN0""98N$!!**&r;[9,#6b)-$j-SMbm=aX#Q"N#!W<!3!<E6(!sAi/#V)_a!WWK-
!sAc0l2^eapB(<oquHd!r;lcq!s&H)!VcX&!<if1#T*dJ>*NM[.462X)]9G+&J,Nf()\#0*#on9)&aJ<
-8@,TNDp)e#87d`#QOi+!sA]%!!**%q?-]urrMlpmf<Om!WrK)pAbp/#65#J$OLIILi?s;BPM@"CM@Hr
CD^o,EH?8HG^4R\I=[*1H^2-](C^HQ#mpk7!!!&o!;urp!ri;s!<3-!!UB_3!<WK2$4-q;!#?.bK\42Q
]=u2%aNMoWeCN:+gu.5Ul0@Qul08rJlKQODl]a(E%M0-_%1*7D"Tnf#!!!'!!r`5l!;6Hl!rW6$!r;lt
!s8E$%0d(D"9o&1])VgD$j?\-!<3)u!"K#3"9\f-!$E2*#m:_>$j$bB"R6!d!VZZp!;?Nj!!!&n!#GY=
"W7:?'L%sD0c^rA)]9J.'b_2o(E38nr>beW'c\591GrE^+!:Rp%1`XC!!*-'!WW5t!!**%r<*!"rW2co
o`>'or;lm!!!2cn/cl+m!<XQG\R9&V?XRV^B4YU`@:EbZBPM@$E,p&DH%(@#Lld4TU,X_)"U#)7rW2Wk
rW2`oq>gKrrW2lrrrMZj3!9Kp$jm(M!!"K]foMu1\A-50b08/Wd*^:kf%]0Glg4!(m.'cEp$g>Xc<*@?
#mUnK$jm:G"U"N"!!3'#rrMlpqZ-KorW)ouqZ?cuq#LBq%KQP1!s/K'#QhgM!!!$#pAb3q!W2p)!sJ`+
!X&K'4LYXr!!EB,!s&Gh!;urn!rN*!!WE)u!Up(J!<<*,'aG3K"HY5g0e3\<)AsA.()7N")]g.F*uu=A
*ZuUJ)]95L$9h.C'En^J$j?V2!<N<'q#CKt!WrQ'!rW/o!;cfr!<3)t!rW0#!Vl^Q!<E0##o*a]!?JOQ
B68<'=D;;R?X?uA>[CcG@qB=gD/aQ?IY3H/ULJn-YUBbW!=&c0!Whonm/d.errN#tqZ6Ek('"=;#RUtP
('G*J.*I10[)BJabfRoHr5g&'bgG)#jlYailLXoQqu==R\Ca+`"9],B%1EUN#6Y)'!!!'!!ri;l!;llq
!;urt!WW8q!!rZ."9er2!<<*B$38QW!!<3.!WW3$qZ$Zu!Wi3!"Tno/!!<N+!"1'l!<<B.!!!*'!Wh]h
r;lcsrWE'!q>^Krn,O(%!!!99!!!4rCF1MD1(#?:(`FG5()7N")BBn@*?,q;*?QCF)]9>=%Q-dYH2nfp
%0HM/!s/T-!Vucr!W3#u!Vufi!W<#u!Vc]r!Vufq!?;(>"q^h<)o.bDB3'C]F&u^S>Zt94=^#':@:a-d
Ci402FEr=gJraSsKnGTi((1HNklCP\quQj#rW<*#quHQop&G[*"9\l<('=ghf!gF,R)uJT[/RfS]tCti
]tV7q]tM2#ce.7EpAOjfbR`CO]=\b#'+kNS"pYD>"p=]%rrN-$rrMWi!!<*"q>gBnpAbd+!WrH'!X8W1
#aR^U!!*0-"SVor!W<!#!<`Q-rW!0*%KICs[K$R2!!!&p!V?Bj!W3#u"8r8^!&"?W#m(*7N@H(]-l=i[
'H\//()7Mu(E"/2)AsD2*$$(@*#fh7)`B<+F*@Th'*nL:!s/W/!rDs#!!**%!rW/s!;$<i!!!'!!rW3&
!WiE"!!33(!WE'1!XoGJI'QmX9PI^X?<:N9=8c/)='8d9ASH"!rbi9gH%(<jFG=gLQ%o>C&I.J"rrE$!
quZg!rrW3$quH`tr;ls"nc1QT()S0ZeV9-AXes:HXLGC:Y,n\+Y->13Un4*T\&[(Zlgj`7i9JOlc)qTl
*";lJ!X8r:"9JE#rrN*#rrMcmrW*'$!Wr?%pAk3op&P'm&-)\4%0-DNRfE]o'Fb6M"Tn8q"9J]/!s/?#
#R)%]BiG]F#6Ff(!!<-%quZiupAk0nquZj"rrW3$qZ-NorrM]k)$UNP!<>$A/gMDO(G?mP,7#A.'bhAt
()Iec(]kQn*<$rl+!DRD/M/8=Rkt*X"T\T'!X8c/qZ-Hnq#LBpquZftqZ-WsrrW*#!<N<!!!*-(rW"SQ
!!WR#ZrgF2;H.F9=^=?s;c-Cj<E<4*?!q/RB4u$qDf^/MFEE%X?uWG8!##P3!!!&h!<3*"!r2ru!ri<!
!<3)t!WW8n!##J>'H1cALldmeRBiT_WK3pKS!s>G+Io!pTqnWi[CsQ*g#MA[k4%BC\`dE2+UeDP!!EW7
"9SQ&rrN$!rrMfnquQg!rW20^!W`?'rW!,7!X&K'#m1J;"9\8r!W`<'rW<H.!<E0#$PWR@`r,l@#6Y#-
"9eT(rrW3$p]16nr;us#rrW3$p&P*no)KO6(B=F<P]/&i-R'WH+!)@D&/#]n()7r,'GM8s()If*)B9b>
+s\9P+tG6(;3q7k!!r],!<rZ-qZ-NppAk3orW<'$r;lcq$3://!s8Z/!s8T*qZ%oD"98E'$NL/BZBnZi
@U3&-;Gg1g77^-K;,^Ir=^#!5?!h&PBFelrEccACG'e.AEMj*S!!i?#rW2QirrN-$rr`3&rW<3'!<N)u
#6=i,!WrN+!V?@B#lkPogW>V@WMH)EP`q5sLl..NNJi[ON0^3@\@K)V[CsZ1hW*hho@^ma%FljO#6t5/
!=9#7!s/N"!ri;p!<3)s!r`5`!!*0.rW!(12Zs*]rVus%!qZHm!W)p4"9o)5!!<H+"<YDZ"TT#9!!!0*
"8W*"!r`5r!<*#r!X&T,!W`>a!##VL"TT^".4QA^*ZGt:*?,n0',:E\!#5DG*#','(Dn#/*$$+E*uuLR
.PO;B:]LJ$!rr?*!s/<"quHctpAk3orW<'$r;lcq!W`<'rW<9+!s8T+qZ$Wu"TABT#6P2jW)R#'?WpE(
9hnAT6q0aA:/Fhf<E<1'>$PEEAnYprDfB`@I<'"<RpZ4!#l4Q!!V69l!<N<(!sAK)rW<3'!<N)urrN$!
!!2]l&HrR_=k/G!S#<!KOH#9[N.lubL*;8(K8,GUVQ[8.YHYORbh(e;oD.@`[a9^F%LE+8!=/l4q#gTt
!!2cnrrN'"rrW0#jT#Gg(_29##lFZ'!s8,qrrMuu('=[C!rr<%!!=:/+U.uV"onZ+!s/Q-r<*'$quQZp
rW2cqrrMrrm/Rb%#R(3TB-/?;*#TV5*#fb2'GLEZ#nmsb',)&p()Ikf)A=&1*#p+L-n[J]RfEHl!WW3&
!Wi9#quQEirrMuurW2iqrrN-$qu[!%!Wi3!!<E<%!&4N\$^H]H=]Sa.;G^(\8OZ!77S$-F9i"Vb<E<4+
?=@AUB5).!Ed<(UD/"C)":>D8qZ-TsquQKk"9AQ*!sAK)rW<3'!<N&trW3!"!!2]l!!3ZD,.P:>QC4J=
Q]d>cM1pT\JfoVpJV/fBR\H[XWiieFa3i`,p%mgq\$t3:(CC3D!<r`("TAN'!ri;q!<3)s!r`5^!!E<&
VCDlM!!**%!<N;p!<3)p!WW9#!!rfC"uW@[!"9,7rW*'%!sJT*r;ultquHZrq#^QsjT#et!%+$^.2<X9
(D[l,)&F"c'*8j]')iLI',)&p(E!)g$5sg%+!`*Y3^J]nqu?d"!s8E%rrW3$oDnjkquZiuq>gNrrrW'"
!<N<"!!**%rW")H!'.Je>YS1!<)?=_84Gp35sn%084lNL:Jk%k=^5<C@h*$\B5DR4I!'7IE3<CN#Q"K$
!Vulr!Vl`q!WN6#"9/N'!s/N)!Vufn!V?@(#RO>]KTh:ZSXPb(MMHn:J:INH(4CX^KoM@fTVJEdZb+-!
g#_f!k0CuO"5eJD%/p5."U,&-"o\Z(!s/N)!VZTo!W3#u!U9[b!WE'(!<<>I"onc,rW!!#!Wr#prrN*#
!s8W,!W)j"#7ge9SGiKm!<N9%!<NB&"8`/t!W<#r!W)rt!Ta:l#69*D0c(]A&eYin(`*o$r"K)CrXf;H
',))r(]G6S(Dn#.*W@/`4>LN5qu?m%!s8T*!W<'"!W<#m!<*#t!WW8r!<3*!!rN-$!Wi3!!<E9$!&+]]
P&=Z$;c6Li9hS&H69m^u5=%Y)7Rp$C:/Fhh=^>ED@Uit`Dg$DJCO^,_Z4I6;!!E<(!WrQ&!r`5s!!30%
!WW;t!s/N)!VZTm!VHFH$kTJ'O+WLVQ'78eLP12,I!^0cH[:!bI=d<;Q^aVCWNWeF`m`o6o&\6LZH1ZD
%K6>-"TAT)#6+l+"9\f/!WiDs!;uru!rW-"!:9dd!WN6#!!WT,2$a3a#Q+Q'!WiDt!;uru!r`9&!Wi6"
#lt,2"ona"S,ifl!!!&u"9/H%!WE0!!W<#q!W<)u!VHHe!!30&"9&92!XGGP-P@"%&.oQk(`!f!r"B#A
rX]eV&ebrn'c%T&)&X>2)]Tk@1H%ge+8l3=!s/N)!W<'"!V6<f!VZTo!W<)u!s&H(quH`urW"VX(VWpQ
8ki#T9M.iE69dRo4$5Yj5XIk.84lQO;H?t,?=.)LB5M[4FE)bSJ@dfFqZ$TsrW;s!rrW3$q>gNrrrW$!
!WiB'oDndiq#CR--.mU&JI73lOH,3QJUMihG5QJ$G'A4\KoD1\R\$:RYdV9ig?7kcg=sZ]jA6Bd!<**$
"o\]+"o\W-!s8T+!VZTg!U]pf!WE/u!!Wr6d/Xs_"T/9!!WN0!!;Z`q!r`9&!Wi3!#Qb&3"WA-"&H_n2
!<E9$!sAZ+!!*-!!rW0!!:p6W!!36+#5nN5+.5J+"q;"O&/,cp().Dp')iLC&H31@&.ofn&ebro(E"/3
)]BS3)^-Xm13?1i!!36*!s8H&rW3'#nGrFepAk0nquQs&!s/N%!!30&"9&9I#W'#06pO=98kDK?5s@@j
3&ioZ4$>en6:=:792AJe>$P?>?tF']DK9lEHA6L?CBX\?!W<!"!<N?!!s/N*!Vufr!WE/u"9/H&!V?Bg
!W)jO%7A[5GBnmuMMQq8H?XFMDf9N3E,]f;FaAUpNfoZpS>)sb[`$YPkih*ahR;$j&cr@D"9\f/"U>59
"oSQ,!s8T*!VZTh!Ug!k!<N?*!r`0*"TSc0Ym^s>"9&9#!W2rm!W<)u!s&H(qZ$j'#mV"Y?iUK2!!`N*
!WrK)!!!$"!W<)u!W<#j!UB^f!X8o6rW!F<E"s6"%1<OR&JQ#s'GLEW+V5.p%LimY&.oKe&ec$!*?Q:?
(DRf1,r%&HHN4-P"pG,,!<N<(!VZT[!;urr!WrN+!Wi6"'EJ:<!<<+HPXSMB8Oc-95sILn3&^an+Z;;?
4$>eo6UaO=:K(=t>$PBCB52=,I!gNmNM-CX#6b2.!!E<'!WiK&"9\f/!W`?!!<*#t!X8].!s/N)!V?Bl
!W<'$!<<-!!B^>dN3[AWJq\l0J:)T_E,B?(BP;*pCM[m-G(#%%Nf]HjS"Za`^!#'fkj%<h`PB,"%LWLE
!WiK0#6b;0"9\f/!W`>r!;QZl!;-<o!<WK.rW3K/!Wrre?j6c7!<<-$quH`trrW0#q?$Tt!<N<!!!WN0
"U#\QE;BP:!<WB(rW!!#!X&E'r;lltoE"F]qu@K6"pkP;!!&H<*YAnn$OI4Q',D;s&eY*S#S.CT%1E[U
%hS^P(D7K&+!MdG()%N,+s\okSH'!&#R1A2!<*!#!WiD]!;llo!WW9"!!E<*"U,)m!4>^%9MA)J5<V+j
3Ar]L0ekF>1c@9Q4$>eo6qC!J<*!+)>[V)TCNY&SH\QU_#Rq+H"T\T'!<E6'"8i9(!s/N)q>gNrquZm#
rrW3$oDf[.!<N<)!s&B%!X&]6#KUn4JVAi0HZsQ7E,0-!AH$$c@q9.`Bl%g8J;9#@NffTqTW#9:d+mgP
mGQNnkSk<J#mCA2":#/8qud-)!s/K(pAk!imJm[s"9el/"9nr."9>/,'E.t5!<N<"!!!&s!r;us!s&H(
q>^g&!sT8OaT)MG!W<!!!s8E$"T\Z,!s/Q&!W2ro!TsFt!XB);!!!(k,9.4'%LWRN%h]Qj&eY*Rrso&<
rX8f:%fHq=&Jc-#+!MdG(DI]++!E*YQQQJ:":,,1!W3!!!T=%T!W<*"!W<!4!<iT.#nsjB:J+5M6TdCi
2`3BG0E*R@0/,.;2)dNW5!VM-9i4hh='8j=AnlF8I1(@SG/>^7#m:J7!!*!"rWE-&"9S`-!<N#srrN$!
rr`9&rrM]k"9AN)!sJT''*A:>%NWi1H[pa$I<KUIBObFV?2e(R?!^lH@qKOuH@^a)MN*aaS"m4&bh2%E
n)i,roK3g!"pY20"9\u8"U+`*rrW3$pAk*llMq@p!sA],!sJ]*"TX_d%/g2+!W2p!!<WGp!WW8t!!rZ,
!Wif9Y5et3qu?a"!rN$"!WrQ)!rN)S!#>S@$j$D/+,hNh$k!IN#n%4T'+tlf%fHh@$k*LO$k3^G%il2n
'cJ,:*ul.7(`FD;,US+7!!3--"98H*!s/N)nGr(ZpAm_b!W`9%!<<*$#6=f10r[oG7n,p43]K#S1,(=3
.k3&"/1rS11Gq*P4[DP0:Jk"h='K*EC3"TGH%CII;ZR"$#m1/."9eN&!WiE(q#LEqquZm#rrW3$nc/am
!<WK(!"oA6!Y7H/E.<7bIX,sMAmeeE=8l5L<E<1'>$PHICiaoOJqf/CP*_cA]?&O^lgX2fWUjU1%Km%=
!!<N5"U"W'rrMioqZ6Bjo`,C%!s/H(!rr<("`+2Cp&G'orWDrtrW3!"!!2rsrW*3)!X]-P$4m"6!<WE$
!!E<)!s/Q%!V$0h!V69q!!!$"!!`u4!"_MB-QWa*$OI+I%1a$^%h/sE$RH,e$OdIS%hB3`'cA#7*uu:<
(`4,0.3i_K!!!'*"98K-"Tnf,iW/QN$31)-!!!',!!*+#30d6784>g-3&NKH0.e\'-mpAj-n6`!0/5:A
3^,o%9MSD^<*<R>C2nE>F,5C7GQ7^F#6Or-"pOi*rrW3$q>gKqquZm#rrW3$nGiUk!sJT'%g)e7$"U/X
I!g?gFDb_u<rc+s:B45j:FAt9;c[%.Ao2U7IY3H7O-?$1\&HePkO%KeVXB6M#7(P9!!EW7"9SN&!WiB'
pAk$jl2V.l!WW3$!rr<-$9[q\!!<*$rW<'#q>pHn$NU;1!<`W3#<tN["T/6#!s8B#!!3$"qZ66fr;lKi
"T\Z)!!Wo3!"WaO.NB$/$4.%I$k<gZ%1Dq<#R_%M%Ls![&JPHe*?Q@D*?,mq(Cr,A>E/[`"U+u.!s]#4
!Wh<]o)Ta0!!*-$!!3H,"9<ar:eXGJ4utSX0J4n+-RSd;(aULV.4Zu(1H.B\77p6J:Jt8"A86%(EGl>H
JV9<h!!WW0!!3B0!sAE%rrMoqrW2ourr`9&rrMTh!<WK(!#,J7"p0^LFEr:\F`;)(=AMIX7nH>O8Kpc$
:K(D'Ao2U7J;&i=OHuZI_9UfqlK.!&kGA^i%0Zb4"9Su:!s/B$rW2cop]9X[%06J0!!*-$!"C(`!!!&o
!!!*!"8i6#!VHF%!<WB("q1S@'n-,f!!E3#!<N<"!!!'!!r;rg!;uri!#Pb>!!!02!!*(S9J%.q$OI+I
$OdIS%1EUC#l=oP$4@7O%M''^'Gqf3*uu@A)&=)0,9KsS!<<B0"98N/"Te_n!;-?c!W)j6!WrE&!=8`2
!17Cs8Ol'.2`*3@.k)hl,Q&]3+sSB].4d/03Bff#8P;cR<*NdDCiFE9K7S?C!!!90"98K."Tni*!WN6$
!VcZo!W3!!"9&?%!WN2j!!*0)quAhc!iglsG'\=NCLpaJ7mK:(6:=4/6:+(08PN,d?tXA"I"R01NKTp9
]?&O[kiUX(l`Up&&-i7:!so/5quH`tqZ-9inGrCc!<NB&!!iZ,!"!ZL#64f!!!!'!"8i6"!VHF*!X&N(
"Ub;<&Y/n+!!iT*!!33!!!!'!!r;rg!;lli!!<9*!!!E0$31/.S3/GB&do!QrX8o=%1ERLr<N9,+peSa
$k3[W%hTKm*$64B*?5n3)^-%?:n@ml#RLY7!X8c.iW/ZQqZ$Wu"9&9,#QP/2Y#eOk76WOf1bp[6.4-;a
+<MXF*?H7D+X8<_/MT.F5t+:88ki2c?=[bfF*MnYG,5BC#mpk:!X8c/q#U9krW2`prW2Nh!<WN'!"o\C
_K:$CGB.M4@9-#d3&`i[4t&TX4?Pem6UsjL>%),bH@^a)M3"+([DL8Djlb1-l*D32&deaA!XAl"!;-B`
!<3)t!!30(#6"T."98o6_?:DM!WE'"!s8B#"9AT,!Wr6"rrD`m&H`1;!!<N-$PofD!rr]2!!!)t!!!'!
!r;rg!!E<'!WiDp!"f;9!!!$*!!<4u4=V*[$jd7Mr<r`8#m^G5'*\XG#7(SA$OdIS%hB6d(`XS<*>0>2
(`")9(aD&>%KHP>#64c."5s7V!VZQp!sJT'2$X*f!4Q!'5t!gm1,(7.-6s`V*?6":)B0V8*?QIP.PEV=
5!qb/84u`Y>@D/]F*VkQE2EsJ!!Ef<!!*6*!W<#t!VcZo!VZZo!V-3k!sST&3t)G?FE25@DeEQc;+3K!
0/>FG3&``R2`a,h7nlrfA8ZU@JqSo;QD:Xrak#>/gXF<]*t8Vh"onZ-!r`2o!;$<_!<3)t!"/f3#Qau+
"98E(ecP^K!<r])!!!'!!r;ri!"f><!WW</!!<Y'!!3--!WW3%qZ$TsrW;uurrMZj"9AN)!Whro!W`E-
rW#(d!!<5"5pR*X%1*@N%1EXQ#mUV:!sA`1"pP;<#mq(M%M'*_'Gqc1*ZQ.=(`+/:)^m#9'*/(F#QOl.
!pBX\!;cfj!!*0)rW#(c!!r\:=[kPA4#8QC.OHDa*ul4;(`4&+(`=53+<r9c1,h<]6UaL:9iG/#ASZ@3
EcQ/p$j-JC#lju/!rDrt!VcZn!VZZo!WN/l!!*3+quAee%aTB8Ble*$?Wg)f1Fah)0/G@<0JG4<3'9Mu
:KLq=FFA[kKSYe_Wj]mof\PNJXiht("VV+@!!E>p!;$<f!!!&s!<3)u!"8i/#7:P5!<`B&"kEeR!!<6-
"TeQ%!!3'#q>p6h%KQ\;!rrH1!!!(_#Qau2rVus#!W)ls!r2lf!!E<'!WiDq!!30("o\K("on`*&#h];
',:r_$4RCO$OR.D"9&?K!sAc2"pbMB$k3[W&/#]p*$-.@*#f_1)^61I/Z]Tf!"K/4!!ED_!;cfk!!30'
"TAB2"onr0\5YjY6TQtT/1;bs+W_U@(`!i$'GV>u(E+;;,q:Q*3^5nt77^-N=C5TREcuA:Kp`5N!"]A8
!<`K*quH`tq#L?opB(6no)Jdo#5eH;$k(C%BkML&@9cf(4>8*.-RgSs.Ocet,;1i34[Vh>>\A&&I=Hd#
O.</V_TpZ`hVl)`+Vk4o"onW,!qZKb!Vl]q!W2rs!W2p,!<i`1!!!$'!"%?^!!3#u!<r])!!!'!!r;ro
!;lg$!<i]1!!<N+!!J>h"TSc+!!*-%qZ-Wtq#U$d"9AN)!Whro!WiK.rW"ST!!<4s4!YLT%LEIN$OR4I
#6Y).!!**&"9eu7#RUqK%M'*`'c@u5*ZZ4>(`"#"+;uRgV@j"3#m(),"Tneb!;cfk!!30'"TAB8"onr0
Yu*kN6TQtS.OH;[)]9G,'E&Oe',2/t)]p:Q/Mf@L5XIk.9N,)%ASQ1+D.]2q"U+l7"98Q*"U"i,rW)ou
q#L<nq#^Hpo)Jgm"U=l)3t)A6DJ*R%C1(1A76)tH+sJ6W,9e<V-7LQ'3Bou/=_)DoH@1-lNLHcP_9C<V
g"=WZ*>Skj"98H,"8Mro!;-Ba!<*#r!!*0*r;[$1$Ob,^"UY,-!<WE$!!WH+!s/N)!WE-#!VHF&!<i]1
!!3B*!We8d$318/!!*-%qZ-Wtq#UHpo`,*q!<N<'p&G0q!X&]+!"B)3!<AEO+Vbb'$47.JrWrT0"8i-A
!WrQ/#7(YE%1Wm\&f)?)+!)FB)]0;,*ZZgmV%3_0"o\K'"U"ki!;ccn!VcWs!<E9*rW#+d!!`Lt<BiQ4
4#/B:,Te!D().An&.]9_&/#Wl)''kI/29(G5!VJ)9N,,'Anl4&DJPYs!!`K1!WW6*"TnK#q>gEoq?$Np
rW)Wl!WiN1qu@?9#.8G\Ao_Wn<_c"@/0l>Z*?G,!-6=<U.5!J?6VCHgCisuJH[gsAVmO7^c-Fnnb-;d#
"q1S6!XJr1oDnOboDngjqu?cu!<W6#$ipM<"cWWd"9nl,!!2rs!!3'$qZ6`uo`,I&"U>,0!X8W.#E&Zp
!!W?%!<N<!!<3,r!V-6g!VZQs!<N<+"o\K%"TAB$IKWFg()@G[$3^_B#RCS8qu@i?!WrT1#RUqK%hK<d
()e28*uu=?(DR`,+>c-O%0lk6rW!!'"9RQ_quQTnrW*'%!sJT'%gE"9!/FuE4@;1c/12V_)CQ@8&eGQ`
%1NdW&/#Zn)^$FV0JtmS5=.e4;d3^CC2@a+EKl%T#64u-!!<E/!s8E%!!<*"r;cZpqZ?Zro)Jjn!sT#.
!"fDAR<r4NEG8]X90bBd,9@a?rY>SP)&sbD,qC]05Y+g[BleHAG^YF9VR+%XaiW&d`2FCf"ptD3!so/5
g]76Qp&GC%!!<3l$NL/7#5A/u!WE2u!ri;t!;um-!X/f2!!*6'"r)Id'*8:8!!*-%qu?d!!Wr/unc8Rg
pAb<s!WrT0rW!B/!!!=&DAsB*%LNLL$2t22"TeK#(BFR?"pbPE%M'*`'GhZ/+<DL@(`!l(*X<rI98<r\
!!3'!!X&T+i;ifWq>gNrrW3*&"TAB_"TSN3=ar:k5<1GK-6X?G'bV#e$k*LO$k3[X',DK.,:P6%3BTMl
78$Q_?tO.jDfK]^DZBtA#6=f)"9\f.!Wi0"quHctq#UHrq>p6h"T\W+":#50!%Je!Qr[a6Am8,&4uFl:
*>]A#%hK?f(`X\H/i>d];-[aRFEMbQLR"X=]`,k[dalL$',Cf]"98N0"p+i(!!30$!94(X!VZR%!<`B&
!?O#s!!ri1q#CBqrWDuurrMio!s8`4"8r3("trLU%Kcb2!!*-%qu?d!!Wr/ur;cNkquQNl"9JZ."U4c'
#8SVE)&a"o$N:A2#QP#'!$21D"U>AC%M'-a'Gqc1+<DI='bqN(+Xf*RBb(=H"9&<#!TF+Z!<*#p!!!'!
!r`<$!'C>`!#[;V1HdcX0InFl)]'/!%L`^P#mq"I%1a'd)'0tM/Mf@J5!_S0;-7.9CN"35CReH."98`0
!!!*"!Vlf_!VZR#!!!$#!X&Z4#Qai'4<Z_j;IjEL=\hFJ1b9ml'b:ZZ$OmX](`jqQ1HS!#>@qeoFEMk_
PG#%g_o'=;d*H_H&d]'R!X&`3!Wi9#rW1pWrrMus!s&H'!"&c0!!!0(@fQQ6"o\Q"!!30&"8N#u!VcWt
!<WN2"TAB*!WuC8('as?!!*-%qu?d!!Wr/unGrOhpAb?t!WrQ/"oA9(%L\^H+:AMW$46V9!!N)t*WZ?H
#7:kL&.oQj(`XV@*Z5\+'c7u;/2;09'`\4:d/X4K!<W0$rW!W5!!!N>V`$n"1b^C)*ubt.%h/mQ,RF__
#n%.P&JZ0(+t"rt3'0;i77pEX?"IhmF)kZi2@9Ec$3^8,!!3'#r<*$#mK)q[#6=l."U55<!rN$<()snb
BOG.I9gUou/LDJP$jHk?$4RR_)^6^c3Z^X`=_2JjF*)Y[Oe/S^^qmb/`SF6)%1<aT"9\o3!r2lM!"o>8
!<<*#!<<<(RK*ft!<E6(!W2ot!VQTn!W)it!X&Q/#6b#+#6t6s!"fA<"9&9$!Wi3!!W`?(p]9mb!!2cn
"p"f/"9er0qu@!(!0o,_#m^nFr<NE/"Si$:!<WK1$4ICU&ebus*$6:D(_[Gp)B^@^1k$kj!rr<*!R^rK
!<W-#qu@?1!W\l\7kl_P.jQ5V((q,d$46\;+UJMb%h]Tp*?lj_1,h9Y5t+CB<a93QFEDP-Zkj2P!t,>1
!!!'#!rE*"!q-0^!!iT,!sAf5#RCP2!':5f$+!rQ>$4iu5rpkU-QNm."9Sf5$kO-l+Xf'*6V^cpD/jW=
H%_<NW3sCS]#_MB.iAU$'+G*J"U"Z(r;lfrhZ*`Z!sA])!!WN."TYqH)#aL;!WrK)r;Zfuo`G!krW!T5
!sJl3!<E0,!5edA":#,5!!!&s!!30&!q63j!U]ph!<NB&"98K!!!\-I+:\bh$N121"p=Z$*ruHI#7:kM
&/#Wk(E+86)AWnq(*4VF4[s]1%0-D4!SIJL!!**%qZH`r&HMk3O'=h+1Gg[1+WVC5%h/pF#pBWa%M09h
)BL+O/M]7H5!h_4;HI+8DfBQ;Cmt_7!!<N2qZ-Tsr<*$#mfE%\!s&H*"9\o6#RCP2!'LA`!2"@?>$+j"
5s.([-m'04"U##9%M9Hq+t59.6r$lqD/jZAI#!u[Wj][RZGsZ!)\<8_&.AaH"U"o0rW<'"f`2*T!sA]'
!!!$)!Djs?#Qk/1rW2osquQWqqZ6Zr!<E<$"9\`+!"a8O!!33+"TAH!!!30&!q-0X!!**%r<!$#qZ$s*
5'S1a%20-S"U5#3"9SE"+9;NH"U>AC%M06d'G_N')Aj2#%i?K6,Y;<R"TSN(!s-gM!W`?(r<!'%!W)j3
"%A)03AWZL-mToR'G1f`$OR4K$k=?j&eu6'+=/Hh1H.B[6UsjM=^Gc\CM&$KEruCB!<rZ(!!!&o!q66_
!!rZ,!WrQ/"pYA8qZ%`G;kI/q<EW'a4ukAJ+W(^r#RV"Q'Gql:.l9@X:g.CH'Q\JFJ;fqmXgl-RX2DoH
'*\^L%1<(=#6b54!s/N)!U]se!U]pl!<N?*!WiE%!!``7Du^CM#6OZ#quHp%!WrK*q>pNprW3-(#6=o/
!&kVj!!EH.!W`?!!!!'!!q66Y!!!&t!WW8u!!`u=SfSg`((L6H!X&T+qZ%f@!WrQ0#RUtM&.oNg'c%Q$
'b_,h)C?UR;1p\-!!!$$!<C[Nr;lp"rW<3'!Wi/u0FSGo2a',_1b0pu*#92!%L`aT%1a!_'c.f1+snfn
1cRT_6qC*T>@;2cARL"_3s>N_!<WE$!<3)t!r`8j!V?@!!<E6'!sAc2"pP2,!&Y?*^JA$6>#7XQ4>\T6
)\W\j%M9Em*$H[^2Es`1>@h\oH@LX3T;]!*^TaQIem9'l"pPA>rW`W3"U"o/!<Mfmq>gKqmJm7g!r`9&
!Wi6""sh#&#65&3o`,0s!<N<)!Wr6"qu@$(!<<<3!!Wn3$iL&-!sA]-qZ-WsrW;QimK!4e!!<-#qZ%',
%$i%](`<ee"9\f.!W2p-!<N?+"U55>$k<g\&ebrX'FPQe%hBX/,:?c`!sef*rW1[PrrDuuq?$Ztq>`/[
UcCe)5;t2D,p+!?'+bZa%hK?e'c.c/+XJQh0JtjR5t+CD=^>KOE+3()XUGC3!<3)u!9XCU!<*#u!WiH+
"9Sc1"9SH#2$+Z$9j:Y%;+O&<2_QO#(_[Mr()e29,UtN/6;(9`B5`!BKSu1lXL#OPXIm#P-Plac!sSu.
#6Y25!s/Mi!;ure!!WH*!WrN+!W<!&$?HFR!"&f"!<3)u!rE#r!!iT*!!Wl4$Qmdo!!<9)!s8?"!!3$"
n,_tXquQNl#6RAN(CM2q"TAH(!s/Q'!<E6(rWEQ3"U>AC%M'*_&JG'V&J5N_%NHrK.>1n/!!!$$!s8VV
!<*#q!r`5s!#5`8Shhrc4>895,9@a>'+kfh',;<#(`OJ<,Ub2s1,V'U6qL-Q>$bZQD.HY@C^^.@rrN&u
quHctmK)t\rW3!"r<!-)"9S`%!$D\SX[kib<D#\F3]&B6*Z5e4*$6@N-nR8=78?okBQ/8;K8YqaVm!J=
\Z:tCN$/T0!WiN0#6tM>"p>#0!UKgb!Up*g!<`H*!s8W&!!EG3!=K53!!36(!Vufh!W2p$!<N?*#Qb*(
4TGT`!!<6'!Wi3!rrN$!o`>!mnc8Ofq>^Krr;[95"0F'W*t\VU!!3<-"TAK'"T&?D#71bJ%hB3_&ebrm
%h&gT)_!^$R2->6!!*3,"TneX!<3)r!r`5r!%nWg^I9J=4>SQ<-6sZP()%>r(E",2*Zu[T.k`V62EF)n
9i>"q?=IS^Bi_J_'`A%2!VHEm!;urn!r`5o!<*$!!r2p!!Wi,t1(G#A<B48_9L_<23AN*1+!)OK,pt,n
0fVHj;HdODEd`b,S"m$h[C<HCOPE&I!<<*$rWWT4#R:P;!s/Mo!;cco!V-6h!WE-%!s/N&!!NE(f)PdU
r;Zp#"pG,'!<*!!!;cfq!"&c2!!!K9S,`ir!rW/t!<*#r!qlZm!WW9"!;HQk!Vud0!<N6$!<iZ4:43Wj
"UP51!XK&9rWNB."pYA3"U##9$OmUF%i,`j'bq5d$kX=$7V>p-"p+f*":,26!SIJP!<<3!!r`5r!&"?X
%pkJQ5;G5R-n-Vl*uPh0(`FD9+<i'Y.P<J52E*]a8l8\n>%)#P??(U6$jce3rrVclr;lQmp&P*nrrW*#
rW<*#rrDor0*`/&TKZ7E;G'5?5WLPK,pale/1iM12EaK(='fEQF+B7<UT(B'\Zhm5\!&*R"o\N$"pYA=
#6k>6!WhWf!!<*"nc8Of"p+i.!!!'(rVut,!;lg!!t,D<oDnjk('"=8!<N<&!!Nc2!!I4B!!39)!!!$#
quH`tq?$BlqZ?cup&P*nrW<*#q>_63!rr<)%KHYCW#?]W&Hi(9$OR.E#:9Z\#RCY>"pG5<$OmRU%hB6c
()IMh%i-$-=Gddm!"9&3"UYJ:!SIJQ!W)ru!VZR5#lkAS]f/;+68U,B0.J.d)&XA7+<i$V-Rp]&'Jq^,
3BT]'<Ei[2@VB+OI%MMa!!rQ(rrV`krrM`np&G-p!<W0$rrW0#q#D`F!"C*j6W6*M9gM*75;t;J/1iM1
1Gq*Q6:t-Z@:sJ$K92\'X/lW8\uM7-bsE?S$N:&)"pP;<#6k;5!p]jd!r`5k!;Z^"!WrE&#7pe6"2Y$<
!WE'$":Y_BoDnmlrW!K1!X&Z,!!a,:"VJi\&c`.:!rr<&!W2ot!Vlfl!Vult!VQKn!W<'"!Vl^5!<W?&
"UY;6!(;bU*t&2T#7(VC#mgkC#7(56*si8]$OdIS&/#Wk()IVq&K;`XI7OD>!"&o3"UPD9!W2rS!<3)t
!ri;p!&+WZ$3O>*01RrU0.ne),p=<M*ZlOM,pt,m/hf(=3'9Gq9iG.s>$Y]EEh$5=!!!6&!!*-%nc/^l
!<Voqp&GF#!WiH+"9S`-!<Mop0EM4]"^J5o>"qLV6pX%!2`*<H1c@<S4[DS5<Es$KEdEG$R\QaYWj&.u
c%%2U"U=r+rWNK1#6k>7!WhWf!WW9'rW2Bd'`e=:!s&B)#R:J4!1O&j!WW3%#R:M&!!!'!!XSr1!!!'4
!#.3rrW!*,!rr<&!W2rt!W)rm!Vult!Vl`q!<3)u!WW8r!"f85!<WK-!WWCU;A(8^%LE@GrX/]4rWa2E
$4I@Q$k!CN%MBKl()If))&OMP@#t9e#Qb27"9o)8!s.'TrrN$!!<E2o!&+HW#6bg/DDOs?1bC.)-mg/^
+<VgP-7LJt0/,+<3Boo'9i4nm>?bNKLoCX_!!*/g!<3)l!qlU#!<N<)!sA]-!Whup0E;(V"rEqY6XN8R
6U![u5!1kd3BKAh6qC$M=C,QUG(5:-Q(+A=TVJ9oe1)FK#6Ol)#m1;5"U5,5!s/Mh!<3-"!UKdg!<E6&
qZ$g%C+92g!!!-%!s/N)qZ$TsrW<*#rW!*&!s8T+!WE'$$P,5;rW!!#"9\W(qZ-*dq#^QspAk3or;ls"
pAc$2!X/c.!#5taT0!#j#6thN#n%.K#6kD>+Uenp&Io0U$P*sj(DIf5+sA3\0TnU#!!!'+#R1J:"9JVW
!<3)u!ri;p!"o>9!!"#X0==h&3[cC2/gi"p-2o(i,q(;B0*Esd3^ZLI8Ou]_>$>0;>I%-7rVus%"7?-h
!V?En!VZR#!<E6'!s8Z.!Whil-lj<c^LT#m4?Z/%5X@_%5!D4u7S?NU='K'FE-m:nLQS'pR@0D%h0'>W
&I8LA!<<*#!WrQ/"Tnf,l2^hcrW23_rW2uu":"tY"pt8/":,&/!!<*!"p"c."U"l-rW!*("T\T+$N:#.
!<ASk"TAB'"pG)0rW)fqncAOfrrMiorrN'"!!2cn3!'3d!Wi?7!*#<k'H.N&'+,'U$3pb?$4[[`'+YKX
$P+!m(D@oC/hK@LNGeh%!!!'-$3p_:!WhupirK)[r;ls"p&H]G!sJc2!#l/SX<9,R/NGO7.P*"p,U=`e
0/>:;0JPIJ7SZNE;I<d:De#u+&.SU=!X8f0n,WIhrrW0%rrW-#rW2`nrrN-$r<!'%!V6:E!rs>MD7D5`
83p$C6Uj[=77B[;9i>%r?!h,XFF]7'K8uCfPG45nW\#G&"Tno1r;[!%!sJf0!U0Ua!r`5a!!30("o\KL
!XSk"":P87%Kc\2!s&B%!<N?+"U"o/!<<*&"onW-&I/:E#/:ufr;Zp("p4o)!<3)k!;urr!r`<%!VcZo
!W<'"!VHEn!X&E%-NX8QBoatX.2*7'%h8pO"9Si9%h]E_#mUbF%MBX$,q:;o6][68(B+:=":#,6!s/K(
fDtpPr<!!"rrDfo/-?"V!!!<*&pL!;,XO.:0etO=/1Dts/i#=C2)I0N5!qh8;,p[q;eE//*$G4\!WiK+
mf<@grrW0%quZftpAk3orrW-$!<N;o!<)sL#lkclXAh&X7nHHR<E)gk:Jk.s?XdS[Cik&VLlIIWNeW.J
e&F=)%g`CA!rN$%!<WH-!WhNcrrW0#k5Ynl"98E)#QOuI8e_F/!t>G7!W<#t!WE'3!<E6&!<WE*!!!0&
!%25n%KHS0!!39*!W<#s!V?Bj!W<)u"9/Ds!<*#t!WW8o!!**%rW!Q7!!!Im<&6NX&Jl&i$O?k9":,nS
%LiaM"pYG=#TG<D-9Oh)RfETl(CL9G"9\K$g&V-Rr<!!"p&Gp2"98E&#QP&CSmk,a4>8fV3&WTI/MAn=
rAk*D5!hM#;@[&8:LIgYXpP[>(^g<D!Vucr!VQKp!<E9""8r<"!VZTo!WN6"!s&H(nGjsC!!sUBDcL=I
9j:n1?X?r>>@1oSCN"9<IY<E0Pb!qhNfTRN+X-q3!>5P2!!E?+!s/Mf!<3-"!TsFo!<N<*#n6q=%p/l;
#RLhF"TAB&!<WB#!!WH+"9\c+!r`0-!X(3d&c_n?"98E&qu?`u!ri?%!VHHl!W3#t"9/Dt!;urs!ri;o
!!E<&!!*0#!!Wh#J.<;7#Q>)H#mLM:$4RLR#RCbF$j[1U-R:<.CR>P0!!Wl="9S`-!W<#t!VcZU!<*#u
!r`5q!!WH+"9JQ*"9&9C%\o",/j([B3]oJa2`a)f6U<q'7S$0A85EAa;Hn^M(&e19$jQh7!Vufr!VZQq
!<N?#"9/H&!rW/p!<*$!!rW3&!W`>m!!!'!!%&G`SM`oA:L7XIC1q3nD/jZ?G^bC+OcPTgR"p<IUVS>b
#m_.O"8Mp"!WrN+!U0Ua!r`3#!U0S$!<N?+"9o)2!WWsQ=qV,E'F=a>!X/f3!W<!2!s],="9So>#QP&P
O9Q3q!"&r+!!NB)!s8T*o`4slr;um!rrMoqrW3!"rrW3$oDgTI!s&B,%0-A=>_OXI,8:=f%1<FK%1a!Y
#n.=U&.TBj0Ju.<Jfk3s%0ut9"U"o/!W<!#!<N9&g]7<SrW;osrr=kU!!*-("U,#0!!N]0!"rk-5WVD!
2EO5k5XIn18Ol3@:/=Y[:eb;%@#C'o"oo#8!!!'%q#LBpp](?r!Wr9%r;uoup]19orrW-$!WiB'nGiOl
-jfqU*-A,_=_h\\C3"?6F*;eTI"$g1PEqN&OdqPnY,sc!!>,Y?!<Mur"T\]-!W`>e!<3-!!U9Xh!<WH.
"9S`(!!iT5!3Q;2$NL/1!!NW8#6Ol)'`eLG$k*FK!!aPFKg,PG!#5kD!WrN%!!**%rW<3'!WhuprW2s!
qucs"q>gHpquZiuoDf@%!!!$%#7^_P40E0/!Y#&7#7CnH$k3a]%i,Tj+t+Q\&o4%I('"=9!sAW+!s8T+
!WE'%!<E6&!Sd\S!WE/s!W<!%!<N?+"9\T&*s2lN+@j4r0d\e:3''2e5X@e.8k)3D='SU"3/P"`+8l0A
!<<*#q#L?op](?r!Wr9%r;uoup]1<prW<$#!WiE(mf4U;&-sjjesTB-?!h#OBPD3tDg$MTI#4,XOGn"a
g6"<%#R1D7qZ-No"T\]-!W`>e!<3-!!U9Xh!<WH."U"o(!"/i8\gIX]!!a&C!s/?#"9AQ,%heg@$m;u6
%0-tH#mLP9!s/<"#6=l."9S`-!VQNm!W<)t"9&>u!;urr!r`5g!%J*W"s+CsUIYIk)]04u$4.(U*ubq-
'/276NK#b%!!N`4!!!'%!<N<'!WE'%!<E6&!V?BV!<*#t!rE#s!!NB)!s8T*qZ%]C#ppaH\mls65s[[r
3&s)j:.[`74&o<nVP-Bm"U583!!!&o!;urn!!30&!rN0!!r`3#!VcZp!WE0!"9/H&!Ug"6"qMG+0ppF>
6:kWq?sQu@?Yjn,DJX-ELm??,@kJW6'*eL;!quZu!<WE*!<MHcrrW-"r;c6c#6=o0"U,#3!r`0-!t#M<
!->OJ!"B;?r;[T8!WW6&"9\c+#EH%h'`\C=!rrH0"p=c'#QXu.!sA].!WhuprW2s!qucp!qZ-QqqZ?cu
mf3Fk":582!#I>[T4&EH+<i$R*uZ"<-ndhPMmRR+%1`78!<E8s!WN6$!Sd\S!W<)n!WN6$!rDs!!=/o/
!#Io)[<jS_6V'jC8jkp38PNDlT>Z9\'bg':r;lZn!W`?(qucm!r;lZnrrN*#r<*'$rrMTh!s8c>&L%Vh
&5pHiP"82M@:a%^@:!GZE.<>TkFiVC.0p:f"TSN(!VcWu!<WE*!<MHcrrW-"l2V%j!sJl4"9S`)!"Au6
$NLP;!1/cl"p#5A(^1-P$47:Y!!3@9dNA\o!WW?'!s&T4#6Xl(#QXu/!sA].!WhuprW2s!qucp!qZ-Qq
qZ?cun,O@.!Wr]:#mUe;!AnqrHpTJ4+!)OR4&g`uN&Ck?!#>P7&Hhq2pAt9qrrLmTrW2s!p&Y-orrMus
*X3#\$P<[S6AE+;?;=$Z6UXLJCm:lb4TPO#!!!W6r;Ziu!Vl`n!VcWr!<N?#"8r<"!VcZp!WE0!"9/H&
!V-4=!<WH0%M]]o*>TPiQ-6%D?s?]7=^Q*$Xhq>E)@eD3&L%ee!!36)!VcWu!WrK*!<MHcrrW-"l2V%j
"9eu5"9JW'!WrH+#6Ol)"Te[gi.r$D!#,J;)J6\A!rr<,!!!<-!!!0.#mUS1!!iT,!sA`/!s/N$!;ccq
!W<)t"9&>u!;urq!ri;j!!NB)":,>8r;[B9#7`b,J<,kUQ^<VP6P]Y2rW!$$#S."7!;HTo!ri;i!:Bjd
!W<)m!<N<(!W)j!!<ri4rW!N5'c%ofJXs!P[CEW@M,PT!&H2Y3!=')8qu?]tq#L<np](?r!Wr9%r;uou
p]1<prW<$#rrW3$nGj^6"UGSN$jd1D%j</L?')2(`lH9E\XmIo(aft)'+u-&%fQG0!<WAt!<!!!!U9[b
!rW/t!:Tt7!<NB-"pG,3!<N<'!!N]7"TSN0!!*35-!chE_RQ+P3=Gm*!!3#u#RLS5!!<H5#6Xl(#Qb)1
"9\f/!WhuprW2s!qucp!qZ-QqqZ6g"!<DTh!s/W3#lO`'!qH<s"TSN)":YnO!rN&n!WE0#!Sd\S!W<)m
!WN3$!W)j<!X/f0!!!00#m:55%LE:M)]05%&Hr.B!!*-'$kEdD!!!&q!;llm!!30&!rN0!!rW/p!<3*!
!rW6$!ri;k!!NB,#n7CP'EnaQ'bq8g'ce/-+Y5,j-RK`@+V4Pf"!/O&%K-8-!s//sr<!!"l2^hcr;l3a
)?BmB"U5,5!s/K(!!!66$j[1J#6b>C%13:A!<`N(!!Nc9!!!K0rW!6-#Qk&,!XB&<"8i-#!WrQ("9JZ,
!VQNm!W<)t"+U~>

%%EndBinary
grestore
np
grestore
RVGGZC+TimesNewRomanPSMT*1 [24.025 0 0 -24.025 0 0 ]msf
99.27 389.607 mo
(...)sh
gsave
2.1066 410.531 mo
44.0636 410.531 li
44.0636 353.277 li
2.1066 353.277 li
cp
clp
2.09 353.19 mo
44.11 353.19 li
44.11 410.61 li
2.09 410.61 li
cp
/0 /CSA get_res setcolorspace
gsave
clp
[1 0 0 -1 0 570 ]ct
[42.02 0 0 -57.42 2.09 216.81 ]ct
snap_to_device
Adobe_AGM_Image/AGMIMG_fl cf /ASCII85Decode fl /RunLengthDecode filter ddf
<<
/T 1
/W 116 
/H 159 
/M[116 0 0 -159 0 159 ]
/BC 8 
/I true
/D[0 1 0 1 0 1 0 1 ]
/DS [
[AGMIMG_fl 116 string /rs cvx /pop cvx] cvx
[AGMIMG_fl 116 string /rs cvx /pop cvx] cvx
[AGMIMG_fl 116 string /rs cvx /pop cvx] cvx
[AGMIMG_fl 116 string /rs cvx /pop cvx] cvx
]
/O 3
>>
%%BeginBinary: 1
img
jT#Da!WiH+o`PL'"U5/7"9S]%!#YhA"U#&9!!!*2&f2/c"U,8G&.]Eh&ISpOqu@$-!rr<&"UGA;!r`3"
!UBa_!;?Nn!rE*"!ri;i!!WK,"9SZ+!r`0&$4dg^"n;R!#nRII!W`<'!Wi9#"9AT."9S>urr`6%rrMZj
q#LEqrrW0#lMq=r#RUtN&I&4<$k3^Pn,O()%1*+="UGJC#Qt//!s8Z.!Wi9#quQTnncAIbqZ-EmmJmIq
"U"i/!WiT)!!WT2"p+c+"9&9%%LN=8!!<9)!WgjPrrN-$rWE0'rr`6%rrWN0"9eu6"Tnf,q#D96"U>88
!!3?4%L<FQ)DtN;ML]D>4=V9`%/g/+!W<#t!W2ot!TF+U!W3$!"9&B%!V$0f!!E<("9er,!!*-)rW!?2
*B7#1=[Fb^&I8RFrW!!#"TnT%!!3'!"9JZ.!s85trr`6%rrMBbq>oj]"To#=%hB!I!Vl^'(Go!#=[Ok`
&-`4<r;[0,!<<3)"U5,4!Wr<&!!;orq#L!emf<1bnc/gp!WW6$!WE'&('ss@&HMe1$N^D4!W`E($31&-
"oA9%!<N9&f)YdNrW<'$!<N<$!!rZ-!sAc3"p=u.rW)s!qu@T;"pYGB"qhpc,&sdEj42&T^<PKn_3.kI
"p5nV"9R$Pq>pEo!!2forrMusrrN&u*!$6K#6k;2!snr4;2VlmV3$1]Pc1jQD)`"*&Hqk/!<<0!!r`5r
!;lot!U0U_!VcWt!<N?*!VQL4!XK/A$3pP5#QOs$L:+@^Ndc\HVm)D"1^O-hqu?]trW!!#!Wr?'qZ6a!
quQQmp&X@WrW2Wk"9AZ2#6Ol)&-`+;!%b%bBKdFn>a)L:-5$1V"9Jc1"9SN%!W`?(mJuJOrW2s!!!2rs
#6=l/"U527!r`0%!<WE*qZ%Z=$P!mZ-]m&bSqDWIF(]]QH#AJ=c-sNo.ME%#&-;G(rW2Wkr;lfrq>g*f
q>^["!WrQ/!rDut!W2p?!X&c4"98[@XEnDH5s?e>/3P^;8ogAuS0/@C!!ir7!W<!#"9S]+rW)ouqZ-Nq
r;l?en,NUm!sAc3"7lL7!X8`/!!d5>HXoT34XqC#4"_mMD3UZW(^pBE&ebHMr;[$)"9S]+!Wr?'rrW-"
o`4jimf3@h!;QWo!VZR/!X&Q)":"r-!!302i&2>Z(B=F9"pk2.$l*Htf`2<i!<<6.!Wr?$!<WE#!!!&S
!;lln!!E?*"9o&2"9SQ&"p+o2"9JW*rW!uB!#-l8goQ$MEcc8>KU%FBK84DNB8*GRc#FO2*!c0;!!3'#
!!2cnq>p<jquQ<f"p+l1"pY83quH]s!!<3'rW"&F!!NsCY&ur],U+0F.QT4,.l8C^,=ZddUJ:dh&I&ID
rW!!("TnW&!W`?'qZ-Kpr;kgV#6=o0"pYD;!q?6m%:?8^(dg)-,oddO2_#dm//\d54DD$l:]h"B#mL8-
!X/].rW*!#rWE9)!Wh'V!s&E(!Vl`o!W2p9!<E0#"q(M5!!NB2!!.9X!WW3&#S.:H!s/W+#Q4W/#&mZS
!"]SH"pY&,!<`N&!;HTF!!E?*!s&E#!<WB*!s88u)](-FhJRseH[UL"Lk^S<Ljs]/SsG4SH$dlo4p)6J
$Np,'rW2]mq#U3irrMNf!!E3'rW<-%rW2`n*srgXY;8<c+s8*W-mg5h/LD]%:.[`)4@Z*X,lf;!#6"T)
"U"l,rW)ouqZ-Wsq?$Zti;`u^"9er3rW<6(!<N>r!$2T=X>E0k.OQSj,p40J*YoD<5<C\I0fY;n%KI@H
!r`0-"U+u1!WiH+"9S]+rW(jV!W`<'rW<0&!W2rs!VQKo!s\](!sSmA?2=O&!<WE#!"&c/!!!FMGQ7^J
"TAB(!<WH,!W2ro!VZTV!!NB)!s/K(rW3'#rW!-'!WiH,"9SK$.0]hm9C90"IpRGJH?OXdK7\AhH@pm%
I!9^OF'XXdYTjc!!WiH-!s&Gl!<*$!!r`5r!:'Uh!<WH,!<<0""9JZ-!Vl^<%5c4`.l[nV'bLli*?laM
)C-ph/h8>!-T!5X`g.,;&H2Y1"9\W(p&P$lqZ6`uli?n_$NU;1!<N?,"U"i+!rW9'"9S>u&LG/A-o___
*Z,J&()@Pj!XfeB(^qB&*X4?_C]FGH!!!)t"TAK(!Wh-XrW*<,!sAc2"9S]+!<3'!!Ug!n#GO3Y$31&.
rW)s$q?%?5#64r@$36_Y!"&]+"9\f0"9SH#rrN'"g].N\"U>89!s8H&rW!$&!<<,t!#l"G$kasFhj7;p
J9P^bKR\Q+Jq/5oI"6j&IsV*D%WlQ<b/%$h!sAi<"onW)nGrRir<!!"k5Ynl!W`9$!<WH+!!<H/pAb6t
(EFR2C)T2c(B>6`%hos)+X89]/1rS*,qCT)0euLrSN$KI!!N9$!<WDt!;urq!ri;b!"T)4"U5,4!sAc2
!WW?."Te>t$j$[7>7`bF*![Z*&J,Tf%LWID#7D%T&.TKq+;u.UMi]Xk!!ri3!!3B0!s/N)h#ITZ!<N?+
"o\]-"U"o+!WE'!!rW8u!"8l@"T\Ue%1ECD!!*3"!!iT,!s8T+!s8Z2!!!0+!!$1oqu?d%!s/2t!!<*$
qZ-TrjT#bm"pkVB"Tnc,!WW3%"TnZ'(^^up)%6j-BX-TGCgUdqKTC\<Lk^M4It.HH%XibTJ9l?bJ8&(g
Rb(:L"t:)q"TSN)nGrRir;us!kl;.n"9el/!<<0(!s/W1!r`0O!t,PH!!"$9QGQKU)\s2/*!Zlc()\/<
.5!5(.46Ml+WVm`*toZ+X!n#[!!<-"!<`N(!;HQn!W)ou!U'Ln!<i]7#R(>5"9el/"U>//!#>_I$jQb4
%6T-?4<tIL(*Fn9',1uc$2t/K"pG/7#RUb>(+C@F,\a;+!"],6!!!$*#6P#.q>fRV$ipA1!X&Z2"pY>:
"U+f+$ig8.":,>?"onW+#Qju*$3gKF`"rCR#R1M9q>^[#!sA]-!W2p*"98T*'USq%$NLD4p](<r"9&H#
!<*$!!9O80!WrQ/"pYA7!!392&Io-V%gN@g=g%>HWJ[-E?X.GiJqei0L4t5/IJeI*I=Hj"Isc^!Kk#7R
cCQ!b-PZdQ!<3)u!r`5r!:^$u!<N<*"U5/4!!*-+$O-G./.F_'d^4^;DBU/:)Aa>.$kO0l*$?LU/M&A!
,pjub+sJEl3Z^4LSok#5&dRn+rrMuu!!2`m!!2lqqu@0-!sAf5#R:G3!<NN8#Q=`B!!!KiM9)Q79i_Z6
#8.^j)\Wl!&If'Q#6tJ4"W.LP$4IOi1Hm!C7@S>u!#,b?!!EE,!s/M]!!<6'!X&B("9S`/"9\T("T\W(
!s8W(!"oSB!"/c,?-nri(CpoS#7:Y@!r;m#!<WH-!s8?""pPA6'aW&1oDf!q!s8Z/q>gNrn,WFgo`,F%
#7:kD!XB/C%2^E=1`(_ef?'k;>>\1p>[V#]G'\OcJV&H'I=(s='mb4SIY!0,Jp_WUE->9/nr+_4%1NC-
!<3*"!rW/^!#PkG$O[(;!<`B&!t5DG=eD^_G"aA-*-35J*>]e:(_dVu)BBqF,q(5m-mg2b,pjuc+rqUJ
0,6df@/pB0"8r3$!WiDt!<*#s!ri;q!;lli!$_UP$O[%:!<iK(#8%C]@&L/sE^UrZ#[IiI#o+0j'GV>s
'+c,n$OI(E#6tMA%1s9i(DRZ,/.t.\@/pH2"p+c*rW<-%m/[+dpAc$3!sAc3"p=u.!!!$"!!*0'!<`Q/
!WW<+r;[=:GZ,Fe!<i]8!!EK4#mU2*"T\Z,"9\i+!;lg&#n[@AK)bl["8Dir!rW5b!!NB)!WrK)pAd2U
$46k9!"^Cb!%`!"o"f`_<F'BUG&bB9BP2I1G'JFaIXQWjG^"=SG^4XaIt<3'IW8q@I;EP@hZQ%a'GL]=
!;QZf!<3)r!($\d!!*92%LW=<!!Eu9!"),S]n\cp'HAVS2_ot6*uQ:E)AsJ7+!DmU-7:2h-6sf[+X/*T
+r:b5/g;N'XV1^8#lO`)!X&Q)!VcZo!WE0"!VZTo!W<'"!VZQr!XB)>rW"&D'EA+D9:!S[7jo2n-6al^
D\`ik(DRVu(`*r&'+k]`r!O>M%M9?i(C^Tf.30NlX:kX8$NgA/!X&W.p&OmgquQTn#QXu0"pYD>"TnQ$
*<ZZT#QOi."pbS="HpQ"!!!'#'+"dK&.J[F#mUP,!!WH*!WrK*!W<!'!<<-#!!<50o`,!n!r`;l!;QU!
!<N?+"9S]"!$M@K%134R(CMO1^<![18kr`*C1^p\B5"npF)Q5CEcueVrd#K-G'.nLG'J=[I!g?jIt`]'
DKM7cUA#NJ)@HECrrM`lq>p3g!W`?'qZ%uF!!!*/%hT-K%1*"C;ja#(63dZ+(E=8,&fi'7,psf]+<;OK
,:"T6-5RsS,U4HT*ZZ4@+=Jfa(a;X+Bup>\%0le3!s8]/!VZTn!WN6#!VZQq!<E9$!rrDu!%@mJ"UY\C
!"&u3%9B!lLIr-i*$6:@&df6_@1sCg(_dSu)B'G/()7Jpr=Ai<'bM)p*[DR7*ChSl`rHAT#Qb#."9enr
!<3*!!WW8s!!iT-"9o):#R(8+!!`]<%1NLU!tGD<C6'P;!"B,;#Qt,-!WrQ-!<ri5o`,*q!<N?+r<3T4
"9JZ*%MAi2!!i]0q>^Krr;u6a#6=i,!s8Z-!VcX.!WrH'$OK%i_5i#h6;:cn?!UcQ$[HQ(CVOh/DK^&>
Fo6P(H$=FSFa&(VH@(!dI!pU"I<0"7A#&%#+:o%]!!*-%o)SRep&P'mq#CKt!s8W'!#R,;TS-/j#RqXc
%L`gd.30BLE[)hN,p=<?+XSQ`-R^>h,U4KV+<MXErYlLk,:F]S&JuL#Yt,*#$3L;/!X/]!!;HTk!<*!!
!r`9%!q?78."n:L<%JLm+<)%-%iQ].&J&:^'+Pcj&/?*%)&aA0(DRVtq%FDU)BK_-#S@e\X[NEq$O-_7
!sJer!!`N*!WiH+!Wi)s"p"f/"U>88qZ$s)!WWuE!!"j?8.#7qrs8T(!W`9$rW33*!sSu4oDeso!WrQ%
":>/0!"8i/EWuLJ"8W#t!WE/d!!!'!!r`9%!WE'S!WrE&"UkeH&./n>W5sci4[)SH>?,$EBOt^b@;Khs
DfBN7EGorEH?spbH?j^XGBeE3H4P@KH@:<gFGZE:BpZd_#7ge:rVus#!Ug$d!VQKn!WE'J!<N?'!!*<.
!!<3$15r,A,S(7u,8q.0*?,e0'bMB*E$$/@,Tn0R-n5-D$77#B+<M[H*?6";rYcCj+rhIT7Q2f-Sd,6&
#6Y#."p=c'q>g-grrDuu"9JW,!s/B$rrN*!,Qn/K!<<*SN2U;7&IfR'*>BA5)\`hm#7h;O%LrgZ&.T?k
)B8Yq!?)jT)#b?N().Gr()RVn-9Ee'?C:rs$jd+<!sShs!!<3%!<W6&!WiE(q#CR!!WrQ/!rN$3!<`E'
!!HEc%g)q7"pG)/!<`Q/rW!0)!<<3*"U"o"!;urr!Y#57!!!')!<Wfl!!N?'r;Zj!!;lla!!30&!r`9r
!WiB&!!*3,"pkYD"q2)7[]XOA4@)8%92SYi>[LfD@V91dDo-L4C3"93F*MtVH[L0dH$FRZH$Xa]G^+L[
I=HTgJVJDgGh=#L"p=i)rr_Zhr;lKi!!*-&"9\K#.kI!E80JHS%1Nj^'GM<!'b_<"',qs2*Zc1C+<Vs[
.k2tr-6jWS*?6%<)ZCTg)B0_@*?6F^/MKSs!<N9,!<<0+"S;]_!W<'"!WE*!!r;ls/-qT$8g=lZ%Ls*M
',_Ju&.AsW#7V/M%1EIQ%Lj'h)]Tn@+!)IDrYudp)AsA/()7T$&e>m++=0.L!!*--"98N/"7Z?t!<E6'
!s8Z.!Whro!W`?(r;[04%0-j=L&_8T!"8c+!!3-$qZ$j&"9er5"p>#,!WN6#!W)lr!W<!"!<WK(!"8u1
!XEfI"TSf0!!!'!!;urb!!**%r<!r>!W`9$!X8r@((_N85GuhP4\&7B92Sel<)rlt#$>5F@r$#$$#slt
E,KQ7G^4W7Hi\S?rcnisH$OXYG'J=\IXM-?#B5!!fbbb1!r`0%"U"i,n,W@eo`,$o!<W6'%gN(?%3L8%
:(S3\(_[]*)?(?b'G:rg'cIc)*,lr>(a'qE-S-eu.1%CK+s%^C)B'J2rYQ@f)]g+C*?HFN3A.N9%0-P3
!!3E0!V?Bg!WN5r!AOWW!<E0#!<N?+#QP/A,)3-q&fMf0'c7o-'+kcb$4$hC%L*:M?k!JI%1E[Y(`OJ;
r?2@f+<M[H*?5h5)&O/,(D@;i',<&CVuR2*#6=f+#6aPs#lt&.!WrQ.!s/Mq!#5P>#7LY:&-+))!!!E-
!!il>"p"c,qZ%*."pbM@"TeZ(!WrQ.!s8H&p&G-p!sJT'!<W</!">e+"TT#9!!!&]!&XcY!sAZ+!sAZ*
!sJo@"q;7dNp:j4-Vm8q6qpQZ;GU.h<``C,@;'.dDo?X6BQ%d+Ed)eSrd4Zkr-8p"GB\4SH$apbG^"CM
G%9GJ(^0d;!!N?*rW2KgrW2]m"p+c)!WrK/rW"DKDoPTR!$2gX$P=*h'+YZg',2&l()mo))f?Z8(EXbC
-S-eu.46Aa*?4tqq\U"b)]]k9*$HF]/[k]c!!<3$!XJu2quHKlpAt6n$ipA1!<<-&!!!$$!=&N'%Kg^l
;ZHe@(C(?]'bq;grX9JK#R1VG"q(iH$jm+G$k3gd)]^"Cr#m"%+<MXF)]BS1()7Ai$kX(!,Hq.P!!NB'
!sf&!!<3*"!r`9&!Whon!<NH(!!<<B^^U)?!s/T1!r)a,!sJl6"pG&.!!36*"9S]+!V??m!X&E%$j6P1
$EX:3!"K/4!!2orrW2Ee2us*a!W`E/"9AZ5"W%pm5LYic69@V076j@>;,C"^:fCG">[:fQ@r$##E,K?-
DJjK=G^+L[H$T72rHA]qH$X[WGC+1IC?-9E%/g2+"T8Aa!!iT*!!*3'!!*3V!"/u7-FRq9(_.8u%gNLU
&eGK\%1j3h'bhH'',VX))]BJ6+!E!_/1N%o,9ImD)?(KM(D@W'(D[r6*\T=\!!!6)!!!*,"Te,nqZ6Qo
"T\Z)!!*6%!"/l/$O-e_[r`c3&/QH.&I8gZ&Io-R#RUtL$OI1N"q(iG$OHqE$k3jf)]Tn@q]He!*Zc=A
)]0>)'+G9W'+cB;ZN't2"9JQ*#R'SrrrN'"rrMoq!W`9$rW*9)(^UY90)tt_o`4jh!<E<$":5)/!!*-'
!s/K(o)SdlrW!?3!!!7u!!N?2"98E&rW)s!rrDuumf4j=!X&T-"UG>;%2Kim&:rb;6S:,Q5t=C69iFtg
:f(%i=^><>@qfIhDo-H!DJ*m)DK9rGGQ)jaG5um`G7&J5FE_VGCZ-*@%K-8-"9\N%lMrgD!WrK)!sA]+
"Ukh?!,0;+*sMoT&/#H]&/5ci%Lip]'c7]#(E*r()Jg<1'cnG>-7gYr-6ra<*ZQ%7)#>'J((h5o(EX\S
1q*Gb#Qau+!sf&2jT%1>!W`9&!s/H+$k31:BuMnP#RCbL'FtWa'G:l`#mgtK%h&dR%L*:L?4.)C$k*RY
)&jM7*?P,#rZ;(['cRu)'+kTX$4mds/$T'S#m:;0":#%r!;llo!"T)3!WrK("on])!Sm_U$j?J.!s/Q,
!qlU"!<N<)!W`9%!WE0#!V-3q!<E0#!=/Z*#m?Xr!<<K1!!!'!!;HT`!&=TX"9f#:$P!I]&1#Sg1H?p<
4A&%,7o3/c<E)mq<**7/?!_#S@r#u!Df'-)D/F<;GPlXaFoHR]G7A_=F`VPCF`2S@h%^G.r;Zj$"8`,c
!!NB)!sA`/rWG+_!"Ao>[sSl*"9f8R&df*_()@Ss&J,Ng(E"#((E4#))Jg<0'cnD=-7^Pn,pFEO)]9J/
(Dcrc'G_Dt'G:ul*$@0rZ2ak0!rr<'#R1)*rrN*!mJo0H!<<-%!sAT5!"l_h()I/[&0)>j%MTWm&e>EZ
$OdLV%13LS#7M&K$jm+H$k3jf)B'P6*$$(!*rI#n*#KD'&.8^K%hpTHXT/>-"p4i.#6X8lp](a(!WrN-
"TSr2!7aaW$N1#(!!EE3#Qt5&!;6Hc!<3)s!"&`4!!!%["98E/"8`)s!WN6#!Ug!g!WE-S"ptJ5!"qE)
BKJOB2).0a76sIA<*!!t;GpFn=Bf!7@:s%aDS^7.B5VR'Ed)_NFo6@\Fnp1gF`VPCF`2P<gCju(r;cj"
q>p9i!!2rs#lt)0"9er2!WrT)!!NBNThHCI.hi?n$Pa0X%29Nl'G:uh&el-"(DRc,'H%g+)As50*?QRW
.4-8^*ZQ(8(]"m]'bhAt',)-&+?)!Z!!!9,!<<3-"oA;u!Vufo!VHEm!WE'1!@X[:*?c1-"Uu7Z#n7O^
'-7\p$jm@N%M'!U%1idS%U]_R"UtnN',_]+)&aD4*<$uV*#0D1'b_/f$4@F\/h*n&!"&o5!!EN/k5Ybg
!!!$$!!!*)qu?eb!!r<!"9\r5!Wi)srW)`pnGrRiqZ$X!$N:#/Mu`nY#m0u(r;lm!rrMHd$N^J>!"pc9
Z:$2b/H.U85=S(08l/Gd<)W]m&5uS2=BT!C@;0SoDJa$(D/BDrGB\1Or,_jZqK33iG'%eIGA_S7fFSAs
r;cj!rrN-$qZ6NnqZ/q^!!*0)"U,#2!WiN*";u3I-OKhW%13:I&.AjS&JGfj&J,Ne'GhW(()\,-)B3N4
)AO85*[E0^,U"3K)Aj8+!#GAF&f)5t'cA/<2(u-5!!`W-!!<H/qZ-WtrW2lr!W`?(rW2Wk.fpQ-ROARE
#S7FO%1s$U$kO!^%L`[N$4@:Q$jmFT#n@JS%L`OO%1X$h)?(HV)&aG5*$"qs"rnU%)&<r#&.]3\'c/DL
WrN,+#6b)1"p3ugr;dE2"98E&"onZ(#\seJ!X8i)!<*'#!qcQn!WN6"!U'La":P2/!/UUS!=8i*!;lls
!ri;u!;cfp!&joY!!Wl?!!"<D]i-"">;\H$4?u;(85)iX;c?Rk:f("f<E3++A70(e^i!t#DJa93GBS(L
EcM)!rcA!Z%s<#<GBJ"NH#7P:cjL6`!r`0%!Wi?&rW<'#rW2lr!!3'#r;dZ8!sJo4!=92?!!!`tUc&2S
1C=Np#RUJ<!t>eR')iIa&ebur)&O,-*Yo\7DB'Q0*?6(E-RBrY*#]\2()@Y_'`JgR(Dmr**$c[]2Q6TT
"UG21!XAl*!<*'"!W2rt!W3#o!!!3%!"T`,Uc/8V2@U0($OdIQ$P!(F!=TA8$5j3[%L`[R&IK$[@LinQ
%h9'_)&O/*()If*q\g7i)]BS1()7Gn',_T80VnaL!Xf24!sShj!!**%"9S`/"9\Q%!tF5i"8;cs!<N;q
!<*#s!r`5d!"Ar/!!Nc2!![`Q!!!9+qu?]tr;ls$rW<*#quHQo%0-A/!WrE&$5XKd%XZ;2-pK170KLdF
6:4+19MSA\;Gp@hr_O;+;H$S"@pWe`^MRe!DJa93GBS(Krc%jVr,NBjF*)PJGBS+RHYdJ=`s<1U"o\K,
!Wi?&!WiB'rW<*#qZ$Zu!Wr?%)$0jA"9o,6!"0JP!!$Z:$m#TX"UkA5$OR.>$iUV[%hK<b&ebro(E"&+
)BK\7*H)o:'ce87+snQX*?#b2()@Ya'GqJs'GM8t(`=20+=86_5G.uW!"/o0!X8c(!!!-#!WW8u!!!&t
!WW8t!#,GA#ljs:YRDTZ$4%.B#7_1M$k<dH%0$_7$5j3[%1<LQ&do6_@h9+U%h9*`(`4#''GVB"q\fAO
!#bbP&/5cn*#Kq^S,`Tj%gN(9"Tdif!W`?)qZIQ4"one"!!3H2(C'p?"Tnc,!s/Mt!<*#u!riB%!ri;e
!"Ar/!!Wi3!"N`P!!!6)qu?]tq#^Kqp])K>"9o)7":,;="p=pF^Gn5'/MT1F2*=5n6qC$J:f1+g;,R<h
'N%b,<Eis>B5>8"ChIX&DKC#FF)_2!rbqaSrG`BhF*)PKG'8.XD/4C.&Ie^DrVus$!rE#u"9/H&!VQL!
!X/f7#6bA>"9&9&?)Sb^rWb%_$3CG?#m^nK%h9*\&.oNg'GVH&(`+)4(E=H6*?,_6*$$4M,Tn'E(`*r&
'GUKZ%29Nl()Rr.)^-US/4Gj'!!N]3!!3?,qZ-WurrW3$p&G0q!WrN"!"rG2*#](h$4RFK$4[IO$kEgW
%/pVN$47.K$k3RO%MB-\&Ru@^#S.CT',VN#rY,AJ(AesJ)$h&q()@St(*".m,<q=i!!Nf9!!3<*k5YVd
!WrT0qu?_fr;[3,%L)n5!s/K)"9S]!!<3)u!riB%!ri;e!"8l.!!N`1!XW<@!!!3$!!3-#!Vlcs!W<'"
!Vud?!sf;E#mLqX#m_/V[n%i%0fM!K3Bf\q6q'[A:Jand;Gg<j:_ci+;cR(4?Y=/hDJWs(DJjN>G&qYA
qelCO"`SF#EcZ@%FpWJBDejg,)[cWJrW!$'!s&H$!!<?+!s8E%p])37#R_%F!t,\@!!6)l/I2ps%grXK
$4@4K#n-_B+qG1q&J>`k'c7f*(E4G4*$&r<)\jA5*?lgU+<;=:()7Pur=]t]'GVB!(`F;3+XeWg9T0&R
!!r],!<rZ'!<*'#!rW0!!;ca$!X/f5!!!$(rW!7!RjnUS%1isV$iUV@%1E[V%LijUq[45L%1<LQ&do6`
@h9+U%h9'_(Ddf#',2/sr"fk\(`=2-()7Mr&JZ6%,"%(`!!N`6!!3?+lMpncr;Zfu%06S:!!WE'`;fl@
!"925":"u.!!*-'!s//srW2cqrrMHd%06J0!!ET/"pJ-3"98Q&!!30$!VZZp!rrAu!"T8E&J,6K!"T/>
<m36K0.@G]0/P[N5!VG&7S6BN:f1+gr)"5-<)cn'A7'"d^i""%Df0K7G]n.JDf5Dg'5h]+E,fo>F`hkR
I;s+VWuDQL!r`0%"U"l-r;Zp&"9S`'!Vl^1"UtnJ!<<*#!!#9k'FbKS!X/i;$4Hh?!=K;9%fHn[&.fEe
'GVH&(`+,5(E=H6*?,b8*??=N,Tn*G(`!i#r"Bk\'c%Q$(`F;4+t+fl;MP>U!!`N)!<r](!!<?+!s8B$
q#CL"$4-k4!"(`h%gi[I!X8r?%K6hC%1NdX%h9$W%/^JM$k3UQ%MB-\&n;I_#S.@S&f2;t'+trm(&SgX
(Ddo*()7Ms&J,Wo(a;M"rW!*-!rrB,!pTah!W`9'"9\T&!s-XH!r`0."pP,2!s&B%!<N?)!VcZo!Vuls
!WW8i!"]/2!!**#!!<H,!tR[-!<<3"!<*#q!WiB("9&E'!r;m>#Se'e%13@_1`j8%2EaGa/13,54[)(s
6q9jD:/Fec;Z0H.;H$Rq=']?EBPbJ%D.dd)Dfg5IF)c'uD/B,c'PqT&DJsK6EccGJH[TsQN27@(!!3'!
!XAo2qu@!+"9S]+!<N<'q#D*6&Io'I!!!?H"J7:_)]oLk!!<W<rX&`8$k3^F%iu8n&J>cm(`=/,)BTb8
*H)r;(*4J;,:=c\*?#b1(&ejL&ebom'bqK#(Dn&0*?lp]0O021"oni-!!*9,qZ$a%"9S]+rW3'#q#CL#
%LN=:!"9M@QmWL_*=N#M":bq@%1*LT&.f?_%LigTr<jGO%1EUS&do6_@h9+T%h/s\()@St&ebomr"T2I
rYGkV'+tlf%h]Zq+UV"i!!*'(!<<0*"8)Wq!<E8t!!!-#"V:b;"UG).ScAuq!"B27!<N<#!!!'!!WW8r
!;urn!ri;k!;lj+!WW3&"T\T@.N&3d!WE*!!WN3!!rW-'!WrQ/"U"T$+9W8_)\No=,o,'E3'/WO2)6gA
3]oSk6:FF;9MSA\;H!Hj),aC5<``U=?taAlDJa'+Df9`BG&qV?ChmebBcCf%CMRa'DK'T:Fa&4^FDID:
'G:BH!!!$*"p4]&"9er3!Wi6#q#D$.$NLV:!#5e?\4%,J"VM7M!X8Q1!t,JF%K6k:%j)>o&J>`l(E"&+
)BTb8*cN,>(*4J;,:=c\*?#b1'GLHY)&!Yt()Ic()&aG8,:Y/rD0l6f!!WE'!<iW'!!i]1!s/K(!WiE!
!#Yb:#lk52!"8i-YWWL/!>#VD!X9#A%1WmZr=BqZ%h9$W$k!FO%1N^R%MB-\&n;I_#7_1P&Jc)prY#5E
r"KYV()@]$&ePZb%MBQo*aWa`!!NN,!!3?,p&P*nrrW&t$N^G2!<<?9"TSN*^AIs5#7(G6qZ$a"!<N9&
p]16np]CHrnc8Rg$3C80!!39)!YcgoqZ-TrquZft"p+l0"U5)1rW!`;"U>#@%O*i]]$JKq.R#pN2)mQU
3&iu+5=%Y*7nH?J:Jgpc3)W[T<`i[>?taAlDf06-DfBfCGB7_?CMIQsB4kmkBkhF"D/XE8Fa/=aF_RqA
&.nmD!!!',#6Xl(!sSo3!rW/s!#Ye?#65,4&0YSQXJC=J()%#_%1EUN#71bHrXJf9rsp.^&.oNg'c.`)
(E+A3*?K/?*#9V;*[<$Y+WVI;()6ZZ(_[W"(Dmu-)]TqG.P!*#F8uLF#6=f)"U"W%!sJf0!rN)s!"f88
"ono/$QEB7URZQ/&.SmMrX/i8#RV"Oq@Ec?%h9$WrX/i;%1EUS&eYQ`&n;I_#7_1P&JZ#o&eP]gq\'JS
'c%Q!&eGQ_%1s?l)K'-c!!NN,!!3?,p&G'nrW3'#r;[Q8#7(;0#6Or+:lM^p"98T,!WWB0"8`)t!VHHl
!WE0""8r9$!<</l!;urt!XJf,!<WB,&02>Z!<*#s!rW-M!WrQ0"pG,1!!39(!!!0QL!ZkY4taNK0eb@@
4$5Sb2`a,g6q0[;8k_uVr_X5':f1+i<`W=/ART:h^i++(rbr3eH$==KD/3iuAnE#pAnPaiBkqO&E-$2J
IXlTU\;^h,!!<3$!t#;9qu?g'"U"r+!W)is!W<!4)fN*@&/52.-j0YW$4dUT#mLYB%/gY=%1WjY&,m+g
&J>co)&F)-*u>q=E#ou8+!)LL-m^#W)Aa,%&eP]g&ebuq(`=20*"a26,qCQ"Mf/S"!!`N)!!EB)qu?g&
"9S`'!W2ot!rW*5(i$7,#Rg]j+TMKC"q1nJ#R:YF&,m1<&-<@O%/pVJ$k3RP%MB-]&nDO`#7_1O&/>ll
r=So>%hfWl'b_/i%LijY'c.d6?iC$/"T\T)"pFZ#$3://!s8T*!!!')qu@3]\L%^b!'CSg!!36&!sJN%
rW2TjrW3$#qucp"rW2Zlr;liurW*3)!Wa2O$N^/*rW2s!!!<'!/-?"Z#6kA8!WiH+#R<02Jj1hM5<Q5B
4t\WN5<_.h3''5h77Kd<8P;cR;,R<h3Di[R<``C1AmoCj_/F4*EH#l>H$==KChdWqARo=_AS,RgC2@d,
Ecu_WJ9YkGKa/+g"98E)$O?k4!!EK0"9JW%!;ca7"99aZBH@Bk%h!q(%KHV<&.]0T"pYJE%hB0L%06qL
r=Bn[&el)u(D[o2(EFQ9*ZPt<*ZlXU,p=9I(DRV^&K28q'c.]))B0Y;+=/Nj0U?AP"TSf/!!!-(!W2p"
"U"o/qZ6Qo"9ecM[q$3k!=K/8Gn:5]!!Nf@$4$hA$kEs`&c3+@%h9$I$Q'9]$OR@V$P="^&Io$U$k*[]
'G:uh&.oNO&e5Qh'G:re%1EXV'Gqa?=8i1'"T\T)"pFZ#)Z]s@!s8Z.!<<0)!<<*$Z2kI9!!EZG#64`+
!s&H(qZ$[!!<MclrW3$#qucp"r;lTlr;d$&!WrN+r;d!#/-Z=X!WE)t!W<'"!W<!E!X&]5#6kA<"UG)S
45<t!8O>Bf3k@dF0K2$W5<_.i4?l/$7RmYR8P;cR;,R9g%8p/+='/d?@;0SpDf0:gE$odRGB7\<BkM!f
@q0%[AS,RhCMe$2G'SOcH>UcH$jlt<!!!-0#Qsu)!sJf/!Vl^7!WW9%*A5K#)C64,!!S)i$igJ=&.]3W
#RLkJrXSo:!=fY=&-3@U2\[#E(D[o1(EFQ:*ZZ%=*ZlXU,p=9H().An&.oKe',;<#)&aG6*Zu^V0J]5&
!!*'*!WW3&!rDs""9S]+rW)ou,6.`H!<`BD0$-<o+;+_U!.P@\!!*94$k!@H#n.=V&J,Ka&,m+A%h/sH
$OI4N$OR@V$P=%`$5!dS%L`aX'bh8mrX])B')`CQ&eYik&eGN^$k*XZ)BF`,rW!*+!WW9+"82]r!<NB&
":58;!rr<&&tf4.qu?^<rW!$%!s/N#!!*-%nc8XirrW*#rW<$!rrDipquI3-!WrN+!<E0$!(6eirW2uu
r;liu!!3#u.KKVU#mLM<$k!RX2mu+K*\TZ:1/YbK68Uee5<hCs4[)/!77Kd;8P;cRqbR`"<*!(&?=dPZ
D8L70B`;rVG'\@QDJEisAGfp<A7Z!YBPVI(F*;m/HjjuAA.SqF"p"],$3p\2!!36(!W2p@!<<*%#6Y58
.ASLK!!a&?!#gUu%06eD%M'$X$471N%M&FH!=fY<&/l/p()Ri')''M6+)rAC(EOV>,Uar]*#KD(')iFP
&J5Zk(Dn#.)]Tk?+XJiE25WtE!!NT/!!!'%qZ$["!Wi6"+9;NE!!<K2#RDrW/2$u*$NU5@J,olT":#8B
$jm:K%1iFL!=o\=%j)8j$O[:L$k3RO%MB-^'P7sg#S%:Q&JYum&.]9_&JG'T!>#kB&do9_%h9$X%M0X(
P;rOA"9nr.!X/Q+o`,L'!sJf0$4[:@%0GVm!sJ`)!!*WRrVus"!r`5u!<3)i!<3*"!rN0"!rW/k!"]/4
!sA`/!<<*$!+,^/!WiE%!;QWq!W2pH!s]/:!<WZ8,8e0k3(,AL>pqm6[l[)?5<_:s5sR\$6:4.07Rp$C
9i(ab*D]I-;H-[u=C,NGBl:e,DJ4!-E-?POEc#N'ARo<L@MrZdAnYprE-$5LH[:*[gK"Ud!<rQ)":5;8
qu?a!!W2p"!<N6$)?9sD(^[6$)^>Ug/H?"mIfp>e$k*UU%h/pUq$d?7&,Ztl&ec#t()7]-(*+K;*uu+<
*ZlXU,p4-C'G:uh%hK9a&el)u)&aG6*?H:G0fH:!rW!B4!<<*$!<<*#!<<*$!W2ou!X/K&#mLMN%'MZ3
+pJ#\-ia5ZGQ8*O"pYGB$k*LP%1WmZr!ii?%LigSrX'SQ$k!CO&e#BfB+kg^%LijZ()7Gn%M'*_&eP`T
&.T9b&ePZc%LrpW%j*$g/H,VQ#6Or-"U"Dt'ESCA"9JZ1!>PU4"9nr.!!iW+%NYHI!!30&!W<#t!V$0i
!WE0!"9/H%!W<#o!W2p#!<WH."9&9*!W[KG!s/N)r;Zj!!;cfp!$).I$NpG1#6YTKV`Qpk9NXnS3D6V=
9Kkd-5<qM$r^-fV6q'R8"\D?\:/Fdd:HD<M<*!(&?"@>WDSg@1BQ%g.G'\@QD.mNl@q&nU@:E_WAS5ap
E-$5LH[1'\i^s:[!sJ]*!sf)5!VQKo!<`<$)[-3D:lQG2#9kW7%0.#c";M4Q%1NdX%h9'Y%K-\;%1NdX
r"&lA',VK$()7Z+(*+K;*uu+;*?QOU,p4*A'+kfT%g`dY&el)u)&aG6rZ)7c1,l`u!!*''rW!!#!<Dut
qZ$X!"o\K<"98U)Os(_K+X[p.!"*ZF%KZn@#RUqJrXJi:r=/`9&.K!S#mgqH$k!CO&e#EgBG;-l#nIIS
&f)2p%h9'\&J>Zf&.]<`rXfJK%hB-[%1XO.W$2-?"U>/1!X&W&!!!&t!#,J<#6Y#,!W`Z/7K<i*!XTDD
!=]qE!!NE+!W`9$rW2KgrrN*#rWE-$rW2uurrMrsqu?j#!sJi1rW!0*!0mNd!<WE#!;cfq!!E<*#n$n8
!#GqO\TKJf1dal+8NT\Q4A7q+5X7V%6UUf?#Xq3R8P;`P:Jh$d)c0F3<`W:-A70+h_f9R,Df9T<HZsIG
B4YR^@f9^:@UiscB52:&F*DtXG_'ql4pMK!"98E(#R1A3p&G*p"8r3;!W\oo#Sm^^)%mJ\'6jTo#S%:R
%M''[%Lr=E!t>\L&,Ztj&JGlq().T*'c\<:*ul%:*?QOU,p+!=&ePWb%M'']&el)u)&aG6*??+>1H,KE
-3+,J"8`&u!W<)s!!30("oSE;!Wo6'%N5]i((LZO$ZH(T!=/o9$4@7Nq[NQ6r=(+_$OR1H$4@7L#n7LU
',G<t&.&jV%MKWn&e>E]%hTEe&J,H`&.fHQ&-rdW&.T0q.&@aZ!!NQ/!!39*qZ$Tsqu@E3"9el-!WiH(
OUqQp#6>&<"p#2NquH]u!!<'!n,WFgrrW0%rW<*#r;ccsrrW0#qu?j#!sJl2rW!0+!42_-!!<<!!;llr
!!EB.#n$n8!#-(jd6ou]4?#Ag9fu:\5"e(,5s[j:6iKIY77Kd<8P;`Pr(e8.;H-[t=']?DBPtb.D.dd*
E-?SPEGK/s@U`dE?lEH`A7fRnE-$8OH[13beM@[E"TeZ(!XAl2!VZQq!<NB%!!3Q@Zk"/e'b(?P$53CS
H3=ld%Lr@I":bkM$k*%C!t>_M&,ZtW&JGlq'bhH('cS69*ubq8*?QRV,p!p;&J,KP%M]Kc&JGos)&aG6
*??(<1H;KV!!E<'qZ$Tsr;uls!s&H+"T8<0$l$9!'cISe"U,>8%<;XQ$igM;#n$Y>oaE#P$4-tE#n%.K
#n7LT&f5=!&.&jW%MKZp&e>E]%hTEe&J4pPq@F2M%hC!:T+1i$!<iN)!X&T+quH`tqu@B2!W`9'!X\ql
!!*B0!<WK,!=p+I!!!*""9JZ,!r`5i!<*#u!WW?%!r`6!!<*#t!ri;u!!<<-#6b#+#6b+P!!3-&"82`n
!<iN-"pbM<rW"/S.*+8,5<h7n5t""<[Q[>J6UF.-6pj=06q'O67n?3E9MSC^:HMBN<*!%$?"@;TDT$L2
AT2R,G'eFPC1Uj`@:3JM?XR;OA7fOmE-$8OI=-BdcR0G<"p"](!X8f1!Wi)sr;llt+oqr`V[3\>$j[(C
#Qtri";;"L%M'*^%LijU$k!FO$k3[Wq[`rD',;;u'Gi8>'H8-8*ubn8*?QRV,p!m9&.]6\%1WjY&JGlq
)&aG5*$$"?.m0^A#R1>+!!**%rWE*!"9AQ*!sAK%!XKUFrXoeR#Qt52!"X)M$NLA9#mq%J$MY#.$l'-W
#m^eC$4I7J%2''^(Macu#S@RX%MT`q&e>B[%hTEe&J#?]rX\r=&J5Wg'Hf)t"98K)!s&B'"9S]&!!*-%
p])98!WrG@!!!*)"9S]*!X9\G!<<-&"U,#3!s/N)mf<=frW3'%rW<*#quH]sr<!!"qZ$^#"pY;1!!if0
f)PmQ!X&Pu!$;4B!WiH,"pYD:!<EH6/[7&p4$Z/"5rqM;[m!JL6UL`>$U[<M77Ka:84cHJ:Adm):f:7o
='/a=?Y=2lDf'*)DfKrIG&M))@K'[5?O'tI@qB@kE,uA2I=HcgHcmEI%gW(6"9AZ0!s8H&qu?d"!Wi9#
'`eIG";m+"$3^bF#mLA8)0uAt"q;(A&.K*Y$k*LO$k*RS%M'*_r=BhY',;8t'Gh]&)BNl>)\a;5+!i?]
*>]:u%fHhN%M'*a'c.`+)]Kb;*?cXlUB_23!r;ls!rW6#!!!&t!Z:t<!XAfHPRJ35%1NOD!!*XO!"&]0
#7:hHr<i9,!=B/4#TX3Y$OR1L&e#BgC)%<e&J#Bd)&<hp$k3^Z'+tier=05H%hK9a&el#t)E!l^rWEE-
!<<0'!s/?#!rrB(!VZR,"9;6u!rrB-!rr<(!$VCF!!<B'"U"r1!WiDj!<3)r!ri<!!<3)t!ri;u!!<<-
#6b#+#RLO_!!E9'"Te>t#lt&.!WrQ/#6tAH!<<?519`N"5!_J"5WVG<\3NbQ6ppoA$UdEP7Rfm=8P2WL
:&[m+:JXeb<EE7(?=[GWC;"@rDej61GC"CLB4>9J?QWT\?!^lG@V'7jE--ASJ:M`bfFel.#6=f)!X/`0
!Wi,t!WiB'rW!9+"UbJRMZF1k$47+E"98`GHNXue%1`@K!Y5_Lr!Wc=%Ls!\&J>!R(_IDq()7N")\j;2
D&=*2)&s_E.3ooL&.\[K((:W]%M06f(E",1)]Tk<+<rnM!!`Z/q>^Krr<*$!!!3$"(BFL9!<rWJOp_p4
%134<!!*[P!"/c2#6G5?$iUM,$NUS@rWjMN$4@1J%MK9b'P7pf'+GH`'c@c!%LW[U&JGcg&,cqQ%M'*_
&JGlo)&k<-!!*0*"9JT*!s8T%!!33'!VcWs!<r[$r;[30!rr<(!$_IG!!<B'"U"r1!WiE%!:g-h!W)rt
!W)ls!W<'"!Vucu!sJo4rW!3/!6kKF!!3<*p&P'm.foeV"pY51!!E`e[5LB>69[Ru4@iVd5u0d86q'O6
7R]d97n6*@8P2WL:&[lh:JXh';cQn$>$kfKBP4bbB6S$+EHc\MD.[2S?63BW>[:ZC@:X%gE--ASJ:M`_
i!Kr&#6Fl*!X/]/!Vl`q!W2p3!sf)PO9?%%$3gV8!!jHi"V_1O%fR"A%h9$XrX8r>%1WmZ&Gm%H',22s
'Gh]')]3,o'GVr1*$?OU,9.F/q@"#H&/#]o)&aG5*$$"@+uZn1!!35u!!!&u"8r5u!WW9#!!rc2+I3HO
&I\jErW!<<ErZRJ"pYJB$O[=8$N^YB$2t22#n$Y>&.T?`'G=a^$lfTa&Jc3!&Ifok$k<j_&eGN^$k*RS
%M03b'G_H%*A=Vs!!3<-"9JZ.!s/<"!WrK)p](Bs$3t)>!##J9!!!-%+ohZE!WrQ/"9\f.!Wh`irW2lt
rW2lrrW3$#rrN&urW!$%"U5).!!i`.[K$=.!X/Yt!$qXH!sAf5!WW3(#qa"Q7n#d/5!V5%>.[-u6:XI6
7Ros<7n6*@r^eD.91qrQ:/4S];,^Is=^,6E@V]>PC1hL$DK0iEF)5Do?!LW?>lIq9?!h#NBPh^1H@LHt
E".BD%h&^J"9AK)"U"l-nc0@+#m(s8"qhFS"p4r-#TA'o'aP9ZrX]&?rXSo:":bnP%hSUM(D7Aq'bqE!
)]'M+>T":u)''hG-mKZF%K6_K$k!FO%1a'c(E",1)]Tk<+WWqGp](?q!!3$#r;cft!<N<$!!i]-)5@ZY
'+G-D!!j0X!"8i3#71b9$iCG3$iUJV#mgkD#mq(K$kF!_(CF1U%M]Hb&f)<!&I]!S%M9?e&.\XI$OmRW
&JGio(EFAWTDefq":#)4!sA],qu?a"!rDs+!<<*#!XJdr!!3-#!r`0)"TT_H!<<-%rWE?+!WiB'mf<=f
qZ?`tq>gEoq#CKu"9eo,!!ic2K`D/S!<iSr!!NE+"U5#.(B=UC,gJDA7RK@'5s7eD]L5Xb84H'=8,Z!X
8cD=(91qrQ9hnJ\;H-\!>$PHHA8GJBDeWg%E,g#EEb])ir*0/()I-TV@q]^uFF&FeKkum['ak0J"Te],
"p=u.nc0"!$31U;#o+$]#6YP?!!jKk"r.FT%hK<b&.]<L%f[(>&H!+B&eYilrY6(_)AjM(:EC>f*ZlLN
-R'HB$jm@>$P*XV&JQ$!)B0Y9*?6:A;N(JR!!2rs!<E9$"8i/t!WE')"99":&/u;m"oSE+&Te!^!!``8
!"/]5rX8c9rXAf7rX/Q0*=</_$k3a]&K(dF(_@)h&ec#t'bCc[$Om[]&e>HM$O[@Q&.oQi(De20:l,)N
!Wr]4rWE6(!W2ou!s8B#$3:2/!!33+!7UuRqZ$[%!$_@A!!3'$rrW0#r;cEhrW2ltrW2corrMlp!s&K,
!r`0*#RsT7"98E*"7cF2!<NE/!<<*%$QI;O91D<85smh.?G&^*77g!>rCHr[r(?r]#>@fc:/=_b<#8V=
>?tZKA8#S5EG0!&E,g#DEG8ic=]t`-r`L.D?!h&RCiFNCIt35iQE(Z+#R(>4!<WN0!Whil(]t$I#HA4M
&Io-Q"onoKHj1>m%hB3`&J4mO!"Su=rt,2Bq[roC'`JgO(`F2/(-<Z_(D\#5+XJKZ)%m;`#mq%I$4@7P
&JQ$!)B0Y9*?-1@<e'fC!<E9$"8W#t!WE'*!W`M-&f_Pp#6Xr*#S_=[%KQe>#n$Y>!"Af8rs\o8rX/Q0
%13IO$k3a^&eu$;)\<JX'*T-g'G(WX*"!,d'+k`a$OR4K$OmX['GVH%+;e./!!!$&#6t/1!WrK)r;Zj#
!rW*$!<N?(rW!'+!8.>WqZ$[&!@%IB"9AT,!Wr<$n,WCfqZ?`tmf3Lk!!*-'!r`0*#SAKm!rr<)"TAGo
!"8o3"T\T'!>,sb5>4KE70l@J9O>G&<(9LZ8H)3\9))%!9MJ8Y;,^Ir>$PBCARo=kG]IJ3D/XE9F`;#%
=oMP'=oMM4>$PEDB5DR1H[pX"E1.3,&./dL!W`<)"pG&/nc0@+"Ub=-&K22k%LNIA$6=O"(CCZ`rXf,A
q[`Z;rXo&@(D@Gr'GVB#)Aa,3-Qs9C*$6=M-6O-;$N:A1$4dLS&JPut)B0Y9*ZH7C>&s?;"TSQ)!WrPs
!#,Y<W"pBc%grRC!!*dU!"K#7#71b:$O@.M%1WgV$k*OC$N:A2$60E^%1Ws`&J6$.*"WYo',23!'FtQW
$4RO[&J#<K$5X'Z&/#Zm)&OJ9>BBiF"U5,6"9\l2!Wi6""9S]+!!!-%!<WH+rW!'-!7UuRqZ$['![IUC
rW<'"mK!1dqZ?`tli@"drW!60'+5*J!!!0*!r`5n!!rZ."9AK&!tGaZ%RNlV7S--A6rI%'8QA5Qr^m)]
"%u9\:&[ib9+FWi:/Fhf<`iO1?XdPWB)Z["C27X(EHH;?B4"bA='&L+='&L,>[ClPCiOTEJU`;oVLfKj
%L2t6!<`T1!s.rm%g3+D!2UGN%M9<`$3LhQK*2Js$4maI&c!":&cE@@'/(%6'c%T'(`+88*Z5k9+!N!W
+;bXr#RC_D$4.%I%1j0g(`F>5*?H+A+D+UR!!E#s!!3$"oDf!s!2^VTrXTAC"98Z6H2nEU#7(\8$NLS8
%K6h@%1N^R$4?b=rX&f:$OdIT&cNFt)]BS-&eYim(Dmhs$O6tI&/,Wd$jm:I$474R&el-#(EXf7=o\O/
#6P&2"U,#1!W<!"!s/N&!!<9*"TnZ'":,"c!!W6"!XSrRquH`urrM`lq>gEoquZftli7(f!Wi9#!X0&7
rW!'%"9\f.rW2Zl!<WK(!"oDB#fT5,5Y"OA8k2uVb"Gc*9`@Z`9,:2q9hnGX9h\5R92&&U:f:7n=B]!<
@KC"Prb4!"Ci!m)EHH;?AmJJ<<E<1&<`W:)>[ClPCiFNDJUN,pZXk!`&-`+7!<`T1!s.rm'EnaH!2^YT
%2'Hh$jIIRL^P"+&.ndPrXer=r=\u@%ho]m()If*)AsA1*#fh<+p]J@*u>Fn#6tP5#ndRS&/,fr)B0Y:
*uQ1IF#a4#"o/,u!W<)m!#5P9!2^_X%1j-["TSu3If^)\#7(YDrX/`8%K6hB%1N^R$47(GrX/W4)%6uc
&J>cn'bhAt'G;)q(`3qt$O6tI&/,ZX%h&gE#o<pX&/#]p)]'SDG<Z65$jQh8"9er3!s/?#!WrK)rW!$%
"U5).!!EN,li7.b!!3K0,Q%Q@!UKg`!W<)u!UKgd!<<0"!!3<4!WE'%!X&W."8r8o!!*0)rW!W7$jt0K
:d.BG9h\,^9[$44852`MrCd5d:B"&h:B+&f9H?i';,^Ir=Bf'=@Us+cBP2'rChmp.FEDD4>ujs*rDjV6
=B\s:@V9LrFF&IbJ:"q.)[m5\#64`)!sJf/!V-4/":#,2WuW8i&fD>l#8[]'$lB<_&.oNf&J,NP&c<::
',M>t()If*)Aj5-*#fh=+seQY(CpcU#7(56'+#!T&/,cq)B0Y;+;l:NI4,*r"Si&r!<<2s!!!&u!#,G6
WuiGk%hoHW!"ApX!Y,28#71b:$OR:O%1WjW$k*LN$N:A2$6BQ_$k3^Y&el)q&el)q&el-")AWnn#RV"Q
'+tfb$iLDJ%1j-e(`X;5.tKA]":PJ8!WrT0"9S]'!!*0'r;Zp$"9el+!!ET.n,NUh!!<6.![@OBrW2?c
q>pTtr;l6br;llt!XoeLrVup#rWE3&r;lWm!W`B+rW!3)%1pl\;*@HJ&Pl+n>>NI<=\;F_9heAW9hnL`
:]aEg:Amm+:/Fed<EE=-?!q,PB5)$lC2@^%DK9iADJ!3Ur`(%@<``@*>?tWHBP_U-H%:6kID\Pq$4I%;
!!*0)!s/Mo!#,J="oteL+:/Z"'FkBb$],9/$5!jK')W@>'(utF'GVB"(`=5/(E*2k#9P0;-6O-9#lY#D
#6tM@$4RLY'c.c-*$-7A+YJHh"98Mu!;urp!<3)u!#,J7Y9P1r%i#NX!"AsX!=f)7#71_9$3:MCrXAi9
!t5PE$N1;0$9/D$%1a!^',;/n'GV;q'c7l0(_R8a$P!a^&eGN]$OR4K%1j-e(`X;5/rCqb":>84!<WH.
"9JW&!!*-%r;Zp#!sA])!"B;9mf3Lk!s8Q(!=/]LquH`tm/[.doE":Y!s&H)!WE'#'.+7h!!E?*"9S`)
!W2ot!W2p!!<WN(!##n]b?@Y+7o`D]93b?>:g-Lg:/:a`#Z+>p;Gg:f:J^sb%o6#"<)m"&>?tWGA7fLg
BdRS1CM[p0F`hV7?<:**<E3($=B\s:@:X%fDK0oNH$t7b3ZeS6"9&9&!WrN+quQHj'*JRBW@](t&KDMr
#T*u,$lB?a&cE@B&cE@>'DrRD',)&o()If*)&O2.)]Kb=,:=i^(_@Mi"pG/7#6tPB%1a'c(E",2+!V^K
1lW+Qli7(f!Wr<#'*A66/fb9.(CgWL%0:nY%0-S:#lP&1$4He@rsSi6r!E</"Ub_K%hTHQ'E/[X()e/5
)AE\h$P!a^&eGN^$k!^V$OmX['c7o**]0#u'*8FA!!*3$"9AQ)r;Zj"!W2p!!WrK&!"BDAjo>Sc"U>/1
!=&TIquH`tl2^MYli7"drW3'#rVup/!C@7p!!NB*"9S]+q>gNrr;Zm""9n`()%dq0BM(W`<`2ag?;o0I
>>.mi:f("c:f1-i;Zfop:f.-e%o?,$<)m"&>?tTFA7fLhCAquSCi=?:F`1o!=8l/=<E<1(>?tWHASGsu
E-HbTI"KWu*sDlN!<<*#!r;uk!#PbD#bj?r%MBct%ga'^M@CF2&J5Wh'+toV')WF='`A[H'GVG`(_%?#
)B'P7+=&<_+rLptr<3i=#7(YF%hTKl)&aJ;,TJ$fPmRig!;c`t!<WH&!#YqEUH9;$%MoTZ!"AsX!=]#5
"pbJ@#m^hEr<rT3q$I$-"UkhN&.oQS'E/[W(E4D;)\rtn$kEp`&ePWa%K6bO%M06e(`X832OP3n!X8Z*
!<N?+!s/N%!!*-%qu?g"!W`93!!!N7fDl-W#7:Y:!!N?EqZ$TsklCGYm/R.f!r`9%!WE'##\+,<!<*'#
!Vl]r!Wi6"!W`E-rW!6+%Mm3.7n-KV;$p/q?rYNO>u"<q;>jDm;uT_u;c6Ljr_O)%;H$Oq='8a5?XdPX
BPIE\#]+F"F`hV8?<@))(KOU@>[LoMAnc'tDKUAOIs'9r('jsA!W<!"!<E9#"8)X.":#"+64j_K)&*Vh
)%DH4)%.&h'E8aE')`LA'EAmG'`Ja['GVB"(`4,/)B0V9+=&?`+rLpt"o\W<"U55>$kEp`()Rr/+=/'X
/Y<IQm/R4h!WrQ'!##D6VaM.-)%m>^!"AsX!"8i2"UFr2!"&Q1!"/H,0+&$o$k<dZ&J>`j'GM9!*$?CF
(D.)c%hTHg&J,H_%1EXT&.oQl*>ThLU)"4D!WE'!!r`9'!W`?$!<3)s!"o;4!!**-!7:cM!XK,;!WWB(
+6<M$!;QZ^!!**&rWEH,!!!$"M#[SU!<*$"!Vl]r!s8E$3roEe!!!$)$4G%,7nR/c;,U5!<mjrR:K14j
;cH[o<)lq!<E3!s;Gp@h;H$Op<`iL/?!h#NAnYppD#S5rDfTuCDe<<W<)Z^p<`iO2?t*\[BkqL#F*r.]
CYLQP$ig8/!W<!!!<`9'q#D33!!!')"9>An%h^6*'+bNi%Z:f7$PF'M'E8^F'DiLA(&epH',)&p()If)
)&aG5*$$1K-n$8W&-s$T"9S`/"pbPE%M9?h(`=56-6OleV[r\*rrM]k!s&H*"TAB?!<<+u:(Rs\%LNC?
%0:nX$igG7#6tM>#7(SAr<i3(*srAa%1Wm\&ebom'c%Z-+X8'H'+PK`&ebok&J,H_%1NaV&.oQl*>TnF
WYbsLr;Zs$!WrN+r;cp!!Vud/!<<*$!sAV6!!<9-#mC>0"99P$!;lla!!30&"9&H-!<<**!3#u!#lXi'
!VcWr!s/N%!#PeA!<<62#mdr#;c$Uq;GpA%=4:/V:fUKl<<-)!<u"b9<)cdp;H$Op<``C+>?tTE@qKCh
r+lXWEccD@AmJG:r_jY6=Bf*?@qKChCMIU)HZOIUg`m78!!!'$r;Zm"!sJT,q#D<6!!!*,"9=Wf(`+83
'G(Wk%uUo8$ka0d'GUKZr=o&Br=g"\',2/s(Dn#.)]Kb:*[)gX-mBN?#R120)?^6M$4ICU&eu3")B^CL
.5S",!!*'"!<N9&oDeso!X&Z*!##J8!0US*'cR_m"TT#5IK0cV"U4c.rs8*#(((EX%1a!^',2,q(E+>=
,Tn!>%hB3arY#nW&J,H_%1a!]&f2Q&+"s`)$4Qk5"9AQ+!s8?#pAb=!"98G'$31,."pY83!!E9D`;fr?
!X/K,#6Fo+#lqF7$iBu)!VcWr!s/N%!##G<!<<<7#RHom?<:!+<)ZY)=k+-c?rC'+<`W:&<``C*=]ea,
<`T)t2cWjY='/X1?!h#MAnYpqD/F**DfKi>D.QsP;c6Ll<ENL5@Us+cC27R!EdDYEK\R:Q#QOi,!rW*"
!<`<)!!`9"(]aX;!!<N1!deN&*#9P0&.9EfN"-a7&eb0XrY,8Fr"]/GrtYDF-l!I4(`=52*$$%@+XJKa
+W(^q"9S],"9o,>$k<g]'GhQ'+=J9W7'6@e!s&K*!VHF3!<E6)"T\T("onXLC*OW/'ak0F%KV"Y$igG7
r<EE/#7(V4$2t;3$N(2J$47.L%1Wp]',2/s(E4G@,Tn$@&.fEd'GUN[&.oHa%M'*_&f2Q$)F(D*%1<%6
!!3$"qZ6Bj%KZ_63"l]#!<iQ*!!E9EhuMm>!W`?*rWWT0!WWK+\cE0/!!36(!W<!8!sSc+#8%+BOfVVi
;HZst;Is%_=CP32=8Z2#=oMS-=]ea+<rH#3<``C+>$G9>@:WtaCMdp)Chmp-"`eTu@Tl_0;&N83=Bo6C
AS5^mD/F03G]7h[i"?G&!!!-(r;Zj!"8rE"!#P_<!!!'+!s<R_(a0\8'G(Wl&<.2=$kj9P'ESp^'`AdC
(B,'H'GhK"(Dn#/*#ot>*[)dU-Qj38#6Y,1!sB/>#R_(O&/#Zm(`FJB+"Kmgqu?g#!s/Mr!$2.B!sJl0
!!*9(!,lru*tf:r"TT#6IfTrX"U,,:#lY&/#lY/.$N:G0$5a-Y$k3[X&J>`k'c.f2+s\9L'G(ff',;8]
'F,6_&.]<a',1]g)\X;[ZiCI>r;Zfur;uiso)Jq;*!H<B!r`0$"99Ra!"K#2!sA`/!W`<%!X,Y1"o\Mp
!!*0'r;[c;"9nl,#8%%>LUBlc<`rC$;Is%a=^tH8=BSf*=pS>:>[(B8=]ec)<]F/^=BJ^0>[:`HA7oUl
D/F*)C2@d+DJ3EZ;,9ta;,gY&?t3b\Bl%^-F*)SFH\gSn#m1/-"U"l)!!<9*"U+l0q>_H9!WW3$#6G$C
GRc#;)\`hk*"e2B)@[>n'GM;]'`SpE(B53N(B5-J'F#9e(Dn#.)uL]s+<r0Y*Yo1g!s/N+"U58@%1Wp^
'G_Q+*[2a_9XO]t!s8Z.!VHEr!<N?,"p#P@!!N?&Apb.7'GLoY!"K*]!Y#,6"pbJ@rWrN1rX/T3rXAW2
((:T\%M'*_&ebro()e5;,9Id:%hB9erY?+]'b_2l&.oQj(Ddr)-UtHC"pFo*rW*!#q#U?mrrMus!>6aX
!<)s""TT_D!<*#E!!E<(!s8W%!!3Fo$N'o(!VcWq!Wi6")$'jF!WWH:!<RGV:gmC.<E)k->M34l<a8f.
>5_Y*>l@qn>[(B7=BJX+=BJ^/>$G6<?t3b\C2@a(Chma"CM[cs>Z=Hl9hnPb=Bo6DAS5apEHQMKFE2bo
eJSGk!!!3,!W;uu!rW9!!!30&"9&99"T\j3I1IS?)\`hl*"e5C)\!Go'GVA^'EAmH('#-I(]P9N(&emO
'c%T&)B0[o*??4G,9n0B$NpM4!sAc4#n%1P&/#Zm)''_>+uNT+qu?g%"9S\t!$2.B!sSu2!!!*$!*4X_
+qk\!"TT#7JHHA_#6tPA$N:A3$N:G3%/gY7%/gSL%1WjY&.oNg'GVB$*?ZLG(_R;h&et9\'c%Js&J5Wi
(E+,,(b/Lc"98N(!!*/u!W;uu!W2p!!<N?"!!3ET!W)iu"ookF!<*#Z!:0[f!<N?)qZ$a%"+1@Vnc/[l
!W<!;!<i]0!!a&8"(T/H?rgN5<E!I5fj&/l?!CQ=rET\8?XI,F?!LT;r)jP6>$G39?=@>TBPM@#D/<tc
B`i!U=A^,48kVlT;cd43@Us+dDK9uLGB.bOUqn)P!WW3*"p4`'"9AT,"9eW&!s&E("9&97"9Am%K+]@D
)\`hl*>+>E*"EYr'`JgL'GVB!pD<fE$PaBj'GVE$)&aG6*W7#k+!DdM)A3>Y!<N?,"pbPE%1WdX&ebut
*?,tD2Jnidr;Zp&"Tneu!$2.B":#26!!!'#!(2JT+;,Cs"oo,8JHQJb#m^kG$iUJ5$iUS5%JpY4%2B?_
%hB3_&J>cm()\)5*ubt-%1a'dr>5t['b_2l&el3'(`"#?AdF_/!!*'"!<N?$!W2rt!W<!"!<WH$!!30S
"8`'""ookG!!E<(!W`>J!!30&"8i-)!<<H/<Wr[-!W)ln!!!&t!#bnB#Qau1%fc`0a&ZSK>ut'*Am*hn
BNebK?2\(0?i=@8?X@#C>Pq\(>7"P??X[GVB5)*rrbNosC1q0f>?"<f84cKN;cd11@Us(bD/slLG]S%O
Z()^8!!!$*"p4`'!<E9$"8i0!!WN9$!##G8%QB4X+Vbq1&.BTkO:`HB'GL?Y!#GDIrtt_OrYGJJ.M`g;
)B'P7*$-1E+X%sM*>T.j!<E6("pYD@$k3^Y&eYin)B'SD1OO?Kr;Zp&"9S\t!!WH+":#26!#5J7!!"a4
'd"&'$jH\B!eLRf!t#ACrX8i9$k3+Er=8T5rsni8+qYM*)&jP9*#KA#$k<mc)&aA1(`!f!&eYlq)]0A5
.!9P6r;cfurW2lrrrN&u!W`B+q>^LYqu@$'!!WEL!!*'"!WE-#!R:]F!W)j#!<j,[!<VTf)?L*K!WWE8
!!PU3='o!7=]\R7>2!:t>[UlE!+5_5$=R@P@UW\Q?X@#CrEK8+1L4<o@Us(`BP;*qD/O6,An#"G:J!uD
7nQNS<a/p?A7fOlEHceUFEhi>E#&f]!!<K2"8r3"!W<)t!!<6&!sJT')Zg!M-]\ub'H7\s%3?(A&KMAs
'GV>u'bqK"(]>3K)#b?N('G?e()Rqf)C-7C+X86W+<;:3$O$M1!X&]5#mq(M%hK?c&/#]p*@ik%9E>4o
!!<?,!Whro*!$-F#RLP4!!*'"+H[H]&JbcZ!"]3_"VLtH$Om"D":P_K%M&FJpCR66)\3Gh%1Nma)''_;
)]0;%%1<XY(E+52)&O/)'E/UE(&f'S,:A(6!!N9$rW<'"qZ$Wu!W<!"!<WK&!!E<&9E54n!!3?)-2dfI
!<WE*!<M6]quH]sl2UfAkl;e,"pb81"V1S:1=0-1<a]*5<+BCg>&IYU?XR8M@:E^E@gHOP?sd5G?!LY5
>m=VA?t*YYB)ZENC2Im.CLg^O:eF/C*CE7e9i4no?=@;SB5;F.H?sgYG/uf^%0?S7#mLM0!;urr!!<6&
!sJT')Zg!N)NtpY',qVt$l^%@%3Q5t'GV>u()7T$(\\dG(]>*N(Dn%h)Aj>1*[2pZ,p+$>%L<+9!!3</
#mq%K%1WpX&J#<\&JuZ?2jbQd"o\K("9S]+o`,s4!sJr:!WW3$!!![t(EF&&%0lkB$@W!k#7M"Mr!r]:
rXf#?rY#&>rX^@c%1<RU(*"G=*#KD&%L`[S&f2K,)]BS1'bh;n&/,iu*[<7u('+C=rW)p!rW2lr!<N<#
!!30'"T/6&!Wu@("T/6%!XBbKrW!*'"9\f.!T3tU!V$-q!sS`*"UI?n#58,j!#ktD#m()0%KHY[dog$Z
@9cu8?u4"fE+*6b@:K4G$=m[YARo:[@:3GLqHa;3?X[GTram]mASH"#EGArb:eF/B5<qS+92JSj?!h#M
Anc(%G^4XUHHd0?%0lq=#mUP5r;ccsqu?g"!<WK(!#5P8%hG!C*toS-&I]L"IgRA5'bhAtr>#ALobdWD
!u;Xg)#bE^)&O53,:G#g*Z#=n"o\KB!X/i9$4@7O%M03]$4@@],UYdK!!EK.!!*3)!Whro"T\]/#RLS1
!!!68Ql$eR((CNL$5@O](^^`^%f?k;&H3:@')E:@')`Cs&.T*U$4n!p,9Rp@&Io3V$4RUa)]Te8)&F#%
'+bZd'cSA@24":C"9JQ'!s8T+!<N&t!<N<#!!<6("TeQ%"p509$3U>1r;Zj-(((?J!!*0)"9S]+!T=%V
!V$-k"ptP5!!K8$!s/Mq!!!&s!#ktD#Qau.$3C>If32K^A7/\G@!/S[DId<g@UoCJ!+l+@"_D4S@UW[D
?i+4d@Uit]An>L`BPh^.BjO\.6U*^r4[;D+9i4qq?=78SBP_X1G'7V>`tT3n"9A]6#Qt2,!;urr!<3*"
"8r33":P=&)BKM1()%2o.U`u4'c6iar>#ALpDEiGr"f>NrYc1_(Dn/;.4cec'++mErW!r?"UGDA$k3[X
&ebfb$kF1#,rhFq"9JT(!X/].!VHEr!<WK2#m0u(&"aaZ%MfN\!souJ#o3s]&,["<&cWLD'E/^F(&emK
'+trV&If9]$jm@S)'L=N)\WYfrWrZ9&Jc8`)@[Q$(D[`!&JGp!,9JV)qZ$d&"9S]+!W)it!Wi6"%flb9
!<<*$!!`XD"UP/4!WE'-$P*IB!!*0)"9S]+!T3tV!V$.!"9ni+$imR5"onZ(!!2lqrW2lr*ruNM!<<-)
$3C[k>?t<B@piVOHAlWTAnP[cA7]=aB)Q?FAn>L_@eX:J@q91aAn>L_B5DO+Am%em4?>G^3^#_s8Jt9%
=Bo3AA7oXpEH#i.E3^Mt"98E*$OHt<r;ccsqZ$Zu!X&B$'FY6IV&^Qg)]'2$(+qin*>fV/'c$Z_rtkJJ
!#PSNr>,JO)?(N](`*u/,Ut>k)@crK!"K&6#RLkI%1a$a'G:oe&I''r,s@1i"TAB(!X8f1!qZHq!X&`6
!r`02!<<+r*#]8$%grXM,;g,J&Gm(=')rXF'`SpI('bWk()7Ms&eY$Q'+PHZ$kjR)-mKWB#mU\@#n.@Z
(]"sT(DRW!(`OYB22(i,"U,&4!W`?!!!*-%qu@c?"9AK&"TSl0IK0cW#Qau+!<rl5!!!$%"9\f.!<M*Y
rW2Wk&ci(8!!**#!!`La":5&.!<N?)q>gNr!!2rs*ruKK!<<*'#ltFg>@(BFAn,CcF*;A8BkV*iAS,Oe
BDlKKB4b^dA7K(XqI;9kAS,ReARf4^CMn$"<(/f)1c70N3^#bu92S\k>?tTE@q]^lBksJo*tJ_]!!N`9
"9SN%r;l`p!WiE''`\47$NpI.+!(t5(_mi+-Rg,Y)]BOl(&f!A(]>3M(Ch9")B'J1(De):.4c\[$MsfD
!X&`7$OdLU&/#We$k<pc,;=7H#QtA6!!3?.!Whon"9J]2#Qaf&"K!1W$5EjX$k3dg*u,M('E&RC'E/[K
'c%Q$(]>0U(D[`"&ePZcrX]nW%1E[[*@3-Z)%QoS"U>>B%M9Bj(Dmu*rY?.\&eu9%+tRV5!<<3%!!*9-
!s/N"!<3)t!##G;!<<0,!"&^Z!=T#;"TSN(!X&E%!<E6("9S`-rW1pW!!2Zk"Tno/!!3E)!!t+r#R(A4
!!*3)qZ-NpqZ$X!"o\K>"U>#9fih`cCM7<qDej!$Chm`tAnG[gBP@?Y!,)IIB4b`QAH-6?A27_.B4kgf
@q0(`CM@'L5;OuI1,LjI3^#f"9Mnbi=^,-:@qo@[F4*`)%1rgG"UYJ:!WE)s!Vucs!<W6#('=jC!2q"^
&KDW')^$.=*ZuLB(`!i$rYG,BrYYVN!>l^R)@78u(`aeJ.3B3-qu@c=!X&`6$4ICS%hTEa$kO3h,!MtY
$j."E!!3?-!Whon"9JZ0#6F]%%]16a$5=![&f25n'G_Gur=f/E#8Ish()If))?(NY)&O/)'G:uV%g<LV
&.]6]'G_]8-m9B9"9Sf4#n%1Q&JGin()Hla'G:un*>]n\U*g*E$3C2."pG)1!<N&t!!2rs&HW(9!!<N-
#Qf\_$N^bA!!*0!!!NB)!s8T+rW1dSpAbj-"9nl,":P83#M]:\!"/i.!!NK%!;cfp!!*0)rW!0+#65(_
=C,V=BEi9kBjtajCA_cFC&D]LBk_6nAnM$Rs(;1?s(;7C(M78jA7AkD7QN4U0/57>2)dQZ5Xe7?<>8\H
@qBIr?rh3h0-Uc6"98N1#6Y,,!W<)q!!!'!!##GA!!&u?*ZQ"4()nA7'cS58)Ar;drYPDHrYGPOr>,SR
)&aG5rYu+`+<_gC%0QP/!s&H+"o\`:#RLnO()n/0+!hjG5c5>(&H`FE!!*6+!W`>p!!<6("U=f'%At-^
'b:`_',V>j&JZ&Z'`JjH(+0n8(`=52)]Th:)&F&%&J#?]%hK<c',20!*?ZLE'+4sI#71bH%1`=I&.fKj
)]p+B,q9uV4eWAn!!iK'"9o#3!Wi?&qZ$Tsqu@?1!sJ]*!XA]2!.k1Y!=K&2!!2ut"T\Z,!s/Q'!SIJQ
!W2p-!X/f1!!3B*!s[0\!!!6&!!*3)qZ$TsrW3*%!W2ou!X/K&%g<+:#Lup`E+WctD/O&tAc??CC&D`D
CB\HfBkV-lrFQ%Bq.;6mBkh?n?W^/q4uFrE/hf(;1c73O3]oYu;Hm[EBQ/#u96I3S+USJT!!3E2"9\H$
q#CHs!!!`6":5&.V]['.'GM9#*>oS/*#fb4(]G0M(\AL?(Ch9!)&aG7+!DgN*#TG##Q4WD!<WK/#6tG9
!sAoB)'C(H.4u\Y98Nle":,#.!!NN)!WW8p!!<6'"U=f'"f31U*=</\%2'Hi$kEsa',:?[#T"9o(`=52
)]\ht)B9Y4'b_/i%1NdX&JQ$"*#on9(D@;d#7(VDrXBSP%1ERM$4dmn,UOlk1EmW,KE2J]!r`0("U+u1
!WiE#!!!&t!"T)5"T\T'!rrN*GQ8$M#Qjc$!<N?)!s/Q&!S[VR!W<!-!<NE/!rr<%!!rX&!!N3"!<WE$
!!!&t!WW9!!!**&rW!B5!!!)GAR]CiCMI[&C&VWJAS5^mCi!m&r+uCK");OaB_c<=Ae&KiD/<]b:.%-%
0J+k/0`<dG1c70M3^6#*:JOV^>!G9W>o41Z"onW)#6k>1"8`/n!"o>=!WrFr/0Q)P'bhH&(`!o+)?(KO
(\8F@(Cq<!(`=52+!N$Y+W1ju"9JH$*WlTO#7(P=!s&E)#7M+P$kXHb'9#6^#6G)2!!!-(rW3'#p&G0q
!X&]'!"Y\N)AWbi$kX3e%Ls!]',CE]*#KM1)&aG6*??1C*ZZ.9'b_,g%1NdX&f)E/+s%jE'+PBX$47.L
%M''[%1<II"pG8?&/5`h(*EtuMEV"@qu?p)"U"o0!Whup!s/W1!W<!&!<?[2"98W"!!E?*!s/Q&!Sd\Q
!WE'-!<WK0!WW3$!X&K'"oA9"!W)is!rW3%!Wi3!(]a[<!!*H-!<C,[An,guCM[g%An,:\B57B^!,VRM
"DhmiCMN`\rFcXQB4bahCMdlr;aiZ$0`EX)0/<>Z"Z%tm2`Ni14#J`M59iSO'G^cR"9AK("pOu/q?-Ek
%0?n;#6:/P,o7O:',;A_(],'K(\ALB(C_2u)&X>2*$?LT.3K?3qZ$[!"UG#4!s]#4!Vl^"#QPjX!!`K,
!<iQ*!W3$#!Whup!W`E,rVup"rW!Iq2'!,;$k!RZ&eGN^%h]WS(bQ[D)B0Y9*?H7D*uu7:'bV&f$k3[X
',Vc8-6F!4"pG5<$k3^Y&.]6Z$4$h="8r<#!!Nc2*P;@RqZ$d&"U"r1!rrDs!!E<)"U5#*!!NC$!rr<&
pAb0or;uoug]73P&-)\2!sJl0!!!**$*F7.#R0r&!<E9#!s&H(rW!$#!!*3$!#Q"B!"?Y]CM%U*Ci+'*
BOt[bBPVL(DJj=gDZ=SQD#J/IC(tAqB4kmlBkL[G5W(5J/M&J+0JP<]0GlN"1Gh$M3B8oM4?aU6TF2&+
!<`H(!sJl,"T8H&!qlTs!=Af1!!e]G.2a*@',:B]rttYOrttbPqA/uFrYQ(^)&aG5*$$+F,U46>"oA9$
!X/i.#Qk;8!s/5u"9])4?\SFY!sJf.!WE-&!s8T*p&G-p!sJT'!!<-"$BQtc%hK*V%MKHe"V;1V',;>^
)#bBU)B'P7*;pm%)]9G+&eGQ`%hK?g)''kF*#&b`":#8B%M'*^%h/mQ#6k>0!s\l-!"'8;@"e@V!<E<%
"9JZ-!VQKq!X/c/qZ$ap!!3-$pAb0orW<'"!!1gS$NU80!W`<%!!*-'"8i-&#"&@o"TnDu!<E9#!s&H(
qu?a!"TAB7#64`@\o)G%F)Z#8Df'6%AnPjqrGV^RqeuFN!,_^Pr+lgXCM@HpAn,1J8Nnsb0)dF</h\n4
0.nk21,CdJ4?Yhf2+Tt]Zr.M8!!NK-!WrT0r<3-&r;uWl$O6Y5"H5/g*#fV+(&f!M(`E5iru(hRrtkYM
rYPPNr>>eX)B0Y9*?G)"!uhp^"8`'!!X8K,!X/Z,q>^[3%fhhV!r`0,"U+r/!<E6'!s/Ms!!30("TAB$
!r`0*M(^+e&.8jU'E&OH',22u(]G9M)?(QP)\j5,().An&.fEe'c.c.*?>t/$3^S=%LNUS%M''[$jm7F
"pG/7rW`W2";qsYQ95!E!W`9%quZs$!VQKq!X&Z-r;[$&!)!:p!!2fo!!3'#rW1^Q"9AQ*!s8E$rrN&u
"p=p@":>,1p&P*nr;ls"qZ$X!"o\K8"TSWAZ$pS+F`MG@EGoZ.BPM@$rc%aQpi-4Ns).gQ&8Z,rAmntH
:.79%0J>%1/M@#U%PB=b0/>@C3^#_o4ZPo#"&-'>')hn*"TJT&!r2fr!WE'0"TS].JjLn))\s)%(Dmu-
q\o_X)AsA/(DcudrttbRrYkbT!ur:$*r[5c*?#_-%0lq2!!33)#6"i="pG)1!<<*#!<<*2)CLmV#Q=]*
"U+u0!WW6%rW3'#pAb9r!X&Z*!!!'!!"49>+V>:p$P!d_',:E\rY>JMrYYAI(`4&)'b_2m&J5Zk(`F;1
)&Eqr$3g_A$P!%E!t>VE#lOu9#RUqJ$4.Rn/=HbHrW)ourW<'$!<N<#!;ZZt!<WH*qu?m+3=,Zc!quZt
!<E6&!S@AT!<N?*!rDs!!<WN)!!-L:nc8Xi!WiE(qu?g""9ni@!!!-%#8F/!CM\09EcQ5@Df'<,DK#Mo
qf)FPs)S*YrbrEeDJj<,BOY4G9h%?-1bg[;r@S+(0)dF90/>CF4?l5(6pNOa^K_HS!!!$%p]LR!quZ]p
rrN*!#Qk&5!-qKg)B/qt'GVH%)&jP9r>YqZ)]BS2rYGbU(`=20)]S_q!$2%[#p194*ubt-$jQn2!!33)
"oSW8"U"o/!<E9,"pY/8SO3S[!!`Q."9S]*!!3'#!!2fo!s&H+"TAB$!WE'0F\Wqh&If-Y&el&s(`4&)
!u2Od(\nmR(Ddi&'bqDr'E/UT',;?&)]BM,&Io3U#RLhHrXB8G%1ERM#R:VA$4@7RrY#DB&Yhf!r;Zfu
rW3'#quQj!p&GR'!WrH'!!*'"'djas!!;ior;l`phZ*c[!WrN*qZ$j&#Rgt?[K$R&!;urq!!30)#Q=]0
"TSW;Vj_:DF*7J("`n[&Df9UlEV4AMEW0tdE,96!>Z46]4?,/PqChq'0)dFE0/>FG4?uJ55rh#/^`*@_
!rr<%!WrQ0"pG/5"9S],rW2iq!<E9$!##D6#lo'N+XIp>'GVE$)B9e>*?G,!%3$6))&O/+(`4,/)]Tjr
*<I9)+oWYh+WhU:%L<(<!W)j8!<NB-"pP;;"p>#0!<EE6!s&c`U':T%!W`?$!r`6"!ri;q!!<6'"9e](
!!E3#'6$qh*"EDd%M9?i)&jJ2'bh>s(B,-V)&X8-()7Ms')iIQ&.oNg'c%W()]KV.&.ApE#ltDBr=0MN
$jm:H#RLhG$k=$m&e5[;W!WM-qu?]tqZ6`uoDemm!rDs$'-%Sa!!;iorW2WkrW2-]!s&H)!W2p'!X8l5
!sm6[&a',q!X/i.!"T>8!"Pj"BS(8IF`qqNFE@;!rH&!\s)\-Zqf)UVrcAHcCLpgO8j>6j0`E^+0JWP^
(,7Kr/hJY/1H%9V5Y4g<68buD$jI4Ir;[-*"U>8:"U"r1!rW/r!<3-"!!iT*#QSdN+"e9,'aPQl)BBnA
*Zc@$*!7,u)&`Dj"W80r)]Tms*Xs59,UF]\+W_I5$O-\6qZ$a"!sAc3rWa#>"U"o.!!Wo7$j_bJ!!!H6
!W;uu!W3!!!VQKq!<N?+rVup%rW![L>Sndr%1NdY',MT/*#TJ(',22u)#bBW(D[\t&J,KO%Km:T'GhYd
)?^om&I]!F#TX3Y$k3^X%LrpV$OR1H$4I@Q%i6<$)AJGu!!!H4qu?]urW<3'!Wi/uq#CBqr;[''!tH%P
!!!&n!<3)l!;cfd!<*#q!;urt!!r]3!t>?G#6b)1kPt_e"pb50#m(G6!!f7#DLH^,GQ)akF`__HEcZ;D
FSp7_FE;L"EW:(YF")*GB44q<5rC2B.4Ql$0JbRC1G^a>0.nk32*4#b3^#l*951.<%g<:Ar;[0+"pkP?
"p>#0!<Mrq!W`?(qu?s-!,6*l-l<^+'bqK$)BL"D+!1D%!ur:")Z1H[)B0Y:*ZlLI+X/-0,6oD9*uGRs
"9JB""p"c-"9eu7r<N]9#QXo*!>$#0Jc5WM$O-G.!!<-%!WiE(p&G<u!WrQ*!!3E)!"`dS*?c"*%1Wm^
(`ab@)&3_d&ebur)#bC4(DRSp%LidQ$OdLV&el)u)&aD2'b:TS"U55>$OmRW&.]6\$k!CL$P!a^%LW[Z
+XKa=#6b)7"T8<)!<WH-!s/Mj!!NK4%h]!HkQ(S^p]:$fquQTn%flb9"p"](!s/]-?5*G@!U'Lo!X8o2
!!EZ0!!8UtFEVtUqfiBjG'.nJF*)MHr,r3cFE;JCrc.jV.<'-;@9QMs3@uL#,UY&n0Jk[G2)@!B0J>(8
3'BPg1c76i3TNO:$3LG0!"&`/#71\A"p>#0!VZQq!<NB$!##V<@<*h@*>fP-(E"27+sA'N*Zk;$!?<'V
)@.9%*$$(C+X/-0,7,P<+Wh[>%gW7<qZ.*,!WrQ."pYD?$471Lr;Zp8#J28\!!*<*r;[''!sA`/!W`>q
!!`N+!sAT(!t"r,4C;tN)ANen%M0<l+!MdF'G(fg'c.]()&O/(&e>EZ$4.%J%hTHi()If*)&Eqq#Qt87
#R_(O&.oHa%LiCHrX08H&/5li"pYMa(<A*.!s/].r;[$&!sJf0!WhZg"pPMI%gWCBr;ciuli?\Zq#L9m
q#CU#"UGD9!!!6)"U(P"$j-On!#YhA#6=f,$31&3L:;8JG^4R\H[9s^GBS+OrH/!\q0"E6F)c,8DfTr?
B3Iql2(g7$,:"Tb/MK">2)?s@0JP=<1c@9P1GD*W2NY0a!"/o.!"8i-!<`T4#R1G7!WiDs!!30&"9&9X
!<<9';gBu@*>o\3)]^"D,9nBU+<VaJ*ZZ7@)]Kb:*??1C+!)ID*?caZ/1)DQ%13=D"9\W)q#M-3#7(YC
#R:J4!!`Q,A;pWj!<<3!!!`N,"9S]+!<Dfn#6=i-"9AK*$2soH;0=3)'+YTb',DK-+<;:4&.fEe'c%Q$
(D[`!&ePWbr=0\V'cS8@*uGRt#m^b@#RUqK%hK<c&.T*V$iUP7%K6hF#mM1Z&osBJ!!NH+r;[$&!WrQ.
!Whonqu?`u!r`9/"U,nM"98E&!<N;f!;Z`m!<3)i!!NB)"9\f/rW!*('e04g!p0Ih!<`T-!!3E+!"TKT
\T2n:G^=acI!U$\r,qjX"*Sp7HN&7EH?O:EBkqX-E+)O)/1)Yg,palc.4d//2)I'A/MJt<2Dm9E/hJ_E
3_\3[(^(*Fqu@')!sJo6"Tnf-!<Mlo!<NB&!"K)2!WYQ=0I[t\)]g+F+qGqF,pX`\+sA*P+!)ID*Zk2#
$6:*))B^C[0I@VDrW!''"pG,2quQ`r"p"o7$4$e9rW!*6#U$Je!r)a!!<N?)!<Mcl"p"f/!<<6.rW!Zu
I4--I%M09i)&jS:)AWqr%hTEf'EAjA'fcp?&J>p'-S$AV$31&/#Rh1Q%hB6b',(re$3pkG%1N^Q#R1J=
*Yp?B)[QKI!<<*#!!!$$!WrK)p](9pq>^X!!WiQ2r;[*j!X/W,!<N?)l2^GVrW2Wk"9JZ-!Wi9##Qt,.
%FkR`!!E3#rrMBb*<QHG!!*9*#7aGLC3O]BH[^KoHZsRRF`qqNF`_^'EY<M>H[^ElI!^0aG&hD0>>dsR
1&rd&-N5A6-n6c$1GgmA/LrJ13'&oM/1NtV,X0mP+US>P!<`K&!!NE,"U"o/rW2Zl!<NB&!!!0$!!k*E
/h@t^+!N$--3bbB,U4KV+T<H#+<_pO*ZZ4A+X89X+<;:3$NpG0!X/f5"9\W(rrN#t%0QtG#6=f)'c[2h
[42L]!!3<,!rW*#!<N;l!!WH*"9AK*#lXf<.?u/#$k3da)]Th:)Aa,$&.]<a&cNCF',23!r#$%b*[)^M
*?#\*$jQn>#n7IZrXfPO',2,l$j["A$4[RS#mLM7*@(_0^G6B"!!E<,"Tnf)!!30&!VZTo!W2p+!<WB)
#7:V7"TY4u%/p5/!X&T+h>mNUoDf7#"pY//!!EB3!!(IH!!`N1"T\W*!WhTe!<NE'!&4T\%1Or<Ap/-;
I"6ctHZsOPFEVkOF`_\GEcQ5EH@:<oIscTjI=6?R<C&>i.Ochrr[8p=.4Qi"0/>=</hAJ)1cdcX/Lr;,
2B/31+q>7g!!!B4"9&9$!<N?*!s/Mo!"]26!!!$'!<<*8X=l4I+!W-3.0(do-Pe$T,U4KV+<VgO,:"ER
)]BhG/1r4b$N:#2!X&Z2#6tG:"8r8t!"K&9$jH\3!=TP?ITm3\"o\K'$O?k4!!!&o!;QU3!X&Q)!sSi/
!#)1S*srGj)''_:)&<o!&H*.=&-WXY'GhZ-rZ)Lj,:P6!,o6mg!!3?4%1j0N'GqJt'c%Mr$jQn=#n7FQ
!s8`?(BB.t&HN4;!!<W:"9J#mrrW)u!WiH*#lt5<#m:Y:i!'_k!!<9*!s.6YrW2Wk!WrZ6rW!K<!"BQ&
&/5*S$47"@!s8T*nc/XjqZ$Wt"9&9+!X9)E*klW8Esd5DKReJrG&qbJGQ)gmGB\:WH$XjeJGt-WJ:;fe
De<$<1*dtb+XA?[-RgMr/MAe41,:R</hSk93BB#N2*s):CRcIe%M&[B!t#88!WE'$!<N<'nGj1'!s&B&
!s/K($_9I8+sSHa-78U9"XPE>,9e?0,Q8qp,9e<W,pt#['+"R;$j$P8"pP;:"U"o/!Wi/u%KQ\;"9AoO
&HG[`%1WFDrW!!*"p4&i"T\].!WW<$":kP@Q80Ki%i--()&<nu&.e^K#7_4T&ebrp)&4)3+X89\.4Qep
*>/PV!!3?4%M06erY5GL(]G6i'bC`Y#RLhG#6YMY'ED*h&.esM!!!'-#Qt1u!!39*!W<!,!<N9&"ptJ5
%LLDc%/p8+!qu]k!VQNg!!!&l!!30&!Vl]t3sl,nrX&c5"9S]+nGiOiqZ$Wt!r`0@!<iiA'q0hsGCG:#
IsZE_FEMbOH$XgaI"$TsJqAXRJe<Q^FD+lQ5Vj`-)B'S:+<r3^"Y;8\1G^fc0c;`&1Gq*N3Ar`B4>:Ej
0E;@a%LE7A#6b21rW)ounGj:)!sAZ*!!*-'"p]QW0de>".3fuY,5ibc+p/u3+sZt1$RR5L-mg,Y)&!Je
#6"c#"Tnl0!Wi9#rW!Q3!sAi/)A>rX,QIfG#R(51"9Rff:]UY%!s&B&!sJr8G=`kf&fVf.'bLrc$k!CL
$OdIS&/,cp)&aJ9,:G)q.jcAV&e"sF!X&`8%1a$b'c%Q$)&aG4(_mVl$OI(D#71DL'2T+I,6.]F#mCA5
"pG&/nGiXp"9S]%!!<6*#6Ff(#!rb!!<E6&rW)ltrW)s!qZ?cuiW/rZ!!2ut%06G4df:9i#m^hC"p+i*
!V$-i!Vucr!W<!6!sf/I?FOcnJW,21H?XLRFa&(VH[UDCJj"dAKnP)0J:2`cAl_A[.j5cE',;B)+<r6`
/ho4B2)?s@0f(^J2Dm`g2_Ha(?ca_t!!!**"pG28"Tnf,q#L$e'`eC>!s&B%!<`K57Z/oH.l/Ip*ZcI'
+UB24+!;^N+Wqs-,7>bC-7:/f+W;"'$4?b=rWiN0#5n]>"pP55!W`<'!sAT(#7Ue:#lmN,+T;?B!X&Z*
!WW8i!;ca4!<WK-!<<*$#6kW'IiAk4+W)%0%LWUMrWiQ3$4ZtG0G>3>)]^%H-nHnr*>Ane"Tnf."pk\I
%hTEg'c%W()]Tk;(`!bn"qD7N!snrs[N,5GrW<9+"9S]+nGiXq"U"o(!!!$;!sAW)!!<6Q$ig80!WW3%
!sA`/!<<*#!Wr?'rW3'#iW'#^"9JH$"9SW+"cWE\#Qb27#6k;4!<MfmquQWo!!2ut#6b)D-e*6[ISQ2R
JU;WbF`qtRH@('nM1g>/KnP#+HZjCE@T,WL,T@I1%hKEl*?c^W/2/k=3B&cL0JPCE4ZG8c:HU`n*4A<P
$31M<!!!0,"U,#1!UKdh!<WH,!WE'3"TT/JXZ7g\4rY^f*ZlOJ+<MX2*ZlXU+W;@E+sR"20d7b^(_?uV
"9o/?$k*LO#m^_<"9eu6"U"o/!WrW4!<<HD$5!^JUcT4u!>#J9!!<;m!;urq!!E<*"U"o+!"K58'Fpf`
&JZl/*"rei$2k,:#n%@^&e#?g)&jSN+<i'W,TRO*!WW3$!sJr;%1Wm[&J>cm(Dn&1*ZQ(9(C^Q\*"<Jg
!2)4Z"oo#5!!*!#!WiE(nGi[s"p>#/quHWq#64c3`W-&?!r`0+!sJl4!s&B%!<W0$!WiE(p&OI[('=a@
!!<T/#64b\#6Y,0!WrT0"9SZ*oDnahnc1BT)3V48RVAF5G^F^ZGBnL^IXZBUJ<GnDI<TR>>#7[N1bC'u
*#B;%'Gqf5-7LK!1)i&-2)[BM1Gh$L3BK8W1H[WT_Fk%8!!!6*!!)s"!WiB'li7+g!WrN&!"8o/%1$lu
+%m;;&f`(n,7u1H,pXBB,r[S.-RBlS((gr\r<<<.#RUJ;&ISsR#mUV;"pG,5"pG)3"U"u@"pFu,%M9MX
49,H`"UkS8!!2TiquQZp"9AT-!s/B$)$C$Q"_DBS3!MMT'bq>k%M'-a'GCcU(Fgg3+;,_7(_mYo$k!@I
#6k>8#7(\H&,m+?')iRF(]G<_)&O)%&IedD%hTPT2ZNg_!!!6*!!!$#m/R7n"p>#0q#CEr!r`0./0tE!
#QOo+!!*3)!rN#u!W<*!!TO.^!s])7r;Zp#!3m@=!<3-#!WE0#!VHHi!V-4^#89>\JT6okM1BtuF`r%V
H@($jK6_?UGB%4s8N\XO)]B\<+s7pG)B9kE-S$f'1,LjD0/GRI2E3]S1d",Q1bC8[LEI'8!s8E$quQKk
qZ$TsqZ$Zu!Wi/u*X;lmYsBa)(,%$],U=]a-n-Vr0f1@&-7gVl)\NGXr;['*#mptF#RCb9$6BKZ"pYA8
!!<K2"9eu2!=9><#6bKtF;,#j#RCV;!V$0d!W2p#!!!'%!W2pW":>8LUbEZH&1f"F(DIW%)B9_;,:4EG
*$cgS*#/qg!<<*'$4dUT$4."G$4I@R%hB9d&.T?j(]G-[&.K9i!!rf9O)Y^6#6P&/kPtbi"U"o/!Vl]r
!<io;!<@KI!X\o7!<<*$!S.5_!X8o;"p4i4!!#k+!!*'*"9JH$"9AT+!<Mloq>p0f$3UYfRIb$GGBnk$
4FqX!H$OUOAnGasG&qA!6T?_H+rqO:'GD,q)BL(K-7:/i.k`\4/i>aM1,_3S2`NTI0Jt+@c;"?S'bgQH
!s&H(!UKgd!V6:+"oo<S\Ka3_,;(u1-RpZ!/0u>[,q]N_1bKm`$j[%?!s8B#-NO;Q"pP24!<E9+!WWK9
#QY&5"U"u0!<W]0+0mj+$P='Q!sAc1!qlWi!<E0$q#LEqqZ%c@$31TJXV`r?+tPQ!*$6@M,TIL5)'^X_
-QNg2%h9!U$7lGf"pG5<$OdFN#6b56#R^tH',qYq%M93]&.AjN%KIQT2?4!l&-)\2!WiDg!!WQ/!s/N)
!Vl^$!XA]*#cdq+"oSE%"9IN_o`,=#!<<9/!WW3$!3,kr!XJr1r;Zs$!s8T*p&Opio)LZP"ro\El?Zoj
M2lsuCi3ruCik&QA4S^6.4$&T)]^%E*>]>"(Eb1`2E!BG/hJqD4#S`A.k_Gm4ZYJ_0JZBH;8ZHC*!.&`
rW!$%"9S\k!<*#k!$V[K"r<K-2]+>45r'Z3.4$2i2aTqd('t$C!W`<*$4daX"8r3.":5DB"p+c)":PVA
!WE'+":,25#lk/V!&CJ\5l_Dq(^C$@"9o&5pAk!imJor`%0-MBNMnZM1cdfP*?ZUN+"&d(4=:XB!!*<2
$kF!e(_R2Z!!3E9&ePTY!<<*%$Od@I"9Sc5%1<IT#n8?a0W%&7%KI4H!!!$&"98Pi!<30#!r`5r!"9,:
%00?q!"9#7!!<DV!!*-)rW!B1#RUP5TE"s%!"&u9"T/6&!<`N-!rW,q!;cff!(R7q!$<DuXI4!=ATE06
?>"1d9JdtE2(p:#+<27<*[2s_1,qKf9iYD*AoN-SO+D+P9fjgW3&icI-m(fG3*jF&'EA4>'*\@8!s&K*
!UTje!<*#l!'(5k!!!-%OEb+d-RUf=1+"\90H15s!Y5V?!sAZ+!X&]5$4IFX()\,9,:>3.8l7u2,8:4[
!!NQ0rW!-:*"tQ:63R8f#8%.?!!*0*"8;fk!V6<h!&Fuo!<<-#Mfi;Z,pb<0/gE#10,Xil!"KDB$4[RW
%1<FG#RV%R'cA#7+!)XV2a/r<'F=[<$j?nC!WW3@,8WSB4otW_!=o>4!!33)!qcQl!W)lr!rN)p!!!'!
!!!6+4<4P+f)YgOqZ$j-%Kd.PV#U`!!!<<-"pFi("Tef0!s/Mt!;cfg!"]29!<N6N,)>,i4!$+:-n$8u
+!W*\-mBZQ+<_mM*[3!b2ap_YF*`7cKT2:fSskt5S=#M(MI\n).5`eF4$dB!.hE9t&e>6Kr;ciulN$nb
p&G-r#RgV3#SI8N\N:9$"qLP2#Qb5<"p+o4#RDsc!s&B%!=Thn1,_'N3C$)-9hS)U=&i'o8gt&H!"&iB
%N.X=)$1!B$OR(>r;Zj"!VcZi!Up("!XK8I!rr<4!F`Dr$NL59qu@-.#R^qE%2'Hp(_dD_rW!$/)'p^T
.kE8*0J+b$,V(W+1,q-1!WW?:%NcQ37^3[.!WWQ6"TeQ%!<N;q!;cfp!;uri!"K)2"p+tU#6b\?!!!''
"5s4^!<WN3q>^s3$O>_u$kNFE!<<-("8i-&!X&T-!Wi#qquQ<f3s,H_"W@da+fgi3,oJ9\*Z#G2(_I5e
&/5s$*[3@-<b?E%LQ@XaQC+>DY-P40UnOWbUS`0$1+F(r+U]`k]+u;')\ND]!s/5uq>p0frW2]m!W`H0
rW!H>!!3LiGs;W9&IAL=!!i`+!##G<"p>#6%MTg+.l9:L4Zttr8PT1](K+79?W^Sj%0Zn8$NL0RT*#Q9
'FOsE!V?Bc!Ug"]!X9#B!rr<2!!!4]F?9[,&.8XA!"B5<"ptnX)]]k6'b_,g&f;]:.4d)*0.eY#+WMFA
,qgl4)up*M!#G_EK;/GR%1igI!s/K(p]10kq>oj]#6Y,3!!iR$3;`a^!<`E'!<<-%!rN)j!<3)u!$hXO
$k3FA!!*6-!!"`a&Hi.9!=&c.!<WB(!!!$$!WrN+!W`>u!<3&s!UTkP#6PMO'f;SS7M[*\'E]No#mCG:
$kaF#.n!fnP+%o2S"-%?Sti9gZEC-uS#X-%[>.4*+>b3Fa-dMa&e#Te!r`0"!W2p$!<N?*!Wr?%oDnjk
o`,!n"9&93"onu=$7M+!3!Tut"TT>I!W<!(!X&W2&g/bb48h8^4[)(s77g0I9hJ)`CKY48%KuhH!&gNr
!#5nJ'ajm>!!2rs!!3$"p]9pc!W`9$8,rVj!s]/9!!<H+"pP/QNf5k%'+#'I*YSkf%MK^"*ZZ4C,UY#h
-6sf`.kWM-.3ouP&ISpa0-`D!!!*<I$Uh.L!##P<&-r17!s&K*!VHHi!U0Re":,GG#8$qM!!'!4!!!?+
"Tno1!<N?*rW<*#pAk-mrrW-"(^13U&.A[H$NL/.[Ntnn!!!91#6k>6!<N0$r<*$#rrMoqqZ6$`$N^D2
$kX=0Wh(4K">_k7#n%(I$k<pk018r\KTqgfOGo-XNfTBkSY;aMSt2INWR./C3\iOD`*!KY!t5SO$N^5,
rrN&u!<E9$"9/H%!VHHl!V??n!WW6"!Yk_9"ptniU6ZN+!%n6T#R1D7!W`?1%i-?A3^cA&5<M.t7nZTS
<;]c);cd"J;^W(h)/-$8rW!$+$5!XD!<3)t!!!&r!rE#c!!iW."pbA6"Tnf)!#>\G-)$YC(^;ht#n.:V
(E+22,:P#d,Q8hg+<M^L*$Z[M)]'5*)]]t=+!*s'%0RCgEjeU@!WW3&$jZb3!s&N,!VHHk!TsFb!sJo3
r;[36!Z$AW!rrN*!!38r!!!&h!#,M?#m1/2!!!GJ&c`%:!rrH-"9S`(!Vlfq!W)ln!UKeF!XB)F$5<dR
Kop'`$4da[%h]Ni(a;.KC3+o]LOjeqF`qtSI"6p-NKKEmXhLEqW(TBbYa?[@#8%%A#n.1H!r`3"!WE'#
!<N?%"9&B#!VZTm!VHHl!C6\c!X8l<":bP=JraRZ$4d^X$k3RL!<<`Z0K;El8OPg.6V1'R=^,0=?<piD
CiiEA?P!r@RYM[Z$31&1$47"?rVus#!WE)u!Vc`q!Ug$f!C-_i"U5/7!WW9(!sS`4!X=@CD]B<#&.8s_
)&a;,-T3V(,9nWk1,:R=0J=t+-RUZ44#oSr)A"\)"@/K9+9iAU!!<9*!s/B$rr`9%q>gHorW2Hfr;d*&
!<E0#!<W0!$j$D4$33&/$3gP:!!;lp!sAi4"7Q9r!<<f=!',f7%fQG1#6k20quHTprW;uur;cftqZ6Nn
!!2Zk4TP]p$3pP2!Z6rs2&60+$j[Lh*[*sdDf0`HI<p-\EG]E%BP_X1I"I6;OdE/kWFs9*9F1t.#QXr3
#R(;.!;lls!riB#!r`5p!;lld!(Htn"9SW(!umE+3Z7u3#m(GG"99&d1H%[#>$bTGA7fLiCi433F)l/2
>ZP9Y@P+(`3rfKm%0HV7"pG,2!<<-%!W`<'!rW/q!ri;i!!NB)!WrQ.!sA`/!W;uu!W<!Q"sBAD4r=8,
"9fJ^'*oX;2_cj1*>]bE.4Qi!/M8\0-mq2W5qO`W1^f&F2ZX<u&Hhe.r<!!"p]19on,W:c!WiE(q>^Qu
!!!H5"98F"fDl$S%0-A/!rDs!"UYY:$lfW]#R:P<"U,)9#mgb:"UPGC0>%8k!!EH*!!rl&!;HTp!;6Hk
!;uri!"K&8%1`^E"p,;pRZS[-(F';#.j?')DJj'#DJsK7EGArd<)m%*@VKe)IZU1dNO%b?+rC1X"9AZ4
"TeK#!!3'#!!DrsrW2coqZ6Wqr;lWm(]amM"TSf5(."[\+qt[m#9!aG&i)C)5trS&=^YfP@pr_P@Us%]
Anc%!DcK8IZm#b^!!!E6#mUV9!<E9$!W<'$!s/Q%!W)ru!Ug!h!<W3%!WiB'qZ%fC#m:5:%3J3=Or"</
!=U:e!#[d\6XYG/Up.DE`5]pFe^tPdb-[%8<_k7a8WsP_!rr<5%1*.4!<3*!!ri;t!<*#f!;cd!!WiH*
q#Cs5%LE4;!!*V.PlUjm!!W]3qu@'.$kO'e(D[\t&.eaM#nR^`'+G3I%2Rk'!!!c4!!<?0#mKo#nH&Ri
r;cZpo`.#S"UPM;!!X#=$iiPhJjU=q&eGgA@VKFa?X-c8;GKeP6:==;:fCFu?Z:URP*+9H#QYA;!!!-,
#R(2/q>^KrrW;our<!!"p]10lrW)isp&GR+"onW/'akWS7&GJt%1rL=.Mb$59NGJ/A7fLiCM[j*E,fl<
EGT<)De<QmYRgd7$k!@H$3p_9!!!'%r;cs$!X&H(r;l`rrrMQg!!3!!rrMrr2?F$^!"9e\*!AQtE\e(=
$j6YX8n<-qKoqq$WN`kE_9('RdCPp,H#@1l9i%;]!!!E=&.AsOp&P$lquHZr!!2QhquQcurWDrr!s],:
"TAB)"98V=&In[=$j6P1!=95J&J,B[$k<1G%h/sV%M'*^&J+pB#A=;H#6"T*":,;="76*a!W3!!!rW,u
!WN6#!VZR8!WrN."T\T'!s/H8$Nan[A/$!p(c5,s@9H;p5r^Y!0H;i*3'BMk4Zbi*BQ/-`S/)nA"98E(
#7(S=!W`?!!!!'!!r2rt!WW8r!;?Nm!W;uu!WE'%!<<*$!r`0Y"9SZ=$j'qS<s&X,!['g1@q/nS?X-c?
@V0@lDJsH1CM7@!G&M)PN!B[i!<WN3#mUS6!!*-&quQ]s!!2irrrMoqr;lcqqZ-g"!<E0#qu@c=!!!-0
%1=$\!*?[4$l9Bl4(O&?][#*]g"PHNnb<"^'CsYVO,/R9Cl4)R$315:%hB*T"7lNf!Up*e!WE0!!rrAu
!!WK-!s/W3$8Df%!!!&O!!!-,$O$M9&ekui#m1/-!sT&=#mgkC#m^hI'+ksMB*/SC!WiK0#m^\9m/["a
q#^KprrN'"rrMoq!<E9#"9JZ-!rW**&fq#Y(1k-j2%(?J;bobC2(pF*+WqjL+XJNg0J4n*.QgR.>D]!O
!"0)<!sJr:#R:M9!s/9!"p"c,!s8Z/qu[!%!Wi&ro)\di#QXr-!WrK*!<N&t'G)2`"V"M2:a5ub>@V/U
C27QuBPS/sEHHAKH$OXXF)cGSF`3P@rW!?0"9AT."9S]+!<N9&rW)ltp]:R#!WiB'q#L<noDejlpAcE=
"U>8J)ZTjE=gM[)-;TbsW3sF\bKnYjhrO"ho_8%Dg;^N4Z*'UVXL/<:!t>_K%1EOI"9J/qp]9mbqZ6Zt
quZs$!W)j$!<N?)!!3<%!"o_R]F4cG!"9;I$O-b:!<<*$"8rE&"q1Y>$P<dY-s$BN!"B/:!!*6,!s7ii
r;lWor;ciuquQj!qZ$Zu!X&B(4Tb`g"TSN(#mq(Q%g<k%WIn>C:,jOB*uc%5(D[`#()\)7,9e6M*@s<7
5^&e#!!3Q9#7(VB#RCY>"9JT#!!30&"8rB$!s/N*!VZTe!W<!"!<NB%"9\f-!!!'!!&"BV#7V(A$lG7T
>ZblU?Y==uF*)SLG^4U_IXcluIscToLO!p1]*869#Qk&,!<W6&!WiB'qZ-TrrW;lsrrMoqquQBhqZ/_X
!!*0%!!Wo@#RLV6&gjcQNg@,VUo:K*]uA7De(31+hr3SSi7ur9e%Da(h]NIA'bC`[$OR1F"TnAt!!3$"
rW2lrq>g6jrW<!"rWE6'!W<!!!X/H%%0Qn9!"9&3SQQU+'b:WL!#bk?!s/N)!<N<)!sA]/#7LS74h(S%
!#Gn@!;us!!U]sd!VZZo!<3)u!r`5u!!**%r<!0(!<<0(rW"eZ#7CnC!rrZ5EMPiO*Zc7=()%;m&J>`l
(E+87*?,k6+tPB,9m0\O&HE%H&.T!L"9er3!r;lu!<NB&"T/?'!WiDt!;6Hm!WE'"!<W3%!<N<$!!!&u
!"T)7#Qau+!s3\V@pW>LC2j,k#'+d-G'J=\rdG9'I"6p%J;BtF+W(1[rWN9(qZ6KmrrMiqrrMoqqZ69g
!<E2t!!`Q+!='#>#6Xr*'bVO[n>NOl['mQ\`QQWWe^rL1i8WhsjqQn;in)Gset+rS%h0$Z%L`XL"p>#%
!!!&u!r`5m!;?Nn!rN0""98N$!!**&r;[9,#6b)-$j-SMbm=aX#Q"N#!W<!3!<E6(!sAi/#V)_a!WWK-
!sAc0l2^eapB(<oquHd!r;lcq!s&H)!VcX&!<if1#T*dJ>*NM[.462X)]9G+&J,Nf()\#0*#on9)&aJ<
-8@,TNDp)e#87d`#QOi+!sA]%!!**%q?-]urrMlpmf<Om!WrK)pAbp/#65#J$OLIILi?s;BPM@"CM@Hr
CD^o,EH?8HG^4R\I=[*1H^2-](C^HQ#mpk7!!!&o!;urp!ri;s!<3-!!UB_3!<WK2$4-q;!#?.bK\42Q
]=u2%aNMoWeCN:+gu.5Ul0@Qul08rJlKQODl]a(E%M0-_%1*7D"Tnf#!!!'!!r`5l!;6Hl!rW6$!r;lt
!s8E$%0d(D"9o&1])VgD$j?\-!<3)u!"K#3"9\f-!$E2*#m:_>$j$bB"R6!d!VZZp!;?Nj!!!&n!#GY=
"W7:?'L%sD0c^rA)]9J.'b_2o(E38nr>beW'c\591GrE^+!:Rp%1`XC!!*-'!WW5t!!**%r<*!"rW2co
o`>'or;lm!!!2cn/cl+m!<XQG\R9&V?XRV^B4YU`@:EbZBPM@$E,p&DH%(@#Lld4TU,X_)"U#)7rW2Wk
rW2`oq>gKrrW2lrrrMZj3!9Kp$jm(M!!"K]foMu1\A-50b08/Wd*^:kf%]0Glg4!(m.'cEp$g>Xc<*@?
#mUnK$jm:G"U"N"!!3'#rrMlpqZ-KorW)ouqZ?cuq#LBq%KQP1!s/K'#QhgM!!!$#pAb3q!W2p)!sJ`+
!X&K'4LYXr!!EB,!s&Gh!;urn!rN*!!WE)u!Up(J!<<*,'aG3K"HY5g0e3\<)AsA.()7N")]g.F*uu=A
*ZuUJ)]95L$9h.C'En^J$j?V2!<N<'q#CKt!WrQ'!rW/o!;cfr!<3)t!rW0#!Vl^Q!<E0##o*a]!?JOQ
B68<'=D;;R?X?uA>[CcG@qB=gD/aQ?IY3H/ULJn-YUBbW!=&c0!Whonm/d.errN#tqZ6Ek('"=;#RUtP
('G*J.*I10[)BJabfRoHr5g&'bgG)#jlYailLXoQqu==R\Ca+`"9],B%1EUN#6Y)'!!!'!!ri;l!;llq
!;urt!WW8q!!rZ."9er2!<<*B$38QW!!<3.!WW3$qZ$Zu!Wi3!"Tno/!!<N+!"1'l!<<B.!!!*'!Wh]h
r;lcsrWE'!q>^Krn,O(%!!!99!!!4rCF1MD1(#?:(`FG5()7N")BBn@*?,q;*?QCF)]9>=%Q-dYH2nfp
%0HM/!s/T-!Vucr!W3#u!Vufi!W<#u!Vc]r!Vufq!?;(>"q^h<)o.bDB3'C]F&u^S>Zt94=^#':@:a-d
Ci402FEr=gJraSsKnGTi((1HNklCP\quQj#rW<*#quHQop&G[*"9\l<('=ghf!gF,R)uJT[/RfS]tCti
]tV7q]tM2#ce.7EpAOjfbR`CO]=\b#'+kNS"pYD>"p=]%rrN-$rrMWi!!<*"q>gBnpAbd+!WrH'!X8W1
#aR^U!!*0-"SVor!W<!#!<`Q-rW!0*%KICs[K$R2!!!&p!V?Bj!W3#u"8r8^!&"?W#m(*7N@H(]-l=i[
'H\//()7Mu(E"/2)AsD2*$$(@*#fh7)`B<+F*@Th'*nL:!s/W/!rDs#!!**%!rW/s!;$<i!!!'!!rW3&
!WiE"!!33(!WE'1!XoGJI'QmX9PI^X?<:N9=8c/)='8d9ASH"!rbi9gH%(<jFG=gLQ%o>C&I.J"rrE$!
quZg!rrW3$quH`tr;ls"nc1QT()S0ZeV9-AXes:HXLGC:Y,n\+Y->13Un4*T\&[(Zlgj`7i9JOlc)qTl
*";lJ!X8r:"9JE#rrN*#rrMcmrW*'$!Wr?%pAk3op&P'm&-)\4%0-DNRfE]o'Fb6M"Tn8q"9J]/!s/?#
#R)%]BiG]F#6Ff(!!<-%quZiupAk0nquZj"rrW3$qZ-NorrM]k)$UNP!<>$A/gMDO(G?mP,7#A.'bhAt
()Iec(]kQn*<$rl+!DRD/M/8=Rkt*X"T\T'!X8c/qZ-Hnq#LBpquZftqZ-WsrrW*#!<N<!!!*-(rW"SQ
!!WR#ZrgF2;H.F9=^=?s;c-Cj<E<4*?!q/RB4u$qDf^/MFEE%X?uWG8!##P3!!!&h!<3*"!r2ru!ri<!
!<3)t!WW8n!##J>'H1cALldmeRBiT_WK3pKS!s>G+Io!pTqnWi[CsQ*g#MA[k4%BC\`dE2+UeDP!!EW7
"9SQ&rrN$!rrMfnquQg!rW20^!W`?'rW!,7!X&K'#m1J;"9\8r!W`<'rW<H.!<E0#$PWR@`r,l@#6Y#-
"9eT(rrW3$p]16nr;us#rrW3$p&P*no)KO6(B=F<P]/&i-R'WH+!)@D&/#]n()7r,'GM8s()If*)B9b>
+s\9P+tG6(;3q7k!!r],!<rZ-qZ-NppAk3orW<'$r;lcq$3://!s8Z/!s8T*qZ%oD"98E'$NL/BZBnZi
@U3&-;Gg1g77^-K;,^Ir=^#!5?!h&PBFelrEccACG'e.AEMj*S!!i?#rW2QirrN-$rr`3&rW<3'!<N)u
#6=i,!WrN+!V?@B#lkPogW>V@WMH)EP`q5sLl..NNJi[ON0^3@\@K)V[CsZ1hW*hho@^ma%FljO#6t5/
!=9#7!s/N"!ri;p!<3)s!r`5`!!*0.rW!(12Zs*]rVus%!qZHm!W)p4"9o)5!!<H+"<YDZ"TT#9!!!0*
"8W*"!r`5r!<*#r!X&T,!W`>a!##VL"TT^".4QA^*ZGt:*?,n0',:E\!#5DG*#','(Dn#/*$$+E*uuLR
.PO;B:]LJ$!rr?*!s/<"quHctpAk3orW<'$r;lcq!W`<'rW<9+!s8T+qZ$Wu"TABT#6P2jW)R#'?WpE(
9hnAT6q0aA:/Fhf<E<1'>$PEEAnYprDfB`@I<'"<RpZ4!#l4Q!!V69l!<N<(!sAK)rW<3'!<N)urrN$!
!!2]l&HrR_=k/G!S#<!KOH#9[N.lubL*;8(K8,GUVQ[8.YHYORbh(e;oD.@`[a9^F%LE+8!=/l4q#gTt
!!2cnrrN'"rrW0#jT#Gg(_29##lFZ'!s8,qrrMuu('=[C!rr<%!!=:/+U.uV"onZ+!s/Q-r<*'$quQZp
rW2cqrrMrrm/Rb%#R(3TB-/?;*#TV5*#fb2'GLEZ#nmsb',)&p()Ikf)A=&1*#p+L-n[J]RfEHl!WW3&
!Wi9#quQEirrMuurW2iqrrN-$qu[!%!Wi3!!<E<%!&4N\$^H]H=]Sa.;G^(\8OZ!77S$-F9i"Vb<E<4+
?=@AUB5).!Ed<(UD/"C)":>D8qZ-TsquQKk"9AQ*!sAK)rW<3'!<N&trW3!"!!2]l!!3ZD,.P:>QC4J=
Q]d>cM1pT\JfoVpJV/fBR\H[XWiieFa3i`,p%mgq\$t3:(CC3D!<r`("TAN'!ri;q!<3)s!r`5^!!E<&
VCDlM!!**%!<N;p!<3)p!WW9#!!rfC"uW@[!"9,7rW*'%!sJT*r;ultquHZrq#^QsjT#et!%+$^.2<X9
(D[l,)&F"c'*8j]')iLI',)&p(E!)g$5sg%+!`*Y3^J]nqu?d"!s8E%rrW3$oDnjkquZiuq>gNrrrW'"
!<N<"!!**%rW")H!'.Je>YS1!<)?=_84Gp35sn%084lNL:Jk%k=^5<C@h*$\B5DR4I!'7IE3<CN#Q"K$
!Vulr!Vl`q!WN6#"9/N'!s/N)!Vufn!V?@(#RO>]KTh:ZSXPb(MMHn:J:INH(4CX^KoM@fTVJEdZb+-!
g#_f!k0CuO"5eJD%/p5."U,&-"o\Z(!s/N)!VZTo!W3#u!U9[b!WE'(!<<>I"onc,rW!!#!Wr#prrN*#
!s8W,!W)j"#7ge9SGiKm!<N9%!<NB&"8`/t!W<#r!W)rt!Ta:l#69*D0c(]A&eYin(`*o$r"K)CrXf;H
',))r(]G6S(Dn#.*W@/`4>LN5qu?m%!s8T*!W<'"!W<#m!<*#t!WW8r!<3*!!rN-$!Wi3!!<E9$!&+]]
P&=Z$;c6Li9hS&H69m^u5=%Y)7Rp$C:/Fhh=^>ED@Uit`Dg$DJCO^,_Z4I6;!!E<(!WrQ&!r`5s!!30%
!WW;t!s/N)!VZTm!VHFH$kTJ'O+WLVQ'78eLP12,I!^0cH[:!bI=d<;Q^aVCWNWeF`m`o6o&\6LZH1ZD
%K6>-"TAT)#6+l+"9\f/!WiDs!;uru!rW-"!:9dd!WN6#!!WT,2$a3a#Q+Q'!WiDt!;uru!r`9&!Wi6"
#lt,2"ona"S,ifl!!!&u"9/H%!WE0!!W<#q!W<)u!VHHe!!30&"9&92!XGGP-P@"%&.oQk(`!f!r"B#A
rX]eV&ebrn'c%T&)&X>2)]Tk@1H%ge+8l3=!s/N)!W<'"!V6<f!VZTo!W<)u!s&H(quH`urW"VX(VWpQ
8ki#T9M.iE69dRo4$5Yj5XIk.84lQO;H?t,?=.)LB5M[4FE)bSJ@dfFqZ$TsrW;s!rrW3$q>gNrrrW$!
!WiB'oDndiq#CR--.mU&JI73lOH,3QJUMihG5QJ$G'A4\KoD1\R\$:RYdV9ig?7kcg=sZ]jA6Bd!<**$
"o\]+"o\W-!s8T+!VZTg!U]pf!WE/u!!Wr6d/Xs_"T/9!!WN0!!;Z`q!r`9&!Wi3!#Qb&3"WA-"&H_n2
!<E9$!sAZ+!!*-!!rW0!!:p6W!!36+#5nN5+.5J+"q;"O&/,cp().Dp')iLC&H31@&.ofn&ebro(E"/3
)]BS3)^-Xm13?1i!!36*!s8H&rW3'#nGrFepAk0nquQs&!s/N%!!30&"9&9I#W'#06pO=98kDK?5s@@j
3&ioZ4$>en6:=:792AJe>$P?>?tF']DK9lEHA6L?CBX\?!W<!"!<N?!!s/N*!Vufr!WE/u"9/H&!V?Bg
!W)jO%7A[5GBnmuMMQq8H?XFMDf9N3E,]f;FaAUpNfoZpS>)sb[`$YPkih*ahR;$j&cr@D"9\f/"U>59
"oSQ,!s8T*!VZTh!Ug!k!<N?*!r`0*"TSc0Ym^s>"9&9#!W2rm!W<)u!s&H(qZ$j'#mV"Y?iUK2!!`N*
!WrK)!!!$"!W<)u!W<#j!UB^f!X8o6rW!F<E"s6"%1<OR&JQ#s'GLEW+V5.p%LimY&.oKe&ec$!*?Q:?
(DRf1,r%&HHN4-P"pG,,!<N<(!VZT[!;urr!WrN+!Wi6"'EJ:<!<<+HPXSMB8Oc-95sILn3&^an+Z;;?
4$>eo6UaO=:K(=t>$PBCB52=,I!gNmNM-CX#6b2.!!E<'!WiK&"9\f/!W`?!!<*#t!X8].!s/N)!V?Bl
!W<'$!<<-!!B^>dN3[AWJq\l0J:)T_E,B?(BP;*pCM[m-G(#%%Nf]HjS"Za`^!#'fkj%<h`PB,"%LWLE
!WiK0#6b;0"9\f/!W`>r!;QZl!;-<o!<WK.rW3K/!Wrre?j6c7!<<-$quH`trrW0#q?$Tt!<N<!!!WN0
"U#\QE;BP:!<WB(rW!!#!X&E'r;lltoE"F]qu@K6"pkP;!!&H<*YAnn$OI4Q',D;s&eY*S#S.CT%1E[U
%hS^P(D7K&+!MdG()%N,+s\okSH'!&#R1A2!<*!#!WiD]!;llo!WW9"!!E<*"U,)m!4>^%9MA)J5<V+j
3Ar]L0ekF>1c@9Q4$>eo6qC!J<*!+)>[V)TCNY&SH\QU_#Rq+H"T\T'!<E6'"8i9(!s/N)q>gNrquZm#
rrW3$oDf[.!<N<)!s&B%!X&]6#KUn4JVAi0HZsQ7E,0-!AH$$c@q9.`Bl%g8J;9#@NffTqTW#9:d+mgP
mGQNnkSk<J#mCA2":#/8qud-)!s/K(pAk!imJm[s"9el/"9nr."9>/,'E.t5!<N<"!!!&s!r;us!s&H(
q>^g&!sT8OaT)MG!W<!!!s8E$"T\Z,!s/Q&!W2ro!TsFt!XB);!!!(k,9.4'%LWRN%h]Qj&eY*Rrso&<
rX8f:%fHq=&Jc-#+!MdG(DI]++!E*YQQQJ:":,,1!W3!!!T=%T!W<*"!W<!4!<iT.#nsjB:J+5M6TdCi
2`3BG0E*R@0/,.;2)dNW5!VM-9i4hh='8j=AnlF8I1(@SG/>^7#m:J7!!*!"rWE-&"9S`-!<N#srrN$!
rr`9&rrM]k"9AN)!sJT''*A:>%NWi1H[pa$I<KUIBObFV?2e(R?!^lH@qKOuH@^a)MN*aaS"m4&bh2%E
n)i,roK3g!"pY20"9\u8"U+`*rrW3$pAk*llMq@p!sA],!sJ]*"TX_d%/g2+!W2p!!<WGp!WW8t!!rZ,
!Wif9Y5et3qu?a"!rN$"!WrQ)!rN)S!#>S@$j$D/+,hNh$k!IN#n%4T'+tlf%fHh@$k*LO$k3^G%il2n
'cJ,:*ul.7(`FD;,US+7!!3--"98H*!s/N)nGr(ZpAm_b!W`9%!<<*$#6=f10r[oG7n,p43]K#S1,(=3
.k3&"/1rS11Gq*P4[DP0:Jk"h='K*EC3"TGH%CII;ZR"$#m1/."9eN&!WiE(q#LEqquZm#rrW3$nc/am
!<WK(!"oA6!Y7H/E.<7bIX,sMAmeeE=8l5L<E<1'>$PHICiaoOJqf/CP*_cA]?&O^lgX2fWUjU1%Km%=
!!<N5"U"W'rrMioqZ6Bjo`,C%!s/H(!rr<("`+2Cp&G'orWDrtrW3!"!!2rsrW*3)!X]-P$4m"6!<WE$
!!E<)!s/Q%!V$0h!V69q!!!$"!!`u4!"_MB-QWa*$OI+I%1a$^%h/sE$RH,e$OdIS%hB3`'cA#7*uu:<
(`4,0.3i_K!!!'*"98K-"Tnf,iW/QN$31)-!!!',!!*+#30d6784>g-3&NKH0.e\'-mpAj-n6`!0/5:A
3^,o%9MSD^<*<R>C2nE>F,5C7GQ7^F#6Or-"pOi*rrW3$q>gKqquZm#rrW3$nGiUk!sJT'%g)e7$"U/X
I!g?gFDb_u<rc+s:B45j:FAt9;c[%.Ao2U7IY3H7O-?$1\&HePkO%KeVXB6M#7(P9!!EW7"9SN&!WiB'
pAk$jl2V.l!WW3$!rr<-$9[q\!!<*$rW<'#q>pHn$NU;1!<`W3#<tN["T/6#!s8B#!!3$"qZ66fr;lKi
"T\Z)!!Wo3!"WaO.NB$/$4.%I$k<gZ%1Dq<#R_%M%Ls![&JPHe*?Q@D*?,mq(Cr,A>E/[`"U+u.!s]#4
!Wh<]o)Ta0!!*-$!!3H,"9<ar:eXGJ4utSX0J4n+-RSd;(aULV.4Zu(1H.B\77p6J:Jt8"A86%(EGl>H
JV9<h!!WW0!!3B0!sAE%rrMoqrW2ourr`9&rrMTh!<WK(!#,J7"p0^LFEr:\F`;)(=AMIX7nH>O8Kpc$
:K(D'Ao2U7J;&i=OHuZI_9UfqlK.!&kGA^i%0Zb4"9Su:!s/B$rW2cop]9X[%06J0!!*-$!"C(`!!!&o
!!!*!"8i6#!VHF%!<WB("q1S@'n-,f!!E3#!<N<"!!!'!!r;rg!;uri!#Pb>!!!02!!*(S9J%.q$OI+I
$OdIS%1EUC#l=oP$4@7O%M''^'Gqf3*uu@A)&=)0,9KsS!<<B0"98N/"Te_n!;-?c!W)j6!WrE&!=8`2
!17Cs8Ol'.2`*3@.k)hl,Q&]3+sSB].4d/03Bff#8P;cR<*NdDCiFE9K7S?C!!!90"98K."Tni*!WN6$
!VcZo!W3!!"9&?%!WN2j!!*0)quAhc!iglsG'\=NCLpaJ7mK:(6:=4/6:+(08PN,d?tXA"I"R01NKTp9
]?&O[kiUX(l`Up&&-i7:!so/5quH`tqZ-9inGrCc!<NB&!!iZ,!"!ZL#64f!!!!'!"8i6"!VHF*!X&N(
"Ub;<&Y/n+!!iT*!!33!!!!'!!r;rg!;lli!!<9*!!!E0$31/.S3/GB&do!QrX8o=%1ERLr<N9,+peSa
$k3[W%hTKm*$64B*?5n3)^-%?:n@ml#RLY7!X8c.iW/ZQqZ$Wu"9&9,#QP/2Y#eOk76WOf1bp[6.4-;a
+<MXF*?H7D+X8<_/MT.F5t+:88ki2c?=[bfF*MnYG,5BC#mpk:!X8c/q#U9krW2`prW2Nh!<WN'!"o\C
_K:$CGB.M4@9-#d3&`i[4t&TX4?Pem6UsjL>%),bH@^a)M3"+([DL8Djlb1-l*D32&deaA!XAl"!;-B`
!<3)t!!30(#6"T."98o6_?:DM!WE'"!s8B#"9AT,!Wr6"rrD`m&H`1;!!<N-$PofD!rr]2!!!)t!!!'!
!r;rg!!E<'!WiDp!"f;9!!!$*!!<4u4=V*[$jd7Mr<r`8#m^G5'*\XG#7(SA$OdIS%hB6d(`XS<*>0>2
(`")9(aD&>%KHP>#64c."5s7V!VZQp!sJT'2$X*f!4Q!'5t!gm1,(7.-6s`V*?6":)B0V8*?QIP.PEV=
5!qb/84u`Y>@D/]F*VkQE2EsJ!!Ef<!!*6*!W<#t!VcZo!VZZo!V-3k!sST&3t)G?FE25@DeEQc;+3K!
0/>FG3&``R2`a,h7nlrfA8ZU@JqSo;QD:Xrak#>/gXF<]*t8Vh"onZ-!r`2o!;$<_!<3)t!"/f3#Qau+
"98E(ecP^K!<r])!!!'!!r;ri!"f><!WW</!!<Y'!!3--!WW3%qZ$TsrW;uurrMZj"9AN)!Whro!W`E-
rW#(d!!<5"5pR*X%1*@N%1EXQ#mUV:!sA`1"pP;<#mq(M%M'*_'Gqc1*ZQ.=(`+/:)^m#9'*/(F#QOl.
!pBX\!;cfj!!*0)rW#(c!!r\:=[kPA4#8QC.OHDa*ul4;(`4&+(`=53+<r9c1,h<]6UaL:9iG/#ASZ@3
EcQ/p$j-JC#lju/!rDrt!VcZn!VZZo!WN/l!!*3+quAee%aTB8Ble*$?Wg)f1Fah)0/G@<0JG4<3'9Mu
:KLq=FFA[kKSYe_Wj]mof\PNJXiht("VV+@!!E>p!;$<f!!!&s!<3)u!"8i/#7:P5!<`B&"kEeR!!<6-
"TeQ%!!3'#q>p6h%KQ\;!rrH1!!!(_#Qau2rVus#!W)ls!r2lf!!E<'!WiDq!!30("o\K("on`*&#h];
',:r_$4RCO$OR.D"9&?K!sAc2"pbMB$k3[W&/#]p*$-.@*#f_1)^61I/Z]Tf!"K/4!!ED_!;cfk!!30'
"TAB2"onr0\5YjY6TQtT/1;bs+W_U@(`!i$'GV>u(E+;;,q:Q*3^5nt77^-N=C5TREcuA:Kp`5N!"]A8
!<`K*quH`tq#L?opB(6no)Jdo#5eH;$k(C%BkML&@9cf(4>8*.-RgSs.Ocet,;1i34[Vh>>\A&&I=Hd#
O.</V_TpZ`hVl)`+Vk4o"onW,!qZKb!Vl]q!W2rs!W2p,!<i`1!!!$'!"%?^!!3#u!<r])!!!'!!r;ro
!;lg$!<i]1!!<N+!!J>h"TSc+!!*-%qZ-Wtq#U$d"9AN)!Whro!WiK.rW"ST!!<4s4!YLT%LEIN$OR4I
#6Y).!!**&"9eu7#RUqK%M'*`'c@u5*ZZ4>(`"#"+;uRgV@j"3#m(),"Tneb!;cfk!!30'"TAB8"onr0
Yu*kN6TQtS.OH;[)]9G,'E&Oe',2/t)]p:Q/Mf@L5XIk.9N,)%ASQ1+D.]2q"U+l7"98Q*"U"i,rW)ou
q#L<nq#^Hpo)Jgm"U=l)3t)A6DJ*R%C1(1A76)tH+sJ6W,9e<V-7LQ'3Bou/=_)DoH@1-lNLHcP_9C<V
g"=WZ*>Skj"98H,"8Mro!;-Ba!<*#r!!*0*r;[$1$Ob,^"UY,-!<WE$!!WH+!s/N)!WE-#!VHF&!<i]1
!!3B*!We8d$318/!!*-%qZ-Wtq#UHpo`,*q!<N<'p&G0q!X&]+!"B)3!<AEO+Vbb'$47.JrWrT0"8i-A
!WrQ/#7(YE%1Wm\&f)?)+!)FB)]0;,*ZZgmV%3_0"o\K'"U"ki!;ccn!VcWs!<E9*rW#+d!!`Lt<BiQ4
4#/B:,Te!D().An&.]9_&/#Wl)''kI/29(G5!VJ)9N,,'Anl4&DJPYs!!`K1!WW6*"TnK#q>gEoq?$Np
rW)Wl!WiN1qu@?9#.8G\Ao_Wn<_c"@/0l>Z*?G,!-6=<U.5!J?6VCHgCisuJH[gsAVmO7^c-Fnnb-;d#
"q1S6!XJr1oDnOboDngjqu?cu!<W6#$ipM<"cWWd"9nl,!!2rs!!3'$qZ6`uo`,I&"U>,0!X8W.#E&Zp
!!W?%!<N<!!<3,r!V-6g!VZQs!<N<+"o\K%"TAB$IKWFg()@G[$3^_B#RCS8qu@i?!WrT1#RUqK%hK<d
()e28*uu=?(DR`,+>c-O%0lk6rW!!'"9RQ_quQTnrW*'%!sJT'%gE"9!/FuE4@;1c/12V_)CQ@8&eGQ`
%1NdW&/#Zn)^$FV0JtmS5=.e4;d3^CC2@a+EKl%T#64u-!!<E/!s8E%!!<*"r;cZpqZ?Zro)Jjn!sT#.
!"fDAR<r4NEG8]X90bBd,9@a?rY>SP)&sbD,qC]05Y+g[BleHAG^YF9VR+%XaiW&d`2FCf"ptD3!so/5
g]76Qp&GC%!!<3l$NL/7#5A/u!WE2u!ri;t!;um-!X/f2!!*6'"r)Id'*8:8!!*-%qu?d!!Wr/unc8Rg
pAb<s!WrT0rW!B/!!!=&DAsB*%LNLL$2t22"TeK#(BFR?"pbPE%M'*`'GhZ/+<DL@(`!l(*X<rI98<r\
!!3'!!X&T+i;ifWq>gNrrW3*&"TAB_"TSN3=ar:k5<1GK-6X?G'bV#e$k*LO$k3[X',DK.,:P6%3BTMl
78$Q_?tO.jDfK]^DZBtA#6=f)"9\f.!Wi0"quHctq#UHrq>p6h"T\W+":#50!%Je!Qr[a6Am8,&4uFl:
*>]A#%hK?f(`X\H/i>d];-[aRFEMbQLR"X=]`,k[dalL$',Cf]"98N0"p+i(!!30$!94(X!VZR%!<`B&
!?O#s!!ri1q#CBqrWDuurrMio!s8`4"8r3("trLU%Kcb2!!*-%qu?d!!Wr/ur;cNkquQNl"9JZ."U4c'
#8SVE)&a"o$N:A2#QP#'!$21D"U>AC%M'-a'Gqc1+<DI='bqN(+Xf*RBb(=H"9&<#!TF+Z!<*#p!!!'!
!r`<$!'C>`!#[;V1HdcX0InFl)]'/!%L`^P#mq"I%1a'd)'0tM/Mf@J5!_S0;-7.9CN"35CReH."98`0
!!!*"!Vlf_!VZR#!!!$#!X&Z4#Qai'4<Z_j;IjEL=\hFJ1b9ml'b:ZZ$OmX](`jqQ1HS!#>@qeoFEMk_
PG#%g_o'=;d*H_H&d]'R!X&`3!Wi9#rW1pWrrMus!s&H'!"&c0!!!0(@fQQ6"o\Q"!!30&"8N#u!VcWt
!<WN2"TAB*!WuC8('as?!!*-%qu?d!!Wr/unGrOhpAb?t!WrQ/"oA9(%L\^H+:AMW$46V9!!N)t*WZ?H
#7:kL&.oQj(`XV@*Z5\+'c7u;/2;09'`\4:d/X4K!<W0$rW!W5!!!N>V`$n"1b^C)*ubt.%h/mQ,RF__
#n%.P&JZ0(+t"rt3'0;i77pEX?"IhmF)kZi2@9Ec$3^8,!!3'#r<*$#mK)q[#6=l."U55<!rN$<()snb
BOG.I9gUou/LDJP$jHk?$4RR_)^6^c3Z^X`=_2JjF*)Y[Oe/S^^qmb/`SF6)%1<aT"9\o3!r2lM!"o>8
!<<*#!<<<(RK*ft!<E6(!W2ot!VQTn!W)it!X&Q/#6b#+#6t6s!"fA<"9&9$!Wi3!!W`?(p]9mb!!2cn
"p"f/"9er0qu@!(!0o,_#m^nFr<NE/"Si$:!<WK1$4ICU&ebus*$6:D(_[Gp)B^@^1k$kj!rr<*!R^rK
!<W-#qu@?1!W\l\7kl_P.jQ5V((q,d$46\;+UJMb%h]Tp*?lj_1,h9Y5t+CB<a93QFEDP-Zkj2P!t,>1
!!!'#!rE*"!q-0^!!iT,!sAf5#RCP2!':5f$+!rQ>$4iu5rpkU-QNm."9Sf5$kO-l+Xf'*6V^cpD/jW=
H%_<NW3sCS]#_MB.iAU$'+G*J"U"Z(r;lfrhZ*`Z!sA])!!WN."TYqH)#aL;!WrK)r;Zfuo`G!krW!T5
!sJl3!<E0,!5edA":#,5!!!&s!!30&!q63j!U]ph!<NB&"98K!!!\-I+:\bh$N121"p=Z$*ruHI#7:kM
&/#Wk(E+86)AWnq(*4VF4[s]1%0-D4!SIJL!!**%qZH`r&HMk3O'=h+1Gg[1+WVC5%h/pF#pBWa%M09h
)BL+O/M]7H5!h_4;HI+8DfBQ;Cmt_7!!<N2qZ-Tsr<*$#mfE%\!s&H*"9\o6#RCP2!'LA`!2"@?>$+j"
5s.([-m'04"U##9%M9Hq+t59.6r$lqD/jZAI#!u[Wj][RZGsZ!)\<8_&.AaH"U"o0rW<'"f`2*T!sA]'
!!!$)!Djs?#Qk/1rW2osquQWqqZ6Zr!<E<$"9\`+!"a8O!!33+"TAH!!!30&!q-0X!!**%r<!$#qZ$s*
5'S1a%20-S"U5#3"9SE"+9;NH"U>AC%M06d'G_N')Aj2#%i?K6,Y;<R"TSN(!s-gM!W`?(r<!'%!W)j3
"%A)03AWZL-mToR'G1f`$OR4K$k=?j&eu6'+=/Hh1H.B[6UsjM=^Gc\CM&$KEruCB!<rZ(!!!&o!q66_
!!rZ,!WrQ/"pYA8qZ%`G;kI/q<EW'a4ukAJ+W(^r#RV"Q'Gql:.l9@X:g.CH'Q\JFJ;fqmXgl-RX2DoH
'*\^L%1<(=#6b54!s/N)!U]se!U]pl!<N?*!WiE%!!``7Du^CM#6OZ#quHp%!WrK*q>pNprW3-(#6=o/
!&kVj!!EH.!W`?!!!!'!!q66Y!!!&t!WW8u!!`u=SfSg`((L6H!X&T+qZ%f@!WrQ0#RUtM&.oNg'c%Q$
'b_,h)C?UR;1p\-!!!$$!<C[Nr;lp"rW<3'!Wi/u0FSGo2a',_1b0pu*#92!%L`aT%1a!_'c.f1+snfn
1cRT_6qC*T>@;2cARL"_3s>N_!<WE$!<3)t!r`8j!V?@!!<E6'!sAc2"pP2,!&Y?*^JA$6>#7XQ4>\T6
)\W\j%M9Em*$H[^2Es`1>@h\oH@LX3T;]!*^TaQIem9'l"pPA>rW`W3"U"o/!<Mfmq>gKqmJm7g!r`9&
!Wi6""sh#&#65&3o`,0s!<N<)!Wr6"qu@$(!<<<3!!Wn3$iL&-!sA]-qZ-WsrW;QimK!4e!!<-#qZ%',
%$i%](`<ee"9\f.!W2p-!<N?+"U55>$k<g\&ebrX'FPQe%hBX/,:?c`!sef*rW1[PrrDuuq?$Ztq>`/[
UcCe)5;t2D,p+!?'+bZa%hK?e'c.c/+XJQh0JtjR5t+CD=^>KOE+3()XUGC3!<3)u!9XCU!<*#u!WiH+
"9Sc1"9SH#2$+Z$9j:Y%;+O&<2_QO#(_[Mr()e29,UtN/6;(9`B5`!BKSu1lXL#OPXIm#P-Plac!sSu.
#6Y25!s/Mi!;ure!!WH*!WrN+!W<!&$?HFR!"&f"!<3)u!rE#r!!iT*!!Wl4$Qmdo!!<9)!s8?"!!3$"
n,_tXquQNl#6RAN(CM2q"TAH(!s/Q'!<E6(rWEQ3"U>AC%M'*_&JG'V&J5N_%NHrK.>1n/!!!$$!s8VV
!<*#q!r`5s!#5`8Shhrc4>895,9@a>'+kfh',;<#(`OJ<,Ub2s1,V'U6qL-Q>$bZQD.HY@C^^.@rrN&u
quHctmK)t\rW3!"r<!-)"9S`%!$D\SX[kib<D#\F3]&B6*Z5e4*$6@N-nR8=78?okBQ/8;K8YqaVm!J=
\Z:tCN$/T0!WiN0#6tM>"p>#0!UKgb!Up*g!<`H*!s8W&!!EG3!=K53!!36(!Vufh!W2p$!<N?*#Qb*(
4TGT`!!<6'!Wi3!rrN$!o`>!mnc8Ofq>^Krr;[95"0F'W*t\VU!!3<-"TAK'"T&?D#71bJ%hB3_&ebrm
%h&gT)_!^$R2->6!!*3,"TneX!<3)r!r`5r!%nWg^I9J=4>SQ<-6sZP()%>r(E",2*Zu[T.k`V62EF)n
9i>"q?=IS^Bi_J_'`A%2!VHEm!;urn!r`5o!<*$!!r2p!!Wi,t1(G#A<B48_9L_<23AN*1+!)OK,pt,n
0fVHj;HdODEd`b,S"m$h[C<HCOPE&I!<<*$rWWT4#R:P;!s/Mo!;cco!V-6h!WE-%!s/N&!!NE(f)PdU
r;Zp#"pG,'!<*!!!;cfq!"&c2!!!K9S,`ir!rW/t!<*#r!qlZm!WW9"!;HQk!Vud0!<N6$!<iZ4:43Wj
"UP51!XK&9rWNB."pYA3"U##9$OmUF%i,`j'bq5d$kX=$7V>p-"p+f*":,26!SIJP!<<3!!r`5r!&"?X
%pkJQ5;G5R-n-Vl*uPh0(`FD9+<i'Y.P<J52E*]a8l8\n>%)#P??(U6$jce3rrVclr;lQmp&P*nrrW*#
rW<*#rrDor0*`/&TKZ7E;G'5?5WLPK,pale/1iM12EaK(='fEQF+B7<UT(B'\Zhm5\!&*R"o\N$"pYA=
#6k>6!WhWf!!<*"nc8Of"p+i.!!!'(rVut,!;lg!!t,D<oDnjk('"=8!<N<&!!Nc2!!I4B!!39)!!!$#
quH`tq?$BlqZ?cup&P*nrW<*#q>_63!rr<)%KHYCW#?]W&Hi(9$OR.E#:9Z\#RCY>"pG5<$OmRU%hB6c
()IMh%i-$-=Gddm!"9&3"UYJ:!SIJQ!W)ru!VZR5#lkAS]f/;+68U,B0.J.d)&XA7+<i$V-Rp]&'Jq^,
3BT]'<Ei[2@VB+OI%MMa!!rQ(rrV`krrM`np&G-p!<W0$rrW0#q#D`F!"C*j6W6*M9gM*75;t;J/1iM1
1Gq*Q6:t-Z@:sJ$K92\'X/lW8\uM7-bsE?S$N:&)"pP;<#6k;5!p]jd!r`5k!;Z^"!WrE&#7pe6"2Y$<
!WE'$":Y_BoDnmlrW!K1!X&Z,!!a,:"VJi\&c`.:!rr<&!W2ot!Vlfl!Vult!VQKn!W<'"!Vl^5!<W?&
"UY;6!(;bU*t&2T#7(VC#mgkC#7(56*si8]$OdIS&/#Wk()IVq&K;`XI7OD>!"&o3"UPD9!W2rS!<3)t
!ri;p!&+WZ$3O>*01RrU0.ne),p=<M*ZlOM,pt,m/hf(=3'9Gq9iG.s>$Y]EEh$5=!!!6&!!*-%nc/^l
!<Voqp&GF#!WiH+"9S`-!<Mop0EM4]"^J5o>"qLV6pX%!2`*<H1c@<S4[DS5<Es$KEdEG$R\QaYWj&.u
c%%2U"U=r+rWNK1#6k>7!WhWf!WW9'rW2Bd'`e=:!s&B)#R:J4!1O&j!WW3%#R:M&!!!'!!XSr1!!!'4
!#.3rrW!*,!rr<&!W2rt!W)rm!Vult!Vl`q!<3)u!WW8r!"f85!<WK-!WWCU;A(8^%LE@GrX/]4rWa2E
$4I@Q$k!CN%MBKl()If))&OMP@#t9e#Qb27"9o)8!s.'TrrN$!!<E2o!&+HW#6bg/DDOs?1bC.)-mg/^
+<VgP-7LJt0/,+<3Boo'9i4nm>?bNKLoCX_!!*/g!<3)l!qlU#!<N<)!sA]-!Whup0E;(V"rEqY6XN8R
6U![u5!1kd3BKAh6qC$M=C,QUG(5:-Q(+A=TVJ9oe1)FK#6Ol)#m1;5"U5,5!s/Mh!<3-"!UKdg!<E6&
qZ$g%C+92g!!!-%!s/N)qZ$TsrW<*#rW!*&!s8T+!WE'$$P,5;rW!!#"9\W(qZ-*dq#^QspAk3or;ls"
pAc$2!X/c.!#5taT0!#j#6thN#n%.K#6kD>+Uenp&Io0U$P*sj(DIf5+sA3\0TnU#!!!'+#R1J:"9JVW
!<3)u!ri;p!"o>9!!"#X0==h&3[cC2/gi"p-2o(i,q(;B0*Esd3^ZLI8Ou]_>$>0;>I%-7rVus%"7?-h
!V?En!VZR#!<E6'!s8Z.!Whil-lj<c^LT#m4?Z/%5X@_%5!D4u7S?NU='K'FE-m:nLQS'pR@0D%h0'>W
&I8LA!<<*#!WrQ/"Tnf,l2^hcrW23_rW2uu":"tY"pt8/":,&/!!<*!"p"c."U"l-rW!*("T\T+$N:#.
!<ASk"TAB'"pG)0rW)fqncAOfrrMiorrN'"!!2cn3!'3d!Wi?7!*#<k'H.N&'+,'U$3pb?$4[[`'+YKX
$P+!m(D@oC/hK@LNGeh%!!!'-$3p_:!WhupirK)[r;ls"p&H]G!sJc2!#l/SX<9,R/NGO7.P*"p,U=`e
0/>:;0JPIJ7SZNE;I<d:De#u+&.SU=!X8f0n,WIhrrW0%rrW-#rW2`nrrN-$r<!'%!V6:E!rs>MD7D5`
83p$C6Uj[=77B[;9i>%r?!h,XFF]7'K8uCfPG45nW\#G&"Tno1r;[!%!sJf0!U0Ua!r`5a!!30("o\KL
!XSk"":P87%Kc\2!s&B%!<N?+"U"o/!<<*&"onW-&I/:E#/:ufr;Zp("p4o)!<3)k!;urr!r`<%!VcZo
!W<'"!VHEn!X&E%-NX8QBoatX.2*7'%h8pO"9Si9%h]E_#mUbF%MBX$,q:;o6][68(B+:=":#,6!s/K(
fDtpPr<!!"rrDfo/-?"V!!!<*&pL!;,XO.:0etO=/1Dts/i#=C2)I0N5!qh8;,p[q;eE//*$G4\!WiK+
mf<@grrW0%quZftpAk3orrW-$!<N;o!<)sL#lkclXAh&X7nHHR<E)gk:Jk.s?XdS[Cik&VLlIIWNeW.J
e&F=)%g`CA!rN$%!<WH-!WhNcrrW0#k5Ynl"98E)#QOuI8e_F/!t>G7!W<#t!WE'3!<E6&!<WE*!!!0&
!%25n%KHS0!!39*!W<#s!V?Bj!W<)u"9/Ds!<*#t!WW8o!!**%rW!Q7!!!Im<&6NX&Jl&i$O?k9":,nS
%LiaM"pYG=#TG<D-9Oh)RfETl(CL9G"9\K$g&V-Rr<!!"p&Gp2"98E&#QP&CSmk,a4>8fV3&WTI/MAn=
rAk*D5!hM#;@[&8:LIgYXpP[>(^g<D!Vucr!VQKp!<E9""8r<"!VZTo!WN6"!s&H(nGjsC!!sUBDcL=I
9j:n1?X?r>>@1oSCN"9<IY<E0Pb!qhNfTRN+X-q3!>5P2!!E?+!s/Mf!<3-"!TsFo!<N<*#n6q=%p/l;
#RLhF"TAB&!<WB#!!WH+"9\c+!r`0-!X(3d&c_n?"98E&qu?`u!ri?%!VHHl!W3#t"9/Dt!;urs!ri;o
!!E<&!!*0#!!Wh#J.<;7#Q>)H#mLM:$4RLR#RCbF$j[1U-R:<.CR>P0!!Wl="9S`-!W<#t!VcZU!<*#u
!r`5q!!WH+"9JQ*"9&9C%\o",/j([B3]oJa2`a)f6U<q'7S$0A85EAa;Hn^M(&e19$jQh7!Vufr!VZQq
!<N?#"9/H&!rW/p!<*$!!rW3&!W`>m!!!'!!%&G`SM`oA:L7XIC1q3nD/jZ?G^bC+OcPTgR"p<IUVS>b
#m_.O"8Mp"!WrN+!U0Ua!r`3#!U0S$!<N?+"9o)2!WWsQ=qV,E'F=a>!X/f3!W<!2!s],="9So>#QP&P
O9Q3q!"&r+!!NB)!s8T*o`4slr;um!rrMoqrW3!"rrW3$oDgTI!s&B,%0-A=>_OXI,8:=f%1<FK%1a!Y
#n.=U&.TBj0Ju.<Jfk3s%0ut9"U"o/!W<!#!<N9&g]7<SrW;osrr=kU!!*-("U,#0!!N]0!"rk-5WVD!
2EO5k5XIn18Ol3@:/=Y[:eb;%@#C'o"oo#8!!!'%q#LBpp](?r!Wr9%r;uoup]19orrW-$!WiB'nGiOl
-jfqU*-A,_=_h\\C3"?6F*;eTI"$g1PEqN&OdqPnY,sc!!>,Y?!<Mur"T\]-!W`>e!<3-!!U9Xh!<WH.
"9S`(!!iT5!3Q;2$NL/1!!NW8#6Ol)'`eLG$k*FK!!aPFKg,PG!#5kD!WrN%!!**%rW<3'!WhuprW2s!
qucs"q>gHpquZiuoDf@%!!!$%#7^_P40E0/!Y#&7#7CnH$k3a]%i,Tj+t+Q\&o4%I('"=9!sAW+!s8T+
!WE'%!<E6&!Sd\S!WE/s!W<!%!<N?+"9\T&*s2lN+@j4r0d\e:3''2e5X@e.8k)3D='SU"3/P"`+8l0A
!<<*#q#L?op](?r!Wr9%r;uoup]1<prW<$#!WiE(mf4U;&-sjjesTB-?!h#OBPD3tDg$MTI#4,XOGn"a
g6"<%#R1D7qZ-No"T\]-!W`>e!<3-!!U9Xh!<WH."U"o(!"/i8\gIX]!!a&C!s/?#"9AQ,%heg@$m;u6
%0-tH#mLP9!s/<"#6=l."9S`-!VQNm!W<)t"9&>u!;urr!r`5g!%J*W"s+CsUIYIk)]04u$4.(U*ubq-
'/276NK#b%!!N`4!!!'%!<N<'!WE'%!<E6&!V?BV!<*#t!rE#s!!NB)!s8T*qZ%]C#ppaH\mls65s[[r
3&s)j:.[`74&o<nVP-Bm"U583!!!&o!;urn!!30&!rN0!!r`3#!VcZp!WE0!"9/H&!Ug"6"qMG+0ppF>
6:kWq?sQu@?Yjn,DJX-ELm??,@kJW6'*eL;!quZu!<WE*!<MHcrrW-"r;c6c#6=o0"U,#3!r`0-!t#M<
!->OJ!"B;?r;[T8!WW6&"9\c+#EH%h'`\C=!rrH0"p=c'#QXu.!sA].!WhuprW2s!qucp!qZ-QqqZ?cu
mf3Fk":582!#I>[T4&EH+<i$R*uZ"<-ndhPMmRR+%1`78!<E8s!WN6$!Sd\S!W<)n!WN6$!rDs!!=/o/
!#Io)[<jS_6V'jC8jkp38PNDlT>Z9\'bg':r;lZn!W`?(qucm!r;lZnrrN*#r<*'$rrMTh!s8c>&L%Vh
&5pHiP"82M@:a%^@:!GZE.<>TkFiVC.0p:f"TSN(!VcWu!<WE*!<MHcrrW-"l2V%j!sJl4"9S`)!"Au6
$NLP;!1/cl"p#5A(^1-P$47:Y!!3@9dNA\o!WW?'!s&T4#6Xl(#QXu/!sA].!WhuprW2s!qucp!qZ-Qq
qZ?cun,O@.!Wr]:#mUe;!AnqrHpTJ4+!)OR4&g`uN&Ck?!#>P7&Hhq2pAt9qrrLmTrW2s!p&Y-orrMus
*X3#\$P<[S6AE+;?;=$Z6UXLJCm:lb4TPO#!!!W6r;Ziu!Vl`n!VcWr!<N?#"8r<"!VcZp!WE0!"9/H&
!V-4=!<WH0%M]]o*>TPiQ-6%D?s?]7=^Q*$Xhq>E)@eD3&L%ee!!36)!VcWu!WrK*!<MHcrrW-"l2V%j
"9eu5"9JW'!WrH+#6Ol)"Te[gi.r$D!#,J;)J6\A!rr<,!!!<-!!!0.#mUS1!!iT,!sA`/!s/N$!;ccq
!W<)t"9&>u!;urq!ri;j!!NB)":,>8r;[B9#7`b,J<,kUQ^<VP6P]Y2rW!$$#S."7!;HTo!ri;i!:Bjd
!W<)m!<N<(!W)j!!<ri4rW!N5'c%ofJXs!P[CEW@M,PT!&H2Y3!=')8qu?]tq#L<np](?r!Wr9%r;uou
p]1<prW<$#rrW3$nGj^6"UGSN$jd1D%j</L?')2(`lH9E\XmIo(aft)'+u-&%fQG0!<WAt!<!!!!U9[b
!rW/t!:Tt7!<NB-"pG,3!<N<'!!N]7"TSN0!!*35-!chE_RQ+P3=Gm*!!3#u#RLS5!!<H5#6Xl(#Qb)1
"9\f/!WhuprW2s!qucp!qZ-QqqZ6g"!<DTh!s/W3#lO`'!qH<s"TSN)":YnO!rN&n!WE0#!Sd\S!W<)m
!WN3$!W)j<!X/f0!!!00#m:55%LE:M)]05%&Hr.B!!*-'$kEdD!!!&q!;llm!!30&!rN0!!rW/p!<3*!
!rW6$!ri;k!!NB,#n7CP'EnaQ'bq8g'ce/-+Y5,j-RK`@+V4Pf"!/O&%K-8-!s//sr<!!"l2^hcr;l3a
)?BmB"U5,5!s/K(!!!66$j[1J#6b>C%13:A!<`N(!!Nc9!!!K0rW!6-#Qk&,!XB&<"8i-#!WrQ("9JZ,
!VQNm!W<)t"+U~>

%%EndBinary
grestore
np
grestore
gsave
44.6254 410.531 mo
86.5824 410.531 li
86.5824 353.277 li
44.6254 353.277 li
cp
clp
44.59 353.19 mo
86.61 353.19 li
86.61 410.61 li
44.59 410.61 li
cp
/0 /CSA get_res setcolorspace
gsave
clp
[1 0 0 -1 0 570 ]ct
[42.02 0 0 -57.42 44.59 216.81 ]ct
snap_to_device
Adobe_AGM_Image/AGMIMG_fl cf /ASCII85Decode fl /RunLengthDecode filter ddf
<<
/T 1
/W 116 
/H 159 
/M[116 0 0 -159 0 159 ]
/BC 8 
/I true
/D[0 1 0 1 0 1 0 1 ]
/DS [
[AGMIMG_fl 116 string /rs cvx /pop cvx] cvx
[AGMIMG_fl 116 string /rs cvx /pop cvx] cvx
[AGMIMG_fl 116 string /rs cvx /pop cvx] cvx
[AGMIMG_fl 116 string /rs cvx /pop cvx] cvx
]
/O 3
>>
%%BeginBinary: 1
img
jT#Da!WiH+o`PL'"U5/7"9S]%!#YhA"U#&9!!!*2&f2/c"U,8G&.]Eh&ISpOqu@$-!rr<&"UGA;!r`3"
!UBa_!;?Nn!rE*"!ri;i!!WK,"9SZ+!r`0&$4dg^"n;R!#nRII!W`<'!Wi9#"9AT."9S>urr`6%rrMZj
q#LEqrrW0#lMq=r#RUtN&I&4<$k3^Pn,O()%1*+="UGJC#Qt//!s8Z.!Wi9#quQTnncAIbqZ-EmmJmIq
"U"i/!WiT)!!WT2"p+c+"9&9%%LN=8!!<9)!WgjPrrN-$rWE0'rr`6%rrWN0"9eu6"Tnf,q#D96"U>88
!!3?4%L<FQ)DtN;ML]D>4=V9`%/g/+!W<#t!W2ot!TF+U!W3$!"9&B%!V$0f!!E<("9er,!!*-)rW!?2
*B7#1=[Fb^&I8RFrW!!#"TnT%!!3'!"9JZ.!s85trr`6%rrMBbq>oj]"To#=%hB!I!Vl^'(Go!#=[Ok`
&-`4<r;[0,!<<3)"U5,4!Wr<&!!;orq#L!emf<1bnc/gp!WW6$!WE'&('ss@&HMe1$N^D4!W`E($31&-
"oA9%!<N9&f)YdNrW<'$!<N<$!!rZ-!sAc3"p=u.rW)s!qu@T;"pYGB"qhpc,&sdEj42&T^<PKn_3.kI
"p5nV"9R$Pq>pEo!!2forrMusrrN&u*!$6K#6k;2!snr4;2VlmV3$1]Pc1jQD)`"*&Hqk/!<<0!!r`5r
!;lot!U0U_!VcWt!<N?*!VQL4!XK/A$3pP5#QOs$L:+@^Ndc\HVm)D"1^O-hqu?]trW!!#!Wr?'qZ6a!
quQQmp&X@WrW2Wk"9AZ2#6Ol)&-`+;!%b%bBKdFn>a)L:-5$1V"9Jc1"9SN%!W`?(mJuJOrW2s!!!2rs
#6=l/"U527!r`0%!<WE*qZ%Z=$P!mZ-]m&bSqDWIF(]]QH#AJ=c-sNo.ME%#&-;G(rW2Wkr;lfrq>g*f
q>^["!WrQ/!rDut!W2p?!X&c4"98[@XEnDH5s?e>/3P^;8ogAuS0/@C!!ir7!W<!#"9S]+rW)ouqZ-Nq
r;l?en,NUm!sAc3"7lL7!X8`/!!d5>HXoT34XqC#4"_mMD3UZW(^pBE&ebHMr;[$)"9S]+!Wr?'rrW-"
o`4jimf3@h!;QWo!VZR/!X&Q)":"r-!!302i&2>Z(B=F9"pk2.$l*Htf`2<i!<<6.!Wr?$!<WE#!!!&S
!;lln!!E?*"9o&2"9SQ&"p+o2"9JW*rW!uB!#-l8goQ$MEcc8>KU%FBK84DNB8*GRc#FO2*!c0;!!3'#
!!2cnq>p<jquQ<f"p+l1"pY83quH]s!!<3'rW"&F!!NsCY&ur],U+0F.QT4,.l8C^,=ZddUJ:dh&I&ID
rW!!("TnW&!W`?'qZ-Kpr;kgV#6=o0"pYD;!q?6m%:?8^(dg)-,oddO2_#dm//\d54DD$l:]h"B#mL8-
!X/].rW*!#rWE9)!Wh'V!s&E(!Vl`o!W2p9!<E0#"q(M5!!NB2!!.9X!WW3&#S.:H!s/W+#Q4W/#&mZS
!"]SH"pY&,!<`N&!;HTF!!E?*!s&E#!<WB*!s88u)](-FhJRseH[UL"Lk^S<Ljs]/SsG4SH$dlo4p)6J
$Np,'rW2]mq#U3irrMNf!!E3'rW<-%rW2`n*srgXY;8<c+s8*W-mg5h/LD]%:.[`)4@Z*X,lf;!#6"T)
"U"l,rW)ouqZ-Wsq?$Zti;`u^"9er3rW<6(!<N>r!$2T=X>E0k.OQSj,p40J*YoD<5<C\I0fY;n%KI@H
!r`0-"U+u1!WiH+"9S]+rW(jV!W`<'rW<0&!W2rs!VQKo!s\](!sSmA?2=O&!<WE#!"&c/!!!FMGQ7^J
"TAB(!<WH,!W2ro!VZTV!!NB)!s/K(rW3'#rW!-'!WiH,"9SK$.0]hm9C90"IpRGJH?OXdK7\AhH@pm%
I!9^OF'XXdYTjc!!WiH-!s&Gl!<*$!!r`5r!:'Uh!<WH,!<<0""9JZ-!Vl^<%5c4`.l[nV'bLli*?laM
)C-ph/h8>!-T!5X`g.,;&H2Y1"9\W(p&P$lqZ6`uli?n_$NU;1!<N?,"U"i+!rW9'"9S>u&LG/A-o___
*Z,J&()@Pj!XfeB(^qB&*X4?_C]FGH!!!)t"TAK(!Wh-XrW*<,!sAc2"9S]+!<3'!!Ug!n#GO3Y$31&.
rW)s$q?%?5#64r@$36_Y!"&]+"9\f0"9SH#rrN'"g].N\"U>89!s8H&rW!$&!<<,t!#l"G$kasFhj7;p
J9P^bKR\Q+Jq/5oI"6j&IsV*D%WlQ<b/%$h!sAi<"onW)nGrRir<!!"k5Ynl!W`9$!<WH+!!<H/pAb6t
(EFR2C)T2c(B>6`%hos)+X89]/1rS*,qCT)0euLrSN$KI!!N9$!<WDt!;urq!ri;b!"T)4"U5,4!sAc2
!WW?."Te>t$j$[7>7`bF*![Z*&J,Tf%LWID#7D%T&.TKq+;u.UMi]Xk!!ri3!!3B0!s/N)h#ITZ!<N?+
"o\]-"U"o+!WE'!!rW8u!"8l@"T\Ue%1ECD!!*3"!!iT,!s8T+!s8Z2!!!0+!!$1oqu?d%!s/2t!!<*$
qZ-TrjT#bm"pkVB"Tnc,!WW3%"TnZ'(^^up)%6j-BX-TGCgUdqKTC\<Lk^M4It.HH%XibTJ9l?bJ8&(g
Rb(:L"t:)q"TSN)nGrRir;us!kl;.n"9el/!<<0(!s/W1!r`0O!t,PH!!"$9QGQKU)\s2/*!Zlc()\/<
.5!5(.46Ml+WVm`*toZ+X!n#[!!<-"!<`N(!;HQn!W)ou!U'Ln!<i]7#R(>5"9el/"U>//!#>_I$jQb4
%6T-?4<tIL(*Fn9',1uc$2t/K"pG/7#RUb>(+C@F,\a;+!"],6!!!$*#6P#.q>fRV$ipA1!X&Z2"pY>:
"U+f+$ig8.":,>?"onW+#Qju*$3gKF`"rCR#R1M9q>^[#!sA]-!W2p*"98T*'USq%$NLD4p](<r"9&H#
!<*$!!9O80!WrQ/"pYA7!!392&Io-V%gN@g=g%>HWJ[-E?X.GiJqei0L4t5/IJeI*I=Hj"Isc^!Kk#7R
cCQ!b-PZdQ!<3)u!r`5r!:^$u!<N<*"U5/4!!*-+$O-G./.F_'d^4^;DBU/:)Aa>.$kO0l*$?LU/M&A!
,pjub+sJEl3Z^4LSok#5&dRn+rrMuu!!2`m!!2lqqu@0-!sAf5#R:G3!<NN8#Q=`B!!!KiM9)Q79i_Z6
#8.^j)\Wl!&If'Q#6tJ4"W.LP$4IOi1Hm!C7@S>u!#,b?!!EE,!s/M]!!<6'!X&B("9S`/"9\T("T\W(
!s8W(!"oSB!"/c,?-nri(CpoS#7:Y@!r;m#!<WH-!s8?""pPA6'aW&1oDf!q!s8Z/q>gNrn,WFgo`,F%
#7:kD!XB/C%2^E=1`(_ef?'k;>>\1p>[V#]G'\OcJV&H'I=(s='mb4SIY!0,Jp_WUE->9/nr+_4%1NC-
!<3*"!rW/^!#PkG$O[(;!<`B&!t5DG=eD^_G"aA-*-35J*>]e:(_dVu)BBqF,q(5m-mg2b,pjuc+rqUJ
0,6df@/pB0"8r3$!WiDt!<*#s!ri;q!;lli!$_UP$O[%:!<iK(#8%C]@&L/sE^UrZ#[IiI#o+0j'GV>s
'+c,n$OI(E#6tMA%1s9i(DRZ,/.t.\@/pH2"p+c*rW<-%m/[+dpAc$3!sAc3"p=u.!!!$"!!*0'!<`Q/
!WW<+r;[=:GZ,Fe!<i]8!!EK4#mU2*"T\Z,"9\i+!;lg&#n[@AK)bl["8Dir!rW5b!!NB)!WrK)pAd2U
$46k9!"^Cb!%`!"o"f`_<F'BUG&bB9BP2I1G'JFaIXQWjG^"=SG^4XaIt<3'IW8q@I;EP@hZQ%a'GL]=
!;QZf!<3)r!($\d!!*92%LW=<!!Eu9!"),S]n\cp'HAVS2_ot6*uQ:E)AsJ7+!DmU-7:2h-6sf[+X/*T
+r:b5/g;N'XV1^8#lO`)!X&Q)!VcZo!WE0"!VZTo!W<'"!VZQr!XB)>rW"&D'EA+D9:!S[7jo2n-6al^
D\`ik(DRVu(`*r&'+k]`r!O>M%M9?i(C^Tf.30NlX:kX8$NgA/!X&W.p&OmgquQTn#QXu0"pYD>"TnQ$
*<ZZT#QOi."pbS="HpQ"!!!'#'+"dK&.J[F#mUP,!!WH*!WrK*!W<!'!<<-#!!<50o`,!n!r`;l!;QU!
!<N?+"9S]"!$M@K%134R(CMO1^<![18kr`*C1^p\B5"npF)Q5CEcueVrd#K-G'.nLG'J=[I!g?jIt`]'
DKM7cUA#NJ)@HECrrM`lq>p3g!W`?'qZ%uF!!!*/%hT-K%1*"C;ja#(63dZ+(E=8,&fi'7,psf]+<;OK
,:"T6-5RsS,U4HT*ZZ4@+=Jfa(a;X+Bup>\%0le3!s8]/!VZTn!WN6#!VZQq!<E9$!rrDu!%@mJ"UY\C
!"&u3%9B!lLIr-i*$6:@&df6_@1sCg(_dSu)B'G/()7Jpr=Ai<'bM)p*[DR7*ChSl`rHAT#Qb#."9enr
!<3*!!WW8s!!iT-"9o):#R(8+!!`]<%1NLU!tGD<C6'P;!"B,;#Qt,-!WrQ-!<ri5o`,*q!<N?+r<3T4
"9JZ*%MAi2!!i]0q>^Krr;u6a#6=i,!s8Z-!VcX.!WrH'$OK%i_5i#h6;:cn?!UcQ$[HQ(CVOh/DK^&>
Fo6P(H$=FSFa&(VH@(!dI!pU"I<0"7A#&%#+:o%]!!*-%o)SRep&P'mq#CKt!s8W'!#R,;TS-/j#RqXc
%L`gd.30BLE[)hN,p=<?+XSQ`-R^>h,U4KV+<MXErYlLk,:F]S&JuL#Yt,*#$3L;/!X/]!!;HTk!<*!!
!r`9%!q?78."n:L<%JLm+<)%-%iQ].&J&:^'+Pcj&/?*%)&aA0(DRVtq%FDU)BK_-#S@e\X[NEq$O-_7
!sJer!!`N*!WiH+!Wi)s"p"f/"U>88qZ$s)!WWuE!!"j?8.#7qrs8T(!W`9$rW33*!sSu4oDeso!WrQ%
":>/0!"8i/EWuLJ"8W#t!WE/d!!!'!!r`9%!WE'S!WrE&"UkeH&./n>W5sci4[)SH>?,$EBOt^b@;Khs
DfBN7EGorEH?spbH?j^XGBeE3H4P@KH@:<gFGZE:BpZd_#7ge:rVus#!Ug$d!VQKn!WE'J!<N?'!!*<.
!!<3$15r,A,S(7u,8q.0*?,e0'bMB*E$$/@,Tn0R-n5-D$77#B+<M[H*?6";rYcCj+rhIT7Q2f-Sd,6&
#6Y#."p=c'q>g-grrDuu"9JW,!s/B$rrN*!,Qn/K!<<*SN2U;7&IfR'*>BA5)\`hm#7h;O%LrgZ&.T?k
)B8Yq!?)jT)#b?N().Gr()RVn-9Ee'?C:rs$jd+<!sShs!!<3%!<W6&!WiE(q#CR!!WrQ/!rN$3!<`E'
!!HEc%g)q7"pG)/!<`Q/rW!0)!<<3*"U"o"!;urr!Y#57!!!')!<Wfl!!N?'r;Zj!!;lla!!30&!r`9r
!WiB&!!*3,"pkYD"q2)7[]XOA4@)8%92SYi>[LfD@V91dDo-L4C3"93F*MtVH[L0dH$FRZH$Xa]G^+L[
I=HTgJVJDgGh=#L"p=i)rr_Zhr;lKi!!*-&"9\K#.kI!E80JHS%1Nj^'GM<!'b_<"',qs2*Zc1C+<Vs[
.k2tr-6jWS*?6%<)ZCTg)B0_@*?6F^/MKSs!<N9,!<<0+"S;]_!W<'"!WE*!!r;ls/-qT$8g=lZ%Ls*M
',_Ju&.AsW#7V/M%1EIQ%Lj'h)]Tn@+!)IDrYudp)AsA/()7T$&e>m++=0.L!!*--"98N/"7Z?t!<E6'
!s8Z.!Whro!W`?(r;[04%0-j=L&_8T!"8c+!!3-$qZ$j&"9er5"p>#,!WN6#!W)lr!W<!"!<WK(!"8u1
!XEfI"TSf0!!!'!!;urb!!**%r<!r>!W`9$!X8r@((_N85GuhP4\&7B92Sel<)rlt#$>5F@r$#$$#slt
E,KQ7G^4W7Hi\S?rcnisH$OXYG'J=\IXM-?#B5!!fbbb1!r`0%"U"i,n,W@eo`,$o!<W6'%gN(?%3L8%
:(S3\(_[]*)?(?b'G:rg'cIc)*,lr>(a'qE-S-eu.1%CK+s%^C)B'J2rYQ@f)]g+C*?HFN3A.N9%0-P3
!!3E0!V?Bg!WN5r!AOWW!<E0#!<N?+#QP/A,)3-q&fMf0'c7o-'+kcb$4$hC%L*:M?k!JI%1E[Y(`OJ;
r?2@f+<M[H*?5h5)&O/,(D@;i',<&CVuR2*#6=f+#6aPs#lt&.!WrQ.!s/Mq!#5P>#7LY:&-+))!!!E-
!!il>"p"c,qZ%*."pbM@"TeZ(!WrQ.!s8H&p&G-p!sJT'!<W</!">e+"TT#9!!!&]!&XcY!sAZ+!sAZ*
!sJo@"q;7dNp:j4-Vm8q6qpQZ;GU.h<``C,@;'.dDo?X6BQ%d+Ed)eSrd4Zkr-8p"GB\4SH$apbG^"CM
G%9GJ(^0d;!!N?*rW2KgrW2]m"p+c)!WrK/rW"DKDoPTR!$2gX$P=*h'+YZg',2&l()mo))f?Z8(EXbC
-S-eu.46Aa*?4tqq\U"b)]]k9*$HF]/[k]c!!<3$!XJu2quHKlpAt6n$ipA1!<<-&!!!$$!=&N'%Kg^l
;ZHe@(C(?]'bq;grX9JK#R1VG"q(iH$jm+G$k3gd)]^"Cr#m"%+<MXF)]BS1()7Ai$kX(!,Hq.P!!NB'
!sf&!!<3*"!r`9&!Whon!<NH(!!<<B^^U)?!s/T1!r)a,!sJl6"pG&.!!36*"9S]+!V??m!X&E%$j6P1
$EX:3!"K/4!!2orrW2Ee2us*a!W`E/"9AZ5"W%pm5LYic69@V076j@>;,C"^:fCG">[:fQ@r$##E,K?-
DJjK=G^+L[H$T72rHA]qH$X[WGC+1IC?-9E%/g2+"T8Aa!!iT*!!*3'!!*3V!"/u7-FRq9(_.8u%gNLU
&eGK\%1j3h'bhH'',VX))]BJ6+!E!_/1N%o,9ImD)?(KM(D@W'(D[r6*\T=\!!!6)!!!*,"Te,nqZ6Qo
"T\Z)!!*6%!"/l/$O-e_[r`c3&/QH.&I8gZ&Io-R#RUtL$OI1N"q(iG$OHqE$k3jf)]Tn@q]He!*Zc=A
)]0>)'+G9W'+cB;ZN't2"9JQ*#R'SrrrN'"rrMoq!W`9$rW*9)(^UY90)tt_o`4jh!<E<$":5)/!!*-'
!s/K(o)SdlrW!?3!!!7u!!N?2"98E&rW)s!rrDuumf4j=!X&T-"UG>;%2Kim&:rb;6S:,Q5t=C69iFtg
:f(%i=^><>@qfIhDo-H!DJ*m)DK9rGGQ)jaG5um`G7&J5FE_VGCZ-*@%K-8-"9\N%lMrgD!WrK)!sA]+
"Ukh?!,0;+*sMoT&/#H]&/5ci%Lip]'c7]#(E*r()Jg<1'cnG>-7gYr-6ra<*ZQ%7)#>'J((h5o(EX\S
1q*Gb#Qau+!sf&2jT%1>!W`9&!s/H+$k31:BuMnP#RCbL'FtWa'G:l`#mgtK%h&dR%L*:L?4.)C$k*RY
)&jM7*?P,#rZ;(['cRu)'+kTX$4mds/$T'S#m:;0":#%r!;llo!"T)3!WrK("on])!Sm_U$j?J.!s/Q,
!qlU"!<N<)!W`9%!WE0#!V-3q!<E0#!=/Z*#m?Xr!<<K1!!!'!!;HT`!&=TX"9f#:$P!I]&1#Sg1H?p<
4A&%,7o3/c<E)mq<**7/?!_#S@r#u!Df'-)D/F<;GPlXaFoHR]G7A_=F`VPCF`2S@h%^G.r;Zj$"8`,c
!!NB)!sA`/rWG+_!"Ao>[sSl*"9f8R&df*_()@Ss&J,Ng(E"#((E4#))Jg<0'cnD=-7^Pn,pFEO)]9J/
(Dcrc'G_Dt'G:ul*$@0rZ2ak0!rr<'#R1)*rrN*!mJo0H!<<-%!sAT5!"l_h()I/[&0)>j%MTWm&e>EZ
$OdLV%13LS#7M&K$jm+H$k3jf)B'P6*$$(!*rI#n*#KD'&.8^K%hpTHXT/>-"p4i.#6X8lp](a(!WrN-
"TSr2!7aaW$N1#(!!EE3#Qt5&!;6Hc!<3)s!"&`4!!!%["98E/"8`)s!WN6#!Ug!g!WE-S"ptJ5!"qE)
BKJOB2).0a76sIA<*!!t;GpFn=Bf!7@:s%aDS^7.B5VR'Ed)_NFo6@\Fnp1gF`VPCF`2P<gCju(r;cj"
q>p9i!!2rs#lt)0"9er2!WrT)!!NBNThHCI.hi?n$Pa0X%29Nl'G:uh&el-"(DRc,'H%g+)As50*?QRW
.4-8^*ZQ(8(]"m]'bhAt',)-&+?)!Z!!!9,!<<3-"oA;u!Vufo!VHEm!WE'1!@X[:*?c1-"Uu7Z#n7O^
'-7\p$jm@N%M'!U%1idS%U]_R"UtnN',_]+)&aD4*<$uV*#0D1'b_/f$4@F\/h*n&!"&o5!!EN/k5Ybg
!!!$$!!!*)qu?eb!!r<!"9\r5!Wi)srW)`pnGrRiqZ$X!$N:#/Mu`nY#m0u(r;lm!rrMHd$N^J>!"pc9
Z:$2b/H.U85=S(08l/Gd<)W]m&5uS2=BT!C@;0SoDJa$(D/BDrGB\1Or,_jZqK33iG'%eIGA_S7fFSAs
r;cj!rrN-$qZ6NnqZ/q^!!*0)"U,#2!WiN*";u3I-OKhW%13:I&.AjS&JGfj&J,Ne'GhW(()\,-)B3N4
)AO85*[E0^,U"3K)Aj8+!#GAF&f)5t'cA/<2(u-5!!`W-!!<H/qZ-WtrW2lr!W`?(rW2Wk.fpQ-ROARE
#S7FO%1s$U$kO!^%L`[N$4@:Q$jmFT#n@JS%L`OO%1X$h)?(HV)&aG5*$"qs"rnU%)&<r#&.]3\'c/DL
WrN,+#6b)1"p3ugr;dE2"98E&"onZ(#\seJ!X8i)!<*'#!qcQn!WN6"!U'La":P2/!/UUS!=8i*!;lls
!ri;u!;cfp!&joY!!Wl?!!"<D]i-"">;\H$4?u;(85)iX;c?Rk:f("f<E3++A70(e^i!t#DJa93GBS(L
EcM)!rcA!Z%s<#<GBJ"NH#7P:cjL6`!r`0%!Wi?&rW<'#rW2lr!!3'#r;dZ8!sJo4!=92?!!!`tUc&2S
1C=Np#RUJ<!t>eR')iIa&ebur)&O,-*Yo\7DB'Q0*?6(E-RBrY*#]\2()@Y_'`JgR(Dmr**$c[]2Q6TT
"UG21!XAl*!<*'"!W2rt!W3#o!!!3%!"T`,Uc/8V2@U0($OdIQ$P!(F!=TA8$5j3[%L`[R&IK$[@LinQ
%h9'_)&O/*()If*q\g7i)]BS1()7Gn',_T80VnaL!Xf24!sShj!!**%"9S`/"9\Q%!tF5i"8;cs!<N;q
!<*#s!r`5d!"Ar/!!Nc2!![`Q!!!9+qu?]tr;ls$rW<*#quHQo%0-A/!WrE&$5XKd%XZ;2-pK170KLdF
6:4+19MSA\;Gp@hr_O;+;H$S"@pWe`^MRe!DJa93GBS(Krc%jVr,NBjF*)PJGBS+RHYdJ=`s<1U"o\K,
!Wi?&!WiB'rW<*#qZ$Zu!Wr?%)$0jA"9o,6!"0JP!!$Z:$m#TX"UkA5$OR.>$iUV[%hK<b&ebro(E"&+
)BK\7*H)o:'ce87+snQX*?#b2()@Ya'GqJs'GM8t(`=20+=86_5G.uW!"/o0!X8c(!!!-#!WW8u!!!&t
!WW8t!#,GA#ljs:YRDTZ$4%.B#7_1M$k<dH%0$_7$5j3[%1<LQ&do6_@h9+U%h9*`(`4#''GVB"q\fAO
!#bbP&/5cn*#Kq^S,`Tj%gN(9"Tdif!W`?)qZIQ4"one"!!3H2(C'p?"Tnc,!s/Mt!<*#u!riB%!ri;e
!"Ar/!!Wi3!"N`P!!!6)qu?]tq#^Kqp])K>"9o)7":,;="p=pF^Gn5'/MT1F2*=5n6qC$J:f1+g;,R<h
'N%b,<Eis>B5>8"ChIX&DKC#FF)_2!rbqaSrG`BhF*)PKG'8.XD/4C.&Ie^DrVus$!rE#u"9/H&!VQL!
!X/f7#6bA>"9&9&?)Sb^rWb%_$3CG?#m^nK%h9*\&.oNg'GVH&(`+)4(E=H6*?,_6*$$4M,Tn'E(`*r&
'GUKZ%29Nl()Rr.)^-US/4Gj'!!N]3!!3?,qZ-WurrW3$p&G0q!WrN"!"rG2*#](h$4RFK$4[IO$kEgW
%/pVN$47.K$k3RO%MB-\&Ru@^#S.CT',VN#rY,AJ(AesJ)$h&q()@St(*".m,<q=i!!Nf9!!3<*k5YVd
!WrT0qu?_fr;[3,%L)n5!s/K)"9S]!!<3)u!riB%!ri;e!"8l.!!N`1!XW<@!!!3$!!3-#!Vlcs!W<'"
!Vud?!sf;E#mLqX#m_/V[n%i%0fM!K3Bf\q6q'[A:Jand;Gg<j:_ci+;cR(4?Y=/hDJWs(DJjN>G&qYA
qelCO"`SF#EcZ@%FpWJBDejg,)[cWJrW!$'!s&H$!!<?+!s8E%p])37#R_%F!t,\@!!6)l/I2ps%grXK
$4@4K#n-_B+qG1q&J>`k'c7f*(E4G4*$&r<)\jA5*?lgU+<;=:()7Pur=]t]'GVB!(`F;3+XeWg9T0&R
!!r],!<rZ'!<*'#!rW0!!;ca$!X/f5!!!$(rW!7!RjnUS%1isV$iUV@%1E[V%LijUq[45L%1<LQ&do6`
@h9+U%h9'_(Ddf#',2/sr"fk\(`=2-()7Mr&JZ6%,"%(`!!N`6!!3?+lMpncr;Zfu%06S:!!WE'`;fl@
!"925":"u.!!*-'!s//srW2cqrrMHd%06J0!!ET/"pJ-3"98Q&!!30$!VZZp!rrAu!"T8E&J,6K!"T/>
<m36K0.@G]0/P[N5!VG&7S6BN:f1+gr)"5-<)cn'A7'"d^i""%Df0K7G]n.JDf5Dg'5h]+E,fo>F`hkR
I;s+VWuDQL!r`0%"U"l-r;Zp&"9S`'!Vl^1"UtnJ!<<*#!!#9k'FbKS!X/i;$4Hh?!=K;9%fHn[&.fEe
'GVH&(`+,5(E=H6*?,b8*??=N,Tn*G(`!i#r"Bk\'c%Q$(`F;4+t+fl;MP>U!!`N)!<r](!!<?+!s8B$
q#CL"$4-k4!"(`h%gi[I!X8r?%K6hC%1NdX%h9$W%/^JM$k3UQ%MB-\&n;I_#S.@S&f2;t'+trm(&SgX
(Ddo*()7Ms&J,Wo(a;M"rW!*-!rrB,!pTah!W`9'"9\T&!s-XH!r`0."pP,2!s&B%!<N?)!VcZo!Vuls
!WW8i!"]/2!!**#!!<H,!tR[-!<<3"!<*#q!WiB("9&E'!r;m>#Se'e%13@_1`j8%2EaGa/13,54[)(s
6q9jD:/Fec;Z0H.;H$Rq=']?EBPbJ%D.dd)Dfg5IF)c'uD/B,c'PqT&DJsK6EccGJH[TsQN27@(!!3'!
!XAo2qu@!+"9S]+!<N<'q#D*6&Io'I!!!?H"J7:_)]oLk!!<W<rX&`8$k3^F%iu8n&J>cm(`=/,)BTb8
*H)r;(*4J;,:=c\*?#b1(&ejL&ebom'bqK#(Dn&0*?lp]0O021"oni-!!*9,qZ$a%"9S]+rW3'#q#CL#
%LN=:!"9M@QmWL_*=N#M":bq@%1*LT&.f?_%LigTr<jGO%1EUS&do6_@h9+T%h/s\()@St&ebomr"T2I
rYGkV'+tlf%h]Zq+UV"i!!*'(!<<0*"8)Wq!<E8t!!!-#"V:b;"UG).ScAuq!"B27!<N<#!!!'!!WW8r
!;urn!ri;k!;lj+!WW3&"T\T@.N&3d!WE*!!WN3!!rW-'!WrQ/"U"T$+9W8_)\No=,o,'E3'/WO2)6gA
3]oSk6:FF;9MSA\;H!Hj),aC5<``U=?taAlDJa'+Df9`BG&qV?ChmebBcCf%CMRa'DK'T:Fa&4^FDID:
'G:BH!!!$*"p4]&"9er3!Wi6#q#D$.$NLV:!#5e?\4%,J"VM7M!X8Q1!t,JF%K6k:%j)>o&J>`l(E"&+
)BTb8*cN,>(*4J;,:=c\*?#b1'GLHY)&!Yt()Ic()&aG8,:Y/rD0l6f!!WE'!<iW'!!i]1!s/K(!WiE!
!#Yb:#lk52!"8i-YWWL/!>#VD!X9#A%1WmZr=BqZ%h9$W$k!FO%1N^R%MB-\&n;I_#7_1P&Jc)prY#5E
r"KYV()@]$&ePZb%MBQo*aWa`!!NN,!!3?,p&P*nrrW&t$N^G2!<<?9"TSN*^AIs5#7(G6qZ$a"!<N9&
p]16np]CHrnc8Rg$3C80!!39)!YcgoqZ-TrquZft"p+l0"U5)1rW!`;"U>#@%O*i]]$JKq.R#pN2)mQU
3&iu+5=%Y*7nH?J:Jgpc3)W[T<`i[>?taAlDf06-DfBfCGB7_?CMIQsB4kmkBkhF"D/XE8Fa/=aF_RqA
&.nmD!!!',#6Xl(!sSo3!rW/s!#Ye?#65,4&0YSQXJC=J()%#_%1EUN#71bHrXJf9rsp.^&.oNg'c.`)
(E+A3*?K/?*#9V;*[<$Y+WVI;()6ZZ(_[W"(Dmu-)]TqG.P!*#F8uLF#6=f)"U"W%!sJf0!rN)s!"f88
"ono/$QEB7URZQ/&.SmMrX/i8#RV"Oq@Ec?%h9$WrX/i;%1EUS&eYQ`&n;I_#7_1P&JZ#o&eP]gq\'JS
'c%Q!&eGQ_%1s?l)K'-c!!NN,!!3?,p&G'nrW3'#r;[Q8#7(;0#6Or+:lM^p"98T,!WWB0"8`)t!VHHl
!WE0""8r9$!<</l!;urt!XJf,!<WB,&02>Z!<*#s!rW-M!WrQ0"pG,1!!39(!!!0QL!ZkY4taNK0eb@@
4$5Sb2`a,g6q0[;8k_uVr_X5':f1+i<`W=/ART:h^i++(rbr3eH$==KD/3iuAnE#pAnPaiBkqO&E-$2J
IXlTU\;^h,!!<3$!t#;9qu?g'"U"r+!W)is!W<!4)fN*@&/52.-j0YW$4dUT#mLYB%/gY=%1WjY&,m+g
&J>co)&F)-*u>q=E#ou8+!)LL-m^#W)Aa,%&eP]g&ebuq(`=20*"a26,qCQ"Mf/S"!!`N)!!EB)qu?g&
"9S`'!W2ot!rW*5(i$7,#Rg]j+TMKC"q1nJ#R:YF&,m1<&-<@O%/pVJ$k3RP%MB-]&nDO`#7_1O&/>ll
r=So>%hfWl'b_/i%LijY'c.d6?iC$/"T\T)"pFZ#$3://!s8T*!!!')qu@3]\L%^b!'CSg!!36&!sJN%
rW2TjrW3$#qucp"rW2Zlr;liurW*3)!Wa2O$N^/*rW2s!!!<'!/-?"Z#6kA8!WiH+#R<02Jj1hM5<Q5B
4t\WN5<_.h3''5h77Kd<8P;cR;,R<h3Di[R<``C1AmoCj_/F4*EH#l>H$==KChdWqARo=_AS,RgC2@d,
Ecu_WJ9YkGKa/+g"98E)$O?k4!!EK0"9JW%!;ca7"99aZBH@Bk%h!q(%KHV<&.]0T"pYJE%hB0L%06qL
r=Bn[&el)u(D[o2(EFQ9*ZPt<*ZlXU,p=9I(DRV^&K28q'c.]))B0Y;+=/Nj0U?AP"TSf/!!!-(!W2p"
"U"o/qZ6Qo"9ecM[q$3k!=K/8Gn:5]!!Nf@$4$hA$kEs`&c3+@%h9$I$Q'9]$OR@V$P="^&Io$U$k*[]
'G:uh&.oNO&e5Qh'G:re%1EXV'Gqa?=8i1'"T\T)"pFZ#)Z]s@!s8Z.!<<0)!<<*$Z2kI9!!EZG#64`+
!s&H(qZ$[!!<MclrW3$#qucp"r;lTlr;d$&!WrN+r;d!#/-Z=X!WE)t!W<'"!W<!E!X&]5#6kA<"UG)S
45<t!8O>Bf3k@dF0K2$W5<_.i4?l/$7RmYR8P;cR;,R9g%8p/+='/d?@;0SpDf0:gE$odRGB7\<BkM!f
@q0%[AS,RhCMe$2G'SOcH>UcH$jlt<!!!-0#Qsu)!sJf/!Vl^7!WW9%*A5K#)C64,!!S)i$igJ=&.]3W
#RLkJrXSo:!=fY=&-3@U2\[#E(D[o1(EFQ:*ZZ%=*ZlXU,p=9H().An&.oKe',;<#)&aG6*Zu^V0J]5&
!!*'*!WW3&!rDs""9S]+rW)ou,6.`H!<`BD0$-<o+;+_U!.P@\!!*94$k!@H#n.=V&J,Ka&,m+A%h/sH
$OI4N$OR@V$P=%`$5!dS%L`aX'bh8mrX])B')`CQ&eYik&eGN^$k*XZ)BF`,rW!*+!WW9+"82]r!<NB&
":58;!rr<&&tf4.qu?^<rW!$%!s/N#!!*-%nc8XirrW*#rW<$!rrDipquI3-!WrN+!<E0$!(6eirW2uu
r;liu!!3#u.KKVU#mLM<$k!RX2mu+K*\TZ:1/YbK68Uee5<hCs4[)/!77Kd;8P;cRqbR`"<*!(&?=dPZ
D8L70B`;rVG'\@QDJEisAGfp<A7Z!YBPVI(F*;m/HjjuAA.SqF"p"],$3p\2!!36(!W2p@!<<*%#6Y58
.ASLK!!a&?!#gUu%06eD%M'$X$471N%M&FH!=fY<&/l/p()Ri')''M6+)rAC(EOV>,Uar]*#KD(')iFP
&J5Zk(Dn#.)]Tk?+XJiE25WtE!!NT/!!!'%qZ$["!Wi6"+9;NE!!<K2#RDrW/2$u*$NU5@J,olT":#8B
$jm:K%1iFL!=o\=%j)8j$O[:L$k3RO%MB-^'P7sg#S%:Q&JYum&.]9_&JG'T!>#kB&do9_%h9$X%M0X(
P;rOA"9nr.!X/Q+o`,L'!sJf0$4[:@%0GVm!sJ`)!!*WRrVus"!r`5u!<3)i!<3*"!rN0"!rW/k!"]/4
!sA`/!<<*$!+,^/!WiE%!;QWq!W2pH!s]/:!<WZ8,8e0k3(,AL>pqm6[l[)?5<_:s5sR\$6:4.07Rp$C
9i(ab*D]I-;H-[u=C,NGBl:e,DJ4!-E-?POEc#N'ARo<L@MrZdAnYprE-$5LH[:*[gK"Ud!<rQ)":5;8
qu?a!!W2p"!<N6$)?9sD(^[6$)^>Ug/H?"mIfp>e$k*UU%h/pUq$d?7&,Ztl&ec#t()7]-(*+K;*uu+<
*ZlXU,p4-C'G:uh%hK9a&el)u)&aG6*?H:G0fH:!rW!B4!<<*$!<<*#!<<*$!W2ou!X/K&#mLMN%'MZ3
+pJ#\-ia5ZGQ8*O"pYGB$k*LP%1WmZr!ii?%LigSrX'SQ$k!CO&e#BfB+kg^%LijZ()7Gn%M'*_&eP`T
&.T9b&ePZc%LrpW%j*$g/H,VQ#6Or-"U"Dt'ESCA"9JZ1!>PU4"9nr.!!iW+%NYHI!!30&!W<#t!V$0i
!WE0!"9/H%!W<#o!W2p#!<WH."9&9*!W[KG!s/N)r;Zj!!;cfp!$).I$NpG1#6YTKV`Qpk9NXnS3D6V=
9Kkd-5<qM$r^-fV6q'R8"\D?\:/Fdd:HD<M<*!(&?"@>WDSg@1BQ%g.G'\@QD.mNl@q&nU@:E_WAS5ap
E-$5LH[1'\i^s:[!sJ]*!sf)5!VQKo!<`<$)[-3D:lQG2#9kW7%0.#c";M4Q%1NdX%h9'Y%K-\;%1NdX
r"&lA',VK$()7Z+(*+K;*uu+;*?QOU,p4*A'+kfT%g`dY&el)u)&aG6rZ)7c1,l`u!!*''rW!!#!<Dut
qZ$X!"o\K<"98U)Os(_K+X[p.!"*ZF%KZn@#RUqJrXJi:r=/`9&.K!S#mgqH$k!CO&e#EgBG;-l#nIIS
&f)2p%h9'\&J>Zf&.]<`rXfJK%hB-[%1XO.W$2-?"U>/1!X&W&!!!&t!#,J<#6Y#,!W`Z/7K<i*!XTDD
!=]qE!!NE+!W`9$rW2KgrrN*#rWE-$rW2uurrMrsqu?j#!sJi1rW!0*!0mNd!<WE#!;cfq!!E<*#n$n8
!#GqO\TKJf1dal+8NT\Q4A7q+5X7V%6UUf?#Xq3R8P;`P:Jh$d)c0F3<`W:-A70+h_f9R,Df9T<HZsIG
B4YR^@f9^:@UiscB52:&F*DtXG_'ql4pMK!"98E(#R1A3p&G*p"8r3;!W\oo#Sm^^)%mJ\'6jTo#S%:R
%M''[%Lr=E!t>\L&,Ztj&JGlq().T*'c\<:*ul%:*?QOU,p+!=&ePWb%M'']&el)u)&aG6*??+>1H,KE
-3+,J"8`&u!W<)s!!30("oSE;!Wo6'%N5]i((LZO$ZH(T!=/o9$4@7Nq[NQ6r=(+_$OR1H$4@7L#n7LU
',G<t&.&jV%MKWn&e>E]%hTEe&J,H`&.fHQ&-rdW&.T0q.&@aZ!!NQ/!!39*qZ$Tsqu@E3"9el-!WiH(
OUqQp#6>&<"p#2NquH]u!!<'!n,WFgrrW0%rW<*#r;ccsrrW0#qu?j#!sJl2rW!0+!42_-!!<<!!;llr
!!EB.#n$n8!#-(jd6ou]4?#Ag9fu:\5"e(,5s[j:6iKIY77Kd<8P;`Pr(e8.;H-[t=']?DBPtb.D.dd*
E-?SPEGK/s@U`dE?lEH`A7fRnE-$8OH[13beM@[E"TeZ(!XAl2!VZQq!<NB%!!3Q@Zk"/e'b(?P$53CS
H3=ld%Lr@I":bkM$k*%C!t>_M&,ZtW&JGlq'bhH('cS69*ubq8*?QRV,p!p;&J,KP%M]Kc&JGos)&aG6
*??(<1H;KV!!E<'qZ$Tsr;uls!s&H+"T8<0$l$9!'cISe"U,>8%<;XQ$igM;#n$Y>oaE#P$4-tE#n%.K
#n7LT&f5=!&.&jW%MKZp&e>E]%hTEe&J4pPq@F2M%hC!:T+1i$!<iN)!X&T+quH`tqu@B2!W`9'!X\ql
!!*B0!<WK,!=p+I!!!*""9JZ,!r`5i!<*#u!WW?%!r`6!!<*#t!ri;u!!<<-#6b#+#6b+P!!3-&"82`n
!<iN-"pbM<rW"/S.*+8,5<h7n5t""<[Q[>J6UF.-6pj=06q'O67n?3E9MSC^:HMBN<*!%$?"@;TDT$L2
AT2R,G'eFPC1Uj`@:3JM?XR;OA7fOmE-$8OI=-BdcR0G<"p"](!X8f1!Wi)sr;llt+oqr`V[3\>$j[(C
#Qtri";;"L%M'*^%LijU$k!FO$k3[Wq[`rD',;;u'Gi8>'H8-8*ubn8*?QRV,p!m9&.]6\%1WjY&JGlq
)&aG5*$$"?.m0^A#R1>+!!**%rWE*!"9AQ*!sAK%!XKUFrXoeR#Qt52!"X)M$NLA9#mq%J$MY#.$l'-W
#m^eC$4I7J%2''^(Macu#S@RX%MT`q&e>B[%hTEe&J#?]rX\r=&J5Wg'Hf)t"98K)!s&B'"9S]&!!*-%
p])98!WrG@!!!*)"9S]*!X9\G!<<-&"U,#3!s/N)mf<=frW3'%rW<*#quH]sr<!!"qZ$^#"pY;1!!if0
f)PmQ!X&Pu!$;4B!WiH,"pYD:!<EH6/[7&p4$Z/"5rqM;[m!JL6UL`>$U[<M77Ka:84cHJ:Adm):f:7o
='/a=?Y=2lDf'*)DfKrIG&M))@K'[5?O'tI@qB@kE,uA2I=HcgHcmEI%gW(6"9AZ0!s8H&qu?d"!Wi9#
'`eIG";m+"$3^bF#mLA8)0uAt"q;(A&.K*Y$k*LO$k*RS%M'*_r=BhY',;8t'Gh]&)BNl>)\a;5+!i?]
*>]:u%fHhN%M'*a'c.`+)]Kb;*?cXlUB_23!r;ls!rW6#!!!&t!Z:t<!XAfHPRJ35%1NOD!!*XO!"&]0
#7:hHr<i9,!=B/4#TX3Y$OR1L&e#BgC)%<e&J#Bd)&<hp$k3^Z'+tier=05H%hK9a&el#t)E!l^rWEE-
!<<0'!s/?#!rrB(!VZR,"9;6u!rrB-!rr<(!$VCF!!<B'"U"r1!WiDj!<3)r!ri<!!<3)t!ri;u!!<<-
#6b#+#RLO_!!E9'"Te>t#lt&.!WrQ/#6tAH!<<?519`N"5!_J"5WVG<\3NbQ6ppoA$UdEP7Rfm=8P2WL
:&[m+:JXeb<EE7(?=[GWC;"@rDej61GC"CLB4>9J?QWT\?!^lG@V'7jE--ASJ:M`bfFel.#6=f)!X/`0
!Wi,t!WiB'rW!9+"UbJRMZF1k$47+E"98`GHNXue%1`@K!Y5_Lr!Wc=%Ls!\&J>!R(_IDq()7N")\j;2
D&=*2)&s_E.3ooL&.\[K((:W]%M06f(E",1)]Tk<+<rnM!!`Z/q>^Krr<*$!!!3$"(BFL9!<rWJOp_p4
%134<!!*[P!"/c2#6G5?$iUM,$NUS@rWjMN$4@1J%MK9b'P7pf'+GH`'c@c!%LW[U&JGcg&,cqQ%M'*_
&JGlo)&k<-!!*0*"9JT*!s8T%!!33'!VcWs!<r[$r;[30!rr<(!$_IG!!<B'"U"r1!WiE%!:g-h!W)rt
!W)ls!W<'"!Vucu!sJo4rW!3/!6kKF!!3<*p&P'm.foeV"pY51!!E`e[5LB>69[Ru4@iVd5u0d86q'O6
7R]d97n6*@8P2WL:&[lh:JXh';cQn$>$kfKBP4bbB6S$+EHc\MD.[2S?63BW>[:ZC@:X%gE--ASJ:M`_
i!Kr&#6Fl*!X/]/!Vl`q!W2p3!sf)PO9?%%$3gV8!!jHi"V_1O%fR"A%h9$XrX8r>%1WmZ&Gm%H',22s
'Gh]')]3,o'GVr1*$?OU,9.F/q@"#H&/#]o)&aG5*$$"@+uZn1!!35u!!!&u"8r5u!WW9#!!rc2+I3HO
&I\jErW!<<ErZRJ"pYJB$O[=8$N^YB$2t22#n$Y>&.T?`'G=a^$lfTa&Jc3!&Ifok$k<j_&eGN^$k*RS
%M03b'G_H%*A=Vs!!3<-"9JZ.!s/<"!WrK)p](Bs$3t)>!##J9!!!-%+ohZE!WrQ/"9\f.!Wh`irW2lt
rW2lrrW3$#rrN&urW!$%"U5).!!i`.[K$=.!X/Yt!$qXH!sAf5!WW3(#qa"Q7n#d/5!V5%>.[-u6:XI6
7Ros<7n6*@r^eD.91qrQ:/4S];,^Is=^,6E@V]>PC1hL$DK0iEF)5Do?!LW?>lIq9?!h#NBPh^1H@LHt
E".BD%h&^J"9AK)"U"l-nc0@+#m(s8"qhFS"p4r-#TA'o'aP9ZrX]&?rXSo:":bnP%hSUM(D7Aq'bqE!
)]'M+>T":u)''hG-mKZF%K6_K$k!FO%1a'c(E",1)]Tk<+WWqGp](?q!!3$#r;cft!<N<$!!i]-)5@ZY
'+G-D!!j0X!"8i3#71b9$iCG3$iUJV#mgkD#mq(K$kF!_(CF1U%M]Hb&f)<!&I]!S%M9?e&.\XI$OmRW
&JGio(EFAWTDefq":#)4!sA],qu?a"!rDs+!<<*#!XJdr!!3-#!r`0)"TT_H!<<-%rWE?+!WiB'mf<=f
qZ?`tq>gEoq#CKu"9eo,!!ic2K`D/S!<iSr!!NE+"U5#.(B=UC,gJDA7RK@'5s7eD]L5Xb84H'=8,Z!X
8cD=(91qrQ9hnJ\;H-\!>$PHHA8GJBDeWg%E,g#EEb])ir*0/()I-TV@q]^uFF&FeKkum['ak0J"Te],
"p=u.nc0"!$31U;#o+$]#6YP?!!jKk"r.FT%hK<b&.]<L%f[(>&H!+B&eYilrY6(_)AjM(:EC>f*ZlLN
-R'HB$jm@>$P*XV&JQ$!)B0Y9*?6:A;N(JR!!2rs!<E9$"8i/t!WE')"99":&/u;m"oSE+&Te!^!!``8
!"/]5rX8c9rXAf7rX/Q0*=</_$k3a]&K(dF(_@)h&ec#t'bCc[$Om[]&e>HM$O[@Q&.oQi(De20:l,)N
!Wr]4rWE6(!W2ou!s8B#$3:2/!!33+!7UuRqZ$[%!$_@A!!3'$rrW0#r;cEhrW2ltrW2corrMlp!s&K,
!r`0*#RsT7"98E*"7cF2!<NE/!<<*%$QI;O91D<85smh.?G&^*77g!>rCHr[r(?r]#>@fc:/=_b<#8V=
>?tZKA8#S5EG0!&E,g#DEG8ic=]t`-r`L.D?!h&RCiFNCIt35iQE(Z+#R(>4!<WN0!Whil(]t$I#HA4M
&Io-Q"onoKHj1>m%hB3`&J4mO!"Su=rt,2Bq[roC'`JgO(`F2/(-<Z_(D\#5+XJKZ)%m;`#mq%I$4@7P
&JQ$!)B0Y9*?-1@<e'fC!<E9$"8W#t!WE'*!W`M-&f_Pp#6Xr*#S_=[%KQe>#n$Y>!"Af8rs\o8rX/Q0
%13IO$k3a^&eu$;)\<JX'*T-g'G(WX*"!,d'+k`a$OR4K$OmX['GVH%+;e./!!!$&#6t/1!WrK)r;Zj#
!rW*$!<N?(rW!'+!8.>WqZ$[&!@%IB"9AT,!Wr<$n,WCfqZ?`tmf3Lk!!*-'!r`0*#SAKm!rr<)"TAGo
!"8o3"T\T'!>,sb5>4KE70l@J9O>G&<(9LZ8H)3\9))%!9MJ8Y;,^Ir>$PBCARo=kG]IJ3D/XE9F`;#%
=oMP'=oMM4>$PEDB5DR1H[pX"E1.3,&./dL!W`<)"pG&/nc0@+"Ub=-&K22k%LNIA$6=O"(CCZ`rXf,A
q[`Z;rXo&@(D@Gr'GVB#)Aa,3-Qs9C*$6=M-6O-;$N:A1$4dLS&JPut)B0Y9*ZH7C>&s?;"TSQ)!WrPs
!#,Y<W"pBc%grRC!!*dU!"K#7#71b:$O@.M%1WgV$k*OC$N:A2$60E^%1Ws`&J6$.*"WYo',23!'FtQW
$4RO[&J#<K$5X'Z&/#Zm)&OJ9>BBiF"U5,6"9\l2!Wi6""9S]+!!!-%!<WH+rW!'-!7UuRqZ$['![IUC
rW<'"mK!1dqZ?`tli@"drW!60'+5*J!!!0*!r`5n!!rZ."9AK&!tGaZ%RNlV7S--A6rI%'8QA5Qr^m)]
"%u9\:&[ib9+FWi:/Fhf<`iO1?XdPWB)Z["C27X(EHH;?B4"bA='&L+='&L,>[ClPCiOTEJU`;oVLfKj
%L2t6!<`T1!s.rm%g3+D!2UGN%M9<`$3LhQK*2Js$4maI&c!":&cE@@'/(%6'c%T'(`+88*Z5k9+!N!W
+;bXr#RC_D$4.%I%1j0g(`F>5*?H+A+D+UR!!E#s!!3$"oDf!s!2^VTrXTAC"98Z6H2nEU#7(\8$NLS8
%K6h@%1N^R$4?b=rX&f:$OdIT&cNFt)]BS-&eYim(Dmhs$O6tI&/,Wd$jm:I$474R&el-#(EXf7=o\O/
#6P&2"U,#1!W<!"!s/N&!!<9*"TnZ'":,"c!!W6"!XSrRquH`urrM`lq>gEoquZftli7(f!Wi9#!X0&7
rW!'%"9\f.rW2Zl!<WK(!"oDB#fT5,5Y"OA8k2uVb"Gc*9`@Z`9,:2q9hnGX9h\5R92&&U:f:7n=B]!<
@KC"Prb4!"Ci!m)EHH;?AmJJ<<E<1&<`W:)>[ClPCiFNDJUN,pZXk!`&-`+7!<`T1!s.rm'EnaH!2^YT
%2'Hh$jIIRL^P"+&.ndPrXer=r=\u@%ho]m()If*)AsA1*#fh<+p]J@*u>Fn#6tP5#ndRS&/,fr)B0Y:
*uQ1IF#a4#"o/,u!W<)m!#5P9!2^_X%1j-["TSu3If^)\#7(YDrX/`8%K6hB%1N^R$47(GrX/W4)%6uc
&J>cn'bhAt'G;)q(`3qt$O6tI&/,ZX%h&gE#o<pX&/#]p)]'SDG<Z65$jQh8"9er3!s/?#!WrK)rW!$%
"U5).!!EN,li7.b!!3K0,Q%Q@!UKg`!W<)u!UKgd!<<0"!!3<4!WE'%!X&W."8r8o!!*0)rW!W7$jt0K
:d.BG9h\,^9[$44852`MrCd5d:B"&h:B+&f9H?i';,^Ir=Bf'=@Us+cBP2'rChmp.FEDD4>ujs*rDjV6
=B\s:@V9LrFF&IbJ:"q.)[m5\#64`)!sJf/!V-4/":#,2WuW8i&fD>l#8[]'$lB<_&.oNf&J,NP&c<::
',M>t()If*)Aj5-*#fh=+seQY(CpcU#7(56'+#!T&/,cq)B0Y;+;l:NI4,*r"Si&r!<<2s!!!&u!#,G6
WuiGk%hoHW!"ApX!Y,28#71b:$OR:O%1WjW$k*LN$N:A2$6BQ_$k3^Y&el)q&el)q&el-")AWnn#RV"Q
'+tfb$iLDJ%1j-e(`X;5.tKA]":PJ8!WrT0"9S]'!!*0'r;Zp$"9el+!!ET.n,NUh!!<6.![@OBrW2?c
q>pTtr;l6br;llt!XoeLrVup#rWE3&r;lWm!W`B+rW!3)%1pl\;*@HJ&Pl+n>>NI<=\;F_9heAW9hnL`
:]aEg:Amm+:/Fed<EE=-?!q,PB5)$lC2@^%DK9iADJ!3Ur`(%@<``@*>?tWHBP_U-H%:6kID\Pq$4I%;
!!*0)!s/Mo!#,J="oteL+:/Z"'FkBb$],9/$5!jK')W@>'(utF'GVB"(`=5/(E*2k#9P0;-6O-9#lY#D
#6tM@$4RLY'c.c-*$-7A+YJHh"98Mu!;urp!<3)u!#,J7Y9P1r%i#NX!"AsX!=f)7#71_9$3:MCrXAi9
!t5PE$N1;0$9/D$%1a!^',;/n'GV;q'c7l0(_R8a$P!a^&eGN]$OR4K%1j-e(`X;5/rCqb":>84!<WH.
"9JW&!!*-%r;Zp#!sA])!"B;9mf3Lk!s8Q(!=/]LquH`tm/[.doE":Y!s&H)!WE'#'.+7h!!E?*"9S`)
!W2ot!W2p!!<WN(!##n]b?@Y+7o`D]93b?>:g-Lg:/:a`#Z+>p;Gg:f:J^sb%o6#"<)m"&>?tWGA7fLg
BdRS1CM[p0F`hV7?<:**<E3($=B\s:@:X%fDK0oNH$t7b3ZeS6"9&9&!WrN+quQHj'*JRBW@](t&KDMr
#T*u,$lB?a&cE@B&cE@>'DrRD',)&o()If*)&O2.)]Kb=,:=i^(_@Mi"pG/7#6tPB%1a'c(E",2+!V^K
1lW+Qli7(f!Wr<#'*A66/fb9.(CgWL%0:nY%0-S:#lP&1$4He@rsSi6r!E</"Ub_K%hTHQ'E/[X()e/5
)AE\h$P!a^&eGN^$k!^V$OmX['c7o**]0#u'*8FA!!*3$"9AQ)r;Zj"!W2p!!WrK&!"BDAjo>Sc"U>/1
!=&TIquH`tl2^MYli7"drW3'#rVup/!C@7p!!NB*"9S]+q>gNrr;Zm""9n`()%dq0BM(W`<`2ag?;o0I
>>.mi:f("c:f1-i;Zfop:f.-e%o?,$<)m"&>?tTFA7fLhCAquSCi=?:F`1o!=8l/=<E<1(>?tWHASGsu
E-HbTI"KWu*sDlN!<<*#!r;uk!#PbD#bj?r%MBct%ga'^M@CF2&J5Wh'+toV')WF='`A[H'GVG`(_%?#
)B'P7+=&<_+rLptr<3i=#7(YF%hTKl)&aJ;,TJ$fPmRig!;c`t!<WH&!#YqEUH9;$%MoTZ!"AsX!=]#5
"pbJ@#m^hEr<rT3q$I$-"UkhN&.oQS'E/[W(E4D;)\rtn$kEp`&ePWa%K6bO%M06e(`X832OP3n!X8Z*
!<N?+!s/N%!!*-%qu?g"!W`93!!!N7fDl-W#7:Y:!!N?EqZ$TsklCGYm/R.f!r`9%!WE'##\+,<!<*'#
!Vl]r!Wi6"!W`E-rW!6+%Mm3.7n-KV;$p/q?rYNO>u"<q;>jDm;uT_u;c6Ljr_O)%;H$Oq='8a5?XdPX
BPIE\#]+F"F`hV8?<@))(KOU@>[LoMAnc'tDKUAOIs'9r('jsA!W<!"!<E9#"8)X.":#"+64j_K)&*Vh
)%DH4)%.&h'E8aE')`LA'EAmG'`Ja['GVB"(`4,/)B0V9+=&?`+rLpt"o\W<"U55>$kEp`()Rr/+=/'X
/Y<IQm/R4h!WrQ'!##D6VaM.-)%m>^!"AsX!"8i2"UFr2!"&Q1!"/H,0+&$o$k<dZ&J>`j'GM9!*$?CF
(D.)c%hTHg&J,H_%1EXT&.oQl*>ThLU)"4D!WE'!!r`9'!W`?$!<3)s!"o;4!!**-!7:cM!XK,;!WWB(
+6<M$!;QZ^!!**&rWEH,!!!$"M#[SU!<*$"!Vl]r!s8E$3roEe!!!$)$4G%,7nR/c;,U5!<mjrR:K14j
;cH[o<)lq!<E3!s;Gp@h;H$Op<`iL/?!h#NAnYppD#S5rDfTuCDe<<W<)Z^p<`iO2?t*\[BkqL#F*r.]
CYLQP$ig8/!W<!!!<`9'q#D33!!!')"9>An%h^6*'+bNi%Z:f7$PF'M'E8^F'DiLA(&epH',)&p()If)
)&aG5*$$1K-n$8W&-s$T"9S`/"pbPE%M9?h(`=56-6OleV[r\*rrM]k!s&H*"TAB?!<<+u:(Rs\%LNC?
%0:nX$igG7#6tM>#7(SAr<i3(*srAa%1Wm\&ebom'c%Z-+X8'H'+PK`&ebok&J,H_%1NaV&.oQl*>TnF
WYbsLr;Zs$!WrN+r;cp!!Vud/!<<*$!sAV6!!<9-#mC>0"99P$!;lla!!30&"9&H-!<<**!3#u!#lXi'
!VcWr!s/N%!#PeA!<<62#mdr#;c$Uq;GpA%=4:/V:fUKl<<-)!<u"b9<)cdp;H$Op<``C+>?tTE@qKCh
r+lXWEccD@AmJG:r_jY6=Bf*?@qKChCMIU)HZOIUg`m78!!!'$r;Zm"!sJT,q#D<6!!!*,"9=Wf(`+83
'G(Wk%uUo8$ka0d'GUKZr=o&Br=g"\',2/s(Dn#.)]Kb:*[)gX-mBN?#R120)?^6M$4ICU&eu3")B^CL
.5S",!!*'"!<N9&oDeso!X&Z*!##J8!0US*'cR_m"TT#5IK0cV"U4c.rs8*#(((EX%1a!^',2,q(E+>=
,Tn!>%hB3arY#nW&J,H_%1a!]&f2Q&+"s`)$4Qk5"9AQ+!s8?#pAb=!"98G'$31,."pY83!!E9D`;fr?
!X/K,#6Fo+#lqF7$iBu)!VcWr!s/N%!##G<!<<<7#RHom?<:!+<)ZY)=k+-c?rC'+<`W:&<``C*=]ea,
<`T)t2cWjY='/X1?!h#MAnYpqD/F**DfKi>D.QsP;c6Ll<ENL5@Us+cC27R!EdDYEK\R:Q#QOi,!rW*"
!<`<)!!`9"(]aX;!!<N1!deN&*#9P0&.9EfN"-a7&eb0XrY,8Fr"]/GrtYDF-l!I4(`=52*$$%@+XJKa
+W(^q"9S],"9o,>$k<g]'GhQ'+=J9W7'6@e!s&K*!VHF3!<E6)"T\T("onXLC*OW/'ak0F%KV"Y$igG7
r<EE/#7(V4$2t;3$N(2J$47.L%1Wp]',2/s(E4G@,Tn$@&.fEd'GUN[&.oHa%M'*_&f2Q$)F(D*%1<%6
!!3$"qZ6Bj%KZ_63"l]#!<iQ*!!E9EhuMm>!W`?*rWWT0!WWK+\cE0/!!36(!W<!8!sSc+#8%+BOfVVi
;HZst;Is%_=CP32=8Z2#=oMS-=]ea+<rH#3<``C+>$G9>@:WtaCMdp)Chmp-"`eTu@Tl_0;&N83=Bo6C
AS5^mD/F03G]7h[i"?G&!!!-(r;Zj!"8rE"!#P_<!!!'+!s<R_(a0\8'G(Wl&<.2=$kj9P'ESp^'`AdC
(B,'H'GhK"(Dn#/*#ot>*[)dU-Qj38#6Y,1!sB/>#R_(O&/#Zm(`FJB+"Kmgqu?g#!s/Mr!$2.B!sJl0
!!*9(!,lru*tf:r"TT#6IfTrX"U,,:#lY&/#lY/.$N:G0$5a-Y$k3[X&J>`k'c.f2+s\9L'G(ff',;8]
'F,6_&.]<a',1]g)\X;[ZiCI>r;Zfur;uiso)Jq;*!H<B!r`0$"99Ra!"K#2!sA`/!W`<%!X,Y1"o\Mp
!!*0'r;[c;"9nl,#8%%>LUBlc<`rC$;Is%a=^tH8=BSf*=pS>:>[(B8=]ec)<]F/^=BJ^0>[:`HA7oUl
D/F*)C2@d+DJ3EZ;,9ta;,gY&?t3b\Bl%^-F*)SFH\gSn#m1/-"U"l)!!<9*"U+l0q>_H9!WW3$#6G$C
GRc#;)\`hk*"e2B)@[>n'GM;]'`SpE(B53N(B5-J'F#9e(Dn#.)uL]s+<r0Y*Yo1g!s/N+"U58@%1Wp^
'G_Q+*[2a_9XO]t!s8Z.!VHEr!<N?,"p#P@!!N?&Apb.7'GLoY!"K*]!Y#,6"pbJ@rWrN1rX/T3rXAW2
((:T\%M'*_&ebro()e5;,9Id:%hB9erY?+]'b_2l&.oQj(Ddr)-UtHC"pFo*rW*!#q#U?mrrMus!>6aX
!<)s""TT_D!<*#E!!E<(!s8W%!!3Fo$N'o(!VcWq!Wi6")$'jF!WWH:!<RGV:gmC.<E)k->M34l<a8f.
>5_Y*>l@qn>[(B7=BJX+=BJ^/>$G6<?t3b\C2@a(Chma"CM[cs>Z=Hl9hnPb=Bo6DAS5apEHQMKFE2bo
eJSGk!!!3,!W;uu!rW9!!!30&"9&99"T\j3I1IS?)\`hl*"e5C)\!Go'GVA^'EAmH('#-I(]P9N(&emO
'c%T&)B0[o*??4G,9n0B$NpM4!sAc4#n%1P&/#Zm)''_>+uNT+qu?g%"9S\t!$2.B!sSu2!!!*$!*4X_
+qk\!"TT#7JHHA_#6tPA$N:A3$N:G3%/gY7%/gSL%1WjY&.oNg'GVB$*?ZLG(_R;h&et9\'c%Js&J5Wi
(E+,,(b/Lc"98N(!!*/u!W;uu!W2p!!<N?"!!3ET!W)iu"ookF!<*#Z!:0[f!<N?)qZ$a%"+1@Vnc/[l
!W<!;!<i]0!!a&8"(T/H?rgN5<E!I5fj&/l?!CQ=rET\8?XI,F?!LT;r)jP6>$G39?=@>TBPM@#D/<tc
B`i!U=A^,48kVlT;cd43@Us+dDK9uLGB.bOUqn)P!WW3*"p4`'"9AT,"9eW&!s&E("9&97"9Am%K+]@D
)\`hl*>+>E*"EYr'`JgL'GVB!pD<fE$PaBj'GVE$)&aG6*W7#k+!DdM)A3>Y!<N?,"pbPE%1WdX&ebut
*?,tD2Jnidr;Zp&"Tneu!$2.B":#26!!!'#!(2JT+;,Cs"oo,8JHQJb#m^kG$iUJ5$iUS5%JpY4%2B?_
%hB3_&J>cm()\)5*ubt-%1a'dr>5t['b_2l&el3'(`"#?AdF_/!!*'"!<N?$!W2rt!W<!"!<WH$!!30S
"8`'""ookG!!E<(!W`>J!!30&"8i-)!<<H/<Wr[-!W)ln!!!&t!#bnB#Qau1%fc`0a&ZSK>ut'*Am*hn
BNebK?2\(0?i=@8?X@#C>Pq\(>7"P??X[GVB5)*rrbNosC1q0f>?"<f84cKN;cd11@Us(bD/slLG]S%O
Z()^8!!!$*"p4`'!<E9$"8i0!!WN9$!##G8%QB4X+Vbq1&.BTkO:`HB'GL?Y!#GDIrtt_OrYGJJ.M`g;
)B'P7*$-1E+X%sM*>T.j!<E6("pYD@$k3^Y&eYin)B'SD1OO?Kr;Zp&"9S\t!!WH+":#26!#5J7!!"a4
'd"&'$jH\B!eLRf!t#ACrX8i9$k3+Er=8T5rsni8+qYM*)&jP9*#KA#$k<mc)&aA1(`!f!&eYlq)]0A5
.!9P6r;cfurW2lrrrN&u!W`B+q>^LYqu@$'!!WEL!!*'"!WE-#!R:]F!W)j#!<j,[!<VTf)?L*K!WWE8
!!PU3='o!7=]\R7>2!:t>[UlE!+5_5$=R@P@UW\Q?X@#CrEK8+1L4<o@Us(`BP;*qD/O6,An#"G:J!uD
7nQNS<a/p?A7fOlEHceUFEhi>E#&f]!!<K2"8r3"!W<)t!!<6&!sJT')Zg!M-]\ub'H7\s%3?(A&KMAs
'GV>u'bqK"(]>3K)#b?N('G?e()Rqf)C-7C+X86W+<;:3$O$M1!X&]5#mq(M%hK?c&/#]p*@ik%9E>4o
!!<?,!Whro*!$-F#RLP4!!*'"+H[H]&JbcZ!"]3_"VLtH$Om"D":P_K%M&FJpCR66)\3Gh%1Nma)''_;
)]0;%%1<XY(E+52)&O/)'E/UE(&f'S,:A(6!!N9$rW<'"qZ$Wu!W<!"!<WK&!!E<&9E54n!!3?)-2dfI
!<WE*!<M6]quH]sl2UfAkl;e,"pb81"V1S:1=0-1<a]*5<+BCg>&IYU?XR8M@:E^E@gHOP?sd5G?!LY5
>m=VA?t*YYB)ZENC2Im.CLg^O:eF/C*CE7e9i4no?=@;SB5;F.H?sgYG/uf^%0?S7#mLM0!;urr!!<6&
!sJT')Zg!N)NtpY',qVt$l^%@%3Q5t'GV>u()7T$(\\dG(]>*N(Dn%h)Aj>1*[2pZ,p+$>%L<+9!!3</
#mq%K%1WpX&J#<\&JuZ?2jbQd"o\K("9S]+o`,s4!sJr:!WW3$!!![t(EF&&%0lkB$@W!k#7M"Mr!r]:
rXf#?rY#&>rX^@c%1<RU(*"G=*#KD&%L`[S&f2K,)]BS1'bh;n&/,iu*[<7u('+C=rW)p!rW2lr!<N<#
!!30'"T/6&!Wu@("T/6%!XBbKrW!*'"9\f.!T3tU!V$-q!sS`*"UI?n#58,j!#ktD#m()0%KHY[dog$Z
@9cu8?u4"fE+*6b@:K4G$=m[YARo:[@:3GLqHa;3?X[GTram]mASH"#EGArb:eF/B5<qS+92JSj?!h#M
Anc(%G^4XUHHd0?%0lq=#mUP5r;ccsqu?g"!<WK(!#5P8%hG!C*toS-&I]L"IgRA5'bhAtr>#ALobdWD
!u;Xg)#bE^)&O53,:G#g*Z#=n"o\KB!X/i9$4@7O%M03]$4@@],UYdK!!EK.!!*3)!Whro"T\]/#RLS1
!!!68Ql$eR((CNL$5@O](^^`^%f?k;&H3:@')E:@')`Cs&.T*U$4n!p,9Rp@&Io3V$4RUa)]Te8)&F#%
'+bZd'cSA@24":C"9JQ'!s8T+!<N&t!<N<#!!<6("TeQ%"p509$3U>1r;Zj-(((?J!!*0)"9S]+!T=%V
!V$-k"ptP5!!K8$!s/Mq!!!&s!#ktD#Qau.$3C>If32K^A7/\G@!/S[DId<g@UoCJ!+l+@"_D4S@UW[D
?i+4d@Uit]An>L`BPh^.BjO\.6U*^r4[;D+9i4qq?=78SBP_X1G'7V>`tT3n"9A]6#Qt2,!;urr!<3*"
"8r33":P=&)BKM1()%2o.U`u4'c6iar>#ALpDEiGr"f>NrYc1_(Dn/;.4cec'++mErW!r?"UGDA$k3[X
&ebfb$kF1#,rhFq"9JT(!X/].!VHEr!<WK2#m0u(&"aaZ%MfN\!souJ#o3s]&,["<&cWLD'E/^F(&emK
'+trV&If9]$jm@S)'L=N)\WYfrWrZ9&Jc8`)@[Q$(D[`!&JGp!,9JV)qZ$d&"9S]+!W)it!Wi6"%flb9
!<<*$!!`XD"UP/4!WE'-$P*IB!!*0)"9S]+!T3tV!V$.!"9ni+$imR5"onZ(!!2lqrW2lr*ruNM!<<-)
$3C[k>?t<B@piVOHAlWTAnP[cA7]=aB)Q?FAn>L_@eX:J@q91aAn>L_B5DO+Am%em4?>G^3^#_s8Jt9%
=Bo3AA7oXpEH#i.E3^Mt"98E*$OHt<r;ccsqZ$Zu!X&B$'FY6IV&^Qg)]'2$(+qin*>fV/'c$Z_rtkJJ
!#PSNr>,JO)?(N](`*u/,Ut>k)@crK!"K&6#RLkI%1a$a'G:oe&I''r,s@1i"TAB(!X8f1!qZHq!X&`6
!r`02!<<+r*#]8$%grXM,;g,J&Gm(=')rXF'`SpI('bWk()7Ms&eY$Q'+PHZ$kjR)-mKWB#mU\@#n.@Z
(]"sT(DRW!(`OYB22(i,"U,&4!W`?!!!*-%qu@c?"9AK&"TSl0IK0cW#Qau+!<rl5!!!$%"9\f.!<M*Y
rW2Wk&ci(8!!**#!!`La":5&.!<N?)q>gNr!!2rs*ruKK!<<*'#ltFg>@(BFAn,CcF*;A8BkV*iAS,Oe
BDlKKB4b^dA7K(XqI;9kAS,ReARf4^CMn$"<(/f)1c70N3^#bu92S\k>?tTE@q]^lBksJo*tJ_]!!N`9
"9SN%r;l`p!WiE''`\47$NpI.+!(t5(_mi+-Rg,Y)]BOl(&f!A(]>3M(Ch9")B'J1(De):.4c\[$MsfD
!X&`7$OdLU&/#We$k<pc,;=7H#QtA6!!3?.!Whon"9J]2#Qaf&"K!1W$5EjX$k3dg*u,M('E&RC'E/[K
'c%Q$(]>0U(D[`"&ePZcrX]nW%1E[[*@3-Z)%QoS"U>>B%M9Bj(Dmu*rY?.\&eu9%+tRV5!<<3%!!*9-
!s/N"!<3)t!##G;!<<0,!"&^Z!=T#;"TSN(!X&E%!<E6("9S`-rW1pW!!2Zk"Tno/!!3E)!!t+r#R(A4
!!*3)qZ-NpqZ$X!"o\K>"U>#9fih`cCM7<qDej!$Chm`tAnG[gBP@?Y!,)IIB4b`QAH-6?A27_.B4kgf
@q0(`CM@'L5;OuI1,LjI3^#f"9Mnbi=^,-:@qo@[F4*`)%1rgG"UYJ:!WE)s!Vucs!<W6#('=jC!2q"^
&KDW')^$.=*ZuLB(`!i$rYG,BrYYVN!>l^R)@78u(`aeJ.3B3-qu@c=!X&`6$4ICS%hTEa$kO3h,!MtY
$j."E!!3?-!Whon"9JZ0#6F]%%]16a$5=![&f25n'G_Gur=f/E#8Ish()If))?(NY)&O/)'G:uV%g<LV
&.]6]'G_]8-m9B9"9Sf4#n%1Q&JGin()Hla'G:un*>]n\U*g*E$3C2."pG)1!<N&t!!2rs&HW(9!!<N-
#Qf\_$N^bA!!*0!!!NB)!s8T+rW1dSpAbj-"9nl,":P83#M]:\!"/i.!!NK%!;cfp!!*0)rW!0+#65(_
=C,V=BEi9kBjtajCA_cFC&D]LBk_6nAnM$Rs(;1?s(;7C(M78jA7AkD7QN4U0/57>2)dQZ5Xe7?<>8\H
@qBIr?rh3h0-Uc6"98N1#6Y,,!W<)q!!!'!!##GA!!&u?*ZQ"4()nA7'cS58)Ar;drYPDHrYGPOr>,SR
)&aG5rYu+`+<_gC%0QP/!s&H+"o\`:#RLnO()n/0+!hjG5c5>(&H`FE!!*6+!W`>p!!<6("U=f'%At-^
'b:`_',V>j&JZ&Z'`JjH(+0n8(`=52)]Th:)&F&%&J#?]%hK<c',20!*?ZLE'+4sI#71bH%1`=I&.fKj
)]p+B,q9uV4eWAn!!iK'"9o#3!Wi?&qZ$Tsqu@?1!sJ]*!XA]2!.k1Y!=K&2!!2ut"T\Z,!s/Q'!SIJQ
!W2p-!X/f1!!3B*!s[0\!!!6&!!*3)qZ$TsrW3*%!W2ou!X/K&%g<+:#Lup`E+WctD/O&tAc??CC&D`D
CB\HfBkV-lrFQ%Bq.;6mBkh?n?W^/q4uFrE/hf(;1c73O3]oYu;Hm[EBQ/#u96I3S+USJT!!3E2"9\H$
q#CHs!!!`6":5&.V]['.'GM9#*>oS/*#fb4(]G0M(\AL?(Ch9!)&aG7+!DgN*#TG##Q4WD!<WK/#6tG9
!sAoB)'C(H.4u\Y98Nle":,#.!!NN)!WW8p!!<6'"U=f'"f31U*=</\%2'Hi$kEsa',:?[#T"9o(`=52
)]\ht)B9Y4'b_/i%1NdX&JQ$"*#on9(D@;d#7(VDrXBSP%1ERM$4dmn,UOlk1EmW,KE2J]!r`0("U+u1
!WiE#!!!&t!"T)5"T\T'!rrN*GQ8$M#Qjc$!<N?)!s/Q&!S[VR!W<!-!<NE/!rr<%!!rX&!!N3"!<WE$
!!!&t!WW9!!!**&rW!B5!!!)GAR]CiCMI[&C&VWJAS5^mCi!m&r+uCK");OaB_c<=Ae&KiD/<]b:.%-%
0J+k/0`<dG1c70M3^6#*:JOV^>!G9W>o41Z"onW)#6k>1"8`/n!"o>=!WrFr/0Q)P'bhH&(`!o+)?(KO
(\8F@(Cq<!(`=52+!N$Y+W1ju"9JH$*WlTO#7(P=!s&E)#7M+P$kXHb'9#6^#6G)2!!!-(rW3'#p&G0q
!X&]'!"Y\N)AWbi$kX3e%Ls!]',CE]*#KM1)&aG6*??1C*ZZ.9'b_,g%1NdX&f)E/+s%jE'+PBX$47.L
%M''[%1<II"pG8?&/5`h(*EtuMEV"@qu?p)"U"o0!Whup!s/W1!W<!&!<?[2"98W"!!E?*!s/Q&!Sd\Q
!WE'-!<WK0!WW3$!X&K'"oA9"!W)is!rW3%!Wi3!(]a[<!!*H-!<C,[An,guCM[g%An,:\B57B^!,VRM
"DhmiCMN`\rFcXQB4bahCMdlr;aiZ$0`EX)0/<>Z"Z%tm2`Ni14#J`M59iSO'G^cR"9AK("pOu/q?-Ek
%0?n;#6:/P,o7O:',;A_(],'K(\ALB(C_2u)&X>2*$?LT.3K?3qZ$[!"UG#4!s]#4!Vl^"#QPjX!!`K,
!<iQ*!W3$#!Whup!W`E,rVup"rW!Iq2'!,;$k!RZ&eGN^%h]WS(bQ[D)B0Y9*?H7D*uu7:'bV&f$k3[X
',Vc8-6F!4"pG5<$k3^Y&.]6Z$4$h="8r<#!!Nc2*P;@RqZ$d&"U"r1!rrDs!!E<)"U5#*!!NC$!rr<&
pAb0or;uoug]73P&-)\2!sJl0!!!**$*F7.#R0r&!<E9#!s&H(rW!$#!!*3$!#Q"B!"?Y]CM%U*Ci+'*
BOt[bBPVL(DJj=gDZ=SQD#J/IC(tAqB4kmlBkL[G5W(5J/M&J+0JP<]0GlN"1Gh$M3B8oM4?aU6TF2&+
!<`H(!sJl,"T8H&!qlTs!=Af1!!e]G.2a*@',:B]rttYOrttbPqA/uFrYQ(^)&aG5*$$+F,U46>"oA9$
!X/i.#Qk;8!s/5u"9])4?\SFY!sJf.!WE-&!s8T*p&G-p!sJT'!!<-"$BQtc%hK*V%MKHe"V;1V',;>^
)#bBU)B'P7*;pm%)]9G+&eGQ`%hK?g)''kF*#&b`":#8B%M'*^%h/mQ#6k>0!s\l-!"'8;@"e@V!<E<%
"9JZ-!VQKq!X/c/qZ$ap!!3-$pAb0orW<'"!!1gS$NU80!W`<%!!*-'"8i-&#"&@o"TnDu!<E9#!s&H(
qu?a!"TAB7#64`@\o)G%F)Z#8Df'6%AnPjqrGV^RqeuFN!,_^Pr+lgXCM@HpAn,1J8Nnsb0)dF</h\n4
0.nk21,CdJ4?Yhf2+Tt]Zr.M8!!NK-!WrT0r<3-&r;uWl$O6Y5"H5/g*#fV+(&f!M(`E5iru(hRrtkYM
rYPPNr>>eX)B0Y9*?G)"!uhp^"8`'!!X8K,!X/Z,q>^[3%fhhV!r`0,"U+r/!<E6'!s/Ms!!30("TAB$
!r`0*M(^+e&.8jU'E&OH',22u(]G9M)?(QP)\j5,().An&.fEe'c.c.*?>t/$3^S=%LNUS%M''[$jm7F
"pG/7rW`W2";qsYQ95!E!W`9%quZs$!VQKq!X&Z-r;[$&!)!:p!!2fo!!3'#rW1^Q"9AQ*!s8E$rrN&u
"p=p@":>,1p&P*nr;ls"qZ$X!"o\K8"TSWAZ$pS+F`MG@EGoZ.BPM@$rc%aQpi-4Ns).gQ&8Z,rAmntH
:.79%0J>%1/M@#U%PB=b0/>@C3^#_o4ZPo#"&-'>')hn*"TJT&!r2fr!WE'0"TS].JjLn))\s)%(Dmu-
q\o_X)AsA/(DcudrttbRrYkbT!ur:$*r[5c*?#_-%0lq2!!33)#6"i="pG)1!<<*#!<<*2)CLmV#Q=]*
"U+u0!WW6%rW3'#pAb9r!X&Z*!!!'!!"49>+V>:p$P!d_',:E\rY>JMrYYAI(`4&)'b_2m&J5Zk(`F;1
)&Eqr$3g_A$P!%E!t>VE#lOu9#RUqJ$4.Rn/=HbHrW)ourW<'$!<N<#!;ZZt!<WH*qu?m+3=,Zc!quZt
!<E6&!S@AT!<N?*!rDs!!<WN)!!-L:nc8Xi!WiE(qu?g""9ni@!!!-%#8F/!CM\09EcQ5@Df'<,DK#Mo
qf)FPs)S*YrbrEeDJj<,BOY4G9h%?-1bg[;r@S+(0)dF90/>CF4?l5(6pNOa^K_HS!!!$%p]LR!quZ]p
rrN*!#Qk&5!-qKg)B/qt'GVH%)&jP9r>YqZ)]BS2rYGbU(`=20)]S_q!$2%[#p194*ubt-$jQn2!!33)
"oSW8"U"o/!<E9,"pY/8SO3S[!!`Q."9S]*!!3'#!!2fo!s&H+"TAB$!WE'0F\Wqh&If-Y&el&s(`4&)
!u2Od(\nmR(Ddi&'bqDr'E/UT',;?&)]BM,&Io3U#RLhHrXB8G%1ERM#R:VA$4@7RrY#DB&Yhf!r;Zfu
rW3'#quQj!p&GR'!WrH'!!*'"'djas!!;ior;l`phZ*c[!WrN*qZ$j&#Rgt?[K$R&!;urq!!30)#Q=]0
"TSW;Vj_:DF*7J("`n[&Df9UlEV4AMEW0tdE,96!>Z46]4?,/PqChq'0)dFE0/>FG4?uJ55rh#/^`*@_
!rr<%!WrQ0"pG/5"9S],rW2iq!<E9$!##D6#lo'N+XIp>'GVE$)B9e>*?G,!%3$6))&O/+(`4,/)]Tjr
*<I9)+oWYh+WhU:%L<(<!W)j8!<NB-"pP;;"p>#0!<EE6!s&c`U':T%!W`?$!r`6"!ri;q!!<6'"9e](
!!E3#'6$qh*"EDd%M9?i)&jJ2'bh>s(B,-V)&X8-()7Ms')iIQ&.oNg'c%W()]KV.&.ApE#ltDBr=0MN
$jm:H#RLhG$k=$m&e5[;W!WM-qu?]tqZ6`uoDemm!rDs$'-%Sa!!;iorW2WkrW2-]!s&H)!W2p'!X8l5
!sm6[&a',q!X/i.!"T>8!"Pj"BS(8IF`qqNFE@;!rH&!\s)\-Zqf)UVrcAHcCLpgO8j>6j0`E^+0JWP^
(,7Kr/hJY/1H%9V5Y4g<68buD$jI4Ir;[-*"U>8:"U"r1!rW/r!<3-"!!iT*#QSdN+"e9,'aPQl)BBnA
*Zc@$*!7,u)&`Dj"W80r)]Tms*Xs59,UF]\+W_I5$O-\6qZ$a"!sAc3rWa#>"U"o.!!Wo7$j_bJ!!!H6
!W;uu!W3!!!VQKq!<N?+rVup%rW![L>Sndr%1NdY',MT/*#TJ(',22u)#bBW(D[\t&J,KO%Km:T'GhYd
)?^om&I]!F#TX3Y$k3^X%LrpV$OR1H$4I@Q%i6<$)AJGu!!!H4qu?]urW<3'!Wi/uq#CBqr;[''!tH%P
!!!&n!<3)l!;cfd!<*#q!;urt!!r]3!t>?G#6b)1kPt_e"pb50#m(G6!!f7#DLH^,GQ)akF`__HEcZ;D
FSp7_FE;L"EW:(YF")*GB44q<5rC2B.4Ql$0JbRC1G^a>0.nk32*4#b3^#l*951.<%g<:Ar;[0+"pkP?
"p>#0!<Mrq!W`?(qu?s-!,6*l-l<^+'bqK$)BL"D+!1D%!ur:")Z1H[)B0Y:*ZlLI+X/-0,6oD9*uGRs
"9JB""p"c-"9eu7r<N]9#QXo*!>$#0Jc5WM$O-G.!!<-%!WiE(p&G<u!WrQ*!!3E)!"`dS*?c"*%1Wm^
(`ab@)&3_d&ebur)#bC4(DRSp%LidQ$OdLV&el)u)&aD2'b:TS"U55>$OmRW&.]6\$k!CL$P!a^%LW[Z
+XKa=#6b)7"T8<)!<WH-!s/Mj!!NK4%h]!HkQ(S^p]:$fquQTn%flb9"p"](!s/]-?5*G@!U'Lo!X8o2
!!EZ0!!8UtFEVtUqfiBjG'.nJF*)MHr,r3cFE;JCrc.jV.<'-;@9QMs3@uL#,UY&n0Jk[G2)@!B0J>(8
3'BPg1c76i3TNO:$3LG0!"&`/#71\A"p>#0!VZQq!<NB$!##V<@<*h@*>fP-(E"27+sA'N*Zk;$!?<'V
)@.9%*$$(C+X/-0,7,P<+Wh[>%gW7<qZ.*,!WrQ."pYD?$471Lr;Zp8#J28\!!*<*r;[''!sA`/!W`>q
!!`N+!sAT(!t"r,4C;tN)ANen%M0<l+!MdF'G(fg'c.]()&O/(&e>EZ$4.%J%hTHi()If*)&Eqq#Qt87
#R_(O&.oHa%LiCHrX08H&/5li"pYMa(<A*.!s/].r;[$&!sJf0!WhZg"pPMI%gWCBr;ciuli?\Zq#L9m
q#CU#"UGD9!!!6)"U(P"$j-On!#YhA#6=f,$31&3L:;8JG^4R\H[9s^GBS+OrH/!\q0"E6F)c,8DfTr?
B3Iql2(g7$,:"Tb/MK">2)?s@0JP=<1c@9P1GD*W2NY0a!"/o.!"8i-!<`T4#R1G7!WiDs!!30&"9&9X
!<<9';gBu@*>o\3)]^"D,9nBU+<VaJ*ZZ7@)]Kb:*??1C+!)ID*?caZ/1)DQ%13=D"9\W)q#M-3#7(YC
#R:J4!!`Q,A;pWj!<<3!!!`N,"9S]+!<Dfn#6=i-"9AK*$2soH;0=3)'+YTb',DK-+<;:4&.fEe'c%Q$
(D[`!&ePWbr=0\V'cS8@*uGRt#m^b@#RUqK%hK<c&.T*V$iUP7%K6hF#mM1Z&osBJ!!NH+r;[$&!WrQ.
!Whonqu?`u!r`9/"U,nM"98E&!<N;f!;Z`m!<3)i!!NB)"9\f/rW!*('e04g!p0Ih!<`T-!!3E+!"TKT
\T2n:G^=acI!U$\r,qjX"*Sp7HN&7EH?O:EBkqX-E+)O)/1)Yg,palc.4d//2)I'A/MJt<2Dm9E/hJ_E
3_\3[(^(*Fqu@')!sJo6"Tnf-!<Mlo!<NB&!"K)2!WYQ=0I[t\)]g+F+qGqF,pX`\+sA*P+!)ID*Zk2#
$6:*))B^C[0I@VDrW!''"pG,2quQ`r"p"o7$4$e9rW!*6#U$Je!r)a!!<N?)!<Mcl"p"f/!<<6.rW!Zu
I4--I%M09i)&jS:)AWqr%hTEf'EAjA'fcp?&J>p'-S$AV$31&/#Rh1Q%hB6b',(re$3pkG%1N^Q#R1J=
*Yp?B)[QKI!<<*#!!!$$!WrK)p](9pq>^X!!WiQ2r;[*j!X/W,!<N?)l2^GVrW2Wk"9JZ-!Wi9##Qt,.
%FkR`!!E3#rrMBb*<QHG!!*9*#7aGLC3O]BH[^KoHZsRRF`qqNF`_^'EY<M>H[^ElI!^0aG&hD0>>dsR
1&rd&-N5A6-n6c$1GgmA/LrJ13'&oM/1NtV,X0mP+US>P!<`K&!!NE,"U"o/rW2Zl!<NB&!!!0$!!k*E
/h@t^+!N$--3bbB,U4KV+T<H#+<_pO*ZZ4A+X89X+<;:3$NpG0!X/f5"9\W(rrN#t%0QtG#6=f)'c[2h
[42L]!!3<,!rW*#!<N;l!!WH*"9AK*#lXf<.?u/#$k3da)]Th:)Aa,$&.]<a&cNCF',23!r#$%b*[)^M
*?#\*$jQn>#n7IZrXfPO',2,l$j["A$4[RS#mLM7*@(_0^G6B"!!E<,"Tnf)!!30&!VZTo!W2p+!<WB)
#7:V7"TY4u%/p5/!X&T+h>mNUoDf7#"pY//!!EB3!!(IH!!`N1"T\W*!WhTe!<NE'!&4T\%1Or<Ap/-;
I"6ctHZsOPFEVkOF`_\GEcQ5EH@:<oIscTjI=6?R<C&>i.Ochrr[8p=.4Qi"0/>=</hAJ)1cdcX/Lr;,
2B/31+q>7g!!!B4"9&9$!<N?*!s/Mo!"]26!!!$'!<<*8X=l4I+!W-3.0(do-Pe$T,U4KV+<VgO,:"ER
)]BhG/1r4b$N:#2!X&Z2#6tG:"8r8t!"K&9$jH\3!=TP?ITm3\"o\K'$O?k4!!!&o!;QU3!X&Q)!sSi/
!#)1S*srGj)''_:)&<o!&H*.=&-WXY'GhZ-rZ)Lj,:P6!,o6mg!!3?4%1j0N'GqJt'c%Mr$jQn=#n7FQ
!s8`?(BB.t&HN4;!!<W:"9J#mrrW)u!WiH*#lt5<#m:Y:i!'_k!!<9*!s.6YrW2Wk!WrZ6rW!K<!"BQ&
&/5*S$47"@!s8T*nc/XjqZ$Wt"9&9+!X9)E*klW8Esd5DKReJrG&qbJGQ)gmGB\:WH$XjeJGt-WJ:;fe
De<$<1*dtb+XA?[-RgMr/MAe41,:R</hSk93BB#N2*s):CRcIe%M&[B!t#88!WE'$!<N<'nGj1'!s&B&
!s/K($_9I8+sSHa-78U9"XPE>,9e?0,Q8qp,9e<W,pt#['+"R;$j$P8"pP;:"U"o/!Wi/u%KQ\;"9AoO
&HG[`%1WFDrW!!*"p4&i"T\].!WW<$":kP@Q80Ki%i--()&<nu&.e^K#7_4T&ebrp)&4)3+X89\.4Qep
*>/PV!!3?4%M06erY5GL(]G6i'bC`Y#RLhG#6YMY'ED*h&.esM!!!'-#Qt1u!!39*!W<!,!<N9&"ptJ5
%LLDc%/p8+!qu]k!VQNg!!!&l!!30&!Vl]t3sl,nrX&c5"9S]+nGiOiqZ$Wt!r`0@!<iiA'q0hsGCG:#
IsZE_FEMbOH$XgaI"$TsJqAXRJe<Q^FD+lQ5Vj`-)B'S:+<r3^"Y;8\1G^fc0c;`&1Gq*N3Ar`B4>:Ej
0E;@a%LE7A#6b21rW)ounGj:)!sAZ*!!*-'"p]QW0de>".3fuY,5ibc+p/u3+sZt1$RR5L-mg,Y)&!Je
#6"c#"Tnl0!Wi9#rW!Q3!sAi/)A>rX,QIfG#R(51"9Rff:]UY%!s&B&!sJr8G=`kf&fVf.'bLrc$k!CL
$OdIS&/,cp)&aJ9,:G)q.jcAV&e"sF!X&`8%1a$b'c%Q$)&aG4(_mVl$OI(D#71DL'2T+I,6.]F#mCA5
"pG&/nGiXp"9S]%!!<6*#6Ff(#!rb!!<E6&rW)ltrW)s!qZ?cuiW/rZ!!2ut%06G4df:9i#m^hC"p+i*
!V$-i!Vucr!W<!6!sf/I?FOcnJW,21H?XLRFa&(VH[UDCJj"dAKnP)0J:2`cAl_A[.j5cE',;B)+<r6`
/ho4B2)?s@0f(^J2Dm`g2_Ha(?ca_t!!!**"pG28"Tnf,q#L$e'`eC>!s&B%!<`K57Z/oH.l/Ip*ZcI'
+UB24+!;^N+Wqs-,7>bC-7:/f+W;"'$4?b=rWiN0#5n]>"pP55!W`<'!sAT(#7Ue:#lmN,+T;?B!X&Z*
!WW8i!;ca4!<WK-!<<*$#6kW'IiAk4+W)%0%LWUMrWiQ3$4ZtG0G>3>)]^%H-nHnr*>Ane"Tnf."pk\I
%hTEg'c%W()]Tk;(`!bn"qD7N!snrs[N,5GrW<9+"9S]+nGiXq"U"o(!!!$;!sAW)!!<6Q$ig80!WW3%
!sA`/!<<*#!Wr?'rW3'#iW'#^"9JH$"9SW+"cWE\#Qb27#6k;4!<MfmquQWo!!2ut#6b)D-e*6[ISQ2R
JU;WbF`qtRH@('nM1g>/KnP#+HZjCE@T,WL,T@I1%hKEl*?c^W/2/k=3B&cL0JPCE4ZG8c:HU`n*4A<P
$31M<!!!0,"U,#1!UKdh!<WH,!WE'3"TT/JXZ7g\4rY^f*ZlOJ+<MX2*ZlXU+W;@E+sR"20d7b^(_?uV
"9o/?$k*LO#m^_<"9eu6"U"o/!WrW4!<<HD$5!^JUcT4u!>#J9!!<;m!;urq!!E<*"U"o+!"K58'Fpf`
&JZl/*"rei$2k,:#n%@^&e#?g)&jSN+<i'W,TRO*!WW3$!sJr;%1Wm[&J>cm(Dn&1*ZQ(9(C^Q\*"<Jg
!2)4Z"oo#5!!*!#!WiE(nGi[s"p>#/quHWq#64c3`W-&?!r`0+!sJl4!s&B%!<W0$!WiE(p&OI[('=a@
!!<T/#64b\#6Y,0!WrT0"9SZ*oDnahnc1BT)3V48RVAF5G^F^ZGBnL^IXZBUJ<GnDI<TR>>#7[N1bC'u
*#B;%'Gqf5-7LK!1)i&-2)[BM1Gh$L3BK8W1H[WT_Fk%8!!!6*!!)s"!WiB'li7+g!WrN&!"8o/%1$lu
+%m;;&f`(n,7u1H,pXBB,r[S.-RBlS((gr\r<<<.#RUJ;&ISsR#mUV;"pG,5"pG)3"U"u@"pFu,%M9MX
49,H`"UkS8!!2TiquQZp"9AT-!s/B$)$C$Q"_DBS3!MMT'bq>k%M'-a'GCcU(Fgg3+;,_7(_mYo$k!@I
#6k>8#7(\H&,m+?')iRF(]G<_)&O)%&IedD%hTPT2ZNg_!!!6*!!!$#m/R7n"p>#0q#CEr!r`0./0tE!
#QOo+!!*3)!rN#u!W<*!!TO.^!s])7r;Zp#!3m@=!<3-#!WE0#!VHHi!V-4^#89>\JT6okM1BtuF`r%V
H@($jK6_?UGB%4s8N\XO)]B\<+s7pG)B9kE-S$f'1,LjD0/GRI2E3]S1d",Q1bC8[LEI'8!s8E$quQKk
qZ$TsqZ$Zu!Wi/u*X;lmYsBa)(,%$],U=]a-n-Vr0f1@&-7gVl)\NGXr;['*#mptF#RCb9$6BKZ"pYA8
!!<K2"9eu2!=9><#6bKtF;,#j#RCV;!V$0d!W2p#!!!'%!W2pW":>8LUbEZH&1f"F(DIW%)B9_;,:4EG
*$cgS*#/qg!<<*'$4dUT$4."G$4I@R%hB9d&.T?j(]G-[&.K9i!!rf9O)Y^6#6P&/kPtbi"U"o/!Vl]r
!<io;!<@KI!X\o7!<<*$!S.5_!X8o;"p4i4!!#k+!!*'*"9JH$"9AT+!<Mloq>p0f$3UYfRIb$GGBnk$
4FqX!H$OUOAnGasG&qA!6T?_H+rqO:'GD,q)BL(K-7:/i.k`\4/i>aM1,_3S2`NTI0Jt+@c;"?S'bgQH
!s&H(!UKgd!V6:+"oo<S\Ka3_,;(u1-RpZ!/0u>[,q]N_1bKm`$j[%?!s8B#-NO;Q"pP24!<E9+!WWK9
#QY&5"U"u0!<W]0+0mj+$P='Q!sAc1!qlWi!<E0$q#LEqqZ%c@$31TJXV`r?+tPQ!*$6@M,TIL5)'^X_
-QNg2%h9!U$7lGf"pG5<$OdFN#6b56#R^tH',qYq%M93]&.AjN%KIQT2?4!l&-)\2!WiDg!!WQ/!s/N)
!Vl^$!XA]*#cdq+"oSE%"9IN_o`,=#!<<9/!WW3$!3,kr!XJr1r;Zs$!s8T*p&Opio)LZP"ro\El?Zoj
M2lsuCi3ruCik&QA4S^6.4$&T)]^%E*>]>"(Eb1`2E!BG/hJqD4#S`A.k_Gm4ZYJ_0JZBH;8ZHC*!.&`
rW!$%"9S\k!<*#k!$V[K"r<K-2]+>45r'Z3.4$2i2aTqd('t$C!W`<*$4daX"8r3.":5DB"p+c)":PVA
!WE'+":,25#lk/V!&CJ\5l_Dq(^C$@"9o&5pAk!imJor`%0-MBNMnZM1cdfP*?ZUN+"&d(4=:XB!!*<2
$kF!e(_R2Z!!3E9&ePTY!<<*%$Od@I"9Sc5%1<IT#n8?a0W%&7%KI4H!!!$&"98Pi!<30#!r`5r!"9,:
%00?q!"9#7!!<DV!!*-)rW!B1#RUP5TE"s%!"&u9"T/6&!<`N-!rW,q!;cff!(R7q!$<DuXI4!=ATE06
?>"1d9JdtE2(p:#+<27<*[2s_1,qKf9iYD*AoN-SO+D+P9fjgW3&icI-m(fG3*jF&'EA4>'*\@8!s&K*
!UTje!<*#l!'(5k!!!-%OEb+d-RUf=1+"\90H15s!Y5V?!sAZ+!X&]5$4IFX()\,9,:>3.8l7u2,8:4[
!!NQ0rW!-:*"tQ:63R8f#8%.?!!*0*"8;fk!V6<h!&Fuo!<<-#Mfi;Z,pb<0/gE#10,Xil!"KDB$4[RW
%1<FG#RV%R'cA#7+!)XV2a/r<'F=[<$j?nC!WW3@,8WSB4otW_!=o>4!!33)!qcQl!W)lr!rN)p!!!'!
!!!6+4<4P+f)YgOqZ$j-%Kd.PV#U`!!!<<-"pFi("Tef0!s/Mt!;cfg!"]29!<N6N,)>,i4!$+:-n$8u
+!W*\-mBZQ+<_mM*[3!b2ap_YF*`7cKT2:fSskt5S=#M(MI\n).5`eF4$dB!.hE9t&e>6Kr;ciulN$nb
p&G-r#RgV3#SI8N\N:9$"qLP2#Qb5<"p+o4#RDsc!s&B%!=Thn1,_'N3C$)-9hS)U=&i'o8gt&H!"&iB
%N.X=)$1!B$OR(>r;Zj"!VcZi!Up("!XK8I!rr<4!F`Dr$NL59qu@-.#R^qE%2'Hp(_dD_rW!$/)'p^T
.kE8*0J+b$,V(W+1,q-1!WW?:%NcQ37^3[.!WWQ6"TeQ%!<N;q!;cfp!;uri!"K)2"p+tU#6b\?!!!''
"5s4^!<WN3q>^s3$O>_u$kNFE!<<-("8i-&!X&T-!Wi#qquQ<f3s,H_"W@da+fgi3,oJ9\*Z#G2(_I5e
&/5s$*[3@-<b?E%LQ@XaQC+>DY-P40UnOWbUS`0$1+F(r+U]`k]+u;')\ND]!s/5uq>p0frW2]m!W`H0
rW!H>!!3LiGs;W9&IAL=!!i`+!##G<"p>#6%MTg+.l9:L4Zttr8PT1](K+79?W^Sj%0Zn8$NL0RT*#Q9
'FOsE!V?Bc!Ug"]!X9#B!rr<2!!!4]F?9[,&.8XA!"B5<"ptnX)]]k6'b_,g&f;]:.4d)*0.eY#+WMFA
,qgl4)up*M!#G_EK;/GR%1igI!s/K(p]10kq>oj]#6Y,3!!iR$3;`a^!<`E'!<<-%!rN)j!<3)u!$hXO
$k3FA!!*6-!!"`a&Hi.9!=&c.!<WB(!!!$$!WrN+!W`>u!<3&s!UTkP#6PMO'f;SS7M[*\'E]No#mCG:
$kaF#.n!fnP+%o2S"-%?Sti9gZEC-uS#X-%[>.4*+>b3Fa-dMa&e#Te!r`0"!W2p$!<N?*!Wr?%oDnjk
o`,!n"9&93"onu=$7M+!3!Tut"TT>I!W<!(!X&W2&g/bb48h8^4[)(s77g0I9hJ)`CKY48%KuhH!&gNr
!#5nJ'ajm>!!2rs!!3$"p]9pc!W`9$8,rVj!s]/9!!<H+"pP/QNf5k%'+#'I*YSkf%MK^"*ZZ4C,UY#h
-6sf`.kWM-.3ouP&ISpa0-`D!!!*<I$Uh.L!##P<&-r17!s&K*!VHHi!U0Re":,GG#8$qM!!'!4!!!?+
"Tno1!<N?*rW<*#pAk-mrrW-"(^13U&.A[H$NL/.[Ntnn!!!91#6k>6!<N0$r<*$#rrMoqqZ6$`$N^D2
$kX=0Wh(4K">_k7#n%(I$k<pk018r\KTqgfOGo-XNfTBkSY;aMSt2INWR./C3\iOD`*!KY!t5SO$N^5,
rrN&u!<E9$"9/H%!VHHl!V??n!WW6"!Yk_9"ptniU6ZN+!%n6T#R1D7!W`?1%i-?A3^cA&5<M.t7nZTS
<;]c);cd"J;^W(h)/-$8rW!$+$5!XD!<3)t!!!&r!rE#c!!iW."pbA6"Tnf)!#>\G-)$YC(^;ht#n.:V
(E+22,:P#d,Q8hg+<M^L*$Z[M)]'5*)]]t=+!*s'%0RCgEjeU@!WW3&$jZb3!s&N,!VHHk!TsFb!sJo3
r;[36!Z$AW!rrN*!!38r!!!&h!#,M?#m1/2!!!GJ&c`%:!rrH-"9S`(!Vlfq!W)ln!UKeF!XB)F$5<dR
Kop'`$4da[%h]Ni(a;.KC3+o]LOjeqF`qtSI"6p-NKKEmXhLEqW(TBbYa?[@#8%%A#n.1H!r`3"!WE'#
!<N?%"9&B#!VZTm!VHHl!C6\c!X8l<":bP=JraRZ$4d^X$k3RL!<<`Z0K;El8OPg.6V1'R=^,0=?<piD
CiiEA?P!r@RYM[Z$31&1$47"?rVus#!WE)u!Vc`q!Ug$f!C-_i"U5/7!WW9(!sS`4!X=@CD]B<#&.8s_
)&a;,-T3V(,9nWk1,:R=0J=t+-RUZ44#oSr)A"\)"@/K9+9iAU!!<9*!s/B$rr`9%q>gHorW2Hfr;d*&
!<E0#!<W0!$j$D4$33&/$3gP:!!;lp!sAi4"7Q9r!<<f=!',f7%fQG1#6k20quHTprW;uur;cftqZ6Nn
!!2Zk4TP]p$3pP2!Z6rs2&60+$j[Lh*[*sdDf0`HI<p-\EG]E%BP_X1I"I6;OdE/kWFs9*9F1t.#QXr3
#R(;.!;lls!riB#!r`5p!;lld!(Htn"9SW(!umE+3Z7u3#m(GG"99&d1H%[#>$bTGA7fLiCi433F)l/2
>ZP9Y@P+(`3rfKm%0HV7"pG,2!<<-%!W`<'!rW/q!ri;i!!NB)!WrQ.!sA`/!W;uu!W<!Q"sBAD4r=8,
"9fJ^'*oX;2_cj1*>]bE.4Qi!/M8\0-mq2W5qO`W1^f&F2ZX<u&Hhe.r<!!"p]19on,W:c!WiE(q>^Qu
!!!H5"98F"fDl$S%0-A/!rDs!"UYY:$lfW]#R:P<"U,)9#mgb:"UPGC0>%8k!!EH*!!rl&!;HTp!;6Hk
!;uri!"K&8%1`^E"p,;pRZS[-(F';#.j?')DJj'#DJsK7EGArd<)m%*@VKe)IZU1dNO%b?+rC1X"9AZ4
"TeK#!!3'#!!DrsrW2coqZ6Wqr;lWm(]amM"TSf5(."[\+qt[m#9!aG&i)C)5trS&=^YfP@pr_P@Us%]
Anc%!DcK8IZm#b^!!!E6#mUV9!<E9$!W<'$!s/Q%!W)ru!Ug!h!<W3%!WiB'qZ%fC#m:5:%3J3=Or"</
!=U:e!#[d\6XYG/Up.DE`5]pFe^tPdb-[%8<_k7a8WsP_!rr<5%1*.4!<3*!!ri;t!<*#f!;cd!!WiH*
q#Cs5%LE4;!!*V.PlUjm!!W]3qu@'.$kO'e(D[\t&.eaM#nR^`'+G3I%2Rk'!!!c4!!<?0#mKo#nH&Ri
r;cZpo`.#S"UPM;!!X#=$iiPhJjU=q&eGgA@VKFa?X-c8;GKeP6:==;:fCFu?Z:URP*+9H#QYA;!!!-,
#R(2/q>^KrrW;our<!!"p]10lrW)isp&GR+"onW/'akWS7&GJt%1rL=.Mb$59NGJ/A7fLiCM[j*E,fl<
EGT<)De<QmYRgd7$k!@H$3p_9!!!'%r;cs$!X&H(r;l`rrrMQg!!3!!rrMrr2?F$^!"9e\*!AQtE\e(=
$j6YX8n<-qKoqq$WN`kE_9('RdCPp,H#@1l9i%;]!!!E=&.AsOp&P$lquHZr!!2QhquQcurWDrr!s],:
"TAB)"98V=&In[=$j6P1!=95J&J,B[$k<1G%h/sV%M'*^&J+pB#A=;H#6"T*":,;="76*a!W3!!!rW,u
!WN6#!VZR8!WrN."T\T'!s/H8$Nan[A/$!p(c5,s@9H;p5r^Y!0H;i*3'BMk4Zbi*BQ/-`S/)nA"98E(
#7(S=!W`?!!!!'!!r2rt!WW8r!;?Nm!W;uu!WE'%!<<*$!r`0Y"9SZ=$j'qS<s&X,!['g1@q/nS?X-c?
@V0@lDJsH1CM7@!G&M)PN!B[i!<WN3#mUS6!!*-&quQ]s!!2irrrMoqr;lcqqZ-g"!<E0#qu@c=!!!-0
%1=$\!*?[4$l9Bl4(O&?][#*]g"PHNnb<"^'CsYVO,/R9Cl4)R$315:%hB*T"7lNf!Up*e!WE0!!rrAu
!!WK-!s/W3$8Df%!!!&O!!!-,$O$M9&ekui#m1/-!sT&=#mgkC#m^hI'+ksMB*/SC!WiK0#m^\9m/["a
q#^KprrN'"rrMoq!<E9#"9JZ-!rW**&fq#Y(1k-j2%(?J;bobC2(pF*+WqjL+XJNg0J4n*.QgR.>D]!O
!"0)<!sJr:#R:M9!s/9!"p"c,!s8Z/qu[!%!Wi&ro)\di#QXr-!WrK*!<N&t'G)2`"V"M2:a5ub>@V/U
C27QuBPS/sEHHAKH$OXXF)cGSF`3P@rW!?0"9AT."9S]+!<N9&rW)ltp]:R#!WiB'q#L<noDejlpAcE=
"U>8J)ZTjE=gM[)-;TbsW3sF\bKnYjhrO"ho_8%Dg;^N4Z*'UVXL/<:!t>_K%1EOI"9J/qp]9mbqZ6Zt
quZs$!W)j$!<N?)!!3<%!"o_R]F4cG!"9;I$O-b:!<<*$"8rE&"q1Y>$P<dY-s$BN!"B/:!!*6,!s7ii
r;lWor;ciuquQj!qZ$Zu!X&B(4Tb`g"TSN(#mq(Q%g<k%WIn>C:,jOB*uc%5(D[`#()\)7,9e6M*@s<7
5^&e#!!3Q9#7(VB#RCY>"9JT#!!30&"8rB$!s/N*!VZTe!W<!"!<NB%"9\f-!!!'!!&"BV#7V(A$lG7T
>ZblU?Y==uF*)SLG^4U_IXcluIscToLO!p1]*869#Qk&,!<W6&!WiB'qZ-TrrW;lsrrMoqquQBhqZ/_X
!!*0%!!Wo@#RLV6&gjcQNg@,VUo:K*]uA7De(31+hr3SSi7ur9e%Da(h]NIA'bC`[$OR1F"TnAt!!3$"
rW2lrq>g6jrW<!"rWE6'!W<!!!X/H%%0Qn9!"9&3SQQU+'b:WL!#bk?!s/N)!<N<)!sA]/#7LS74h(S%
!#Gn@!;us!!U]sd!VZZo!<3)u!r`5u!!**%r<!0(!<<0(rW"eZ#7CnC!rrZ5EMPiO*Zc7=()%;m&J>`l
(E+87*?,k6+tPB,9m0\O&HE%H&.T!L"9er3!r;lu!<NB&"T/?'!WiDt!;6Hm!WE'"!<W3%!<N<$!!!&u
!"T)7#Qau+!s3\V@pW>LC2j,k#'+d-G'J=\rdG9'I"6p%J;BtF+W(1[rWN9(qZ6KmrrMiqrrMoqqZ69g
!<E2t!!`Q+!='#>#6Xr*'bVO[n>NOl['mQ\`QQWWe^rL1i8WhsjqQn;in)Gset+rS%h0$Z%L`XL"p>#%
!!!&u!r`5m!;?Nn!rN0""98N$!!**&r;[9,#6b)-$j-SMbm=aX#Q"N#!W<!3!<E6(!sAi/#V)_a!WWK-
!sAc0l2^eapB(<oquHd!r;lcq!s&H)!VcX&!<if1#T*dJ>*NM[.462X)]9G+&J,Nf()\#0*#on9)&aJ<
-8@,TNDp)e#87d`#QOi+!sA]%!!**%q?-]urrMlpmf<Om!WrK)pAbp/#65#J$OLIILi?s;BPM@"CM@Hr
CD^o,EH?8HG^4R\I=[*1H^2-](C^HQ#mpk7!!!&o!;urp!ri;s!<3-!!UB_3!<WK2$4-q;!#?.bK\42Q
]=u2%aNMoWeCN:+gu.5Ul0@Qul08rJlKQODl]a(E%M0-_%1*7D"Tnf#!!!'!!r`5l!;6Hl!rW6$!r;lt
!s8E$%0d(D"9o&1])VgD$j?\-!<3)u!"K#3"9\f-!$E2*#m:_>$j$bB"R6!d!VZZp!;?Nj!!!&n!#GY=
"W7:?'L%sD0c^rA)]9J.'b_2o(E38nr>beW'c\591GrE^+!:Rp%1`XC!!*-'!WW5t!!**%r<*!"rW2co
o`>'or;lm!!!2cn/cl+m!<XQG\R9&V?XRV^B4YU`@:EbZBPM@$E,p&DH%(@#Lld4TU,X_)"U#)7rW2Wk
rW2`oq>gKrrW2lrrrMZj3!9Kp$jm(M!!"K]foMu1\A-50b08/Wd*^:kf%]0Glg4!(m.'cEp$g>Xc<*@?
#mUnK$jm:G"U"N"!!3'#rrMlpqZ-KorW)ouqZ?cuq#LBq%KQP1!s/K'#QhgM!!!$#pAb3q!W2p)!sJ`+
!X&K'4LYXr!!EB,!s&Gh!;urn!rN*!!WE)u!Up(J!<<*,'aG3K"HY5g0e3\<)AsA.()7N")]g.F*uu=A
*ZuUJ)]95L$9h.C'En^J$j?V2!<N<'q#CKt!WrQ'!rW/o!;cfr!<3)t!rW0#!Vl^Q!<E0##o*a]!?JOQ
B68<'=D;;R?X?uA>[CcG@qB=gD/aQ?IY3H/ULJn-YUBbW!=&c0!Whonm/d.errN#tqZ6Ek('"=;#RUtP
('G*J.*I10[)BJabfRoHr5g&'bgG)#jlYailLXoQqu==R\Ca+`"9],B%1EUN#6Y)'!!!'!!ri;l!;llq
!;urt!WW8q!!rZ."9er2!<<*B$38QW!!<3.!WW3$qZ$Zu!Wi3!"Tno/!!<N+!"1'l!<<B.!!!*'!Wh]h
r;lcsrWE'!q>^Krn,O(%!!!99!!!4rCF1MD1(#?:(`FG5()7N")BBn@*?,q;*?QCF)]9>=%Q-dYH2nfp
%0HM/!s/T-!Vucr!W3#u!Vufi!W<#u!Vc]r!Vufq!?;(>"q^h<)o.bDB3'C]F&u^S>Zt94=^#':@:a-d
Ci402FEr=gJraSsKnGTi((1HNklCP\quQj#rW<*#quHQop&G[*"9\l<('=ghf!gF,R)uJT[/RfS]tCti
]tV7q]tM2#ce.7EpAOjfbR`CO]=\b#'+kNS"pYD>"p=]%rrN-$rrMWi!!<*"q>gBnpAbd+!WrH'!X8W1
#aR^U!!*0-"SVor!W<!#!<`Q-rW!0*%KICs[K$R2!!!&p!V?Bj!W3#u"8r8^!&"?W#m(*7N@H(]-l=i[
'H\//()7Mu(E"/2)AsD2*$$(@*#fh7)`B<+F*@Th'*nL:!s/W/!rDs#!!**%!rW/s!;$<i!!!'!!rW3&
!WiE"!!33(!WE'1!XoGJI'QmX9PI^X?<:N9=8c/)='8d9ASH"!rbi9gH%(<jFG=gLQ%o>C&I.J"rrE$!
quZg!rrW3$quH`tr;ls"nc1QT()S0ZeV9-AXes:HXLGC:Y,n\+Y->13Un4*T\&[(Zlgj`7i9JOlc)qTl
*";lJ!X8r:"9JE#rrN*#rrMcmrW*'$!Wr?%pAk3op&P'm&-)\4%0-DNRfE]o'Fb6M"Tn8q"9J]/!s/?#
#R)%]BiG]F#6Ff(!!<-%quZiupAk0nquZj"rrW3$qZ-NorrM]k)$UNP!<>$A/gMDO(G?mP,7#A.'bhAt
()Iec(]kQn*<$rl+!DRD/M/8=Rkt*X"T\T'!X8c/qZ-Hnq#LBpquZftqZ-WsrrW*#!<N<!!!*-(rW"SQ
!!WR#ZrgF2;H.F9=^=?s;c-Cj<E<4*?!q/RB4u$qDf^/MFEE%X?uWG8!##P3!!!&h!<3*"!r2ru!ri<!
!<3)t!WW8n!##J>'H1cALldmeRBiT_WK3pKS!s>G+Io!pTqnWi[CsQ*g#MA[k4%BC\`dE2+UeDP!!EW7
"9SQ&rrN$!rrMfnquQg!rW20^!W`?'rW!,7!X&K'#m1J;"9\8r!W`<'rW<H.!<E0#$PWR@`r,l@#6Y#-
"9eT(rrW3$p]16nr;us#rrW3$p&P*no)KO6(B=F<P]/&i-R'WH+!)@D&/#]n()7r,'GM8s()If*)B9b>
+s\9P+tG6(;3q7k!!r],!<rZ-qZ-NppAk3orW<'$r;lcq$3://!s8Z/!s8T*qZ%oD"98E'$NL/BZBnZi
@U3&-;Gg1g77^-K;,^Ir=^#!5?!h&PBFelrEccACG'e.AEMj*S!!i?#rW2QirrN-$rr`3&rW<3'!<N)u
#6=i,!WrN+!V?@B#lkPogW>V@WMH)EP`q5sLl..NNJi[ON0^3@\@K)V[CsZ1hW*hho@^ma%FljO#6t5/
!=9#7!s/N"!ri;p!<3)s!r`5`!!*0.rW!(12Zs*]rVus%!qZHm!W)p4"9o)5!!<H+"<YDZ"TT#9!!!0*
"8W*"!r`5r!<*#r!X&T,!W`>a!##VL"TT^".4QA^*ZGt:*?,n0',:E\!#5DG*#','(Dn#/*$$+E*uuLR
.PO;B:]LJ$!rr?*!s/<"quHctpAk3orW<'$r;lcq!W`<'rW<9+!s8T+qZ$Wu"TABT#6P2jW)R#'?WpE(
9hnAT6q0aA:/Fhf<E<1'>$PEEAnYprDfB`@I<'"<RpZ4!#l4Q!!V69l!<N<(!sAK)rW<3'!<N)urrN$!
!!2]l&HrR_=k/G!S#<!KOH#9[N.lubL*;8(K8,GUVQ[8.YHYORbh(e;oD.@`[a9^F%LE+8!=/l4q#gTt
!!2cnrrN'"rrW0#jT#Gg(_29##lFZ'!s8,qrrMuu('=[C!rr<%!!=:/+U.uV"onZ+!s/Q-r<*'$quQZp
rW2cqrrMrrm/Rb%#R(3TB-/?;*#TV5*#fb2'GLEZ#nmsb',)&p()Ikf)A=&1*#p+L-n[J]RfEHl!WW3&
!Wi9#quQEirrMuurW2iqrrN-$qu[!%!Wi3!!<E<%!&4N\$^H]H=]Sa.;G^(\8OZ!77S$-F9i"Vb<E<4+
?=@AUB5).!Ed<(UD/"C)":>D8qZ-TsquQKk"9AQ*!sAK)rW<3'!<N&trW3!"!!2]l!!3ZD,.P:>QC4J=
Q]d>cM1pT\JfoVpJV/fBR\H[XWiieFa3i`,p%mgq\$t3:(CC3D!<r`("TAN'!ri;q!<3)s!r`5^!!E<&
VCDlM!!**%!<N;p!<3)p!WW9#!!rfC"uW@[!"9,7rW*'%!sJT*r;ultquHZrq#^QsjT#et!%+$^.2<X9
(D[l,)&F"c'*8j]')iLI',)&p(E!)g$5sg%+!`*Y3^J]nqu?d"!s8E%rrW3$oDnjkquZiuq>gNrrrW'"
!<N<"!!**%rW")H!'.Je>YS1!<)?=_84Gp35sn%084lNL:Jk%k=^5<C@h*$\B5DR4I!'7IE3<CN#Q"K$
!Vulr!Vl`q!WN6#"9/N'!s/N)!Vufn!V?@(#RO>]KTh:ZSXPb(MMHn:J:INH(4CX^KoM@fTVJEdZb+-!
g#_f!k0CuO"5eJD%/p5."U,&-"o\Z(!s/N)!VZTo!W3#u!U9[b!WE'(!<<>I"onc,rW!!#!Wr#prrN*#
!s8W,!W)j"#7ge9SGiKm!<N9%!<NB&"8`/t!W<#r!W)rt!Ta:l#69*D0c(]A&eYin(`*o$r"K)CrXf;H
',))r(]G6S(Dn#.*W@/`4>LN5qu?m%!s8T*!W<'"!W<#m!<*#t!WW8r!<3*!!rN-$!Wi3!!<E9$!&+]]
P&=Z$;c6Li9hS&H69m^u5=%Y)7Rp$C:/Fhh=^>ED@Uit`Dg$DJCO^,_Z4I6;!!E<(!WrQ&!r`5s!!30%
!WW;t!s/N)!VZTm!VHFH$kTJ'O+WLVQ'78eLP12,I!^0cH[:!bI=d<;Q^aVCWNWeF`m`o6o&\6LZH1ZD
%K6>-"TAT)#6+l+"9\f/!WiDs!;uru!rW-"!:9dd!WN6#!!WT,2$a3a#Q+Q'!WiDt!;uru!r`9&!Wi6"
#lt,2"ona"S,ifl!!!&u"9/H%!WE0!!W<#q!W<)u!VHHe!!30&"9&92!XGGP-P@"%&.oQk(`!f!r"B#A
rX]eV&ebrn'c%T&)&X>2)]Tk@1H%ge+8l3=!s/N)!W<'"!V6<f!VZTo!W<)u!s&H(quH`urW"VX(VWpQ
8ki#T9M.iE69dRo4$5Yj5XIk.84lQO;H?t,?=.)LB5M[4FE)bSJ@dfFqZ$TsrW;s!rrW3$q>gNrrrW$!
!WiB'oDndiq#CR--.mU&JI73lOH,3QJUMihG5QJ$G'A4\KoD1\R\$:RYdV9ig?7kcg=sZ]jA6Bd!<**$
"o\]+"o\W-!s8T+!VZTg!U]pf!WE/u!!Wr6d/Xs_"T/9!!WN0!!;Z`q!r`9&!Wi3!#Qb&3"WA-"&H_n2
!<E9$!sAZ+!!*-!!rW0!!:p6W!!36+#5nN5+.5J+"q;"O&/,cp().Dp')iLC&H31@&.ofn&ebro(E"/3
)]BS3)^-Xm13?1i!!36*!s8H&rW3'#nGrFepAk0nquQs&!s/N%!!30&"9&9I#W'#06pO=98kDK?5s@@j
3&ioZ4$>en6:=:792AJe>$P?>?tF']DK9lEHA6L?CBX\?!W<!"!<N?!!s/N*!Vufr!WE/u"9/H&!V?Bg
!W)jO%7A[5GBnmuMMQq8H?XFMDf9N3E,]f;FaAUpNfoZpS>)sb[`$YPkih*ahR;$j&cr@D"9\f/"U>59
"oSQ,!s8T*!VZTh!Ug!k!<N?*!r`0*"TSc0Ym^s>"9&9#!W2rm!W<)u!s&H(qZ$j'#mV"Y?iUK2!!`N*
!WrK)!!!$"!W<)u!W<#j!UB^f!X8o6rW!F<E"s6"%1<OR&JQ#s'GLEW+V5.p%LimY&.oKe&ec$!*?Q:?
(DRf1,r%&HHN4-P"pG,,!<N<(!VZT[!;urr!WrN+!Wi6"'EJ:<!<<+HPXSMB8Oc-95sILn3&^an+Z;;?
4$>eo6UaO=:K(=t>$PBCB52=,I!gNmNM-CX#6b2.!!E<'!WiK&"9\f/!W`?!!<*#t!X8].!s/N)!V?Bl
!W<'$!<<-!!B^>dN3[AWJq\l0J:)T_E,B?(BP;*pCM[m-G(#%%Nf]HjS"Za`^!#'fkj%<h`PB,"%LWLE
!WiK0#6b;0"9\f/!W`>r!;QZl!;-<o!<WK.rW3K/!Wrre?j6c7!<<-$quH`trrW0#q?$Tt!<N<!!!WN0
"U#\QE;BP:!<WB(rW!!#!X&E'r;lltoE"F]qu@K6"pkP;!!&H<*YAnn$OI4Q',D;s&eY*S#S.CT%1E[U
%hS^P(D7K&+!MdG()%N,+s\okSH'!&#R1A2!<*!#!WiD]!;llo!WW9"!!E<*"U,)m!4>^%9MA)J5<V+j
3Ar]L0ekF>1c@9Q4$>eo6qC!J<*!+)>[V)TCNY&SH\QU_#Rq+H"T\T'!<E6'"8i9(!s/N)q>gNrquZm#
rrW3$oDf[.!<N<)!s&B%!X&]6#KUn4JVAi0HZsQ7E,0-!AH$$c@q9.`Bl%g8J;9#@NffTqTW#9:d+mgP
mGQNnkSk<J#mCA2":#/8qud-)!s/K(pAk!imJm[s"9el/"9nr."9>/,'E.t5!<N<"!!!&s!r;us!s&H(
q>^g&!sT8OaT)MG!W<!!!s8E$"T\Z,!s/Q&!W2ro!TsFt!XB);!!!(k,9.4'%LWRN%h]Qj&eY*Rrso&<
rX8f:%fHq=&Jc-#+!MdG(DI]++!E*YQQQJ:":,,1!W3!!!T=%T!W<*"!W<!4!<iT.#nsjB:J+5M6TdCi
2`3BG0E*R@0/,.;2)dNW5!VM-9i4hh='8j=AnlF8I1(@SG/>^7#m:J7!!*!"rWE-&"9S`-!<N#srrN$!
rr`9&rrM]k"9AN)!sJT''*A:>%NWi1H[pa$I<KUIBObFV?2e(R?!^lH@qKOuH@^a)MN*aaS"m4&bh2%E
n)i,roK3g!"pY20"9\u8"U+`*rrW3$pAk*llMq@p!sA],!sJ]*"TX_d%/g2+!W2p!!<WGp!WW8t!!rZ,
!Wif9Y5et3qu?a"!rN$"!WrQ)!rN)S!#>S@$j$D/+,hNh$k!IN#n%4T'+tlf%fHh@$k*LO$k3^G%il2n
'cJ,:*ul.7(`FD;,US+7!!3--"98H*!s/N)nGr(ZpAm_b!W`9%!<<*$#6=f10r[oG7n,p43]K#S1,(=3
.k3&"/1rS11Gq*P4[DP0:Jk"h='K*EC3"TGH%CII;ZR"$#m1/."9eN&!WiE(q#LEqquZm#rrW3$nc/am
!<WK(!"oA6!Y7H/E.<7bIX,sMAmeeE=8l5L<E<1'>$PHICiaoOJqf/CP*_cA]?&O^lgX2fWUjU1%Km%=
!!<N5"U"W'rrMioqZ6Bjo`,C%!s/H(!rr<("`+2Cp&G'orWDrtrW3!"!!2rsrW*3)!X]-P$4m"6!<WE$
!!E<)!s/Q%!V$0h!V69q!!!$"!!`u4!"_MB-QWa*$OI+I%1a$^%h/sE$RH,e$OdIS%hB3`'cA#7*uu:<
(`4,0.3i_K!!!'*"98K-"Tnf,iW/QN$31)-!!!',!!*+#30d6784>g-3&NKH0.e\'-mpAj-n6`!0/5:A
3^,o%9MSD^<*<R>C2nE>F,5C7GQ7^F#6Or-"pOi*rrW3$q>gKqquZm#rrW3$nGiUk!sJT'%g)e7$"U/X
I!g?gFDb_u<rc+s:B45j:FAt9;c[%.Ao2U7IY3H7O-?$1\&HePkO%KeVXB6M#7(P9!!EW7"9SN&!WiB'
pAk$jl2V.l!WW3$!rr<-$9[q\!!<*$rW<'#q>pHn$NU;1!<`W3#<tN["T/6#!s8B#!!3$"qZ66fr;lKi
"T\Z)!!Wo3!"WaO.NB$/$4.%I$k<gZ%1Dq<#R_%M%Ls![&JPHe*?Q@D*?,mq(Cr,A>E/[`"U+u.!s]#4
!Wh<]o)Ta0!!*-$!!3H,"9<ar:eXGJ4utSX0J4n+-RSd;(aULV.4Zu(1H.B\77p6J:Jt8"A86%(EGl>H
JV9<h!!WW0!!3B0!sAE%rrMoqrW2ourr`9&rrMTh!<WK(!#,J7"p0^LFEr:\F`;)(=AMIX7nH>O8Kpc$
:K(D'Ao2U7J;&i=OHuZI_9UfqlK.!&kGA^i%0Zb4"9Su:!s/B$rW2cop]9X[%06J0!!*-$!"C(`!!!&o
!!!*!"8i6#!VHF%!<WB("q1S@'n-,f!!E3#!<N<"!!!'!!r;rg!;uri!#Pb>!!!02!!*(S9J%.q$OI+I
$OdIS%1EUC#l=oP$4@7O%M''^'Gqf3*uu@A)&=)0,9KsS!<<B0"98N/"Te_n!;-?c!W)j6!WrE&!=8`2
!17Cs8Ol'.2`*3@.k)hl,Q&]3+sSB].4d/03Bff#8P;cR<*NdDCiFE9K7S?C!!!90"98K."Tni*!WN6$
!VcZo!W3!!"9&?%!WN2j!!*0)quAhc!iglsG'\=NCLpaJ7mK:(6:=4/6:+(08PN,d?tXA"I"R01NKTp9
]?&O[kiUX(l`Up&&-i7:!so/5quH`tqZ-9inGrCc!<NB&!!iZ,!"!ZL#64f!!!!'!"8i6"!VHF*!X&N(
"Ub;<&Y/n+!!iT*!!33!!!!'!!r;rg!;lli!!<9*!!!E0$31/.S3/GB&do!QrX8o=%1ERLr<N9,+peSa
$k3[W%hTKm*$64B*?5n3)^-%?:n@ml#RLY7!X8c.iW/ZQqZ$Wu"9&9,#QP/2Y#eOk76WOf1bp[6.4-;a
+<MXF*?H7D+X8<_/MT.F5t+:88ki2c?=[bfF*MnYG,5BC#mpk:!X8c/q#U9krW2`prW2Nh!<WN'!"o\C
_K:$CGB.M4@9-#d3&`i[4t&TX4?Pem6UsjL>%),bH@^a)M3"+([DL8Djlb1-l*D32&deaA!XAl"!;-B`
!<3)t!!30(#6"T."98o6_?:DM!WE'"!s8B#"9AT,!Wr6"rrD`m&H`1;!!<N-$PofD!rr]2!!!)t!!!'!
!r;rg!!E<'!WiDp!"f;9!!!$*!!<4u4=V*[$jd7Mr<r`8#m^G5'*\XG#7(SA$OdIS%hB6d(`XS<*>0>2
(`")9(aD&>%KHP>#64c."5s7V!VZQp!sJT'2$X*f!4Q!'5t!gm1,(7.-6s`V*?6":)B0V8*?QIP.PEV=
5!qb/84u`Y>@D/]F*VkQE2EsJ!!Ef<!!*6*!W<#t!VcZo!VZZo!V-3k!sST&3t)G?FE25@DeEQc;+3K!
0/>FG3&``R2`a,h7nlrfA8ZU@JqSo;QD:Xrak#>/gXF<]*t8Vh"onZ-!r`2o!;$<_!<3)t!"/f3#Qau+
"98E(ecP^K!<r])!!!'!!r;ri!"f><!WW</!!<Y'!!3--!WW3%qZ$TsrW;uurrMZj"9AN)!Whro!W`E-
rW#(d!!<5"5pR*X%1*@N%1EXQ#mUV:!sA`1"pP;<#mq(M%M'*_'Gqc1*ZQ.=(`+/:)^m#9'*/(F#QOl.
!pBX\!;cfj!!*0)rW#(c!!r\:=[kPA4#8QC.OHDa*ul4;(`4&+(`=53+<r9c1,h<]6UaL:9iG/#ASZ@3
EcQ/p$j-JC#lju/!rDrt!VcZn!VZZo!WN/l!!*3+quAee%aTB8Ble*$?Wg)f1Fah)0/G@<0JG4<3'9Mu
:KLq=FFA[kKSYe_Wj]mof\PNJXiht("VV+@!!E>p!;$<f!!!&s!<3)u!"8i/#7:P5!<`B&"kEeR!!<6-
"TeQ%!!3'#q>p6h%KQ\;!rrH1!!!(_#Qau2rVus#!W)ls!r2lf!!E<'!WiDq!!30("o\K("on`*&#h];
',:r_$4RCO$OR.D"9&?K!sAc2"pbMB$k3[W&/#]p*$-.@*#f_1)^61I/Z]Tf!"K/4!!ED_!;cfk!!30'
"TAB2"onr0\5YjY6TQtT/1;bs+W_U@(`!i$'GV>u(E+;;,q:Q*3^5nt77^-N=C5TREcuA:Kp`5N!"]A8
!<`K*quH`tq#L?opB(6no)Jdo#5eH;$k(C%BkML&@9cf(4>8*.-RgSs.Ocet,;1i34[Vh>>\A&&I=Hd#
O.</V_TpZ`hVl)`+Vk4o"onW,!qZKb!Vl]q!W2rs!W2p,!<i`1!!!$'!"%?^!!3#u!<r])!!!'!!r;ro
!;lg$!<i]1!!<N+!!J>h"TSc+!!*-%qZ-Wtq#U$d"9AN)!Whro!WiK.rW"ST!!<4s4!YLT%LEIN$OR4I
#6Y).!!**&"9eu7#RUqK%M'*`'c@u5*ZZ4>(`"#"+;uRgV@j"3#m(),"Tneb!;cfk!!30'"TAB8"onr0
Yu*kN6TQtS.OH;[)]9G,'E&Oe',2/t)]p:Q/Mf@L5XIk.9N,)%ASQ1+D.]2q"U+l7"98Q*"U"i,rW)ou
q#L<nq#^Hpo)Jgm"U=l)3t)A6DJ*R%C1(1A76)tH+sJ6W,9e<V-7LQ'3Bou/=_)DoH@1-lNLHcP_9C<V
g"=WZ*>Skj"98H,"8Mro!;-Ba!<*#r!!*0*r;[$1$Ob,^"UY,-!<WE$!!WH+!s/N)!WE-#!VHF&!<i]1
!!3B*!We8d$318/!!*-%qZ-Wtq#UHpo`,*q!<N<'p&G0q!X&]+!"B)3!<AEO+Vbb'$47.JrWrT0"8i-A
!WrQ/#7(YE%1Wm\&f)?)+!)FB)]0;,*ZZgmV%3_0"o\K'"U"ki!;ccn!VcWs!<E9*rW#+d!!`Lt<BiQ4
4#/B:,Te!D().An&.]9_&/#Wl)''kI/29(G5!VJ)9N,,'Anl4&DJPYs!!`K1!WW6*"TnK#q>gEoq?$Np
rW)Wl!WiN1qu@?9#.8G\Ao_Wn<_c"@/0l>Z*?G,!-6=<U.5!J?6VCHgCisuJH[gsAVmO7^c-Fnnb-;d#
"q1S6!XJr1oDnOboDngjqu?cu!<W6#$ipM<"cWWd"9nl,!!2rs!!3'$qZ6`uo`,I&"U>,0!X8W.#E&Zp
!!W?%!<N<!!<3,r!V-6g!VZQs!<N<+"o\K%"TAB$IKWFg()@G[$3^_B#RCS8qu@i?!WrT1#RUqK%hK<d
()e28*uu=?(DR`,+>c-O%0lk6rW!!'"9RQ_quQTnrW*'%!sJT'%gE"9!/FuE4@;1c/12V_)CQ@8&eGQ`
%1NdW&/#Zn)^$FV0JtmS5=.e4;d3^CC2@a+EKl%T#64u-!!<E/!s8E%!!<*"r;cZpqZ?Zro)Jjn!sT#.
!"fDAR<r4NEG8]X90bBd,9@a?rY>SP)&sbD,qC]05Y+g[BleHAG^YF9VR+%XaiW&d`2FCf"ptD3!so/5
g]76Qp&GC%!!<3l$NL/7#5A/u!WE2u!ri;t!;um-!X/f2!!*6'"r)Id'*8:8!!*-%qu?d!!Wr/unc8Rg
pAb<s!WrT0rW!B/!!!=&DAsB*%LNLL$2t22"TeK#(BFR?"pbPE%M'*`'GhZ/+<DL@(`!l(*X<rI98<r\
!!3'!!X&T+i;ifWq>gNrrW3*&"TAB_"TSN3=ar:k5<1GK-6X?G'bV#e$k*LO$k3[X',DK.,:P6%3BTMl
78$Q_?tO.jDfK]^DZBtA#6=f)"9\f.!Wi0"quHctq#UHrq>p6h"T\W+":#50!%Je!Qr[a6Am8,&4uFl:
*>]A#%hK?f(`X\H/i>d];-[aRFEMbQLR"X=]`,k[dalL$',Cf]"98N0"p+i(!!30$!94(X!VZR%!<`B&
!?O#s!!ri1q#CBqrWDuurrMio!s8`4"8r3("trLU%Kcb2!!*-%qu?d!!Wr/ur;cNkquQNl"9JZ."U4c'
#8SVE)&a"o$N:A2#QP#'!$21D"U>AC%M'-a'Gqc1+<DI='bqN(+Xf*RBb(=H"9&<#!TF+Z!<*#p!!!'!
!r`<$!'C>`!#[;V1HdcX0InFl)]'/!%L`^P#mq"I%1a'd)'0tM/Mf@J5!_S0;-7.9CN"35CReH."98`0
!!!*"!Vlf_!VZR#!!!$#!X&Z4#Qai'4<Z_j;IjEL=\hFJ1b9ml'b:ZZ$OmX](`jqQ1HS!#>@qeoFEMk_
PG#%g_o'=;d*H_H&d]'R!X&`3!Wi9#rW1pWrrMus!s&H'!"&c0!!!0(@fQQ6"o\Q"!!30&"8N#u!VcWt
!<WN2"TAB*!WuC8('as?!!*-%qu?d!!Wr/unGrOhpAb?t!WrQ/"oA9(%L\^H+:AMW$46V9!!N)t*WZ?H
#7:kL&.oQj(`XV@*Z5\+'c7u;/2;09'`\4:d/X4K!<W0$rW!W5!!!N>V`$n"1b^C)*ubt.%h/mQ,RF__
#n%.P&JZ0(+t"rt3'0;i77pEX?"IhmF)kZi2@9Ec$3^8,!!3'#r<*$#mK)q[#6=l."U55<!rN$<()snb
BOG.I9gUou/LDJP$jHk?$4RR_)^6^c3Z^X`=_2JjF*)Y[Oe/S^^qmb/`SF6)%1<aT"9\o3!r2lM!"o>8
!<<*#!<<<(RK*ft!<E6(!W2ot!VQTn!W)it!X&Q/#6b#+#6t6s!"fA<"9&9$!Wi3!!W`?(p]9mb!!2cn
"p"f/"9er0qu@!(!0o,_#m^nFr<NE/"Si$:!<WK1$4ICU&ebus*$6:D(_[Gp)B^@^1k$kj!rr<*!R^rK
!<W-#qu@?1!W\l\7kl_P.jQ5V((q,d$46\;+UJMb%h]Tp*?lj_1,h9Y5t+CB<a93QFEDP-Zkj2P!t,>1
!!!'#!rE*"!q-0^!!iT,!sAf5#RCP2!':5f$+!rQ>$4iu5rpkU-QNm."9Sf5$kO-l+Xf'*6V^cpD/jW=
H%_<NW3sCS]#_MB.iAU$'+G*J"U"Z(r;lfrhZ*`Z!sA])!!WN."TYqH)#aL;!WrK)r;Zfuo`G!krW!T5
!sJl3!<E0,!5edA":#,5!!!&s!!30&!q63j!U]ph!<NB&"98K!!!\-I+:\bh$N121"p=Z$*ruHI#7:kM
&/#Wk(E+86)AWnq(*4VF4[s]1%0-D4!SIJL!!**%qZH`r&HMk3O'=h+1Gg[1+WVC5%h/pF#pBWa%M09h
)BL+O/M]7H5!h_4;HI+8DfBQ;Cmt_7!!<N2qZ-Tsr<*$#mfE%\!s&H*"9\o6#RCP2!'LA`!2"@?>$+j"
5s.([-m'04"U##9%M9Hq+t59.6r$lqD/jZAI#!u[Wj][RZGsZ!)\<8_&.AaH"U"o0rW<'"f`2*T!sA]'
!!!$)!Djs?#Qk/1rW2osquQWqqZ6Zr!<E<$"9\`+!"a8O!!33+"TAH!!!30&!q-0X!!**%r<!$#qZ$s*
5'S1a%20-S"U5#3"9SE"+9;NH"U>AC%M06d'G_N')Aj2#%i?K6,Y;<R"TSN(!s-gM!W`?(r<!'%!W)j3
"%A)03AWZL-mToR'G1f`$OR4K$k=?j&eu6'+=/Hh1H.B[6UsjM=^Gc\CM&$KEruCB!<rZ(!!!&o!q66_
!!rZ,!WrQ/"pYA8qZ%`G;kI/q<EW'a4ukAJ+W(^r#RV"Q'Gql:.l9@X:g.CH'Q\JFJ;fqmXgl-RX2DoH
'*\^L%1<(=#6b54!s/N)!U]se!U]pl!<N?*!WiE%!!``7Du^CM#6OZ#quHp%!WrK*q>pNprW3-(#6=o/
!&kVj!!EH.!W`?!!!!'!!q66Y!!!&t!WW8u!!`u=SfSg`((L6H!X&T+qZ%f@!WrQ0#RUtM&.oNg'c%Q$
'b_,h)C?UR;1p\-!!!$$!<C[Nr;lp"rW<3'!Wi/u0FSGo2a',_1b0pu*#92!%L`aT%1a!_'c.f1+snfn
1cRT_6qC*T>@;2cARL"_3s>N_!<WE$!<3)t!r`8j!V?@!!<E6'!sAc2"pP2,!&Y?*^JA$6>#7XQ4>\T6
)\W\j%M9Em*$H[^2Es`1>@h\oH@LX3T;]!*^TaQIem9'l"pPA>rW`W3"U"o/!<Mfmq>gKqmJm7g!r`9&
!Wi6""sh#&#65&3o`,0s!<N<)!Wr6"qu@$(!<<<3!!Wn3$iL&-!sA]-qZ-WsrW;QimK!4e!!<-#qZ%',
%$i%](`<ee"9\f.!W2p-!<N?+"U55>$k<g\&ebrX'FPQe%hBX/,:?c`!sef*rW1[PrrDuuq?$Ztq>`/[
UcCe)5;t2D,p+!?'+bZa%hK?e'c.c/+XJQh0JtjR5t+CD=^>KOE+3()XUGC3!<3)u!9XCU!<*#u!WiH+
"9Sc1"9SH#2$+Z$9j:Y%;+O&<2_QO#(_[Mr()e29,UtN/6;(9`B5`!BKSu1lXL#OPXIm#P-Plac!sSu.
#6Y25!s/Mi!;ure!!WH*!WrN+!W<!&$?HFR!"&f"!<3)u!rE#r!!iT*!!Wl4$Qmdo!!<9)!s8?"!!3$"
n,_tXquQNl#6RAN(CM2q"TAH(!s/Q'!<E6(rWEQ3"U>AC%M'*_&JG'V&J5N_%NHrK.>1n/!!!$$!s8VV
!<*#q!r`5s!#5`8Shhrc4>895,9@a>'+kfh',;<#(`OJ<,Ub2s1,V'U6qL-Q>$bZQD.HY@C^^.@rrN&u
quHctmK)t\rW3!"r<!-)"9S`%!$D\SX[kib<D#\F3]&B6*Z5e4*$6@N-nR8=78?okBQ/8;K8YqaVm!J=
\Z:tCN$/T0!WiN0#6tM>"p>#0!UKgb!Up*g!<`H*!s8W&!!EG3!=K53!!36(!Vufh!W2p$!<N?*#Qb*(
4TGT`!!<6'!Wi3!rrN$!o`>!mnc8Ofq>^Krr;[95"0F'W*t\VU!!3<-"TAK'"T&?D#71bJ%hB3_&ebrm
%h&gT)_!^$R2->6!!*3,"TneX!<3)r!r`5r!%nWg^I9J=4>SQ<-6sZP()%>r(E",2*Zu[T.k`V62EF)n
9i>"q?=IS^Bi_J_'`A%2!VHEm!;urn!r`5o!<*$!!r2p!!Wi,t1(G#A<B48_9L_<23AN*1+!)OK,pt,n
0fVHj;HdODEd`b,S"m$h[C<HCOPE&I!<<*$rWWT4#R:P;!s/Mo!;cco!V-6h!WE-%!s/N&!!NE(f)PdU
r;Zp#"pG,'!<*!!!;cfq!"&c2!!!K9S,`ir!rW/t!<*#r!qlZm!WW9"!;HQk!Vud0!<N6$!<iZ4:43Wj
"UP51!XK&9rWNB."pYA3"U##9$OmUF%i,`j'bq5d$kX=$7V>p-"p+f*":,26!SIJP!<<3!!r`5r!&"?X
%pkJQ5;G5R-n-Vl*uPh0(`FD9+<i'Y.P<J52E*]a8l8\n>%)#P??(U6$jce3rrVclr;lQmp&P*nrrW*#
rW<*#rrDor0*`/&TKZ7E;G'5?5WLPK,pale/1iM12EaK(='fEQF+B7<UT(B'\Zhm5\!&*R"o\N$"pYA=
#6k>6!WhWf!!<*"nc8Of"p+i.!!!'(rVut,!;lg!!t,D<oDnjk('"=8!<N<&!!Nc2!!I4B!!39)!!!$#
quH`tq?$BlqZ?cup&P*nrW<*#q>_63!rr<)%KHYCW#?]W&Hi(9$OR.E#:9Z\#RCY>"pG5<$OmRU%hB6c
()IMh%i-$-=Gddm!"9&3"UYJ:!SIJQ!W)ru!VZR5#lkAS]f/;+68U,B0.J.d)&XA7+<i$V-Rp]&'Jq^,
3BT]'<Ei[2@VB+OI%MMa!!rQ(rrV`krrM`np&G-p!<W0$rrW0#q#D`F!"C*j6W6*M9gM*75;t;J/1iM1
1Gq*Q6:t-Z@:sJ$K92\'X/lW8\uM7-bsE?S$N:&)"pP;<#6k;5!p]jd!r`5k!;Z^"!WrE&#7pe6"2Y$<
!WE'$":Y_BoDnmlrW!K1!X&Z,!!a,:"VJi\&c`.:!rr<&!W2ot!Vlfl!Vult!VQKn!W<'"!Vl^5!<W?&
"UY;6!(;bU*t&2T#7(VC#mgkC#7(56*si8]$OdIS&/#Wk()IVq&K;`XI7OD>!"&o3"UPD9!W2rS!<3)t
!ri;p!&+WZ$3O>*01RrU0.ne),p=<M*ZlOM,pt,m/hf(=3'9Gq9iG.s>$Y]EEh$5=!!!6&!!*-%nc/^l
!<Voqp&GF#!WiH+"9S`-!<Mop0EM4]"^J5o>"qLV6pX%!2`*<H1c@<S4[DS5<Es$KEdEG$R\QaYWj&.u
c%%2U"U=r+rWNK1#6k>7!WhWf!WW9'rW2Bd'`e=:!s&B)#R:J4!1O&j!WW3%#R:M&!!!'!!XSr1!!!'4
!#.3rrW!*,!rr<&!W2rt!W)rm!Vult!Vl`q!<3)u!WW8r!"f85!<WK-!WWCU;A(8^%LE@GrX/]4rWa2E
$4I@Q$k!CN%MBKl()If))&OMP@#t9e#Qb27"9o)8!s.'TrrN$!!<E2o!&+HW#6bg/DDOs?1bC.)-mg/^
+<VgP-7LJt0/,+<3Boo'9i4nm>?bNKLoCX_!!*/g!<3)l!qlU#!<N<)!sA]-!Whup0E;(V"rEqY6XN8R
6U![u5!1kd3BKAh6qC$M=C,QUG(5:-Q(+A=TVJ9oe1)FK#6Ol)#m1;5"U5,5!s/Mh!<3-"!UKdg!<E6&
qZ$g%C+92g!!!-%!s/N)qZ$TsrW<*#rW!*&!s8T+!WE'$$P,5;rW!!#"9\W(qZ-*dq#^QspAk3or;ls"
pAc$2!X/c.!#5taT0!#j#6thN#n%.K#6kD>+Uenp&Io0U$P*sj(DIf5+sA3\0TnU#!!!'+#R1J:"9JVW
!<3)u!ri;p!"o>9!!"#X0==h&3[cC2/gi"p-2o(i,q(;B0*Esd3^ZLI8Ou]_>$>0;>I%-7rVus%"7?-h
!V?En!VZR#!<E6'!s8Z.!Whil-lj<c^LT#m4?Z/%5X@_%5!D4u7S?NU='K'FE-m:nLQS'pR@0D%h0'>W
&I8LA!<<*#!WrQ/"Tnf,l2^hcrW23_rW2uu":"tY"pt8/":,&/!!<*!"p"c."U"l-rW!*("T\T+$N:#.
!<ASk"TAB'"pG)0rW)fqncAOfrrMiorrN'"!!2cn3!'3d!Wi?7!*#<k'H.N&'+,'U$3pb?$4[[`'+YKX
$P+!m(D@oC/hK@LNGeh%!!!'-$3p_:!WhupirK)[r;ls"p&H]G!sJc2!#l/SX<9,R/NGO7.P*"p,U=`e
0/>:;0JPIJ7SZNE;I<d:De#u+&.SU=!X8f0n,WIhrrW0%rrW-#rW2`nrrN-$r<!'%!V6:E!rs>MD7D5`
83p$C6Uj[=77B[;9i>%r?!h,XFF]7'K8uCfPG45nW\#G&"Tno1r;[!%!sJf0!U0Ua!r`5a!!30("o\KL
!XSk"":P87%Kc\2!s&B%!<N?+"U"o/!<<*&"onW-&I/:E#/:ufr;Zp("p4o)!<3)k!;urr!r`<%!VcZo
!W<'"!VHEn!X&E%-NX8QBoatX.2*7'%h8pO"9Si9%h]E_#mUbF%MBX$,q:;o6][68(B+:=":#,6!s/K(
fDtpPr<!!"rrDfo/-?"V!!!<*&pL!;,XO.:0etO=/1Dts/i#=C2)I0N5!qh8;,p[q;eE//*$G4\!WiK+
mf<@grrW0%quZftpAk3orrW-$!<N;o!<)sL#lkclXAh&X7nHHR<E)gk:Jk.s?XdS[Cik&VLlIIWNeW.J
e&F=)%g`CA!rN$%!<WH-!WhNcrrW0#k5Ynl"98E)#QOuI8e_F/!t>G7!W<#t!WE'3!<E6&!<WE*!!!0&
!%25n%KHS0!!39*!W<#s!V?Bj!W<)u"9/Ds!<*#t!WW8o!!**%rW!Q7!!!Im<&6NX&Jl&i$O?k9":,nS
%LiaM"pYG=#TG<D-9Oh)RfETl(CL9G"9\K$g&V-Rr<!!"p&Gp2"98E&#QP&CSmk,a4>8fV3&WTI/MAn=
rAk*D5!hM#;@[&8:LIgYXpP[>(^g<D!Vucr!VQKp!<E9""8r<"!VZTo!WN6"!s&H(nGjsC!!sUBDcL=I
9j:n1?X?r>>@1oSCN"9<IY<E0Pb!qhNfTRN+X-q3!>5P2!!E?+!s/Mf!<3-"!TsFo!<N<*#n6q=%p/l;
#RLhF"TAB&!<WB#!!WH+"9\c+!r`0-!X(3d&c_n?"98E&qu?`u!ri?%!VHHl!W3#t"9/Dt!;urs!ri;o
!!E<&!!*0#!!Wh#J.<;7#Q>)H#mLM:$4RLR#RCbF$j[1U-R:<.CR>P0!!Wl="9S`-!W<#t!VcZU!<*#u
!r`5q!!WH+"9JQ*"9&9C%\o",/j([B3]oJa2`a)f6U<q'7S$0A85EAa;Hn^M(&e19$jQh7!Vufr!VZQq
!<N?#"9/H&!rW/p!<*$!!rW3&!W`>m!!!'!!%&G`SM`oA:L7XIC1q3nD/jZ?G^bC+OcPTgR"p<IUVS>b
#m_.O"8Mp"!WrN+!U0Ua!r`3#!U0S$!<N?+"9o)2!WWsQ=qV,E'F=a>!X/f3!W<!2!s],="9So>#QP&P
O9Q3q!"&r+!!NB)!s8T*o`4slr;um!rrMoqrW3!"rrW3$oDgTI!s&B,%0-A=>_OXI,8:=f%1<FK%1a!Y
#n.=U&.TBj0Ju.<Jfk3s%0ut9"U"o/!W<!#!<N9&g]7<SrW;osrr=kU!!*-("U,#0!!N]0!"rk-5WVD!
2EO5k5XIn18Ol3@:/=Y[:eb;%@#C'o"oo#8!!!'%q#LBpp](?r!Wr9%r;uoup]19orrW-$!WiB'nGiOl
-jfqU*-A,_=_h\\C3"?6F*;eTI"$g1PEqN&OdqPnY,sc!!>,Y?!<Mur"T\]-!W`>e!<3-!!U9Xh!<WH.
"9S`(!!iT5!3Q;2$NL/1!!NW8#6Ol)'`eLG$k*FK!!aPFKg,PG!#5kD!WrN%!!**%rW<3'!WhuprW2s!
qucs"q>gHpquZiuoDf@%!!!$%#7^_P40E0/!Y#&7#7CnH$k3a]%i,Tj+t+Q\&o4%I('"=9!sAW+!s8T+
!WE'%!<E6&!Sd\S!WE/s!W<!%!<N?+"9\T&*s2lN+@j4r0d\e:3''2e5X@e.8k)3D='SU"3/P"`+8l0A
!<<*#q#L?op](?r!Wr9%r;uoup]1<prW<$#!WiE(mf4U;&-sjjesTB-?!h#OBPD3tDg$MTI#4,XOGn"a
g6"<%#R1D7qZ-No"T\]-!W`>e!<3-!!U9Xh!<WH."U"o(!"/i8\gIX]!!a&C!s/?#"9AQ,%heg@$m;u6
%0-tH#mLP9!s/<"#6=l."9S`-!VQNm!W<)t"9&>u!;urr!r`5g!%J*W"s+CsUIYIk)]04u$4.(U*ubq-
'/276NK#b%!!N`4!!!'%!<N<'!WE'%!<E6&!V?BV!<*#t!rE#s!!NB)!s8T*qZ%]C#ppaH\mls65s[[r
3&s)j:.[`74&o<nVP-Bm"U583!!!&o!;urn!!30&!rN0!!r`3#!VcZp!WE0!"9/H&!Ug"6"qMG+0ppF>
6:kWq?sQu@?Yjn,DJX-ELm??,@kJW6'*eL;!quZu!<WE*!<MHcrrW-"r;c6c#6=o0"U,#3!r`0-!t#M<
!->OJ!"B;?r;[T8!WW6&"9\c+#EH%h'`\C=!rrH0"p=c'#QXu.!sA].!WhuprW2s!qucp!qZ-QqqZ?cu
mf3Fk":582!#I>[T4&EH+<i$R*uZ"<-ndhPMmRR+%1`78!<E8s!WN6$!Sd\S!W<)n!WN6$!rDs!!=/o/
!#Io)[<jS_6V'jC8jkp38PNDlT>Z9\'bg':r;lZn!W`?(qucm!r;lZnrrN*#r<*'$rrMTh!s8c>&L%Vh
&5pHiP"82M@:a%^@:!GZE.<>TkFiVC.0p:f"TSN(!VcWu!<WE*!<MHcrrW-"l2V%j!sJl4"9S`)!"Au6
$NLP;!1/cl"p#5A(^1-P$47:Y!!3@9dNA\o!WW?'!s&T4#6Xl(#QXu/!sA].!WhuprW2s!qucp!qZ-Qq
qZ?cun,O@.!Wr]:#mUe;!AnqrHpTJ4+!)OR4&g`uN&Ck?!#>P7&Hhq2pAt9qrrLmTrW2s!p&Y-orrMus
*X3#\$P<[S6AE+;?;=$Z6UXLJCm:lb4TPO#!!!W6r;Ziu!Vl`n!VcWr!<N?#"8r<"!VcZp!WE0!"9/H&
!V-4=!<WH0%M]]o*>TPiQ-6%D?s?]7=^Q*$Xhq>E)@eD3&L%ee!!36)!VcWu!WrK*!<MHcrrW-"l2V%j
"9eu5"9JW'!WrH+#6Ol)"Te[gi.r$D!#,J;)J6\A!rr<,!!!<-!!!0.#mUS1!!iT,!sA`/!s/N$!;ccq
!W<)t"9&>u!;urq!ri;j!!NB)":,>8r;[B9#7`b,J<,kUQ^<VP6P]Y2rW!$$#S."7!;HTo!ri;i!:Bjd
!W<)m!<N<(!W)j!!<ri4rW!N5'c%ofJXs!P[CEW@M,PT!&H2Y3!=')8qu?]tq#L<np](?r!Wr9%r;uou
p]1<prW<$#rrW3$nGj^6"UGSN$jd1D%j</L?')2(`lH9E\XmIo(aft)'+u-&%fQG0!<WAt!<!!!!U9[b
!rW/t!:Tt7!<NB-"pG,3!<N<'!!N]7"TSN0!!*35-!chE_RQ+P3=Gm*!!3#u#RLS5!!<H5#6Xl(#Qb)1
"9\f/!WhuprW2s!qucp!qZ-QqqZ6g"!<DTh!s/W3#lO`'!qH<s"TSN)":YnO!rN&n!WE0#!Sd\S!W<)m
!WN3$!W)j<!X/f0!!!00#m:55%LE:M)]05%&Hr.B!!*-'$kEdD!!!&q!;llm!!30&!rN0!!rW/p!<3*!
!rW6$!ri;k!!NB,#n7CP'EnaQ'bq8g'ce/-+Y5,j-RK`@+V4Pf"!/O&%K-8-!s//sr<!!"l2^hcr;l3a
)?BmB"U5,5!s/K(!!!66$j[1J#6b>C%13:A!<`N(!!Nc9!!!K0rW!6-#Qk&,!XB&<"8i-#!WrQ("9JZ,
!VQNm!W<)t"+U~>

%%EndBinary
grestore
np
grestore
gsave
125.841 410.531 mo
167.798 410.531 li
167.798 353.277 li
125.841 353.277 li
cp
clp
125.79 353.19 mo
167.81 353.19 li
167.81 410.61 li
125.79 410.61 li
cp
/0 /CSA get_res setcolorspace
gsave
clp
[1 0 0 -1 0 570 ]ct
[42.02 0 0 -57.42 125.79 216.81 ]ct
snap_to_device
Adobe_AGM_Image/AGMIMG_fl cf /ASCII85Decode fl /RunLengthDecode filter ddf
<<
/T 1
/W 116 
/H 159 
/M[116 0 0 -159 0 159 ]
/BC 8 
/I true
/D[0 1 0 1 0 1 0 1 ]
/DS [
[AGMIMG_fl 116 string /rs cvx /pop cvx] cvx
[AGMIMG_fl 116 string /rs cvx /pop cvx] cvx
[AGMIMG_fl 116 string /rs cvx /pop cvx] cvx
[AGMIMG_fl 116 string /rs cvx /pop cvx] cvx
]
/O 3
>>
%%BeginBinary: 1
img
jT#Da!WiH+o`PL'"U5/7"9S]%!#YhA"U#&9!!!*2&f2/c"U,8G&.]Eh&ISpOqu@$-!rr<&"UGA;!r`3"
!UBa_!;?Nn!rE*"!ri;i!!WK,"9SZ+!r`0&$4dg^"n;R!#nRII!W`<'!Wi9#"9AT."9S>urr`6%rrMZj
q#LEqrrW0#lMq=r#RUtN&I&4<$k3^Pn,O()%1*+="UGJC#Qt//!s8Z.!Wi9#quQTnncAIbqZ-EmmJmIq
"U"i/!WiT)!!WT2"p+c+"9&9%%LN=8!!<9)!WgjPrrN-$rWE0'rr`6%rrWN0"9eu6"Tnf,q#D96"U>88
!!3?4%L<FQ)DtN;ML]D>4=V9`%/g/+!W<#t!W2ot!TF+U!W3$!"9&B%!V$0f!!E<("9er,!!*-)rW!?2
*B7#1=[Fb^&I8RFrW!!#"TnT%!!3'!"9JZ.!s85trr`6%rrMBbq>oj]"To#=%hB!I!Vl^'(Go!#=[Ok`
&-`4<r;[0,!<<3)"U5,4!Wr<&!!;orq#L!emf<1bnc/gp!WW6$!WE'&('ss@&HMe1$N^D4!W`E($31&-
"oA9%!<N9&f)YdNrW<'$!<N<$!!rZ-!sAc3"p=u.rW)s!qu@T;"pYGB"qhpc,&sdEj42&T^<PKn_3.kI
"p5nV"9R$Pq>pEo!!2forrMusrrN&u*!$6K#6k;2!snr4;2VlmV3$1]Pc1jQD)`"*&Hqk/!<<0!!r`5r
!;lot!U0U_!VcWt!<N?*!VQL4!XK/A$3pP5#QOs$L:+@^Ndc\HVm)D"1^O-hqu?]trW!!#!Wr?'qZ6a!
quQQmp&X@WrW2Wk"9AZ2#6Ol)&-`+;!%b%bBKdFn>a)L:-5$1V"9Jc1"9SN%!W`?(mJuJOrW2s!!!2rs
#6=l/"U527!r`0%!<WE*qZ%Z=$P!mZ-]m&bSqDWIF(]]QH#AJ=c-sNo.ME%#&-;G(rW2Wkr;lfrq>g*f
q>^["!WrQ/!rDut!W2p?!X&c4"98[@XEnDH5s?e>/3P^;8ogAuS0/@C!!ir7!W<!#"9S]+rW)ouqZ-Nq
r;l?en,NUm!sAc3"7lL7!X8`/!!d5>HXoT34XqC#4"_mMD3UZW(^pBE&ebHMr;[$)"9S]+!Wr?'rrW-"
o`4jimf3@h!;QWo!VZR/!X&Q)":"r-!!302i&2>Z(B=F9"pk2.$l*Htf`2<i!<<6.!Wr?$!<WE#!!!&S
!;lln!!E?*"9o&2"9SQ&"p+o2"9JW*rW!uB!#-l8goQ$MEcc8>KU%FBK84DNB8*GRc#FO2*!c0;!!3'#
!!2cnq>p<jquQ<f"p+l1"pY83quH]s!!<3'rW"&F!!NsCY&ur],U+0F.QT4,.l8C^,=ZddUJ:dh&I&ID
rW!!("TnW&!W`?'qZ-Kpr;kgV#6=o0"pYD;!q?6m%:?8^(dg)-,oddO2_#dm//\d54DD$l:]h"B#mL8-
!X/].rW*!#rWE9)!Wh'V!s&E(!Vl`o!W2p9!<E0#"q(M5!!NB2!!.9X!WW3&#S.:H!s/W+#Q4W/#&mZS
!"]SH"pY&,!<`N&!;HTF!!E?*!s&E#!<WB*!s88u)](-FhJRseH[UL"Lk^S<Ljs]/SsG4SH$dlo4p)6J
$Np,'rW2]mq#U3irrMNf!!E3'rW<-%rW2`n*srgXY;8<c+s8*W-mg5h/LD]%:.[`)4@Z*X,lf;!#6"T)
"U"l,rW)ouqZ-Wsq?$Zti;`u^"9er3rW<6(!<N>r!$2T=X>E0k.OQSj,p40J*YoD<5<C\I0fY;n%KI@H
!r`0-"U+u1!WiH+"9S]+rW(jV!W`<'rW<0&!W2rs!VQKo!s\](!sSmA?2=O&!<WE#!"&c/!!!FMGQ7^J
"TAB(!<WH,!W2ro!VZTV!!NB)!s/K(rW3'#rW!-'!WiH,"9SK$.0]hm9C90"IpRGJH?OXdK7\AhH@pm%
I!9^OF'XXdYTjc!!WiH-!s&Gl!<*$!!r`5r!:'Uh!<WH,!<<0""9JZ-!Vl^<%5c4`.l[nV'bLli*?laM
)C-ph/h8>!-T!5X`g.,;&H2Y1"9\W(p&P$lqZ6`uli?n_$NU;1!<N?,"U"i+!rW9'"9S>u&LG/A-o___
*Z,J&()@Pj!XfeB(^qB&*X4?_C]FGH!!!)t"TAK(!Wh-XrW*<,!sAc2"9S]+!<3'!!Ug!n#GO3Y$31&.
rW)s$q?%?5#64r@$36_Y!"&]+"9\f0"9SH#rrN'"g].N\"U>89!s8H&rW!$&!<<,t!#l"G$kasFhj7;p
J9P^bKR\Q+Jq/5oI"6j&IsV*D%WlQ<b/%$h!sAi<"onW)nGrRir<!!"k5Ynl!W`9$!<WH+!!<H/pAb6t
(EFR2C)T2c(B>6`%hos)+X89]/1rS*,qCT)0euLrSN$KI!!N9$!<WDt!;urq!ri;b!"T)4"U5,4!sAc2
!WW?."Te>t$j$[7>7`bF*![Z*&J,Tf%LWID#7D%T&.TKq+;u.UMi]Xk!!ri3!!3B0!s/N)h#ITZ!<N?+
"o\]-"U"o+!WE'!!rW8u!"8l@"T\Ue%1ECD!!*3"!!iT,!s8T+!s8Z2!!!0+!!$1oqu?d%!s/2t!!<*$
qZ-TrjT#bm"pkVB"Tnc,!WW3%"TnZ'(^^up)%6j-BX-TGCgUdqKTC\<Lk^M4It.HH%XibTJ9l?bJ8&(g
Rb(:L"t:)q"TSN)nGrRir;us!kl;.n"9el/!<<0(!s/W1!r`0O!t,PH!!"$9QGQKU)\s2/*!Zlc()\/<
.5!5(.46Ml+WVm`*toZ+X!n#[!!<-"!<`N(!;HQn!W)ou!U'Ln!<i]7#R(>5"9el/"U>//!#>_I$jQb4
%6T-?4<tIL(*Fn9',1uc$2t/K"pG/7#RUb>(+C@F,\a;+!"],6!!!$*#6P#.q>fRV$ipA1!X&Z2"pY>:
"U+f+$ig8.":,>?"onW+#Qju*$3gKF`"rCR#R1M9q>^[#!sA]-!W2p*"98T*'USq%$NLD4p](<r"9&H#
!<*$!!9O80!WrQ/"pYA7!!392&Io-V%gN@g=g%>HWJ[-E?X.GiJqei0L4t5/IJeI*I=Hj"Isc^!Kk#7R
cCQ!b-PZdQ!<3)u!r`5r!:^$u!<N<*"U5/4!!*-+$O-G./.F_'d^4^;DBU/:)Aa>.$kO0l*$?LU/M&A!
,pjub+sJEl3Z^4LSok#5&dRn+rrMuu!!2`m!!2lqqu@0-!sAf5#R:G3!<NN8#Q=`B!!!KiM9)Q79i_Z6
#8.^j)\Wl!&If'Q#6tJ4"W.LP$4IOi1Hm!C7@S>u!#,b?!!EE,!s/M]!!<6'!X&B("9S`/"9\T("T\W(
!s8W(!"oSB!"/c,?-nri(CpoS#7:Y@!r;m#!<WH-!s8?""pPA6'aW&1oDf!q!s8Z/q>gNrn,WFgo`,F%
#7:kD!XB/C%2^E=1`(_ef?'k;>>\1p>[V#]G'\OcJV&H'I=(s='mb4SIY!0,Jp_WUE->9/nr+_4%1NC-
!<3*"!rW/^!#PkG$O[(;!<`B&!t5DG=eD^_G"aA-*-35J*>]e:(_dVu)BBqF,q(5m-mg2b,pjuc+rqUJ
0,6df@/pB0"8r3$!WiDt!<*#s!ri;q!;lli!$_UP$O[%:!<iK(#8%C]@&L/sE^UrZ#[IiI#o+0j'GV>s
'+c,n$OI(E#6tMA%1s9i(DRZ,/.t.\@/pH2"p+c*rW<-%m/[+dpAc$3!sAc3"p=u.!!!$"!!*0'!<`Q/
!WW<+r;[=:GZ,Fe!<i]8!!EK4#mU2*"T\Z,"9\i+!;lg&#n[@AK)bl["8Dir!rW5b!!NB)!WrK)pAd2U
$46k9!"^Cb!%`!"o"f`_<F'BUG&bB9BP2I1G'JFaIXQWjG^"=SG^4XaIt<3'IW8q@I;EP@hZQ%a'GL]=
!;QZf!<3)r!($\d!!*92%LW=<!!Eu9!"),S]n\cp'HAVS2_ot6*uQ:E)AsJ7+!DmU-7:2h-6sf[+X/*T
+r:b5/g;N'XV1^8#lO`)!X&Q)!VcZo!WE0"!VZTo!W<'"!VZQr!XB)>rW"&D'EA+D9:!S[7jo2n-6al^
D\`ik(DRVu(`*r&'+k]`r!O>M%M9?i(C^Tf.30NlX:kX8$NgA/!X&W.p&OmgquQTn#QXu0"pYD>"TnQ$
*<ZZT#QOi."pbS="HpQ"!!!'#'+"dK&.J[F#mUP,!!WH*!WrK*!W<!'!<<-#!!<50o`,!n!r`;l!;QU!
!<N?+"9S]"!$M@K%134R(CMO1^<![18kr`*C1^p\B5"npF)Q5CEcueVrd#K-G'.nLG'J=[I!g?jIt`]'
DKM7cUA#NJ)@HECrrM`lq>p3g!W`?'qZ%uF!!!*/%hT-K%1*"C;ja#(63dZ+(E=8,&fi'7,psf]+<;OK
,:"T6-5RsS,U4HT*ZZ4@+=Jfa(a;X+Bup>\%0le3!s8]/!VZTn!WN6#!VZQq!<E9$!rrDu!%@mJ"UY\C
!"&u3%9B!lLIr-i*$6:@&df6_@1sCg(_dSu)B'G/()7Jpr=Ai<'bM)p*[DR7*ChSl`rHAT#Qb#."9enr
!<3*!!WW8s!!iT-"9o):#R(8+!!`]<%1NLU!tGD<C6'P;!"B,;#Qt,-!WrQ-!<ri5o`,*q!<N?+r<3T4
"9JZ*%MAi2!!i]0q>^Krr;u6a#6=i,!s8Z-!VcX.!WrH'$OK%i_5i#h6;:cn?!UcQ$[HQ(CVOh/DK^&>
Fo6P(H$=FSFa&(VH@(!dI!pU"I<0"7A#&%#+:o%]!!*-%o)SRep&P'mq#CKt!s8W'!#R,;TS-/j#RqXc
%L`gd.30BLE[)hN,p=<?+XSQ`-R^>h,U4KV+<MXErYlLk,:F]S&JuL#Yt,*#$3L;/!X/]!!;HTk!<*!!
!r`9%!q?78."n:L<%JLm+<)%-%iQ].&J&:^'+Pcj&/?*%)&aA0(DRVtq%FDU)BK_-#S@e\X[NEq$O-_7
!sJer!!`N*!WiH+!Wi)s"p"f/"U>88qZ$s)!WWuE!!"j?8.#7qrs8T(!W`9$rW33*!sSu4oDeso!WrQ%
":>/0!"8i/EWuLJ"8W#t!WE/d!!!'!!r`9%!WE'S!WrE&"UkeH&./n>W5sci4[)SH>?,$EBOt^b@;Khs
DfBN7EGorEH?spbH?j^XGBeE3H4P@KH@:<gFGZE:BpZd_#7ge:rVus#!Ug$d!VQKn!WE'J!<N?'!!*<.
!!<3$15r,A,S(7u,8q.0*?,e0'bMB*E$$/@,Tn0R-n5-D$77#B+<M[H*?6";rYcCj+rhIT7Q2f-Sd,6&
#6Y#."p=c'q>g-grrDuu"9JW,!s/B$rrN*!,Qn/K!<<*SN2U;7&IfR'*>BA5)\`hm#7h;O%LrgZ&.T?k
)B8Yq!?)jT)#b?N().Gr()RVn-9Ee'?C:rs$jd+<!sShs!!<3%!<W6&!WiE(q#CR!!WrQ/!rN$3!<`E'
!!HEc%g)q7"pG)/!<`Q/rW!0)!<<3*"U"o"!;urr!Y#57!!!')!<Wfl!!N?'r;Zj!!;lla!!30&!r`9r
!WiB&!!*3,"pkYD"q2)7[]XOA4@)8%92SYi>[LfD@V91dDo-L4C3"93F*MtVH[L0dH$FRZH$Xa]G^+L[
I=HTgJVJDgGh=#L"p=i)rr_Zhr;lKi!!*-&"9\K#.kI!E80JHS%1Nj^'GM<!'b_<"',qs2*Zc1C+<Vs[
.k2tr-6jWS*?6%<)ZCTg)B0_@*?6F^/MKSs!<N9,!<<0+"S;]_!W<'"!WE*!!r;ls/-qT$8g=lZ%Ls*M
',_Ju&.AsW#7V/M%1EIQ%Lj'h)]Tn@+!)IDrYudp)AsA/()7T$&e>m++=0.L!!*--"98N/"7Z?t!<E6'
!s8Z.!Whro!W`?(r;[04%0-j=L&_8T!"8c+!!3-$qZ$j&"9er5"p>#,!WN6#!W)lr!W<!"!<WK(!"8u1
!XEfI"TSf0!!!'!!;urb!!**%r<!r>!W`9$!X8r@((_N85GuhP4\&7B92Sel<)rlt#$>5F@r$#$$#slt
E,KQ7G^4W7Hi\S?rcnisH$OXYG'J=\IXM-?#B5!!fbbb1!r`0%"U"i,n,W@eo`,$o!<W6'%gN(?%3L8%
:(S3\(_[]*)?(?b'G:rg'cIc)*,lr>(a'qE-S-eu.1%CK+s%^C)B'J2rYQ@f)]g+C*?HFN3A.N9%0-P3
!!3E0!V?Bg!WN5r!AOWW!<E0#!<N?+#QP/A,)3-q&fMf0'c7o-'+kcb$4$hC%L*:M?k!JI%1E[Y(`OJ;
r?2@f+<M[H*?5h5)&O/,(D@;i',<&CVuR2*#6=f+#6aPs#lt&.!WrQ.!s/Mq!#5P>#7LY:&-+))!!!E-
!!il>"p"c,qZ%*."pbM@"TeZ(!WrQ.!s8H&p&G-p!sJT'!<W</!">e+"TT#9!!!&]!&XcY!sAZ+!sAZ*
!sJo@"q;7dNp:j4-Vm8q6qpQZ;GU.h<``C,@;'.dDo?X6BQ%d+Ed)eSrd4Zkr-8p"GB\4SH$apbG^"CM
G%9GJ(^0d;!!N?*rW2KgrW2]m"p+c)!WrK/rW"DKDoPTR!$2gX$P=*h'+YZg',2&l()mo))f?Z8(EXbC
-S-eu.46Aa*?4tqq\U"b)]]k9*$HF]/[k]c!!<3$!XJu2quHKlpAt6n$ipA1!<<-&!!!$$!=&N'%Kg^l
;ZHe@(C(?]'bq;grX9JK#R1VG"q(iH$jm+G$k3gd)]^"Cr#m"%+<MXF)]BS1()7Ai$kX(!,Hq.P!!NB'
!sf&!!<3*"!r`9&!Whon!<NH(!!<<B^^U)?!s/T1!r)a,!sJl6"pG&.!!36*"9S]+!V??m!X&E%$j6P1
$EX:3!"K/4!!2orrW2Ee2us*a!W`E/"9AZ5"W%pm5LYic69@V076j@>;,C"^:fCG">[:fQ@r$##E,K?-
DJjK=G^+L[H$T72rHA]qH$X[WGC+1IC?-9E%/g2+"T8Aa!!iT*!!*3'!!*3V!"/u7-FRq9(_.8u%gNLU
&eGK\%1j3h'bhH'',VX))]BJ6+!E!_/1N%o,9ImD)?(KM(D@W'(D[r6*\T=\!!!6)!!!*,"Te,nqZ6Qo
"T\Z)!!*6%!"/l/$O-e_[r`c3&/QH.&I8gZ&Io-R#RUtL$OI1N"q(iG$OHqE$k3jf)]Tn@q]He!*Zc=A
)]0>)'+G9W'+cB;ZN't2"9JQ*#R'SrrrN'"rrMoq!W`9$rW*9)(^UY90)tt_o`4jh!<E<$":5)/!!*-'
!s/K(o)SdlrW!?3!!!7u!!N?2"98E&rW)s!rrDuumf4j=!X&T-"UG>;%2Kim&:rb;6S:,Q5t=C69iFtg
:f(%i=^><>@qfIhDo-H!DJ*m)DK9rGGQ)jaG5um`G7&J5FE_VGCZ-*@%K-8-"9\N%lMrgD!WrK)!sA]+
"Ukh?!,0;+*sMoT&/#H]&/5ci%Lip]'c7]#(E*r()Jg<1'cnG>-7gYr-6ra<*ZQ%7)#>'J((h5o(EX\S
1q*Gb#Qau+!sf&2jT%1>!W`9&!s/H+$k31:BuMnP#RCbL'FtWa'G:l`#mgtK%h&dR%L*:L?4.)C$k*RY
)&jM7*?P,#rZ;(['cRu)'+kTX$4mds/$T'S#m:;0":#%r!;llo!"T)3!WrK("on])!Sm_U$j?J.!s/Q,
!qlU"!<N<)!W`9%!WE0#!V-3q!<E0#!=/Z*#m?Xr!<<K1!!!'!!;HT`!&=TX"9f#:$P!I]&1#Sg1H?p<
4A&%,7o3/c<E)mq<**7/?!_#S@r#u!Df'-)D/F<;GPlXaFoHR]G7A_=F`VPCF`2S@h%^G.r;Zj$"8`,c
!!NB)!sA`/rWG+_!"Ao>[sSl*"9f8R&df*_()@Ss&J,Ng(E"#((E4#))Jg<0'cnD=-7^Pn,pFEO)]9J/
(Dcrc'G_Dt'G:ul*$@0rZ2ak0!rr<'#R1)*rrN*!mJo0H!<<-%!sAT5!"l_h()I/[&0)>j%MTWm&e>EZ
$OdLV%13LS#7M&K$jm+H$k3jf)B'P6*$$(!*rI#n*#KD'&.8^K%hpTHXT/>-"p4i.#6X8lp](a(!WrN-
"TSr2!7aaW$N1#(!!EE3#Qt5&!;6Hc!<3)s!"&`4!!!%["98E/"8`)s!WN6#!Ug!g!WE-S"ptJ5!"qE)
BKJOB2).0a76sIA<*!!t;GpFn=Bf!7@:s%aDS^7.B5VR'Ed)_NFo6@\Fnp1gF`VPCF`2P<gCju(r;cj"
q>p9i!!2rs#lt)0"9er2!WrT)!!NBNThHCI.hi?n$Pa0X%29Nl'G:uh&el-"(DRc,'H%g+)As50*?QRW
.4-8^*ZQ(8(]"m]'bhAt',)-&+?)!Z!!!9,!<<3-"oA;u!Vufo!VHEm!WE'1!@X[:*?c1-"Uu7Z#n7O^
'-7\p$jm@N%M'!U%1idS%U]_R"UtnN',_]+)&aD4*<$uV*#0D1'b_/f$4@F\/h*n&!"&o5!!EN/k5Ybg
!!!$$!!!*)qu?eb!!r<!"9\r5!Wi)srW)`pnGrRiqZ$X!$N:#/Mu`nY#m0u(r;lm!rrMHd$N^J>!"pc9
Z:$2b/H.U85=S(08l/Gd<)W]m&5uS2=BT!C@;0SoDJa$(D/BDrGB\1Or,_jZqK33iG'%eIGA_S7fFSAs
r;cj!rrN-$qZ6NnqZ/q^!!*0)"U,#2!WiN*";u3I-OKhW%13:I&.AjS&JGfj&J,Ne'GhW(()\,-)B3N4
)AO85*[E0^,U"3K)Aj8+!#GAF&f)5t'cA/<2(u-5!!`W-!!<H/qZ-WtrW2lr!W`?(rW2Wk.fpQ-ROARE
#S7FO%1s$U$kO!^%L`[N$4@:Q$jmFT#n@JS%L`OO%1X$h)?(HV)&aG5*$"qs"rnU%)&<r#&.]3\'c/DL
WrN,+#6b)1"p3ugr;dE2"98E&"onZ(#\seJ!X8i)!<*'#!qcQn!WN6"!U'La":P2/!/UUS!=8i*!;lls
!ri;u!;cfp!&joY!!Wl?!!"<D]i-"">;\H$4?u;(85)iX;c?Rk:f("f<E3++A70(e^i!t#DJa93GBS(L
EcM)!rcA!Z%s<#<GBJ"NH#7P:cjL6`!r`0%!Wi?&rW<'#rW2lr!!3'#r;dZ8!sJo4!=92?!!!`tUc&2S
1C=Np#RUJ<!t>eR')iIa&ebur)&O,-*Yo\7DB'Q0*?6(E-RBrY*#]\2()@Y_'`JgR(Dmr**$c[]2Q6TT
"UG21!XAl*!<*'"!W2rt!W3#o!!!3%!"T`,Uc/8V2@U0($OdIQ$P!(F!=TA8$5j3[%L`[R&IK$[@LinQ
%h9'_)&O/*()If*q\g7i)]BS1()7Gn',_T80VnaL!Xf24!sShj!!**%"9S`/"9\Q%!tF5i"8;cs!<N;q
!<*#s!r`5d!"Ar/!!Nc2!![`Q!!!9+qu?]tr;ls$rW<*#quHQo%0-A/!WrE&$5XKd%XZ;2-pK170KLdF
6:4+19MSA\;Gp@hr_O;+;H$S"@pWe`^MRe!DJa93GBS(Krc%jVr,NBjF*)PJGBS+RHYdJ=`s<1U"o\K,
!Wi?&!WiB'rW<*#qZ$Zu!Wr?%)$0jA"9o,6!"0JP!!$Z:$m#TX"UkA5$OR.>$iUV[%hK<b&ebro(E"&+
)BK\7*H)o:'ce87+snQX*?#b2()@Ya'GqJs'GM8t(`=20+=86_5G.uW!"/o0!X8c(!!!-#!WW8u!!!&t
!WW8t!#,GA#ljs:YRDTZ$4%.B#7_1M$k<dH%0$_7$5j3[%1<LQ&do6_@h9+U%h9*`(`4#''GVB"q\fAO
!#bbP&/5cn*#Kq^S,`Tj%gN(9"Tdif!W`?)qZIQ4"one"!!3H2(C'p?"Tnc,!s/Mt!<*#u!riB%!ri;e
!"Ar/!!Wi3!"N`P!!!6)qu?]tq#^Kqp])K>"9o)7":,;="p=pF^Gn5'/MT1F2*=5n6qC$J:f1+g;,R<h
'N%b,<Eis>B5>8"ChIX&DKC#FF)_2!rbqaSrG`BhF*)PKG'8.XD/4C.&Ie^DrVus$!rE#u"9/H&!VQL!
!X/f7#6bA>"9&9&?)Sb^rWb%_$3CG?#m^nK%h9*\&.oNg'GVH&(`+)4(E=H6*?,_6*$$4M,Tn'E(`*r&
'GUKZ%29Nl()Rr.)^-US/4Gj'!!N]3!!3?,qZ-WurrW3$p&G0q!WrN"!"rG2*#](h$4RFK$4[IO$kEgW
%/pVN$47.K$k3RO%MB-\&Ru@^#S.CT',VN#rY,AJ(AesJ)$h&q()@St(*".m,<q=i!!Nf9!!3<*k5YVd
!WrT0qu?_fr;[3,%L)n5!s/K)"9S]!!<3)u!riB%!ri;e!"8l.!!N`1!XW<@!!!3$!!3-#!Vlcs!W<'"
!Vud?!sf;E#mLqX#m_/V[n%i%0fM!K3Bf\q6q'[A:Jand;Gg<j:_ci+;cR(4?Y=/hDJWs(DJjN>G&qYA
qelCO"`SF#EcZ@%FpWJBDejg,)[cWJrW!$'!s&H$!!<?+!s8E%p])37#R_%F!t,\@!!6)l/I2ps%grXK
$4@4K#n-_B+qG1q&J>`k'c7f*(E4G4*$&r<)\jA5*?lgU+<;=:()7Pur=]t]'GVB!(`F;3+XeWg9T0&R
!!r],!<rZ'!<*'#!rW0!!;ca$!X/f5!!!$(rW!7!RjnUS%1isV$iUV@%1E[V%LijUq[45L%1<LQ&do6`
@h9+U%h9'_(Ddf#',2/sr"fk\(`=2-()7Mr&JZ6%,"%(`!!N`6!!3?+lMpncr;Zfu%06S:!!WE'`;fl@
!"925":"u.!!*-'!s//srW2cqrrMHd%06J0!!ET/"pJ-3"98Q&!!30$!VZZp!rrAu!"T8E&J,6K!"T/>
<m36K0.@G]0/P[N5!VG&7S6BN:f1+gr)"5-<)cn'A7'"d^i""%Df0K7G]n.JDf5Dg'5h]+E,fo>F`hkR
I;s+VWuDQL!r`0%"U"l-r;Zp&"9S`'!Vl^1"UtnJ!<<*#!!#9k'FbKS!X/i;$4Hh?!=K;9%fHn[&.fEe
'GVH&(`+,5(E=H6*?,b8*??=N,Tn*G(`!i#r"Bk\'c%Q$(`F;4+t+fl;MP>U!!`N)!<r](!!<?+!s8B$
q#CL"$4-k4!"(`h%gi[I!X8r?%K6hC%1NdX%h9$W%/^JM$k3UQ%MB-\&n;I_#S.@S&f2;t'+trm(&SgX
(Ddo*()7Ms&J,Wo(a;M"rW!*-!rrB,!pTah!W`9'"9\T&!s-XH!r`0."pP,2!s&B%!<N?)!VcZo!Vuls
!WW8i!"]/2!!**#!!<H,!tR[-!<<3"!<*#q!WiB("9&E'!r;m>#Se'e%13@_1`j8%2EaGa/13,54[)(s
6q9jD:/Fec;Z0H.;H$Rq=']?EBPbJ%D.dd)Dfg5IF)c'uD/B,c'PqT&DJsK6EccGJH[TsQN27@(!!3'!
!XAo2qu@!+"9S]+!<N<'q#D*6&Io'I!!!?H"J7:_)]oLk!!<W<rX&`8$k3^F%iu8n&J>cm(`=/,)BTb8
*H)r;(*4J;,:=c\*?#b1(&ejL&ebom'bqK#(Dn&0*?lp]0O021"oni-!!*9,qZ$a%"9S]+rW3'#q#CL#
%LN=:!"9M@QmWL_*=N#M":bq@%1*LT&.f?_%LigTr<jGO%1EUS&do6_@h9+T%h/s\()@St&ebomr"T2I
rYGkV'+tlf%h]Zq+UV"i!!*'(!<<0*"8)Wq!<E8t!!!-#"V:b;"UG).ScAuq!"B27!<N<#!!!'!!WW8r
!;urn!ri;k!;lj+!WW3&"T\T@.N&3d!WE*!!WN3!!rW-'!WrQ/"U"T$+9W8_)\No=,o,'E3'/WO2)6gA
3]oSk6:FF;9MSA\;H!Hj),aC5<``U=?taAlDJa'+Df9`BG&qV?ChmebBcCf%CMRa'DK'T:Fa&4^FDID:
'G:BH!!!$*"p4]&"9er3!Wi6#q#D$.$NLV:!#5e?\4%,J"VM7M!X8Q1!t,JF%K6k:%j)>o&J>`l(E"&+
)BTb8*cN,>(*4J;,:=c\*?#b1'GLHY)&!Yt()Ic()&aG8,:Y/rD0l6f!!WE'!<iW'!!i]1!s/K(!WiE!
!#Yb:#lk52!"8i-YWWL/!>#VD!X9#A%1WmZr=BqZ%h9$W$k!FO%1N^R%MB-\&n;I_#7_1P&Jc)prY#5E
r"KYV()@]$&ePZb%MBQo*aWa`!!NN,!!3?,p&P*nrrW&t$N^G2!<<?9"TSN*^AIs5#7(G6qZ$a"!<N9&
p]16np]CHrnc8Rg$3C80!!39)!YcgoqZ-TrquZft"p+l0"U5)1rW!`;"U>#@%O*i]]$JKq.R#pN2)mQU
3&iu+5=%Y*7nH?J:Jgpc3)W[T<`i[>?taAlDf06-DfBfCGB7_?CMIQsB4kmkBkhF"D/XE8Fa/=aF_RqA
&.nmD!!!',#6Xl(!sSo3!rW/s!#Ye?#65,4&0YSQXJC=J()%#_%1EUN#71bHrXJf9rsp.^&.oNg'c.`)
(E+A3*?K/?*#9V;*[<$Y+WVI;()6ZZ(_[W"(Dmu-)]TqG.P!*#F8uLF#6=f)"U"W%!sJf0!rN)s!"f88
"ono/$QEB7URZQ/&.SmMrX/i8#RV"Oq@Ec?%h9$WrX/i;%1EUS&eYQ`&n;I_#7_1P&JZ#o&eP]gq\'JS
'c%Q!&eGQ_%1s?l)K'-c!!NN,!!3?,p&G'nrW3'#r;[Q8#7(;0#6Or+:lM^p"98T,!WWB0"8`)t!VHHl
!WE0""8r9$!<</l!;urt!XJf,!<WB,&02>Z!<*#s!rW-M!WrQ0"pG,1!!39(!!!0QL!ZkY4taNK0eb@@
4$5Sb2`a,g6q0[;8k_uVr_X5':f1+i<`W=/ART:h^i++(rbr3eH$==KD/3iuAnE#pAnPaiBkqO&E-$2J
IXlTU\;^h,!!<3$!t#;9qu?g'"U"r+!W)is!W<!4)fN*@&/52.-j0YW$4dUT#mLYB%/gY=%1WjY&,m+g
&J>co)&F)-*u>q=E#ou8+!)LL-m^#W)Aa,%&eP]g&ebuq(`=20*"a26,qCQ"Mf/S"!!`N)!!EB)qu?g&
"9S`'!W2ot!rW*5(i$7,#Rg]j+TMKC"q1nJ#R:YF&,m1<&-<@O%/pVJ$k3RP%MB-]&nDO`#7_1O&/>ll
r=So>%hfWl'b_/i%LijY'c.d6?iC$/"T\T)"pFZ#$3://!s8T*!!!')qu@3]\L%^b!'CSg!!36&!sJN%
rW2TjrW3$#qucp"rW2Zlr;liurW*3)!Wa2O$N^/*rW2s!!!<'!/-?"Z#6kA8!WiH+#R<02Jj1hM5<Q5B
4t\WN5<_.h3''5h77Kd<8P;cR;,R<h3Di[R<``C1AmoCj_/F4*EH#l>H$==KChdWqARo=_AS,RgC2@d,
Ecu_WJ9YkGKa/+g"98E)$O?k4!!EK0"9JW%!;ca7"99aZBH@Bk%h!q(%KHV<&.]0T"pYJE%hB0L%06qL
r=Bn[&el)u(D[o2(EFQ9*ZPt<*ZlXU,p=9I(DRV^&K28q'c.]))B0Y;+=/Nj0U?AP"TSf/!!!-(!W2p"
"U"o/qZ6Qo"9ecM[q$3k!=K/8Gn:5]!!Nf@$4$hA$kEs`&c3+@%h9$I$Q'9]$OR@V$P="^&Io$U$k*[]
'G:uh&.oNO&e5Qh'G:re%1EXV'Gqa?=8i1'"T\T)"pFZ#)Z]s@!s8Z.!<<0)!<<*$Z2kI9!!EZG#64`+
!s&H(qZ$[!!<MclrW3$#qucp"r;lTlr;d$&!WrN+r;d!#/-Z=X!WE)t!W<'"!W<!E!X&]5#6kA<"UG)S
45<t!8O>Bf3k@dF0K2$W5<_.i4?l/$7RmYR8P;cR;,R9g%8p/+='/d?@;0SpDf0:gE$odRGB7\<BkM!f
@q0%[AS,RhCMe$2G'SOcH>UcH$jlt<!!!-0#Qsu)!sJf/!Vl^7!WW9%*A5K#)C64,!!S)i$igJ=&.]3W
#RLkJrXSo:!=fY=&-3@U2\[#E(D[o1(EFQ:*ZZ%=*ZlXU,p=9H().An&.oKe',;<#)&aG6*Zu^V0J]5&
!!*'*!WW3&!rDs""9S]+rW)ou,6.`H!<`BD0$-<o+;+_U!.P@\!!*94$k!@H#n.=V&J,Ka&,m+A%h/sH
$OI4N$OR@V$P=%`$5!dS%L`aX'bh8mrX])B')`CQ&eYik&eGN^$k*XZ)BF`,rW!*+!WW9+"82]r!<NB&
":58;!rr<&&tf4.qu?^<rW!$%!s/N#!!*-%nc8XirrW*#rW<$!rrDipquI3-!WrN+!<E0$!(6eirW2uu
r;liu!!3#u.KKVU#mLM<$k!RX2mu+K*\TZ:1/YbK68Uee5<hCs4[)/!77Kd;8P;cRqbR`"<*!(&?=dPZ
D8L70B`;rVG'\@QDJEisAGfp<A7Z!YBPVI(F*;m/HjjuAA.SqF"p"],$3p\2!!36(!W2p@!<<*%#6Y58
.ASLK!!a&?!#gUu%06eD%M'$X$471N%M&FH!=fY<&/l/p()Ri')''M6+)rAC(EOV>,Uar]*#KD(')iFP
&J5Zk(Dn#.)]Tk?+XJiE25WtE!!NT/!!!'%qZ$["!Wi6"+9;NE!!<K2#RDrW/2$u*$NU5@J,olT":#8B
$jm:K%1iFL!=o\=%j)8j$O[:L$k3RO%MB-^'P7sg#S%:Q&JYum&.]9_&JG'T!>#kB&do9_%h9$X%M0X(
P;rOA"9nr.!X/Q+o`,L'!sJf0$4[:@%0GVm!sJ`)!!*WRrVus"!r`5u!<3)i!<3*"!rN0"!rW/k!"]/4
!sA`/!<<*$!+,^/!WiE%!;QWq!W2pH!s]/:!<WZ8,8e0k3(,AL>pqm6[l[)?5<_:s5sR\$6:4.07Rp$C
9i(ab*D]I-;H-[u=C,NGBl:e,DJ4!-E-?POEc#N'ARo<L@MrZdAnYprE-$5LH[:*[gK"Ud!<rQ)":5;8
qu?a!!W2p"!<N6$)?9sD(^[6$)^>Ug/H?"mIfp>e$k*UU%h/pUq$d?7&,Ztl&ec#t()7]-(*+K;*uu+<
*ZlXU,p4-C'G:uh%hK9a&el)u)&aG6*?H:G0fH:!rW!B4!<<*$!<<*#!<<*$!W2ou!X/K&#mLMN%'MZ3
+pJ#\-ia5ZGQ8*O"pYGB$k*LP%1WmZr!ii?%LigSrX'SQ$k!CO&e#BfB+kg^%LijZ()7Gn%M'*_&eP`T
&.T9b&ePZc%LrpW%j*$g/H,VQ#6Or-"U"Dt'ESCA"9JZ1!>PU4"9nr.!!iW+%NYHI!!30&!W<#t!V$0i
!WE0!"9/H%!W<#o!W2p#!<WH."9&9*!W[KG!s/N)r;Zj!!;cfp!$).I$NpG1#6YTKV`Qpk9NXnS3D6V=
9Kkd-5<qM$r^-fV6q'R8"\D?\:/Fdd:HD<M<*!(&?"@>WDSg@1BQ%g.G'\@QD.mNl@q&nU@:E_WAS5ap
E-$5LH[1'\i^s:[!sJ]*!sf)5!VQKo!<`<$)[-3D:lQG2#9kW7%0.#c";M4Q%1NdX%h9'Y%K-\;%1NdX
r"&lA',VK$()7Z+(*+K;*uu+;*?QOU,p4*A'+kfT%g`dY&el)u)&aG6rZ)7c1,l`u!!*''rW!!#!<Dut
qZ$X!"o\K<"98U)Os(_K+X[p.!"*ZF%KZn@#RUqJrXJi:r=/`9&.K!S#mgqH$k!CO&e#EgBG;-l#nIIS
&f)2p%h9'\&J>Zf&.]<`rXfJK%hB-[%1XO.W$2-?"U>/1!X&W&!!!&t!#,J<#6Y#,!W`Z/7K<i*!XTDD
!=]qE!!NE+!W`9$rW2KgrrN*#rWE-$rW2uurrMrsqu?j#!sJi1rW!0*!0mNd!<WE#!;cfq!!E<*#n$n8
!#GqO\TKJf1dal+8NT\Q4A7q+5X7V%6UUf?#Xq3R8P;`P:Jh$d)c0F3<`W:-A70+h_f9R,Df9T<HZsIG
B4YR^@f9^:@UiscB52:&F*DtXG_'ql4pMK!"98E(#R1A3p&G*p"8r3;!W\oo#Sm^^)%mJ\'6jTo#S%:R
%M''[%Lr=E!t>\L&,Ztj&JGlq().T*'c\<:*ul%:*?QOU,p+!=&ePWb%M'']&el)u)&aG6*??+>1H,KE
-3+,J"8`&u!W<)s!!30("oSE;!Wo6'%N5]i((LZO$ZH(T!=/o9$4@7Nq[NQ6r=(+_$OR1H$4@7L#n7LU
',G<t&.&jV%MKWn&e>E]%hTEe&J,H`&.fHQ&-rdW&.T0q.&@aZ!!NQ/!!39*qZ$Tsqu@E3"9el-!WiH(
OUqQp#6>&<"p#2NquH]u!!<'!n,WFgrrW0%rW<*#r;ccsrrW0#qu?j#!sJl2rW!0+!42_-!!<<!!;llr
!!EB.#n$n8!#-(jd6ou]4?#Ag9fu:\5"e(,5s[j:6iKIY77Kd<8P;`Pr(e8.;H-[t=']?DBPtb.D.dd*
E-?SPEGK/s@U`dE?lEH`A7fRnE-$8OH[13beM@[E"TeZ(!XAl2!VZQq!<NB%!!3Q@Zk"/e'b(?P$53CS
H3=ld%Lr@I":bkM$k*%C!t>_M&,ZtW&JGlq'bhH('cS69*ubq8*?QRV,p!p;&J,KP%M]Kc&JGos)&aG6
*??(<1H;KV!!E<'qZ$Tsr;uls!s&H+"T8<0$l$9!'cISe"U,>8%<;XQ$igM;#n$Y>oaE#P$4-tE#n%.K
#n7LT&f5=!&.&jW%MKZp&e>E]%hTEe&J4pPq@F2M%hC!:T+1i$!<iN)!X&T+quH`tqu@B2!W`9'!X\ql
!!*B0!<WK,!=p+I!!!*""9JZ,!r`5i!<*#u!WW?%!r`6!!<*#t!ri;u!!<<-#6b#+#6b+P!!3-&"82`n
!<iN-"pbM<rW"/S.*+8,5<h7n5t""<[Q[>J6UF.-6pj=06q'O67n?3E9MSC^:HMBN<*!%$?"@;TDT$L2
AT2R,G'eFPC1Uj`@:3JM?XR;OA7fOmE-$8OI=-BdcR0G<"p"](!X8f1!Wi)sr;llt+oqr`V[3\>$j[(C
#Qtri";;"L%M'*^%LijU$k!FO$k3[Wq[`rD',;;u'Gi8>'H8-8*ubn8*?QRV,p!m9&.]6\%1WjY&JGlq
)&aG5*$$"?.m0^A#R1>+!!**%rWE*!"9AQ*!sAK%!XKUFrXoeR#Qt52!"X)M$NLA9#mq%J$MY#.$l'-W
#m^eC$4I7J%2''^(Macu#S@RX%MT`q&e>B[%hTEe&J#?]rX\r=&J5Wg'Hf)t"98K)!s&B'"9S]&!!*-%
p])98!WrG@!!!*)"9S]*!X9\G!<<-&"U,#3!s/N)mf<=frW3'%rW<*#quH]sr<!!"qZ$^#"pY;1!!if0
f)PmQ!X&Pu!$;4B!WiH,"pYD:!<EH6/[7&p4$Z/"5rqM;[m!JL6UL`>$U[<M77Ka:84cHJ:Adm):f:7o
='/a=?Y=2lDf'*)DfKrIG&M))@K'[5?O'tI@qB@kE,uA2I=HcgHcmEI%gW(6"9AZ0!s8H&qu?d"!Wi9#
'`eIG";m+"$3^bF#mLA8)0uAt"q;(A&.K*Y$k*LO$k*RS%M'*_r=BhY',;8t'Gh]&)BNl>)\a;5+!i?]
*>]:u%fHhN%M'*a'c.`+)]Kb;*?cXlUB_23!r;ls!rW6#!!!&t!Z:t<!XAfHPRJ35%1NOD!!*XO!"&]0
#7:hHr<i9,!=B/4#TX3Y$OR1L&e#BgC)%<e&J#Bd)&<hp$k3^Z'+tier=05H%hK9a&el#t)E!l^rWEE-
!<<0'!s/?#!rrB(!VZR,"9;6u!rrB-!rr<(!$VCF!!<B'"U"r1!WiDj!<3)r!ri<!!<3)t!ri;u!!<<-
#6b#+#RLO_!!E9'"Te>t#lt&.!WrQ/#6tAH!<<?519`N"5!_J"5WVG<\3NbQ6ppoA$UdEP7Rfm=8P2WL
:&[m+:JXeb<EE7(?=[GWC;"@rDej61GC"CLB4>9J?QWT\?!^lG@V'7jE--ASJ:M`bfFel.#6=f)!X/`0
!Wi,t!WiB'rW!9+"UbJRMZF1k$47+E"98`GHNXue%1`@K!Y5_Lr!Wc=%Ls!\&J>!R(_IDq()7N")\j;2
D&=*2)&s_E.3ooL&.\[K((:W]%M06f(E",1)]Tk<+<rnM!!`Z/q>^Krr<*$!!!3$"(BFL9!<rWJOp_p4
%134<!!*[P!"/c2#6G5?$iUM,$NUS@rWjMN$4@1J%MK9b'P7pf'+GH`'c@c!%LW[U&JGcg&,cqQ%M'*_
&JGlo)&k<-!!*0*"9JT*!s8T%!!33'!VcWs!<r[$r;[30!rr<(!$_IG!!<B'"U"r1!WiE%!:g-h!W)rt
!W)ls!W<'"!Vucu!sJo4rW!3/!6kKF!!3<*p&P'm.foeV"pY51!!E`e[5LB>69[Ru4@iVd5u0d86q'O6
7R]d97n6*@8P2WL:&[lh:JXh';cQn$>$kfKBP4bbB6S$+EHc\MD.[2S?63BW>[:ZC@:X%gE--ASJ:M`_
i!Kr&#6Fl*!X/]/!Vl`q!W2p3!sf)PO9?%%$3gV8!!jHi"V_1O%fR"A%h9$XrX8r>%1WmZ&Gm%H',22s
'Gh]')]3,o'GVr1*$?OU,9.F/q@"#H&/#]o)&aG5*$$"@+uZn1!!35u!!!&u"8r5u!WW9#!!rc2+I3HO
&I\jErW!<<ErZRJ"pYJB$O[=8$N^YB$2t22#n$Y>&.T?`'G=a^$lfTa&Jc3!&Ifok$k<j_&eGN^$k*RS
%M03b'G_H%*A=Vs!!3<-"9JZ.!s/<"!WrK)p](Bs$3t)>!##J9!!!-%+ohZE!WrQ/"9\f.!Wh`irW2lt
rW2lrrW3$#rrN&urW!$%"U5).!!i`.[K$=.!X/Yt!$qXH!sAf5!WW3(#qa"Q7n#d/5!V5%>.[-u6:XI6
7Ros<7n6*@r^eD.91qrQ:/4S];,^Is=^,6E@V]>PC1hL$DK0iEF)5Do?!LW?>lIq9?!h#NBPh^1H@LHt
E".BD%h&^J"9AK)"U"l-nc0@+#m(s8"qhFS"p4r-#TA'o'aP9ZrX]&?rXSo:":bnP%hSUM(D7Aq'bqE!
)]'M+>T":u)''hG-mKZF%K6_K$k!FO%1a'c(E",1)]Tk<+WWqGp](?q!!3$#r;cft!<N<$!!i]-)5@ZY
'+G-D!!j0X!"8i3#71b9$iCG3$iUJV#mgkD#mq(K$kF!_(CF1U%M]Hb&f)<!&I]!S%M9?e&.\XI$OmRW
&JGio(EFAWTDefq":#)4!sA],qu?a"!rDs+!<<*#!XJdr!!3-#!r`0)"TT_H!<<-%rWE?+!WiB'mf<=f
qZ?`tq>gEoq#CKu"9eo,!!ic2K`D/S!<iSr!!NE+"U5#.(B=UC,gJDA7RK@'5s7eD]L5Xb84H'=8,Z!X
8cD=(91qrQ9hnJ\;H-\!>$PHHA8GJBDeWg%E,g#EEb])ir*0/()I-TV@q]^uFF&FeKkum['ak0J"Te],
"p=u.nc0"!$31U;#o+$]#6YP?!!jKk"r.FT%hK<b&.]<L%f[(>&H!+B&eYilrY6(_)AjM(:EC>f*ZlLN
-R'HB$jm@>$P*XV&JQ$!)B0Y9*?6:A;N(JR!!2rs!<E9$"8i/t!WE')"99":&/u;m"oSE+&Te!^!!``8
!"/]5rX8c9rXAf7rX/Q0*=</_$k3a]&K(dF(_@)h&ec#t'bCc[$Om[]&e>HM$O[@Q&.oQi(De20:l,)N
!Wr]4rWE6(!W2ou!s8B#$3:2/!!33+!7UuRqZ$[%!$_@A!!3'$rrW0#r;cEhrW2ltrW2corrMlp!s&K,
!r`0*#RsT7"98E*"7cF2!<NE/!<<*%$QI;O91D<85smh.?G&^*77g!>rCHr[r(?r]#>@fc:/=_b<#8V=
>?tZKA8#S5EG0!&E,g#DEG8ic=]t`-r`L.D?!h&RCiFNCIt35iQE(Z+#R(>4!<WN0!Whil(]t$I#HA4M
&Io-Q"onoKHj1>m%hB3`&J4mO!"Su=rt,2Bq[roC'`JgO(`F2/(-<Z_(D\#5+XJKZ)%m;`#mq%I$4@7P
&JQ$!)B0Y9*?-1@<e'fC!<E9$"8W#t!WE'*!W`M-&f_Pp#6Xr*#S_=[%KQe>#n$Y>!"Af8rs\o8rX/Q0
%13IO$k3a^&eu$;)\<JX'*T-g'G(WX*"!,d'+k`a$OR4K$OmX['GVH%+;e./!!!$&#6t/1!WrK)r;Zj#
!rW*$!<N?(rW!'+!8.>WqZ$[&!@%IB"9AT,!Wr<$n,WCfqZ?`tmf3Lk!!*-'!r`0*#SAKm!rr<)"TAGo
!"8o3"T\T'!>,sb5>4KE70l@J9O>G&<(9LZ8H)3\9))%!9MJ8Y;,^Ir>$PBCARo=kG]IJ3D/XE9F`;#%
=oMP'=oMM4>$PEDB5DR1H[pX"E1.3,&./dL!W`<)"pG&/nc0@+"Ub=-&K22k%LNIA$6=O"(CCZ`rXf,A
q[`Z;rXo&@(D@Gr'GVB#)Aa,3-Qs9C*$6=M-6O-;$N:A1$4dLS&JPut)B0Y9*ZH7C>&s?;"TSQ)!WrPs
!#,Y<W"pBc%grRC!!*dU!"K#7#71b:$O@.M%1WgV$k*OC$N:A2$60E^%1Ws`&J6$.*"WYo',23!'FtQW
$4RO[&J#<K$5X'Z&/#Zm)&OJ9>BBiF"U5,6"9\l2!Wi6""9S]+!!!-%!<WH+rW!'-!7UuRqZ$['![IUC
rW<'"mK!1dqZ?`tli@"drW!60'+5*J!!!0*!r`5n!!rZ."9AK&!tGaZ%RNlV7S--A6rI%'8QA5Qr^m)]
"%u9\:&[ib9+FWi:/Fhf<`iO1?XdPWB)Z["C27X(EHH;?B4"bA='&L+='&L,>[ClPCiOTEJU`;oVLfKj
%L2t6!<`T1!s.rm%g3+D!2UGN%M9<`$3LhQK*2Js$4maI&c!":&cE@@'/(%6'c%T'(`+88*Z5k9+!N!W
+;bXr#RC_D$4.%I%1j0g(`F>5*?H+A+D+UR!!E#s!!3$"oDf!s!2^VTrXTAC"98Z6H2nEU#7(\8$NLS8
%K6h@%1N^R$4?b=rX&f:$OdIT&cNFt)]BS-&eYim(Dmhs$O6tI&/,Wd$jm:I$474R&el-#(EXf7=o\O/
#6P&2"U,#1!W<!"!s/N&!!<9*"TnZ'":,"c!!W6"!XSrRquH`urrM`lq>gEoquZftli7(f!Wi9#!X0&7
rW!'%"9\f.rW2Zl!<WK(!"oDB#fT5,5Y"OA8k2uVb"Gc*9`@Z`9,:2q9hnGX9h\5R92&&U:f:7n=B]!<
@KC"Prb4!"Ci!m)EHH;?AmJJ<<E<1&<`W:)>[ClPCiFNDJUN,pZXk!`&-`+7!<`T1!s.rm'EnaH!2^YT
%2'Hh$jIIRL^P"+&.ndPrXer=r=\u@%ho]m()If*)AsA1*#fh<+p]J@*u>Fn#6tP5#ndRS&/,fr)B0Y:
*uQ1IF#a4#"o/,u!W<)m!#5P9!2^_X%1j-["TSu3If^)\#7(YDrX/`8%K6hB%1N^R$47(GrX/W4)%6uc
&J>cn'bhAt'G;)q(`3qt$O6tI&/,ZX%h&gE#o<pX&/#]p)]'SDG<Z65$jQh8"9er3!s/?#!WrK)rW!$%
"U5).!!EN,li7.b!!3K0,Q%Q@!UKg`!W<)u!UKgd!<<0"!!3<4!WE'%!X&W."8r8o!!*0)rW!W7$jt0K
:d.BG9h\,^9[$44852`MrCd5d:B"&h:B+&f9H?i';,^Ir=Bf'=@Us+cBP2'rChmp.FEDD4>ujs*rDjV6
=B\s:@V9LrFF&IbJ:"q.)[m5\#64`)!sJf/!V-4/":#,2WuW8i&fD>l#8[]'$lB<_&.oNf&J,NP&c<::
',M>t()If*)Aj5-*#fh=+seQY(CpcU#7(56'+#!T&/,cq)B0Y;+;l:NI4,*r"Si&r!<<2s!!!&u!#,G6
WuiGk%hoHW!"ApX!Y,28#71b:$OR:O%1WjW$k*LN$N:A2$6BQ_$k3^Y&el)q&el)q&el-")AWnn#RV"Q
'+tfb$iLDJ%1j-e(`X;5.tKA]":PJ8!WrT0"9S]'!!*0'r;Zp$"9el+!!ET.n,NUh!!<6.![@OBrW2?c
q>pTtr;l6br;llt!XoeLrVup#rWE3&r;lWm!W`B+rW!3)%1pl\;*@HJ&Pl+n>>NI<=\;F_9heAW9hnL`
:]aEg:Amm+:/Fed<EE=-?!q,PB5)$lC2@^%DK9iADJ!3Ur`(%@<``@*>?tWHBP_U-H%:6kID\Pq$4I%;
!!*0)!s/Mo!#,J="oteL+:/Z"'FkBb$],9/$5!jK')W@>'(utF'GVB"(`=5/(E*2k#9P0;-6O-9#lY#D
#6tM@$4RLY'c.c-*$-7A+YJHh"98Mu!;urp!<3)u!#,J7Y9P1r%i#NX!"AsX!=f)7#71_9$3:MCrXAi9
!t5PE$N1;0$9/D$%1a!^',;/n'GV;q'c7l0(_R8a$P!a^&eGN]$OR4K%1j-e(`X;5/rCqb":>84!<WH.
"9JW&!!*-%r;Zp#!sA])!"B;9mf3Lk!s8Q(!=/]LquH`tm/[.doE":Y!s&H)!WE'#'.+7h!!E?*"9S`)
!W2ot!W2p!!<WN(!##n]b?@Y+7o`D]93b?>:g-Lg:/:a`#Z+>p;Gg:f:J^sb%o6#"<)m"&>?tWGA7fLg
BdRS1CM[p0F`hV7?<:**<E3($=B\s:@:X%fDK0oNH$t7b3ZeS6"9&9&!WrN+quQHj'*JRBW@](t&KDMr
#T*u,$lB?a&cE@B&cE@>'DrRD',)&o()If*)&O2.)]Kb=,:=i^(_@Mi"pG/7#6tPB%1a'c(E",2+!V^K
1lW+Qli7(f!Wr<#'*A66/fb9.(CgWL%0:nY%0-S:#lP&1$4He@rsSi6r!E</"Ub_K%hTHQ'E/[X()e/5
)AE\h$P!a^&eGN^$k!^V$OmX['c7o**]0#u'*8FA!!*3$"9AQ)r;Zj"!W2p!!WrK&!"BDAjo>Sc"U>/1
!=&TIquH`tl2^MYli7"drW3'#rVup/!C@7p!!NB*"9S]+q>gNrr;Zm""9n`()%dq0BM(W`<`2ag?;o0I
>>.mi:f("c:f1-i;Zfop:f.-e%o?,$<)m"&>?tTFA7fLhCAquSCi=?:F`1o!=8l/=<E<1(>?tWHASGsu
E-HbTI"KWu*sDlN!<<*#!r;uk!#PbD#bj?r%MBct%ga'^M@CF2&J5Wh'+toV')WF='`A[H'GVG`(_%?#
)B'P7+=&<_+rLptr<3i=#7(YF%hTKl)&aJ;,TJ$fPmRig!;c`t!<WH&!#YqEUH9;$%MoTZ!"AsX!=]#5
"pbJ@#m^hEr<rT3q$I$-"UkhN&.oQS'E/[W(E4D;)\rtn$kEp`&ePWa%K6bO%M06e(`X832OP3n!X8Z*
!<N?+!s/N%!!*-%qu?g"!W`93!!!N7fDl-W#7:Y:!!N?EqZ$TsklCGYm/R.f!r`9%!WE'##\+,<!<*'#
!Vl]r!Wi6"!W`E-rW!6+%Mm3.7n-KV;$p/q?rYNO>u"<q;>jDm;uT_u;c6Ljr_O)%;H$Oq='8a5?XdPX
BPIE\#]+F"F`hV8?<@))(KOU@>[LoMAnc'tDKUAOIs'9r('jsA!W<!"!<E9#"8)X.":#"+64j_K)&*Vh
)%DH4)%.&h'E8aE')`LA'EAmG'`Ja['GVB"(`4,/)B0V9+=&?`+rLpt"o\W<"U55>$kEp`()Rr/+=/'X
/Y<IQm/R4h!WrQ'!##D6VaM.-)%m>^!"AsX!"8i2"UFr2!"&Q1!"/H,0+&$o$k<dZ&J>`j'GM9!*$?CF
(D.)c%hTHg&J,H_%1EXT&.oQl*>ThLU)"4D!WE'!!r`9'!W`?$!<3)s!"o;4!!**-!7:cM!XK,;!WWB(
+6<M$!;QZ^!!**&rWEH,!!!$"M#[SU!<*$"!Vl]r!s8E$3roEe!!!$)$4G%,7nR/c;,U5!<mjrR:K14j
;cH[o<)lq!<E3!s;Gp@h;H$Op<`iL/?!h#NAnYppD#S5rDfTuCDe<<W<)Z^p<`iO2?t*\[BkqL#F*r.]
CYLQP$ig8/!W<!!!<`9'q#D33!!!')"9>An%h^6*'+bNi%Z:f7$PF'M'E8^F'DiLA(&epH',)&p()If)
)&aG5*$$1K-n$8W&-s$T"9S`/"pbPE%M9?h(`=56-6OleV[r\*rrM]k!s&H*"TAB?!<<+u:(Rs\%LNC?
%0:nX$igG7#6tM>#7(SAr<i3(*srAa%1Wm\&ebom'c%Z-+X8'H'+PK`&ebok&J,H_%1NaV&.oQl*>TnF
WYbsLr;Zs$!WrN+r;cp!!Vud/!<<*$!sAV6!!<9-#mC>0"99P$!;lla!!30&"9&H-!<<**!3#u!#lXi'
!VcWr!s/N%!#PeA!<<62#mdr#;c$Uq;GpA%=4:/V:fUKl<<-)!<u"b9<)cdp;H$Op<``C+>?tTE@qKCh
r+lXWEccD@AmJG:r_jY6=Bf*?@qKChCMIU)HZOIUg`m78!!!'$r;Zm"!sJT,q#D<6!!!*,"9=Wf(`+83
'G(Wk%uUo8$ka0d'GUKZr=o&Br=g"\',2/s(Dn#.)]Kb:*[)gX-mBN?#R120)?^6M$4ICU&eu3")B^CL
.5S",!!*'"!<N9&oDeso!X&Z*!##J8!0US*'cR_m"TT#5IK0cV"U4c.rs8*#(((EX%1a!^',2,q(E+>=
,Tn!>%hB3arY#nW&J,H_%1a!]&f2Q&+"s`)$4Qk5"9AQ+!s8?#pAb=!"98G'$31,."pY83!!E9D`;fr?
!X/K,#6Fo+#lqF7$iBu)!VcWr!s/N%!##G<!<<<7#RHom?<:!+<)ZY)=k+-c?rC'+<`W:&<``C*=]ea,
<`T)t2cWjY='/X1?!h#MAnYpqD/F**DfKi>D.QsP;c6Ll<ENL5@Us+cC27R!EdDYEK\R:Q#QOi,!rW*"
!<`<)!!`9"(]aX;!!<N1!deN&*#9P0&.9EfN"-a7&eb0XrY,8Fr"]/GrtYDF-l!I4(`=52*$$%@+XJKa
+W(^q"9S],"9o,>$k<g]'GhQ'+=J9W7'6@e!s&K*!VHF3!<E6)"T\T("onXLC*OW/'ak0F%KV"Y$igG7
r<EE/#7(V4$2t;3$N(2J$47.L%1Wp]',2/s(E4G@,Tn$@&.fEd'GUN[&.oHa%M'*_&f2Q$)F(D*%1<%6
!!3$"qZ6Bj%KZ_63"l]#!<iQ*!!E9EhuMm>!W`?*rWWT0!WWK+\cE0/!!36(!W<!8!sSc+#8%+BOfVVi
;HZst;Is%_=CP32=8Z2#=oMS-=]ea+<rH#3<``C+>$G9>@:WtaCMdp)Chmp-"`eTu@Tl_0;&N83=Bo6C
AS5^mD/F03G]7h[i"?G&!!!-(r;Zj!"8rE"!#P_<!!!'+!s<R_(a0\8'G(Wl&<.2=$kj9P'ESp^'`AdC
(B,'H'GhK"(Dn#/*#ot>*[)dU-Qj38#6Y,1!sB/>#R_(O&/#Zm(`FJB+"Kmgqu?g#!s/Mr!$2.B!sJl0
!!*9(!,lru*tf:r"TT#6IfTrX"U,,:#lY&/#lY/.$N:G0$5a-Y$k3[X&J>`k'c.f2+s\9L'G(ff',;8]
'F,6_&.]<a',1]g)\X;[ZiCI>r;Zfur;uiso)Jq;*!H<B!r`0$"99Ra!"K#2!sA`/!W`<%!X,Y1"o\Mp
!!*0'r;[c;"9nl,#8%%>LUBlc<`rC$;Is%a=^tH8=BSf*=pS>:>[(B8=]ec)<]F/^=BJ^0>[:`HA7oUl
D/F*)C2@d+DJ3EZ;,9ta;,gY&?t3b\Bl%^-F*)SFH\gSn#m1/-"U"l)!!<9*"U+l0q>_H9!WW3$#6G$C
GRc#;)\`hk*"e2B)@[>n'GM;]'`SpE(B53N(B5-J'F#9e(Dn#.)uL]s+<r0Y*Yo1g!s/N+"U58@%1Wp^
'G_Q+*[2a_9XO]t!s8Z.!VHEr!<N?,"p#P@!!N?&Apb.7'GLoY!"K*]!Y#,6"pbJ@rWrN1rX/T3rXAW2
((:T\%M'*_&ebro()e5;,9Id:%hB9erY?+]'b_2l&.oQj(Ddr)-UtHC"pFo*rW*!#q#U?mrrMus!>6aX
!<)s""TT_D!<*#E!!E<(!s8W%!!3Fo$N'o(!VcWq!Wi6")$'jF!WWH:!<RGV:gmC.<E)k->M34l<a8f.
>5_Y*>l@qn>[(B7=BJX+=BJ^/>$G6<?t3b\C2@a(Chma"CM[cs>Z=Hl9hnPb=Bo6DAS5apEHQMKFE2bo
eJSGk!!!3,!W;uu!rW9!!!30&"9&99"T\j3I1IS?)\`hl*"e5C)\!Go'GVA^'EAmH('#-I(]P9N(&emO
'c%T&)B0[o*??4G,9n0B$NpM4!sAc4#n%1P&/#Zm)''_>+uNT+qu?g%"9S\t!$2.B!sSu2!!!*$!*4X_
+qk\!"TT#7JHHA_#6tPA$N:A3$N:G3%/gY7%/gSL%1WjY&.oNg'GVB$*?ZLG(_R;h&et9\'c%Js&J5Wi
(E+,,(b/Lc"98N(!!*/u!W;uu!W2p!!<N?"!!3ET!W)iu"ookF!<*#Z!:0[f!<N?)qZ$a%"+1@Vnc/[l
!W<!;!<i]0!!a&8"(T/H?rgN5<E!I5fj&/l?!CQ=rET\8?XI,F?!LT;r)jP6>$G39?=@>TBPM@#D/<tc
B`i!U=A^,48kVlT;cd43@Us+dDK9uLGB.bOUqn)P!WW3*"p4`'"9AT,"9eW&!s&E("9&97"9Am%K+]@D
)\`hl*>+>E*"EYr'`JgL'GVB!pD<fE$PaBj'GVE$)&aG6*W7#k+!DdM)A3>Y!<N?,"pbPE%1WdX&ebut
*?,tD2Jnidr;Zp&"Tneu!$2.B":#26!!!'#!(2JT+;,Cs"oo,8JHQJb#m^kG$iUJ5$iUS5%JpY4%2B?_
%hB3_&J>cm()\)5*ubt-%1a'dr>5t['b_2l&el3'(`"#?AdF_/!!*'"!<N?$!W2rt!W<!"!<WH$!!30S
"8`'""ookG!!E<(!W`>J!!30&"8i-)!<<H/<Wr[-!W)ln!!!&t!#bnB#Qau1%fc`0a&ZSK>ut'*Am*hn
BNebK?2\(0?i=@8?X@#C>Pq\(>7"P??X[GVB5)*rrbNosC1q0f>?"<f84cKN;cd11@Us(bD/slLG]S%O
Z()^8!!!$*"p4`'!<E9$"8i0!!WN9$!##G8%QB4X+Vbq1&.BTkO:`HB'GL?Y!#GDIrtt_OrYGJJ.M`g;
)B'P7*$-1E+X%sM*>T.j!<E6("pYD@$k3^Y&eYin)B'SD1OO?Kr;Zp&"9S\t!!WH+":#26!#5J7!!"a4
'd"&'$jH\B!eLRf!t#ACrX8i9$k3+Er=8T5rsni8+qYM*)&jP9*#KA#$k<mc)&aA1(`!f!&eYlq)]0A5
.!9P6r;cfurW2lrrrN&u!W`B+q>^LYqu@$'!!WEL!!*'"!WE-#!R:]F!W)j#!<j,[!<VTf)?L*K!WWE8
!!PU3='o!7=]\R7>2!:t>[UlE!+5_5$=R@P@UW\Q?X@#CrEK8+1L4<o@Us(`BP;*qD/O6,An#"G:J!uD
7nQNS<a/p?A7fOlEHceUFEhi>E#&f]!!<K2"8r3"!W<)t!!<6&!sJT')Zg!M-]\ub'H7\s%3?(A&KMAs
'GV>u'bqK"(]>3K)#b?N('G?e()Rqf)C-7C+X86W+<;:3$O$M1!X&]5#mq(M%hK?c&/#]p*@ik%9E>4o
!!<?,!Whro*!$-F#RLP4!!*'"+H[H]&JbcZ!"]3_"VLtH$Om"D":P_K%M&FJpCR66)\3Gh%1Nma)''_;
)]0;%%1<XY(E+52)&O/)'E/UE(&f'S,:A(6!!N9$rW<'"qZ$Wu!W<!"!<WK&!!E<&9E54n!!3?)-2dfI
!<WE*!<M6]quH]sl2UfAkl;e,"pb81"V1S:1=0-1<a]*5<+BCg>&IYU?XR8M@:E^E@gHOP?sd5G?!LY5
>m=VA?t*YYB)ZENC2Im.CLg^O:eF/C*CE7e9i4no?=@;SB5;F.H?sgYG/uf^%0?S7#mLM0!;urr!!<6&
!sJT')Zg!N)NtpY',qVt$l^%@%3Q5t'GV>u()7T$(\\dG(]>*N(Dn%h)Aj>1*[2pZ,p+$>%L<+9!!3</
#mq%K%1WpX&J#<\&JuZ?2jbQd"o\K("9S]+o`,s4!sJr:!WW3$!!![t(EF&&%0lkB$@W!k#7M"Mr!r]:
rXf#?rY#&>rX^@c%1<RU(*"G=*#KD&%L`[S&f2K,)]BS1'bh;n&/,iu*[<7u('+C=rW)p!rW2lr!<N<#
!!30'"T/6&!Wu@("T/6%!XBbKrW!*'"9\f.!T3tU!V$-q!sS`*"UI?n#58,j!#ktD#m()0%KHY[dog$Z
@9cu8?u4"fE+*6b@:K4G$=m[YARo:[@:3GLqHa;3?X[GTram]mASH"#EGArb:eF/B5<qS+92JSj?!h#M
Anc(%G^4XUHHd0?%0lq=#mUP5r;ccsqu?g"!<WK(!#5P8%hG!C*toS-&I]L"IgRA5'bhAtr>#ALobdWD
!u;Xg)#bE^)&O53,:G#g*Z#=n"o\KB!X/i9$4@7O%M03]$4@@],UYdK!!EK.!!*3)!Whro"T\]/#RLS1
!!!68Ql$eR((CNL$5@O](^^`^%f?k;&H3:@')E:@')`Cs&.T*U$4n!p,9Rp@&Io3V$4RUa)]Te8)&F#%
'+bZd'cSA@24":C"9JQ'!s8T+!<N&t!<N<#!!<6("TeQ%"p509$3U>1r;Zj-(((?J!!*0)"9S]+!T=%V
!V$-k"ptP5!!K8$!s/Mq!!!&s!#ktD#Qau.$3C>If32K^A7/\G@!/S[DId<g@UoCJ!+l+@"_D4S@UW[D
?i+4d@Uit]An>L`BPh^.BjO\.6U*^r4[;D+9i4qq?=78SBP_X1G'7V>`tT3n"9A]6#Qt2,!;urr!<3*"
"8r33":P=&)BKM1()%2o.U`u4'c6iar>#ALpDEiGr"f>NrYc1_(Dn/;.4cec'++mErW!r?"UGDA$k3[X
&ebfb$kF1#,rhFq"9JT(!X/].!VHEr!<WK2#m0u(&"aaZ%MfN\!souJ#o3s]&,["<&cWLD'E/^F(&emK
'+trV&If9]$jm@S)'L=N)\WYfrWrZ9&Jc8`)@[Q$(D[`!&JGp!,9JV)qZ$d&"9S]+!W)it!Wi6"%flb9
!<<*$!!`XD"UP/4!WE'-$P*IB!!*0)"9S]+!T3tV!V$.!"9ni+$imR5"onZ(!!2lqrW2lr*ruNM!<<-)
$3C[k>?t<B@piVOHAlWTAnP[cA7]=aB)Q?FAn>L_@eX:J@q91aAn>L_B5DO+Am%em4?>G^3^#_s8Jt9%
=Bo3AA7oXpEH#i.E3^Mt"98E*$OHt<r;ccsqZ$Zu!X&B$'FY6IV&^Qg)]'2$(+qin*>fV/'c$Z_rtkJJ
!#PSNr>,JO)?(N](`*u/,Ut>k)@crK!"K&6#RLkI%1a$a'G:oe&I''r,s@1i"TAB(!X8f1!qZHq!X&`6
!r`02!<<+r*#]8$%grXM,;g,J&Gm(=')rXF'`SpI('bWk()7Ms&eY$Q'+PHZ$kjR)-mKWB#mU\@#n.@Z
(]"sT(DRW!(`OYB22(i,"U,&4!W`?!!!*-%qu@c?"9AK&"TSl0IK0cW#Qau+!<rl5!!!$%"9\f.!<M*Y
rW2Wk&ci(8!!**#!!`La":5&.!<N?)q>gNr!!2rs*ruKK!<<*'#ltFg>@(BFAn,CcF*;A8BkV*iAS,Oe
BDlKKB4b^dA7K(XqI;9kAS,ReARf4^CMn$"<(/f)1c70N3^#bu92S\k>?tTE@q]^lBksJo*tJ_]!!N`9
"9SN%r;l`p!WiE''`\47$NpI.+!(t5(_mi+-Rg,Y)]BOl(&f!A(]>3M(Ch9")B'J1(De):.4c\[$MsfD
!X&`7$OdLU&/#We$k<pc,;=7H#QtA6!!3?.!Whon"9J]2#Qaf&"K!1W$5EjX$k3dg*u,M('E&RC'E/[K
'c%Q$(]>0U(D[`"&ePZcrX]nW%1E[[*@3-Z)%QoS"U>>B%M9Bj(Dmu*rY?.\&eu9%+tRV5!<<3%!!*9-
!s/N"!<3)t!##G;!<<0,!"&^Z!=T#;"TSN(!X&E%!<E6("9S`-rW1pW!!2Zk"Tno/!!3E)!!t+r#R(A4
!!*3)qZ-NpqZ$X!"o\K>"U>#9fih`cCM7<qDej!$Chm`tAnG[gBP@?Y!,)IIB4b`QAH-6?A27_.B4kgf
@q0(`CM@'L5;OuI1,LjI3^#f"9Mnbi=^,-:@qo@[F4*`)%1rgG"UYJ:!WE)s!Vucs!<W6#('=jC!2q"^
&KDW')^$.=*ZuLB(`!i$rYG,BrYYVN!>l^R)@78u(`aeJ.3B3-qu@c=!X&`6$4ICS%hTEa$kO3h,!MtY
$j."E!!3?-!Whon"9JZ0#6F]%%]16a$5=![&f25n'G_Gur=f/E#8Ish()If))?(NY)&O/)'G:uV%g<LV
&.]6]'G_]8-m9B9"9Sf4#n%1Q&JGin()Hla'G:un*>]n\U*g*E$3C2."pG)1!<N&t!!2rs&HW(9!!<N-
#Qf\_$N^bA!!*0!!!NB)!s8T+rW1dSpAbj-"9nl,":P83#M]:\!"/i.!!NK%!;cfp!!*0)rW!0+#65(_
=C,V=BEi9kBjtajCA_cFC&D]LBk_6nAnM$Rs(;1?s(;7C(M78jA7AkD7QN4U0/57>2)dQZ5Xe7?<>8\H
@qBIr?rh3h0-Uc6"98N1#6Y,,!W<)q!!!'!!##GA!!&u?*ZQ"4()nA7'cS58)Ar;drYPDHrYGPOr>,SR
)&aG5rYu+`+<_gC%0QP/!s&H+"o\`:#RLnO()n/0+!hjG5c5>(&H`FE!!*6+!W`>p!!<6("U=f'%At-^
'b:`_',V>j&JZ&Z'`JjH(+0n8(`=52)]Th:)&F&%&J#?]%hK<c',20!*?ZLE'+4sI#71bH%1`=I&.fKj
)]p+B,q9uV4eWAn!!iK'"9o#3!Wi?&qZ$Tsqu@?1!sJ]*!XA]2!.k1Y!=K&2!!2ut"T\Z,!s/Q'!SIJQ
!W2p-!X/f1!!3B*!s[0\!!!6&!!*3)qZ$TsrW3*%!W2ou!X/K&%g<+:#Lup`E+WctD/O&tAc??CC&D`D
CB\HfBkV-lrFQ%Bq.;6mBkh?n?W^/q4uFrE/hf(;1c73O3]oYu;Hm[EBQ/#u96I3S+USJT!!3E2"9\H$
q#CHs!!!`6":5&.V]['.'GM9#*>oS/*#fb4(]G0M(\AL?(Ch9!)&aG7+!DgN*#TG##Q4WD!<WK/#6tG9
!sAoB)'C(H.4u\Y98Nle":,#.!!NN)!WW8p!!<6'"U=f'"f31U*=</\%2'Hi$kEsa',:?[#T"9o(`=52
)]\ht)B9Y4'b_/i%1NdX&JQ$"*#on9(D@;d#7(VDrXBSP%1ERM$4dmn,UOlk1EmW,KE2J]!r`0("U+u1
!WiE#!!!&t!"T)5"T\T'!rrN*GQ8$M#Qjc$!<N?)!s/Q&!S[VR!W<!-!<NE/!rr<%!!rX&!!N3"!<WE$
!!!&t!WW9!!!**&rW!B5!!!)GAR]CiCMI[&C&VWJAS5^mCi!m&r+uCK");OaB_c<=Ae&KiD/<]b:.%-%
0J+k/0`<dG1c70M3^6#*:JOV^>!G9W>o41Z"onW)#6k>1"8`/n!"o>=!WrFr/0Q)P'bhH&(`!o+)?(KO
(\8F@(Cq<!(`=52+!N$Y+W1ju"9JH$*WlTO#7(P=!s&E)#7M+P$kXHb'9#6^#6G)2!!!-(rW3'#p&G0q
!X&]'!"Y\N)AWbi$kX3e%Ls!]',CE]*#KM1)&aG6*??1C*ZZ.9'b_,g%1NdX&f)E/+s%jE'+PBX$47.L
%M''[%1<II"pG8?&/5`h(*EtuMEV"@qu?p)"U"o0!Whup!s/W1!W<!&!<?[2"98W"!!E?*!s/Q&!Sd\Q
!WE'-!<WK0!WW3$!X&K'"oA9"!W)is!rW3%!Wi3!(]a[<!!*H-!<C,[An,guCM[g%An,:\B57B^!,VRM
"DhmiCMN`\rFcXQB4bahCMdlr;aiZ$0`EX)0/<>Z"Z%tm2`Ni14#J`M59iSO'G^cR"9AK("pOu/q?-Ek
%0?n;#6:/P,o7O:',;A_(],'K(\ALB(C_2u)&X>2*$?LT.3K?3qZ$[!"UG#4!s]#4!Vl^"#QPjX!!`K,
!<iQ*!W3$#!Whup!W`E,rVup"rW!Iq2'!,;$k!RZ&eGN^%h]WS(bQ[D)B0Y9*?H7D*uu7:'bV&f$k3[X
',Vc8-6F!4"pG5<$k3^Y&.]6Z$4$h="8r<#!!Nc2*P;@RqZ$d&"U"r1!rrDs!!E<)"U5#*!!NC$!rr<&
pAb0or;uoug]73P&-)\2!sJl0!!!**$*F7.#R0r&!<E9#!s&H(rW!$#!!*3$!#Q"B!"?Y]CM%U*Ci+'*
BOt[bBPVL(DJj=gDZ=SQD#J/IC(tAqB4kmlBkL[G5W(5J/M&J+0JP<]0GlN"1Gh$M3B8oM4?aU6TF2&+
!<`H(!sJl,"T8H&!qlTs!=Af1!!e]G.2a*@',:B]rttYOrttbPqA/uFrYQ(^)&aG5*$$+F,U46>"oA9$
!X/i.#Qk;8!s/5u"9])4?\SFY!sJf.!WE-&!s8T*p&G-p!sJT'!!<-"$BQtc%hK*V%MKHe"V;1V',;>^
)#bBU)B'P7*;pm%)]9G+&eGQ`%hK?g)''kF*#&b`":#8B%M'*^%h/mQ#6k>0!s\l-!"'8;@"e@V!<E<%
"9JZ-!VQKq!X/c/qZ$ap!!3-$pAb0orW<'"!!1gS$NU80!W`<%!!*-'"8i-&#"&@o"TnDu!<E9#!s&H(
qu?a!"TAB7#64`@\o)G%F)Z#8Df'6%AnPjqrGV^RqeuFN!,_^Pr+lgXCM@HpAn,1J8Nnsb0)dF</h\n4
0.nk21,CdJ4?Yhf2+Tt]Zr.M8!!NK-!WrT0r<3-&r;uWl$O6Y5"H5/g*#fV+(&f!M(`E5iru(hRrtkYM
rYPPNr>>eX)B0Y9*?G)"!uhp^"8`'!!X8K,!X/Z,q>^[3%fhhV!r`0,"U+r/!<E6'!s/Ms!!30("TAB$
!r`0*M(^+e&.8jU'E&OH',22u(]G9M)?(QP)\j5,().An&.fEe'c.c.*?>t/$3^S=%LNUS%M''[$jm7F
"pG/7rW`W2";qsYQ95!E!W`9%quZs$!VQKq!X&Z-r;[$&!)!:p!!2fo!!3'#rW1^Q"9AQ*!s8E$rrN&u
"p=p@":>,1p&P*nr;ls"qZ$X!"o\K8"TSWAZ$pS+F`MG@EGoZ.BPM@$rc%aQpi-4Ns).gQ&8Z,rAmntH
:.79%0J>%1/M@#U%PB=b0/>@C3^#_o4ZPo#"&-'>')hn*"TJT&!r2fr!WE'0"TS].JjLn))\s)%(Dmu-
q\o_X)AsA/(DcudrttbRrYkbT!ur:$*r[5c*?#_-%0lq2!!33)#6"i="pG)1!<<*#!<<*2)CLmV#Q=]*
"U+u0!WW6%rW3'#pAb9r!X&Z*!!!'!!"49>+V>:p$P!d_',:E\rY>JMrYYAI(`4&)'b_2m&J5Zk(`F;1
)&Eqr$3g_A$P!%E!t>VE#lOu9#RUqJ$4.Rn/=HbHrW)ourW<'$!<N<#!;ZZt!<WH*qu?m+3=,Zc!quZt
!<E6&!S@AT!<N?*!rDs!!<WN)!!-L:nc8Xi!WiE(qu?g""9ni@!!!-%#8F/!CM\09EcQ5@Df'<,DK#Mo
qf)FPs)S*YrbrEeDJj<,BOY4G9h%?-1bg[;r@S+(0)dF90/>CF4?l5(6pNOa^K_HS!!!$%p]LR!quZ]p
rrN*!#Qk&5!-qKg)B/qt'GVH%)&jP9r>YqZ)]BS2rYGbU(`=20)]S_q!$2%[#p194*ubt-$jQn2!!33)
"oSW8"U"o/!<E9,"pY/8SO3S[!!`Q."9S]*!!3'#!!2fo!s&H+"TAB$!WE'0F\Wqh&If-Y&el&s(`4&)
!u2Od(\nmR(Ddi&'bqDr'E/UT',;?&)]BM,&Io3U#RLhHrXB8G%1ERM#R:VA$4@7RrY#DB&Yhf!r;Zfu
rW3'#quQj!p&GR'!WrH'!!*'"'djas!!;ior;l`phZ*c[!WrN*qZ$j&#Rgt?[K$R&!;urq!!30)#Q=]0
"TSW;Vj_:DF*7J("`n[&Df9UlEV4AMEW0tdE,96!>Z46]4?,/PqChq'0)dFE0/>FG4?uJ55rh#/^`*@_
!rr<%!WrQ0"pG/5"9S],rW2iq!<E9$!##D6#lo'N+XIp>'GVE$)B9e>*?G,!%3$6))&O/+(`4,/)]Tjr
*<I9)+oWYh+WhU:%L<(<!W)j8!<NB-"pP;;"p>#0!<EE6!s&c`U':T%!W`?$!r`6"!ri;q!!<6'"9e](
!!E3#'6$qh*"EDd%M9?i)&jJ2'bh>s(B,-V)&X8-()7Ms')iIQ&.oNg'c%W()]KV.&.ApE#ltDBr=0MN
$jm:H#RLhG$k=$m&e5[;W!WM-qu?]tqZ6`uoDemm!rDs$'-%Sa!!;iorW2WkrW2-]!s&H)!W2p'!X8l5
!sm6[&a',q!X/i.!"T>8!"Pj"BS(8IF`qqNFE@;!rH&!\s)\-Zqf)UVrcAHcCLpgO8j>6j0`E^+0JWP^
(,7Kr/hJY/1H%9V5Y4g<68buD$jI4Ir;[-*"U>8:"U"r1!rW/r!<3-"!!iT*#QSdN+"e9,'aPQl)BBnA
*Zc@$*!7,u)&`Dj"W80r)]Tms*Xs59,UF]\+W_I5$O-\6qZ$a"!sAc3rWa#>"U"o.!!Wo7$j_bJ!!!H6
!W;uu!W3!!!VQKq!<N?+rVup%rW![L>Sndr%1NdY',MT/*#TJ(',22u)#bBW(D[\t&J,KO%Km:T'GhYd
)?^om&I]!F#TX3Y$k3^X%LrpV$OR1H$4I@Q%i6<$)AJGu!!!H4qu?]urW<3'!Wi/uq#CBqr;[''!tH%P
!!!&n!<3)l!;cfd!<*#q!;urt!!r]3!t>?G#6b)1kPt_e"pb50#m(G6!!f7#DLH^,GQ)akF`__HEcZ;D
FSp7_FE;L"EW:(YF")*GB44q<5rC2B.4Ql$0JbRC1G^a>0.nk32*4#b3^#l*951.<%g<:Ar;[0+"pkP?
"p>#0!<Mrq!W`?(qu?s-!,6*l-l<^+'bqK$)BL"D+!1D%!ur:")Z1H[)B0Y:*ZlLI+X/-0,6oD9*uGRs
"9JB""p"c-"9eu7r<N]9#QXo*!>$#0Jc5WM$O-G.!!<-%!WiE(p&G<u!WrQ*!!3E)!"`dS*?c"*%1Wm^
(`ab@)&3_d&ebur)#bC4(DRSp%LidQ$OdLV&el)u)&aD2'b:TS"U55>$OmRW&.]6\$k!CL$P!a^%LW[Z
+XKa=#6b)7"T8<)!<WH-!s/Mj!!NK4%h]!HkQ(S^p]:$fquQTn%flb9"p"](!s/]-?5*G@!U'Lo!X8o2
!!EZ0!!8UtFEVtUqfiBjG'.nJF*)MHr,r3cFE;JCrc.jV.<'-;@9QMs3@uL#,UY&n0Jk[G2)@!B0J>(8
3'BPg1c76i3TNO:$3LG0!"&`/#71\A"p>#0!VZQq!<NB$!##V<@<*h@*>fP-(E"27+sA'N*Zk;$!?<'V
)@.9%*$$(C+X/-0,7,P<+Wh[>%gW7<qZ.*,!WrQ."pYD?$471Lr;Zp8#J28\!!*<*r;[''!sA`/!W`>q
!!`N+!sAT(!t"r,4C;tN)ANen%M0<l+!MdF'G(fg'c.]()&O/(&e>EZ$4.%J%hTHi()If*)&Eqq#Qt87
#R_(O&.oHa%LiCHrX08H&/5li"pYMa(<A*.!s/].r;[$&!sJf0!WhZg"pPMI%gWCBr;ciuli?\Zq#L9m
q#CU#"UGD9!!!6)"U(P"$j-On!#YhA#6=f,$31&3L:;8JG^4R\H[9s^GBS+OrH/!\q0"E6F)c,8DfTr?
B3Iql2(g7$,:"Tb/MK">2)?s@0JP=<1c@9P1GD*W2NY0a!"/o.!"8i-!<`T4#R1G7!WiDs!!30&"9&9X
!<<9';gBu@*>o\3)]^"D,9nBU+<VaJ*ZZ7@)]Kb:*??1C+!)ID*?caZ/1)DQ%13=D"9\W)q#M-3#7(YC
#R:J4!!`Q,A;pWj!<<3!!!`N,"9S]+!<Dfn#6=i-"9AK*$2soH;0=3)'+YTb',DK-+<;:4&.fEe'c%Q$
(D[`!&ePWbr=0\V'cS8@*uGRt#m^b@#RUqK%hK<c&.T*V$iUP7%K6hF#mM1Z&osBJ!!NH+r;[$&!WrQ.
!Whonqu?`u!r`9/"U,nM"98E&!<N;f!;Z`m!<3)i!!NB)"9\f/rW!*('e04g!p0Ih!<`T-!!3E+!"TKT
\T2n:G^=acI!U$\r,qjX"*Sp7HN&7EH?O:EBkqX-E+)O)/1)Yg,palc.4d//2)I'A/MJt<2Dm9E/hJ_E
3_\3[(^(*Fqu@')!sJo6"Tnf-!<Mlo!<NB&!"K)2!WYQ=0I[t\)]g+F+qGqF,pX`\+sA*P+!)ID*Zk2#
$6:*))B^C[0I@VDrW!''"pG,2quQ`r"p"o7$4$e9rW!*6#U$Je!r)a!!<N?)!<Mcl"p"f/!<<6.rW!Zu
I4--I%M09i)&jS:)AWqr%hTEf'EAjA'fcp?&J>p'-S$AV$31&/#Rh1Q%hB6b',(re$3pkG%1N^Q#R1J=
*Yp?B)[QKI!<<*#!!!$$!WrK)p](9pq>^X!!WiQ2r;[*j!X/W,!<N?)l2^GVrW2Wk"9JZ-!Wi9##Qt,.
%FkR`!!E3#rrMBb*<QHG!!*9*#7aGLC3O]BH[^KoHZsRRF`qqNF`_^'EY<M>H[^ElI!^0aG&hD0>>dsR
1&rd&-N5A6-n6c$1GgmA/LrJ13'&oM/1NtV,X0mP+US>P!<`K&!!NE,"U"o/rW2Zl!<NB&!!!0$!!k*E
/h@t^+!N$--3bbB,U4KV+T<H#+<_pO*ZZ4A+X89X+<;:3$NpG0!X/f5"9\W(rrN#t%0QtG#6=f)'c[2h
[42L]!!3<,!rW*#!<N;l!!WH*"9AK*#lXf<.?u/#$k3da)]Th:)Aa,$&.]<a&cNCF',23!r#$%b*[)^M
*?#\*$jQn>#n7IZrXfPO',2,l$j["A$4[RS#mLM7*@(_0^G6B"!!E<,"Tnf)!!30&!VZTo!W2p+!<WB)
#7:V7"TY4u%/p5/!X&T+h>mNUoDf7#"pY//!!EB3!!(IH!!`N1"T\W*!WhTe!<NE'!&4T\%1Or<Ap/-;
I"6ctHZsOPFEVkOF`_\GEcQ5EH@:<oIscTjI=6?R<C&>i.Ochrr[8p=.4Qi"0/>=</hAJ)1cdcX/Lr;,
2B/31+q>7g!!!B4"9&9$!<N?*!s/Mo!"]26!!!$'!<<*8X=l4I+!W-3.0(do-Pe$T,U4KV+<VgO,:"ER
)]BhG/1r4b$N:#2!X&Z2#6tG:"8r8t!"K&9$jH\3!=TP?ITm3\"o\K'$O?k4!!!&o!;QU3!X&Q)!sSi/
!#)1S*srGj)''_:)&<o!&H*.=&-WXY'GhZ-rZ)Lj,:P6!,o6mg!!3?4%1j0N'GqJt'c%Mr$jQn=#n7FQ
!s8`?(BB.t&HN4;!!<W:"9J#mrrW)u!WiH*#lt5<#m:Y:i!'_k!!<9*!s.6YrW2Wk!WrZ6rW!K<!"BQ&
&/5*S$47"@!s8T*nc/XjqZ$Wt"9&9+!X9)E*klW8Esd5DKReJrG&qbJGQ)gmGB\:WH$XjeJGt-WJ:;fe
De<$<1*dtb+XA?[-RgMr/MAe41,:R</hSk93BB#N2*s):CRcIe%M&[B!t#88!WE'$!<N<'nGj1'!s&B&
!s/K($_9I8+sSHa-78U9"XPE>,9e?0,Q8qp,9e<W,pt#['+"R;$j$P8"pP;:"U"o/!Wi/u%KQ\;"9AoO
&HG[`%1WFDrW!!*"p4&i"T\].!WW<$":kP@Q80Ki%i--()&<nu&.e^K#7_4T&ebrp)&4)3+X89\.4Qep
*>/PV!!3?4%M06erY5GL(]G6i'bC`Y#RLhG#6YMY'ED*h&.esM!!!'-#Qt1u!!39*!W<!,!<N9&"ptJ5
%LLDc%/p8+!qu]k!VQNg!!!&l!!30&!Vl]t3sl,nrX&c5"9S]+nGiOiqZ$Wt!r`0@!<iiA'q0hsGCG:#
IsZE_FEMbOH$XgaI"$TsJqAXRJe<Q^FD+lQ5Vj`-)B'S:+<r3^"Y;8\1G^fc0c;`&1Gq*N3Ar`B4>:Ej
0E;@a%LE7A#6b21rW)ounGj:)!sAZ*!!*-'"p]QW0de>".3fuY,5ibc+p/u3+sZt1$RR5L-mg,Y)&!Je
#6"c#"Tnl0!Wi9#rW!Q3!sAi/)A>rX,QIfG#R(51"9Rff:]UY%!s&B&!sJr8G=`kf&fVf.'bLrc$k!CL
$OdIS&/,cp)&aJ9,:G)q.jcAV&e"sF!X&`8%1a$b'c%Q$)&aG4(_mVl$OI(D#71DL'2T+I,6.]F#mCA5
"pG&/nGiXp"9S]%!!<6*#6Ff(#!rb!!<E6&rW)ltrW)s!qZ?cuiW/rZ!!2ut%06G4df:9i#m^hC"p+i*
!V$-i!Vucr!W<!6!sf/I?FOcnJW,21H?XLRFa&(VH[UDCJj"dAKnP)0J:2`cAl_A[.j5cE',;B)+<r6`
/ho4B2)?s@0f(^J2Dm`g2_Ha(?ca_t!!!**"pG28"Tnf,q#L$e'`eC>!s&B%!<`K57Z/oH.l/Ip*ZcI'
+UB24+!;^N+Wqs-,7>bC-7:/f+W;"'$4?b=rWiN0#5n]>"pP55!W`<'!sAT(#7Ue:#lmN,+T;?B!X&Z*
!WW8i!;ca4!<WK-!<<*$#6kW'IiAk4+W)%0%LWUMrWiQ3$4ZtG0G>3>)]^%H-nHnr*>Ane"Tnf."pk\I
%hTEg'c%W()]Tk;(`!bn"qD7N!snrs[N,5GrW<9+"9S]+nGiXq"U"o(!!!$;!sAW)!!<6Q$ig80!WW3%
!sA`/!<<*#!Wr?'rW3'#iW'#^"9JH$"9SW+"cWE\#Qb27#6k;4!<MfmquQWo!!2ut#6b)D-e*6[ISQ2R
JU;WbF`qtRH@('nM1g>/KnP#+HZjCE@T,WL,T@I1%hKEl*?c^W/2/k=3B&cL0JPCE4ZG8c:HU`n*4A<P
$31M<!!!0,"U,#1!UKdh!<WH,!WE'3"TT/JXZ7g\4rY^f*ZlOJ+<MX2*ZlXU+W;@E+sR"20d7b^(_?uV
"9o/?$k*LO#m^_<"9eu6"U"o/!WrW4!<<HD$5!^JUcT4u!>#J9!!<;m!;urq!!E<*"U"o+!"K58'Fpf`
&JZl/*"rei$2k,:#n%@^&e#?g)&jSN+<i'W,TRO*!WW3$!sJr;%1Wm[&J>cm(Dn&1*ZQ(9(C^Q\*"<Jg
!2)4Z"oo#5!!*!#!WiE(nGi[s"p>#/quHWq#64c3`W-&?!r`0+!sJl4!s&B%!<W0$!WiE(p&OI[('=a@
!!<T/#64b\#6Y,0!WrT0"9SZ*oDnahnc1BT)3V48RVAF5G^F^ZGBnL^IXZBUJ<GnDI<TR>>#7[N1bC'u
*#B;%'Gqf5-7LK!1)i&-2)[BM1Gh$L3BK8W1H[WT_Fk%8!!!6*!!)s"!WiB'li7+g!WrN&!"8o/%1$lu
+%m;;&f`(n,7u1H,pXBB,r[S.-RBlS((gr\r<<<.#RUJ;&ISsR#mUV;"pG,5"pG)3"U"u@"pFu,%M9MX
49,H`"UkS8!!2TiquQZp"9AT-!s/B$)$C$Q"_DBS3!MMT'bq>k%M'-a'GCcU(Fgg3+;,_7(_mYo$k!@I
#6k>8#7(\H&,m+?')iRF(]G<_)&O)%&IedD%hTPT2ZNg_!!!6*!!!$#m/R7n"p>#0q#CEr!r`0./0tE!
#QOo+!!*3)!rN#u!W<*!!TO.^!s])7r;Zp#!3m@=!<3-#!WE0#!VHHi!V-4^#89>\JT6okM1BtuF`r%V
H@($jK6_?UGB%4s8N\XO)]B\<+s7pG)B9kE-S$f'1,LjD0/GRI2E3]S1d",Q1bC8[LEI'8!s8E$quQKk
qZ$TsqZ$Zu!Wi/u*X;lmYsBa)(,%$],U=]a-n-Vr0f1@&-7gVl)\NGXr;['*#mptF#RCb9$6BKZ"pYA8
!!<K2"9eu2!=9><#6bKtF;,#j#RCV;!V$0d!W2p#!!!'%!W2pW":>8LUbEZH&1f"F(DIW%)B9_;,:4EG
*$cgS*#/qg!<<*'$4dUT$4."G$4I@R%hB9d&.T?j(]G-[&.K9i!!rf9O)Y^6#6P&/kPtbi"U"o/!Vl]r
!<io;!<@KI!X\o7!<<*$!S.5_!X8o;"p4i4!!#k+!!*'*"9JH$"9AT+!<Mloq>p0f$3UYfRIb$GGBnk$
4FqX!H$OUOAnGasG&qA!6T?_H+rqO:'GD,q)BL(K-7:/i.k`\4/i>aM1,_3S2`NTI0Jt+@c;"?S'bgQH
!s&H(!UKgd!V6:+"oo<S\Ka3_,;(u1-RpZ!/0u>[,q]N_1bKm`$j[%?!s8B#-NO;Q"pP24!<E9+!WWK9
#QY&5"U"u0!<W]0+0mj+$P='Q!sAc1!qlWi!<E0$q#LEqqZ%c@$31TJXV`r?+tPQ!*$6@M,TIL5)'^X_
-QNg2%h9!U$7lGf"pG5<$OdFN#6b56#R^tH',qYq%M93]&.AjN%KIQT2?4!l&-)\2!WiDg!!WQ/!s/N)
!Vl^$!XA]*#cdq+"oSE%"9IN_o`,=#!<<9/!WW3$!3,kr!XJr1r;Zs$!s8T*p&Opio)LZP"ro\El?Zoj
M2lsuCi3ruCik&QA4S^6.4$&T)]^%E*>]>"(Eb1`2E!BG/hJqD4#S`A.k_Gm4ZYJ_0JZBH;8ZHC*!.&`
rW!$%"9S\k!<*#k!$V[K"r<K-2]+>45r'Z3.4$2i2aTqd('t$C!W`<*$4daX"8r3.":5DB"p+c)":PVA
!WE'+":,25#lk/V!&CJ\5l_Dq(^C$@"9o&5pAk!imJor`%0-MBNMnZM1cdfP*?ZUN+"&d(4=:XB!!*<2
$kF!e(_R2Z!!3E9&ePTY!<<*%$Od@I"9Sc5%1<IT#n8?a0W%&7%KI4H!!!$&"98Pi!<30#!r`5r!"9,:
%00?q!"9#7!!<DV!!*-)rW!B1#RUP5TE"s%!"&u9"T/6&!<`N-!rW,q!;cff!(R7q!$<DuXI4!=ATE06
?>"1d9JdtE2(p:#+<27<*[2s_1,qKf9iYD*AoN-SO+D+P9fjgW3&icI-m(fG3*jF&'EA4>'*\@8!s&K*
!UTje!<*#l!'(5k!!!-%OEb+d-RUf=1+"\90H15s!Y5V?!sAZ+!X&]5$4IFX()\,9,:>3.8l7u2,8:4[
!!NQ0rW!-:*"tQ:63R8f#8%.?!!*0*"8;fk!V6<h!&Fuo!<<-#Mfi;Z,pb<0/gE#10,Xil!"KDB$4[RW
%1<FG#RV%R'cA#7+!)XV2a/r<'F=[<$j?nC!WW3@,8WSB4otW_!=o>4!!33)!qcQl!W)lr!rN)p!!!'!
!!!6+4<4P+f)YgOqZ$j-%Kd.PV#U`!!!<<-"pFi("Tef0!s/Mt!;cfg!"]29!<N6N,)>,i4!$+:-n$8u
+!W*\-mBZQ+<_mM*[3!b2ap_YF*`7cKT2:fSskt5S=#M(MI\n).5`eF4$dB!.hE9t&e>6Kr;ciulN$nb
p&G-r#RgV3#SI8N\N:9$"qLP2#Qb5<"p+o4#RDsc!s&B%!=Thn1,_'N3C$)-9hS)U=&i'o8gt&H!"&iB
%N.X=)$1!B$OR(>r;Zj"!VcZi!Up("!XK8I!rr<4!F`Dr$NL59qu@-.#R^qE%2'Hp(_dD_rW!$/)'p^T
.kE8*0J+b$,V(W+1,q-1!WW?:%NcQ37^3[.!WWQ6"TeQ%!<N;q!;cfp!;uri!"K)2"p+tU#6b\?!!!''
"5s4^!<WN3q>^s3$O>_u$kNFE!<<-("8i-&!X&T-!Wi#qquQ<f3s,H_"W@da+fgi3,oJ9\*Z#G2(_I5e
&/5s$*[3@-<b?E%LQ@XaQC+>DY-P40UnOWbUS`0$1+F(r+U]`k]+u;')\ND]!s/5uq>p0frW2]m!W`H0
rW!H>!!3LiGs;W9&IAL=!!i`+!##G<"p>#6%MTg+.l9:L4Zttr8PT1](K+79?W^Sj%0Zn8$NL0RT*#Q9
'FOsE!V?Bc!Ug"]!X9#B!rr<2!!!4]F?9[,&.8XA!"B5<"ptnX)]]k6'b_,g&f;]:.4d)*0.eY#+WMFA
,qgl4)up*M!#G_EK;/GR%1igI!s/K(p]10kq>oj]#6Y,3!!iR$3;`a^!<`E'!<<-%!rN)j!<3)u!$hXO
$k3FA!!*6-!!"`a&Hi.9!=&c.!<WB(!!!$$!WrN+!W`>u!<3&s!UTkP#6PMO'f;SS7M[*\'E]No#mCG:
$kaF#.n!fnP+%o2S"-%?Sti9gZEC-uS#X-%[>.4*+>b3Fa-dMa&e#Te!r`0"!W2p$!<N?*!Wr?%oDnjk
o`,!n"9&93"onu=$7M+!3!Tut"TT>I!W<!(!X&W2&g/bb48h8^4[)(s77g0I9hJ)`CKY48%KuhH!&gNr
!#5nJ'ajm>!!2rs!!3$"p]9pc!W`9$8,rVj!s]/9!!<H+"pP/QNf5k%'+#'I*YSkf%MK^"*ZZ4C,UY#h
-6sf`.kWM-.3ouP&ISpa0-`D!!!*<I$Uh.L!##P<&-r17!s&K*!VHHi!U0Re":,GG#8$qM!!'!4!!!?+
"Tno1!<N?*rW<*#pAk-mrrW-"(^13U&.A[H$NL/.[Ntnn!!!91#6k>6!<N0$r<*$#rrMoqqZ6$`$N^D2
$kX=0Wh(4K">_k7#n%(I$k<pk018r\KTqgfOGo-XNfTBkSY;aMSt2INWR./C3\iOD`*!KY!t5SO$N^5,
rrN&u!<E9$"9/H%!VHHl!V??n!WW6"!Yk_9"ptniU6ZN+!%n6T#R1D7!W`?1%i-?A3^cA&5<M.t7nZTS
<;]c);cd"J;^W(h)/-$8rW!$+$5!XD!<3)t!!!&r!rE#c!!iW."pbA6"Tnf)!#>\G-)$YC(^;ht#n.:V
(E+22,:P#d,Q8hg+<M^L*$Z[M)]'5*)]]t=+!*s'%0RCgEjeU@!WW3&$jZb3!s&N,!VHHk!TsFb!sJo3
r;[36!Z$AW!rrN*!!38r!!!&h!#,M?#m1/2!!!GJ&c`%:!rrH-"9S`(!Vlfq!W)ln!UKeF!XB)F$5<dR
Kop'`$4da[%h]Ni(a;.KC3+o]LOjeqF`qtSI"6p-NKKEmXhLEqW(TBbYa?[@#8%%A#n.1H!r`3"!WE'#
!<N?%"9&B#!VZTm!VHHl!C6\c!X8l<":bP=JraRZ$4d^X$k3RL!<<`Z0K;El8OPg.6V1'R=^,0=?<piD
CiiEA?P!r@RYM[Z$31&1$47"?rVus#!WE)u!Vc`q!Ug$f!C-_i"U5/7!WW9(!sS`4!X=@CD]B<#&.8s_
)&a;,-T3V(,9nWk1,:R=0J=t+-RUZ44#oSr)A"\)"@/K9+9iAU!!<9*!s/B$rr`9%q>gHorW2Hfr;d*&
!<E0#!<W0!$j$D4$33&/$3gP:!!;lp!sAi4"7Q9r!<<f=!',f7%fQG1#6k20quHTprW;uur;cftqZ6Nn
!!2Zk4TP]p$3pP2!Z6rs2&60+$j[Lh*[*sdDf0`HI<p-\EG]E%BP_X1I"I6;OdE/kWFs9*9F1t.#QXr3
#R(;.!;lls!riB#!r`5p!;lld!(Htn"9SW(!umE+3Z7u3#m(GG"99&d1H%[#>$bTGA7fLiCi433F)l/2
>ZP9Y@P+(`3rfKm%0HV7"pG,2!<<-%!W`<'!rW/q!ri;i!!NB)!WrQ.!sA`/!W;uu!W<!Q"sBAD4r=8,
"9fJ^'*oX;2_cj1*>]bE.4Qi!/M8\0-mq2W5qO`W1^f&F2ZX<u&Hhe.r<!!"p]19on,W:c!WiE(q>^Qu
!!!H5"98F"fDl$S%0-A/!rDs!"UYY:$lfW]#R:P<"U,)9#mgb:"UPGC0>%8k!!EH*!!rl&!;HTp!;6Hk
!;uri!"K&8%1`^E"p,;pRZS[-(F';#.j?')DJj'#DJsK7EGArd<)m%*@VKe)IZU1dNO%b?+rC1X"9AZ4
"TeK#!!3'#!!DrsrW2coqZ6Wqr;lWm(]amM"TSf5(."[\+qt[m#9!aG&i)C)5trS&=^YfP@pr_P@Us%]
Anc%!DcK8IZm#b^!!!E6#mUV9!<E9$!W<'$!s/Q%!W)ru!Ug!h!<W3%!WiB'qZ%fC#m:5:%3J3=Or"</
!=U:e!#[d\6XYG/Up.DE`5]pFe^tPdb-[%8<_k7a8WsP_!rr<5%1*.4!<3*!!ri;t!<*#f!;cd!!WiH*
q#Cs5%LE4;!!*V.PlUjm!!W]3qu@'.$kO'e(D[\t&.eaM#nR^`'+G3I%2Rk'!!!c4!!<?0#mKo#nH&Ri
r;cZpo`.#S"UPM;!!X#=$iiPhJjU=q&eGgA@VKFa?X-c8;GKeP6:==;:fCFu?Z:URP*+9H#QYA;!!!-,
#R(2/q>^KrrW;our<!!"p]10lrW)isp&GR+"onW/'akWS7&GJt%1rL=.Mb$59NGJ/A7fLiCM[j*E,fl<
EGT<)De<QmYRgd7$k!@H$3p_9!!!'%r;cs$!X&H(r;l`rrrMQg!!3!!rrMrr2?F$^!"9e\*!AQtE\e(=
$j6YX8n<-qKoqq$WN`kE_9('RdCPp,H#@1l9i%;]!!!E=&.AsOp&P$lquHZr!!2QhquQcurWDrr!s],:
"TAB)"98V=&In[=$j6P1!=95J&J,B[$k<1G%h/sV%M'*^&J+pB#A=;H#6"T*":,;="76*a!W3!!!rW,u
!WN6#!VZR8!WrN."T\T'!s/H8$Nan[A/$!p(c5,s@9H;p5r^Y!0H;i*3'BMk4Zbi*BQ/-`S/)nA"98E(
#7(S=!W`?!!!!'!!r2rt!WW8r!;?Nm!W;uu!WE'%!<<*$!r`0Y"9SZ=$j'qS<s&X,!['g1@q/nS?X-c?
@V0@lDJsH1CM7@!G&M)PN!B[i!<WN3#mUS6!!*-&quQ]s!!2irrrMoqr;lcqqZ-g"!<E0#qu@c=!!!-0
%1=$\!*?[4$l9Bl4(O&?][#*]g"PHNnb<"^'CsYVO,/R9Cl4)R$315:%hB*T"7lNf!Up*e!WE0!!rrAu
!!WK-!s/W3$8Df%!!!&O!!!-,$O$M9&ekui#m1/-!sT&=#mgkC#m^hI'+ksMB*/SC!WiK0#m^\9m/["a
q#^KprrN'"rrMoq!<E9#"9JZ-!rW**&fq#Y(1k-j2%(?J;bobC2(pF*+WqjL+XJNg0J4n*.QgR.>D]!O
!"0)<!sJr:#R:M9!s/9!"p"c,!s8Z/qu[!%!Wi&ro)\di#QXr-!WrK*!<N&t'G)2`"V"M2:a5ub>@V/U
C27QuBPS/sEHHAKH$OXXF)cGSF`3P@rW!?0"9AT."9S]+!<N9&rW)ltp]:R#!WiB'q#L<noDejlpAcE=
"U>8J)ZTjE=gM[)-;TbsW3sF\bKnYjhrO"ho_8%Dg;^N4Z*'UVXL/<:!t>_K%1EOI"9J/qp]9mbqZ6Zt
quZs$!W)j$!<N?)!!3<%!"o_R]F4cG!"9;I$O-b:!<<*$"8rE&"q1Y>$P<dY-s$BN!"B/:!!*6,!s7ii
r;lWor;ciuquQj!qZ$Zu!X&B(4Tb`g"TSN(#mq(Q%g<k%WIn>C:,jOB*uc%5(D[`#()\)7,9e6M*@s<7
5^&e#!!3Q9#7(VB#RCY>"9JT#!!30&"8rB$!s/N*!VZTe!W<!"!<NB%"9\f-!!!'!!&"BV#7V(A$lG7T
>ZblU?Y==uF*)SLG^4U_IXcluIscToLO!p1]*869#Qk&,!<W6&!WiB'qZ-TrrW;lsrrMoqquQBhqZ/_X
!!*0%!!Wo@#RLV6&gjcQNg@,VUo:K*]uA7De(31+hr3SSi7ur9e%Da(h]NIA'bC`[$OR1F"TnAt!!3$"
rW2lrq>g6jrW<!"rWE6'!W<!!!X/H%%0Qn9!"9&3SQQU+'b:WL!#bk?!s/N)!<N<)!sA]/#7LS74h(S%
!#Gn@!;us!!U]sd!VZZo!<3)u!r`5u!!**%r<!0(!<<0(rW"eZ#7CnC!rrZ5EMPiO*Zc7=()%;m&J>`l
(E+87*?,k6+tPB,9m0\O&HE%H&.T!L"9er3!r;lu!<NB&"T/?'!WiDt!;6Hm!WE'"!<W3%!<N<$!!!&u
!"T)7#Qau+!s3\V@pW>LC2j,k#'+d-G'J=\rdG9'I"6p%J;BtF+W(1[rWN9(qZ6KmrrMiqrrMoqqZ69g
!<E2t!!`Q+!='#>#6Xr*'bVO[n>NOl['mQ\`QQWWe^rL1i8WhsjqQn;in)Gset+rS%h0$Z%L`XL"p>#%
!!!&u!r`5m!;?Nn!rN0""98N$!!**&r;[9,#6b)-$j-SMbm=aX#Q"N#!W<!3!<E6(!sAi/#V)_a!WWK-
!sAc0l2^eapB(<oquHd!r;lcq!s&H)!VcX&!<if1#T*dJ>*NM[.462X)]9G+&J,Nf()\#0*#on9)&aJ<
-8@,TNDp)e#87d`#QOi+!sA]%!!**%q?-]urrMlpmf<Om!WrK)pAbp/#65#J$OLIILi?s;BPM@"CM@Hr
CD^o,EH?8HG^4R\I=[*1H^2-](C^HQ#mpk7!!!&o!;urp!ri;s!<3-!!UB_3!<WK2$4-q;!#?.bK\42Q
]=u2%aNMoWeCN:+gu.5Ul0@Qul08rJlKQODl]a(E%M0-_%1*7D"Tnf#!!!'!!r`5l!;6Hl!rW6$!r;lt
!s8E$%0d(D"9o&1])VgD$j?\-!<3)u!"K#3"9\f-!$E2*#m:_>$j$bB"R6!d!VZZp!;?Nj!!!&n!#GY=
"W7:?'L%sD0c^rA)]9J.'b_2o(E38nr>beW'c\591GrE^+!:Rp%1`XC!!*-'!WW5t!!**%r<*!"rW2co
o`>'or;lm!!!2cn/cl+m!<XQG\R9&V?XRV^B4YU`@:EbZBPM@$E,p&DH%(@#Lld4TU,X_)"U#)7rW2Wk
rW2`oq>gKrrW2lrrrMZj3!9Kp$jm(M!!"K]foMu1\A-50b08/Wd*^:kf%]0Glg4!(m.'cEp$g>Xc<*@?
#mUnK$jm:G"U"N"!!3'#rrMlpqZ-KorW)ouqZ?cuq#LBq%KQP1!s/K'#QhgM!!!$#pAb3q!W2p)!sJ`+
!X&K'4LYXr!!EB,!s&Gh!;urn!rN*!!WE)u!Up(J!<<*,'aG3K"HY5g0e3\<)AsA.()7N")]g.F*uu=A
*ZuUJ)]95L$9h.C'En^J$j?V2!<N<'q#CKt!WrQ'!rW/o!;cfr!<3)t!rW0#!Vl^Q!<E0##o*a]!?JOQ
B68<'=D;;R?X?uA>[CcG@qB=gD/aQ?IY3H/ULJn-YUBbW!=&c0!Whonm/d.errN#tqZ6Ek('"=;#RUtP
('G*J.*I10[)BJabfRoHr5g&'bgG)#jlYailLXoQqu==R\Ca+`"9],B%1EUN#6Y)'!!!'!!ri;l!;llq
!;urt!WW8q!!rZ."9er2!<<*B$38QW!!<3.!WW3$qZ$Zu!Wi3!"Tno/!!<N+!"1'l!<<B.!!!*'!Wh]h
r;lcsrWE'!q>^Krn,O(%!!!99!!!4rCF1MD1(#?:(`FG5()7N")BBn@*?,q;*?QCF)]9>=%Q-dYH2nfp
%0HM/!s/T-!Vucr!W3#u!Vufi!W<#u!Vc]r!Vufq!?;(>"q^h<)o.bDB3'C]F&u^S>Zt94=^#':@:a-d
Ci402FEr=gJraSsKnGTi((1HNklCP\quQj#rW<*#quHQop&G[*"9\l<('=ghf!gF,R)uJT[/RfS]tCti
]tV7q]tM2#ce.7EpAOjfbR`CO]=\b#'+kNS"pYD>"p=]%rrN-$rrMWi!!<*"q>gBnpAbd+!WrH'!X8W1
#aR^U!!*0-"SVor!W<!#!<`Q-rW!0*%KICs[K$R2!!!&p!V?Bj!W3#u"8r8^!&"?W#m(*7N@H(]-l=i[
'H\//()7Mu(E"/2)AsD2*$$(@*#fh7)`B<+F*@Th'*nL:!s/W/!rDs#!!**%!rW/s!;$<i!!!'!!rW3&
!WiE"!!33(!WE'1!XoGJI'QmX9PI^X?<:N9=8c/)='8d9ASH"!rbi9gH%(<jFG=gLQ%o>C&I.J"rrE$!
quZg!rrW3$quH`tr;ls"nc1QT()S0ZeV9-AXes:HXLGC:Y,n\+Y->13Un4*T\&[(Zlgj`7i9JOlc)qTl
*";lJ!X8r:"9JE#rrN*#rrMcmrW*'$!Wr?%pAk3op&P'm&-)\4%0-DNRfE]o'Fb6M"Tn8q"9J]/!s/?#
#R)%]BiG]F#6Ff(!!<-%quZiupAk0nquZj"rrW3$qZ-NorrM]k)$UNP!<>$A/gMDO(G?mP,7#A.'bhAt
()Iec(]kQn*<$rl+!DRD/M/8=Rkt*X"T\T'!X8c/qZ-Hnq#LBpquZftqZ-WsrrW*#!<N<!!!*-(rW"SQ
!!WR#ZrgF2;H.F9=^=?s;c-Cj<E<4*?!q/RB4u$qDf^/MFEE%X?uWG8!##P3!!!&h!<3*"!r2ru!ri<!
!<3)t!WW8n!##J>'H1cALldmeRBiT_WK3pKS!s>G+Io!pTqnWi[CsQ*g#MA[k4%BC\`dE2+UeDP!!EW7
"9SQ&rrN$!rrMfnquQg!rW20^!W`?'rW!,7!X&K'#m1J;"9\8r!W`<'rW<H.!<E0#$PWR@`r,l@#6Y#-
"9eT(rrW3$p]16nr;us#rrW3$p&P*no)KO6(B=F<P]/&i-R'WH+!)@D&/#]n()7r,'GM8s()If*)B9b>
+s\9P+tG6(;3q7k!!r],!<rZ-qZ-NppAk3orW<'$r;lcq$3://!s8Z/!s8T*qZ%oD"98E'$NL/BZBnZi
@U3&-;Gg1g77^-K;,^Ir=^#!5?!h&PBFelrEccACG'e.AEMj*S!!i?#rW2QirrN-$rr`3&rW<3'!<N)u
#6=i,!WrN+!V?@B#lkPogW>V@WMH)EP`q5sLl..NNJi[ON0^3@\@K)V[CsZ1hW*hho@^ma%FljO#6t5/
!=9#7!s/N"!ri;p!<3)s!r`5`!!*0.rW!(12Zs*]rVus%!qZHm!W)p4"9o)5!!<H+"<YDZ"TT#9!!!0*
"8W*"!r`5r!<*#r!X&T,!W`>a!##VL"TT^".4QA^*ZGt:*?,n0',:E\!#5DG*#','(Dn#/*$$+E*uuLR
.PO;B:]LJ$!rr?*!s/<"quHctpAk3orW<'$r;lcq!W`<'rW<9+!s8T+qZ$Wu"TABT#6P2jW)R#'?WpE(
9hnAT6q0aA:/Fhf<E<1'>$PEEAnYprDfB`@I<'"<RpZ4!#l4Q!!V69l!<N<(!sAK)rW<3'!<N)urrN$!
!!2]l&HrR_=k/G!S#<!KOH#9[N.lubL*;8(K8,GUVQ[8.YHYORbh(e;oD.@`[a9^F%LE+8!=/l4q#gTt
!!2cnrrN'"rrW0#jT#Gg(_29##lFZ'!s8,qrrMuu('=[C!rr<%!!=:/+U.uV"onZ+!s/Q-r<*'$quQZp
rW2cqrrMrrm/Rb%#R(3TB-/?;*#TV5*#fb2'GLEZ#nmsb',)&p()Ikf)A=&1*#p+L-n[J]RfEHl!WW3&
!Wi9#quQEirrMuurW2iqrrN-$qu[!%!Wi3!!<E<%!&4N\$^H]H=]Sa.;G^(\8OZ!77S$-F9i"Vb<E<4+
?=@AUB5).!Ed<(UD/"C)":>D8qZ-TsquQKk"9AQ*!sAK)rW<3'!<N&trW3!"!!2]l!!3ZD,.P:>QC4J=
Q]d>cM1pT\JfoVpJV/fBR\H[XWiieFa3i`,p%mgq\$t3:(CC3D!<r`("TAN'!ri;q!<3)s!r`5^!!E<&
VCDlM!!**%!<N;p!<3)p!WW9#!!rfC"uW@[!"9,7rW*'%!sJT*r;ultquHZrq#^QsjT#et!%+$^.2<X9
(D[l,)&F"c'*8j]')iLI',)&p(E!)g$5sg%+!`*Y3^J]nqu?d"!s8E%rrW3$oDnjkquZiuq>gNrrrW'"
!<N<"!!**%rW")H!'.Je>YS1!<)?=_84Gp35sn%084lNL:Jk%k=^5<C@h*$\B5DR4I!'7IE3<CN#Q"K$
!Vulr!Vl`q!WN6#"9/N'!s/N)!Vufn!V?@(#RO>]KTh:ZSXPb(MMHn:J:INH(4CX^KoM@fTVJEdZb+-!
g#_f!k0CuO"5eJD%/p5."U,&-"o\Z(!s/N)!VZTo!W3#u!U9[b!WE'(!<<>I"onc,rW!!#!Wr#prrN*#
!s8W,!W)j"#7ge9SGiKm!<N9%!<NB&"8`/t!W<#r!W)rt!Ta:l#69*D0c(]A&eYin(`*o$r"K)CrXf;H
',))r(]G6S(Dn#.*W@/`4>LN5qu?m%!s8T*!W<'"!W<#m!<*#t!WW8r!<3*!!rN-$!Wi3!!<E9$!&+]]
P&=Z$;c6Li9hS&H69m^u5=%Y)7Rp$C:/Fhh=^>ED@Uit`Dg$DJCO^,_Z4I6;!!E<(!WrQ&!r`5s!!30%
!WW;t!s/N)!VZTm!VHFH$kTJ'O+WLVQ'78eLP12,I!^0cH[:!bI=d<;Q^aVCWNWeF`m`o6o&\6LZH1ZD
%K6>-"TAT)#6+l+"9\f/!WiDs!;uru!rW-"!:9dd!WN6#!!WT,2$a3a#Q+Q'!WiDt!;uru!r`9&!Wi6"
#lt,2"ona"S,ifl!!!&u"9/H%!WE0!!W<#q!W<)u!VHHe!!30&"9&92!XGGP-P@"%&.oQk(`!f!r"B#A
rX]eV&ebrn'c%T&)&X>2)]Tk@1H%ge+8l3=!s/N)!W<'"!V6<f!VZTo!W<)u!s&H(quH`urW"VX(VWpQ
8ki#T9M.iE69dRo4$5Yj5XIk.84lQO;H?t,?=.)LB5M[4FE)bSJ@dfFqZ$TsrW;s!rrW3$q>gNrrrW$!
!WiB'oDndiq#CR--.mU&JI73lOH,3QJUMihG5QJ$G'A4\KoD1\R\$:RYdV9ig?7kcg=sZ]jA6Bd!<**$
"o\]+"o\W-!s8T+!VZTg!U]pf!WE/u!!Wr6d/Xs_"T/9!!WN0!!;Z`q!r`9&!Wi3!#Qb&3"WA-"&H_n2
!<E9$!sAZ+!!*-!!rW0!!:p6W!!36+#5nN5+.5J+"q;"O&/,cp().Dp')iLC&H31@&.ofn&ebro(E"/3
)]BS3)^-Xm13?1i!!36*!s8H&rW3'#nGrFepAk0nquQs&!s/N%!!30&"9&9I#W'#06pO=98kDK?5s@@j
3&ioZ4$>en6:=:792AJe>$P?>?tF']DK9lEHA6L?CBX\?!W<!"!<N?!!s/N*!Vufr!WE/u"9/H&!V?Bg
!W)jO%7A[5GBnmuMMQq8H?XFMDf9N3E,]f;FaAUpNfoZpS>)sb[`$YPkih*ahR;$j&cr@D"9\f/"U>59
"oSQ,!s8T*!VZTh!Ug!k!<N?*!r`0*"TSc0Ym^s>"9&9#!W2rm!W<)u!s&H(qZ$j'#mV"Y?iUK2!!`N*
!WrK)!!!$"!W<)u!W<#j!UB^f!X8o6rW!F<E"s6"%1<OR&JQ#s'GLEW+V5.p%LimY&.oKe&ec$!*?Q:?
(DRf1,r%&HHN4-P"pG,,!<N<(!VZT[!;urr!WrN+!Wi6"'EJ:<!<<+HPXSMB8Oc-95sILn3&^an+Z;;?
4$>eo6UaO=:K(=t>$PBCB52=,I!gNmNM-CX#6b2.!!E<'!WiK&"9\f/!W`?!!<*#t!X8].!s/N)!V?Bl
!W<'$!<<-!!B^>dN3[AWJq\l0J:)T_E,B?(BP;*pCM[m-G(#%%Nf]HjS"Za`^!#'fkj%<h`PB,"%LWLE
!WiK0#6b;0"9\f/!W`>r!;QZl!;-<o!<WK.rW3K/!Wrre?j6c7!<<-$quH`trrW0#q?$Tt!<N<!!!WN0
"U#\QE;BP:!<WB(rW!!#!X&E'r;lltoE"F]qu@K6"pkP;!!&H<*YAnn$OI4Q',D;s&eY*S#S.CT%1E[U
%hS^P(D7K&+!MdG()%N,+s\okSH'!&#R1A2!<*!#!WiD]!;llo!WW9"!!E<*"U,)m!4>^%9MA)J5<V+j
3Ar]L0ekF>1c@9Q4$>eo6qC!J<*!+)>[V)TCNY&SH\QU_#Rq+H"T\T'!<E6'"8i9(!s/N)q>gNrquZm#
rrW3$oDf[.!<N<)!s&B%!X&]6#KUn4JVAi0HZsQ7E,0-!AH$$c@q9.`Bl%g8J;9#@NffTqTW#9:d+mgP
mGQNnkSk<J#mCA2":#/8qud-)!s/K(pAk!imJm[s"9el/"9nr."9>/,'E.t5!<N<"!!!&s!r;us!s&H(
q>^g&!sT8OaT)MG!W<!!!s8E$"T\Z,!s/Q&!W2ro!TsFt!XB);!!!(k,9.4'%LWRN%h]Qj&eY*Rrso&<
rX8f:%fHq=&Jc-#+!MdG(DI]++!E*YQQQJ:":,,1!W3!!!T=%T!W<*"!W<!4!<iT.#nsjB:J+5M6TdCi
2`3BG0E*R@0/,.;2)dNW5!VM-9i4hh='8j=AnlF8I1(@SG/>^7#m:J7!!*!"rWE-&"9S`-!<N#srrN$!
rr`9&rrM]k"9AN)!sJT''*A:>%NWi1H[pa$I<KUIBObFV?2e(R?!^lH@qKOuH@^a)MN*aaS"m4&bh2%E
n)i,roK3g!"pY20"9\u8"U+`*rrW3$pAk*llMq@p!sA],!sJ]*"TX_d%/g2+!W2p!!<WGp!WW8t!!rZ,
!Wif9Y5et3qu?a"!rN$"!WrQ)!rN)S!#>S@$j$D/+,hNh$k!IN#n%4T'+tlf%fHh@$k*LO$k3^G%il2n
'cJ,:*ul.7(`FD;,US+7!!3--"98H*!s/N)nGr(ZpAm_b!W`9%!<<*$#6=f10r[oG7n,p43]K#S1,(=3
.k3&"/1rS11Gq*P4[DP0:Jk"h='K*EC3"TGH%CII;ZR"$#m1/."9eN&!WiE(q#LEqquZm#rrW3$nc/am
!<WK(!"oA6!Y7H/E.<7bIX,sMAmeeE=8l5L<E<1'>$PHICiaoOJqf/CP*_cA]?&O^lgX2fWUjU1%Km%=
!!<N5"U"W'rrMioqZ6Bjo`,C%!s/H(!rr<("`+2Cp&G'orWDrtrW3!"!!2rsrW*3)!X]-P$4m"6!<WE$
!!E<)!s/Q%!V$0h!V69q!!!$"!!`u4!"_MB-QWa*$OI+I%1a$^%h/sE$RH,e$OdIS%hB3`'cA#7*uu:<
(`4,0.3i_K!!!'*"98K-"Tnf,iW/QN$31)-!!!',!!*+#30d6784>g-3&NKH0.e\'-mpAj-n6`!0/5:A
3^,o%9MSD^<*<R>C2nE>F,5C7GQ7^F#6Or-"pOi*rrW3$q>gKqquZm#rrW3$nGiUk!sJT'%g)e7$"U/X
I!g?gFDb_u<rc+s:B45j:FAt9;c[%.Ao2U7IY3H7O-?$1\&HePkO%KeVXB6M#7(P9!!EW7"9SN&!WiB'
pAk$jl2V.l!WW3$!rr<-$9[q\!!<*$rW<'#q>pHn$NU;1!<`W3#<tN["T/6#!s8B#!!3$"qZ66fr;lKi
"T\Z)!!Wo3!"WaO.NB$/$4.%I$k<gZ%1Dq<#R_%M%Ls![&JPHe*?Q@D*?,mq(Cr,A>E/[`"U+u.!s]#4
!Wh<]o)Ta0!!*-$!!3H,"9<ar:eXGJ4utSX0J4n+-RSd;(aULV.4Zu(1H.B\77p6J:Jt8"A86%(EGl>H
JV9<h!!WW0!!3B0!sAE%rrMoqrW2ourr`9&rrMTh!<WK(!#,J7"p0^LFEr:\F`;)(=AMIX7nH>O8Kpc$
:K(D'Ao2U7J;&i=OHuZI_9UfqlK.!&kGA^i%0Zb4"9Su:!s/B$rW2cop]9X[%06J0!!*-$!"C(`!!!&o
!!!*!"8i6#!VHF%!<WB("q1S@'n-,f!!E3#!<N<"!!!'!!r;rg!;uri!#Pb>!!!02!!*(S9J%.q$OI+I
$OdIS%1EUC#l=oP$4@7O%M''^'Gqf3*uu@A)&=)0,9KsS!<<B0"98N/"Te_n!;-?c!W)j6!WrE&!=8`2
!17Cs8Ol'.2`*3@.k)hl,Q&]3+sSB].4d/03Bff#8P;cR<*NdDCiFE9K7S?C!!!90"98K."Tni*!WN6$
!VcZo!W3!!"9&?%!WN2j!!*0)quAhc!iglsG'\=NCLpaJ7mK:(6:=4/6:+(08PN,d?tXA"I"R01NKTp9
]?&O[kiUX(l`Up&&-i7:!so/5quH`tqZ-9inGrCc!<NB&!!iZ,!"!ZL#64f!!!!'!"8i6"!VHF*!X&N(
"Ub;<&Y/n+!!iT*!!33!!!!'!!r;rg!;lli!!<9*!!!E0$31/.S3/GB&do!QrX8o=%1ERLr<N9,+peSa
$k3[W%hTKm*$64B*?5n3)^-%?:n@ml#RLY7!X8c.iW/ZQqZ$Wu"9&9,#QP/2Y#eOk76WOf1bp[6.4-;a
+<MXF*?H7D+X8<_/MT.F5t+:88ki2c?=[bfF*MnYG,5BC#mpk:!X8c/q#U9krW2`prW2Nh!<WN'!"o\C
_K:$CGB.M4@9-#d3&`i[4t&TX4?Pem6UsjL>%),bH@^a)M3"+([DL8Djlb1-l*D32&deaA!XAl"!;-B`
!<3)t!!30(#6"T."98o6_?:DM!WE'"!s8B#"9AT,!Wr6"rrD`m&H`1;!!<N-$PofD!rr]2!!!)t!!!'!
!r;rg!!E<'!WiDp!"f;9!!!$*!!<4u4=V*[$jd7Mr<r`8#m^G5'*\XG#7(SA$OdIS%hB6d(`XS<*>0>2
(`")9(aD&>%KHP>#64c."5s7V!VZQp!sJT'2$X*f!4Q!'5t!gm1,(7.-6s`V*?6":)B0V8*?QIP.PEV=
5!qb/84u`Y>@D/]F*VkQE2EsJ!!Ef<!!*6*!W<#t!VcZo!VZZo!V-3k!sST&3t)G?FE25@DeEQc;+3K!
0/>FG3&``R2`a,h7nlrfA8ZU@JqSo;QD:Xrak#>/gXF<]*t8Vh"onZ-!r`2o!;$<_!<3)t!"/f3#Qau+
"98E(ecP^K!<r])!!!'!!r;ri!"f><!WW</!!<Y'!!3--!WW3%qZ$TsrW;uurrMZj"9AN)!Whro!W`E-
rW#(d!!<5"5pR*X%1*@N%1EXQ#mUV:!sA`1"pP;<#mq(M%M'*_'Gqc1*ZQ.=(`+/:)^m#9'*/(F#QOl.
!pBX\!;cfj!!*0)rW#(c!!r\:=[kPA4#8QC.OHDa*ul4;(`4&+(`=53+<r9c1,h<]6UaL:9iG/#ASZ@3
EcQ/p$j-JC#lju/!rDrt!VcZn!VZZo!WN/l!!*3+quAee%aTB8Ble*$?Wg)f1Fah)0/G@<0JG4<3'9Mu
:KLq=FFA[kKSYe_Wj]mof\PNJXiht("VV+@!!E>p!;$<f!!!&s!<3)u!"8i/#7:P5!<`B&"kEeR!!<6-
"TeQ%!!3'#q>p6h%KQ\;!rrH1!!!(_#Qau2rVus#!W)ls!r2lf!!E<'!WiDq!!30("o\K("on`*&#h];
',:r_$4RCO$OR.D"9&?K!sAc2"pbMB$k3[W&/#]p*$-.@*#f_1)^61I/Z]Tf!"K/4!!ED_!;cfk!!30'
"TAB2"onr0\5YjY6TQtT/1;bs+W_U@(`!i$'GV>u(E+;;,q:Q*3^5nt77^-N=C5TREcuA:Kp`5N!"]A8
!<`K*quH`tq#L?opB(6no)Jdo#5eH;$k(C%BkML&@9cf(4>8*.-RgSs.Ocet,;1i34[Vh>>\A&&I=Hd#
O.</V_TpZ`hVl)`+Vk4o"onW,!qZKb!Vl]q!W2rs!W2p,!<i`1!!!$'!"%?^!!3#u!<r])!!!'!!r;ro
!;lg$!<i]1!!<N+!!J>h"TSc+!!*-%qZ-Wtq#U$d"9AN)!Whro!WiK.rW"ST!!<4s4!YLT%LEIN$OR4I
#6Y).!!**&"9eu7#RUqK%M'*`'c@u5*ZZ4>(`"#"+;uRgV@j"3#m(),"Tneb!;cfk!!30'"TAB8"onr0
Yu*kN6TQtS.OH;[)]9G,'E&Oe',2/t)]p:Q/Mf@L5XIk.9N,)%ASQ1+D.]2q"U+l7"98Q*"U"i,rW)ou
q#L<nq#^Hpo)Jgm"U=l)3t)A6DJ*R%C1(1A76)tH+sJ6W,9e<V-7LQ'3Bou/=_)DoH@1-lNLHcP_9C<V
g"=WZ*>Skj"98H,"8Mro!;-Ba!<*#r!!*0*r;[$1$Ob,^"UY,-!<WE$!!WH+!s/N)!WE-#!VHF&!<i]1
!!3B*!We8d$318/!!*-%qZ-Wtq#UHpo`,*q!<N<'p&G0q!X&]+!"B)3!<AEO+Vbb'$47.JrWrT0"8i-A
!WrQ/#7(YE%1Wm\&f)?)+!)FB)]0;,*ZZgmV%3_0"o\K'"U"ki!;ccn!VcWs!<E9*rW#+d!!`Lt<BiQ4
4#/B:,Te!D().An&.]9_&/#Wl)''kI/29(G5!VJ)9N,,'Anl4&DJPYs!!`K1!WW6*"TnK#q>gEoq?$Np
rW)Wl!WiN1qu@?9#.8G\Ao_Wn<_c"@/0l>Z*?G,!-6=<U.5!J?6VCHgCisuJH[gsAVmO7^c-Fnnb-;d#
"q1S6!XJr1oDnOboDngjqu?cu!<W6#$ipM<"cWWd"9nl,!!2rs!!3'$qZ6`uo`,I&"U>,0!X8W.#E&Zp
!!W?%!<N<!!<3,r!V-6g!VZQs!<N<+"o\K%"TAB$IKWFg()@G[$3^_B#RCS8qu@i?!WrT1#RUqK%hK<d
()e28*uu=?(DR`,+>c-O%0lk6rW!!'"9RQ_quQTnrW*'%!sJT'%gE"9!/FuE4@;1c/12V_)CQ@8&eGQ`
%1NdW&/#Zn)^$FV0JtmS5=.e4;d3^CC2@a+EKl%T#64u-!!<E/!s8E%!!<*"r;cZpqZ?Zro)Jjn!sT#.
!"fDAR<r4NEG8]X90bBd,9@a?rY>SP)&sbD,qC]05Y+g[BleHAG^YF9VR+%XaiW&d`2FCf"ptD3!so/5
g]76Qp&GC%!!<3l$NL/7#5A/u!WE2u!ri;t!;um-!X/f2!!*6'"r)Id'*8:8!!*-%qu?d!!Wr/unc8Rg
pAb<s!WrT0rW!B/!!!=&DAsB*%LNLL$2t22"TeK#(BFR?"pbPE%M'*`'GhZ/+<DL@(`!l(*X<rI98<r\
!!3'!!X&T+i;ifWq>gNrrW3*&"TAB_"TSN3=ar:k5<1GK-6X?G'bV#e$k*LO$k3[X',DK.,:P6%3BTMl
78$Q_?tO.jDfK]^DZBtA#6=f)"9\f.!Wi0"quHctq#UHrq>p6h"T\W+":#50!%Je!Qr[a6Am8,&4uFl:
*>]A#%hK?f(`X\H/i>d];-[aRFEMbQLR"X=]`,k[dalL$',Cf]"98N0"p+i(!!30$!94(X!VZR%!<`B&
!?O#s!!ri1q#CBqrWDuurrMio!s8`4"8r3("trLU%Kcb2!!*-%qu?d!!Wr/ur;cNkquQNl"9JZ."U4c'
#8SVE)&a"o$N:A2#QP#'!$21D"U>AC%M'-a'Gqc1+<DI='bqN(+Xf*RBb(=H"9&<#!TF+Z!<*#p!!!'!
!r`<$!'C>`!#[;V1HdcX0InFl)]'/!%L`^P#mq"I%1a'd)'0tM/Mf@J5!_S0;-7.9CN"35CReH."98`0
!!!*"!Vlf_!VZR#!!!$#!X&Z4#Qai'4<Z_j;IjEL=\hFJ1b9ml'b:ZZ$OmX](`jqQ1HS!#>@qeoFEMk_
PG#%g_o'=;d*H_H&d]'R!X&`3!Wi9#rW1pWrrMus!s&H'!"&c0!!!0(@fQQ6"o\Q"!!30&"8N#u!VcWt
!<WN2"TAB*!WuC8('as?!!*-%qu?d!!Wr/unGrOhpAb?t!WrQ/"oA9(%L\^H+:AMW$46V9!!N)t*WZ?H
#7:kL&.oQj(`XV@*Z5\+'c7u;/2;09'`\4:d/X4K!<W0$rW!W5!!!N>V`$n"1b^C)*ubt.%h/mQ,RF__
#n%.P&JZ0(+t"rt3'0;i77pEX?"IhmF)kZi2@9Ec$3^8,!!3'#r<*$#mK)q[#6=l."U55<!rN$<()snb
BOG.I9gUou/LDJP$jHk?$4RR_)^6^c3Z^X`=_2JjF*)Y[Oe/S^^qmb/`SF6)%1<aT"9\o3!r2lM!"o>8
!<<*#!<<<(RK*ft!<E6(!W2ot!VQTn!W)it!X&Q/#6b#+#6t6s!"fA<"9&9$!Wi3!!W`?(p]9mb!!2cn
"p"f/"9er0qu@!(!0o,_#m^nFr<NE/"Si$:!<WK1$4ICU&ebus*$6:D(_[Gp)B^@^1k$kj!rr<*!R^rK
!<W-#qu@?1!W\l\7kl_P.jQ5V((q,d$46\;+UJMb%h]Tp*?lj_1,h9Y5t+CB<a93QFEDP-Zkj2P!t,>1
!!!'#!rE*"!q-0^!!iT,!sAf5#RCP2!':5f$+!rQ>$4iu5rpkU-QNm."9Sf5$kO-l+Xf'*6V^cpD/jW=
H%_<NW3sCS]#_MB.iAU$'+G*J"U"Z(r;lfrhZ*`Z!sA])!!WN."TYqH)#aL;!WrK)r;Zfuo`G!krW!T5
!sJl3!<E0,!5edA":#,5!!!&s!!30&!q63j!U]ph!<NB&"98K!!!\-I+:\bh$N121"p=Z$*ruHI#7:kM
&/#Wk(E+86)AWnq(*4VF4[s]1%0-D4!SIJL!!**%qZH`r&HMk3O'=h+1Gg[1+WVC5%h/pF#pBWa%M09h
)BL+O/M]7H5!h_4;HI+8DfBQ;Cmt_7!!<N2qZ-Tsr<*$#mfE%\!s&H*"9\o6#RCP2!'LA`!2"@?>$+j"
5s.([-m'04"U##9%M9Hq+t59.6r$lqD/jZAI#!u[Wj][RZGsZ!)\<8_&.AaH"U"o0rW<'"f`2*T!sA]'
!!!$)!Djs?#Qk/1rW2osquQWqqZ6Zr!<E<$"9\`+!"a8O!!33+"TAH!!!30&!q-0X!!**%r<!$#qZ$s*
5'S1a%20-S"U5#3"9SE"+9;NH"U>AC%M06d'G_N')Aj2#%i?K6,Y;<R"TSN(!s-gM!W`?(r<!'%!W)j3
"%A)03AWZL-mToR'G1f`$OR4K$k=?j&eu6'+=/Hh1H.B[6UsjM=^Gc\CM&$KEruCB!<rZ(!!!&o!q66_
!!rZ,!WrQ/"pYA8qZ%`G;kI/q<EW'a4ukAJ+W(^r#RV"Q'Gql:.l9@X:g.CH'Q\JFJ;fqmXgl-RX2DoH
'*\^L%1<(=#6b54!s/N)!U]se!U]pl!<N?*!WiE%!!``7Du^CM#6OZ#quHp%!WrK*q>pNprW3-(#6=o/
!&kVj!!EH.!W`?!!!!'!!q66Y!!!&t!WW8u!!`u=SfSg`((L6H!X&T+qZ%f@!WrQ0#RUtM&.oNg'c%Q$
'b_,h)C?UR;1p\-!!!$$!<C[Nr;lp"rW<3'!Wi/u0FSGo2a',_1b0pu*#92!%L`aT%1a!_'c.f1+snfn
1cRT_6qC*T>@;2cARL"_3s>N_!<WE$!<3)t!r`8j!V?@!!<E6'!sAc2"pP2,!&Y?*^JA$6>#7XQ4>\T6
)\W\j%M9Em*$H[^2Es`1>@h\oH@LX3T;]!*^TaQIem9'l"pPA>rW`W3"U"o/!<Mfmq>gKqmJm7g!r`9&
!Wi6""sh#&#65&3o`,0s!<N<)!Wr6"qu@$(!<<<3!!Wn3$iL&-!sA]-qZ-WsrW;QimK!4e!!<-#qZ%',
%$i%](`<ee"9\f.!W2p-!<N?+"U55>$k<g\&ebrX'FPQe%hBX/,:?c`!sef*rW1[PrrDuuq?$Ztq>`/[
UcCe)5;t2D,p+!?'+bZa%hK?e'c.c/+XJQh0JtjR5t+CD=^>KOE+3()XUGC3!<3)u!9XCU!<*#u!WiH+
"9Sc1"9SH#2$+Z$9j:Y%;+O&<2_QO#(_[Mr()e29,UtN/6;(9`B5`!BKSu1lXL#OPXIm#P-Plac!sSu.
#6Y25!s/Mi!;ure!!WH*!WrN+!W<!&$?HFR!"&f"!<3)u!rE#r!!iT*!!Wl4$Qmdo!!<9)!s8?"!!3$"
n,_tXquQNl#6RAN(CM2q"TAH(!s/Q'!<E6(rWEQ3"U>AC%M'*_&JG'V&J5N_%NHrK.>1n/!!!$$!s8VV
!<*#q!r`5s!#5`8Shhrc4>895,9@a>'+kfh',;<#(`OJ<,Ub2s1,V'U6qL-Q>$bZQD.HY@C^^.@rrN&u
quHctmK)t\rW3!"r<!-)"9S`%!$D\SX[kib<D#\F3]&B6*Z5e4*$6@N-nR8=78?okBQ/8;K8YqaVm!J=
\Z:tCN$/T0!WiN0#6tM>"p>#0!UKgb!Up*g!<`H*!s8W&!!EG3!=K53!!36(!Vufh!W2p$!<N?*#Qb*(
4TGT`!!<6'!Wi3!rrN$!o`>!mnc8Ofq>^Krr;[95"0F'W*t\VU!!3<-"TAK'"T&?D#71bJ%hB3_&ebrm
%h&gT)_!^$R2->6!!*3,"TneX!<3)r!r`5r!%nWg^I9J=4>SQ<-6sZP()%>r(E",2*Zu[T.k`V62EF)n
9i>"q?=IS^Bi_J_'`A%2!VHEm!;urn!r`5o!<*$!!r2p!!Wi,t1(G#A<B48_9L_<23AN*1+!)OK,pt,n
0fVHj;HdODEd`b,S"m$h[C<HCOPE&I!<<*$rWWT4#R:P;!s/Mo!;cco!V-6h!WE-%!s/N&!!NE(f)PdU
r;Zp#"pG,'!<*!!!;cfq!"&c2!!!K9S,`ir!rW/t!<*#r!qlZm!WW9"!;HQk!Vud0!<N6$!<iZ4:43Wj
"UP51!XK&9rWNB."pYA3"U##9$OmUF%i,`j'bq5d$kX=$7V>p-"p+f*":,26!SIJP!<<3!!r`5r!&"?X
%pkJQ5;G5R-n-Vl*uPh0(`FD9+<i'Y.P<J52E*]a8l8\n>%)#P??(U6$jce3rrVclr;lQmp&P*nrrW*#
rW<*#rrDor0*`/&TKZ7E;G'5?5WLPK,pale/1iM12EaK(='fEQF+B7<UT(B'\Zhm5\!&*R"o\N$"pYA=
#6k>6!WhWf!!<*"nc8Of"p+i.!!!'(rVut,!;lg!!t,D<oDnjk('"=8!<N<&!!Nc2!!I4B!!39)!!!$#
quH`tq?$BlqZ?cup&P*nrW<*#q>_63!rr<)%KHYCW#?]W&Hi(9$OR.E#:9Z\#RCY>"pG5<$OmRU%hB6c
()IMh%i-$-=Gddm!"9&3"UYJ:!SIJQ!W)ru!VZR5#lkAS]f/;+68U,B0.J.d)&XA7+<i$V-Rp]&'Jq^,
3BT]'<Ei[2@VB+OI%MMa!!rQ(rrV`krrM`np&G-p!<W0$rrW0#q#D`F!"C*j6W6*M9gM*75;t;J/1iM1
1Gq*Q6:t-Z@:sJ$K92\'X/lW8\uM7-bsE?S$N:&)"pP;<#6k;5!p]jd!r`5k!;Z^"!WrE&#7pe6"2Y$<
!WE'$":Y_BoDnmlrW!K1!X&Z,!!a,:"VJi\&c`.:!rr<&!W2ot!Vlfl!Vult!VQKn!W<'"!Vl^5!<W?&
"UY;6!(;bU*t&2T#7(VC#mgkC#7(56*si8]$OdIS&/#Wk()IVq&K;`XI7OD>!"&o3"UPD9!W2rS!<3)t
!ri;p!&+WZ$3O>*01RrU0.ne),p=<M*ZlOM,pt,m/hf(=3'9Gq9iG.s>$Y]EEh$5=!!!6&!!*-%nc/^l
!<Voqp&GF#!WiH+"9S`-!<Mop0EM4]"^J5o>"qLV6pX%!2`*<H1c@<S4[DS5<Es$KEdEG$R\QaYWj&.u
c%%2U"U=r+rWNK1#6k>7!WhWf!WW9'rW2Bd'`e=:!s&B)#R:J4!1O&j!WW3%#R:M&!!!'!!XSr1!!!'4
!#.3rrW!*,!rr<&!W2rt!W)rm!Vult!Vl`q!<3)u!WW8r!"f85!<WK-!WWCU;A(8^%LE@GrX/]4rWa2E
$4I@Q$k!CN%MBKl()If))&OMP@#t9e#Qb27"9o)8!s.'TrrN$!!<E2o!&+HW#6bg/DDOs?1bC.)-mg/^
+<VgP-7LJt0/,+<3Boo'9i4nm>?bNKLoCX_!!*/g!<3)l!qlU#!<N<)!sA]-!Whup0E;(V"rEqY6XN8R
6U![u5!1kd3BKAh6qC$M=C,QUG(5:-Q(+A=TVJ9oe1)FK#6Ol)#m1;5"U5,5!s/Mh!<3-"!UKdg!<E6&
qZ$g%C+92g!!!-%!s/N)qZ$TsrW<*#rW!*&!s8T+!WE'$$P,5;rW!!#"9\W(qZ-*dq#^QspAk3or;ls"
pAc$2!X/c.!#5taT0!#j#6thN#n%.K#6kD>+Uenp&Io0U$P*sj(DIf5+sA3\0TnU#!!!'+#R1J:"9JVW
!<3)u!ri;p!"o>9!!"#X0==h&3[cC2/gi"p-2o(i,q(;B0*Esd3^ZLI8Ou]_>$>0;>I%-7rVus%"7?-h
!V?En!VZR#!<E6'!s8Z.!Whil-lj<c^LT#m4?Z/%5X@_%5!D4u7S?NU='K'FE-m:nLQS'pR@0D%h0'>W
&I8LA!<<*#!WrQ/"Tnf,l2^hcrW23_rW2uu":"tY"pt8/":,&/!!<*!"p"c."U"l-rW!*("T\T+$N:#.
!<ASk"TAB'"pG)0rW)fqncAOfrrMiorrN'"!!2cn3!'3d!Wi?7!*#<k'H.N&'+,'U$3pb?$4[[`'+YKX
$P+!m(D@oC/hK@LNGeh%!!!'-$3p_:!WhupirK)[r;ls"p&H]G!sJc2!#l/SX<9,R/NGO7.P*"p,U=`e
0/>:;0JPIJ7SZNE;I<d:De#u+&.SU=!X8f0n,WIhrrW0%rrW-#rW2`nrrN-$r<!'%!V6:E!rs>MD7D5`
83p$C6Uj[=77B[;9i>%r?!h,XFF]7'K8uCfPG45nW\#G&"Tno1r;[!%!sJf0!U0Ua!r`5a!!30("o\KL
!XSk"":P87%Kc\2!s&B%!<N?+"U"o/!<<*&"onW-&I/:E#/:ufr;Zp("p4o)!<3)k!;urr!r`<%!VcZo
!W<'"!VHEn!X&E%-NX8QBoatX.2*7'%h8pO"9Si9%h]E_#mUbF%MBX$,q:;o6][68(B+:=":#,6!s/K(
fDtpPr<!!"rrDfo/-?"V!!!<*&pL!;,XO.:0etO=/1Dts/i#=C2)I0N5!qh8;,p[q;eE//*$G4\!WiK+
mf<@grrW0%quZftpAk3orrW-$!<N;o!<)sL#lkclXAh&X7nHHR<E)gk:Jk.s?XdS[Cik&VLlIIWNeW.J
e&F=)%g`CA!rN$%!<WH-!WhNcrrW0#k5Ynl"98E)#QOuI8e_F/!t>G7!W<#t!WE'3!<E6&!<WE*!!!0&
!%25n%KHS0!!39*!W<#s!V?Bj!W<)u"9/Ds!<*#t!WW8o!!**%rW!Q7!!!Im<&6NX&Jl&i$O?k9":,nS
%LiaM"pYG=#TG<D-9Oh)RfETl(CL9G"9\K$g&V-Rr<!!"p&Gp2"98E&#QP&CSmk,a4>8fV3&WTI/MAn=
rAk*D5!hM#;@[&8:LIgYXpP[>(^g<D!Vucr!VQKp!<E9""8r<"!VZTo!WN6"!s&H(nGjsC!!sUBDcL=I
9j:n1?X?r>>@1oSCN"9<IY<E0Pb!qhNfTRN+X-q3!>5P2!!E?+!s/Mf!<3-"!TsFo!<N<*#n6q=%p/l;
#RLhF"TAB&!<WB#!!WH+"9\c+!r`0-!X(3d&c_n?"98E&qu?`u!ri?%!VHHl!W3#t"9/Dt!;urs!ri;o
!!E<&!!*0#!!Wh#J.<;7#Q>)H#mLM:$4RLR#RCbF$j[1U-R:<.CR>P0!!Wl="9S`-!W<#t!VcZU!<*#u
!r`5q!!WH+"9JQ*"9&9C%\o",/j([B3]oJa2`a)f6U<q'7S$0A85EAa;Hn^M(&e19$jQh7!Vufr!VZQq
!<N?#"9/H&!rW/p!<*$!!rW3&!W`>m!!!'!!%&G`SM`oA:L7XIC1q3nD/jZ?G^bC+OcPTgR"p<IUVS>b
#m_.O"8Mp"!WrN+!U0Ua!r`3#!U0S$!<N?+"9o)2!WWsQ=qV,E'F=a>!X/f3!W<!2!s],="9So>#QP&P
O9Q3q!"&r+!!NB)!s8T*o`4slr;um!rrMoqrW3!"rrW3$oDgTI!s&B,%0-A=>_OXI,8:=f%1<FK%1a!Y
#n.=U&.TBj0Ju.<Jfk3s%0ut9"U"o/!W<!#!<N9&g]7<SrW;osrr=kU!!*-("U,#0!!N]0!"rk-5WVD!
2EO5k5XIn18Ol3@:/=Y[:eb;%@#C'o"oo#8!!!'%q#LBpp](?r!Wr9%r;uoup]19orrW-$!WiB'nGiOl
-jfqU*-A,_=_h\\C3"?6F*;eTI"$g1PEqN&OdqPnY,sc!!>,Y?!<Mur"T\]-!W`>e!<3-!!U9Xh!<WH.
"9S`(!!iT5!3Q;2$NL/1!!NW8#6Ol)'`eLG$k*FK!!aPFKg,PG!#5kD!WrN%!!**%rW<3'!WhuprW2s!
qucs"q>gHpquZiuoDf@%!!!$%#7^_P40E0/!Y#&7#7CnH$k3a]%i,Tj+t+Q\&o4%I('"=9!sAW+!s8T+
!WE'%!<E6&!Sd\S!WE/s!W<!%!<N?+"9\T&*s2lN+@j4r0d\e:3''2e5X@e.8k)3D='SU"3/P"`+8l0A
!<<*#q#L?op](?r!Wr9%r;uoup]1<prW<$#!WiE(mf4U;&-sjjesTB-?!h#OBPD3tDg$MTI#4,XOGn"a
g6"<%#R1D7qZ-No"T\]-!W`>e!<3-!!U9Xh!<WH."U"o(!"/i8\gIX]!!a&C!s/?#"9AQ,%heg@$m;u6
%0-tH#mLP9!s/<"#6=l."9S`-!VQNm!W<)t"9&>u!;urr!r`5g!%J*W"s+CsUIYIk)]04u$4.(U*ubq-
'/276NK#b%!!N`4!!!'%!<N<'!WE'%!<E6&!V?BV!<*#t!rE#s!!NB)!s8T*qZ%]C#ppaH\mls65s[[r
3&s)j:.[`74&o<nVP-Bm"U583!!!&o!;urn!!30&!rN0!!r`3#!VcZp!WE0!"9/H&!Ug"6"qMG+0ppF>
6:kWq?sQu@?Yjn,DJX-ELm??,@kJW6'*eL;!quZu!<WE*!<MHcrrW-"r;c6c#6=o0"U,#3!r`0-!t#M<
!->OJ!"B;?r;[T8!WW6&"9\c+#EH%h'`\C=!rrH0"p=c'#QXu.!sA].!WhuprW2s!qucp!qZ-QqqZ?cu
mf3Fk":582!#I>[T4&EH+<i$R*uZ"<-ndhPMmRR+%1`78!<E8s!WN6$!Sd\S!W<)n!WN6$!rDs!!=/o/
!#Io)[<jS_6V'jC8jkp38PNDlT>Z9\'bg':r;lZn!W`?(qucm!r;lZnrrN*#r<*'$rrMTh!s8c>&L%Vh
&5pHiP"82M@:a%^@:!GZE.<>TkFiVC.0p:f"TSN(!VcWu!<WE*!<MHcrrW-"l2V%j!sJl4"9S`)!"Au6
$NLP;!1/cl"p#5A(^1-P$47:Y!!3@9dNA\o!WW?'!s&T4#6Xl(#QXu/!sA].!WhuprW2s!qucp!qZ-Qq
qZ?cun,O@.!Wr]:#mUe;!AnqrHpTJ4+!)OR4&g`uN&Ck?!#>P7&Hhq2pAt9qrrLmTrW2s!p&Y-orrMus
*X3#\$P<[S6AE+;?;=$Z6UXLJCm:lb4TPO#!!!W6r;Ziu!Vl`n!VcWr!<N?#"8r<"!VcZp!WE0!"9/H&
!V-4=!<WH0%M]]o*>TPiQ-6%D?s?]7=^Q*$Xhq>E)@eD3&L%ee!!36)!VcWu!WrK*!<MHcrrW-"l2V%j
"9eu5"9JW'!WrH+#6Ol)"Te[gi.r$D!#,J;)J6\A!rr<,!!!<-!!!0.#mUS1!!iT,!sA`/!s/N$!;ccq
!W<)t"9&>u!;urq!ri;j!!NB)":,>8r;[B9#7`b,J<,kUQ^<VP6P]Y2rW!$$#S."7!;HTo!ri;i!:Bjd
!W<)m!<N<(!W)j!!<ri4rW!N5'c%ofJXs!P[CEW@M,PT!&H2Y3!=')8qu?]tq#L<np](?r!Wr9%r;uou
p]1<prW<$#rrW3$nGj^6"UGSN$jd1D%j</L?')2(`lH9E\XmIo(aft)'+u-&%fQG0!<WAt!<!!!!U9[b
!rW/t!:Tt7!<NB-"pG,3!<N<'!!N]7"TSN0!!*35-!chE_RQ+P3=Gm*!!3#u#RLS5!!<H5#6Xl(#Qb)1
"9\f/!WhuprW2s!qucp!qZ-QqqZ6g"!<DTh!s/W3#lO`'!qH<s"TSN)":YnO!rN&n!WE0#!Sd\S!W<)m
!WN3$!W)j<!X/f0!!!00#m:55%LE:M)]05%&Hr.B!!*-'$kEdD!!!&q!;llm!!30&!rN0!!rW/p!<3*!
!rW6$!ri;k!!NB,#n7CP'EnaQ'bq8g'ce/-+Y5,j-RK`@+V4Pf"!/O&%K-8-!s//sr<!!"l2^hcr;l3a
)?BmB"U5,5!s/K(!!!66$j[1J#6b>C%13:A!<`N(!!Nc9!!!K0rW!6-#Qk&,!XB&<"8i-#!WrQ("9JZ,
!VQNm!W<)t"+U~>

%%EndBinary
grestore
np
grestore
gsave
0 570 mo
756.961 570 li
756.961 .893066 li
0 .893066 li
cp
clp
%ADOBeginSubsetFont: FBAAAA+TimesNewRomanPSMT AddGlyphs
ct_T42Dict begin
systemdict /gcheck known {currentglobal RVGGZC+TimesNewRomanPSMT gcheck setglobal} if
3 6138 83 <0002fff9fe4a03ba03af002700390253b0852b58b1020243545840293b40
13130255320a2a131302550a060f0f02550a1813190020032913080d0d02
551320161313025520b8fffab40d0d025520b8fffcb40f0f025520b8fff4
400d101002552003282b12040e061aba03e2001703e2400b1819182e250e
3659060727b803e24009004009100255000107003fdd2bed3fed2fed2f2f
10eded11121739012f2b2b2b2bdd2bc0c010c6c410c42f2b2bcd31302b1b
b10602435458b90032fffcb50d0d0655320ab8fff040180d0d06550a0a3b
3a0329130c0d0d06551302101006551320b8fff6b40d0d065520b8ffee40
1b1010065520203b3a0328060e270001190e2e250e0b365906070107003f
3fed3fed3f10ddcd11123939011112392f2b2bdd2b2bd0c01112392f2bcd
2b31301b407e0a3b430d5d36391049105b10891104862c013b2c3f3b4b2c
5b2c6a116a2c73087911792c8408a507e908f9090d303b583359346c3404
403b012f08032829121320291e19862213291e1827230027214f271e0044
02122b2803042e1036013659060702072e250e0b19180e32311f0a900a02
600a800aaf0a030aeb200213b80167401b20205021702102802101002110
21b021c021d0210521603ac24b182b10f65d71723c10fd3c10fd5d72ed00
3f3c3fed3f3fed7211173910f5edfc01f52b2b030e103c3c3c3c31304379
40202f35070d082534260c26302535073220012f0d322001330936200131
0b2e2000002b2b012b2b2b2b2b2b81810171725d00715d2b59591bb30107
0636b80817b46c06070e2eb807e7b56c0e0b17191ab803e2b26c190e0018
3f2b323f2b3f2b3f30315903253315363633321716151407062322272627
111416163315213533163736363511342626232207051114171616333237
36353427262322070602011a26478f4f8a5c718870aa4a36283217394bfe
20193727131510231e18250134090e6d53643e515c4058302f24033972d6
79616c84d4ed9b7f150f2dfee95e331e252501160b316403625930180e7f
feaa6f233a584e66b9d2714e1812>RVGGZC+TimesNewRomanPSMT AddT42Char 
RVGGZC+TimesNewRomanPSMT /CharStrings get begin
/g83 83 def
end
RVGGZC+TimesNewRomanPSMT /Encoding get
dup 112 /g83 put
pop
systemdict /gcheck known {setglobal} if
end
%ADOEndSubsetFont
/RVGGZC+TimesNewRomanPSMT*1 
[32{/.notdef}rp /g3 12{/.notdef}rp /g16 /g17 2{/.notdef}rp /g20 /g21 
14{/.notdef}rp /g36 6{/.notdef}rp /g43 2{/.notdef}rp /g46 /g47 /g48 
/g49 /.notdef /g51 /g52 /g53 /g54 2{/.notdef}rp /g57 
10{/.notdef}rp /g68 2{/.notdef}rp /g71 /g72 /g73 /g74 /g75 
/g76 2{/.notdef}rp /g79 /g80 /g81 /g82 /g83 /.notdef 
/g85 /.notdef /g87 /g88 /g89 /g90 /g91 /g92 
134{/.notdef}rp]
RVGGZC+TimesNewRomanPSMT nf
RVGGZC+TimesNewRomanPSMT*1 [24.025 0 0 -24.025 0 0 ]msf
99.27 389.607 mo
(...)sh
RVGGZC+TimesNewRomanPSMT*1 [12.025 0 0 -12.025 0 0 ]msf
152.261 556.557 mo
(P)sh
159.019 556.557 mo
(aper)
[5.2731 6.0125 5.291 0 ]xsh
1.5 lw
2 lc
161.641 478.557 mo
160.991 453.047 li
83.3203 453.047 li
83.3203 428.667 li
@
79.3004 428.727 mo
83.3203 424.707 li
87.3406 428.727 li
79.3004 428.727 li
cp
ef
161.641 478.557 mo
160.991 453.047 li
231.851 453.047 li
231.121 422.837 li
@
227.101 422.987 mo
231.021 418.867 li
235.141 422.787 li
227.101 422.987 li
cp
ef
%ADOBeginSubsetFont: FBAAAA+TimesNewRomanPSMT AddGlyphs
ct_T42Dict begin
systemdict /gcheck known {currentglobal RVGGZC+TimesNewRomanPSMT gcheck setglobal} if
2 2134 38 <0001004affe1050f056b0024013bb0852b584042091e2f012f022f032f1f
960f991ea30fa312b60fb7120b081e011617017d037b1578168d038a169d
03961aac03bb03090c030e04021d48035903052f081011241b00b80105b5
021b0101ba00b8034bb6209a05281c0301b802dfb5112bb0100110b80341
b58f0d9f0d020db8032f402f140902ac000101013210acaf11011f113f11
02111a40260126093c2018010f181f1802180c0d0d02551849256463182b
4e10f42b5d724ded4e105df672714dedf471ed003ffd71f45df4e63fedec
f4ed0110edf4ed10c9313043794020151b060c07251a260b261625061b09
2d000c15092d000819052d010a170d2d00002b2b012b2b2b2b2b2b818101
715d0072715d1b400e20201c10101c0202141c24031c05b807ebb46c1c03
140db807f5b26c140900183f2b3f2b3f1112392f11392f11392f30315901
132326262322060215141216333236371706042320272635341224333217
16333237363704d11f1f3ee6a187da7d76ed9884ca791f66fef0bbfeafb9
8ab6013fbd938f2a121b141a0b056bfe33cfb689fed4dfb8fef29071a814
b5a8fabafccb0154bb4816131b30>RVGGZC+TimesNewRomanPSMT AddT42Char 
2 3078 42 <00010048ffe105aa056b003401a3b0852b5840540a04462e0219271a2802
1018101902203640366036780870187019782a90189019b018b0190b2d2f
760b870b0318362e1a503670368c04ad04e036040c03860bc0360348081e
1f1b18f322121f1b172123341b00b80105b3021b0101ba01b30000034b40
43319a2c1718182206282c030e282209012b1f1e0c131302551e0c0f0f02
551e060d0d02551e22111150129012020f124f1202001210127f12ff1204
1204101002551212b8ffe4b40d0d025512b802f8400b0a3c5026010f261f
260226b8fff040100f0f025526100d0d0255264935648a182b4e10f42b2b
5d724dfdf62b2f2b5d71723c10fd2b2b2b3ce4003fed3fed12392f3c10ec
f4ed0110edf4ed2b2b313043794034202b07100825282729272a2703060c
2624250f21113b01201f1011072b0a2d000d230a2d0010200e3b00092706
2d010b250e2d002b2b2b012b2b103c103c2b2b2b2a2b818101715d2b005d
015d01720072711b400a31312c0202222c16171ab803e240096c1717222c
34032c06b807ecb46c2c03220eb807eab26c220900183f2b3f2b3f111239
2f2b321112392f11392f3031590113232627262320070615141216333236
371134262623352115232207061511060623202726353437363736333216
17163332363704e92323355479befefd877196f3804b8c411f4152020d19
4e1d1473e089fe77cc995666b295cb4a796f3813131b03056bfe54a05175
cdadefc2fec09526250188663f21262634256dfe613e3afcbdf7b3a4c369
571829152333>RVGGZC+TimesNewRomanPSMT AddT42Char 
2 9428 55 <0001003e000004b0054c001f011eb0852b58403a5a015a025a1d5a1e6b01
6b026b1d6b1e082f213f214f219805971ba805a61b0702011d1e161f1b10
2122091f1b0f2123071823001f02100f0821b802c0401309012b0040170e
3f120f001f005000af000400b80228401a08090613130255090c0f0f0255
090c0d0d0255092217161f2b1eb8ffc0400e170e3f12001e101e5f1ea01e
041eba02280016ffec400b10100255161a0d0d025516b802c0b320645d18
2b10f62b2bf45d4358b9001effc0b20b351eb8ffc0b20b0f342b2b592be4
103cfd2b2b2b3cf45d4358400900400b3500400b0f342b2b592be410e600
3f3c3f3cfd3c2b2b0110c910c93130015d005d1bb6021e1e10081f18b807
f4b56c1f020d1011b803e2b26c100800183f2b323f2b3212392f33303159
011323262726262323111417163333152135333237363511232207060607
231304a10f260b131f6754bf1b264f2ffdc130562416a35f28344a072610
054cfec254243a37fbf47d1f2a2525342072040c0e136c5c013e>RVGGZC+TimesNewRomanPSMT AddT42Char 
3 7498 86 <00010064ffe402d503af0031046ab0852b58b10202435458402733401313
025533400b0b02550201181010025501180f0f0255010f1b1a08270c0b0b
025527210fb8ffe0b4101002550fb8fff440320f0f02550f310708270f21
04122b05017905016c050105252f0101012a0719771e01631e011e25201a
01601a701a021a120b003fc45d5ded5d5d2f3fc45ded5d5d5d1217393f01
2f2b2bcd2f2bcdd4cd10d42b2bcd31302b2b1bb106024354584032210f27
08042a161e122e05022a3107601a701a021a19124b05016b057b05020525
2a07441e01641e741e021e25120b01210fb8fff2401a0d0d06550f0f3332
1a080e0d0d06550827120d0d0655272733321112392f2bcd2bc41112392f
2bcdc4003fed5d5d3fed5d5d10c4c45d3f10c4123911123912173931301b
4029092c192c0212122e400b392c280b391814590c5a269b109424050a07
0a280a29603370338033060f33b8012040870d5d36cb0dcb0ec424c425d7
23d624d92ce604e623e624e92c0b123f2c5d2c6e2d7d2c8f018f028f0380
15801a801b801c892d8f2e0d0f010f020a03090c061c0a2cc822c923081c
031614121c161d19291b2c9909990a9b20932393240b122b0d282c4a2c4f
335f337829782c860ea823af33e803e61c0c2908311e00bd021e011f012f
010201b8012bb200bd2eb8011a40112a181e19bd1b1e1a1f1a01101a201a
021ab8012bb219bd16b8011a4022121224230d0b040f2724230d0b04051e
01c7002e2f2a31000005252a071a7e191918b803464014162f1e25120b02
cc12010112cf21df21ef210321b80314400b700f01600f700f900f030fb8
01364019271a192e1f0801082c9f270160277027802703202730270227ba
012000320120b14b182b4e10f45d71724ded72f43c10fd5d71fd5d4358b2
ff21015d59392f435c58b2ff01015d59ed003fede4f43c10ed3fed3c103c
10e410ed1112173901111217394358400a242323240d0b140d0d0b870e2e
2b0e7d10c459180010ecf4ed5d720110edf4ed0010ecf4ed5d0110edf4ed
b10602435458b42e20090d34002b5931304379401c28291f20101106071f
11211c010629081c0020101e1c000728051c01002b2b012b2b8181818101
5d43584009fb07f610f611fb28045d5901720071005d435840199f019f02
9f039f0b9a0d9015901a901b901c992297239f2d0c5d595d2b017100722b
2b4358400b2f232f248b2c9b249b2c055d59435c58401128201939092819
3901400a3902400a391bb8ffc0b20a391ab8ffc040190a392e400a392c40
0a392c4009390c101e123f0e201e123f0eb8fff0b21b390eb8fff0b21939
24b8ffe8b2133923b8ffe8b213390cb8ffe8b613392c1813391bb8ffc0b2
12391ab8ffc0400f123901401239024012392c20123924b8fff0400f0f39
2c180f3903100d392e400d3923b8fff040120d390c100d392c200d392c18
11392c181139002b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b
2b2b2b2b2b2b012b2b59005d59591b400d02022e1a1a162e3107190a2a05
b807e6b46c2a07121eb807e6b26c120b00183f2b3f2b3f3f1112392f1139
2f3031590111232626232206151417161717161514062322272623220723
11331616333236353426242726353436333217163332363702902126775c
4656201f5f92cbbd75546c2115170d21211c9e62455761fede2d2d9b7b36
4d331110120c03affec8936a4a2d3828292e4763a27d991e0a1a01478c8e
5139455e903a39577198170f0e18>RVGGZC+TimesNewRomanPSMT AddT42Char 
RVGGZC+TimesNewRomanPSMT /CharStrings get begin
/g38 38 def
/g42 42 def
/g55 55 def
/g86 86 def
end
RVGGZC+TimesNewRomanPSMT /Encoding get
dup 67 /g38 put
dup 71 /g42 put
dup 84 /g55 put
dup 115 /g86 put
pop
systemdict /gcheck known {setglobal} if
end
%ADOEndSubsetFont
/RVGGZC+TimesNewRomanPSMT*1 
[32{/.notdef}rp /g3 12{/.notdef}rp /g16 /g17 2{/.notdef}rp /g20 /g21 
14{/.notdef}rp /g36 /.notdef /g38 3{/.notdef}rp /g42 /g43 2{/.notdef}rp 
/g46 /g47 /g48 /g49 /.notdef /g51 /g52 /g53 
/g54 /g55 /.notdef /g57 10{/.notdef}rp /g68 2{/.notdef}rp /g71 
/g72 /g73 /g74 /g75 /g76 2{/.notdef}rp /g79 /g80 
/g81 /g82 /g83 /.notdef /g85 /g86 /g87 /g88 
/g89 /g90 /g91 /g92 134{/.notdef}rp]
RVGGZC+TimesNewRomanPSMT nf
RVGGZC+TimesNewRomanPSMT*1 [12.025 0 0 -12.025 0 0 ]msf
59.711 424.657 mo
(Reviewers)
[8.26136 5.279 6.0125 3.04225 5.279 9.01875 5.27901 3.77563 0 ]xsh
214.191 319.087 mo
(C)sh
222.427 319.087 mo
(hatGPT)
[6.0125 5.2429 2.99425 8.98265 6.73399 0 ]xsh
83.3203 356.677 mo
83.3203 329.457 li
@
79.3004 329.507 mo
83.3203 325.487 li
87.3406 329.507 li
79.3004 329.507 li
cp
ef
RVGGZC+TimesNewRomanPSMT*1 [12.025 0 0 -12.025 0 0 ]msf
48.541 319.087 mo
(Review reports)
[8.26136 5.279 6.0125 3.04225 5.279 9.01875 3.00626 3.78773 5.2731 6.0125 6.0125 4.53913 
3.03026 0 ]xsh
18.7266 300.177 mo
18.7266 299.207 li
34.5254 299.207 li
34.5254 300.177 li
18.7266 300.177 li
cp
18.7266 296.297 mo
18.7266 295.327 li
34.5254 295.327 li
34.5254 296.297 li
18.7266 296.297 li
cp
18.7266 292.407 mo
18.7266 291.437 li
34.5254 291.437 li
34.5254 292.407 li
18.7266 292.407 li
cp
18.7266 288.517 mo
18.7266 287.547 li
34.5254 287.547 li
34.5254 288.517 li
18.7266 288.517 li
cp
18.7266 284.627 mo
18.7266 283.657 li
28.6395 283.657 li
28.6395 284.627 li
18.7266 284.627 li
cp
37.4875 305.037 mo
37.4875 283.657 li
31.5625 283.657 li
31.5625 277.827 li
15.7645 277.827 li
15.7645 305.037 li
37.4875 305.037 li
cp
37.2406 282.687 mo
32.5504 278.067 li
32.5504 282.687 li
37.2406 282.687 li
cp
33.2906 275.887 mo
39.4625 281.957 li
39.4625 306.987 li
13.7895 306.987 li
13.7895 275.887 li
33.2906 275.887 li
.66 .302 0 0 cmyk
ef
.75 lw
0 lc
18.7266 300.177 mo
18.7266 299.207 li
34.5254 299.207 li
34.5254 300.177 li
18.7266 300.177 li
cp
18.7266 296.297 mo
18.7266 295.327 li
34.5254 295.327 li
34.5254 296.297 li
18.7266 296.297 li
cp
18.7266 292.407 mo
18.7266 291.437 li
34.5254 291.437 li
34.5254 292.407 li
18.7266 292.407 li
cp
18.7266 288.517 mo
18.7266 287.547 li
34.5254 287.547 li
34.5254 288.517 li
18.7266 288.517 li
cp
18.7266 284.627 mo
18.7266 283.657 li
28.6395 283.657 li
28.6395 284.627 li
18.7266 284.627 li
cp
37.4875 305.037 mo
37.4875 283.657 li
31.5625 283.657 li
31.5625 277.827 li
15.7645 277.827 li
15.7645 305.037 li
37.4875 305.037 li
cp
37.2406 282.687 mo
32.5504 278.067 li
32.5504 282.687 li
37.2406 282.687 li
cp
33.2906 275.887 mo
39.4625 281.957 li
39.4625 306.987 li
13.7895 306.987 li
13.7895 275.887 li
33.2906 275.887 li
cp
@
65.6605 300.177 mo
65.6605 299.207 li
81.4605 299.207 li
81.4605 300.177 li
65.6605 300.177 li
cp
65.6605 296.297 mo
65.6605 295.327 li
81.4605 295.327 li
81.4605 296.297 li
65.6605 296.297 li
cp
65.6605 292.407 mo
65.6605 291.437 li
81.4605 291.437 li
81.4605 292.407 li
65.6605 292.407 li
cp
65.6605 288.517 mo
65.6605 287.547 li
81.4605 287.547 li
81.4605 288.517 li
65.6605 288.517 li
cp
65.6605 284.627 mo
65.6605 283.657 li
75.5703 283.657 li
75.5703 284.627 li
65.6605 284.627 li
cp
84.4203 305.037 mo
84.4203 283.657 li
78.4906 283.657 li
78.4906 277.827 li
62.7004 277.827 li
62.7004 305.037 li
84.4203 305.037 li
cp
84.1703 282.687 mo
79.4805 278.067 li
79.4805 282.687 li
84.1703 282.687 li
cp
80.2203 275.887 mo
86.3906 281.957 li
86.3906 306.987 li
60.7203 306.987 li
60.7203 275.887 li
80.2203 275.887 li
ef
65.6605 300.177 mo
65.6605 299.207 li
81.4605 299.207 li
81.4605 300.177 li
65.6605 300.177 li
cp
65.6605 296.297 mo
65.6605 295.327 li
81.4605 295.327 li
81.4605 296.297 li
65.6605 296.297 li
cp
65.6605 292.407 mo
65.6605 291.437 li
81.4605 291.437 li
81.4605 292.407 li
65.6605 292.407 li
cp
65.6605 288.517 mo
65.6605 287.547 li
81.4605 287.547 li
81.4605 288.517 li
65.6605 288.517 li
cp
65.6605 284.627 mo
65.6605 283.657 li
75.5703 283.657 li
75.5703 284.627 li
65.6605 284.627 li
cp
84.4203 305.037 mo
84.4203 283.657 li
78.4906 283.657 li
78.4906 277.827 li
62.7004 277.827 li
62.7004 305.037 li
84.4203 305.037 li
cp
84.1703 282.687 mo
79.4805 278.067 li
79.4805 282.687 li
84.1703 282.687 li
cp
80.2203 275.887 mo
86.3906 281.957 li
86.3906 306.987 li
60.7203 306.987 li
60.7203 275.887 li
80.2203 275.887 li
cp
@
133.451 300.177 mo
133.451 299.207 li
149.251 299.207 li
149.251 300.177 li
133.451 300.177 li
cp
133.451 296.297 mo
133.451 295.327 li
149.251 295.327 li
149.251 296.297 li
133.451 296.297 li
cp
133.451 292.407 mo
133.451 291.437 li
149.251 291.437 li
149.251 292.407 li
133.451 292.407 li
cp
133.451 288.517 mo
133.451 287.547 li
149.251 287.547 li
149.251 288.517 li
133.451 288.517 li
cp
133.451 284.627 mo
133.451 283.657 li
143.361 283.657 li
143.361 284.627 li
133.451 284.627 li
cp
152.211 305.037 mo
152.211 283.657 li
146.291 283.657 li
146.291 277.827 li
130.491 277.827 li
130.491 305.037 li
152.211 305.037 li
cp
151.961 282.687 mo
147.271 278.067 li
147.271 282.687 li
151.961 282.687 li
cp
148.011 275.887 mo
154.181 281.957 li
154.181 306.987 li
128.511 306.987 li
128.511 275.887 li
148.011 275.887 li
ef
133.451 300.177 mo
133.451 299.207 li
149.251 299.207 li
149.251 300.177 li
133.451 300.177 li
cp
133.451 296.297 mo
133.451 295.327 li
149.251 295.327 li
149.251 296.297 li
133.451 296.297 li
cp
133.451 292.407 mo
133.451 291.437 li
149.251 291.437 li
149.251 292.407 li
133.451 292.407 li
cp
133.451 288.517 mo
133.451 287.547 li
149.251 287.547 li
149.251 288.517 li
133.451 288.517 li
cp
133.451 284.627 mo
133.451 283.657 li
143.361 283.657 li
143.361 284.627 li
133.451 284.627 li
cp
152.211 305.037 mo
152.211 283.657 li
146.291 283.657 li
146.291 277.827 li
130.491 277.827 li
130.491 305.037 li
152.211 305.037 li
cp
151.961 282.687 mo
147.271 278.067 li
147.271 282.687 li
151.961 282.687 li
cp
148.011 275.887 mo
154.181 281.957 li
154.181 306.987 li
128.511 306.987 li
128.511 275.887 li
148.011 275.887 li
cp
@
1 /0 /CSD get_res sepcs
1 sep
RVGGZC+TimesNewRomanPSMT*1 [24.025 0 0 -24.025 0 0 ]msf
99.97 299.007 mo
(...)sh
18.7266 300.177 mo
18.7266 299.207 li
34.5254 299.207 li
34.5254 300.177 li
18.7266 300.177 li
cp
18.7266 296.297 mo
18.7266 295.327 li
34.5254 295.327 li
34.5254 296.297 li
18.7266 296.297 li
cp
18.7266 292.407 mo
18.7266 291.437 li
34.5254 291.437 li
34.5254 292.407 li
18.7266 292.407 li
cp
18.7266 288.517 mo
18.7266 287.547 li
34.5254 287.547 li
34.5254 288.517 li
18.7266 288.517 li
cp
18.7266 284.627 mo
18.7266 283.657 li
28.6395 283.657 li
28.6395 284.627 li
18.7266 284.627 li
cp
37.4875 305.037 mo
37.4875 283.657 li
31.5625 283.657 li
31.5625 277.827 li
15.7645 277.827 li
15.7645 305.037 li
37.4875 305.037 li
cp
37.2406 282.687 mo
32.5504 278.067 li
32.5504 282.687 li
37.2406 282.687 li
cp
33.2906 275.887 mo
39.4625 281.957 li
39.4625 306.987 li
13.7895 306.987 li
13.7895 275.887 li
33.2906 275.887 li
.66 .302 0 0 cmyk
ef
18.7266 300.177 mo
18.7266 299.207 li
34.5254 299.207 li
34.5254 300.177 li
18.7266 300.177 li
cp
18.7266 296.297 mo
18.7266 295.327 li
34.5254 295.327 li
34.5254 296.297 li
18.7266 296.297 li
cp
18.7266 292.407 mo
18.7266 291.437 li
34.5254 291.437 li
34.5254 292.407 li
18.7266 292.407 li
cp
18.7266 288.517 mo
18.7266 287.547 li
34.5254 287.547 li
34.5254 288.517 li
18.7266 288.517 li
cp
18.7266 284.627 mo
18.7266 283.657 li
28.6395 283.657 li
28.6395 284.627 li
18.7266 284.627 li
cp
37.4875 305.037 mo
37.4875 283.657 li
31.5625 283.657 li
31.5625 277.827 li
15.7645 277.827 li
15.7645 305.037 li
37.4875 305.037 li
cp
37.2406 282.687 mo
32.5504 278.067 li
32.5504 282.687 li
37.2406 282.687 li
cp
33.2906 275.887 mo
39.4625 281.957 li
39.4625 306.987 li
13.7895 306.987 li
13.7895 275.887 li
33.2906 275.887 li
cp
@
65.6605 300.177 mo
65.6605 299.207 li
81.4605 299.207 li
81.4605 300.177 li
65.6605 300.177 li
cp
65.6605 296.297 mo
65.6605 295.327 li
81.4605 295.327 li
81.4605 296.297 li
65.6605 296.297 li
cp
65.6605 292.407 mo
65.6605 291.437 li
81.4605 291.437 li
81.4605 292.407 li
65.6605 292.407 li
cp
65.6605 288.517 mo
65.6605 287.547 li
81.4605 287.547 li
81.4605 288.517 li
65.6605 288.517 li
cp
65.6605 284.627 mo
65.6605 283.657 li
75.5703 283.657 li
75.5703 284.627 li
65.6605 284.627 li
cp
84.4203 305.037 mo
84.4203 283.657 li
78.4906 283.657 li
78.4906 277.827 li
62.7004 277.827 li
62.7004 305.037 li
84.4203 305.037 li
cp
84.1703 282.687 mo
79.4805 278.067 li
79.4805 282.687 li
84.1703 282.687 li
cp
80.2203 275.887 mo
86.3906 281.957 li
86.3906 306.987 li
60.7203 306.987 li
60.7203 275.887 li
80.2203 275.887 li
ef
65.6605 300.177 mo
65.6605 299.207 li
81.4605 299.207 li
81.4605 300.177 li
65.6605 300.177 li
cp
65.6605 296.297 mo
65.6605 295.327 li
81.4605 295.327 li
81.4605 296.297 li
65.6605 296.297 li
cp
65.6605 292.407 mo
65.6605 291.437 li
81.4605 291.437 li
81.4605 292.407 li
65.6605 292.407 li
cp
65.6605 288.517 mo
65.6605 287.547 li
81.4605 287.547 li
81.4605 288.517 li
65.6605 288.517 li
cp
65.6605 284.627 mo
65.6605 283.657 li
75.5703 283.657 li
75.5703 284.627 li
65.6605 284.627 li
cp
84.4203 305.037 mo
84.4203 283.657 li
78.4906 283.657 li
78.4906 277.827 li
62.7004 277.827 li
62.7004 305.037 li
84.4203 305.037 li
cp
84.1703 282.687 mo
79.4805 278.067 li
79.4805 282.687 li
84.1703 282.687 li
cp
80.2203 275.887 mo
86.3906 281.957 li
86.3906 306.987 li
60.7203 306.987 li
60.7203 275.887 li
80.2203 275.887 li
cp
@
133.451 300.177 mo
133.451 299.207 li
149.251 299.207 li
149.251 300.177 li
133.451 300.177 li
cp
133.451 296.297 mo
133.451 295.327 li
149.251 295.327 li
149.251 296.297 li
133.451 296.297 li
cp
133.451 292.407 mo
133.451 291.437 li
149.251 291.437 li
149.251 292.407 li
133.451 292.407 li
cp
133.451 288.517 mo
133.451 287.547 li
149.251 287.547 li
149.251 288.517 li
133.451 288.517 li
cp
133.451 284.627 mo
133.451 283.657 li
143.361 283.657 li
143.361 284.627 li
133.451 284.627 li
cp
152.211 305.037 mo
152.211 283.657 li
146.291 283.657 li
146.291 277.827 li
130.491 277.827 li
130.491 305.037 li
152.211 305.037 li
cp
151.961 282.687 mo
147.271 278.067 li
147.271 282.687 li
151.961 282.687 li
cp
148.011 275.887 mo
154.181 281.957 li
154.181 306.987 li
128.511 306.987 li
128.511 275.887 li
148.011 275.887 li
ef
133.451 300.177 mo
133.451 299.207 li
149.251 299.207 li
149.251 300.177 li
133.451 300.177 li
cp
133.451 296.297 mo
133.451 295.327 li
149.251 295.327 li
149.251 296.297 li
133.451 296.297 li
cp
133.451 292.407 mo
133.451 291.437 li
149.251 291.437 li
149.251 292.407 li
133.451 292.407 li
cp
133.451 288.517 mo
133.451 287.547 li
149.251 287.547 li
149.251 288.517 li
133.451 288.517 li
cp
133.451 284.627 mo
133.451 283.657 li
143.361 283.657 li
143.361 284.627 li
133.451 284.627 li
cp
152.211 305.037 mo
152.211 283.657 li
146.291 283.657 li
146.291 277.827 li
130.491 277.827 li
130.491 305.037 li
152.211 305.037 li
cp
151.961 282.687 mo
147.271 278.067 li
147.271 282.687 li
151.961 282.687 li
cp
148.011 275.887 mo
154.181 281.957 li
154.181 306.987 li
128.511 306.987 li
128.511 275.887 li
148.011 275.887 li
cp
@
1 /0 /CSD get_res sepcs
1 sep
RVGGZC+TimesNewRomanPSMT*1 [24.025 0 0 -24.025 0 0 ]msf
99.97 299.007 mo
(...)sh
1.5 lw
2 lc
233.551 356.267 mo
233.551 329.047 li
@
229.531 329.107 mo
233.551 325.087 li
237.571 329.107 li
229.531 329.107 li
cp
ef
RVGGZC+TimesNewRomanPSMT*1 [12.025 0 0 -12.025 0 0 ]msf
215.571 417.477 mo
(Prompt)
[6.73399 3.75165 6.0125 9.72234 6.01251 0 ]xsh
206.171 393.647 mo
206.171 392.347 li
227.381 392.347 li
227.381 393.647 li
206.171 393.647 li
cp
206.171 388.427 mo
206.171 387.127 li
227.381 387.127 li
227.381 388.427 li
206.171 388.427 li
cp
206.171 383.207 mo
206.171 381.907 li
227.381 381.907 li
227.381 383.207 li
206.171 383.207 li
cp
206.171 377.987 mo
206.171 376.687 li
227.381 376.687 li
227.381 377.987 li
206.171 377.987 li
cp
206.171 372.767 mo
206.171 371.467 li
219.481 371.467 li
219.481 372.767 li
206.171 372.767 li
cp
231.361 400.177 mo
231.361 371.467 li
223.401 371.467 li
223.401 363.637 li
202.191 363.637 li
202.191 400.177 li
231.361 400.177 li
cp
231.031 370.157 mo
224.731 363.957 li
224.731 370.157 li
231.031 370.157 li
cp
225.731 361.027 mo
234.011 369.177 li
234.011 402.787 li
199.541 402.787 li
199.541 361.027 li
225.731 361.027 li
.44 .555 1 .3 cmyk
ef
.75 lw
0 lc
206.171 393.647 mo
206.171 392.347 li
227.381 392.347 li
227.381 393.647 li
206.171 393.647 li
cp
206.171 388.427 mo
206.171 387.127 li
227.381 387.127 li
227.381 388.427 li
206.171 388.427 li
cp
206.171 383.207 mo
206.171 381.907 li
227.381 381.907 li
227.381 383.207 li
206.171 383.207 li
cp
206.171 377.987 mo
206.171 376.687 li
227.381 376.687 li
227.381 377.987 li
206.171 377.987 li
cp
206.171 372.767 mo
206.171 371.467 li
219.481 371.467 li
219.481 372.767 li
206.171 372.767 li
cp
231.361 400.177 mo
231.361 371.467 li
223.401 371.467 li
223.401 363.637 li
202.191 363.637 li
202.191 400.177 li
231.361 400.177 li
cp
231.031 370.157 mo
224.731 363.957 li
224.731 370.157 li
231.031 370.157 li
cp
225.731 361.027 mo
234.011 369.177 li
234.011 402.787 li
199.541 402.787 li
199.541 361.027 li
225.731 361.027 li
cp
@
1.5 lw
2 lc
234.011 373.677 mo
244.331 373.677 li
1 /0 /CSD get_res sepcs
1 sep
@
244.271 369.657 mo
248.291 373.677 li
244.271 377.697 li
244.271 369.657 li
cp
ef
234.011 385.017 mo
244.331 385.017 li
@
244.271 380.997 mo
248.291 385.017 li
244.271 389.037 li
244.271 380.997 li
cp
ef
234.011 397.777 mo
244.331 397.777 li
@
244.271 393.757 mo
248.291 397.777 li
244.271 401.797 li
244.271 393.757 li
cp
ef
%ADOBeginSubsetFont: FBAAAA+TimesNewRomanPSMT AddGlyphs
ct_T42Dict begin
systemdict /gcheck known {currentglobal RVGGZC+TimesNewRomanPSMT gcheck setglobal} if
3 1594 78 <000100110000040c058e003703f9b0852b58b10202435458402b1a0c1010
0255190c10100255200c0d0d0255110c0d0d0255010c0d0d0255200c0d10
02551f160d10025526b8ffe8b40d0d025526b8ffe8402b10100255262136
272e1f0121080d0d025521040f0f025521060c0c0255212e0e131302552e
16121202552eb8fff6b40d0d02552eb8fff4b40f0f02552eb8ffeeb41010
02552eb8fffe40100f0f02552e1001111f04260a171a2528b8ffe8b40d0f
025528bb03e20026003503e240123640090d025536370026190c0c0d0d02
550cb803e2b6090c0d0f025509b803e2b10a06003fed2bed2b2f2f3fdd2b
ed10fd2bc0c0c011121739012f2b2b2b2b2b2bdd2b2b2bc0c610c4c610c4
2b2b3130002b2b2b2b2b012b2b1b40b90f391f3902120610010610019309
950a900b900c9b0f9a119b129a1f9f39b30a0a3919391a5f105f115f1f6c
106f116f1f9b0209eb1eed1f028009810ec603c60fe902e90fed11ef1208
3f113f183f1f38203f39460f720a750f082f022a10202520262f39380138
100715105501521054200423105701570fe610f510054911481fc209c20a
e30a05170916101f1d1f1f4502420f060b110f130d1a0c1d0f1e0e1f0653
035504530559105411541306190f1d1d1e1f530204b10602435458402f36
1810100655200110030a27353637007c0c010c7b0901090a0619270c0c39
3801210210100655210c0f0f0655212eb8ffe6b4101006552eb8fff0b40f
0f06552eb8fffab70d0d06552e2e39381112392f2b2b2bdd2b2bc0111239
2f002f2f3fcd5dcd5d3fddcd111217393130012b1b4055100f0102111213
1310191f1a1e192e291e2727220a02091e0a21291e26272336272f41351e
3644002f000b13101024201f14200102201f0f1010300102140101020120
00201f13010427020f0a1010180a37000017b801ec404c180ccc0b0b0a06
2726261919180a0b300c800c02f00c01d00ce00c02700cc00c020c2f1717
9f1801181a1f39013921242e00242f2f002e102eb02ec02ed02e05502e01
802e902e022e603839b80178b321a66e182b2b4ef471725d3c4d10ed10ed
4e1072f65d3c4d10f45d5d5d713c003f3c103c103c3f3c10ed10ed3f3c19
1112392f12393912173901103c3c870e2e182b0e7d10c487082e182b0e7d
10c4001112391810f5edfc01f52b10ed0110c02b10ed0110c0870e7d10c4
c4070759313001727271715d005d72015d5d5d5d5d5d00710071435c58b9
0010ffe84014120b3f1f281239012812391d400f391f280f3902b8ffc0b2
0b390bb8ffc0b211390fb8ffc0b2113909b8ffc0b211390cb8ffc0b11139
012b2b2b2b002b2b2b2b2b012b59015d591b400b01102003270a37000c0a
09b803e240096c0a06251a16032728b803e2b36c19270a00183f332b1732
3f2b323f1112173930315901113736373635342627352115060607071316
171617163315213536363534270111141616171521353237363736351134
26262322072725014fe94a0c082126018e526d41ebeb62223024193efe43
261b28fee7192e4dfe2e4623150b0f0e201a152a110110058efc71d44412
0c0c141d022020022e3bd9fed77b212f0e0a242401151317330167fed059
3818012424110b17215103429f471b112370>RVGGZC+TimesNewRomanPSMT AddT42Char 
RVGGZC+TimesNewRomanPSMT /CharStrings get begin
/g78 78 def
end
RVGGZC+TimesNewRomanPSMT /Encoding get
dup 107 /g78 put
pop
systemdict /gcheck known {setglobal} if
end
%ADOEndSubsetFont
/RVGGZC+TimesNewRomanPSMT*1 
[32{/.notdef}rp /g3 12{/.notdef}rp /g16 /g17 2{/.notdef}rp /g20 /g21 
14{/.notdef}rp /g36 /.notdef /g38 3{/.notdef}rp /g42 /g43 2{/.notdef}rp 
/g46 /g47 /g48 /g49 /.notdef /g51 /g52 /g53 
/g54 /g55 /.notdef /g57 10{/.notdef}rp /g68 2{/.notdef}rp /g71 
/g72 /g73 /g74 /g75 /g76 /.notdef /g78 /g79 
/g80 /g81 /g82 /g83 /.notdef /g85 /g86 /g87 
/g88 /g89 /g90 /g91 /g92 134{/.notdef}rp]
RVGGZC+TimesNewRomanPSMT nf
RVGGZC+TimesNewRomanPSMT*1 [9.775 0 0 -9.775 0 0 ]msf
250.591 377.527 mo
(Task)
[5.97244 4.51611 3.75375 0 ]xsh
RVGGZC+TimesNewRomanPSMT*1 [9.75 0 0 -9.75 0 0 ]msf
250.591 389.557 mo
(T)sh
256.577 389.557 mo
(itle)
[2.99329 2.99323 2.25229 0 ]xsh
RVGGZC+TimesNewRomanPSMT*1 [9.775 0 0 -9.775 0 0 ]msf
250.591 401.557 mo
(Method text)
[8.99316 4.48669 2.24823 5.23941 5.23941 4.49649 2.99115 2.99115 3.7536 5.23941 0 ]xsh
232.511 240.447 mo
232.511 145.207 li
@
228.491 145.257 mo
232.511 141.237 li
236.531 145.257 li
228.491 145.257 li
cp
ef
217.941 74.877 mo
217.941 72.927 li
249.621 72.927 li
249.621 74.877 li
217.941 74.877 li
cp
217.941 67.077 mo
217.941 65.127 li
249.621 65.127 li
249.621 67.077 li
217.941 67.077 li
cp
217.941 59.287 mo
217.941 57.337 li
249.621 57.337 li
249.621 59.287 li
217.941 59.287 li
cp
217.941 51.487 mo
217.941 49.537 li
249.621 49.537 li
249.621 51.487 li
217.941 51.487 li
cp
217.941 43.697 mo
217.941 41.747 li
237.821 41.747 li
237.821 43.697 li
217.941 43.697 li
cp
255.561 84.617 mo
255.561 41.747 li
243.681 41.747 li
243.681 30.047 li
212.001 30.047 li
212.001 84.617 li
255.561 84.617 li
cp
255.071 39.797 mo
245.661 30.537 li
245.661 39.797 li
255.071 39.797 li
cp
247.151 26.157 mo
259.521 38.337 li
259.521 88.517 li
208.041 88.517 li
208.041 26.157 li
247.151 26.157 li
.377 .016 .604 0 cmyk
ef
.75 lw
0 lc
217.941 74.877 mo
217.941 72.927 li
249.621 72.927 li
249.621 74.877 li
217.941 74.877 li
cp
217.941 67.077 mo
217.941 65.127 li
249.621 65.127 li
249.621 67.077 li
217.941 67.077 li
cp
217.941 59.287 mo
217.941 57.337 li
249.621 57.337 li
249.621 59.287 li
217.941 59.287 li
cp
217.941 51.487 mo
217.941 49.537 li
249.621 49.537 li
249.621 51.487 li
217.941 51.487 li
cp
217.941 43.697 mo
217.941 41.747 li
237.821 41.747 li
237.821 43.697 li
217.941 43.697 li
cp
255.561 84.617 mo
255.561 41.747 li
243.681 41.747 li
243.681 30.047 li
212.001 30.047 li
212.001 84.617 li
255.561 84.617 li
cp
255.071 39.797 mo
245.661 30.537 li
245.661 39.797 li
255.071 39.797 li
cp
247.151 26.157 mo
259.521 38.337 li
259.521 88.517 li
208.041 88.517 li
208.041 26.157 li
247.151 26.157 li
cp
@
1 /0 /CSD get_res sepcs
1 sep
%ADOBeginSubsetFont: FBAAAA+TimesNewRomanPSMT AddGlyphs
ct_T42Dict begin
systemdict /gcheck known {currentglobal RVGGZC+TimesNewRomanPSMT gcheck setglobal} if
2 150 11 <00010054fe4a027c058e0013004bb0852b5840239611a71102860c891102
0a980911009801130100000a09a80e22500601068014545e182b10f65ded
fd3c3c103c003fed3fed3130005d015d1bb30113091100183f3f30315901
152627260235100037150606021514171e02027c9765909c0132f67b9e4e
211a4a7dfe6f254c6691018ad4013601ff6e2a44ecfe96c5d6af8aa79a00
>RVGGZC+TimesNewRomanPSMT AddT42Char 
2 300 12 <0001002efe4a0256058e0013004ab0852b58402429042a08480503009801
110a980913000101090aa80e222006300640060306801558a4182b10f65d
edfd3c3c103c003fed3fed3130015d1bb30913011100183f3f3031591335
1617161215100007353636123534272e022e98658f9cfecff77b9f4d2119
4b7c05642a4b6692fe77d5fecafe016e2545eb016bc5d5b08aa69a00>RVGGZC+TimesNewRomanPSMT AddT42Char 
RVGGZC+TimesNewRomanPSMT /CharStrings get begin
/g11 11 def
/g12 12 def
end
RVGGZC+TimesNewRomanPSMT /Encoding get
dup 40 /g11 put
dup 41 /g12 put
pop
systemdict /gcheck known {setglobal} if
end
%ADOEndSubsetFont
/RVGGZC+TimesNewRomanPSMT*1 
[32{/.notdef}rp /g3 7{/.notdef}rp /g11 /g12 3{/.notdef}rp /g16 /g17 
2{/.notdef}rp /g20 /g21 14{/.notdef}rp /g36 /.notdef /g38 3{/.notdef}rp 
/g42 /g43 2{/.notdef}rp /g46 /g47 /g48 /g49 /.notdef 
/g51 /g52 /g53 /g54 /g55 /.notdef /g57 10{/.notdef}rp 
/g68 2{/.notdef}rp /g71 /g72 /g73 /g74 /g75 /g76 
/.notdef /g78 /g79 /g80 /g81 /g82 /g83 /.notdef 
/g85 /g86 /g87 /g88 /g89 /g90 /g91 /g92 
134{/.notdef}rp]
RVGGZC+TimesNewRomanPSMT nf
RVGGZC+TimesNewRomanPSMT*1 [12 0 0 -12 0 0 ]msf
194.941 102.237 mo
(LLM Knowledge )
[7.48781 7.48782 10.5002 3 8.244 6 5.99998 8.9881 3 5.24402 6 6 
5.98801 0 ]xsh
RVGGZC+TimesNewRomanPSMT*1 [12.025 0 0 -12.025 0 0 ]msf
186.441 116.627 mo
(\()sh
190.193 116.627 mo
(summary of method )
[5.24312 6.0125 8.98265 8.99474 5.9884 3.75165 6.0125 3.00624 6.01251 3.71555 3.00624 9.72826 
5.25488 2.99426 6.01251 6.01248 5.97641 0 ]xsh
216.791 131.057 mo
(nov)sh
234.792 131.057 mo
(elty\))
[5.25491 3.73975 2.99425 6.0125 0 ]xsh
217.941 74.877 mo
217.941 72.927 li
249.621 72.927 li
249.621 74.877 li
217.941 74.877 li
cp
217.941 67.077 mo
217.941 65.127 li
249.621 65.127 li
249.621 67.077 li
217.941 67.077 li
cp
217.941 59.287 mo
217.941 57.337 li
249.621 57.337 li
249.621 59.287 li
217.941 59.287 li
cp
217.941 51.487 mo
217.941 49.537 li
249.621 49.537 li
249.621 51.487 li
217.941 51.487 li
cp
217.941 43.697 mo
217.941 41.747 li
237.821 41.747 li
237.821 43.697 li
217.941 43.697 li
cp
255.561 84.617 mo
255.561 41.747 li
243.681 41.747 li
243.681 30.047 li
212.001 30.047 li
212.001 84.617 li
255.561 84.617 li
cp
255.071 39.797 mo
245.661 30.537 li
245.661 39.797 li
255.071 39.797 li
cp
247.151 26.157 mo
259.521 38.337 li
259.521 88.517 li
208.041 88.517 li
208.041 26.157 li
247.151 26.157 li
.377 .016 .604 0 cmyk
ef
217.941 74.877 mo
217.941 72.927 li
249.621 72.927 li
249.621 74.877 li
217.941 74.877 li
cp
217.941 67.077 mo
217.941 65.127 li
249.621 65.127 li
249.621 67.077 li
217.941 67.077 li
cp
217.941 59.287 mo
217.941 57.337 li
249.621 57.337 li
249.621 59.287 li
217.941 59.287 li
cp
217.941 51.487 mo
217.941 49.537 li
249.621 49.537 li
249.621 51.487 li
217.941 51.487 li
cp
217.941 43.697 mo
217.941 41.747 li
237.821 41.747 li
237.821 43.697 li
217.941 43.697 li
cp
255.561 84.617 mo
255.561 41.747 li
243.681 41.747 li
243.681 30.047 li
212.001 30.047 li
212.001 84.617 li
255.561 84.617 li
cp
255.071 39.797 mo
245.661 30.537 li
245.661 39.797 li
255.071 39.797 li
cp
247.151 26.157 mo
259.521 38.337 li
259.521 88.517 li
208.041 88.517 li
208.041 26.157 li
247.151 26.157 li
cp
@
1 /0 /CSD get_res sepcs
1 sep
RVGGZC+TimesNewRomanPSMT*1 [12 0 0 -12 0 0 ]msf
194.941 102.237 mo
(LLM Knowledge )
[7.48781 7.48782 10.5002 3 8.244 6 5.99998 8.9881 3 5.24402 6 6 
5.98801 0 ]xsh
RVGGZC+TimesNewRomanPSMT*1 [12.025 0 0 -12.025 0 0 ]msf
186.441 116.627 mo
(\()sh
190.193 116.627 mo
(summary of method )
[5.24312 6.0125 8.98265 8.99474 5.9884 3.75165 6.0125 3.00624 6.01251 3.71555 3.00624 9.72826 
5.25488 2.99426 6.01251 6.01248 5.97641 0 ]xsh
216.791 131.057 mo
(nov)sh
234.792 131.057 mo
(elty\))
[5.25491 3.73975 2.99425 6.0125 0 ]xsh
58.2504 195.327 mo
58.2504 181.107 69.7703 169.587 83.9906 169.587 cv
98.2004 169.587 109.731 181.107 109.731 195.327 cv
109.731 209.547 98.2004 221.067 83.9906 221.067 cv
69.7703 221.067 58.2504 209.547 58.2504 195.327 cv
.111 0 .177 0 cmyk
ef
.25 lw
2 lc
58.2504 195.327 mo
58.2504 181.107 69.7703 169.587 83.9906 169.587 cv
98.2004 169.587 109.731 181.107 109.731 195.327 cv
109.731 209.547 98.2004 221.067 83.9906 221.067 cv
69.7703 221.067 58.2504 209.547 58.2504 195.327 cv
cp
1 /0 /CSD get_res sepcs
.216 sep
@
76.7906 203.297 mo
76.7906 202.417 li
91.1906 202.417 li
91.1906 203.297 li
76.7906 203.297 li
cp
76.7906 199.757 mo
76.7906 198.867 li
91.1906 198.867 li
91.1906 199.757 li
76.7906 199.757 li
cp
76.7906 196.207 mo
76.7906 195.327 li
91.1906 195.327 li
91.1906 196.207 li
76.7906 196.207 li
cp
76.7906 192.667 mo
76.7906 191.787 li
91.1906 191.787 li
91.1906 192.667 li
76.7906 192.667 li
cp
76.7906 189.127 mo
76.7906 188.237 li
85.8203 188.237 li
85.8203 189.127 li
76.7906 189.127 li
cp
93.8906 207.727 mo
93.8906 188.237 li
88.4906 188.237 li
88.4906 182.927 li
74.0906 182.927 li
74.0906 207.727 li
93.8906 207.727 li
cp
93.6605 187.357 mo
89.3906 183.147 li
89.3906 187.357 li
93.6605 187.357 li
cp
90.0605 181.157 mo
95.6906 186.687 li
95.6906 209.497 li
72.2906 209.497 li
72.2906 181.157 li
90.0605 181.157 li
1 /0 /CSD get_res sepcs
0 sep
ef
.75 lw
0 lc
76.7906 203.297 mo
76.7906 202.417 li
91.1906 202.417 li
91.1906 203.297 li
76.7906 203.297 li
cp
76.7906 199.757 mo
76.7906 198.867 li
91.1906 198.867 li
91.1906 199.757 li
76.7906 199.757 li
cp
76.7906 196.207 mo
76.7906 195.327 li
91.1906 195.327 li
91.1906 196.207 li
76.7906 196.207 li
cp
76.7906 192.667 mo
76.7906 191.787 li
91.1906 191.787 li
91.1906 192.667 li
76.7906 192.667 li
cp
76.7906 189.127 mo
76.7906 188.237 li
85.8203 188.237 li
85.8203 189.127 li
76.7906 189.127 li
cp
93.8906 207.727 mo
93.8906 188.237 li
88.4906 188.237 li
88.4906 182.927 li
74.0906 182.927 li
74.0906 207.727 li
93.8906 207.727 li
cp
93.6605 187.357 mo
89.3906 183.147 li
89.3906 187.357 li
93.6605 187.357 li
cp
90.0605 181.157 mo
95.6906 186.687 li
95.6906 209.497 li
72.2906 209.497 li
72.2906 181.157 li
90.0605 181.157 li
cp
@
58.2504 195.327 mo
58.2504 181.107 69.7703 169.587 83.9906 169.587 cv
98.2004 169.587 109.731 181.107 109.731 195.327 cv
109.731 209.547 98.2004 221.067 83.9906 221.067 cv
69.7703 221.067 58.2504 209.547 58.2504 195.327 cv
.111 0 .177 0 cmyk
ef
.25 lw
2 lc
58.2504 195.327 mo
58.2504 181.107 69.7703 169.587 83.9906 169.587 cv
98.2004 169.587 109.731 181.107 109.731 195.327 cv
109.731 209.547 98.2004 221.067 83.9906 221.067 cv
69.7703 221.067 58.2504 209.547 58.2504 195.327 cv
cp
1 /0 /CSD get_res sepcs
.216 sep
@
76.7906 203.297 mo
76.7906 202.417 li
91.1906 202.417 li
91.1906 203.297 li
76.7906 203.297 li
cp
76.7906 199.757 mo
76.7906 198.867 li
91.1906 198.867 li
91.1906 199.757 li
76.7906 199.757 li
cp
76.7906 196.207 mo
76.7906 195.327 li
91.1906 195.327 li
91.1906 196.207 li
76.7906 196.207 li
cp
76.7906 192.667 mo
76.7906 191.787 li
91.1906 191.787 li
91.1906 192.667 li
76.7906 192.667 li
cp
76.7906 189.127 mo
76.7906 188.237 li
85.8203 188.237 li
85.8203 189.127 li
76.7906 189.127 li
cp
93.8906 207.727 mo
93.8906 188.237 li
88.4906 188.237 li
88.4906 182.927 li
74.0906 182.927 li
74.0906 207.727 li
93.8906 207.727 li
cp
93.6605 187.357 mo
89.3906 183.147 li
89.3906 187.357 li
93.6605 187.357 li
cp
90.0605 181.157 mo
95.6906 186.687 li
95.6906 209.497 li
72.2906 209.497 li
72.2906 181.157 li
90.0605 181.157 li
1 /0 /CSD get_res sepcs
0 sep
ef
.75 lw
0 lc
76.7906 203.297 mo
76.7906 202.417 li
91.1906 202.417 li
91.1906 203.297 li
76.7906 203.297 li
cp
76.7906 199.757 mo
76.7906 198.867 li
91.1906 198.867 li
91.1906 199.757 li
76.7906 199.757 li
cp
76.7906 196.207 mo
76.7906 195.327 li
91.1906 195.327 li
91.1906 196.207 li
76.7906 196.207 li
cp
76.7906 192.667 mo
76.7906 191.787 li
91.1906 191.787 li
91.1906 192.667 li
76.7906 192.667 li
cp
76.7906 189.127 mo
76.7906 188.237 li
85.8203 188.237 li
85.8203 189.127 li
76.7906 189.127 li
cp
93.8906 207.727 mo
93.8906 188.237 li
88.4906 188.237 li
88.4906 182.927 li
74.0906 182.927 li
74.0906 207.727 li
93.8906 207.727 li
cp
93.6605 187.357 mo
89.3906 183.147 li
89.3906 187.357 li
93.6605 187.357 li
cp
90.0605 181.157 mo
95.6906 186.687 li
95.6906 209.497 li
72.2906 209.497 li
72.2906 181.157 li
90.0605 181.157 li
cp
@
1 /0 /CSD get_res sepcs
1 sep
%ADOBeginSubsetFont: FBAAAA+TimesNewRomanPSMT AddGlyphs
ct_T42Dict begin
systemdict /gcheck known {currentglobal RVGGZC+TimesNewRomanPSMT gcheck setglobal} if
2 11576 70 <00010046ffe4034a03af00210222b0852b58b2080401b102024354584020
021a060c10100255060c0f0f0255060c0d0d02550616250f090760217021
0221b8ffc0b513130255211db8ffd4b4131402551db8ffcab6121202551d
3103002fed2b2bc42b5d3fc4ed012f2b2b2bcdc431301bb11223b8ffc040
732a2d340023430d5d36170d5705021c135404530553065407581b581c07
6705760580008021b41bc520d020e000e50509370147015618551c5f2360
18601c7618721c8a128e1390119018a601a402af23b301c101c707c719e9
08e41cea20f4011806024a1257128b1f8b208023f02307112001bcffe000
20ffe0001fffe0b2001d00b8034640301021016021802102002110212021
5021602170219021a021b021c021d021e021f0210d21661ddf0f010fc716
2509071db8ffd8b214391db8ffd8403812391d31030b21cc1f0c014f0c8f
0c020c2f100030004000600070009000b000c000e00009300040000200aa
731a831a02501a019f1a011ab8010c4012f0060100061006200630064006
0506432243b9029100182b4e10f472714ded5d7271fd715de47172ed003f
ed2b2b3feded7110f45d7172e412b10602435458400a531d631d731d0393
1d01005d7159393130383838013801715d005d017200722b2b435c58b400
1018391bb8fff0b613390510103901b8ffc0b2103920b8ffc0b11039002b
2b2b2b012b595901711bb70f0f092121030916b807eab46c0907031db808
1cb26c030b00183f2b3f2b12392f11392f30315901060623220235340033
321615140623222726262726232207061514163332373637034a25d8839c
e80101b487ae312c3b1e110b23233e643d51a189624e3734015cb5c30106
dfd8010e8f4d262f2615761f1e4a62a1a4fb432e7900>RVGGZC+TimesNewRomanPSMT AddT42Char 
RVGGZC+TimesNewRomanPSMT /CharStrings get begin
/g70 70 def
end
RVGGZC+TimesNewRomanPSMT /Encoding get
dup 99 /g70 put
pop
systemdict /gcheck known {setglobal} if
end
%ADOEndSubsetFont
/RVGGZC+TimesNewRomanPSMT*1 
[32{/.notdef}rp /g3 7{/.notdef}rp /g11 /g12 3{/.notdef}rp /g16 /g17 
2{/.notdef}rp /g20 /g21 14{/.notdef}rp /g36 /.notdef /g38 3{/.notdef}rp 
/g42 /g43 2{/.notdef}rp /g46 /g47 /g48 /g49 /.notdef 
/g51 /g52 /g53 /g54 /g55 /.notdef /g57 10{/.notdef}rp 
/g68 /.notdef /g70 /g71 /g72 /g73 /g74 /g75 
/g76 /.notdef /g78 /g79 /g80 /g81 /g82 /g83 
/.notdef /g85 /g86 /g87 /g88 /g89 /g90 /g91 
/g92 134{/.notdef}rp]
RVGGZC+TimesNewRomanPSMT nf
RVGGZC+TimesNewRomanPSMT*1 [12.025 0 0 -12.025 0 0 ]msf
27.616 237.257 mo
(Aspect annotation model)
[8.98265 4.49172 6.0125 5.2487 5.255 2.99415 3.36025 5.33201 6.0125 6.0125 6.0363 3.03025 
6.0125 3.03034 3.03025 6.0125 6.0125 3.04235 9.76435 6.0125 6.01251 5.30299 0 ]xsh
1.5 lw
2 lc
83.3203 268.797 mo
83.3203 241.587 li
@
79.3004 241.637 mo
83.3203 237.617 li
87.3406 241.637 li
79.3004 241.637 li
cp
ef
68.9504 74.877 mo
68.9504 72.927 li
100.631 72.927 li
100.631 74.877 li
68.9504 74.877 li
cp
68.9504 67.077 mo
68.9504 65.127 li
100.631 65.127 li
100.631 67.077 li
68.9504 67.077 li
cp
68.9504 59.287 mo
68.9504 57.337 li
100.631 57.337 li
100.631 59.287 li
68.9504 59.287 li
cp
68.9504 51.487 mo
68.9504 49.537 li
100.631 49.537 li
100.631 51.487 li
68.9504 51.487 li
cp
68.9504 43.697 mo
68.9504 41.747 li
88.8305 41.747 li
88.8305 43.697 li
68.9504 43.697 li
cp
106.571 84.617 mo
106.571 41.747 li
94.6906 41.747 li
94.6906 30.047 li
63.0105 30.047 li
63.0105 84.617 li
106.571 84.617 li
cp
106.081 39.797 mo
96.6703 30.537 li
96.6703 39.797 li
106.081 39.797 li
cp
98.1605 26.157 mo
110.531 38.337 li
110.531 88.517 li
59.0504 88.517 li
59.0504 26.157 li
98.1605 26.157 li
.444 .272 0 0 cmyk
ef
.75 lw
0 lc
68.9504 74.877 mo
68.9504 72.927 li
100.631 72.927 li
100.631 74.877 li
68.9504 74.877 li
cp
68.9504 67.077 mo
68.9504 65.127 li
100.631 65.127 li
100.631 67.077 li
68.9504 67.077 li
cp
68.9504 59.287 mo
68.9504 57.337 li
100.631 57.337 li
100.631 59.287 li
68.9504 59.287 li
cp
68.9504 51.487 mo
68.9504 49.537 li
100.631 49.537 li
100.631 51.487 li
68.9504 51.487 li
cp
68.9504 43.697 mo
68.9504 41.747 li
88.8305 41.747 li
88.8305 43.697 li
68.9504 43.697 li
cp
106.571 84.617 mo
106.571 41.747 li
94.6906 41.747 li
94.6906 30.047 li
63.0105 30.047 li
63.0105 84.617 li
106.571 84.617 li
cp
106.081 39.797 mo
96.6703 30.537 li
96.6703 39.797 li
106.081 39.797 li
cp
98.1605 26.157 mo
110.531 38.337 li
110.531 88.517 li
59.0504 88.517 li
59.0504 26.157 li
98.1605 26.157 li
cp
@
1 /0 /CSD get_res sepcs
1 sep
RVGGZC+TimesNewRomanPSMT*1 [12.025 0 0 -12.025 0 0 ]msf
41.116 100.877 mo
(Human Knowledge )
[8.98265 6.0125 8.98265 5.255 6.0125 3.00626 8.97064 6.0125 6.0125 8.22506 3.73984 5.25491 
6.0125 6.0125 5.23091 0 ]xsh
RVGGZC+TimesNewRomanPSMT*1 [12 0 0 -12 0 0 ]msf
41.966 115.307 mo
(\()sh
45.7156 115.307 mo
(sentences with the )
[4.8951 5.28 6 3.792 5.28001 6 5.328 5.244 4.52419 3.00001 9.036 3.024 
3.768 6 3.036 3.02399 6.00001 5.328 0 ]xsh
44.9656 129.737 mo
(aspect of novelty\))
[5.244 4.49429 6 5.24991 5.988 3 3 6 3.75581 3 6 6 
6 5.24401 3.744 3 6.32529 0 ]xsh
1.5 lw
2 lc
83.3203 163.917 mo
83.3203 136.697 li
@
79.3004 136.757 mo
83.3203 132.737 li
87.3406 136.757 li
79.3004 136.757 li
cp
ef
.25 lw
[2 1 ] 0 dsh
2.1066 566.436 mo
302.716 566.436 li
302.716 3.75586 li
2.1066 3.75586 li
cp
@
RVGGZC+TimesNewRomanPSMT*1 [12 0 0 -12 0 0 ]msf
445.471 554.782 mo
(Human Knowledge )
[8.98801 6 9 5.24399 6 3 8.98801 6 6 8.24399 3.74402 5.24402 
6 6 5.24396 0 ]xsh
[2 1 ] 0 dsh
361.111 566.436 mo
752.501 566.436 li
752.501 3.75586 li
361.111 3.75586 li
cp
@
315.531 305.107 mo
315.531 321.027 li
331.201 321.027 li
331.201 328.987 li
350.001 313.097 li
331.201 297.147 li
331.201 305.107 li
315.531 305.107 li
.885 .543 .049 .002 cmyk
ef
473.291 170.077 mo
575.341 170.077 li
578.471 170.077 581.01 167.537 581.01 164.407 cv
581.01 151.837 li
581.01 148.707 578.471 146.167 575.341 146.167 cv
473.291 146.167 li
470.161 146.167 467.63 148.707 467.63 151.837 cv
467.63 164.407 li
467.63 167.537 470.161 170.077 473.291 170.077 cv
.129 .073 0 0 cmyk
ef
[] 0 dsh
473.291 170.077 mo
575.341 170.077 li
578.471 170.077 581.01 167.537 581.01 164.407 cv
581.01 151.837 li
581.01 148.707 578.471 146.167 575.341 146.167 cv
473.291 146.167 li
470.161 146.167 467.63 148.707 467.63 151.837 cv
467.63 164.407 li
467.63 167.537 470.161 170.077 473.291 170.077 cv
cp
.115 .032 .005 0 cmyk
@
1 /0 /CSD get_res sepcs
1 sep
%ADOBeginSubsetFont: FBAAAA+TimesNewRomanPSMT AddGlyphs
ct_T42Dict begin
systemdict /gcheck known {currentglobal RVGGZC+TimesNewRomanPSMT gcheck setglobal} if
2 2568 41 <000100210000041f054c002d0178b0852b58b1282fb8011e403725643609
04090ab02f03982bba2bc62bd903d32be904e90afb04fb0a09700570067f
077f08800580068f078f0808070a092a0207210c0cb80126400d081b071d
1f1b17212206210202b801264029051b060e1f1b1621231e1f1b2621232b
2c280a080c0405020201230c0d0d172d002326002810280228b802d34025
27272602161708272b28ac002901002930294029702904299006061f0701
4f0701bf070107b801b5402e000e06131302550e0c0f0f02550e0c0d0d02
550e221e1d0c101002551d0c0f0f02551d1a0d0d02551d9e2e6163182b4e
10f42b2b2b3c4dfd2b2b2b3cf45d71723c10f65d71fde4003f3c3f3c10ee
5d10fd3c12392f3cfd3c111239111239011112392b2b0110edec0010fd2b
0110edec0010fd313000715d015d712b1b400c2929260505260808172601
0db807f2b56c0101172600b807edb26c2625b803e2b56c2602141718b803
e2b26c170800183f2b323f2b2b12392f2b1112392f11392f11392f303159
0111333236373311232e0223231114171617163333152135333237363511
34272627262323352113232e022301a3f7554f0d252501274544f70d0a20
2c3031fdba305426180d0a1f2b313003f10d231a45656a0502fdeb4b6ffe
354f4a25fe566721191218252531207a036c672119121825fed65f592800
>RVGGZC+TimesNewRomanPSMT AddT42Char 
RVGGZC+TimesNewRomanPSMT /CharStrings get begin
/g41 41 def
end
RVGGZC+TimesNewRomanPSMT /Encoding get
dup 70 /g41 put
pop
systemdict /gcheck known {setglobal} if
end
%ADOEndSubsetFont
/RVGGZC+TimesNewRomanPSMT*1 
[32{/.notdef}rp /g3 7{/.notdef}rp /g11 /g12 3{/.notdef}rp /g16 /g17 
2{/.notdef}rp /g20 /g21 14{/.notdef}rp /g36 /.notdef /g38 2{/.notdef}rp 
/g41 /g42 /g43 2{/.notdef}rp /g46 /g47 /g48 /g49 
/.notdef /g51 /g52 /g53 /g54 /g55 /.notdef /g57 
10{/.notdef}rp /g68 /.notdef /g70 /g71 /g72 /g73 /g74 
/g75 /g76 /.notdef /g78 /g79 /g80 /g81 /g82 
/g83 /.notdef /g85 /g86 /g87 /g88 /g89 /g90 
/g91 /g92 134{/.notdef}rp]
RVGGZC+TimesNewRomanPSMT nf
RVGGZC+TimesNewRomanPSMT*1 [14.275 0 0 -14.275 0 0 ]msf
485.741 162.537 mo
(Feed Forward)
[7.49442 6.73779 5.99548 6.75214 3.74005 7.49426 7.4801 4.49646 9.74988 6.73773 4.49646 0 
]xsh
473.291 131.177 mo
575.341 131.177 li
578.471 131.177 581.01 128.637 581.01 125.507 cv
581.01 112.937 li
581.01 109.807 578.471 107.267 575.341 107.267 cv
473.291 107.267 li
470.161 107.267 467.63 109.807 467.63 112.937 cv
467.63 125.507 li
467.63 128.637 470.161 131.177 473.291 131.177 cv
.111 0 .177 0 cmyk
ef
473.291 131.177 mo
575.341 131.177 li
578.471 131.177 581.01 128.637 581.01 125.507 cv
581.01 112.937 li
581.01 109.807 578.471 107.267 575.341 107.267 cv
473.291 107.267 li
470.161 107.267 467.63 109.807 467.63 112.937 cv
467.63 125.507 li
467.63 128.637 470.161 131.177 473.291 131.177 cv
cp
@
1 /0 /CSD get_res sepcs
1 sep
RVGGZC+TimesNewRomanPSMT*1 [14.275 0 0 -14.275 0 0 ]msf
484.76 123.587 mo
(Att-Reduction)
[9.74985 4.48236 3.67874 4.63889 9.022 6.76642 6.78058 6.78064 6.76642 3.76849 3.76868 6.78058 
0 ]xsh
473.291 92.267 mo
575.341 92.267 li
578.471 92.267 581.01 89.727 581.01 86.597 cv
581.01 74.027 li
581.01 70.897 578.471 68.357 575.341 68.357 cv
473.291 68.357 li
470.161 68.357 467.63 70.897 467.63 74.027 cv
467.63 86.597 li
467.63 89.727 470.161 92.267 473.291 92.267 cv
.129 .073 0 0 cmyk
ef
473.291 92.267 mo
575.341 92.267 li
578.471 92.267 581.01 89.727 581.01 86.597 cv
581.01 74.027 li
581.01 70.897 578.471 68.357 575.341 68.357 cv
473.291 68.357 li
470.161 68.357 467.63 70.897 467.63 74.027 cv
467.63 86.597 li
467.63 89.727 470.161 92.267 473.291 92.267 cv
cp
.115 .032 .005 0 cmyk
@
1 /0 /CSD get_res sepcs
1 sep
RVGGZC+TimesNewRomanPSMT*1 [14.25 0 0 -14.25 0 0 ]msf
497.591 84.627 mo
(FC-Layer)
[7.52499 9.62515 4.67987 8.25055 6.7403 6.75452 5.99915 0 ]xsh
473.291 53.3669 mo
575.341 53.3669 li
578.471 53.3669 581.01 50.827 581.01 47.697 cv
581.01 35.127 li
581.01 31.997 578.471 29.457 575.341 29.457 cv
473.291 29.457 li
470.161 29.457 467.63 31.997 467.63 35.127 cv
467.63 47.697 li
467.63 50.827 470.161 53.3669 473.291 53.3669 cv
.129 .073 0 0 cmyk
ef
473.291 53.3669 mo
575.341 53.3669 li
578.471 53.3669 581.01 50.827 581.01 47.697 cv
581.01 35.127 li
581.01 31.997 578.471 29.457 575.341 29.457 cv
473.291 29.457 li
470.161 29.457 467.63 31.997 467.63 35.127 cv
467.63 47.697 li
467.63 50.827 470.161 53.3669 473.291 53.3669 cv
cp
.115 .032 .005 0 cmyk
@
1 /0 /CSD get_res sepcs
1 sep
RVGGZC+TimesNewRomanPSMT*1 [14.275 0 0 -14.275 0 0 ]msf
501.091 45.6569 mo
(Softmax)
[7.52289 7.50861 4.49646 3.75433 11.2629 5.99554 0 ]xsh
1.5 lw
524.32 68.357 mo
524.32 57.327 li
@
520.301 57.387 mo
524.32 53.367 li
528.341 57.387 li
520.301 57.387 li
cp
ef
524.32 107.267 mo
524.32 96.237 li
@
520.301 96.287 mo
524.32 92.267 li
528.341 96.287 li
520.301 96.287 li
cp
ef
524.32 146.167 mo
524.32 135.137 li
@
520.301 135.197 mo
524.32 131.177 li
528.341 135.197 li
520.301 135.197 li
cp
ef
473.291 170.077 mo
575.341 170.077 li
578.471 170.077 581.01 167.537 581.01 164.407 cv
581.01 151.837 li
581.01 148.707 578.471 146.167 575.341 146.167 cv
473.291 146.167 li
470.161 146.167 467.63 148.707 467.63 151.837 cv
467.63 164.407 li
467.63 167.537 470.161 170.077 473.291 170.077 cv
.129 .073 0 0 cmyk
ef
.25 lw
473.291 170.077 mo
575.341 170.077 li
578.471 170.077 581.01 167.537 581.01 164.407 cv
581.01 151.837 li
581.01 148.707 578.471 146.167 575.341 146.167 cv
473.291 146.167 li
470.161 146.167 467.63 148.707 467.63 151.837 cv
467.63 164.407 li
467.63 167.537 470.161 170.077 473.291 170.077 cv
cp
.115 .032 .005 0 cmyk
@
1 /0 /CSD get_res sepcs
1 sep
RVGGZC+TimesNewRomanPSMT*1 [14.275 0 0 -14.275 0 0 ]msf
485.741 162.537 mo
(Feed Forward)
[7.49442 6.73779 5.99548 6.75214 3.74005 7.49426 7.4801 4.49646 9.74988 6.73773 4.49646 0 
]xsh
473.291 131.177 mo
575.341 131.177 li
578.471 131.177 581.01 128.637 581.01 125.507 cv
581.01 112.937 li
581.01 109.807 578.471 107.267 575.341 107.267 cv
473.291 107.267 li
470.161 107.267 467.63 109.807 467.63 112.937 cv
467.63 125.507 li
467.63 128.637 470.161 131.177 473.291 131.177 cv
.111 0 .177 0 cmyk
ef
473.291 131.177 mo
575.341 131.177 li
578.471 131.177 581.01 128.637 581.01 125.507 cv
581.01 112.937 li
581.01 109.807 578.471 107.267 575.341 107.267 cv
473.291 107.267 li
470.161 107.267 467.63 109.807 467.63 112.937 cv
467.63 125.507 li
467.63 128.637 470.161 131.177 473.291 131.177 cv
cp
@
1 /0 /CSD get_res sepcs
1 sep
RVGGZC+TimesNewRomanPSMT*1 [14.275 0 0 -14.275 0 0 ]msf
484.76 123.587 mo
(Att-Reduction)
[9.74985 4.48236 3.67874 4.63889 9.022 6.76642 6.78058 6.78064 6.76642 3.76849 3.76868 6.78058 
0 ]xsh
473.291 92.267 mo
575.341 92.267 li
578.471 92.267 581.01 89.727 581.01 86.597 cv
581.01 74.027 li
581.01 70.897 578.471 68.357 575.341 68.357 cv
473.291 68.357 li
470.161 68.357 467.63 70.897 467.63 74.027 cv
467.63 86.597 li
467.63 89.727 470.161 92.267 473.291 92.267 cv
.129 .073 0 0 cmyk
ef
473.291 92.267 mo
575.341 92.267 li
578.471 92.267 581.01 89.727 581.01 86.597 cv
581.01 74.027 li
581.01 70.897 578.471 68.357 575.341 68.357 cv
473.291 68.357 li
470.161 68.357 467.63 70.897 467.63 74.027 cv
467.63 86.597 li
467.63 89.727 470.161 92.267 473.291 92.267 cv
cp
.115 .032 .005 0 cmyk
@
1 /0 /CSD get_res sepcs
1 sep
RVGGZC+TimesNewRomanPSMT*1 [14.25 0 0 -14.25 0 0 ]msf
497.591 84.627 mo
(FC-Layer)
[7.52499 9.62515 4.67987 8.25055 6.7403 6.75452 5.99915 0 ]xsh
473.291 53.3669 mo
575.341 53.3669 li
578.471 53.3669 581.01 50.827 581.01 47.697 cv
581.01 35.127 li
581.01 31.997 578.471 29.457 575.341 29.457 cv
473.291 29.457 li
470.161 29.457 467.63 31.997 467.63 35.127 cv
467.63 47.697 li
467.63 50.827 470.161 53.3669 473.291 53.3669 cv
.129 .073 0 0 cmyk
ef
473.291 53.3669 mo
575.341 53.3669 li
578.471 53.3669 581.01 50.827 581.01 47.697 cv
581.01 35.127 li
581.01 31.997 578.471 29.457 575.341 29.457 cv
473.291 29.457 li
470.161 29.457 467.63 31.997 467.63 35.127 cv
467.63 47.697 li
467.63 50.827 470.161 53.3669 473.291 53.3669 cv
cp
.115 .032 .005 0 cmyk
@
1 /0 /CSD get_res sepcs
1 sep
RVGGZC+TimesNewRomanPSMT*1 [14.275 0 0 -14.275 0 0 ]msf
501.091 45.6569 mo
(Softmax)
[7.52289 7.50861 4.49646 3.75433 11.2629 5.99554 0 ]xsh
1.5 lw
524.32 68.357 mo
524.32 57.327 li
@
520.301 57.387 mo
524.32 53.367 li
528.341 57.387 li
520.301 57.387 li
cp
ef
524.32 107.267 mo
524.32 96.237 li
@
520.301 96.287 mo
524.32 92.267 li
528.341 96.287 li
520.301 96.287 li
cp
ef
524.32 146.167 mo
524.32 135.137 li
@
520.301 135.197 mo
524.32 131.177 li
528.341 135.197 li
520.301 135.197 li
cp
ef
584.5 189.217 mo
584.5 177.807 li
@
580.481 177.857 mo
584.5 173.837 li
588.521 177.857 li
580.481 177.857 li
cp
ef
580.801 99.427 mo
603.19 99.287 li
603.051 61.867 li
635.161 61.737 li
@
635.091 57.717 mo
639.121 61.727 li
635.121 65.757 li
635.091 57.717 li
cp
ef
580.801 99.427 mo
603.19 99.287 li
603.481 135.567 li
635.161 135.697 li
@
635.121 131.677 mo
639.121 135.717 li
635.091 139.717 li
635.121 131.677 li
cp
ef
RVGGZC+TimesNewRomanPSMT*1 [12.025 0 0 -12.025 0 0 ]msf
10.766 17.3769 mo
(Process input data )
[6.734 3.75164 6.0125 5.2429 5.25491 5.24311 4.49752 3.00625 2.99425 6.0125 6.0125 5.9823 
3.73975 3.00625 6.0125 5.2309 2.99425 5.25491 0 ]xsh
RVGGZC+TimesNewRomanPSMT*1 [12 0 0 -12 0 0 ]msf
366.591 17.3069 mo
(P)sh
373.359 17.3069 mo
(roposed model)
[3.7438 6 6 6 4.5061 5.98801 6 3 9.02399 6 6 5.24402 
0 ]xsh
378.861 471.427 mo
(Text )
[7.48782 5.24399 6 3 0 ]xsh
RVGGZC+TimesNewRomanPSMT*1 [12.025 0 0 -12.025 0 0 ]msf
370.861 485.827 mo
(encoder)
[5.25491 6.01248 5.24292 6.01248 6.01251 5.2309 0 ]xsh
369.571 262.807 mo
(Knowledge )
[8.98267 6.01248 6.01251 8.22513 3.73978 5.25488 6.01251 6.01251 5.2309 0 ]xsh
380.921 277.237 mo
(guided )
[5.98981 6.01248 2.98224 6.01251 5.97641 6.01248 0 ]xsh
379.241 291.657 mo
(module)
[9.35544 6.01251 6.01248 5.9762 2.99417 0 ]xsh
372.561 96.2769 mo
(Prediction )
[6.73401 3.75162 5.25491 6.01251 3.72772 5.25491 2.99426 3.73975 6.01248 6.01251 0 ]xsh
385.241 110.707 mo
(layer)
[3.35205 5.25491 6.01248 5.24283 0 ]xsh
497.831 434.047 mo
520.76 434.047 li
521.541 434.047 522.181 433.407 522.181 432.627 cv
522.181 417.497 li
522.181 416.707 521.541 416.077 520.76 416.077 cv
497.831 416.077 li
497.051 416.077 496.411 416.707 496.411 417.497 cv
496.411 432.627 li
496.411 433.407 497.051 434.047 497.831 434.047 cv
.444 .272 0 0 cmyk
ef
.25 lw
1 lc
1 lj
497.831 434.047 mo
520.76 434.047 li
521.541 434.047 522.181 433.407 522.181 432.627 cv
522.181 417.497 li
522.181 416.707 521.541 416.077 520.76 416.077 cv
497.831 416.077 li
497.051 416.077 496.411 416.707 496.411 417.497 cv
496.411 432.627 li
496.411 433.407 497.051 434.047 497.831 434.047 cv
cp
1 /0 /CSD get_res sepcs
1 sep
@
548.851 434.547 mo
571.791 434.547 li
572.57 434.547 573.201 433.907 573.201 433.127 cv
573.201 417.997 li
573.201 417.217 572.57 416.577 571.791 416.577 cv
548.851 416.577 li
548.07 416.577 547.431 417.217 547.431 417.997 cv
547.431 433.127 li
547.431 433.907 548.07 434.547 548.851 434.547 cv
.444 .272 0 0 cmyk
ef
548.851 434.547 mo
571.791 434.547 li
572.57 434.547 573.201 433.907 573.201 433.127 cv
573.201 417.997 li
573.201 417.217 572.57 416.577 571.791 416.577 cv
548.851 416.577 li
548.07 416.577 547.431 417.217 547.431 417.997 cv
547.431 433.127 li
547.431 433.907 548.07 434.547 548.851 434.547 cv
cp
1 /0 /CSD get_res sepcs
1 sep
@
458.871 434.617 mo
481.801 434.617 li
482.581 434.617 483.221 433.987 483.221 433.207 cv
483.221 418.067 li
483.221 417.287 482.581 416.657 481.801 416.657 cv
458.871 416.657 li
458.081 416.657 457.451 417.287 457.451 418.067 cv
457.451 433.207 li
457.451 433.987 458.081 434.617 458.871 434.617 cv
.444 .272 0 0 cmyk
ef
458.871 434.617 mo
481.801 434.617 li
482.581 434.617 483.221 433.987 483.221 433.207 cv
483.221 418.067 li
483.221 417.287 482.581 416.657 481.801 416.657 cv
458.871 416.657 li
458.081 416.657 457.451 417.287 457.451 418.067 cv
457.451 433.207 li
457.451 433.987 458.081 434.617 458.871 434.617 cv
cp
1 /0 /CSD get_res sepcs
1 sep
@
grestore
gsave
464.661 434.563 mo
478.629 434.563 li
478.629 415.544 li
464.661 415.544 li
cp
eclp
RVGGZC+TimesNewRomanPSMT*1 [6.94644 0 0 -6.952 0 0 ]msf
471.489 431.655 mo
(1)sh
RVGGZD+TimesNewRomanPS-ItalicMT*1 [6.94644 0 0 -6.952 0 0 ]msf
472.83 423.178 mo
(v)sh
RVGGZD+TimesNewRomanPS-ItalicMT*1 [12.0164 0 0 -12.026 0 0 ]msf
467.03 428.558 mo
(x)sh
grestore
RVGGZC+TimesNewRomanPSMT*1 [18.025 0 0 -18.025 0 0 ]msf
529.491 426.377 mo
(...)sh
gsave
554.56 435.063 mo
568.529 435.064 li
568.529 416.044 li
554.56 416.044 li
554.56 435.063 li
eclp
RVGGZD+TimesNewRomanPS-ItalicMT*1 [6.94644 0 0 -6.952 0 0 ]msf
562.729 423.678 mo
(v)sh
561.92 432.155 mo
(i)sh
RVGGZD+TimesNewRomanPS-ItalicMT*1 [12.0164 0 0 -12.026 0 0 ]msf
556.93 429.058 mo
(x)sh
grestore
420.001 435.027 mo
442.941 435.027 li
443.721 435.027 444.351 434.387 444.351 433.607 cv
444.351 418.477 li
444.351 417.687 443.721 417.057 442.941 417.057 cv
420.001 417.057 li
419.221 417.057 418.591 417.687 418.591 418.477 cv
418.591 433.607 li
418.591 434.387 419.221 435.027 420.001 435.027 cv
.444 .272 0 0 cmyk
ef
.25 lw
1 lc
1 lj
420.001 435.027 mo
442.941 435.027 li
443.721 435.027 444.351 434.387 444.351 433.607 cv
444.351 418.477 li
444.351 417.687 443.721 417.057 442.941 417.057 cv
420.001 417.057 li
419.221 417.057 418.591 417.687 418.591 418.477 cv
418.591 433.607 li
418.591 434.387 419.221 435.027 420.001 435.027 cv
cp
1 /0 /CSD get_res sepcs
1 sep
@
2 lc
0 lj
[2 1 ] 0 dsh
414.331 439.217 mo
577.32 439.217 li
577.32 410.871 li
414.331 410.871 li
cp
@
gsave
424.37 434.963 mo
439.342 434.963 li
439.342 415.944 li
424.37 415.944 li
cp
eclp
RVGGZC+TimesNewRomanPSMT*1 [6.94852 0 0 -6.952 0 0 ]msf
432.73 423.578 mo
(v)sh
RVGGZD+TimesNewRomanPS-ItalicMT*1 [6.94852 0 0 -6.952 0 0 ]msf
431.73 432.055 mo
(C)sh
RVGGZD+TimesNewRomanPS-ItalicMT*1 [12.02 0 0 -12.026 0 0 ]msf
426.741 428.958 mo
(x)sh
grestore
gsave
504.01 432.887 mo
516 432.887 li
516 416.899 li
504.01 416.899 li
cp
clp
RVGGZC+TimesNewRomanPSMT*1 [5.78795 0 0 -5.792 0 0 ]msf
510.708 430.502 mo
(2)sh
RVGGZD+TimesNewRomanPS-ItalicMT*1 [5.78795 0 0 -5.792 0 0 ]msf
511.178 423.403 mo
(v)sh
RVGGZD+TimesNewRomanPS-ItalicMT*1 [10.01 0 0 -10.017 0 0 ]msf
506.327 427.906 mo
(x)sh
grestore
grestore
grestore
pgrs
%%PageTrailer
[
[/CSA [/0 ]]
[/CSD [/0 ]]
] del_res
/RVGGZC+TimesNewRomanPSMT*1 uf
/RVGGZC+TimesNewRomanPSMT uf
/FBAAAA+TimesNewRomanPSMT uf
/RVGGZD+TimesNewRomanPS-ItalicMT*1 uf
/RVGGZD+TimesNewRomanPS-ItalicMT uf
/HBAAAA+TimesNewRomanPS-ItalicMT uf
Adobe_AGM_Image/pt gx
Adobe_CoolType_Core/pt get exec
Adobe_AGM_Core/restore_mysetup gx
Adobe_AGM_Core/pt gx
currentdict Adobe_AGM_Utils eq {end} if
%%Trailer
Adobe_AGM_Utils begin
[/EMC pdfmark_5
currentdict Adobe_AGM_Utils eq {end} if
Adobe_AGM_Image/dt get exec
Adobe_CoolType_Core/dt get exec
Adobe_AGM_Core/dt get exec
%%Pages: 1
%%DocumentNeededResources: 
%%DocumentSuppliedResources: procset Adobe_AGM_Image 1.0 0
%%+ procset Adobe_CoolType_Utility_T42 1.0 0
%%+ procset Adobe_CoolType_Utility_MAKEOCF 1.23 0
%%+ procset Adobe_CoolType_Core 2.31 0
%%+ procset Adobe_AGM_Core 2.0 0
%%+ procset Adobe_AGM_Utils 1.0 0
%%DocumentNeededFeatures: 
%%DocumentSuppliedFeatures: 
%%DocumentCustomColors: 
%%CMYKCustomColor: 
%%RGBCustomColor: 
%%EOF
ing Figure4.eps…]()

## Directory structure

<pre>
originality_predict                               Root directory
├── Code                                          Source code folder
│   ├── baseline_model                            Baseline model folder
│   │    ├── load_method.py                       Load data for Review and Method as input
│   │    ├── main.py                              Train the model for Review and Feedback as input
│   │    ├── method_main.py                       Train the model for Review and Method as input
│   │    ├── model.py                             Model structure
│   │    ├── predict.py                           Predict the result
│   │    ├── split_data.py                        Load data for Review and Feedback as input
│   │    ├── util.py                              Data process tool
│   ├── Bi_interaction.py                         Proposed model structure      
│   ├── p_predict.py                              Predict the result
│   └── proposed_main.py                          Train the proposed model 
│   └── read_data.py                              Load data for Review and Feedback
├── Dataset                                       Dataset folder
│   └── Dataset.json                              Preprocessed Dataset
│
└── README.md
</pre>
## Dataset Discription

The dataset contains four contents: 
  - "novelty_sentence": Originality evaluation sentences by reviewers
  - "chat_content"： Feedback from ChatGPT
  - "nov_score":  Technical Novelty And Significance score
  - "decision":  Paper decsion
  - A Sample From Dataset: 
{"id": "-0Cjhnl-dhK",
**"novelty_sentence"**: "Methodologically speaking, it is not clear to me what is the contribution of this paper.They propose a constrained optimization framework to achieve such results and demonstrate it empirically on different tasks.......which is a constrained optimization alternative to empirical risk minimization. Overall, I liked this paper.", 
**"chat_content"**: "The article \"TOWARDS UNCERTAINTIES IN DEEP LEARNING THAT ARE ACCURATE AND CALIBRATED\" presents a novel approach to achieving calibrated and sharp predictive uncertainties in machine learning models....... The article provides a detailed algorithm for achieving calibrated learning of probabilistic models and discusses the practical considerations and benefits of calibrated predictive uncertainties in machine learning applications.\n", "method_content": "Supervised machine learning models commonly predict a probability distribution over the output variables -e.g. class membership probabilities or the parameters of an exponential family distribution.........Efficient Exploration. Balancing exploration and exploitation is a common challenge in many applications on machine learning such as reinforcement learning, Bayesian optimization, and active learning. When probabilistic models are uncalibrated, inaccurate confidence intervals might incentivize the model to explore ineffective actions, degrading performance. Calibrated uncertainties have been shown to improve decision-making in bandits (Malik et al., 2019) and likely to extend to Bayesian optimization and active learning as well.Other Applications. The importance of accurate confidence estimates has been highlighted by practitioners in many fields, including medicine (Saria, 2018) , meteorology (Raftery et al., 2005) , and natural language processing (Nguyen and O'Connor, 2015) . Accurate confidence estimates also play an important in computer vision applications, such as depth estimation (Kendall and Gal, 2017) .", 
**"novelty_score"**: 2, 
**"decision"**: 1}
## Quick Start

<b> </b>
    - <code> python ./Code/baseline_model./method_main.py</code>  Execute this command to train model with Review and Method as input.<br>
    - <code> python ./Code/baseline_model./main.py</code>  Execute this command to train model with Review and Feedback as input.<br>
    - <code> python ./Code/proposed_main.py</code>  Execute this command to train our proposed model.<br>
## Main result
The results generated by the large language models in this paper can be found at https://drive.google.com/drive/folders/1acu1HKqts-fGFKkq0aVI8XXJgoKl4HBr?usp=drive_link
- <b>Results of originality prediction.</b><br>
<div align=center>

<table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0
 style='border-collapse:collapse;border:none'>
 <tr>
  <td width=184 rowspan=2 style='width:138.25pt;border:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><a
  name="_Hlk160115425"><span lang=EN-US style='font-size:12.0pt;font-family:
  "Times New Roman",serif'>Models</span></a></p>
  </td>
  <td width=184 colspan=2 style='width:138.25pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>Review &amp;
  method</span></p>
  </td>
  <td width=184 colspan=2 style='width:138.3pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>Review &amp;
  feedback</span></p>
  </td>
 </tr>
 <tr>
  <td width=92 style='width:69.1pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>F1</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>Accuracy</span></p>
  </td>
  <td width=92 style='width:69.15pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>F1</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>Accuracy</span></p>
  </td>
 </tr>
 <tr>
  <td width=184 style='width:138.25pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>BERT</span></p>
  </td>
  <td width=92 style='width:69.1pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.70</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.71</span></p>
  </td>
  <td width=92 style='width:69.15pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.72</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.72</span></p>
  </td>
 </tr>
 <tr>
  <td width=184 style='width:138.25pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>RoBERTa</span></p>
  </td>
  <td width=92 style='width:69.1pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.68</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.67</span></p>
  </td>
  <td width=92 style='width:69.15pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.71</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.71</span></p>
  </td>
 </tr>
 <tr>
  <td width=184 style='width:138.25pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>SciBERT</span></p>
  </td>
  <td width=92 style='width:69.1pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.70</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.71</span></p>
  </td>
  <td width=92 style='width:69.15pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.73</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.74</span></p>
  </td>
 </tr>
 <tr>
  <td width=184 style='width:138.25pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>XLNet</span></p>
  </td>
  <td width=92 style='width:69.1pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.62</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.62</span></p>
  </td>
  <td width=92 style='width:69.15pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.69</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.71</span></p>
  </td>
 </tr>
 <tr>
  <td width=184 style='width:138.25pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>AlBERT</span></p>
  </td>
  <td width=92 style='width:69.1pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.52</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.54</span></p>
  </td>
  <td width=92 style='width:69.15pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.64</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.64</span></p>
  </td>
 </tr>
 <tr>
  <td width=184 style='width:138.25pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>Ours-BERT</span></p>
  </td>
  <td width=92 style='width:69.1pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>-</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>-</span></p>
  </td>
  <td width=92 style='width:69.15pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.81</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.82</span></p>
  </td>
 </tr>
 <tr>
  <td width=184 style='width:138.25pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>Ours- RoBERTa</span></p>
  </td>
  <td width=92 style='width:69.1pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>-</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>-</span></p>
  </td>
  <td width=92 style='width:69.15pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.78</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.79</span></p>
  </td>
 </tr>
 <tr>
  <td width=184 style='width:138.25pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>Ours- SciBERT</span></p>
  </td>
  <td width=92 style='width:69.1pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>-</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>-</span></p>
  </td>
  <td width=92 style='width:69.15pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=EN-US style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.83</span></b></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><b><span
  lang=EN-US style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.84</span></b></p>
  </td>
 </tr>
 <tr>
  <td width=184 style='width:138.25pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>Ours- XLNet</span></p>
  </td>
  <td width=92 style='width:69.1pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>-</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>-</span></p>
  </td>
  <td width=92 style='width:69.15pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.78</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.79</span></p>
  </td>
 </tr>
 <tr>
  <td width=184 style='width:138.25pt;border:solid windowtext 1.0pt;border-top:
  none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>Ours- AlBERT</span></p>
  </td>
  <td width=92 style='width:69.1pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>-</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>-</span></p>
  </td>
  <td width=92 style='width:69.15pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.76</span></p>
  </td>
  <td width=92 style='width:69.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:12.0pt;font-family:"Times New Roman",serif'>0.77</span></p>
  </td>
 </tr>
</table>

</div>


## Case study

We conduct a case study for different input and our method.
![case_study](https://github.com/njust-winchy/originality_predict/assets/108659065/9bec6ec3-482c-4ad4-9f76-bce0ddb8f731)

## Dependency packages
System environment is set up according to the following configuration:
- transformers==4.16.2
- nltk==3.6.7
- matplotlib==3.5.1
- scikit-learn==1.1.3
- pytorch 2.0.1
- tqdm 4.65.0
- numpy 1.24.1

## Acknowledgement

We express our gratitude to the team at openreview.net for their dedication to advancing transparency and openness in scientific communication. We utilized the aspect identifying tool developed by Yuan et al.（2022）(https://github.com/neulab/ReviewAdvisor).

>Yuan, W., Liu, P., & Neubig, G. (2022). Can we automate scientific reviewing?. Journal of Artificial Intelligence Research, 75, 171-212.<br>


## Citation
Please cite the following paper if you use this code and dataset in your work.
    
>Wenqing Wu, Chengzhi Zhang\*, Yi Zhao. (2024). Automated Academic Paper Evaluation: A Collaborative Approach Integrating Human Expertise and Large Language Models. ***Journal of the Association for Information Science and Technology***.（submitted)  [[Dataset & Source Code]](https://github.com/njust-winchy/originality_predict/)) 
