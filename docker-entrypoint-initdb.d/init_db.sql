Terminal close -- exit!
(id, username, email, password_hash, is_admin) VALUES (2, 'root', 'root@root.com', '$2b$12$ZdJO3rAzVbsN.wvgFlqfxu2DVZXHbB/LG8SvMHZ1/VXwnt0MdQkx6', 1);
INSERT INTO market.item (id, title, price, weight, color, image) VALUES (1, '#122 Ultramarine', 9, 100, 'Blue', 'static/images/122_UltramarineBlue_a2x.webp');
INSERT INTO market.item (id, title, price, weight, color, image) VALUES (2, '#110 Organic Pyrrole', 15, 100, 'Orange', 'static/images/110_OrganicOrange_a2x.webp');
INSERT INTO market.item (id, title, price, weight, color, image) VALUES (3, '#100 Burnt sienna', 12, 100, 'Oxide Green', 'static/images/104_ChromiumOxideGreen_a2x.webp');
INSERT INTO market.item (id, title, price, weight, color, image) VALUES (4, '#116 Phthalo ', 12, 100, 'Green', 'static/images/116_PhthaloGreen_a2x.webp');
INSERT INTO market.item (id, title, price, weight, color, image) VALUES (5, '#120 Lightfastness', 15, 100, 'Yellow Green', 'static/images/120_YellowGreen_a_59511d56-9740-47da-ab6b-4ddf934b3adf2x.webp');
INSERT INTO market.item (id, title, price, weight, color, image) VALUES (6, '#125 Lightblue', 15, 100, 'Blue', 'static/images/135_PhthaloTurquoise_a2x.webp');

INSERT INTO market.`order` (id, first_name, last_name, country, city, address, status, total_quantity) VALUES (3, 'Evgenidzze', 'Smetaniuk', 'Ukraine', 'Vinnytsia', 'Volodymyra Ilyka 77', 'CANCELED', 3);

INSERT INTO market.order_items (id, order_id, product_id, quantity) VALUES (5, 3, 3, 1);
INSERT INTO market.order_items (id, order_id, product_id, quantity) VALUES (6, 3, 1, 1);
INSERT INTO market.order_items (id, order_id, product_id, quantity) VALUES (7, 3, 4, 1);
INSERT INTO market.order_items (id, order_id, product_id, quantity) VALUES (8, 3, 3, 2);


INSERT INTO market.country (id, name) VALUES (1, 'Ukraine');
INSERT INTO market.order_items (id, name, country_id) VALUES (1, 'Kyiv', 1);