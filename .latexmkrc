$pdf_mode = 4; $aux_dir = "build";

$lualatex = "lualatex %O '". ($ENV{"METADATA"} ? "\\def\\metadata{1}" : "") . "\\input{%S}'";

add_cus_dep("glo", "gls", 0, "makeglossaries");
add_cus_dep("acn", "acr", 0, "makeglossaries");

@default_files = ("main.tex");

make_path("$aux_dir/$_") for grep { -d } @{[
    "chapters", "frontmatter",
    "chapters/01-mathematical_background",
    "chapters/02-time_evolution_in_quantum_mechanics",
    "chapters/03-mixed_quantum_classical_dynamics",
]};

sub makeglossaries {
    system("makeglossaries -d $aux_dir " . basename($_[0]));
}
