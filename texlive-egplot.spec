%global tl_name egplot
%global tl_revision 20617

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.02a
Release:	%{tl_revision}.1
Summary:	Encapsulate Gnuplot sources in LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/egplot
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/egplot.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/egplot.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/egplot.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package to encapsulate gnuplot commands in a LaTeX source file, so
that a document's figures are maintained in parallel with the document
source itself.

