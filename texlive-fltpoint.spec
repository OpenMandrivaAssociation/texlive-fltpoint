Name:		texlive-fltpoint
Version:	1.1b
Release:	1
Summary:	Simple floating point arithmetic
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fltpoint
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fltpoint.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fltpoint.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fltpoint.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides simple floating point operations
(addition, subtraction, multiplication, division and rounding).
Used, for example, by rccol.

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
%{_texmfdistdir}/tex/generic/fltpoint/deccomma.sty
%{_texmfdistdir}/tex/generic/fltpoint/fltpoint.sty
%{_texmfdistdir}/tex/generic/fltpoint/fltpoint.tex
%doc %{_texmfdistdir}/doc/generic/fltpoint/README
%doc %{_texmfdistdir}/doc/generic/fltpoint/fltpoint.pdf
#- source
%doc %{_texmfdistdir}/source/generic/fltpoint/fltpoint.dtx
%doc %{_texmfdistdir}/source/generic/fltpoint/fltpoint.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
