%global tl_name mcite
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6
Release:	%{tl_revision}.1
Summary:	Multiple items in a single citation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mcite
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mcite.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mcite.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mcite.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The mcite package allows the user to collapse multiple citations into
one, as is customary in physics journals. The package requires a
customised BibTeX style for its work; the documentation explains how to
do that customisation.

