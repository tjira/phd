all: tex

tex:
	@lualatex main && biber main && makeglossaries main && lualatex main && lualatex main
