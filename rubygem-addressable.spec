# Generated from addressable-2.2.4.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	addressable

Summary:	A replacement for the URI implementation of Ruby's standard library
Name:		rubygem-%{rbname}
Version:	2.2.8
Release:	2
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
%dir %{gem_dir}/gems/%{rbname}-%{version}
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/addressable
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/addressable/idna
%{gem_dir}/gems/%{rbname}-%{version}/lib/addressable/*.rb
%{gem_dir}/gems/%{rbname}-%{version}/lib/addressable/idna/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/spec
%dir %{gem_dir}/gems/%{rbname}-%{version}/spec/addressable
%{gem_dir}/gems/%{rbname}-%{version}/spec/addressable/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/tasks
%{gem_dir}/gems/%{rbname}-%{version}/tasks/*.rake
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{gem_dir}/doc/%{rbname}-%{version}
%doc %{gem_dir}/gems/%{rbname}-%{version}/README.md
%dir %{gem_dir}/gems/%{rbname}-%{version}/website
%{gem_dir}/gems/%{rbname}-%{version}/website/*.html
