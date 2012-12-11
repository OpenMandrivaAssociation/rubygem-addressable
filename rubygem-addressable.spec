# Generated from addressable-2.2.4.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	addressable

Summary:	A replacement for the URI implementation of Ruby's standard library
Name:		rubygem-%{rbname}
Version:	2.2.8
Release:	1
Group:		Development/Ruby
License:	MIT
URL:		http://addressable.rubyforge.org/
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Addressable is a replacement for the URI implementation that is part of
Ruby's standard library. It more closely conforms to the relevant RFCs and
adds support for IRIs and URI templates.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f '(spec|tasks|website)/'

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/addressable
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/addressable/idna
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/addressable/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/addressable/idna/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/spec
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/spec/addressable
%{ruby_gemdir}/gems/%{rbname}-%{version}/spec/addressable/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/tasks
%{ruby_gemdir}/gems/%{rbname}-%{version}/tasks/*.rake
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/README.md
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/website
%{ruby_gemdir}/gems/%{rbname}-%{version}/website/*.html
