# Tree-sitter VimL parser

A parser for VimL using treesitter.

Any contribution is greatly appreciated, so please look [here](CONTRIBUTING.md) for more information.
__Don't forget that reporting and issue is already a contribution, and will greatly help, so please do report issues!__

## Building

To create `parser/vim.so` run:

```sh
make
```

## Installation

Add directly to `runtimepath`:

```lua
vim.opt.runtimepath:append('<path_to_repo>')
```

Alternatively use a plugin manager.

[packer.nvim]:
```lua
use {'neovim/tree-sitter-vim', run = 'make' }
```
