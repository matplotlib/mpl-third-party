pushd %~dp0

REM Minimal windows makefile for sphinx documentation


set SPHINXOPTS=
set SPHINXBUILD=python -msphinx
set SOURCEDIR=source
set BUILDDIR=build

if "%1" == "" goto help
if "%1" == "show" goto show

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:show
python -m webbrowser -t "%~dp0\build\html\index.html"

:end
