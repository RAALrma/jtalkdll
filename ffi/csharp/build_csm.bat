set jtalkcom=JTalkCOM64.dll
if "%VSCMD_ARG_HOST_ARCH%" == "x86" set jtalkcom=JTalkCOM32.dll
csc /platform:%VSCMD_ARG_HOST_ARCH% /target:winexe /reference:%jtalkcom% jtd_csm.cs