import sys


def get_symbols_for(symbol_group, translation):
    if (
        translation == "latex"
        or translation == "mathml"
        or translation is None
    ):
        return {
            k: (
                v[translation]
                if translation == "latex" or translation == "mathml"
                else None
            )
            for k, v in getattr(sys.modules[__name__], symbol_group).items()
        }
    else:
        raise NotImplementedError


binary_functions = {
    '"frac"': {"latex": "\\frac", "mathml": "<mfrac>{}{}</mfrac>"},
    '"root"': {"latex": "\\sqrt", "mathml": "<mroot>{}{}</mroot>"},
    '"stackrel"': {"latex": "\\stackrel", "mathml": "<mover>{}{}</mover>"},
    '"overset"': {"latex": "\\overset", "mathml": "<mover>{}{}</mover>"},
    '"underset"': {"latex": "\\underset", "mathml": "<munder>{}{}</munder>"},
    '"color"': {
        "latex": "\\textcolor",
        "mathml": "<mstyle mathcolor='{}'><mrow><mi>{}</mi></mrow></mstyle>",
    },
}

unary_functions = {
    '"sqrt"': {"latex": "\\sqrt", "mathml": "<msqrt>{}</msqrt>"},
    '"text"': {"latex": "\\textrm", "mathml": "<mtext>{}</mtext>"},
    '"abs"': {"latex": "abs", "mathml": "<mo>|</mo>{}<mo>|</mo>"},
    '"floor"': {
        "latex": "floor",
        "mathml": "<mo>&#x230A;</mo>{}<mo>&#x230A;</mo>",
    },
    '"ceil"': {
        "latex": "ceil",
        "mathml": "<mo>&#x2308;</mo>{}<mo>&#x2308;</mo>",
    },
    '"norm"': {
        "latex": "norm",
        "mathml": "<mo>&#x2225;</mo>{}<mo>&#x2225;</mo>",
    },
    '"ubrace"': {
        "latex": "\\underbrace",
        "mathml": "<munder>{}<mo>&#x23DF;</mo></munder>",
    },
    '"underbrace"': {
        "latex": "\\underbrace",
        "mathml": "<munder>{}<mo>&#x23DF;</mo></munder>",
    },
    '"obrace"': {
        "latex": "\\overbrace",
        "mathml": "<mover>{}<mo>&#x23DF;</mo></mover>",
    },
    '"overbrace"': {
        "latex": "\\overbrace",
        "mathml": "<mover>{}<mo>&#x23DF;</mo></mover>",
    },
    '"cancel"': {
        "latex": "\\cancel",
        "mathml": "<menclose notation='updiagonalstrike'>{}</menclose>",
    },
    '"bb"': {
        "latex": "\\boldsymbol",
        "mathml": "<mstyle mathvariant='bold'>{}</mstyle>",
    },
    '"bbb"': {
        "latex": "\\mathbb",
        "mathml": "<mstyle mathvariant='double-struck'>{}</mstyle>",
    },
    '"cc"': {
        "latex": "\\mathcal",
        "mathml": "<mstyle mathvariant='script'>{}</mstyle>",
    },
    '"tt"': {
        "latex": "\\texttt",
        "mathml": "<mstyle mathvariant='monospace'>{}</mstyle>",
    },
    '"fr"': {
        "latex": "\\mathfrak",
        "mathml": "<mstyle mathvariant='fraktur'>{}</mstyle>",
    },
    '"sf"': {
        "latex": "\\textsf",
        "mathml": "<mstyle mathvariant='sanf-serif'>{}</mstyle>",
    },
    '"ul"': {
        "latex": "\\underline",
        "mathml": "<munder>{}<mo>&#x332;</mo></munder>",
    },
    '"underline"': {
        "latex": "\\underline",
        "mathml": "<munder>{}<mo>&#x332;</mo></munder>",
    },
    '"bar"': {
        "latex": "\\overline",
        "mathml": "<mover>{}<mo>&#x332;</mo></mover>",
    },
    '"overline"': {
        "latex": "\\overline",
        "mathml": "<mover>{}<mo>&#x332;</mo></mover>",
    },
    '"hat"': {"latex": "\\hat", "mathml": "<mover>{}<mo>^</mo></mover>"},
    '"vec"': {
        "latex": "\\vec",
        "mathml": "<mover>{}<mo stretchy='false'>&#x2192;</mo></mover>",
    },
    '"dot"': {
        "latex": "\\dot",
        "mathml": "<mover>{}<mo stretchy='false'>.</mo></mover>",
    },
    '"ddot"': {
        "latex": "\\ddot",
        "mathml": "<mover>{}<mo stretchy='false'>..</mo></mover>",
    },
}

operation_symbols = {
    '"+"': {"latex": "+", "mathml": "+"},
    '"*"': {"latex": "\\cdot", "mathml": "&#x22C5;"},
    '"-"': {"latex": "-", "mathml": "-"},
    '"cdot"': {"latex": "\\cdot", "mathml": "&CenterDot;"},
    '"**"': {"latex": "\\ast", "mathml": "&ast;"},
    '"ast"': {"latex": "\\ast", "mathml": "&ast;"},
    '"***"': {"latex": "\\star", "mathml": "&Star;"},
    '"star"': {"latex": "\\star", "mathml": "&Star;"},
    '"//"': {"latex": "/", "mathml": "&frasl;"},
    '"\\\\"': {"latex": "\\setminus", "mathml": "&setminus;"},
    '"setminus"': {"latex": "\\setminus", "mathml": "&setminus;"},
    '"xx"': {"latex": "\\times", "mathml": "&times;"},
    '"times"': {"latex": "\\times", "mathml": "&times;"},
    '"-:"': {"latex": "\\div", "mathml": "&div;"},
    '"div"': {"latex": "\\div", "mathml": "&div;"},
    '"|><"': {"latex": "\\ltimes", "mathml": "&ltimes;"},
    '"ltimes"': {"latex": "\\ltimes", "mathml": "&ltimes;"},
    '"><|"': {"latex": "\\rtimes", "mathml": "&rtimes;"},
    '"rtimes"': {"latex": "\\rtimes", "mathml": "&rtimes;"},
    '"|><|"': {"latex": "\\bowtie", "mathml": "&bowtie;"},
    '"bowtie"': {"latex": "\\bowtie", "mathml": "&bowtie;"},
    '"@"': {"latex": "\\circ", "mathml": "&SmallCircle;"},
    '"circ"': {"latex": "\\circ", "mathml": "&SmallCircle;"},
    '"o+"': {"latex": "\\oplus", "mathml": "&oplus;"},
    '"oplus"': {"latex": "\\oplus", "mathml": "&oplus;"},
    '"ox"': {"latex": "\\otimes", "mathml": "&times;"},
    '"otimes"': {"latex": "\\otimes", "mathml": "&times;"},
    '"o."': {"latex": "\\odot", "mathml": "&odot;"},
    '"odot"': {"latex": "\\odot", "mathml": "&odot;"},
    '"sum"': {"latex": "\\sum", "mathml": "&sum;"},
    '"prod"': {"latex": "\\prod", "mathml": "&prod;"},
    '"^^"': {"latex": "\\wedge", "mathml": "&wedge;"},
    '"wedge"': {"latex": "\\wedge", "mathml": "&wedge;"},
    '"^^^"': {"latex": "\\bigwedge", "mathml": "&bidwedge;"},
    '"bidwedge"': {"latex": "\\bidwedge", "mathml": "&bidwedge;"},
    '"vv"': {"latex": "\\vee", "mathml": "&vee;"},
    '"vee"': {"latex": "\\vee", "mathml": "&vee;"},
    '"vvv"': {"latex": "\\bigvee", "mathml": "&bigvee;"},
    '"bigvee"': {"latex": "\\bigvee", "mathml": "&bigvee;"},
    '"nn"': {"latex": "\\cap", "mathml": "&cap;"},
    '"cap"': {"latex": "\\cap", "mathml": "&cap;"},
    '"nnn"': {"latex": "\\bigcap", "mathml": "&bigcap;"},
    '"bigcap"': {"latex": "\\bigcap", "mathml": "&bigcap;"},
    '"uu"': {"latex": "\\cup", "mathml": "&cup;"},
    '"cup"': {"latex": "\\cup", "mathml": "&cup;"},
    '"uuu"': {"latex": "\\bigcup", "mathml": "&bigcup;"},
    '"bigcup"': {"latex": "\\bigcup", "mathml": "&bigcup;"},
}

logical_symbols = {
    '"and"': {"latex": "\\text{and}", "mathml": ""},
    '"or"': {"latex": "\\text{and}", "mathml": ""},
    '"not"': {"latex": "\\neg", "mathml": ""},
    '"neg"': {"latex": "\\neg", "mathml": ""},
    '"=>"': {"latex": "\\implies", "mathml": ""},
    '"implies"': {"latex": "\\implies", "mathml": ""},
    '"if"': {"latex": "\\text{if}", "mathml": ""},
    '"<=>"': {"latex": "\\iff", "mathml": ""},
    '"iff"': {"latex": "\\iff", "mathml": ""},
    '"AA"': {"latex": "\\forall", "mathml": ""},
    '"forall"': {"latex": "\\forall", "mathml": ""},
    '"EE"': {"latex": "\\exists", "mathml": ""},
    '"exists"': {"latex": "\\exists", "mathml": ""},
    '"_|_"': {"latex": "\\bot", "mathml": ""},
    '"bot"': {"latex": "\\bot", "mathml": ""},
    '"TT"': {"latex": "\\top", "mathml": ""},
    '"top"': {"latex": "\\top", "mathml": ""},
    '"|--"': {"latex": "\\vdash", "mathml": ""},
    '"vdash"': {"latex": "\\vdash", "mathml": ""},
    '"|=="': {"latex": "\\models", "mathml": ""},
    '"models"': {"latex": "\\models", "mathml": ""},
}

relation_symbols = {
    '"="': {"latex": "=", "mathml": "="},
    '"!="': {"latex": "\\ne", "mathml": ""},
    '"ne"': {"latex": "\\ne", "mathml": ""},
    '"<"': {"latex": "<", "mathml": ""},
    '"lt"': {"latex": "<", "mathml": ""},
    '">"': {"latex": ">", "mathml": ""},
    '"gt"': {"latex": ">", "mathml": ""},
    '"<="': {"latex": "\\le", "mathml": ""},
    '"le"': {"latex": "\\le", "mathml": ""},
    '">="': {"latex": "\\ge", "mathml": ""},
    '"ge"': {"latex": "\\ge", "mathml": ""},
    '"-<"': {"latex": "\\prec", "mathml": ""},
    '"prec"': {"latex": "\\prec", "mathml": ""},
    '"-<="': {"latex": "\\preceq", "mathml": ""},
    '"preceq"': {"latex": "\\preceq", "mathml": ""},
    '">-"': {"latex": "\\succ", "mathml": ""},
    '"succ"': {"latex": "\\succ", "mathml": ""},
    '">-="': {"latex": "\\succeq", "mathml": ""},
    '"succeq"': {"latex": "\\succeq", "mathml": ""},
    '"in"': {"latex": "\\in", "mathml": ""},
    '"!in"': {"latex": "\\notin", "mathml": ""},
    '"notin"': {"latex": "\\notin", "mathml": ""},
    '"sub"': {"latex": "\\subset", "mathml": ""},
    '"subset"': {"latex": "\\subset", "mathml": ""},
    '"sup"': {"latex": "\\supset", "mathml": ""},
    '"supset"': {"latex": "\\supset", "mathml": ""},
    '"sube"': {"latex": "\\subseteq", "mathml": ""},
    '"subseteq"': {"latex": "\\subseteq", "mathml": ""},
    '"supe"': {"latex": "\\supseteq", "mathml": ""},
    '"supseteq"': {"latex": "\\supseteq", "mathml": ""},
    '"-="': {"latex": "\\equiv", "mathml": ""},
    '"equiv"': {"latex": "\\equiv", "mathml": ""},
    '"~="': {"latex": "\\cong", "mathml": ""},
    '"cong"': {"latex": "\\cong", "mathml": ""},
    '"~~"': {"latex": "\\approx", "mathml": ""},
    '"approx"': {"latex": "\\approx", "mathml": ""},
    '"prop"': {"latex": "\\propto", "mathml": ""},
    '"propto"': {"latex": "\\propto", "mathml": ""},
}

function_symbols = {
    '"sin"': {"latex": "\\sin", "mathml": ""},
    '"cos"': {"latex": "\\cos", "mathml": ""},
    '"tan"': {"latex": "\\tan", "mathml": ""},
    '"sec"': {"latex": "\\sec", "mathml": ""},
    '"csc"': {"latex": "\\csc", "mathml": ""},
    '"cot"': {"latex": "\\cot", "mathml": ""},
    '"arcsin"': {"latex": "\\arcsin", "mathml": ""},
    '"arccos"': {"latex": "\\arccos", "mathml": ""},
    '"arctan"': {"latex": "\\arctan", "mathml": ""},
    '"sinh"': {"latex": "\\sinh", "mathml": ""},
    '"cosh"': {"latex": "\\cosh", "mathml": ""},
    '"tanh"': {"latex": "\\tanh", "mathml": ""},
    '"sech"': {"latex": "\\sech", "mathml": ""},
    '"csch"': {"latex": "\\csch", "mathml": ""},
    '"coth"': {"latex": "\\coth", "mathml": ""},
    '"exp"': {"latex": "\\exp", "mathml": ""},
    '"log"': {"latex": "\\log", "mathml": ""},
    '"ln"': {"latex": "\\ln", "mathml": ""},
    '"det"': {"latex": "\\det", "mathml": ""},
    '"dim"': {"latex": "\\dim", "mathml": ""},
    '"mod"': {"latex": "\\mod", "mathml": ""},
    '"gcd"': {"latex": "\\gcd", "mathml": ""},
    '"lcm"': {"latex": "\\lcm", "mathml": ""},
    '"lub"': {"latex": "\\lub", "mathml": ""},
    '"glb"': {"latex": "\\glb", "mathml": ""},
    '"min"': {"latex": "\\min", "mathml": ""},
    '"max"': {"latex": "\\max", "mathml": ""},
    '"lim"': {"latex": "\\lim", "mathml": ""},
    '"dstyle"': {"latex": "\\displaystyle", "mathml": ""},
    '"f"': {"latex": "f", "mathml": ""},
    '"g"': {"latex": "g", "mathml": ""},
}

greek_letters = {
    '"alpha"': {"latex": "\\alpha", "mathml": ""},
    '"beta"': {"latex": "\\beta", "mathml": ""},
    '"gamma"': {"latex": "\\gamma", "mathml": ""},
    '"Gamma"': {"latex": "\\Gamma", "mathml": ""},
    '"delta"': {"latex": "\\delta", "mathml": ""},
    '"Delta"': {"latex": "\\Delta", "mathml": ""},
    '"epsilon"': {"latex": "\\epsilon", "mathml": ""},
    '"varepsilon"': {"latex": "\\varepsilon", "mathml": ""},
    '"zeta"': {"latex": "\\zeta", "mathml": ""},
    '"eta"': {"latex": "\\eta", "mathml": ""},
    '"theta"': {"latex": "\\theta", "mathml": ""},
    '"Theta"': {"latex": "\\Theta", "mathml": ""},
    '"vartheta"': {"latex": "\\vartheta", "mathml": ""},
    '"iota"': {"latex": "\\iota", "mathml": ""},
    '"kappa"': {"latex": "\\kappa", "mathml": ""},
    '"lambda"': {"latex": "\\lambda", "mathml": ""},
    '"Lambda"': {"latex": "\\Lambda", "mathml": ""},
    '"mu"': {"latex": "\\mu", "mathml": ""},
    '"nu"': {"latex": "\\nu", "mathml": ""},
    '"xi"': {"latex": "\\xi", "mathml": ""},
    '"Xi"': {"latex": "\\Xi", "mathml": ""},
    '"pi"': {"latex": "\\pi", "mathml": ""},
    '"Pi"': {"latex": "\\Pi", "mathml": ""},
    '"rho"': {"latex": "\\rho", "mathml": ""},
    '"sigma"': {"latex": "\\sigma", "mathml": ""},
    '"Sigma"': {"latex": "\\Sigma", "mathml": ""},
    '"tau"': {"latex": "\\tau", "mathml": ""},
    '"upsilon"': {"latex": "\\upsilon", "mathml": ""},
    '"phi"': {"latex": "\\phi", "mathml": ""},
    '"Phi"': {"latex": "\\Phi", "mathml": ""},
    '"varphi"': {"latex": "\\varphi", "mathml": ""},
    '"chi"': {"latex": "\\chi", "mathml": ""},
    '"psi"': {"latex": "\\psi", "mathml": ""},
    '"Psi"': {"latex": "\\Psi", "mathml": ""},
    '"omega"': {"latex": "\\omega", "mathml": ""},
    '"Omega"': {"latex": "\\Omega", "mathml": ""},
}

left_parenthesis = {
    '"(:"': {"latex": "\\langle", "mathml": "&#x2329;"},
    '"("': {"latex": "(", "mathml": "("},
    '"["': {"latex": "[", "mathml": ""},
    '"{:"': {"latex": "{:", "mathml": ""},
    '"{"': {"latex": "\\{", "mathml": ""},
    '"|:"': {"latex": "\\vert", "mathml": ""},
    '"||:"': {"latex": "\\lVert", "mathml": ""},
    '"langle"': {"latex": "\\langle", "mathml": "&#x2329;"},
    '"<<"': {"latex": "\\langle", "mathml": "&#x2329;"},
}

right_parenthesis = {
    '":)"': {"latex": "\\rangle", "mathml": "&#x232A;"},
    '")"': {"latex": ")", "mathml": ")"},
    '"]"': {"latex": "]", "mathml": ""},
    '":}"': {"latex": ":}", "mathml": ""},
    '"}"': {"latex": "\\}", "mathml": ""},
    '":|"': {"latex": "\\vert", "mathml": ""},
    '":||"': {"latex": "\\rVert", "mathml": ""},
    '"rangle"': {"latex": "\\rangle", "mathml": "&#x232A;"},
    '">>"': {"latex": "\\rangle", "mathml": "&#x232A;"},
}

arrows = {
    '"uarr"': {"latex": "\\uparrow", "mathml": ""},
    '"uparrow"': {"latex": "\\uparrow", "mathml": ""},
    '"darr"': {"latex": "\\downarrow", "mathml": ""},
    '"downarrow"': {"latex": "\\downarrow", "mathml": ""},
    '"rarr"': {"latex": "\\rightarrow", "mathml": ""},
    '"rArr"': {"latex": "\\Rightarrow", "mathml": ""},
    '"rightarrow"': {"latex": "\\rightarrow", "mathml": ""},
    '"->"': {"latex": "\\to", "mathml": ""},
    '"to"': {"latex": "\\to", "mathml": ""},
    '">->"': {"latex": "\\rightarrowtail", "mathml": ""},
    '"rightarrowtail"': {"latex": "\\rightarrowtail", "mathml": ""},
    '"->>"': {"latex": "\\twoheadrightarrow", "mathml": ""},
    '"twoheadrightarrow"': {"latex": "\\twoheadrightarrow", "mathml": ""},
    '">->>"': {"latex": "\\twoheadrightarrowtail", "mathml": ""},
    '"twoheadrightarrowtail"': {
        "latex": "\\twoheadrightarrowtail",
        "mathml": "",
    },
    '"|->"': {"latex": "\\mapsto", "mathml": ""},
    '"mapsto"': {"latex": "\\mapsto", "mathml": ""},
    '"larr"': {"latex": "\\leftarrow", "mathml": ""},
    '"leftarrow"': {"latex": "\\leftarrow", "mathml": ""},
    '"harr"': {"latex": "\\leftrightarrow", "mathml": ""},
    '"leftrightarrow"': {"latex": "\\leftrightarrow", "mathml": ""},
    '"lArr"': {"latex": "\\Leftarrow", "mathml": ""},
    '"Leftarrow"': {"latex": "\\Leftarrow", "mathml": ""},
    '"hArr"': {"latex": "\\Leftrightarrow", "mathml": ""},
    '"Leftrightarrow"': {"latex": "\\Leftrightarrow", "mathml": ""},
}

colors = {
    '"red"': {"latex": "red", "mathml": "red"},
}

misc_symbols = {
    '"^"': {"latex": "^", "mathml": ""},
    '","': {"latex": ",", "mathml": ""},
    '"_"': {"latex": "_", "mathml": ""},
    '"\'"': {"latex": "'", "mathml": ""},
    '"/"': {"latex": "/", "mathml": ""},
    '"|"': {"latex": "|", "mathml": ""},
    '":"': {"latex": ":", "mathml": ""},
    '"int"': {"latex": "\\int", "mathml": ""},
    '"integral"': {"latex": "\\int", "mathml": ""},
    '"oint"': {"latex": "\\oint", "mathml": ""},
    '"del"': {"latex": "\\partial", "mathml": ""},
    '"partial"': {"latex": "\\partial", "mathml": ""},
    '"grad"': {"latex": "\\nable", "mathml": ""},
    '"nabla"': {"latex": "\\nabla", "mathml": ""},
    '"+-"': {"latex": "\\pm", "mathml": ""},
    '"pm"': {"latex": "\\pm", "mathml": ""},
    '"O/"': {"latex": "\\emptyset", "mathml": ""},
    '"emptyset"': {"latex": "\\emptyset", "mathml": ""},
    '"oo"': {"latex": "\\infty", "mathml": ""},
    '"infty"': {"latex": "\\infty", "mathml": ""},
    '"aleph"': {"latex": "\\aleph", "mathml": ""},
    '":."': {"latex": "\\therefore", "mathml": ""},
    '"therefore"': {"latex": "\\therefore", "mathml": ""},
    '":\'"': {"latex": "\\because", "mathml": ""},
    '"because"': {"latex": "\\because", "mathml": ""},
    '"..."': {"latex": "\\ldots", "mathml": ""},
    '"ldots"': {"latex": "\\ldots", "mathml": ""},
    '"cdots"': {"latex": "\\cdots", "mathml": ""},
    '"vdots"': {"latex": "\\vdots", "mathml": ""},
    '"ddots"': {"latex": "\\ddots", "mathml": ""},
    '"quad"': {"latex": "\\quad", "mathml": ""},
    '"/_"': {"latex": "\\angle", "mathml": ""},
    '"angle"': {"latex": "\\angle", "mathml": ""},
    '"frown"': {"latex": "\\frown", "mathml": ""},
    '"/_\\\\"': {"latex": "\\triangle", "mathml": ""},
    '"triangle"': {"latex": "\\triangle", "mathml": ""},
    '"diamond"': {"latex": "\\diamond", "mathml": ""},
    '"square"': {"latex": "\\square", "mathml": ""},
    '"|__"': {"latex": "\\lfloor", "mathml": ""},
    '"lfloor"': {"latex": "\\lfloor", "mathml": ""},
    '"__|"': {"latex": "\\rfloor", "mathml": ""},
    '"rfloor"': {"latex": "\\rfloor", "mathml": ""},
    '"|~"': {"latex": "\\lceiling", "mathml": ""},
    '"lceiling"': {"latex": "\\lceiling", "mathml": ""},
    '"~|"': {"latex": "\\rceiling", "mathml": ""},
    '"rceiling"': {"latex": "\\rceiling", "mathml": ""},
    '"CC"': {"latex": "\\mathbb{C}", "mathml": ""},
    '"NN"': {"latex": "\\mathbb{N}", "mathml": ""},
    '"QQ"': {"latex": "\\mathbb{Q}", "mathml": ""},
    '"RR"': {"latex": "\\mathbb{R}", "mathml": ""},
    '"ZZ"': {"latex": "\\mathbb{Z}", "mathml": ""},
}

# matrix2par = {
#     "pmatrix": ["(", ")"],
#     "bmatrix": ["[", "]"],
#     "Bmatrix": ["\{", "\}"],
#     "vmatrix": ["|", "|"],
#     "Vmatrix": ["||", "||"],
# }