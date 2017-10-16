# Installation

From the SPC repo directory, run:

```
# uninstall any previously installed mendel_go
./spc uninstall mendel_go

# Install
./spc install https://github.com/genetic-algorithms/mendel-go-spc/get/master.zip

# Create symlinks to mendel-go binary and defaults file
ln -s $MENDEL_GO_REPO/mendel-go ./src/spc_apps/mendel_go/mendel_go
ln -s $MENDEL_GO_REPO/mendel-defaults.ini ./src/spc_apps/mendel_go/mendel_go.toml
```
