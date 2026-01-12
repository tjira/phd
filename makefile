BUILD = build
MAIN  = main

all: tex

tex:
	@mkdir -p build && $(MAKE) lualatex && $(MAKE) biber && $(MAKE) makeglossaries && $(MAKE) lualatex && $(MAKE) lualatex && cp $(BUILD)/$(MAIN).pdf .

biber:
	@biber --output-directory=$(BUILD) $(MAIN)

lualatex:
	@lualatex --output-directory=$(BUILD) $(MAIN)

makeglossaries:
	@makeglossaries -d $(BUILD) $(MAIN)
