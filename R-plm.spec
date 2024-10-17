%bcond_with bootstrap
%global packname  plm
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.3_1
Release:          2
Summary:          Linear Models for Panel Data
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.3-1.tar.gz
Requires:         R-stats R-bdsmatrix R-nlme R-Formula R-MASS R-sandwich
Requires:         R-lmtest R-car
%if %{without bootstrap}
Requires:         R-AER
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-stats R-bdsmatrix R-nlme R-Formula R-MASS R-sandwich
BuildRequires:    R-lmtest R-car
%if %{without bootstrap}
BuildRequires:    R-AER
%endif

%description
A set of estimators and tests for panel data.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
