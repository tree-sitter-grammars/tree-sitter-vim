# Tree-sitter-vim

A tree-sitter parser for Vimscript.

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

[packer.nvim](https://github.com/wbthomason/packer.nvim):
```lua
use {'neovim/tree-sitter-vim', run = 'make' }
```
