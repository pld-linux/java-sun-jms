%define		srcname		sun-jms
Summary:	Java Message Service (JMS)
Summary(pl.UTF-8):	Serwis komunikacyjny do Javy
Name:		java-%{srcname}
Version:	1.1
Release:	1
License:	restricted, non-distributable (Sun Binary Code License - see URL)
Group:		Development/Languages/Java
# download through forms from URL
Source0:	%{name}-1_1-fr-apidocs.zip
# NoSource0-md5: 11ca2cdc4706d02b372a17cbf33612f6
NoSource:	0
URL:		http://java.sun.com/products/jms/docs.html
BuildRequires:	unzip
Requires:	jre
Provides:	java(jms) = %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Java Message Service (JMS) API is a messaging standard that allows
application components based on the Java 2 Platform, Enterprise
Edition (J2EE) to create, send, receive, and read messages. It enables
distributed communication that is loosely coupled, reliable, and
asynchronous.

%description -l pl.UTF-8
Java Message Service - serwis komunikacyjny do Javy.

%package javadoc
Summary:	Java Message Service documentation
Summary(pl.UTF-8):	Dokumentacja do serwisu komunikacyjnego Javy
Group:		Development/Languages/Java

%description javadoc
Java Message Service documentation.

%description javadoc -l pl.UTF-8
Dokumentacja do JMS - serwisu komunikacyjnego do Javy.

%prep
%setup -q -n jms%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
cp -a lib/*.jar $RPM_BUILD_ROOT%{_javadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%doc doc/api/*
