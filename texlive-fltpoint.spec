%global tl_name fltpoint
%global tl_revision 56594

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1b
Release:	%{tl_revision}.1
Summary:	Simple floating point arithmetic
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/fltpoint
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fltpoint.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fltpoint.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fltpoint.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides simple floating point operations (addition,
subtraction, multiplication, division and rounding). Used, for example,
by rccol.

