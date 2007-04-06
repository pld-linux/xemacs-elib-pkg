Summary:	Portable Emacs Lisp utilities library
Summary(pl.UTF-8):	Przenośna biblioteka narzędzi Emacs Lisp
Name:		xemacs-elib-pkg
%define 	srcname	elib
Version:	1.11
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	914b735704c60f7d534398025ae725db
Patch0:		%{name}-info.patch
URL:		http://www.xemacs.org/
BuildRequires:	texinfo
Requires:	xemacs
Conflicts:	xemacs-sumo
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Portable Emacs Lisp utilities library.

%description -l pl.UTF-8
Przenośna biblioteka narzędzi Emacs Lisp.

%prep
%setup -q -c
%patch0 -p1

%build
cd man/elib
awk '/^\\input texinfo/ {print FILENAME}' * | xargs makeinfo

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xemacs-packages,%{_infodir}}

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
mv -f  $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info/*.info* $RPM_BUILD_ROOT%{_infodir}
rm -fr $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -fr $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc lisp/elib/README lisp/elib/NEWS lisp/elib/ChangeLog
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
%{_infodir}/*.info*
