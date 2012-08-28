# Targets
TEX_NAME = Design_Patterns_In_Python

#==============================================================================
all: open
	@true

#==============================================================================
test: FRC
	@for program in *.py; \
        do \
          echo $$program; \
          ./$$program; \
          echo ""; \
        done

include $(DROPBOX)/Coding/MakeFiles/latex.mk
# override OUTPUT_NAME here
