CREATE DATABASE zarty;
USE zarty;

CREATE TABLE `zarty_lista` (
  `zart_id` bigint NOT NULL,
  `tekst` varchar(500) DEFAULT NULL,
  `autor` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`zart_id`),
  UNIQUE KEY `zart_id` (`zart_id`)
);

INSERT INTO zarty.zarty_lista (zart_id, tekst, autor)
VALUES (1,"Z czego pije informatyk? Z e-kranu!",'Bartek'),
(2,"Na Podhalu do sklepu wpada zlodziej.▒Dawaj kase!▒Jakom? Jeczmienna? czy gryczana?", "Kasia"),
(3,"▒Czesc jez?▒,co jesz? ▒Czesc zajac, co zajac?", "Jakub"),
(4,"Co fryzjer ma w lodowce? Ma-szynke!", "Elon"),
(5,"Jaki jeat najwiekszy las Na swiecie ? - Jasiu odpowiada Las Vegas", "Jasiu")

