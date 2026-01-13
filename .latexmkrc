$pdf_mode = 4; $aux_dir = "build";

add_cus_dep("glo", "gls", 0, "makeglossaries");
add_cus_dep("acn", "acr", 0, "makeglossaries");

@default_files = ("main.tex");

make_path("$aux_dir/$_") for grep { -d } @{["chapters"]};

sub makeglossaries {
    system("makeglossaries -d $aux_dir " . basename($_[0]));
}
