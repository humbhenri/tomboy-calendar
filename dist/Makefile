# Makefile for tomboy-calendar
#
# Humberto H. C. Pinheiro Sex, 11 Set 2009 10:18:14
#

SRCDIR=..
VER=0.1
FILES=$(SRCDIR)/calendar.py $(SRCDIR)/tomboy.py $(SRCDIR)/interface.glade $(SRCDIR)/*.png $(SRCDIR)/*.desktop $(SRCDIR)/calendar.gif
NAME=tomboy-calendar
RPMSRCDIR=/usr/src/packages/SOURCES
RPMSPECDIR=/usr/src/packages/SPECS

pack: $(FILES)
	mkdir $(NAME)-$(VER)
	cp $(FILES) $(NAME)-$(VER)
	tar czf $(NAME)-$(VER).tar.gz $(NAME)-$(VER)

rpm: $(NAME)-$(VER).tar.gz $(NAME).spec
	 mv $(NAME)-$(VER).tar.gz $(RPMSRCDIR)
	 cp $(NAME).spec $(RPMSPECDIR)
	 rpmbuild -ba $(RPMSPECDIR)/$(NAME).spec

