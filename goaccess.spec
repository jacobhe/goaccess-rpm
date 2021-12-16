Name:		goaccess
Version:	1.5.3
Release:	0
Summary:	Apache Log Analyzer	

Group:		Applications/Utilities

License:        GPLv2
URL:            http://goaccess.io 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source:  	http://tar.goaccess.io/goaccess-%{version}.tar.gz

BuildRequires:	glib2-devel
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRequires:	geoip-devel
BuildRequires:	tokyocabinet-devel

%description
An open source real-time web log analyzer and interactive viewer that runs in a terminal in *nix systems. It provides fast and valuable HTTP statistics for system administrators that require a visual server report on the fly.

%prep
%setup -q

%build
%configure --enable-utf8 --enable-geoip=mmdb
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc COPYING README AUTHORS TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}/browsers.list
%config(noreplace) %{_sysconfdir}/%{name}/podcast.list
%{_datarootdir}/locale/de/LC_MESSAGES/goaccess.mo
%{_datarootdir}/locale/es/LC_MESSAGES/goaccess.mo
%{_datarootdir}/locale/fr/LC_MESSAGES/goaccess.mo
%{_datarootdir}/locale/it/LC_MESSAGES/goaccess.mo
%{_datarootdir}/locale/ja/LC_MESSAGES/goaccess.mo
%{_datarootdir}/locale/pt_BR/LC_MESSAGES/goaccess.mo
%{_datarootdir}/locale/ru/LC_MESSAGES/goaccess.mo
%{_datarootdir}/locale/sv/LC_MESSAGES/goaccess.mo
%{_datarootdir}/locale/uk/LC_MESSAGES/goaccess.mo
%{_datarootdir}/locale/zh_CN/LC_MESSAGES/goaccess.mo

%changelog
* Thu Dec 16 2021 Jacob He <koven2045@hotmail.com> - 1.5.3
- Update to 1.5.3
* Mon Apr 24 2017 Chris Collins <collins.christopher@gmail.com> - 1.2
- Initial packaging
