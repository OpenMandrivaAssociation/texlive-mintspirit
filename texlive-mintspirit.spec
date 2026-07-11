%global tl_name mintspirit
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LaTeX support for MintSpirit font families
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/mintspirit
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mintspirit.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mintspirit.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX support for
the MintSpirit and MintSpiritNo2 families of fonts, designed by Hirwen
Harendal. MintSpirit was originally designed for use as a system font on
a Linux Mint system. The No. 2 variant provides more conventional shapes
for some glyphs.

