import React from "react";
import "./Header.scss";
import { Link } from "react-router-dom";

const Header: React.FC = () => {
	return (
		<nav className="menubar">
			<Link className="menubar__link" to="/">
				Home
			</Link>
			<Link className="menubar__link" to="/upload">
				Subir JSON
			</Link>
			<Link className="menubar__link" to="/graph">
				Ver Gráfico
			</Link>
		</nav>
	);
};

export default Header;
