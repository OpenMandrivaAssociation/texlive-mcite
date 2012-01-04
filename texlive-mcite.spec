# revision 18173
# category Package
# catalog-ctan /macros/latex/contrib/mcite
# catalog-date 2007-01-09 22:36:10 +0100
# catalog-license gpl
# catalog-version 1.6
Name:		texlive-mcite
Version:	1.6
Release:	2
Summary:	Multiple items in a single citation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mcite
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mcite.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mcite.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mcite.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The mcite package allows the user to collapse multiple
citations into one, as is customary in physics journals. The
package requires a customised BibTeX style for its work; the
documentation explains how to do that customisation.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mcite/mcite.sty
%doc %{_texmfdistdir}/doc/latex/mcite/COPYING
%doc %{_texmfdistdir}/doc/latex/mcite/README
%doc %{_texmfdistdir}/doc/latex/mcite/mcite.bib
%doc %{_texmfdistdir}/doc/latex/mcite/mcite.pdf
#- source
%doc %{_texmfdistdir}/source/latex/mcite/Makefile
%doc %{_texmfdistdir}/source/latex/mcite/mcite.drv
%doc %{_texmfdistdir}/source/latex/mcite/mcite.dtx
%doc %{_texmfdistdir}/source/latex/mcite/mcite.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
