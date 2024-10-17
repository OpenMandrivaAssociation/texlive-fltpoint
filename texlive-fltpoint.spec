Name:		texlive-fltpoint
Version:	56594
Release:	2
Summary:	Simple floating point arithmetic
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fltpoint
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fltpoint.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fltpoint.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fltpoint.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides simple floating point operations
(addition, subtraction, multiplication, division and rounding).
Used, for example, by rccol.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
