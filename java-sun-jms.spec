Summary:	Java Message Service
Name:		jms
Version:	1.0.2b
Release:	1
License:	Sun Microsystems, Inc. Binary Code License
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Source0:	jms-1_0_2b.zip
URL:		http://java.sun.com/products/jms
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
Java Message Service

%package doc
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Summary:	Java Message Service documentation

%description doc
Java Message Service documentation

%prep
%setup -q -n jms1.0.2b

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_javalibdir}
cp lib/*.jar $RPM_BUILD_ROOT/%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_javalibdir}
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc doc/api
