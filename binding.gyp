{
    "target_defaults": {
        "include_dirs": [
            "C:\\Program Files (x86)\\Windows Kits\\10\\Include\\10.0.17763.0\\ucrt"
        ],
    },
    "targets": [
        {
            "target_name": "jtalkdll",
            "type": "static_library",
            "dependencies": [
                "openjtalk",
                "portaudio_static_x64",
            ],
            "sources": [
                "jtalk/jtalk.c",
            ],
            "include_dirs": [
                "jtalk",
                "portaudio/include",
                "open_jtalk-1.10/bin"
            ],
            'link_settings': {
                "libraries": [
                    "-lC:\\Program Files (x86)\\Windows Kits\\10\\Lib\\10.0.17763.0\\ucrt\\x64\\libucrt.lib"
                ],
            },
        },
        {
            "target_name": "jsay",
            "type": "executable",
            "dependencies": [
                "jtalkdll",
                "portaudio_static_x64"
            ],
            "sources": [
                "jtalk/jsay.c",
            ],
            "include_dirs": [
                "jtalk",
            ],
            'msvs_settings': {
                'VCLinkerTool': {
                    'IgnoreDefaultLibraryNames':['msvcrt.lib'],
                }
            },
            'link_settings': {
                "libraries": [
                    "-lC:\\Program Files (x86)\\Windows Kits\\10\\Lib\\10.0.17763.0\\ucrt\\x64\\ucrt.lib"
                ],
            },
        },
        {
            "target_name": "portaudio_static_x64",
            "type": "static_library",
            "sources": [
                "portaudio/src/common/pa_allocation.c",
                "portaudio/src/common/pa_converters.c",
                "portaudio/src/common/pa_cpuload.c",
                "portaudio/src/common/pa_debugprint.c",
                "portaudio/src/common/pa_dither.c",
                "portaudio/src/common/pa_front.c",
                "portaudio/src/common/pa_process.c",
                "portaudio/src/common/pa_ringbuffer.c",
                "portaudio/src/common/pa_stream.c",
                "portaudio/src/common/pa_trace.c",
                "portaudio/src/os/win/pa_win_hostapis.c",
                "portaudio/src/os/win/pa_win_util.c",
                "portaudio/src/os/win/pa_win_waveformat.c",
                "portaudio/src/os/win/pa_win_wdmks_utils.c",
                "portaudio/src/os/win/pa_win_coinitialize.c",
                "portaudio/src/os/win/pa_x86_plain_converters.c",
            ],
            "include_dirs": [
                "portaudio/include",
                "portaudio/src/common",
                "portaudio/src/os/win"
            ],
            'link_settings': {
                "libraries": [
                    "-lC:\\Program Files (x86)\\Windows Kits\\10\\Lib\\10.0.17763.0\\ucrt\\x64\\libucrt.lib"
                ],
            },
            'defines': [
            ]
        },
        {
            "target_name": "hts_engine_API",
            "type": "static_library",
            "sources": [
                "hts_engine_API-1.10/lib/HTS_hidden.h",
                "hts_engine_API-1.10/lib/HTS_audio.c",
                "hts_engine_API-1.10/lib/HTS_model.c",
                "hts_engine_API-1.10/lib/HTS_engine.c",
                "hts_engine_API-1.10/lib/HTS_pstream.c",
                "hts_engine_API-1.10/lib/HTS_gstream.c",
                "hts_engine_API-1.10/lib/HTS_sstream.c",
                "hts_engine_API-1.10/lib/HTS_label.c",
                "hts_engine_API-1.10/lib/HTS_vocoder.c",
                "hts_engine_API-1.10/lib/HTS_misc.c",
            ],
            "include_dirs": [
                "hts_engine_API-1.10/include",
                "hts_engine_API-1.10/lib",
            ],
            'link_settings': {
                "libraries": [
                    "-lwinmm.lib",
                    "-lC:\\Program Files (x86)\\Windows Kits\\10\\Lib\\10.0.17763.0\\ucrt\\x64\\libucrt.lib"
                ],
            },
            'defines': [
                "DCHARSET_UTF_8",
                "ASCII_HEADER",
            ]
        },
        {
            "target_name": "openjtalk",
            'type': "static_library",
            "include_dirs": [
                "portaudio/include",
                "open_jtalk-1.10/bin",
                "open_jtalk-1.10/mecab/src",
                "open_jtalk-1.10/text2mecab",
                "open_jtalk-1.10/mecab2njd",
                "open_jtalk-1.10/njd",
                "open_jtalk-1.10/njd_set_pronunciation",
                "open_jtalk-1.10/njd_set_digit",
                "open_jtalk-1.10/njd_set_accent_phrase",
                "open_jtalk-1.10/njd_set_accent_type",
                "open_jtalk-1.10/njd_set_unvoiced_vowel",
                "open_jtalk-1.10/njd_set_long_vowel",
                "open_jtalk-1.10/njd2jpcommon",
                "open_jtalk-1.10/jpcommon",
                "hts_engine_API-1.10/include",
            ],
            'link_settings': {
                "libraries": [
                    "-lwinmm.lib",
                    "-lC:\\Program Files (x86)\\Windows Kits\\10\\Lib\\10.0.17763.0\\ucrt\\x64\\ucrt.lib",
                ],
            },
            "dependencies": [
                "mecab",
                "njd",
                "jpcommon",
                "hts_engine_API",
                "text2mecab",
                "mecab2njd",
                "njd_set_pronunciation",
                "njd_set_digit",
                "njd_set_accent_phrase",
                "njd_set_accent_type",
                "njd_set_unvoiced_vowel",
                "njd_set_long_vowel",
                "njd2jpcommon",
            ],
            'msvs_settings': {
                'VCLinkerTool': {
                    'IgnoreDefaultLibraryNames':['msvcrt.lib'],
                }
            },
            "sources": [
                #"open_jtalk-1.10/bin/open_jtalk.c",
                "open_jtalk-1.10/bin/openjtalk.c",
            ],
            'defines': [
                "CHARSET_UTF_8",
                "ASCII_HEADER",
            ]
        },
        {
            "target_name": "mecab",
            "type": "static_library",
            "sources": [
                "open_jtalk-1.10/mecab/src/char_property.cpp",
                "open_jtalk-1.10/mecab/src/connector.cpp",
                "open_jtalk-1.10/mecab/src/context_id.cpp",
                "open_jtalk-1.10/mecab/src/dictionary.cpp",
                "open_jtalk-1.10/mecab/src/dictionary_compiler.cpp",
                "open_jtalk-1.10/mecab/src/dictionary_generator.cpp",
                "open_jtalk-1.10/mecab/src/dictionary_rewriter.cpp",
                "open_jtalk-1.10/mecab/src/eval.cpp",
                "open_jtalk-1.10/mecab/src/feature_index.cpp",
                "open_jtalk-1.10/mecab/src/iconv_utils.cpp",
                "open_jtalk-1.10/mecab/src/lbfgs.cpp",
                "open_jtalk-1.10/mecab/src/learner.cpp",
                "open_jtalk-1.10/mecab/src/learner_tagger.cpp",
                "open_jtalk-1.10/mecab/src/libmecab.cpp",
                "open_jtalk-1.10/mecab/src/mecab.cpp",
                "open_jtalk-1.10/mecab/src/nbest_generator.cpp",
                "open_jtalk-1.10/mecab/src/param.cpp",
                "open_jtalk-1.10/mecab/src/string_buffer.cpp",
                "open_jtalk-1.10/mecab/src/tagger.cpp",
                "open_jtalk-1.10/mecab/src/tokenizer.cpp",
                "open_jtalk-1.10/mecab/src/utils.cpp",
                "open_jtalk-1.10/mecab/src/viterbi.cpp",
                "open_jtalk-1.10/mecab/src/writer.cpp",
            ],
            "include_dirs": [
                "open_jtalk-1.10/mecab",
                "open_jtalk-1.10/mecab/src",
            ],
            'link_settings': {
                "libraries": [
                    "-lC:\\Program Files (x86)\\Windows Kits\\10\\Lib\\10.0.17763.0\\ucrt\\x64\\ucrt.lib"
                ],
            },
            'msbuild_settings': {
                "ClCompile": {
                    'CompileAs': 'CompileAsCpp',
                }
            },
            'msvs_settings': {
                'VCCLCompilerTool': {
                    'ExceptionHandling': '1', # /EHsc
                }
            },
            'defines': [
                "HAVE_WINDOWS_H",
                "ASCII_HEADER",
                "DIC_VERSION=102",
                "MECAB_USE_UTF8_ONLY",
                "CHARSET_UTF_8",
                "MECAB_WITHOUT_MUTEX_LOCK",
                "MECAB_DEFAULT_RC=\"dummy\"",
                "PACKAGE=\"\\\"open_jtalk\\\"\"",
                "VERSION=\"\\\"1.10\\\"\"",
            ],
        },
        {
            "target_name": "text2mecab",
            "type": "static_library",
            "include_dirs": [
                "open_jtalk-1.10/text2mecab",
            ],
            "sources": [
                "open_jtalk-1.10/text2mecab/text2mecab.c",
            ],
            'link_settings': {
                "libraries": [
                    "-lC:\\Program Files (x86)\\Windows Kits\\10\\Lib\\10.0.17763.0\\ucrt\\x64\\libucrt.lib"
                ],
            },
            'defines': [
                "CHARSET_UTF_8",
                "ASCII_HEADER",
            ]
        },
        {
            "target_name": "njd",
            "type": "static_library",
            "include_dirs": [
                "open_jtalk-1.10/njd",
            ],
            'link_settings': {
                "libraries": [
                    "-lC:\\Program Files (x86)\\Windows Kits\\10\\Lib\\10.0.17763.0\\ucrt\\x64\\libucrt.lib"
                ],
            },
            "sources": [
                "open_jtalk-1.10/njd/njd.c",
                "open_jtalk-1.10/njd/njd_node.c",
            ],
            'defines': [
                "CHARSET_UTF_8",
                "ASCII_HEADER",
            ]
        },
        {
            "target_name": "mecab2njd",
            "type": "static_library",
            "include_dirs": [
                "open_jtalk-1.10/njd",
                "open_jtalk-1.10/mecab2njd",
            ],
            'link_settings': {
                "libraries": [
                    "-lC:\\Program Files (x86)\\Windows Kits\\10\\Lib\\10.0.17763.0\\ucrt\\x64\\libucrt.lib"
                ],
            },
            "dependencies": [
                "njd"
            ],
            "sources": [
                "open_jtalk-1.10/mecab2njd/mecab2njd.c",
            ],
            'defines': [
                "CHARSET_UTF_8",
                "ASCII_HEADER",
            ]
        },
        {
            "target_name": "njd_set_pronunciation",
            "type": "static_library",
            "include_dirs": [
                "open_jtalk-1.10/njd",
                "open_jtalk-1.10/njd_set_pronunciation",
            ],
            'link_settings': {
                "libraries": [
                    "-lC:\\Program Files (x86)\\Windows Kits\\10\\Lib\\10.0.17763.0\\ucrt\\x64\\libucrt.lib"
                ],
            },
            "dependencies": [
                "njd"
            ],
            "sources": [
                "open_jtalk-1.10/njd_set_pronunciation/njd_set_pronunciation.c",
            ],
            'defines': [
                "CHARSET_UTF_8",
                "ASCII_HEADER",
            ]
        },
        {
            "target_name": "njd_set_digit",
            "type": "static_library",
            "include_dirs": [
                "open_jtalk-1.10/njd",
                "open_jtalk-1.10/njd_set_digit",
            ],
            'link_settings': {
                "libraries": [
                    "-lC:\\Program Files (x86)\\Windows Kits\\10\\Lib\\10.0.17763.0\\ucrt\\x64\\libucrt.lib"
                ],
            },
            "dependencies": [
                "njd"
            ],
            "sources": [
                "open_jtalk-1.10/njd_set_digit/njd_set_digit.c",
            ],
            'defines': [
                "CHARSET_UTF_8",
                "ASCII_HEADER",
            ]
        },
        {
            "target_name": "njd_set_accent_phrase",
            "type": "static_library",
            "include_dirs": [
                "open_jtalk-1.10/njd",
                "open_jtalk-1.10/njd_set_accent_phrase",
            ],
            'link_settings': {
                "libraries": [
                    "-lC:\\Program Files (x86)\\Windows Kits\\10\\Lib\\10.0.17763.0\\ucrt\\x64\\libucrt.lib"
                ],
            },
            "dependencies": [
                "njd"
            ],
            "sources": [
                "open_jtalk-1.10/njd_set_accent_phrase/njd_set_accent_phrase.c",
            ],
            'defines': [
                "CHARSET_UTF_8",
                "ASCII_HEADER",
            ]
        },
        {
            "target_name": "njd_set_accent_type",
            "type": "static_library",
            "include_dirs": [
                "open_jtalk-1.10/njd",
                "open_jtalk-1.10/njd_set_accent_type",
            ],
            'link_settings': {
                "libraries": [
                    "-lC:\\Program Files (x86)\\Windows Kits\\10\\Lib\\10.0.17763.0\\ucrt\\x64\\libucrt.lib"
                ],
            },
            "dependencies": [
                "njd"
            ],
            "sources": [
                "open_jtalk-1.10/njd_set_accent_type/njd_set_accent_type.c",
            ],
            'defines': [
                "CHARSET_UTF_8",
                "ASCII_HEADER",
            ]
        },
        {
            "target_name": "njd_set_unvoiced_vowel",
            "type": "static_library",
            "include_dirs": [
                "open_jtalk-1.10/njd",
                "open_jtalk-1.10/njd_set_unvoiced_vowel",
            ],
            'link_settings': {
                "libraries": [
                    "-lC:\\Program Files (x86)\\Windows Kits\\10\\Lib\\10.0.17763.0\\ucrt\\x64\\libucrt.lib"
                ],
            },
            "dependencies": [
                "njd"
            ],
            "sources": [
                "open_jtalk-1.10/njd_set_unvoiced_vowel/njd_set_unvoiced_vowel.c",
            ],
            'defines': [
                "CHARSET_UTF_8",
                "ASCII_HEADER",
            ]
        },
        {
            "target_name": "njd_set_long_vowel",
            "type": "static_library",
            "include_dirs": [
                "open_jtalk-1.10/njd",
                "open_jtalk-1.10/njd_set_long_vowel",
            ],
            'link_settings': {
                "libraries": [
                    "-lC:\\Program Files (x86)\\Windows Kits\\10\\Lib\\10.0.17763.0\\ucrt\\x64\\libucrt.lib"
                ],
            },
            "dependencies": [
                "njd"
            ],
            "sources": [
                "open_jtalk-1.10/njd_set_long_vowel/njd_set_long_vowel.c",
            ],
            'defines': [
                "CHARSET_UTF_8",
                "ASCII_HEADER",
            ]
        },
        {
            "target_name": "njd2jpcommon",
            "type": "static_library",
            "include_dirs": [
                "open_jtalk-1.10/njd",
                "open_jtalk-1.10/jpcommon",
                "open_jtalk-1.10/njd2jpcommon",
            ],
            'link_settings': {
                "libraries": [
                    "-lC:\\Program Files (x86)\\Windows Kits\\10\\Lib\\10.0.17763.0\\ucrt\\x64\\libucrt.lib"
                ],
            },
            "dependencies": [
                "jpcommon",
                "njd"
            ],
            "sources": [
                "open_jtalk-1.10/njd2jpcommon/njd2jpcommon.c",
            ],
            'defines': [
                "CHARSET_UTF_8",
                "ASCII_HEADER",
            ]
        },
        {
            "target_name": "jpcommon",
            "type": "static_library",
            "include_dirs": [
                "open_jtalk-1.10/njd",
                "open_jtalk-1.10/jpcommon",
            ],
            'link_settings': {
                "libraries": [
                    "-lC:\\Program Files (x86)\\Windows Kits\\10\\Lib\\10.0.17763.0\\ucrt\\x64\\libucrt.lib"
                ],
            },
            "dependencies": [
                "njd"
            ],
            "sources": [
                "open_jtalk-1.10/jpcommon/jpcommon.c",
                "open_jtalk-1.10/jpcommon/jpcommon_node.c",
                "open_jtalk-1.10/jpcommon/jpcommon_label.c",
            ],
            'defines': [
                "CHARSET_UTF_8",
                "ASCII_HEADER",
            ]
        },
    ]
}
