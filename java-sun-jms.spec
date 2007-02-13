Summary:	Java Message Service
Summary(pl.UTF-8):	Serwis komunikacyjny do Javy
Name:		jms
Version:	1.1
Release:	1
License:	restricted, non-distributable (Sun Binary Code License - see URL)
Group:		Development/Languages/Java
# download through forms from URL
Source0:	%{name}-1_1-fr-apidocs.zip
# NoSource0-md5: 11ca2cdc4706d02b372a17cbf33612f6
URL:		http://java.sun.com/products/jms/docs.html
NoSource:	0
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Java Message Service.

%description -l pl.UTF-8
Java Message Service - serwis komunikacyjny do Javy.

%package doc
Summary:	Java Message Service documentation
Summary(pl.UTF-8):	Dokumentacja do serwisu komunikacyjnego Javy
Group:		Development/Languages/Java

%description doc
Java Message Service documentation.

%description doc -l pl.UTF-8
Dokumentacja do JMS - serwisu komunikacyjnego do Javy.

%prep
%setup -q -n %{name}%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install lib/*.jar $RPM_BUILD_ROOT%{_javadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc doc/api
