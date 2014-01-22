%define		_rc	rc30.79
%define		plugin	layout
Summary:	UI Layout - The Ultimate Page Layout Manager
Name:		jquery-%{plugin}
Version:	1.3.0
Release:	1.%{_rc}
License:	MIT/GPL
Group:		Applications/WWW
Source0:	http://layout.jquery-dev.net/lib/js/jquery.layout-latest.js?/%{plugin}-%{version}-%{_rc}.js
# Source0-md5:	3fb7ea96b3950ad6b475c57c108662cb
Source1:	http://layout.jquery-dev.net/lib/js/jquery.layout-latest.min.js?/%{plugin}-%{version}-%{_rc}.min.js
# Source1-md5:	e11b6855cbbaf72b3f1d1f8e71800ca5
URL:		http://layout.jquery-dev.net/
BuildRequires:	unzip
Requires:	jquery
Requires:	jquery-ui
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
This plug-in was inspired by the extJS border-layout, and recreates
that functionality as a jQuery plug-in. The UI Layout plug-in can
create any UI look you want - from simple headers or sidebars, to a
complex application with toolbars, menus, help-panels, status bars,
sub-forms, etc.

Combined it with other jQuery UI widgets to create a sophisticated
application. There are no limitations or issues - this widget is ready
for production use. All feedback and requests are welcome as
development is ongoing. If you create a good looking application using
UI Layout, please let us know.

%package demo
Summary:	Demo for jQuery.%{plugin}
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu jQuery.%{plugin}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for jQuery.%{plugin}.

%prep
%setup -qcT

cp -p %{SOURCE0} jquery.%{plugin}.js
cp -p %{SOURCE1} jquery.%{plugin}.min.js

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}

cp -p jquery.%{plugin}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js
cp -p jquery.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.src.js
ln -s %{plugin}-%{version}.src.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js

%if 0
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p *.html $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc changelog.txt
%{_appdir}

%if 0
%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
%endif
