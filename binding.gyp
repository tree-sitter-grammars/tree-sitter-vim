{
  'targets': [
    {
      'target_name': 'tree_sitter_vim',
      'include_dirs': [
        'src',
      ],
      'sources': [
        'src/parser.c',
        'src/scanner.c',
      ],
      'cflags_c': [
        '-std=c11',
      ],
    },
  ],
}
