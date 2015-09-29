APP = cassandra
BUILD_NUMBER ?= 1

PWD = $(shell pwd)
TOPDIR = $(PWD)/tmp
OUTPUTDIR = noarch

SELINUX_MAKEFILE = /usr/share/selinux/devel/Makefile


all: build

rpm: build
	rpmbuild -v -bb \
			--define "_sourcedir $(PWD)" \
			--define "_rpmdir $(PWD)" \
			--define "_topdir $(TOPDIR)" \
			--define "build_number $(BUILD_NUMBER)" \
			$(APP)-selinux.spec
	mv $(OUTPUTDIR)/*.rpm .

build: $(APP).pp

$(APP).pp: $(APP).fc $(APP).if $(APP).te
	make -f $(SELINUX_MAKEFILE)

clean:
	make -f $(SELINUX_MAKEFILE) clean
	rm -rf $(TOPDIR)
	rm -fr $(OUTPUTDIR)
	rm -f *.rpm
