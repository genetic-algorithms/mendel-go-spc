# Installation

From the SPC repo directory, run:

```
# Uninstall any previously installed mendel-go
./spc uninstall mendel-go

# Install
./spc install https://bitbucket.org/geneticentropy/mendel-go-spc/get/master.zip

# Create symlinks to mendel-go binary and defaults file
ln -s $MENDEL_GO_REPO/mendel-go ./apps/mendel-go/mendel-go
ln -s $MENDEL_GO_REPO/mendel-defaults.ini ./apps/mendel-go/mendel-defaults.ini
```
