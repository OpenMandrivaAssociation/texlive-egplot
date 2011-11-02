Name:		texlive-egplot
Version:	1.02a
Release:	1
Summary:	Encapsulate Gnuplot sources in LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/egplot
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/egplot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/egplot.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/egplot.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A package to encapsulate gnuplot commands in a LaTeX source
file, so that a document's figures are maintained in parallel
with the document source itself.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/egplot/egplot.sty
%doc %{_texmfdistdir}/doc/latex/egplot/egplot.README
%doc %{_texmfdistdir}/doc/latex/egplot/egplot.pdf
%doc %{_texmfdistdir}/doc/latex/egplot/manual.ps.gz
#- source
%doc %{_texmfdistdir}/source/latex/egplot/egplot.drv
%doc %{_texmfdistdir}/source/latex/egplot/egplot.dtx
%doc %{_texmfdistdir}/source/latex/egplot/egplot.ins
%doc %{_texmfdistdir}/source/latex/egplot/egpman.drv

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
