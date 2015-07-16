#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-cgi_multipart_eof_fix
Version  : 2.5.0
Release  : 1
URL      : https://rubygems.org/downloads/cgi_multipart_eof_fix-2.5.0.gem
Source0  : https://rubygems.org/downloads/cgi_multipart_eof_fix-2.5.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : Ruby
BuildRequires : ruby
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-test-unit

%description
cgi_multipart_eof_fix
Fix an exploitable bug in CGI multipart parsing.
== License

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n cgi_multipart_eof_fix-2.5.0
gem spec %{SOURCE0} -l --ruby > rubygem-cgi_multipart_eof_fix.gemspec

%build
gem build rubygem-cgi_multipart_eof_fix.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
cgi_multipart_eof_fix-2.5.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/cgi_multipart_eof_fix-2.5.0
ruby -v -I.:lib:test test*/test_*.rb
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/cgi_multipart_eof_fix-2.5.0.gem
/usr/lib64/ruby/gems/2.2.0/doc/cgi_multipart_eof_fix-2.5.0/ri/CGI/QueryExtension/body;/cdesc-body;.ri
/usr/lib64/ruby/gems/2.2.0/doc/cgi_multipart_eof_fix-2.5.0/ri/CGI/QueryExtension/cdesc-QueryExtension.ri
/usr/lib64/ruby/gems/2.2.0/doc/cgi_multipart_eof_fix-2.5.0/ri/CGI/QueryExtension/read_multipart-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/cgi_multipart_eof_fix-2.5.0/ri/CGI/cdesc-CGI.ri
/usr/lib64/ruby/gems/2.2.0/doc/cgi_multipart_eof_fix-2.5.0/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/gems/cgi_multipart_eof_fix-2.5.0/CHANGELOG
/usr/lib64/ruby/gems/2.2.0/gems/cgi_multipart_eof_fix-2.5.0/LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/cgi_multipart_eof_fix-2.5.0/Manifest
/usr/lib64/ruby/gems/2.2.0/gems/cgi_multipart_eof_fix-2.5.0/README
/usr/lib64/ruby/gems/2.2.0/gems/cgi_multipart_eof_fix-2.5.0/cgi_multipart_eof_fix.gemspec
/usr/lib64/ruby/gems/2.2.0/gems/cgi_multipart_eof_fix-2.5.0/lib/cgi_multipart_eof_fix.rb
/usr/lib64/ruby/gems/2.2.0/gems/cgi_multipart_eof_fix-2.5.0/test/test_cgi_multipart_eof_fix.rb
/usr/lib64/ruby/gems/2.2.0/specifications/cgi_multipart_eof_fix-2.5.0.gemspec
