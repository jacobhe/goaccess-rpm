Name:		goaccess
Version:	0.8.5
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
%configure --enable-geoip
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc COPYING README AUTHORS TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_sysconfdir}/%{name}.conf

%changelog
* Wed Sep 25 2014 Chris Collins <collins.christopher@gmail.com> - 0.8.5
- Initial packaging
