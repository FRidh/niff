# niff

`niff` is a script that compares two Nix expressions and determines which attributes changed.

- `niff diff` compares `expr` to `--against`
- `niff path` returns a local path to `expr`
- `niff pr` determines a diff between the head of the PR and the base of the PR.

Furthermore, `diff` and `pr` have an `--output` argument for controlling the format of the output:
- `--output=list` is the default and produces a list of attribute names
- `--output=attrs` produces a single string that prepends `-A` for each attribute name, thereby making it easy to use for `nix-build`


## Examples

## `diff`

Check one remote archive against another:

```
niff diff https://github.com/NixOS/nixpkgs/archive/master.zip https://github.com/NixOS/nixpkgs-channels/archive/nixos-unstable.tar.gz
```

Check a PR against a remote archive (note that the hashtag needs to be escaped):

```
niff diff pr://28167 https://github.com/NixOS/nixpkgs/archive/master.zip
```

Check a PR against a local expression:

```
niff diff pr://28167 ../nixpkgs
```

Instead of generating a list of attributes its possible to output them together with `-A`

```
niff diff pr://28167 ../nixpkgs` --output attrs
```

## `pr`

To check a PR (note that with `niff pr` the scheme is not necessary):

```
niff pr 28167
```


## `path`

To get a local path to the `HEAD` of a PR:

```
niff path pr://28167
```

To get a local path to a `NIX_PATH` prefix:

```
niff path nixpath://nixpkgs
```

## How does it work?

1. Fetch archives with `nix-prefetch-url --unpack` and keep the store path, or use a given path to local Nix expression
2. Run `nix-env -qaP` to determine a list of attributes that are provided
3. Compare lists of each expression and output

## Arguments

Valid arguments are

- an url, e.g. `https://https://github.com/NixOS/nixpkgs/archive/master.zip`.
- a local or absolute path, e.g. `../path/to/nixpkgs`. Maps to `file:///abs/path/to/nixpkgs`.

## Available schemes

General schemes.

| Scheme      | Example                                               | Explanation                  |
| ----------- | ------------------------------------------------------| ---------------------------- |
| `file://`   | `file:///abs/path/to/expression`                      | Local expression or archive  |
| `https://`  | `https://github.com/NixOS/nixpkgs/archive/master.zip` | Remote archive               |
| `nixpath://`| `nixpath://nixpkgs`                                   | `NIX_PATH` prefix            |
| `github://` | `github://org/repo/ref`                               | GitHub reference             |

Nixpkgs-specific.

| Scheme      | Example                                                | Explanation                 |
| ------------| -------------------------------------------------------| --------------------------- |
| `channel://`| `channel:///nixos-unstable`                            | Nixpkgs channel             |
| `ref://`    | `ref://staging`                                        | Reference in `nixpkgs` repo |
| `pr://`     | `pr://28032`                                           | Nixpkgs pull request        |

