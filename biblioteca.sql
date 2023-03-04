-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 04-Mar-2023 às 20:57
-- Versão do servidor: 5.7.36
-- versão do PHP: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `biblioteca`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `autores`
--

DROP TABLE IF EXISTS `autores`;
CREATE TABLE IF NOT EXISTS `autores` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nome` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=372 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `autores`
--

INSERT INTO `autores` (`id`, `nome`) VALUES
(1, 'Robert D. Hsrich'),
(2, 'Michael P. Peters'),
(3, 'Dean A Shepherd'),
(4, 'Stephen P Robbins'),
(5, 'Timothy A Judge'),
(6, 'Filipe Sobral'),
(7, 'Luis Cézar G de Araujo'),
(8, 'Luciano Crocco'),
(9, 'Renato Telles'),
(10, 'Ricardo M. Gioia'),
(11, 'Thelma Rocha'),
(12, 'Vivian Lara Strehlau'),
(13, 'Luiz Antonio Bernardi'),
(14, 'Regina Blessa'),
(15, 'Djalma de Pinho Rebolsas de Oliveira'),
(16, 'Cesar Simões Salim'),
(17, 'Alexandre Assaf Neto'),
(18, 'Masakazu Hoji'),
(19, 'Lawrence J Gitman'),
(20, 'Fernando César Lenzi'),
(21, 'André Ofnhejm Mascarenhas'),
(22, 'Ana Cristina Limongi-França'),
(23, 'Sílvio R. I. Pires'),
(24, 'Saulo Barbará'),
(25, 'José Osvaldo De Sordi'),
(26, 'Henrique Corrêa'),
(27, 'Mauro Caon'),
(28, 'Idalberto Chiavenato'),
(29, 'Robert A Baron'),
(30, 'Scott A Shane'),
(31, 'David Simchi Levi'),
(32, 'Philip Kaminsky'),
(33, 'Edith Simchi Levi'),
(34, 'Takeshy Tachizawa'),
(35, 'Eliezer Arantes da Costa'),
(36, 'Edson Pacheco Pladini'),
(37, 'Sergio Cavaline Filho'),
(38, 'Marcelo Marçula'),
(39, 'Pio Armando Benini Filho'),
(40, 'Ralph M. Star'),
(41, 'George W Reynolds'),
(42, 'Juan Carlos Lappani'),
(43, 'H. l. Capron'),
(44, 'J. A. Johnson'),
(45, 'Adriano Leal Bruini'),
(46, 'Roberto Brasileiro Paixão'),
(47, 'Mário Leite'),
(48, 'Sonia M Baccari de Godoy'),
(49, 'Cris Gostow'),
(50, 'Marcello Marcelino'),
(51, 'Efraim Turban'),
(52, 'David King'),
(53, 'Kenneth C. Laudon'),
(54, 'Mitsu Higuchi Yanaze'),
(55, 'Evandir Megliorini'),
(56, 'Marco Aurélio Vallim'),
(57, 'Luciano Thomé e Castro'),
(58, 'Marco Aurélio P Dias'),
(59, 'Fernando César Marra'),
(60, 'Silva Mariângela Abrão'),
(61, 'Amaury Patrick Gremaud'),
(62, 'Marco Antonio Sandoval de Vasconcelos'),
(63, 'Rudinei Toneto Júnior'),
(64, 'Dennis J Sweenney'),
(65, 'Thomas A Williams'),
(66, 'David R Anderson'),
(67, 'Leonard J Kazmier'),
(68, 'Jonh M Ivacevich'),
(69, 'Darcy Mitiko Mori Hanashiro'),
(70, 'Maria Luisa Mendes Teixeira'),
(71, 'Laura Menegon Zaccarelli'),
(72, 'Daniel Goleman, PHD'),
(73, 'Patrônio Gracia Martins'),
(74, 'Paulo Renato Campos Alt'),
(75, 'Ross Wester Jaffe Lamb'),
(77, 'David A. DeCenzo'),
(78, 'Robert M Eolter'),
(79, 'Antonio Cezar Amaru Maximiano'),
(80, 'June Alisson Westarb Crus'),
(81, 'Emir Guimarães Andrich'),
(82, 'Carlos Ubiraten da Costa Schier'),
(83, 'Afrânio Carlos Murolo'),
(84, 'Giacomo Bonetto'),
(85, 'Samuel C Certo'),
(86, 'J P Peter'),
(87, 'Ana Maria Roux Cesar'),
(88, 'Reynaldo Cavalheiro Marcondes'),
(89, 'José Carlos Marion'),
(90, 'Equipe de Professores da FFA/USP'),
(91, 'Jay B Barney'),
(92, 'Wiliam S. Hesterly'),
(93, 'R Duane Ireland'),
(94, 'Robert E Hoskisson'),
(95, 'Michael A Hitt'),
(96, 'Kevin L'),
(97, 'N. Gregory Mankiw'),
(98, 'José Augusto N. G. Manzano'),
(99, 'Fernando de Castro Velloso'),
(100, 'Carlos Patrício Samanez'),
(101, 'Gelson Iezzi Samuel Hazzan'),
(102, 'Samuel Hazzan'),
(103, 'David Mauro Degenszajn'),
(104, 'Pedro A. Morettin'),
(106, 'Wilton O. Bussab'),
(107, 'Franklin D. Demana'),
(108, 'Bert K. Waits'),
(109, 'Gregory D. Foley'),
(110, 'Daniel Kennedy'),
(111, 'Abelardo de Lima Puccini'),
(112, 'José Dutra Vieira Sobrinho'),
(113, 'Sebastião Medeiros da Silva'),
(114, 'Elio Medeiros da Silva'),
(115, 'Ermes Medeiros da Silva'),
(116, 'Seizen Yamashiro'),
(117, 'Suzana Abreu de Oliveira Souza'),
(118, 'André Hidebrando A'),
(119, 'Charles David Forte'),
(120, 'Sérgio Vasconcelos de Luna'),
(121, 'Anderson Semprini'),
(122, 'Fernando Dolabela '),
(123, 'Alexandre Luzzi Las Casas'),
(124, 'Clotilde Perez'),
(125, 'Ivan Santo Barbosa'),
(126, 'Mauro Ferreira'),
(127, 'Silvia Constant Vergara '),
(128, 'Francisco Lacombe'),
(129, 'Marcelo Abilio Públio'),
(130, 'Antônio Joaquim Severino'),
(131, 'Antonio Chizzotti'),
(132, 'Lino Rampazzo'),
(133, 'Sylvia Demetresco'),
(134, 'Dominique Maingueneau '),
(135, 'Helena H. Nagamine Brandão'),
(136, 'Diana Luz Pessoa de Barros'),
(137, 'Ingedore Vilhaça Koch'),
(138, 'Gilles Lipovetsky'),
(139, 'Magda Becker Soares'),
(140, 'Edson Nascimento Campos'),
(141, 'Maria Margarida de Andrade'),
(142, 'Moacyr Motta da Silva'),
(143, 'Karl-Henrik Robèrt '),
(144, 'Othon M. Garcia '),
(145, 'Norma Discini '),
(146, 'Miguel Rende '),
(147, 'Evanildo Bechara '),
(148, 'Rizzato Nunes '),
(149, 'Celso Cunha'),
(150, 'Lindkey Cintra'),
(151, 'Cláudia Lima Marques'),
(152, 'Antonio Herman V. Benjamin'),
(153, 'Bruno Miragem'),
(154, 'Miguel Diaz'),
(155, 'García-Talavera'),
(156, 'Jurandir Freire Costa'),
(157, 'Humberto Maturana '),
(158, 'Umberto Eco'),
(159, 'Marina de Andrade Marconi'),
(160, 'Eva Maria Lakatos'),
(161, 'Fátima Lourenço'),
(162, 'José Oliveira Sam'),
(163, 'Inez Sautchuk '),
(164, 'Christian Laville'),
(165, 'Jean Dionne'),
(166, 'Augusto Massashi Horiguti'),
(167, 'Juliane Donadel'),
(168, 'Alexandra Loras'),
(169, 'Ricardo Amorim'),
(170, 'Carlos Ayres Brito'),
(171, 'Armando Castelar'),
(172, 'Silvio Meira'),
(173, 'Nara Pavão'),
(174, 'Roberto Damata'),
(175, 'Laurentino Gomes'),
(176, 'Luís Roberto Barroso'),
(177, 'Otaviano Canuto'),
(178, 'José Eduardo Faria'),
(179, 'Joice Toyota'),
(180, 'Mario Vargas Llosa'),
(181, 'Vicente Falconi'),
(182, 'Andrés Velasco'),
(183, 'Sérgio Moro'),
(184, 'Paulo Galvão'),
(185, 'Deltan Dallagnol'),
(186, 'Alessando Gerardi'),
(187, 'Escola de Formação de Professores Paulo Renato Costa Sousa'),
(189, 'Rodrigo Soares'),
(190, 'Adhemar Batista Hemeritas'),
(192, 'Gary Armstrong'),
(193, 'João Roberto Santos Réngnier'),
(194, 'William J Good'),
(195, 'Paul K Hatt'),
(196, 'Domingos Sávio Zainaghi'),
(197, 'Isma Marinho Falcão'),
(198, 'Aluysio Mendonça Sapaio'),
(199, 'Friede Roy Reis'),
(200, 'Ovídio Barradas'),
(201, 'Stanley Marcus'),
(202, 'José Cretella Júnior'),
(203, 'João Angélico'),
(204, 'Antonio Carlos Gil'),
(205, 'João Bosco Medeiros'),
(206, 'Dácio G Moura'),
(207, 'Eduardo F Brabosa'),
(208, 'Revista dos Tribunais'),
(209, 'Pedro Paulo Teixeira Manus'),
(210, 'Celso Barroso Leite'),
(211, 'Marcelo Figueiredo'),
(212, 'Adilson Bassalho Pereira'),
(213, 'Mário  Batalha'),
(214, 'Microsoft'),
(215, 'João Batista de Alburquerque'),
(217, 'David R Hampton'),
(218, 'Donald Weiss'),
(219, 'Regis Fernandes de Oliveira'),
(220, 'Estevão Horvath'),
(221, 'Teresa Cristina Castrucci Tambasco'),
(222, 'Enéas Martins de Barros'),
(224, 'Ronaldo Caldeira Xavier'),
(225, 'Manoel Augusto Vieira Neto'),
(226, 'Samuel Moteiro'),
(227, 'Theotonio Negrão'),
(228, 'Paulo Sandroni'),
(229, 'Antonio Luiz de Toledo Pinto'),
(230, 'Juarez de Oliveira'),
(231, 'Antonio da Silva Cabral'),
(232, 'José Luiz Ferreira Prunes'),
(233, 'Antonio Chaves'),
(234, 'Alice Monteiro de Barros'),
(235, 'Evaristo de Moraes Filho'),
(236, 'Fabio Pessoa de As'),
(237, 'Maria Sylvia Zanella Di Pietro'),
(238, 'Charles Thompson'),
(239, 'Aristeu de Oliveira'),
(240, 'Robert E. Alberti'),
(241, 'Michael L. Emmons'),
(242, 'Iracema A. Valverde'),
(243, 'Angela Clara'),
(244, 'Chris Gane'),
(245, 'Oliveira Aristeu'),
(246, 'Silvio Aparecido Crepaldi'),
(248, 'Arnaldo Sussekind'),
(249, 'Wagner D. Giglio'),
(250, 'José Braz de Oliveira'),
(251, 'Heilio Kohama'),
(252, 'Roberto Bocaccio Piscitelli'),
(253, 'Maria Zulene Farias Timbó'),
(254, 'Sandra Maria Deud Brum'),
(255, 'Maria Berenice Rosa'),
(256, 'Lúcio Rodrigues de Almeida'),
(257, 'Luiz Alberto Ferracini'),
(258, 'Governo do Brasil'),
(260, 'João Bosso Medeiros'),
(261, 'Ministério da Educação'),
(262, 'Jacques Marvitch'),
(263, 'Philip Kotler'),
(264, 'Donald H Haider'),
(265, 'Irving Rein'),
(267, 'Karen F A Fox'),
(268, 'Francisco Russo. Nelson de Oliveira'),
(269, 'Nelson de Oliveira'),
(270, 'Vicente Ambrósio'),
(271, 'Gualdo Amaury Formica'),
(272, 'Gil Nuno Vas'),
(273, 'Wilson de Sousa Campos Batalha'),
(274, 'Sílvia Marina L Batalha de Rodrigues Neto'),
(275, 'Ronando Belmonte'),
(276, 'Maria Rita Miranda Gramigna'),
(277, 'Fernando Rezende'),
(279, 'Carlos Alberto Reis de Paula'),
(280, 'R Reis Freire'),
(281, 'Douglas Gabriel Domingues'),
(282, 'Luciano Coutinho'),
(283, 'José Eduardo Cassiolato'),
(284, 'Ana Lucia G da Silva'),
(285, 'Adriano Campanhole'),
(286, 'Hely Lopes Meirelles'),
(287, 'Odete Meduar'),
(288, 'Juares Freitas'),
(289, 'Sergio Pinto Martins'),
(290, 'Luís Paulo Sirvinskas'),
(291, 'José Raimundo Gomes da Cruz'),
(292, 'Sidney Martins'),
(293, 'Luiz Walter Coelho Filho'),
(294, 'Ciro Pereira da Silva'),
(295, 'Jorge Ulisses Jacoby Fernandes'),
(296, 'Ken O´Donnel'),
(298, 'Maria Tereza Leme Flaury'),
(299, 'Rosa Maria Fischer'),
(300, 'Roberto Ribeiro Bazilli'),
(301, 'Irineu Strenger'),
(302, 'James Giacomoni'),
(303, 'Carlos Valder do Nascimento'),
(305, 'OABSP'),
(306, 'Hilton Lobo Campanhole'),
(307, 'Daniel Burrus'),
(308, 'Ana María Kaufman'),
(309, 'María Helena Rodríguez'),
(310, 'Luiz Tzirulnik'),
(311, 'Napoleão Mendes de Almeida'),
(312, 'Toshio Mukai'),
(313, 'Fernando da Costa Touriho Neto'),
(314, 'Setrag Khoshafian'),
(315, 'Paulo César Pêgas Ferreira'),
(317, 'Celso Antônio Bandeira de Mello'),
(318, 'Amílicar de Araújo Falcão'),
(319, 'Vicente Greco Filho'),
(320, 'José Osório de Azevedo JR'),
(326, 'Lino Martins da Silva'),
(327, 'Antônio Carlos Cintra do Amaral'),
(328, 'Izabel Castanha Gil'),
(330, 'Marcelo Baquero'),
(331, 'Gelson Iezzi'),
(332, 'Osvando Dolce'),
(344, 'Ricardo Augusto Pamplona Vaz'),
(345, 'Adelmo de Almeida Cabral'),
(346, 'Setrag Khoshafian'),
(347, 'Paulo César Pêgas Ferreira'),
(348, 'A Delorenzo Neto'),
(349, 'Celso Antônio Bandeira de Mello'),
(353, 'Vicente Greco Filho'),
(354, 'Valentin Carion'),
(356, 'Osmar de Almeida Santos'),
(357, 'Carlos Eduardo Franco'),
(358, 'Antonio Pagliaro'),
(359, 'Paulo José da Costa Jr'),
(360, 'Bobbi Linkemer'),
(365, 'José Braz de Oliveira'),
(366, 'Marcelo Baquero'),
(369, 'David Degenszajn'),
(370, 'Roberto Périgo'),
(371, 'Org. Adriana Ap de Lima Terçariol e outros');

-- --------------------------------------------------------

--
-- Estrutura da tabela `editoras`
--

DROP TABLE IF EXISTS `editoras`;
CREATE TABLE IF NOT EXISTS `editoras` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nome` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=103 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `editoras`
--

INSERT INTO `editoras` (`id`, `nome`) VALUES
(1, 'AMGH'),
(2, 'Pearson'),
(3, 'Atlas'),
(4, 'Saraiva'),
(5, 'Campus'),
(6, 'Cengage'),
(7, 'Qualitymark'),
(8, 'Manole'),
(9, 'Bookman'),
(10, 'Trilha'),
(11, 'Person'),
(12, 'Brasport'),
(13, 'Disal'),
(14, 'Mc Graw Hill'),
(15, 'Objetiva'),
(16, 'Juruá'),
(17, 'LTC'),
(18, 'Elsevier'),
(19, 'Atual'),
(21, 'Blucher'),
(22, 'Moderna'),
(23, 'Copidart'),
(24, 'Educ'),
(25, 'Estação das Letras e Cores'),
(26, 'Sextante'),
(27, 'Thomson Learning'),
(28, 'FTD'),
(29, 'Cortez'),
(30, 'Edições Loyola'),
(31, 'Senac'),
(32, 'Pontes'),
(33, 'Unicamp'),
(34, 'Ática'),
(35, 'Contexto'),
(36, 'Companhia Letras'),
(37, 'Imperial Novo Milênio'),
(39, 'Pensamento-Cultrix '),
(40, 'FGV'),
(41, 'Nova Fronteira'),
(42, 'Lexikon'),
(43, 'Revista dos Tribunais '),
(44, 'Garamond '),
(45, 'UFMG'),
(46, 'Perspectiva'),
(47, 'Érica'),
(48, 'Tutu'),
(49, 'Digerati'),
(50, 'Padre Anchieta'),
(51, 'LCBS'),
(52, 'Fudação FAT'),
(53, 'Malheiros'),
(54, 'Campanhia Editora Nacioal São Paulo'),
(55, 'Edipro'),
(56, 'LTR'),
(57, 'Forense Universitária'),
(58, 'Interciência'),
(59, 'Cyclades'),
(60, 'Vozes'),
(61, 'Gerai'),
(62, 'ABDR'),
(63, 'Nobel'),
(65, 'Hemus'),
(66, 'Best Seller'),
(67, 'CPS'),
(68, 'Interlivros'),
(69, 'Adcoas'),
(70, 'Ciência de Computação'),
(71, 'Diesse'),
(72, 'Osvaldo Cruz'),
(73, 'Aide'),
(74, 'Julex'),
(75, 'Governo Brasileiro'),
(76, 'Inep'),
(77, 'USP'),
(78, 'FreePres'),
(79, 'Reichmann e Affonso'),
(80, 'MAKRON'),
(81, 'Thex'),
(83, 'Papirus'),
(85, 'JM'),
(86, 'FIEB'),
(87, 'Brasília Jurídica'),
(88, 'Casa da Qualidade'),
(89, 'ADCOAS'),
(90, 'Forense'),
(91, 'LEX-MAGISTER'),
(92, 'Record'),
(93, 'ARTMED'),
(94, 'Wirley'),
(95, 'Texto Novo'),
(96, 'Quark'),
(97, 'Novel'),
(98, 'Privado'),
(99, 'UFRGS'),
(100, 'Artesanatoeducacional'),
(102, 'Esplanada LTDA');

-- --------------------------------------------------------

--
-- Estrutura da tabela `emprestimos`
--

DROP TABLE IF EXISTS `emprestimos`;
CREATE TABLE IF NOT EXISTS `emprestimos` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `idLivro` bigint(20) NOT NULL,
  `idUsuario` bigint(20) NOT NULL,
  `dataEmprestimo` date NOT NULL,
  `dataDevolucao` date DEFAULT NULL,
  `estado` varchar(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fkLivros` (`idLivro`),
  KEY `fkUser` (`idUsuario`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `emprestimos`
--

INSERT INTO `emprestimos` (`id`, `idLivro`, `idUsuario`, `dataEmprestimo`, `dataDevolucao`, `estado`) VALUES
(1, 1, 1, '2022-11-05', '2022-11-16', 'D'),
(2, 125, 1, '2022-11-16', '2022-11-16', 'D'),
(3, 452, 1, '2022-11-01', NULL, 'E'),
(5, 452, 1, '2022-11-02', NULL, 'D'),
(6, 65, 1, '2022-11-19', NULL, 'E'),
(8, 588, 1, '2022-11-26', NULL, 'E');

-- --------------------------------------------------------

--
-- Estrutura da tabela `generos`
--

DROP TABLE IF EXISTS `generos`;
CREATE TABLE IF NOT EXISTS `generos` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nome` varchar(200) NOT NULL,
  `descricao` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `generos`
--

INSERT INTO `generos` (`id`, `nome`, `descricao`) VALUES
(1, 'Administração', 'Descrição'),
(2, 'Direito', 'Direito');

-- --------------------------------------------------------

--
-- Estrutura da tabela `listas`
--

DROP TABLE IF EXISTS `listas`;
CREATE TABLE IF NOT EXISTS `listas` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `login` varchar(200) NOT NULL,
  `idUsuario` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idUsuario` (`idUsuario`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `listas`
--

INSERT INTO `listas` (`id`, `login`, `idUsuario`) VALUES
(1, 'String', 1),
(2, 'Mateus', 2),
(3, 'Guilherme Chuman', 3);

-- --------------------------------------------------------

--
-- Estrutura da tabela `lista_livros`
--

DROP TABLE IF EXISTS `lista_livros`;
CREATE TABLE IF NOT EXISTS `lista_livros` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `idLista` bigint(20) DEFAULT NULL,
  `idLivro` bigint(20) DEFAULT NULL,
  `idStatus` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Lista_Livros_idStatus_id_f8039216_fk_Status_id` (`idStatus`),
  KEY `Lista_Livros_idLista_id_d8a1306d_fk_Listas_id` (`idLista`),
  KEY `Lista_Livros_idLivro_id_c09d8e12_fk_Livros_id` (`idLivro`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `lista_livros`
--

INSERT INTO `lista_livros` (`id`, `idLista`, `idLivro`, `idStatus`) VALUES
(1, 1, 451, 1),
(2, 1, 479, 2),
(3, 1, 439, 1),
(4, 1, 451, 1),
(5, 1, 485, 3),
(6, 1, 1, 3),
(7, 1, 591, 2),
(8, 1, 588, 3);

-- --------------------------------------------------------

--
-- Estrutura da tabela `livros`
--

DROP TABLE IF EXISTS `livros`;
CREATE TABLE IF NOT EXISTS `livros` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `isbn` varchar(20) DEFAULT NULL,
  `titulo` varchar(200) NOT NULL,
  `descricao` longtext,
  `volume` varchar(11) DEFAULT NULL,
  `palavraChave1` varchar(50) DEFAULT NULL,
  `palavraChave2` varchar(50) DEFAULT NULL,
  `palavraChave3` varchar(50) DEFAULT NULL,
  `ano` varchar(20) DEFAULT NULL,
  `edicao` varchar(20) DEFAULT NULL,
  `idEditora` bigint(20) DEFAULT NULL,
  `idGenero` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Livros_idEditora_id_9a6c856f_fk_Editoras_id` (`idEditora`),
  KEY `Livros_idGenero_id_cc8def20_fk_Generos_id` (`idGenero`)
) ENGINE=InnoDB AUTO_INCREMENT=593 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `livros`
--

INSERT INTO `livros` (`id`, `isbn`, `titulo`, `descricao`, `volume`, `palavraChave1`, `palavraChave2`, `palavraChave3`, `ano`, `edicao`, `idEditora`, `idGenero`) VALUES
(1, '978-85-8055-33-1', 'Empreendedorismo', NULL, NULL, NULL, NULL, NULL, '2014', '9ª', 1, 2),
(2, '978-85-7605-569-3', 'Comportamento Organizacional', NULL, NULL, NULL, NULL, NULL, '2014', '14ª', 2, NULL),
(3, '978-85-7605-569-3', 'Comportamento Organizacional', NULL, NULL, NULL, NULL, NULL, '2014', '14ª', 2, NULL),
(4, '978-85-7605-569-3', 'Comportamento Organizacional', NULL, NULL, NULL, NULL, NULL, '2014', '14ª', 2, NULL),
(5, '978-85-7605-569-3', 'Comportamento Organizacional', NULL, NULL, NULL, NULL, NULL, '2014', '14ª', 2, NULL),
(6, '978-85-7605-569-3', 'Comportamento Organizacional', NULL, NULL, NULL, NULL, NULL, '2014', '14ª', 2, NULL),
(7, '978-85-224-7354-0', 'Organização Sistemas e Métodos', NULL, NULL, NULL, NULL, NULL, '2017', '4ª', 3, NULL),
(8, '978-85-224-7354-0', 'Organização Sistemas e Métodos', NULL, NULL, NULL, NULL, NULL, '2017', '4ª', 3, NULL),
(9, '978-85-224-7354-0', 'Organização Sistemas e Métodos', NULL, NULL, NULL, NULL, NULL, '2017', '4ª', 3, NULL),
(10, '978-85-02-19750', 'Fundamentos de Marketing', NULL, NULL, NULL, NULL, NULL, '2013', '3ª', 4, NULL),
(11, '978-85-02-19750', 'Fundamentos de Marketing', NULL, NULL, NULL, NULL, NULL, '2013', '3ª', 4, NULL),
(12, '978-85-02-19750', 'Fundamentos de Marketing', NULL, NULL, NULL, NULL, NULL, '2013', '3ª', 4, NULL),
(13, '978-85-02-19750', 'Fundamentos de Marketing', NULL, NULL, NULL, NULL, NULL, '2013', '3ª', 4, NULL),
(14, '978-85-02-19750', 'Fundamentos de Marketing', NULL, NULL, NULL, NULL, NULL, '2013', '3ª', 4, NULL),
(15, '978-85-224-8914-5', 'Manual de Plano de Negócios', NULL, NULL, NULL, NULL, NULL, '2014', '2ª', 3, NULL),
(16, '978-85-224-8914-5', 'Manual de Plano de Negócios', NULL, NULL, NULL, NULL, NULL, '2014', '2ª', 3, NULL),
(17, '978-85-224-4410-06', 'Merchandising no Ponto de Venda ', NULL, NULL, NULL, NULL, NULL, '2015', '4ª', 3, NULL),
(18, '978-85-224-4410-06', 'Merchandising no Ponto de Venda ', NULL, NULL, NULL, NULL, NULL, '2015', '4ª', 3, NULL),
(19, '978-85-224-4410-06', 'Merchandising no Ponto de Venda ', NULL, NULL, NULL, NULL, NULL, '2015', '4ª', 3, NULL),
(20, '978-85-224-4410-06', 'Merchandising no Ponto de Venda ', NULL, NULL, NULL, NULL, NULL, '2015', '4ª', 3, NULL),
(21, '978-85-224-4410-06', 'Merchandising no Ponto de Venda ', NULL, NULL, NULL, NULL, NULL, '2015', '4ª', 3, NULL),
(22, '978-85-97-01577-5', 'Planejamento Estratégico', NULL, NULL, NULL, NULL, NULL, '2018', '34ª', 3, NULL),
(23, '978-85-97-01577-5', 'Planejamento Estratégico', NULL, NULL, NULL, NULL, NULL, '2018', '34ª', 3, NULL),
(24, '978-85-352-3468-8', 'Construindo Planos de Empreendimentos', NULL, NULL, NULL, NULL, NULL, '2010', '2ª', 5, NULL),
(25, '978-85-352-3468-8', 'Construindo Planos de Empreendimentos', NULL, NULL, NULL, NULL, NULL, '2010', '2ª', 5, NULL),
(26, '978-85-352-3468-8', 'Construindo Planos de Empreendimentos', NULL, NULL, NULL, NULL, NULL, '2010', '2ª', 5, NULL),
(27, '978-85-352-3468-8', 'Construindo Planos de Empreendimentos', NULL, NULL, NULL, NULL, NULL, '2010', '2ª', 5, NULL),
(28, '978-85-352-3468-8', 'Construindo Planos de Empreendimentos', NULL, NULL, NULL, NULL, NULL, '2010', '2ª', 5, NULL),
(29, '978-85-224-8517-8', 'Curso de Administração Financeira', NULL, NULL, NULL, NULL, NULL, '2017', '3ª', 3, NULL),
(30, '978-85-224-8517-8', 'Curso de Administração Financeira', NULL, NULL, NULL, NULL, NULL, '2017', '3ª', 3, NULL),
(31, '978-85-224-8517-8', 'Curso de Administração Financeira', NULL, NULL, NULL, NULL, NULL, '2017', '3ª', 3, NULL),
(32, '978-85-224-8517-8', 'Curso de Administração Financeira', NULL, NULL, NULL, NULL, NULL, '2017', '3ª', 3, NULL),
(33, '978-85-97-00285-0', 'Administração Financeira  e Orçamentária', NULL, NULL, NULL, NULL, NULL, '2017', '12ª', 3, NULL),
(34, '978-85-7605-332-3', 'Principios de Adaministração Financeira', NULL, NULL, NULL, NULL, NULL, '2010', '12ª', 2, NULL),
(35, '978-85-7605-332-3', 'Principios de Adaministração Financeira', NULL, NULL, NULL, NULL, NULL, '2010', '12ª', 2, NULL),
(36, '978-85-7605-332-3', 'Principios de Adaministração Financeira', NULL, NULL, NULL, NULL, NULL, '2010', '12ª', 2, NULL),
(37, '978-85-224-5553-9', 'A Nova Geração de Empreendedores', NULL, NULL, NULL, NULL, NULL, '2009', '1ª', 3, NULL),
(38, '978-85-224-5553-9', 'A Nova Geração de Empreendedores', NULL, NULL, NULL, NULL, NULL, '2009', '1ª', 3, NULL),
(39, '978-85-224-5553-9', 'A Nova Geração de Empreendedores', NULL, NULL, NULL, NULL, NULL, '2009', '1ª', 3, NULL),
(40, '978-85-224-5553-9', 'A Nova Geração de Empreendedores', NULL, NULL, NULL, NULL, NULL, '2009', '1ª', 3, NULL),
(41, '978-85-224-5553-9', 'A Nova Geração de Empreendedores', NULL, NULL, NULL, NULL, NULL, '2009', '1ª', 3, NULL),
(42, '978-85-221-0498-7', 'Gestão Estratégica de Pessoas', NULL, NULL, NULL, NULL, NULL, '2009', '1ª', 6, NULL),
(43, '978-85-221-0498-7', 'Gestão Estratégica de Pessoas', NULL, NULL, NULL, NULL, NULL, '2009', '1ª', 6, NULL),
(44, '978-85-02-05475-2', 'Comportamento Organizacional', NULL, NULL, NULL, NULL, NULL, '2006', '1ª', 4, NULL),
(45, '978-85-02-05475-2', 'Comportamento Organizacional', NULL, NULL, NULL, NULL, NULL, '2006', '1ª', 4, NULL),
(46, '978-85-97-00830-2', 'Gestão da Cadeia Suprimentos', NULL, NULL, NULL, NULL, NULL, '2016', '3', 3, NULL),
(47, '978-85-97-00830-2', 'Gestão da Cadeia Suprimentos', NULL, NULL, NULL, NULL, NULL, '2016', '3', 3, NULL),
(48, '978-85-7303-782-1', 'Gestão por Processos', NULL, NULL, NULL, NULL, NULL, '2008', '2ª', 7, NULL),
(49, '978-85-472-2308-3', 'Gestão por Processos', NULL, NULL, NULL, NULL, NULL, '2018', '5ª', 4, NULL),
(50, '978-85-472-2308-3', 'Gestão por Processos', NULL, NULL, NULL, NULL, NULL, '2018', '5ª', 4, NULL),
(51, '978-85-224-3309-4', 'Gestão de Serviços', NULL, NULL, NULL, NULL, NULL, '2018', '1ª', 3, NULL),
(52, '978-85-224-3309-4', 'Gestão de Serviços', NULL, NULL, NULL, NULL, NULL, '2018', '1ª', 3, NULL),
(53, '978-85-224-3309-4', 'Gestão de Serviços', NULL, NULL, NULL, NULL, NULL, '2018', '1ª', 3, NULL),
(54, '978-85-224-3309-4', 'Gestão de Serviços', NULL, NULL, NULL, NULL, NULL, '2018', '1ª', 3, NULL),
(55, '978-85-224-3309-4', 'Gestão de Serviços', NULL, NULL, NULL, NULL, NULL, '2018', '1ª', 3, NULL),
(56, '978-85-204-3277-8', 'Empreendedorismo', NULL, NULL, NULL, NULL, NULL, '2012', '4ª', 8, NULL),
(57, '978-85-204-3277-8', 'Empreendedorismo', NULL, NULL, NULL, NULL, NULL, '2012', '4ª', 8, NULL),
(58, '978-85-224-7423-3', 'Manual do Empreendedorismo', NULL, NULL, NULL, NULL, NULL, '2017', '2ª', 3, NULL),
(59, '978-85-224-7423-3', 'Manual do Empreendedorismo', NULL, NULL, NULL, NULL, NULL, '2017', '2ª', 3, NULL),
(60, '978085-221-0533-5', 'Empreendedorismo Uma Visão do Processo', NULL, NULL, NULL, NULL, NULL, '2007', '1ª', 6, NULL),
(61, '978085-221-0533-5', 'Empreendedorismo Uma Visão do Processo', NULL, NULL, NULL, NULL, NULL, '2007', '1ª', 6, NULL),
(62, '978085-221-0533-5', 'Empreendedorismo Uma Visão do Processo', NULL, NULL, NULL, NULL, NULL, '2007', '1ª', 6, NULL),
(63, '978085-221-0533-5', 'Empreendedorismo Uma Visão do Processo', NULL, NULL, NULL, NULL, NULL, '2007', '1ª', 6, NULL),
(64, '978085-221-0533-5', 'Empreendedorismo Uma Visão do Processo', NULL, NULL, NULL, NULL, NULL, '2007', '1ª', 6, NULL),
(65, '978-85-7780-611-9', 'Cadeia de Suprimentos Projeto e Gestão', NULL, NULL, NULL, NULL, NULL, '2008', '3ª', 9, NULL),
(66, '978-85-7780-611-9', 'Cadeia de Suprimentos Projeto e Gestão', NULL, NULL, NULL, NULL, NULL, '2008', '3ª', 9, NULL),
(67, '978-85-224-9382-1', 'Gestão Ambiental e Responsabilidade Social Corporativa', NULL, NULL, NULL, NULL, NULL, '2017', '8ª', 3, NULL),
(68, '978-85-224-9382-1', 'Gestão Ambiental e Responsabilidade Social Corporativa', NULL, NULL, NULL, NULL, NULL, '2017', '8ª', 3, NULL),
(69, '978-85-02-1256-0', 'Gestão Estratégica Fácil', NULL, NULL, NULL, NULL, NULL, '2012', '1ª', 4, NULL),
(70, '978-85-02-1256-0', 'Gestão Estratégica Fácil', NULL, NULL, NULL, NULL, NULL, '2012', '1ª', 4, NULL),
(71, '978-85-02-1256-0', 'Gestão Estratégica Fácil', NULL, NULL, NULL, NULL, NULL, '2012', '1ª', 4, NULL),
(72, '978-85-02-1256-0', 'Gestão Estratégica Fácil', NULL, NULL, NULL, NULL, NULL, '2012', '1ª', 4, NULL),
(73, '978-85-02-1256-0', 'Gestão Estratégica Fácil', NULL, NULL, NULL, NULL, NULL, '2012', '1ª', 4, NULL),
(74, '978-85-224-5656-8', 'Gestão Estratégica da Qualidade', NULL, NULL, NULL, NULL, NULL, '2007', '2ª', 3, NULL),
(75, '978-85-224-5656-8', 'Gestão Estratégica da Qualidade', NULL, NULL, NULL, NULL, NULL, '2007', '2ª', 3, NULL),
(76, '978-85-224-5656-8', 'Gestão Estratégica da Qualidade', NULL, NULL, NULL, NULL, NULL, '2007', '2ª', 3, NULL),
(77, '978-85-224-5656-8', 'Gestão Estratégica da Qualidade', NULL, NULL, NULL, NULL, NULL, '2007', '2ª', 3, NULL),
(78, '978-85-224-5656-8', 'Gestão Estratégica da Qualidade', NULL, NULL, NULL, NULL, NULL, '2007', '2ª', 3, NULL),
(79, '978-85-224-90780-3', 'Programa de Direito do Consumidor', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 3, NULL),
(80, '978-85-224-90780-3', 'Programa de Direito do Consumidor', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 3, NULL),
(81, '978-85-224-90780-3', 'Programa de Direito do Consumidor', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 3, NULL),
(82, '978-85-224-90780-3', 'Programa de Direito do Consumidor', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 3, NULL),
(83, '978-85-224-90780-3', 'Programa de Direito do Consumidor', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 3, NULL),
(84, '978-85-365-0053-9', 'Informática Conceitos e Aplicações', NULL, NULL, NULL, NULL, NULL, '2017', '4ª', 4, NULL),
(85, '978-85-365-0053-9', 'Informática Conceitos e Aplicações', NULL, NULL, NULL, NULL, NULL, '2017', '4ª', 4, NULL),
(86, '978-85-365-0053-9', 'Informática Conceitos e Aplicações', NULL, NULL, NULL, NULL, NULL, '2017', '4ª', 4, NULL),
(87, '978-85-365-0053-9', 'Informática Conceitos e Aplicações', NULL, NULL, NULL, NULL, NULL, '2017', '4ª', 4, NULL),
(88, '978-85-221-1862-5', 'Princípios  de Sistemas de Infomação', NULL, NULL, NULL, NULL, NULL, '2016', '11ª', 10, NULL),
(89, '978-85-221-1862-5', 'Princípios  de Sistemas de Infomação', NULL, NULL, NULL, NULL, NULL, '2016', '11ª', 10, NULL),
(90, '978-85-221-1862-5', 'Princípios  de Sistemas de Infomação', NULL, NULL, NULL, NULL, NULL, '2016', '11ª', 10, NULL),
(91, '978-85-221-1862-5', 'Princípios  de Sistemas de Infomação', NULL, NULL, NULL, NULL, NULL, '2016', '11ª', 10, NULL),
(92, '978-85-221-1862-5', 'Princípios  de Sistemas de Infomação', NULL, NULL, NULL, NULL, NULL, '2016', '11ª', 10, NULL),
(93, '978-85-221-1862-5', 'Princípios  de Sistemas de Infomação', NULL, NULL, NULL, NULL, NULL, '2016', '11ª', 10, NULL),
(94, '978-85-352-1574-8', 'Estatística usando Excel', NULL, NULL, NULL, NULL, NULL, '2005', '4ª', 5, NULL),
(95, '978-85-352-1574-8', 'Estatística usando Excel', NULL, NULL, NULL, NULL, NULL, '2005', '4ª', 5, NULL),
(96, '978-85-352-1574-8', 'Estatística usando Excel', NULL, NULL, NULL, NULL, NULL, '2005', '4ª', 5, NULL),
(97, '978-85-352-1574-8', 'Estatística usando Excel', NULL, NULL, NULL, NULL, NULL, '2005', '4ª', 5, NULL),
(98, '978-85-352-1574-8', 'Estatística usando Excel', NULL, NULL, NULL, NULL, NULL, '2005', '4ª', 5, NULL),
(99, '978-85-970-0177-8', 'Matemática Financeira e Suas Aplicações', NULL, NULL, NULL, NULL, NULL, '2016', '13ª', 3, NULL),
(100, '978-85-970-0177-8', 'Matemática Financeira e Suas Aplicações', NULL, NULL, NULL, NULL, NULL, '2016', '13ª', 3, NULL),
(101, '978-85-970-0177-8', 'Matemática Financeira e Suas Aplicações', NULL, NULL, NULL, NULL, NULL, '2016', '13ª', 3, NULL),
(102, '978-85-970-0177-8', 'Matemática Financeira e Suas Aplicações', NULL, NULL, NULL, NULL, NULL, '2016', '13ª', 3, NULL),
(103, '978-85-87918-88-8', 'Introdução à Informática', NULL, NULL, NULL, NULL, NULL, '2004', '8ª', 11, NULL),
(104, '978-85-87918-88-8', 'Introdução à Informática', NULL, NULL, NULL, NULL, NULL, '2004', '8ª', 11, NULL),
(105, '978-85-224-6148-6', 'Excel Aplicação', NULL, NULL, NULL, NULL, NULL, '2008', '2ª', 3, NULL),
(106, '978-85-224-6148-6', 'Excel Aplicação', NULL, NULL, NULL, NULL, NULL, '2008', '2ª', 3, NULL),
(107, '978-85-224-6148-6', 'Excel Aplicação', NULL, NULL, NULL, NULL, NULL, '2008', '2ª', 3, NULL),
(108, '978-85-224-6148-6', 'Excel Aplicação', NULL, NULL, NULL, NULL, NULL, '2008', '2ª', 3, NULL),
(109, '978-85-224-6148-6', 'Excel Aplicação', NULL, NULL, NULL, NULL, NULL, '2008', '2ª', 3, NULL),
(110, '978-85-224-6148-6', 'Excel Aplicação', NULL, NULL, NULL, NULL, NULL, '2008', '2ª', 3, NULL),
(111, '978-85-224-6148-6', 'Excel Aplicação', NULL, NULL, NULL, NULL, NULL, '2008', '2ª', 3, NULL),
(112, '978-85-224-6148-6', 'Excel Aplicação', NULL, NULL, NULL, NULL, NULL, '2008', '2ª', 3, NULL),
(113, '978-85-224-6148-6', 'Excel Aplicação', NULL, NULL, NULL, NULL, NULL, '2008', '2ª', 3, NULL),
(114, '978-85-224-6148-6', 'Excel Aplicação', NULL, NULL, NULL, NULL, NULL, '2008', '2ª', 3, NULL),
(115, '978-85-7452-310-1', 'Acessando Bancos de Dados com Ferramentas RAD', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 12, NULL),
(116, '978-85-7452-310-1', 'Acessando Bancos de Dados com Ferramentas RAD', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 12, NULL),
(117, '978-85-7452-310-1', 'Acessando Bancos de Dados com Ferramentas RAD', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 12, NULL),
(118, '978-85-7452-310-1', 'Acessando Bancos de Dados com Ferramentas RAD', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 12, NULL),
(119, '978-85-7452-310-1', 'Acessando Bancos de Dados com Ferramentas RAD', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 12, NULL),
(120, '978-85-7452-310-1', 'Acessando Bancos de Dados com Ferramentas RAD', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 12, NULL),
(121, '978-85-7452-310-1', 'Acessando Bancos de Dados com Ferramentas RAD', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 12, NULL),
(122, '978-85-7452-310-1', 'Acessando Bancos de Dados com Ferramentas RAD', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 12, NULL),
(123, '978-85-7452-310-1', 'Acessando Bancos de Dados com Ferramentas RAD', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 12, NULL),
(124, '978-85-7452-310-1', 'Acessando Bancos de Dados com Ferramentas RAD', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 12, NULL),
(125, '978-85-7452-310-1', 'Acessando Bancos de Dados com Ferramentas RAD', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 12, NULL),
(126, '978-85-7452-310-1', 'Acessando Bancos de Dados com Ferramentas RAD', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 12, NULL),
(127, '978-85-7452-310-1', 'Acessando Bancos de Dados com Ferramentas RAD', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 12, NULL),
(128, '978-85-7452-310-1', 'Acessando Bancos de Dados com Ferramentas RAD', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 12, NULL),
(129, '978-85-89533-70-6', 'English Pronunciantion for Brazilians', NULL, NULL, NULL, NULL, NULL, '2006', '1ª', 13, NULL),
(130, '978-85-89533-70-6', 'English Pronunciantion for Brazilians', NULL, NULL, NULL, NULL, NULL, '2006', '1ª', 13, NULL),
(131, '978-85-87918-09-3', 'Comércio Eletrônico', NULL, NULL, NULL, NULL, NULL, '2019', '1ª', 11, NULL),
(132, '978-85-430-0585-0', 'Sistemas de Informação Gerentes', NULL, NULL, NULL, NULL, NULL, '2014', '11ª', 11, NULL),
(133, '978-85-430-0585-0', 'Sistemas de Informação Gerentes', NULL, NULL, NULL, NULL, NULL, '2014', '11ª', 11, NULL),
(134, '978-85-430-0585-0', 'Sistemas de Informação Gerentes', NULL, NULL, NULL, NULL, NULL, '2014', '11ª', 11, NULL),
(135, '978-85-430-0585-0', 'Sistemas de Informação Gerentes', NULL, NULL, NULL, NULL, NULL, '2014', '11ª', 11, NULL),
(136, '978-85-430-0585-0', 'Sistemas de Informação Gerentes', NULL, NULL, NULL, NULL, NULL, '2014', '11ª', 11, NULL),
(137, '978-85-430-0585-0', 'Sistemas de Informação Gerentes', NULL, NULL, NULL, NULL, NULL, '2014', '11ª', 11, NULL),
(138, '978-85-02-1252-2', 'Gestão de Marketing Comunicação', NULL, NULL, NULL, NULL, NULL, '2012', '2ª', 4, NULL),
(139, '978-85-7605-699-0', 'Administração Financeira ', NULL, NULL, NULL, NULL, NULL, '2015', '1ª', 11, NULL),
(140, '978-85-7605-699-0', 'Administração Financeira ', NULL, NULL, NULL, NULL, NULL, '2015', '1ª', 11, NULL),
(141, '978-85-7605-699-0', 'Administração Financeira ', NULL, NULL, NULL, NULL, NULL, '2015', '1ª', 11, NULL),
(142, '978-85-7605-699-0', 'Administração Financeira ', NULL, NULL, NULL, NULL, NULL, '2015', '1ª', 11, NULL),
(143, '978-85-7605-699-0', 'Administração Financeira ', NULL, NULL, NULL, NULL, NULL, '2015', '1ª', 11, NULL),
(144, '978-85-97-01623-9', 'Administração de Vendas', NULL, NULL, NULL, NULL, NULL, '2018', '2ª', 3, NULL),
(145, '978-85-97-01623-9', 'Administração de Vendas', NULL, NULL, NULL, NULL, NULL, '2018', '2ª', 3, NULL),
(146, '978-85-224-5617-8', 'Administração de Materiais', NULL, NULL, NULL, NULL, NULL, '2018', '6ª', 3, NULL),
(147, '978-85-224-5617-8', 'Administração de Materiais', NULL, NULL, NULL, NULL, NULL, '2018', '6ª', 3, NULL),
(148, '978-85-224-5617-8', 'Administração de Materiais', NULL, NULL, NULL, NULL, NULL, '2018', '6ª', 3, NULL),
(149, '978-85-224-5617-8', 'Administração de Materiais', NULL, NULL, NULL, NULL, NULL, '2018', '6ª', 3, NULL),
(150, '978-85-224-5617-8', 'Administração de Materiais', NULL, NULL, NULL, NULL, NULL, '2018', '6ª', 3, NULL),
(151, '978085-224-8531-4', 'Administração de Processos', NULL, NULL, NULL, NULL, NULL, '2013', '5ª', 3, NULL),
(152, '978085-224-8531-4', 'Administração de Processos', NULL, NULL, NULL, NULL, NULL, '2013', '5ª', 3, NULL),
(153, '978085-224-8531-4', 'Administração de Processos', NULL, NULL, NULL, NULL, NULL, '2013', '5ª', 3, NULL),
(154, '978085-224-8531-4', 'Administração de Processos', NULL, NULL, NULL, NULL, NULL, '2013', '5ª', 3, NULL),
(155, '978085-224-8531-4', 'Administração de Processos', NULL, NULL, NULL, NULL, NULL, '2013', '5ª', 3, NULL),
(156, '978-85-224-5177-7', 'Matemática Básica para Decisões Administrativas', NULL, NULL, NULL, NULL, NULL, '2017', '2ª', 3, NULL),
(157, '978-85-224-5177-7', 'Matemática Básica para Decisões Administrativas', NULL, NULL, NULL, NULL, NULL, '2017', '2ª', 3, NULL),
(158, '978-85-97-00343-7', 'Economia Brasileira Contemporânea', NULL, NULL, NULL, NULL, NULL, '2017', '8ª', 3, NULL),
(159, '978-85-221-1281-4', 'Estatística Aplicada à administração e economia', NULL, NULL, NULL, NULL, NULL, '2014', '1ª', 6, NULL),
(160, '978-85-221-1281-4', 'Estatística Aplicada à administração e economia', NULL, NULL, NULL, NULL, NULL, '2014', '1ª', 6, NULL),
(161, '978-85-60031-47-4', 'Estatística Aplicada à administração e economia', NULL, NULL, NULL, NULL, NULL, '2007', '4ª', 9, NULL),
(162, '978-85-60031-47-4', 'Estatística Aplicada à administração e economia', NULL, NULL, NULL, NULL, NULL, '2007', '4ª', 9, NULL),
(163, '978-85-60031-47-4', 'Estatística Aplicada à administração e economia', NULL, NULL, NULL, NULL, NULL, '2007', '4ª', 9, NULL),
(164, '978-85-60031-47-4', 'Estatística Aplicada à administração e economia', NULL, NULL, NULL, NULL, NULL, '2007', '4ª', 9, NULL),
(165, '978-85-60031-47-4', 'Estatística Aplicada à administração e economia', NULL, NULL, NULL, NULL, NULL, '2007', '4ª', 9, NULL),
(166, '978-85-86804-80-9', 'Gestão de Recursos Humanos', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 14, NULL),
(167, '978-85-86804-80-9', 'Gestão de Recursos Humanos', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 14, NULL),
(168, '978-85-86804-80-9', 'Gestão de Recursos Humanos', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 14, NULL),
(169, '978-85-86804-80-9', 'Gestão de Recursos Humanos', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 14, NULL),
(170, '978-85-86804-80-9', 'Gestão de Recursos Humanos', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 14, NULL),
(171, '978-85-02-06770-7', 'Gestão do Fator Humano ', NULL, NULL, NULL, NULL, NULL, '2012', '2ª', 4, NULL),
(172, '978-85-02-06770-7', 'Gestão do Fator Humano ', NULL, NULL, NULL, NULL, NULL, '2012', '2ª', 4, NULL),
(173, '978-85-02-06770-7', 'Gestão do Fator Humano ', NULL, NULL, NULL, NULL, NULL, '2012', '2ª', 4, NULL),
(174, '978-85-02-06770-7', 'Gestão do Fator Humano ', NULL, NULL, NULL, NULL, NULL, '2012', '2ª', 4, NULL),
(175, '978-85-02-06770-7', 'Gestão do Fator Humano ', NULL, NULL, NULL, NULL, NULL, '2012', '2ª', 4, NULL),
(176, '85-7302-080-6', 'Inteligência Emocional', NULL, NULL, NULL, NULL, NULL, '1995', '60ª', 15, NULL),
(177, '978-85-02-08023-2', 'Administração de Materiais e Recusos Patrimoniais', NULL, NULL, NULL, NULL, NULL, '2017', '3ª', 4, NULL),
(178, '978-85-02-08023-2', 'Administração de Materiais e Recusos Patrimoniais', NULL, NULL, NULL, NULL, NULL, '2017', '3ª', 4, NULL),
(179, '978-85-02-08023-2', 'Administração de Materiais e Recusos Patrimoniais', NULL, NULL, NULL, NULL, NULL, '2017', '3ª', 4, NULL),
(180, '978-85-02-08023-2', 'Administração de Materiais e Recusos Patrimoniais', NULL, NULL, NULL, NULL, NULL, '2017', '3ª', 4, NULL),
(181, '978-85-02-08023-2', 'Administração de Materiais e Recusos Patrimoniais', NULL, NULL, NULL, NULL, NULL, '2017', '3ª', 4, NULL),
(182, '978-85-8055-431-1', 'Administração Financeira', NULL, NULL, NULL, NULL, NULL, '2015', '10ª', 9, NULL),
(183, '978-85-02-22531-2', 'A Nova Administração', NULL, NULL, NULL, NULL, NULL, '2014', '1ª', 4, NULL),
(184, '978-85-02-22531-2', 'A Nova Administração', NULL, NULL, NULL, NULL, NULL, '2014', '1ª', 4, NULL),
(185, '978-85-224-6288-9', 'Introdução à Administração ', NULL, NULL, NULL, NULL, NULL, '2017', '8ª', 3, NULL),
(186, '978-85-224-6288-9', 'Introdução à Administração ', NULL, NULL, NULL, NULL, NULL, '2017', '8ª', 3, NULL),
(187, '978-85-224-6288-9', 'Introdução à Administração ', NULL, NULL, NULL, NULL, NULL, '2017', '8ª', 3, NULL),
(188, '978-85-224-6288-9', 'Introdução à Administração ', NULL, NULL, NULL, NULL, NULL, '2017', '8ª', 3, NULL),
(189, '978-85-224-6288-9', 'Introdução à Administração ', NULL, NULL, NULL, NULL, NULL, '2017', '8ª', 3, NULL),
(190, '978-85-204-3671-4', 'Administração, teoria, processo e prática', NULL, NULL, NULL, NULL, NULL, '2014', '5ª', 8, NULL),
(191, '978-85-204-3671-4', 'Administração, teoria, processo e prática', NULL, NULL, NULL, NULL, NULL, '2014', '5ª', 8, NULL),
(192, '978-85-204-3671-4', 'Administração, teoria, processo e prática', NULL, NULL, NULL, NULL, NULL, '2014', '5ª', 8, NULL),
(193, '978-85-362-2843-2', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2012', '5ª', 16, NULL),
(194, '978-85-362-2843-2', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2012', '5ª', 16, NULL),
(195, '978-85-362-2843-2', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2012', '5ª', 16, NULL),
(196, '978-85-362-2843-2', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2012', '5ª', 16, NULL),
(197, '978-85-362-2843-2', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2012', '5ª', 16, NULL),
(198, '978-85-362-2843-2', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2012', '5ª', 16, NULL),
(199, '978-85-362-2843-2', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2012', '5ª', 16, NULL),
(200, '978-85-362-2843-2', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2012', '5ª', 16, NULL),
(201, '978-85-362-2843-2', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2012', '5ª', 16, NULL),
(202, '978-85-362-2843-2', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2012', '5ª', 16, NULL),
(203, '978-85-221-1125-1', 'Matemática Aplicada', NULL, NULL, NULL, NULL, NULL, '2012', '2ª', 6, NULL),
(204, '978-85-7605-812-0', 'Administração Estratégica', NULL, NULL, NULL, NULL, NULL, '2014', '3ª', 11, NULL),
(205, '978-85-7605-812-0', 'Administração Estratégica', NULL, NULL, NULL, NULL, NULL, '2014', '3ª', 11, NULL),
(206, '978-85-97-01775-5', 'Cantabilidade Básica', NULL, NULL, NULL, NULL, NULL, '2018', '12ª', 3, NULL),
(207, '978-85-97-01775-5', 'Cantabilidade Básica', NULL, NULL, NULL, NULL, NULL, '2018', '12ª', 3, NULL),
(208, '978-85-97-01775-5', 'Cantabilidade Básica', NULL, NULL, NULL, NULL, NULL, '2018', '12ª', 3, NULL),
(209, '978-85-224-5815-8', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2018', '11ª', 3, NULL),
(210, '978-85-224-5815-8', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2018', '11ª', 3, NULL),
(211, '978-85-224-5815-8', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2018', '11ª', 3, NULL),
(212, '978-85-224-5815-8', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2018', '11ª', 3, NULL),
(213, '978-85-224-5815-8', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2018', '11ª', 3, NULL),
(214, '978-85-224-5815-8', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2018', '11ª', 3, NULL),
(215, '978-85-224-5815-8', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2018', '11ª', 3, NULL),
(216, '978-85-224-5815-8', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2018', '11ª', 3, NULL),
(217, '978-85-224-5815-8', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2018', '11ª', 3, NULL),
(218, '978-85-224-5815-8', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2018', '11ª', 3, NULL),
(219, '978-85-224-5815-8', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2018', '11ª', 3, NULL),
(220, '978-85-224-5815-8', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2018', '11ª', 3, NULL),
(221, '978-85-224-5815-8', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2018', '11ª', 3, NULL),
(222, '978-85-224-5815-8', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2018', '11ª', 3, NULL),
(223, '978-85-224-5815-8', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2018', '11ª', 3, NULL),
(224, '978-85-224-5815-8', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2018', '11ª', 3, NULL),
(225, '978-85-224-5815-8', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2018', '11ª', 3, NULL),
(226, '978-85-224-5815-8', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2018', '11ª', 3, NULL),
(227, '978-85-224-5815-8', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2018', '11ª', 3, NULL),
(228, '978-85-224-5815-8', 'Contabilidade Introdutória', NULL, NULL, NULL, NULL, NULL, '2018', '11ª', 3, NULL),
(229, '978-85-430-0586-7', 'Administração Estratégica e Vantagem Competitiva', NULL, NULL, NULL, NULL, NULL, '2017', '5ª', 2, NULL),
(230, '978-85-430-0586-7', 'Administração Estratégica e Vantagem Competitiva', NULL, NULL, NULL, NULL, NULL, '2017', '5ª', 2, NULL),
(231, '978-85-430-0586-7', 'Administração Estratégica e Vantagem Competitiva', NULL, NULL, NULL, NULL, NULL, '2017', '5ª', 2, NULL),
(232, '978-85-430-0586-7', 'Administração Estratégica e Vantagem Competitiva', NULL, NULL, NULL, NULL, NULL, '2017', '5ª', 2, NULL),
(233, '978-85-430-0586-7', 'Administração Estratégica e Vantagem Competitiva', NULL, NULL, NULL, NULL, NULL, '2017', '5ª', 2, NULL),
(234, '978-85-221-1641-6', 'Administração Estratégica', NULL, NULL, NULL, NULL, NULL, '2015', '10ª', 6, NULL),
(235, '978-85-221-1641-6', 'Administração Estratégica', NULL, NULL, NULL, NULL, NULL, '2015', '10ª', 6, NULL),
(236, '978-85-8143-000-3', 'Administração de Marketing', NULL, NULL, NULL, NULL, NULL, '2012', '14ª', 2, NULL),
(237, '978-85-8143-000-3', 'Administração de Marketing', NULL, NULL, NULL, NULL, NULL, '2012', '14ª', 2, NULL),
(238, '978-85-216-2700-5', 'Macroeconomia ', NULL, NULL, NULL, NULL, NULL, '2018', '8ª', 17, NULL),
(239, '978-85-216-2700-5', 'Macroeconomia ', NULL, NULL, NULL, NULL, NULL, '2018', '8ª', 17, NULL),
(240, '978-85-216-2700-5', 'Macroeconomia ', NULL, NULL, NULL, NULL, NULL, '2018', '8ª', 17, NULL),
(241, '978-85-216-2700-5', 'Macroeconomia ', NULL, NULL, NULL, NULL, NULL, '2018', '8ª', 17, NULL),
(242, '978-85-216-2700-5', 'Macroeconomia ', NULL, NULL, NULL, NULL, NULL, '2018', '8ª', 17, NULL),
(243, '978-85-365-0288-5', 'Microsoft Office Excel 2010 Avançado ', NULL, NULL, NULL, NULL, NULL, '2010', '1ª', 4, NULL),
(244, '978-85-365-0288-5', 'Microsoft Office Excel 2010 Avançado ', NULL, NULL, NULL, NULL, NULL, '2010', '1ª', 4, NULL),
(245, '978-85-352-8813-1', 'Infomática Conceitos Básicos', NULL, NULL, NULL, NULL, NULL, '2017', '10ª', 18, NULL),
(246, '978-85-352-8813-1', 'Infomática Conceitos Básicos', NULL, NULL, NULL, NULL, NULL, '2017', '10ª', 18, NULL),
(247, '978-85-352-8813-1', 'Infomática Conceitos Básicos', NULL, NULL, NULL, NULL, NULL, '2017', '10ª', 18, NULL),
(248, '978-85-352-8813-1', 'Infomática Conceitos Básicos', NULL, NULL, NULL, NULL, NULL, '2017', '10ª', 18, NULL),
(249, '978-85-352-8813-1', 'Infomática Conceitos Básicos', NULL, NULL, NULL, NULL, NULL, '2017', '10ª', 18, NULL),
(250, '978-85-224-6868-3', 'Análise das Demonstrações Contábeis: ConEmpresarialtabilidade ', NULL, NULL, NULL, NULL, NULL, '2017', '7ª', 3, NULL),
(251, '978-85-224-6868-3', 'Análise das Demonstrações Contábeis: ConEmpresarialtabilidade ', NULL, NULL, NULL, NULL, NULL, '2017', '7ª', 3, NULL),
(252, '978-85-224-6868-3', 'Análise das Demonstrações Contábeis: ConEmpresarialtabilidade ', NULL, NULL, NULL, NULL, NULL, '2017', '7ª', 3, NULL),
(253, '978-85-224-6868-3', 'Análise das Demonstrações Contábeis: ConEmpresarialtabilidade ', NULL, NULL, NULL, NULL, NULL, '2017', '7ª', 3, NULL),
(254, '978-85-224-6868-3', 'Análise das Demonstrações Contábeis: ConEmpresarialtabilidade ', NULL, NULL, NULL, NULL, NULL, '2017', '7ª', 3, NULL),
(255, '978-85-7605-359-0', 'Engenharia Econômica ', NULL, NULL, NULL, NULL, NULL, '2009', '1ª', 2, NULL),
(256, '978-85-7605-359-0', 'Engenharia Econômica ', NULL, NULL, NULL, NULL, NULL, '2009', '1ª', 2, NULL),
(257, '978-85-357-1760-0', 'Fundamentos de Matemática Elementar: Matemática comercial, Matemática financeira, Estatística descritiva', NULL, NULL, NULL, NULL, NULL, '2013', '2ª', 19, NULL),
(258, '978-85-357-1760-0', 'Fundamentos de Matemática Elementar: Matemática comercial, Matemática financeira, Estatística descritiva', NULL, NULL, NULL, NULL, NULL, '2013', '2ª', 19, NULL),
(259, '978-85-357-1760-0', 'Fundamentos de Matemática Elementar: Matemática comercial, Matemática financeira, Estatística descritiva', NULL, NULL, NULL, NULL, NULL, '2013', '2ª', 19, NULL),
(260, '978-85-357-1760-0', 'Fundamentos de Matemática Elementar: Matemática comercial, Matemática financeira, Estatística descritiva', NULL, NULL, NULL, NULL, NULL, '2013', '2ª', 19, NULL),
(261, '978-85-02-06768-4', 'Introdução ao Cáculo para Administração, Economia e Contabilidade ', NULL, NULL, NULL, NULL, NULL, '2009', '1ª', 4, NULL),
(262, '978-85-02-06768-4', 'Introdução ao Cáculo para Administração, Economia e Contabilidade ', NULL, NULL, NULL, NULL, NULL, '2009', '1ª', 4, NULL),
(263, '978-85-8143-096-6', 'Pré-Cálculo', NULL, NULL, NULL, NULL, NULL, '2013', '2ª', 2, NULL),
(264, '978-85-8143-096-6', 'Pré-Cálculo', NULL, NULL, NULL, NULL, NULL, '2013', '2ª', 2, NULL),
(265, '978-85-8143-096-6', 'Pré-Cálculo', NULL, NULL, NULL, NULL, NULL, '2013', '2ª', 2, NULL),
(266, '978-85-8143-096-6', 'Pré-Cálculo', NULL, NULL, NULL, NULL, NULL, '2013', '2ª', 2, NULL),
(267, '978-85-8143-096-6', 'Pré-Cálculo', NULL, NULL, NULL, NULL, NULL, '2013', '2ª', 2, NULL),
(268, '978-85-472-2025-9', 'Matemática Finaceira: Objetiva e Aplicada', NULL, NULL, NULL, NULL, NULL, '2017', '10ª', 4, NULL),
(269, '978-85-472-2025-9', 'Matemática Finaceira: Objetiva e Aplicada', NULL, NULL, NULL, NULL, NULL, '2017', '10ª', 4, NULL),
(270, '978-85-01411-2', 'Matemática Financeira e Suas Aplicações', NULL, NULL, NULL, NULL, NULL, '2018', '8ª', 3, NULL),
(271, '978-85-01411-2', 'Matemática Financeira e Suas Aplicações', NULL, NULL, NULL, NULL, NULL, '2018', '8ª', 3, NULL),
(272, '978-85-01411-2', 'Matemática Financeira e Suas Aplicações', NULL, NULL, NULL, NULL, NULL, '2018', '8ª', 3, NULL),
(273, '978-85-01411-2', 'Matemática Financeira e Suas Aplicações', NULL, NULL, NULL, NULL, NULL, '2018', '8ª', 3, NULL),
(274, '978-85-224-5834-9', 'Matemática para cursos de economia, administração, ciências contábeis', NULL, NULL, NULL, NULL, NULL, '2010', '6ª', 3, NULL),
(275, '978-85-224-1584-7', 'Matemática para cursos de economia, administração, ciências contábeis', NULL, NULL, NULL, NULL, NULL, '2017', '4ª', 3, NULL),
(276, '978-85-224-1584-7', 'Matemática para cursos de economia, administração, ciências contábeis', NULL, NULL, NULL, NULL, NULL, '2017', '4ª', 3, NULL),
(277, '978-85-97-01529-4', 'Matemática Básica para Cursos Superiores', NULL, NULL, NULL, NULL, NULL, '2018', '2ª', 3, NULL),
(278, '978-85-97-01529-4', 'Matemática Básica para Cursos Superiores', NULL, NULL, NULL, NULL, NULL, '2018', '2ª', 3, NULL),
(279, '978-85-212-1221-8', 'Matemática com Aplicações Tecnológicas', NULL, NULL, NULL, NULL, NULL, '2018', '1ª', 21, NULL),
(280, '978-85-212-1221-8', 'Matemática com Aplicações Tecnológicas', NULL, NULL, NULL, NULL, NULL, '2018', '1ª', 21, NULL),
(281, '85-16-00406-6', 'Gramática Ilustrada', NULL, NULL, NULL, NULL, NULL, '1990', '4ª', 22, NULL),
(282, NULL, 'Marketing Global', NULL, NULL, NULL, NULL, NULL, '2004', '1ª', 23, NULL),
(283, '978-85-283-0408-4', 'Planejamento de Pesquisa: Uma Introdução', NULL, NULL, NULL, NULL, NULL, '2017', '2ª', 24, NULL),
(284, '978-85-283-0408-4', 'Planejamento de Pesquisa: Uma Introdução', NULL, NULL, NULL, NULL, NULL, '2017', '2ª', 24, NULL),
(285, '978-85-60166-25-1', 'A Marca Pós-Moderna Poder e Fragilidade da Marca na Sociedade Corporativista', NULL, NULL, NULL, NULL, NULL, '2010', '2ª', 25, NULL),
(286, '978-85-60166-25-1', 'A Marca Pós-Moderna Poder e Fragilidade da Marca na Sociedade Corporativista', NULL, NULL, NULL, NULL, NULL, '2010', '2ª', 25, NULL),
(287, '978-85-7542-338-7', 'O Segredo de Luísa: Uma Ideia, uma paixão e um plano de negócios: como nasce o empreendedor e se cria uma empresa', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 26, NULL),
(288, '978-85-7542-338-7', 'O Segredo de Luísa: Uma Ideia, uma paixão e um plano de negócios: como nasce o empreendedor e se cria uma empresa', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 26, NULL),
(289, '978-85-224-4790-9', 'Qualidade Total em Serviços: Conceitos, Exercícios e Casos Práticos', NULL, NULL, NULL, NULL, NULL, '2017', '6ª', 3, NULL),
(290, '978-85-224-4790-9', 'Qualidade Total em Serviços: Conceitos, Exercícios e Casos Práticos', NULL, NULL, NULL, NULL, NULL, '2017', '6ª', 3, NULL),
(291, '978-85-221-0603-5', 'Hiperpublicidade: Atividades e tendências', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 27, NULL),
(292, '978-85-221-0603-5', 'Hiperpublicidade: Atividades e tendências', NULL, NULL, NULL, NULL, NULL, '2008', '1ª', 27, NULL),
(293, '978-85-221-0355-3', 'Hiperpublicidade: Fundamentos e Interfaces', NULL, NULL, NULL, NULL, NULL, '2007', '1ª', 27, NULL),
(294, '978-85-221-0355-3', 'Hiperpublicidade: Fundamentos e Interfaces', NULL, NULL, NULL, NULL, NULL, '2007', '1ª', 27, NULL),
(295, '85-322-1746-X', 'Redação comercial e administrativa: gramática aplicada, moedas, atividades práticas ', NULL, NULL, NULL, NULL, NULL, '1996', '1ª', 28, NULL),
(296, '978-85-970-0675-9', 'Projetos e Relatórios de Pesquisa em Administração', NULL, NULL, NULL, NULL, NULL, '2016', '16ª', 3, NULL),
(297, '978-85-970-0675-9', 'Projetos e Relatórios de Pesquisa em Administração', NULL, NULL, NULL, NULL, NULL, '2016', '16ª', 3, NULL),
(298, '978=85-204-4553-2', 'Planejamento, Recrutamento e Seleção de Pessoal', NULL, NULL, NULL, NULL, NULL, '2015', '8ª', 8, NULL),
(299, '978=85-204-4553-2', 'Planejamento, Recrutamento e Seleção de Pessoal', NULL, NULL, NULL, NULL, NULL, '2015', '8ª', 8, NULL),
(300, '978-85-204-4579-2', 'Treinamento e Desenvolvimento de Recursos Humanos', NULL, NULL, NULL, NULL, NULL, '2016', '8ª', 8, NULL),
(301, '978-85-204-4579-2', 'Treinamento e Desenvolvimento de Recursos Humanos', NULL, NULL, NULL, NULL, NULL, '2016', '8ª', 8, NULL),
(302, '978-85-204-4552-5', 'Administração de Recursos Humanos', NULL, NULL, NULL, NULL, NULL, '2016', '8ª', 8, NULL),
(303, '978-85-204-4552-5', 'Administração de Recursos Humanos', NULL, NULL, NULL, NULL, NULL, '2016', '8ª', 8, NULL),
(304, '978-85-02-13514-7', 'Recursos Humanos Princípios e Tendências', NULL, NULL, NULL, NULL, NULL, '2011', '2ª', 4, NULL),
(305, '978-85-02-13514-7', 'Recursos Humanos Princípios e Tendências', NULL, NULL, NULL, NULL, NULL, '2011', '2ª', 4, NULL),
(306, '978-85-224-7466-0', 'Como Planejar e Executar uma Campanha de Propaganda', NULL, NULL, NULL, NULL, NULL, '2013', '2ª', 3, NULL),
(307, '978-85-224-7466-0', 'Como Planejar e Executar uma Campanha de Propaganda', NULL, NULL, NULL, NULL, NULL, '2013', '2ª', 3, NULL),
(308, '978-85-224-7466-0', 'Como Planejar e Executar uma Campanha de Propaganda', NULL, NULL, NULL, NULL, NULL, '2013', '2ª', 3, NULL),
(309, '978-85-224-7466-0', 'Como Planejar e Executar uma Campanha de Propaganda', NULL, NULL, NULL, NULL, NULL, '2013', '2ª', 3, NULL),
(310, '978-85-224-7466-0', 'Como Planejar e Executar uma Campanha de Propaganda', NULL, NULL, NULL, NULL, NULL, '2013', '2ª', 3, NULL),
(311, '978-85-249-2448-4', 'Metodologia do Trabalho Científico ', NULL, NULL, NULL, NULL, NULL, '2016', '24ª', 29, NULL),
(312, '978-85-249-2448-4', 'Metodologia do Trabalho Científico ', NULL, NULL, NULL, NULL, NULL, '2016', '24ª', 29, NULL),
(313, '978-85-249-2448-4', 'Metodologia do Trabalho Científico ', NULL, NULL, NULL, NULL, NULL, '2016', '24ª', 29, NULL),
(314, '978-85-249-2448-4', 'Metodologia do Trabalho Científico ', NULL, NULL, NULL, NULL, NULL, '2016', '24ª', 29, NULL),
(315, '978-85-249-2448-4', 'Metodologia do Trabalho Científico ', NULL, NULL, NULL, NULL, NULL, '2016', '24ª', 29, NULL),
(316, '978-85-249-2448-4', 'Metodologia do Trabalho Científico ', NULL, NULL, NULL, NULL, NULL, '2016', '24ª', 29, NULL),
(317, '978-85-249-2448-4', 'Metodologia do Trabalho Científico ', NULL, NULL, NULL, NULL, NULL, '2016', '24ª', 29, NULL),
(318, '978-85-249-2448-4', 'Metodologia do Trabalho Científico ', NULL, NULL, NULL, NULL, NULL, '2016', '24ª', 29, NULL),
(319, '978-85-249-2448-4', 'Metodologia do Trabalho Científico ', NULL, NULL, NULL, NULL, NULL, '2016', '24ª', 29, NULL),
(320, '978-85-249-2448-4', 'Metodologia do Trabalho Científico ', NULL, NULL, NULL, NULL, NULL, '2016', '24ª', 29, NULL),
(321, '978-85-249-2448-4', 'Metodologia do Trabalho Científico ', NULL, NULL, NULL, NULL, NULL, '2016', '24ª', 29, NULL),
(322, '978-85-249-2426-2', 'Pesquisa em Ciências Humanas e Sociais ', NULL, NULL, NULL, NULL, NULL, '2017', '12ª', 29, NULL),
(323, '978-85-249-2426-2', 'Pesquisa em Ciências Humanas e Sociais ', NULL, NULL, NULL, NULL, NULL, '2017', '12ª', 29, NULL),
(324, '978-85-249-2426-2', 'Pesquisa em Ciências Humanas e Sociais ', NULL, NULL, NULL, NULL, NULL, '2017', '12ª', 29, NULL),
(325, '978-85-249-2426-2', 'Pesquisa em Ciências Humanas e Sociais ', NULL, NULL, NULL, NULL, NULL, '2017', '12ª', 29, NULL),
(326, '978-85-249-2426-2', 'Pesquisa em Ciências Humanas e Sociais ', NULL, NULL, NULL, NULL, NULL, '2017', '12ª', 29, NULL),
(327, '978-85-249-2426-2', 'Pesquisa em Ciências Humanas e Sociais ', NULL, NULL, NULL, NULL, NULL, '2017', '12ª', 29, NULL),
(328, '978-85-249-2426-2', 'Pesquisa em Ciências Humanas e Sociais ', NULL, NULL, NULL, NULL, NULL, '2017', '12ª', 29, NULL),
(329, '978-85-249-2426-2', 'Pesquisa em Ciências Humanas e Sociais ', NULL, NULL, NULL, NULL, NULL, '2017', '12ª', 29, NULL),
(330, '978-85-249-2426-2', 'Pesquisa em Ciências Humanas e Sociais ', NULL, NULL, NULL, NULL, NULL, '2017', '12ª', 29, NULL),
(331, '978-85-249-2426-2', 'Pesquisa em Ciências Humanas e Sociais ', NULL, NULL, NULL, NULL, NULL, '2017', '12ª', 29, NULL),
(332, '978-85-15-02498-8', 'Metodologia Científica para alunos dos cursos de graduação e pós-graduação', NULL, NULL, NULL, NULL, NULL, '2015', '8ª', 30, NULL),
(333, '978-85-15-02498-8', 'Metodologia Científica para alunos dos cursos de graduação e pós-graduação', NULL, NULL, NULL, NULL, NULL, '2015', '8ª', 30, NULL),
(334, '978-85-396-1054-9', 'Vitrina: Construções de Encenações', NULL, NULL, NULL, NULL, NULL, '2016', '6ª', 31, NULL),
(335, '978-85-396-1054-9', 'Vitrina: Construções de Encenações', NULL, NULL, NULL, NULL, NULL, '2016', '6ª', 31, NULL),
(336, '978-85-396-1054-9', 'Vitrina: Construções de Encenações', NULL, NULL, NULL, NULL, NULL, '2016', '6ª', 31, NULL),
(337, '978-85-396-1054-9', 'Vitrina: Construções de Encenações', NULL, NULL, NULL, NULL, NULL, '2016', '6ª', 31, NULL),
(338, '978-85-396-1054-9', 'Vitrina: Construções de Encenações', NULL, NULL, NULL, NULL, NULL, '2016', '6ª', 31, NULL),
(339, '85-7113-081-7', 'Novas Tendências em Análise do Discurso ', NULL, NULL, NULL, NULL, NULL, '1997', '3ª', 32, NULL),
(340, '85-7113-081-7', 'Novas Tendências em Análise do Discurso ', NULL, NULL, NULL, NULL, NULL, '1997', '3ª', 32, NULL),
(341, '978-85-268-0991-8', 'Introdução à Análise do Discurso', NULL, NULL, NULL, NULL, NULL, '2012', '3ª', 33, NULL),
(342, '978-85-268-0991-8', 'Introdução à Análise do Discurso', NULL, NULL, NULL, NULL, NULL, '2012', '3ª', 33, NULL),
(343, '978-85-268-0991-8', 'Introdução à Análise do Discurso', NULL, NULL, NULL, NULL, NULL, '2012', '3ª', 33, NULL),
(344, '978-85-268-0991-8', 'Introdução à Análise do Discurso', NULL, NULL, NULL, NULL, NULL, '2012', '3ª', 33, NULL),
(345, '978-85-268-0991-8', 'Introdução à Análise do Discurso', NULL, NULL, NULL, NULL, NULL, '2012', '3ª', 33, NULL),
(346, '978-85-08-15336-7', 'Teoria Semiótica do Texto ', NULL, NULL, NULL, NULL, NULL, '2011', '5ª', 34, NULL),
(347, '978-85-08-15336-7', 'Teoria Semiótica do Texto ', NULL, NULL, NULL, NULL, NULL, '2011', '5ª', 34, NULL),
(348, '978-85-08-15336-7', 'Teoria Semiótica do Texto ', NULL, NULL, NULL, NULL, NULL, '2011', '5ª', 34, NULL),
(349, '978-85-08-15336-7', 'Teoria Semiótica do Texto ', NULL, NULL, NULL, NULL, NULL, '2011', '5ª', 34, NULL),
(350, '978-85-08-15336-7', 'Teoria Semiótica do Texto ', NULL, NULL, NULL, NULL, NULL, '2011', '5ª', 34, NULL),
(351, '978-85-85134-46-4', 'A Coesão Textual ', NULL, '1', NULL, NULL, NULL, '2018', '5ª', 35, NULL),
(352, '978-85-85134-46-4', 'A Coesão Textual ', NULL, '2', NULL, NULL, NULL, '2018', '5ª', 35, NULL),
(353, '978-85-85134-46-4', 'A Coesão Textual ', NULL, '3', NULL, NULL, NULL, '2018', '5ª', 35, NULL),
(354, '978-85-85134-46-4', 'A Coesão Textual ', NULL, '4', NULL, NULL, NULL, '2018', '5ª', 35, NULL),
(355, '978-85-359-1093-3', 'A Felicidade Paradoxal Ensaio Sobre a Sociedade de Hiperconsumo ', NULL, NULL, NULL, NULL, NULL, '2007', '1ª', 36, NULL),
(356, '978-85-359-1093-3', 'A Felicidade Paradoxal Ensaio Sobre a Sociedade de Hiperconsumo ', NULL, NULL, NULL, NULL, NULL, '2007', '1ª', 36, NULL),
(357, '978-85-99868-86-7', 'Técnica de Redação', NULL, NULL, NULL, NULL, NULL, '2011', '1ª', 37, NULL),
(358, '978-85-224-5856-1', 'Introdução à metodologia do Trabalho Cientìfico: Elaboração de Trabalhos na Graduação', NULL, NULL, NULL, NULL, NULL, '2018', '10ª', 3, NULL),
(359, '978-85-224-5856-1', 'Introdução à metodologia do Trabalho Cientìfico: Elaboração de Trabalhos na Graduação', NULL, NULL, NULL, NULL, NULL, '2018', '10ª', 3, NULL),
(360, '978-85-224-5856-1', 'Introdução à metodologia do Trabalho Cientìfico: Elaboração de Trabalhos na Graduação', NULL, NULL, NULL, NULL, NULL, '2018', '10ª', 3, NULL),
(361, '978-85-224-5856-1', 'Introdução à metodologia do Trabalho Cientìfico: Elaboração de Trabalhos na Graduação', NULL, NULL, NULL, NULL, NULL, '2018', '10ª', 3, NULL),
(362, '978-85-224-5856-1', 'Introdução à metodologia do Trabalho Cientìfico: Elaboração de Trabalhos na Graduação', NULL, NULL, NULL, NULL, NULL, '2018', '10ª', 3, NULL),
(363, '85-7322-253-0', 'Aspectos Probatórios da Carteira de Trabalho e Previdência Social ', NULL, NULL, NULL, NULL, NULL, '1997', '1ª', 56, NULL),
(364, '85-316-0802-3', 'The Natural Step: A História de Uma Revolução Silenciosa ', NULL, NULL, NULL, NULL, NULL, '2011', '11ª', 39, NULL),
(365, '85-316-0802-3', 'The Natural Step: A História de Uma Revolução Silenciosa ', NULL, NULL, NULL, NULL, NULL, '2011', '11ª', 39, NULL),
(366, '85-316-0802-3', 'The Natural Step: A História de Uma Revolução Silenciosa ', NULL, NULL, NULL, NULL, NULL, '2011', '11ª', 39, NULL),
(367, '85-316-0802-3', 'The Natural Step: A História de Uma Revolução Silenciosa ', NULL, NULL, NULL, NULL, NULL, '2011', '11ª', 39, NULL),
(368, '85-316-0802-3', 'The Natural Step: A História de Uma Revolução Silenciosa ', NULL, NULL, NULL, NULL, NULL, '2011', '11ª', 39, NULL),
(369, '978-85-225-0831-0', 'Comunicação em Prosa Moderna ', NULL, NULL, NULL, NULL, NULL, '2010', '27ª', 40, NULL),
(370, '978-85-225-0831-0', 'Comunicação em Prosa Moderna ', NULL, NULL, NULL, NULL, NULL, '2010', '27ª', 40, NULL),
(371, '978-85-225-0831-0', 'Comunicação em Prosa Moderna ', NULL, NULL, NULL, NULL, NULL, '2010', '27ª', 40, NULL),
(372, '978-85-225-0831-0', 'Comunicação em Prosa Moderna ', NULL, NULL, NULL, NULL, NULL, '2010', '27ª', 40, NULL),
(373, '978-85-225-0831-0', 'Comunicação em Prosa Moderna ', NULL, NULL, NULL, NULL, NULL, '2010', '27ª', 40, NULL),
(374, '978-85-225-0831-0', 'Comunicação em Prosa Moderna ', NULL, NULL, NULL, NULL, NULL, '2010', '27ª', 40, NULL),
(375, '978-85-225-0831-0', 'Comunicação em Prosa Moderna ', NULL, NULL, NULL, NULL, NULL, '2010', '27ª', 40, NULL),
(376, '978-85-7244-285-5', 'A comunicação nos textos ', NULL, NULL, NULL, NULL, NULL, '2018', '2ª', 35, NULL),
(377, '978-85-7244-285-5', 'A comunicação nos textos ', NULL, NULL, NULL, NULL, NULL, '2018', '2ª', 35, NULL),
(378, '978-85-7244-285-5', 'A comunicação nos textos ', NULL, NULL, NULL, NULL, NULL, '2018', '2ª', 35, NULL),
(379, '978-85-7244-285-5', 'A comunicação nos textos ', NULL, NULL, NULL, NULL, NULL, '2018', '2ª', 35, NULL),
(380, '978-85-7244-285-5', 'A comunicação nos textos ', NULL, NULL, NULL, NULL, NULL, '2018', '2ª', 35, NULL),
(381, '978-85-02-04126-4', 'Lições Premilinares de Direito ', NULL, NULL, NULL, NULL, NULL, '2018', '27ª', 4, NULL),
(382, '978-85-02-04126-4', 'Lições Premilinares de Direito ', NULL, NULL, NULL, NULL, NULL, '2018', '27ª', 4, NULL),
(383, '978-85-209-3939-0', 'Moderna Gramática Portuguesa ', NULL, NULL, NULL, NULL, NULL, '2015', '38 ª', 41, NULL),
(384, '978-85-472-2809-5', 'Curso de Direito do Consumidor ', NULL, NULL, NULL, NULL, NULL, '2018', '12ª', 4, NULL),
(385, '978-85-8300-026-6', 'Nova Gramática do Português Contemporâneo ', NULL, NULL, NULL, NULL, NULL, '2017', '7ª', 42, NULL),
(386, '978-85-8300-026-6', 'Nova Gramática do Português Contemporâneo ', NULL, NULL, NULL, NULL, NULL, '2017', '7ª', 42, NULL),
(387, '978-85-8300-026-6', 'Nova Gramática do Português Contemporâneo ', NULL, NULL, NULL, NULL, NULL, '2017', '7ª', 42, NULL),
(388, '978-85-8300-026-6', 'Nova Gramática do Português Contemporâneo ', NULL, NULL, NULL, NULL, NULL, '2017', '7ª', 42, NULL),
(389, '978-85-203-6222-8', 'Comentários ao Códigos de Defesa do Consumidor ', NULL, NULL, NULL, NULL, NULL, '2017', '5ª', 43, NULL),
(390, '978-85-203-6222-8', 'Comentários ao Códigos de Defesa do Consumidor ', NULL, NULL, NULL, NULL, NULL, '2017', '5ª', 43, NULL),
(391, '978-85-16-09395-2', 'Dicionário Santilillana', NULL, NULL, NULL, NULL, NULL, '2014', '4ª', 22, NULL),
(392, '978-85-16-09395-2', 'Dicionário Santilillana', NULL, NULL, NULL, NULL, NULL, '2014', '4ª', 22, NULL),
(393, '85-7617-046-9', 'O Vestígio e a Aura: Corpo e Consumismo na Moral do Espetáculo ', NULL, NULL, NULL, NULL, NULL, '2005', '1ª', 44, NULL),
(394, '85-7617-046-9', 'O Vestígio e a Aura: Corpo e Consumismo na Moral do Espetáculo ', NULL, NULL, NULL, NULL, NULL, '2005', '1ª', 44, NULL),
(395, '85-7617-046-9', 'O Vestígio e a Aura: Corpo e Consumismo na Moral do Espetáculo ', NULL, NULL, NULL, NULL, NULL, '2005', '1ª', 44, NULL),
(396, '85-7617-046-9', 'O Vestígio e a Aura: Corpo e Consumismo na Moral do Espetáculo ', NULL, NULL, NULL, NULL, NULL, '2005', '1ª', 44, NULL),
(397, '85-7617-046-9', 'O Vestígio e a Aura: Corpo e Consumismo na Moral do Espetáculo ', NULL, NULL, NULL, NULL, NULL, '2005', '1ª', 44, NULL),
(398, '978-85-423-0013-0', 'A Ontologia da Realidade ', NULL, NULL, NULL, NULL, NULL, '2014', '2ª', 45, NULL),
(399, '978-85-423-0013-0', 'A Ontologia da Realidade ', NULL, NULL, NULL, NULL, NULL, '2014', '2ª', 45, NULL),
(400, '978-85-273-0079-7', 'Como se Faz uma Tese', NULL, NULL, NULL, NULL, NULL, '2016', '26ª', 46, NULL),
(401, '978-85-273-0079-7', 'Como se Faz uma Tese', NULL, NULL, NULL, NULL, NULL, '2016', '26ª', 46, NULL),
(402, '978-85-423-0027-7', 'Cognição, Ciência e Vida Cotidiana ', NULL, NULL, NULL, NULL, NULL, '2014', '2ª', 45, NULL),
(403, '978-85-423-0027-7', 'Cognição, Ciência e Vida Cotidiana ', NULL, NULL, NULL, NULL, NULL, '2014', '2ª', 45, NULL),
(404, '978-85-423-0027-7', 'Cognição, Ciência e Vida Cotidiana ', NULL, NULL, NULL, NULL, NULL, '2014', '2ª', 45, NULL),
(405, '978-85-423-0027-7', 'Cognição, Ciência e Vida Cotidiana ', NULL, NULL, NULL, NULL, NULL, '2014', '2ª', 45, NULL),
(406, '978-85-423-0027-7', 'Cognição, Ciência e Vida Cotidiana ', NULL, NULL, NULL, NULL, NULL, '2014', '2ª', 45, NULL),
(407, '978-85-249-2448-4', 'Metodologia do Trabalho Científico ', NULL, NULL, NULL, NULL, NULL, '2016', '24ª', 29, NULL),
(408, '978-85-97-01012-1', 'Fundamentos de Metodologia Cientìfica ', NULL, NULL, NULL, NULL, NULL, '2019', '8ª', 3, NULL),
(409, '978-85-97-01012-1', 'Fundamentos de Metodologia Cientìfica ', NULL, NULL, NULL, NULL, NULL, '2019', '8ª', 3, NULL),
(410, '978-85-97-01012-1', 'Fundamentos de Metodologia Cientìfica ', NULL, NULL, NULL, NULL, NULL, '2019', '8ª', 3, NULL),
(411, '978-85-97-01012-1', 'Fundamentos de Metodologia Cientìfica ', NULL, NULL, NULL, NULL, NULL, '2019', '8ª', 3, NULL),
(412, '978-85-97-01012-1', 'Fundamentos de Metodologia Cientìfica ', NULL, NULL, NULL, NULL, NULL, '2019', '8ª', 3, NULL),
(413, '978-85-97-01012-1', 'Fundamentos de Metodologia Cientìfica ', NULL, NULL, NULL, NULL, NULL, '2019', '8ª', 3, NULL),
(414, '978-85-97-01012-1', 'Fundamentos de Metodologia Cientìfica ', NULL, NULL, NULL, NULL, NULL, '2019', '8ª', 3, NULL),
(415, '978-85-97-01012-1', 'Fundamentos de Metodologia Cientìfica ', NULL, NULL, NULL, NULL, NULL, '2019', '8ª', 3, NULL),
(416, '978-85-97-01012-1', 'Fundamentos de Metodologia Cientìfica ', NULL, NULL, NULL, NULL, NULL, '2019', '8ª', 3, NULL),
(417, '978-85-97-01012-1', 'Fundamentos de Metodologia Cientìfica ', NULL, NULL, NULL, NULL, NULL, '2019', '8ª', 3, NULL),
(418, '978-85-97-01012-1', 'Fundamentos de Metodologia Cientìfica ', NULL, NULL, NULL, NULL, NULL, '2019', '8ª', 3, NULL),
(419, '978-85-97-01012-1', 'Fundamentos de Metodologia Cientìfica ', NULL, NULL, NULL, NULL, NULL, '2019', '8ª', 3, NULL);
INSERT INTO `livros` (`id`, `isbn`, `titulo`, `descricao`, `volume`, `palavraChave1`, `palavraChave2`, `palavraChave3`, `ano`, `edicao`, `idEditora`, `idGenero`) VALUES
(420, '978-85-97-01012-1', 'Fundamentos de Metodologia Cientìfica ', NULL, NULL, NULL, NULL, NULL, '2019', '8ª', 3, NULL),
(421, '978-85-97-01012-1', 'Fundamentos de Metodologia Cientìfica ', NULL, NULL, NULL, NULL, NULL, '2019', '8ª', 3, NULL),
(422, '978-85-97-01012-1', 'Fundamentos de Metodologia Cientìfica ', NULL, NULL, NULL, NULL, NULL, '2019', '8ª', 3, NULL),
(423, '978-85-396-0858-4', 'Vitrina: Veículo de Comunicação e Venda ', NULL, NULL, NULL, NULL, NULL, '2018', '2ª', 31, NULL),
(424, '978-85-396-0858-4', 'Vitrina: Veículo de Comunicação e Venda ', NULL, NULL, NULL, NULL, NULL, '2018', '2ª', 31, NULL),
(425, '978-85-396-0858-4', 'Vitrina: Veículo de Comunicação e Venda ', NULL, NULL, NULL, NULL, NULL, '2018', '2ª', 31, NULL),
(426, '978-85-396-0858-4', 'Vitrina: Veículo de Comunicação e Venda ', NULL, NULL, NULL, NULL, NULL, '2018', '2ª', 31, NULL),
(427, '978-85-396-0858-4', 'Vitrina: Veículo de Comunicação e Venda ', NULL, NULL, NULL, NULL, NULL, '2018', '2ª', 31, NULL),
(428, '978-85-472-1808-9', 'Perca o Medo de Escrever da Frase ao Texto ', NULL, NULL, NULL, NULL, NULL, '2017', '2ª', 4, NULL),
(429, '978-85-7307-489-5', 'A Construção do Saber: Manual de Metodologia da Pesquisa em Ciências Humanas ', NULL, NULL, NULL, NULL, NULL, '2007', '1º', 45, NULL),
(430, '978-85-7307-489-5', 'A Construção do Saber: Manual de Metodologia da Pesquisa em Ciências Humanas ', NULL, NULL, NULL, NULL, NULL, '2007', '1º', 45, NULL),
(431, '978-85-7307-489-5', 'A Construção do Saber: Manual de Metodologia da Pesquisa em Ciências Humanas ', NULL, NULL, NULL, NULL, NULL, '2007', '1º', 45, NULL),
(432, '978-85-7307-489-5', 'A Construção do Saber: Manual de Metodologia da Pesquisa em Ciências Humanas ', NULL, NULL, NULL, NULL, NULL, '2007', '1º', 45, NULL),
(433, '978-85-365--796-5', 'Matemática Comercial e Financeira e Fundamentos de Estatística', NULL, NULL, NULL, NULL, NULL, '2014', '1ª', 47, NULL),
(434, '978-85-65274-15-9', 'Um Brasil Bilíngue Português English', NULL, NULL, NULL, NULL, NULL, '2014', '1ª', 48, NULL),
(435, '1678538', 'Microsoft Excel', NULL, NULL, NULL, NULL, NULL, '2003', '2ª', 49, NULL),
(436, NULL, 'Quantidade é Qualidade', NULL, NULL, NULL, NULL, NULL, '2011', '1ª', 50, NULL),
(437, '978-85-65274-08-1', 'O Brasil Paga um Preço Alto pelo privilégio de Alguns Grupos', NULL, NULL, NULL, NULL, NULL, '2017', '3ª', 48, NULL),
(438, '978-85-65274-09-9', 'Um Brasil', NULL, NULL, NULL, NULL, NULL, '2014', '4ª', 51, NULL),
(439, NULL, 'Formação Pedagógica Para Docentes da Educação Profissional', NULL, NULL, NULL, NULL, NULL, '2007', '1ª', 52, NULL),
(440, NULL, 'Formação Pedagógica Para Docentes da Educação Profissional', NULL, NULL, NULL, NULL, NULL, '2007', '1ª', 52, NULL),
(441, '978-85-430-0447-1', 'Princípios de Marketing', NULL, NULL, NULL, NULL, NULL, '2015', '15ª', 2, NULL),
(442, '978-85-430-0447-1', 'Princípios de Marketing', NULL, NULL, NULL, NULL, NULL, '2015', '15ª', 2, NULL),
(443, '978-85-430-0447-1', 'Princípios de Marketing', NULL, NULL, NULL, NULL, NULL, '2015', '15ª', 2, NULL),
(444, '978-85-430-0447-1', 'Princípios de Marketing', NULL, NULL, NULL, NULL, NULL, '2015', '15ª', 2, NULL),
(445, '978-85-430-0447-1', 'Princípios de Marketing', NULL, NULL, NULL, NULL, NULL, '2015', '15ª', 2, NULL),
(446, NULL, 'Discricionariedade Adminstrativa', NULL, NULL, NULL, NULL, NULL, '1997', '1', 53, NULL),
(447, NULL, 'Métodos em Pesquisa Social', NULL, NULL, NULL, NULL, NULL, '1979', '7ª', 54, NULL),
(448, NULL, 'A Justa Causa no Direito do Trabalho', NULL, NULL, NULL, NULL, NULL, '1995', '1ª', 53, NULL),
(449, NULL, 'Justa Causa Na Rescisão Trabalhista', NULL, NULL, NULL, NULL, NULL, '1996', '1ª', 55, NULL),
(450, NULL, 'Dicionário de Direito do Trabalho', NULL, NULL, NULL, NULL, NULL, '1993', '1ª', 56, NULL),
(451, NULL, 'Curso de Direito Administrativo ', NULL, NULL, NULL, NULL, NULL, '1993', '1ª', 57, NULL),
(452, NULL, 'Você e as Telecomunicações', NULL, NULL, NULL, NULL, NULL, '1995', '1ª', 58, NULL),
(453, NULL, 'Guia Internet de Connectividade ', NULL, NULL, NULL, NULL, NULL, '1996', '1ª', 59, NULL),
(454, NULL, 'Direito Adminstrativo Perante os Tribunais', NULL, NULL, NULL, NULL, NULL, '1996', '1ª', 57, NULL),
(455, NULL, 'Contabilidade Pública', NULL, NULL, NULL, NULL, NULL, '1994', '8ª', 3, NULL),
(456, NULL, 'Como Elaborar Projetos de Pesquisa', NULL, NULL, NULL, NULL, NULL, '1987', '1ª', 3, NULL),
(457, NULL, 'Correspondência Técnicas de Comunicação Criativa', NULL, NULL, NULL, NULL, NULL, '1997', '12ª', 3, NULL),
(458, NULL, 'Trablhando com Projetos', NULL, NULL, NULL, NULL, NULL, '2006', '2ª', 60, NULL),
(459, NULL, 'Código Tributário Nacional ', NULL, NULL, NULL, NULL, NULL, '2005', '10ª', 43, NULL),
(460, NULL, 'Despedida Arbitrária ou Sem Justa Causa', NULL, NULL, NULL, NULL, NULL, '1996', '1ª', 53, NULL),
(461, NULL, 'Dicionário Enciclopédico de Previdência Social', NULL, NULL, NULL, NULL, NULL, '1996', '1ª', 56, NULL),
(462, NULL, 'Probidade Administrativa', NULL, NULL, NULL, NULL, NULL, '1997', '2ª', 53, NULL),
(463, '85-7322-214-X', 'Os Precedentes Normativos dos Tribunais do Trabalho', NULL, NULL, NULL, NULL, NULL, '1996', '1ª', 56, NULL),
(464, '85-88805-04-9', 'Recursos Humanos e Agronegócio', NULL, NULL, NULL, NULL, NULL, '2005', '1ª', 61, NULL),
(465, '85-88805-04-9', 'Recursos Humanos e Agronegócio', NULL, NULL, NULL, NULL, NULL, '2005', '1ª', 61, NULL),
(466, '85-7001-748-0', 'Dicionário da Informática', NULL, NULL, NULL, NULL, NULL, '1991', '1ª', 5, NULL),
(467, '85-7001-748-0', 'Dicionário da Informática', NULL, NULL, NULL, NULL, NULL, '1992', '1ª', 5, NULL),
(468, '85-7322-127-5', 'O Empregador e o Empregado Rural', NULL, NULL, NULL, NULL, NULL, '1996', '1ª', 56, NULL),
(469, '85-08-04857-2', 'Manual Escolar de Redação', NULL, NULL, NULL, NULL, NULL, '1994', '1ª', 34, NULL),
(470, '0-07-450194-1', 'Adminstração Contemporânea ', NULL, NULL, NULL, NULL, NULL, '1992', '3ª', 62, NULL),
(471, '85-213-0745-4', 'Técinicas para uma Leitura Rápida e Eficaz', NULL, NULL, NULL, NULL, NULL, '1992', '3ª', 63, NULL),
(472, '85-203-0819-8', 'Manusl de Direito Financeiro ', NULL, NULL, NULL, NULL, NULL, '1993', '1ª', 43, NULL),
(473, NULL, 'Cartas Comerciais e Redação Oficial', NULL, NULL, NULL, NULL, NULL, '1992', '1ª', 3, NULL),
(474, '85-203-2667-6', 'Código Penal', NULL, NULL, NULL, NULL, NULL, '2005', '10ª', 43, NULL),
(475, '85-02-02314-4', 'Comentários à Consolidação das Leis do Trabalho', NULL, NULL, NULL, NULL, NULL, '1997', '22ª', 4, NULL),
(476, NULL, 'Português no Direito', NULL, NULL, NULL, NULL, NULL, '1993', '11ª', 90, NULL),
(477, '85-02-02210-5', 'Código Civil', NULL, NULL, NULL, NULL, NULL, '1997', '48ª', 4, NULL),
(478, '85-02-04142-8', 'Código Civil', NULL, NULL, NULL, NULL, NULL, '2002', '54ª', 4, NULL),
(479, NULL, 'Crimes Fiscais e Abuso de Autoridade', NULL, NULL, NULL, NULL, NULL, '1994', '2ª', 65, NULL),
(480, '85-02-02229-6', 'Código Civil e Legislação Civil em Vigor', NULL, NULL, NULL, NULL, NULL, '2000', '19ª', 4, NULL),
(481, '85-7123-500-7', 'Dicionário de Administração e Finanças', NULL, NULL, NULL, NULL, NULL, '1996', '1ª', 66, NULL),
(482, '85-02-04131-2', 'Código de Processo Civil', NULL, NULL, NULL, NULL, NULL, '2003', '33ª', 4, NULL),
(483, '85-02-04144-4', 'Código Penal', NULL, NULL, NULL, NULL, NULL, '2003', '35ª', 4, NULL),
(484, '85-02-01269-x', 'Processo Administrativo Fiscal', NULL, NULL, NULL, NULL, NULL, '1993', '1ª', 4, NULL),
(485, NULL, 'Direito do Trabalho Rural', NULL, NULL, NULL, NULL, NULL, '1991', '1ª', 56, NULL),
(486, '85-7322-148-8', 'Direitos Autorais na Computação de Dados', NULL, NULL, NULL, NULL, NULL, '1996', '1ª', 56, NULL),
(487, '85-7322-027-9', 'A Mulher e o Direito do Trabalho', NULL, NULL, NULL, NULL, NULL, '1995', '1ª', 56, NULL),
(488, '85-7322-165-8', 'A Justa na Rescisão do Contrato de Trabalho', NULL, NULL, NULL, NULL, NULL, '1996', '3ª', 56, NULL),
(489, '85-7322-165-8', 'A Justa na Rescisão do Contrato de Trabalho', NULL, NULL, NULL, NULL, NULL, '1996', '3ª', 56, NULL),
(490, NULL, 'Processando o Saber', NULL, NULL, NULL, NULL, NULL, '2018', '1ª', 67, NULL),
(491, NULL, 'Processando o Saber', NULL, NULL, NULL, NULL, NULL, '2018', '1ª', 67, NULL),
(492, '85-224-0770-3', 'Direito Administrativo', NULL, NULL, NULL, NULL, NULL, '1992', '3ª', 3, NULL),
(493, '978-85-472-1808-9', 'Perca o Medo de Escrever', NULL, NULL, NULL, NULL, NULL, '2017', '2ª', 4, NULL),
(494, '85-02-01260-6', 'Grande Idéia', NULL, NULL, NULL, NULL, NULL, '1995', '2ª', 4, NULL),
(495, '85-224-0846-7', 'Manual de Prática Trabalhista', NULL, NULL, NULL, NULL, NULL, '1992', '16ª', 3, NULL),
(496, NULL, 'Comportamento Assertivo', NULL, NULL, NULL, NULL, NULL, '1978', '1ª', 68, NULL),
(497, '85-7034-246-2', 'Jornada de Trabalho', NULL, NULL, NULL, NULL, NULL, '2003', '2ª', 69, NULL),
(498, '85-216-0612--5', 'Desenvolvimento Rápido de Sistemas', NULL, NULL, NULL, NULL, NULL, '1998', '1ª', 70, NULL),
(499, '85-224-1212-x', 'Cálculos Trabalhista', NULL, NULL, NULL, NULL, NULL, '1995', '1ª', 3, NULL),
(500, '85-224-1006-2', 'Contabilidade Rural', NULL, NULL, NULL, NULL, NULL, '1993', '1ª', 3, NULL),
(501, '85-224-0887-4', 'Correspondência ', NULL, NULL, NULL, NULL, NULL, '1993', '7ª', 3, NULL),
(502, NULL, 'Trabalho e Reestruturação Produtiva', NULL, NULL, NULL, NULL, NULL, '1994', '1ª', 71, NULL),
(503, '85-7322-005-8', 'Direito do Trabalho e Previdência Social', NULL, NULL, NULL, NULL, NULL, '1995', '1ª', 56, NULL),
(504, NULL, 'Direito do Trabalho e Previdência Social', NULL, NULL, NULL, NULL, NULL, '1992', '1ª', 56, NULL),
(505, NULL, 'Justa Causa Na Rescisão Trabalhista', NULL, NULL, NULL, NULL, NULL, '1992', '3ª', 56, NULL),
(506, '978-85-64933-25-5', 'Eu Sei Que Foi Assim', NULL, NULL, NULL, NULL, NULL, '2019', '1ª', 72, NULL),
(507, '85-224-0662-6', 'Contabilidade Pública', NULL, NULL, NULL, NULL, NULL, '1993', '3ª', 3, NULL),
(508, '85-224-0275-2', 'Contabilidade  Pública', NULL, NULL, NULL, NULL, NULL, '1987', '1ª', 3, NULL),
(509, '85-321-0132-1', 'Recursos Trabalhistas', NULL, NULL, NULL, NULL, NULL, '1996', '1ª', 73, NULL),
(510, NULL, 'Improbidade Adminstrativa ', NULL, NULL, NULL, NULL, NULL, '1997', '1ª', 74, NULL),
(511, NULL, 'Manual de Redação Regulamento', NULL, NULL, NULL, NULL, NULL, '1992', '1ª', 75, NULL),
(512, NULL, 'Manual de Estilo ', NULL, NULL, NULL, NULL, NULL, '1990', '4ª', 41, NULL),
(513, '85-224-0712-6', 'Técnicas de Redação', NULL, NULL, NULL, NULL, NULL, '1991', '4ª', 3, NULL),
(514, '85-296-0023-1', 'Matemática e suas Tecnologias', NULL, NULL, NULL, NULL, NULL, '2002', '1ª', 76, NULL),
(515, '85-314-0224-7', 'Cooperação Inernacional Estratégia e Gestão', NULL, NULL, NULL, NULL, NULL, '1994', '1ª', 77, NULL),
(516, '85-346-0294-8', 'Marketing Público', NULL, NULL, NULL, NULL, NULL, '1994', '1ª', 78, NULL),
(517, '85-224-1116-3', 'Marketing Estratégico para Instituições Educacionais', NULL, NULL, NULL, NULL, NULL, '1994', '1ª', 3, NULL),
(518, '85-224-0940-4', 'Manual Prático de Constituição de Empresas', NULL, NULL, NULL, NULL, NULL, '1992', '2ª', 3, NULL),
(519, '85-87148-06-0', 'Plano de Marketing Passo a Passo ', NULL, NULL, NULL, NULL, NULL, '1999', '1ª', 79, NULL),
(520, '85-7322-457-6', 'Curso de Atividades do Departamento do Pessoal', NULL, NULL, NULL, NULL, NULL, '1998', '3ª', 56, NULL),
(521, '85-221-0025-X', 'Marketing Institucional', NULL, NULL, NULL, NULL, NULL, '1995', '1ª', 62, NULL),
(522, '85-7322-219-0', 'Rescisão Contratual Trabalhista', NULL, NULL, NULL, NULL, NULL, '1997', '1ª', 56, NULL),
(523, '85-7322-178-X', 'Obrigações das Empresas Junto à Previdência Social', NULL, NULL, NULL, NULL, NULL, '1996', '1ª', 56, NULL),
(524, '85-346-0139-9', 'Jogos de Empresa', NULL, NULL, NULL, NULL, NULL, '1994', '1ª', 80, NULL),
(525, NULL, 'Finanças Públicas', NULL, NULL, NULL, NULL, NULL, '1992', '1ª', 3, NULL),
(526, '85-7322-059-7', 'Jornadas de Trabalho na CLT e na Legislação Complementar', NULL, NULL, NULL, NULL, NULL, '1995', '1ª', 56, NULL),
(527, NULL, 'O Aviso Prévio', NULL, NULL, NULL, NULL, NULL, '1988', '1ª', 56, NULL),
(528, '85-95585-07-7', '1000 Perguntas Direito Tributário', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.', '1', 'Direito Tributário', 'Guia de Direito', 'Dúvidas de Direito', '1994', '1ª', 81, 2),
(529, NULL, 'Direito Industrial-Patentes', NULL, NULL, NULL, NULL, NULL, '1980', '1ª', 90, NULL),
(530, NULL, 'Telecomunicações Globalização e Competitividade', NULL, NULL, NULL, NULL, NULL, '1995', '1ª', 83, NULL),
(531, NULL, 'Consolidação das Leis da Previdência Social', NULL, NULL, NULL, NULL, NULL, '1984', '34ª', 3, NULL),
(532, NULL, 'Direito Adminstrativo Brasileiro', NULL, NULL, NULL, NULL, NULL, '1993', '18ª', 53, NULL),
(533, '85-203-2201-8', 'Direito Adminstrativo Moderno', NULL, NULL, NULL, NULL, NULL, '2000', '6ª', 43, NULL),
(534, NULL, 'O Controle Dos Atos Administrativos', NULL, NULL, NULL, NULL, NULL, '1997', '1ª', 53, NULL),
(535, NULL, 'Manual do FGTS', NULL, NULL, NULL, NULL, NULL, '1997', '1ª', 53, NULL),
(536, '85-02-03340-9', 'Manual de Direito Ambiental', NULL, NULL, NULL, NULL, NULL, '2002', '1ª', 4, NULL),
(537, NULL, 'O Controle Jurisdicional do Processo Diciplinar', NULL, NULL, NULL, NULL, NULL, '1996', '1ª', 53, NULL),
(538, NULL, 'Licitaões nos Tribunais', NULL, NULL, NULL, NULL, NULL, '1997', '1ª', 85, NULL),
(539, NULL, 'Jurisprudência Fiscal', NULL, NULL, NULL, NULL, NULL, '1995', '1ª', 86, NULL),
(540, '85-7322-238-7', 'A terceirização Responsavel', NULL, NULL, NULL, NULL, NULL, '1997', '1ª', 56, NULL),
(541, NULL, 'Contratação Direta Sem Licitação', NULL, NULL, NULL, NULL, NULL, '1997', '3ª', 87, NULL),
(542, '85-85651-07-5', 'Raízes da Transformação', NULL, NULL, NULL, NULL, NULL, '1995', '1ª', 88, NULL),
(543, '85-70340-1410-5', 'Execução Fiscal', NULL, NULL, NULL, NULL, NULL, '1999', '1ª', 69, NULL),
(544, '85-224-0255-8', 'Processo e Relações do Trabalho no Brasil', NULL, NULL, NULL, NULL, NULL, '1992', '2ª', 3, NULL),
(545, NULL, 'Contratos Administrativos', NULL, NULL, NULL, NULL, NULL, '1996', '1ª', 53, NULL),
(546, '85-218-0186-0', 'Marcas e Patentes', NULL, NULL, NULL, NULL, NULL, '1996', '1ª', 57, NULL),
(547, '85-224-1750-4', 'Orçamento Publico', NULL, NULL, NULL, NULL, NULL, '1997', '7ª', 3, NULL),
(548, '85-309-0277-7', 'Finanças Públicas', NULL, NULL, NULL, NULL, NULL, '1995', '1ª', 90, NULL),
(549, '85-7034-213-6', 'Responsabilidade Tributária', NULL, NULL, NULL, NULL, NULL, '2002', '1ª', 69, NULL),
(550, '978-85-7721-121-0', 'Contratos Internacionais', NULL, NULL, NULL, NULL, NULL, '2011', '1ª', 91, NULL),
(551, '85-224-1690-7', 'Lesgislação de Previdência Social', NULL, NULL, NULL, NULL, NULL, '1997', '8ª', 3, NULL),
(552, '85-01-04192-0', 'Techno Trends', NULL, NULL, NULL, NULL, NULL, '1994', '1ª', 92, NULL),
(553, '85-224-1699-0', 'Consolidação da Legislação Previdenciária', NULL, NULL, NULL, NULL, NULL, '1997', '6ª', 3, NULL),
(554, '85-7307-093-5', 'Escola Leitura e Produção de Textos', NULL, NULL, NULL, NULL, NULL, '1995', '1ª', 93, NULL),
(555, '85-203-1225-5', 'Direito Falimentar', NULL, NULL, NULL, NULL, NULL, '1994', '3ª', 43, NULL),
(556, '85-02-00309-9', 'Gramática Metódica da Língua Portuguesa', NULL, NULL, NULL, NULL, NULL, '1992', '38ª', 4, NULL),
(557, '85-224-1612-5', 'Estudos e Pareceres de Direito Adminstrativo', NULL, NULL, NULL, NULL, NULL, '1997', '1ª', 3, NULL),
(558, '85-224-1212-X', 'Cálculos Tralhistas ', NULL, NULL, NULL, NULL, NULL, '1994', '1ª', 3, NULL),
(559, '85-224-2912-X', 'Clt Consolidação das Leis do Trabalho e Legislação Complementar ', NULL, NULL, NULL, NULL, NULL, '2001', '105ª', 3, NULL),
(560, '85-224-1726-1', 'Clt Consolidação das Leis do Trabalho e Legislação Complementar ', NULL, NULL, NULL, NULL, NULL, '1997', '99ª', 3, NULL),
(561, '85-224-1271-5', 'Clt Consolidação das Leis do Trabalho e Legislação Complementar ', NULL, NULL, NULL, NULL, NULL, '1995', '94ª', 3, NULL),
(562, '85-02-02369-1', 'A Constituição na Visão dos Tribunais', NULL, NULL, NULL, NULL, NULL, '1997', '1ª', 4, NULL),
(563, '85-02-02368-3', 'A Constituição na Visão dos Tribunais', NULL, NULL, NULL, NULL, NULL, '1997', '2ª', 4, NULL),
(564, '85-85392-09-6', 'A Constituição na Visão dos Tribunais', NULL, NULL, NULL, NULL, NULL, '1997', '3ª', 4, NULL),
(565, '85-7034-145-8', 'Compra e Venda', NULL, NULL, NULL, NULL, NULL, '2000', '1ª', 69, NULL),
(566, NULL, 'Adicionais do Direito do Trabalho', NULL, NULL, NULL, NULL, NULL, '1994', '1ª', 56, NULL),
(567, '85-85588-38-1', 'Banco de Dados Orientado a Objeto', NULL, NULL, NULL, NULL, NULL, '1994', '1ª', 94, NULL),
(568, '85-85360-88-7', 'Técnicas de Armazenagem', NULL, NULL, NULL, NULL, NULL, '1994', '1ª', 7, NULL),
(569, NULL, 'Regulamento do Imposto de Renda', NULL, NULL, NULL, NULL, NULL, '1985', '6ª', 3, NULL),
(570, NULL, 'Sociologia Aplicada à Adminstração', NULL, NULL, NULL, NULL, NULL, '1980', '1ª', 3, NULL),
(571, NULL, 'Curso de Direito Adminstrativo', NULL, NULL, NULL, NULL, NULL, '1993', '4ª', 53, NULL),
(572, NULL, 'Fato Gerador Obrigação Tributária', NULL, NULL, NULL, NULL, NULL, '1977', '4ª', 43, NULL),
(573, '85-02-02218-0', 'Direito Processual Civil Brasileiro ', NULL, NULL, NULL, NULL, NULL, '1997', '1ª', 4, NULL),
(574, '85-02-01927-9', 'Direito Processual Civil Brasileiro ', NULL, NULL, NULL, NULL, NULL, '1997', '12ª', 4, NULL),
(575, '85-02-01994-5', 'Direito Processual Civil Brasileiro ', NULL, NULL, NULL, NULL, NULL, '1996', '1ª', 4, NULL),
(576, '85-02-02364-0', 'Nova Jurisprudência em Direito do Trabalho', NULL, NULL, NULL, NULL, NULL, '1997', '1ª', 4, NULL),
(577, NULL, 'Compromisso de Compra e Venda', NULL, NULL, NULL, NULL, NULL, '1992', '3ª', 53, NULL),
(578, '85-85734-18-3', 'O Pão Nosso', NULL, NULL, NULL, NULL, NULL, '1997', '1ª', 95, NULL),
(579, NULL, 'Dicionário da Internet', NULL, NULL, NULL, NULL, NULL, '1996', '1ª', 96, NULL),
(580, NULL, 'Dos Crismes Contra a Adminstração Pública', NULL, NULL, NULL, NULL, NULL, '1997', '1ª', 53, NULL),
(581, '85-213-0710-1', 'Cuide de Sua Imagem Profissional', NULL, NULL, NULL, NULL, NULL, '1991', '1ª', 63, NULL),
(582, '85-224-03750-9', 'Contabilidade Governamental', NULL, NULL, NULL, NULL, NULL, '1988', '1ª', 3, NULL),
(583, '85-213-0725-x', 'Como Escrever com Facilidade', NULL, NULL, NULL, NULL, NULL, '1993', '3ª', 97, NULL),
(584, NULL, 'Concessão de Serviço Público', NULL, NULL, NULL, NULL, NULL, '1996', '1ª', 53, NULL),
(585, '978-85-64933-47-7', 'Antologia', NULL, NULL, NULL, NULL, NULL, '2019', '1ª', 98, NULL),
(586, '978-85-386-0059-6', 'Pesquisa Quantitativa nas Ciências Sociais', NULL, NULL, NULL, NULL, NULL, '2009', '1ª', 99, NULL),
(587, '978-85-386-0059-6', 'Pesquisa Quantitativa nas Ciências Sociais', NULL, NULL, NULL, NULL, NULL, '2009', '1ª', 99, NULL),
(588, '978-85-357-2006-9', 'Matemática', NULL, NULL, NULL, NULL, NULL, '2008', '6ª', 19, NULL),
(589, '978-85-357-2006-9', 'Matemática', NULL, NULL, NULL, NULL, NULL, '2008', '6ª', 19, NULL),
(590, '978-85-357-2006-9', 'Matemática', NULL, NULL, NULL, NULL, NULL, '2008', '6ª', 19, NULL),
(591, '978-85-357-2006-9', 'Matemática', NULL, NULL, NULL, NULL, NULL, '2008', '6ª', 19, NULL),
(592, '978-85-357-2006-9', 'Matemática', NULL, NULL, NULL, NULL, NULL, '2008', '6ª', 19, NULL);

-- --------------------------------------------------------

--
-- Estrutura da tabela `logs`
--

DROP TABLE IF EXISTS `logs`;
CREATE TABLE IF NOT EXISTS `logs` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `data` date NOT NULL,
  `idTipoLog` bigint(20) DEFAULT NULL,
  `idUsuario` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Logs_idTipoLog_id_250c851e_fk_TipoLog_id` (`idTipoLog`),
  KEY `Logs_idUsuario_id_fa2ec9df_fk_Usuarios_id` (`idUsuario`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `status`
--

DROP TABLE IF EXISTS `status`;
CREATE TABLE IF NOT EXISTS `status` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nome` varchar(200) NOT NULL,
  `cor` char(7) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `status`
--

INSERT INTO `status` (`id`, `nome`, `cor`) VALUES
(1, 'Lido', '#3d79e7'),
(2, 'Lendo', '#3de768'),
(3, 'À Ler', '#e8f34b');

-- --------------------------------------------------------

--
-- Estrutura stand-in para vista `tbgenero`
-- (Veja abaixo para a view atual)
--
DROP VIEW IF EXISTS `tbgenero`;
CREATE TABLE IF NOT EXISTS `tbgenero` (
`genero` varchar(200)
,`titulo` varchar(200)
);

-- --------------------------------------------------------

--
-- Estrutura da tabela `tipolog`
--

DROP TABLE IF EXISTS `tipolog`;
CREATE TABLE IF NOT EXISTS `tipolog` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nome` varchar(200) NOT NULL,
  `descricao` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `trabalhos`
--

DROP TABLE IF EXISTS `trabalhos`;
CREATE TABLE IF NOT EXISTS `trabalhos` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `idAutor` bigint(20) DEFAULT NULL,
  `idLivro` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Trabalhos_idAutor_id_c4b49b73_fk_Autores_id` (`idAutor`),
  KEY `Trabalhos_idLivro_id_44ae9a97_fk_Livros_id` (`idLivro`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `trabalhos`
--

INSERT INTO `trabalhos` (`id`, `idAutor`, `idLivro`) VALUES
(6, 280, 528);

-- --------------------------------------------------------

--
-- Estrutura da tabela `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `login` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `nome` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `validationToken` varchar(200) NOT NULL,
  `status` varchar(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `usuarios`
--

INSERT INTO `usuarios` (`id`, `login`, `password`, `nome`, `email`, `validationToken`, `status`) VALUES
(1, 'string', 'string', 'string', 'string', 'string', 'A'),
(2, 'normal', 'normal', 'Mateus', 'normal@normal', 'aaaaaaa', 'C'),
(3, 'guichuman', 'senha123', 'Guilherme Chuman', 'guilherme.troncon@fatec.sp.gov.br', 'VtdytIGytByPGdE', 'T');

-- --------------------------------------------------------

--
-- Estrutura para vista `tbgenero`
--
DROP TABLE IF EXISTS `tbgenero`;

DROP VIEW IF EXISTS `tbgenero`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `tbgenero`  AS   (select coalesce(`generos`.`nome`,'NULL') AS `genero`,`livros`.`titulo` AS `titulo` from (`livros` left join `generos` on((`livros`.`idGenero` = `generos`.`id`))))  ;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `emprestimos`
--
ALTER TABLE `emprestimos`
  ADD CONSTRAINT `fkLivros` FOREIGN KEY (`idLivro`) REFERENCES `livros` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fkUser` FOREIGN KEY (`idUsuario`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limitadores para a tabela `listas`
--
ALTER TABLE `listas`
  ADD CONSTRAINT `Listas_idUsuario_id_d7d28df7_fk_Usuarios_id` FOREIGN KEY (`idUsuario`) REFERENCES `usuarios` (`id`);

--
-- Limitadores para a tabela `lista_livros`
--
ALTER TABLE `lista_livros`
  ADD CONSTRAINT `Lista_Livros_idLista_id_d8a1306d_fk_Listas_id` FOREIGN KEY (`idLista`) REFERENCES `listas` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Lista_Livros_idLivro_id_c09d8e12_fk_Livros_id` FOREIGN KEY (`idLivro`) REFERENCES `livros` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Lista_Livros_idStatus_id_f8039216_fk_Status_id` FOREIGN KEY (`idStatus`) REFERENCES `status` (`id`);

--
-- Limitadores para a tabela `livros`
--
ALTER TABLE `livros`
  ADD CONSTRAINT `Livros_idEditora_id_9a6c856f_fk_Editoras_id` FOREIGN KEY (`idEditora`) REFERENCES `editoras` (`id`),
  ADD CONSTRAINT `Livros_idGenero_id_cc8def20_fk_Generos_id` FOREIGN KEY (`idGenero`) REFERENCES `generos` (`id`);

--
-- Limitadores para a tabela `logs`
--
ALTER TABLE `logs`
  ADD CONSTRAINT `Logs_idTipoLog_id_250c851e_fk_TipoLog_id` FOREIGN KEY (`idTipoLog`) REFERENCES `tipolog` (`id`),
  ADD CONSTRAINT `Logs_idUsuario_id_fa2ec9df_fk_Usuarios_id` FOREIGN KEY (`idUsuario`) REFERENCES `usuarios` (`id`);

--
-- Limitadores para a tabela `trabalhos`
--
ALTER TABLE `trabalhos`
  ADD CONSTRAINT `Trabalhos_idAutor_id_c4b49b73_fk_Autores_id` FOREIGN KEY (`idAutor`) REFERENCES `autores` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Trabalhos_idLivro_id_44ae9a97_fk_Livros_id` FOREIGN KEY (`idLivro`) REFERENCES `livros` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
