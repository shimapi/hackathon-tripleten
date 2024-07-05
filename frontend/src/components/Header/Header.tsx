import React from "react";
import "./Header.scss";
import { Link } from "react-router-dom";

const Header: React.FC = () => {
	return (
		<section className="header">
			<h1>Análisis estadístico en segmentación de clientes</h1>
			<nav className="menubar">
				<Link className="menubar__link" to="/">
					Home
				</Link>
				<Link className="menubar__link" to="/upload-json">
					Subir JSON
				</Link>
				<Link className="menubar__link" to="/upload-csv">
					Subir CSV
				</Link>
				<Link className="menubar__link" to="/graph">
					Ver Gráfico
				</Link>
			</nav>
		</section>
	);
};

export default Header;
