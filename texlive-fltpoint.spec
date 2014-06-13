# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/fltpoint
# catalog-date 2008-04-20 19:53:04 +0200
# catalog-license other-free
# catalog-version 1.1b
Name:		texlive-fltpoint
Version:	1.1b
Release:	7
Summary:	Simple floating point arithmetic
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fltpoint
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fltpoint.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fltpoint.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fltpoint.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1b-2
+ Revision: 751981
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1b-1
+ Revision: 718466
- texlive-fltpoint
- texlive-fltpoint
- texlive-fltpoint
- texlive-fltpoint

