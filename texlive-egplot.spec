Summary:	Encapsulate Gnuplot sources in LaTeX documents
Name:		texlive-egplot
Version:	20617
Release:	1
License:	GPL
Group:		Publishing
Url:		http://www.ctan.org/tex-archive/macros/latex/contrib/egplot
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/egplot.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/egplot.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/egplot.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package to encapsulate gnuplot commands in a LaTeX source
file, so that a document's figures are maintained in parallel
with the document source itself.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
