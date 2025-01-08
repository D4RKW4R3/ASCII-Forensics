print('''  
{}  _                                                      {}
{} |  \   _           |  /  |  |  |  _               ___,  {}
{} ||| | |  \   |`))  |_/   |  |  | |  \   |`))    //      {}
{} ||| | |   \  | \   | \   |  |  | |   \  | \    ||====:  {}
{} |__/  |  _ \ |  \  |  \  |__|__| |  _ \ |  \     \___   {}
{}       |   `´ |                   |   `´ |            `  {}
{}       ;      ;                   ;      ;               {}
{}========================================================={}

by: ✟𝕻𝖆𝖚𝖑𝖔 𝕯𝖚𝖆𝖗𝖙𝖊  

''')

print('''
Escolha a opção:
1- Tabela ASCII para consulta, isso irá gerar um .txt em seu dispositivo (para Windows apenas)
2- Verificação de caracteres manual
3- Scanning
4- Help
qualquer outra tecla cancela
''')

escolha = input("Digite o número correspondente à função desejada: ")
if escolha == '1':
    ASCII = '''
    decimal	binário	Unicode	c	observação
    0	00000000	U+0000	\0	byte nulo
    1	00000001	U+0001		não usamos
    2	00000010	U+0002		não usamos
    3	00000011	U+0003		não usamos
    4	00000100	U+0004		não usamos
    5	00000101	U+0005		não usamos
    6	00000110	U+0006		não usamos
    7	00000111	U+0007	\a	apito
    8	00001000	U+0008	\b	backspace
    9	00001001	U+0009	\t	tabulação
    10	00001010	U+000A	\n	fim de linha
    11	00001011	U+000B	\v	tab vertical
    12	00001100	U+000C	\f	fim de página
    13	00001101	U+000D	\r	carriage return
    14	00001110	U+000E		não usamos
    15	00001111	U+000F		não usamos
    16	00010000	U+0010		não usamos
    17	00010001	U+0011		não usamos
    18	00010010	U+0012		não usamos
    19	00010011	U+0013		não usamos
    20	00010100	U+0014		não usamos
    21	00010101	U+0015		não usamos
    22	00010110	U+0016		não usamos
    23	00010111	U+0017		não usamos
    24	00011000	U+0018		não usamos
    25	00011001	U+0019		não usamos
    26	00011010	U+001A		não usamos
    27	00011011	U+001B		escape
    28	00011100	U+001C		não usamos
    29	00011101	U+001D		não usamos
    30	00011110	U+001E		não usamos
    31	00011111	U+001F		não usamos
    32	00100000	U+0020	 	espaço
    33	00100001	U+0021	!	
    34	00100010	U+0022	"	aspas
    35	00100011	U+0023	#	
    36	00100100	U+0024	$	
    37	00100101	U+0025	%	
    38	00100110	U+0026	&	
    39	00100111	U+0027	'	apóstrofe
    40	00101000	U+0028	(	
    41	00101001	U+0029	)	
    42	00101010	U+002A	*	
    43	00101011	U+002B	+	
    44	00101100	U+002C	,	vírgula
    45	00101101	U+002D	-	hífen
    46	00101110	U+002E	.	ponto
    47	00101111	U+002F	/	
    48	00110000	U+0030	0	
    49	00110001	U+0031	1	
    50	00110010	U+0032	2	
    51	00110011	U+0033	3	
    52	00110100	U+0034	4	
    53	00110101	U+0035	5	
    54	00110110	U+0036	6	
    55	00110111	U+0037	7	
    56	00111000	U+0038	8	
    57	00111001	U+0039	9	
    58	00111010	U+003A	:	
    59	00111011	U+003B	;	
    60	00111100	U+003C	<	
    61	00111101	U+003D	=	
    62	00111110	U+003E	>	
    63	00111111	U+003F	?	
    64	01000000	U+0040	@	
    65	01000001	U+0041	A	
    66	01000010	U+0042	B	
    67	01000011	U+0043	C	
    68	01000100	U+0044	D	
    69	01000101	U+0045	E	
    70	01000110	U+0046	F	
    71	01000111	U+0047	G	
    72	01001000	U+0048	H	
    73	01001001	U+0049	I	
    74	01001010	U+004A	J	
    75	01001011	U+004B	K	
    76	01001100	U+004C	L	
    77	01001101	U+004D	M	
    78	01001110	U+004E	N	
    79	01001111	U+004F	O	
    80	01010000	U+0050	P	
    81	01010001	U+0051	Q	
    82	01010010	U+0052	R	
    83	01010011	U+0053	S	
    84	01010100	U+0054	T	
    85	01010101	U+0055	U	
    86	01010110	U+0056	V	
    87	01010111	U+0057	W	
    88	01011000	U+0058	X	
    89	01011001	U+0059	Y	
    90	01011010	U+005A	Z	
    91	01011011	U+005B	[	
    92	01011100	U+005C	\	
    93	01011101	U+005D	]	
    94	01011110	U+005E	^	
    95	01011111	U+005F	_	underscore
    96	01100000	U+0060	`	apóstrofe esq.
    97	01100001	U+0061	a	
    98	01100010	U+0062	b	
    99	01100011	U+0063	c	
    100	01100100	U+0064	d	
    101	01100101	U+0065	e	
    102	01100110	U+0066	f	
    103	01100111	U+0067	g	
    104	01101000	U+0068	h	
    105	01101001	U+0069	i	
    106	01101010	U+006A	j	
    107	01101011	U+006B	k	
    108	01101100	U+006C	l	
    109	01101101	U+006D	m	
    110	01101110	U+006E	n	
    111	01101111	U+006F	o	
    112	01110000	U+0070	p	
    113	01110001	U+0071	q	
    114	01110010	U+0072	r	
    115	01110011	U+0073	s	
    116	01110100	U+0074	t	
    117	01110101	U+0075	u	
    118	01110110	U+0076	v	
    119	01110111	U+0077	w	
    120	01111000	U+0078	x	
    121	01111001	U+0079	y	
    122	01111010	U+007A	z	
    123	01111011	U+007B	{	
    124	01111100	U+007C	|	
    125	01111101	U+007D	}	
    126	01111110	U+007E	~	
    127	01111111	U+007F		delete
    fonte: https://www.ime.usp.br/~pf/algoritmos/apend/ascii.html
    '''
    nome_arquivo = "ASCII.txt"
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(ASCII)

    print(f'Arquivo para consultas gerado com sucesso! Salvo como {nome_arquivo}')

elif escolha == '2':
    print("insira caracteres")
    input_chars = input()

    print("caractere - unicode - binário - decimal")
    for char in input_chars:
        print(f"{char} - U+{ord(char):04X} - {bin(ord(char))[2:]} - {ord(char)}")



elif escolha == '3':
    print("insira caracteres")
    input_chars = input()

    print("caractere - unicode - binário - decimal")
    for char in input_chars:
        if ord(char) not in range(32, 127) or ord(char) in [7, 8, 9, 10, 11, 12, 13, 27]:
            print(f"\033[91m{char} - U+{ord(char):04X} - {bin(ord(char))[2:]} - {ord(char)}\033[0m")
        else:
            print(f"{char} - U+{ord(char):04X} - {bin(ord(char))[2:]} - {ord(char)}")



elif escolha == '4':
    print('''Esta ferramenta serve para análise de veracidade de caracteres.
    Isso pode ser útil em por exemplo ataques homógrafos/ataques homoglíficos.
    
    "Os ataques homógrafos ou homoglíficos são um tipo de ciberataque que explora 
    a semelhança visual entre caracteres de diferentes conjuntos de caracteres ou 
    alfabetos. Esses ataques são comumente usados em técnicas de phishing e 
    engenharia social para enganar os usuários, levando-os a acreditar que estão 
    acessando um site legítimo quando, na verdade, estão acessando um site 
    fraudulento." Inácio Gorayeb
     
    Mesmo com ferramentas de análise como o Vírus Total e o Anti-Scan Me, pode 
    acontecer de uma URL não ser detectada. Neste contexto, usar este código para 
    fazer a análise, pode ser útil.
    
    O uso é simples, tenha uma tabela ASCII para comparar. Caso não tenha, selecionar
    a opção 1 irá criar em seu dispositivo um arquivo chamado ASCII.txt com a fonte
    da tabela inclusive, para que você tenha a tabela.
    A opção 2 você pode utilizar para fazer uma análise manual.
    A opção 3 já deduz automaticamente quais caracteres não são "normais".
    (mesmo assim prefira a análise manual para melhor acurácia).
    
    Vale lembrar que, isso é válido para, quando você sabe que o link existe, mas
    suspeita que os caracteres não sejam realmente verdadeiros, ou seja, em caso de
    suspeita de ataques homoglíficos.
    ''')

#Tutorial: https://www.youtube.com/watch?v=IzDwclnQBh8





   

