.PHONY: all

# where place files
PREFIX := $(shell echo $(PREFIX))

# custom shebang
BASH_SHEBANG := $(shell echo $(BASH_SHEBANG))
BASH_DEFAULT := $(shell command -v bash 2>&1)

# install command
INSTALL := install

# place for tmp files
BUILD_DIR := build_src

# what scripts install/uninstall
BASH_TARGET := pirx pirx-fotodater

all:
	@printf "usage:\tmake install\n"
	@printf "\tmake uninstall\n"

aa:
	for target in $(BASH_TARGET); do \
		echo $$target; \
	done

install: check-install
	mkdir -p $(BUILD_DIR)
	for target in $(BASH_TARGET); do \
		sed '1,1 s:#!/bin/bash:#!$(BASH_SHEBANG):; 1,1 s:"::g' $$target > $(BUILD_DIR)/$$target.tmp; \
		$(INSTALL) -m 0755 -d $(PREFIX); \
		$(INSTALL) -m 0755 -p $(BUILD_DIR)/$$target.tmp $(PREFIX)/$$target; \
	done
	rm -rf $(BUILD_DIR)

uninstall: check-uninstall
	for target in $(BASH_TARGET); do \
		cd $(PREFIX) && rm -f $$target; \
	done

clean:
	rm -rf $(BUILD_DIR)

check-install:
ifndef PREFIX
  PREFIX := "/usr/local/bin"
endif
ifndef BASH_SHEBANG
  ifndef BASH_DEFAULT
    $(error "bash command not available")
  endif
  BASH_SHEBANG := $(BASH_DEFAULT)
endif

check-uninstall:
ifndef PREFIX
  PREFIX := "/usr/local/bin"
endif
